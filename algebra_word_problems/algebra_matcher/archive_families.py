"""Solver families made from the word archive: one family for every wording the archive proved.

word_archive.py plays every reference problem and calls a wording PROVEN when the stored equation, with each number given a role, solves to the stored answer
for every problem of that wording (and there are at least two).  make_archive_families.py takes each proven wording and writes archive_families.json: the wording
as a pattern, the equation with every number's role (N[i] = the i-th number of the problem, or a fixed number), and how each number of the answer is built from
the solution.  It writes a wording only when EVERY stored problem of it comes back with exactly its stored answer.

This file is the reader.  A family answers ONLY when
  1. the problem is the wording (the whole text matches the pattern),
  2. every number written in the problem was taken by the pattern and every one of them is used in the equation (n_numbers matches),
  3. the equation has exactly one solution that passes the checks the stored answers of that wording all pass (positive, whole ...).
Anything else returns None (a decline).  A wrong role must never become a wrong answer.

    solve("Service A has a $160 sign-up fee and costs $5/month. Service B has no fee and costs $15/month. After how many months is the total cost the same?")
    -> Result(family='archive_break_even_1', values=[Fraction(16, 1)], ...)

The equation is read by a small evaluator of its own (numbers, + - * /, parentheses, N[i], the unknown): nothing is passed to eval().
Standard library only.
"""
import ast
import json
import os
import re
from collections import namedtuple
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
TABLE = os.path.join(HERE, "archive_families.json")
Result = namedtuple("Result", "family values equation reading")
NUM = r"(\d+(?:\.\d+)?)"


def _clean(problem):
    """The same cleaning word_solver.clean does: lower case, $ kept, thousands commas and 'percent' written the short way."""
    t = problem.strip().replace("’", "'").replace("−", "-")
    t = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", t)
    t = re.sub(r"\bper\s?cent\b|\bpercent\b", "%", t, flags=re.I)
    return t.lower()


def _digit_numbers(problem):
    return re.findall(r"\d+(?:\.\d+)?", _clean(problem))


def evaluate(expr, numbers, unknown=None):
    """Value of a table expression: numbers, F('c'), N[i], X, + - * / and parentheses.  Raises ValueError for anything else."""
    tree = ast.parse(expr.strip(), mode="eval")

    def go(node):
        if isinstance(node, ast.Expression):
            return go(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return Fraction(str(node.value))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            v = go(node.operand)
            return -v if isinstance(node.op, ast.USub) else v
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            a, b = go(node.left), go(node.right)
            if isinstance(node.op, ast.Add):
                return a + b
            if isinstance(node.op, ast.Sub):
                return a - b
            if isinstance(node.op, ast.Mult):
                return a * b
            return a / b
        if isinstance(node, ast.Name) and node.id == "X" and unknown is not None:
            return unknown
        if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) and node.value.id == "N" and isinstance(node.slice, ast.Constant):
            return numbers[node.slice.value]
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "F" and len(node.args) == 1
                and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str)):
            return Fraction(node.args[0].value)
        raise ValueError("not an allowed expression: %r" % expr)

    return go(tree)


def roots(left, right, numbers):
    """Every solution of left = right in the unknown X that the exact check accepts (Newton from several starts, then written as a fraction and verified exactly)."""
    def g(x):
        return evaluate(left, numbers, x) - evaluate(right, numbers, x)

    found = set()
    for start in (0.0, 1.0, 2.0, 0.5, 10.0, 0.25, 5.0, 20.0, 50.0, 100.0, 1000.0, -2.0, -10.0):
        x = float(start)
        converged = False
        for _ in range(80):
            try:
                y = float(g(x))
                y2 = float(g(x + 1e-6))
            except (ZeroDivisionError, ValueError, OverflowError):
                break
            slope = (y2 - y) / 1e-6
            if abs(slope) < 1e-14:
                break
            nxt = x - y / slope
            if abs(nxt - x) < 1e-10:
                x, converged = nxt, True
                break
            x = nxt
        if not converged:
            continue
        candidate = Fraction(x).limit_denominator(10 ** 6)
        try:
            if g(candidate) == 0:
                found.add(candidate)
        except ZeroDivisionError:
            pass
    return sorted(found)


def show(v):
    v = Fraction(v)
    if v.denominator == 1:
        return str(v.numerator)
    s = ("%.4f" % float(v)).rstrip("0").rstrip(".")
    return s


def _passes(value, flags):
    if flags.get("positive") and value <= 0:
        return False
    if flags.get("whole") and value.denominator != 1:
        return False
    return True


def make_family(entry):
    pattern = re.compile(entry["pattern"])

    def family(problem):
        t = _clean(problem).strip()
        m = pattern.match(t)
        if not m:
            return None
        numbers = [Fraction(g) for g in m.groups()]
        if len(numbers) != entry["n"] or len(_digit_numbers(problem)) != entry["n"]:      # a number the wording does not own: decline
            return None
        good = []
        for x in roots(entry["left"], entry["right"], numbers):
            try:
                values = [evaluate(v["expr"], numbers, x) for v in entry["values"]]
            except ZeroDivisionError:
                continue
            if all(_passes(v, f) for v, f in zip(values, [v["flags"] for v in entry["values"]])) and _passes(x, entry["unknown_flags"]):
                good.append((x, values))
        if len(good) != 1:
            return None
        x, values = good[0]
        eq = entry["equation"]
        for i, n in enumerate(numbers):
            eq = eq.replace("{%d}" % i, show(n))
        return Result(entry["id"], values, eq, "%s, so %s = %s" % (eq, entry["var"], show(x)))

    family.__name__ = entry["id"]
    return family


def families():
    """One family function for every wording in archive_families.json (none when the file is missing)."""
    if not os.path.isfile(TABLE):
        return []
    with open(TABLE, encoding="utf-8") as handle:
        return [make_family(e) for e in json.load(handle)["families"]]
