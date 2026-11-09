"""Shared by every problem file: solve a problem with the numbers that are in the boxes.

A problem file keeps its text as a TEMPLATE ("A venue charges ${0} plus ${1} per guest. The total was ${2}. ...") and its numbers as written.  compute(*numbers) puts the numbers
into the template and asks the solver that answers the problem:

    "word_solver"    algebra_word_problems/algebra_matcher/word_solver.py   (55 families, standard library only)
    "number_puzzle"  algebra_word_problems/algebra_matcher/number_puzzle.py (the number-puzzle reader)

A solver only answers when it is sure (every number has a role, the answer passes its sanity checks), so numbers that do not fit the problem (a count that would not be whole,
a negative time ...) raise ValueError instead of giving a wrong answer.
"""
import os
import sys
from fractions import Fraction

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_MATCHER = os.path.join(_ROOT, "algebra_word_problems", "algebra_matcher")


def _solvers():
    if _MATCHER not in sys.path:
        sys.path.insert(0, _MATCHER)
    import number_puzzle
    import word_solver
    return word_solver, number_puzzle


def _text(value):
    """A number as it is written in a problem: 12 -> '12', 2.5 -> '2.5', Fraction(5, 2) -> '2.5', '0.15' stays '0.15'."""
    if isinstance(value, str):
        return value.strip()
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    return repr(float(value))


def _number(value):
    """An answer as a calculator number: whole values come back as int, the rest as float."""
    value = Fraction(value)
    return value.numerator if value.denominator == 1 else float(value)


def solve_numbers(template, solver, numbers):
    """Fill `template` with `numbers` and solve it.  Returns a number, or a list of numbers when the problem has several answers."""
    if solver is None:
        raise NotImplementedError("No solver answers this algebra word problem yet (reference only).")
    count = template.count("{") - 2 * template.count("{{")
    if len(numbers) != count:
        raise ValueError("This problem needs %d numbers, got %d." % (count, len(numbers)))
    text = template.format(*[_text(n) for n in numbers])
    word_solver, number_puzzle = _solvers()
    if solver == "word_solver":
        result = word_solver.solve(text)
        values = None if result is None else list(result.values)
    else:
        result = number_puzzle.solve(text)
        values = None if result is None else [result.answer]
    if not values:
        raise ValueError("The solver cannot answer this problem with these numbers: %s" % text)
    out = [_number(v) for v in values]
    return out[0] if len(out) == 1 else out
