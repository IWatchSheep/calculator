"""Tests for archive_families.py (the families made from the word archive).   Run:  python -m unittest test_archive_families

1. Every family returns the stored answer for every stored problem of its wording, and only the proven wordings became families.
2. A number the wording does not own, a missing number, or other words: the family declines.
3. New numbers in the same wording: the family agrees with word_archive.solve_equation on the equation with those numbers (an independent solver).
4. The table reader refuses anything that is not plain arithmetic.
"""
import json
import os
import re
import unittest
from fractions import Fraction

import archive_families as AF
import word_archive as WA
import word_solver as WS

TABLE = json.load(open(AF.TABLE, encoding="utf-8"))["families"]
ARCHIVE = json.load(open(WA.ARCHIVE, encoding="utf-8"))
PROBLEMS = {p.ID: p for p in WA.load_problems()}


def answer_numbers(text):
    text = re.sub(r"\([^)]*\)", "", text)
    text = re.sub(r"(?<=\d),(?=\d{3})", "", text)
    return sorted(Fraction(x) for x in re.findall(r"-?\d+(?:\.\d+)?(?:/\d+)?", text))


def fill(template, numbers):
    return re.sub(r"\{(\d+)\}", lambda m: numbers[int(m.group(1))], template)


class Table(unittest.TestCase):
    def test_there_are_families_and_each_is_a_proven_wording(self):
        self.assertGreater(len(TABLE), 40)
        for e in TABLE:
            row = ARCHIVE["templates"][e["wording"]]
            self.assertTrue(row["proven"], e["id"])
            self.assertGreaterEqual(row["tried"], 2, e["id"])

    def test_every_family_returns_every_stored_answer_of_its_wording(self):
        covered = 0
        for e in TABLE:
            fam = AF.make_family(e)
            for pid in e["problems"]:
                p = PROBLEMS[pid]
                r = fam(p.PROBLEM)
                self.assertIsNotNone(r, "%s declines %s" % (e["id"], pid))
                got, want = sorted(r.values), answer_numbers(p.ANSWER)
                self.assertEqual(len(got), len(want), pid)
                for a, b in zip(got, want):
                    self.assertLessEqual(abs(a - b), Fraction(1, 200), "%s %s: %s vs %s" % (e["id"], pid, got, want))
                covered += 1
        self.assertGreaterEqual(covered, 170)

    def test_the_family_names_are_in_the_solver_and_nothing_else_claims_these_problems_differently(self):
        names = {f.__name__ for f in WS.FAMILIES}
        for e in TABLE:
            self.assertIn(e["id"], names)
            for pid in e["problems"]:
                r = WS.solve(PROBLEMS[pid].PROBLEM)
                self.assertIsNotNone(r, pid)
                self.assertEqual(r.family, e["id"], pid)

    def test_the_older_families_are_all_still_there(self):
        self.assertEqual(len([f for f in WS.FAMILIES if not f.__name__.startswith("archive_")]), 58)


class Declines(unittest.TestCase):
    def test_an_extra_number_a_missing_number_or_other_words_decline(self):
        for e in TABLE:
            fam = AF.make_family(e)
            p = PROBLEMS[e["problems"][0]]
            text = p.PROBLEM
            self.assertIsNotNone(fam(text), e["id"])
            self.assertIsNone(fam(text + " It was 7 o'clock."), e["id"])                       # a number the wording does not own
            blank = fill(p.TEMPLATE, ["" if k == 0 else n for k, n in enumerate(p.NUMBERS)])
            self.assertIsNone(fam(blank), e["id"])                                             # a missing number
            self.assertIsNone(fam("Please look at this: " + text), e["id"])                    # other words in front
            self.assertIsNone(fam(text[: len(text) // 2]), e["id"])                           # half the problem
            self.assertIsNone(fam(""), e["id"])

    def test_a_number_written_in_words_declines(self):
        e = next(x for x in TABLE if x["id"] == "archive_break_even_1")
        fam = AF.make_family(e)
        p = PROBLEMS[e["problems"][0]]
        self.assertIsNone(fam(p.PROBLEM.replace(p.NUMBERS[1], "five", 1)))


class NewNumbers(unittest.TestCase):
    """Change the numbers of a stored problem; whenever the family answers, the unknown it reports must satisfy the stored equation with those numbers
    (checked with word_archive's own reader of equations, not with the table)."""

    @staticmethod
    def residual(equation, x):
        eq = WA._normalize(equation)
        variable, _ = WA._literals(eq)
        left, right = eq.split("=")
        env = {"__builtins__": {}}
        env[variable] = float(x)
        a, b = eval(left, env), eval(right, env)
        return abs(a - b) / (1 + abs(a) + abs(b))

    def test_the_roles_hold_for_other_numbers(self):
        answered = 0
        for e in TABLE:
            fam = AF.make_family(e)
            p = PROBLEMS[e["problems"][0]]
            base = [Fraction(n.replace(",", "")) for n in p.NUMBERS]
            for variant in (lambda n: n * 2, lambda n: n + 1, lambda n: n * 3 + 2, lambda n: n * 5):
                nums = [variant(n) for n in base]
                shown = [AF.show(n) for n in nums]
                r = fam(fill(p.TEMPLATE, shown))
                if r is None:
                    continue
                answered += 1
                x = Fraction(re.search(r"so \w+ = (-?[\d.]+)$", r.reading).group(1))
                self.assertLessEqual(self.residual(fill(e["equation"], shown), x), 1e-5, "%s: %s, x = %s" % (e["id"], fill(e["equation"], shown), x))
        self.assertGreater(answered, 60)


class Reader(unittest.TestCase):
    def test_evaluate_reads_plain_arithmetic_only(self):
        self.assertEqual(AF.evaluate("N[0]*X+F('1/2')", [Fraction(3)], Fraction(2)), Fraction(13, 2))
        for bad in ("__import__('os').system('echo hi')", "open('x')", "N[0].real", "[1,2]", "X**2", "lambda: 1", "'a'+'b'", "N[0] if 1 else 2"):
            with self.assertRaises((ValueError, SyntaxError, TypeError, KeyError, IndexError), msg=bad):
                AF.evaluate(bad, [Fraction(3)], Fraction(2))

    def test_a_missing_table_gives_no_families(self):
        saved = AF.TABLE
        AF.TABLE = os.path.join(os.path.dirname(saved), "no_such_table.json")
        try:
            self.assertEqual(AF.families(), [])
        finally:
            AF.TABLE = saved


if __name__ == "__main__":
    unittest.main()
