"""Tests for paste_text.py (Paste-Text Operator Stage 1a).

Run from algebra_word_problems/algebra_matcher:
    python -m unittest test_paste_text
"""
import unittest
from fractions import Fraction

import number_puzzle as NP
import paste_text as PT
import word_solver as WS

WREN = (
    "Wren is 4 times as old as Jamal. In 5 years, the sum of their ages will be 105. "
    "How old is each now?"
)
NUMBER_PUZZLE = "6 times the difference of a number and 6 is 174. What is the number?"
PROBLEM_0950 = (
    "An apple, a banana, and a cherry cup cost $4.05 together. Two apples and a banana "
    "cost $3.40. A banana and two cherry cups cost $4.70. Find each price."
)
ROOF = (
    "A sloped roof rises 5 m over 12 m, then 7 m over a longer run. "
    "The hypotenuse is 13 m. How long is the run?"
)
FRESH_DECLINES = (
    "A slow train leaves at 70 mph. Two hours later a fast train follows at 50 mph. "
    "How long until the fast one catches it?",
    "How many pounds of coffee worth $10 a pound must be added to 14 lb of coffee "
    "worth $8 a pound to make a mix worth $11 a pound?",
    "Lena spent 100% of a paycheck on rent and had $50 left. How much was the paycheck?",
    "A rectangle has a perimeter of 34 m and an area of 60 m^2. How long is it?",
)
MATH_TEMPLATES = (
    "(□ + 3) × 2",
    "sqrt(16) + abs(-3)",
    "Time dilation(1, □)",
    "(? + 3) × 2",
)


def declined(result):
    return (
        result.supported is False
        and result.family is None
        and result.values == []
        and result.equation is None
        and result.reading == PT.UNSUPPORTED
    )


class Analyze(unittest.TestCase):
    def test_wren_jamal_ages(self):
        expected = WS.solve(WREN)
        result = PT.analyze(WREN)
        self.assertTrue(result.supported)
        self.assertEqual(result.family, "times_as_old_future_sum")
        self.assertEqual(result.values, [Fraction(19), Fraction(76)])
        self.assertEqual(result.values, list(expected.values))
        self.assertEqual(result.equation, expected.equation)
        self.assertEqual(result.reading, expected.reading)
        self.assertNotIn("Jamal", result.reading)
        self.assertNotIn("Wren", result.reading)

    def test_number_puzzle_example(self):
        expected = NP.solve(NUMBER_PUZZLE)
        result = PT.analyze(NUMBER_PUZZLE)
        self.assertIsNone(WS.solve(NUMBER_PUZZLE))
        self.assertTrue(result.supported)
        self.assertEqual(result.family, "number_puzzle")
        self.assertEqual(result.values, [Fraction(35)])
        self.assertEqual(result.values, [expected.answer])
        self.assertEqual(result.equation, expected.equation)
        self.assertEqual(result.reading, expected.reading)

    def test_word_solver_is_tried_before_number_puzzle(self):
        result = PT.analyze(WREN)
        self.assertEqual(result.family, "times_as_old_future_sum")
        self.assertNotEqual(result.family, "number_puzzle")

    def test_problem_0950_is_unsupported(self):
        self.assertTrue(declined(PT.analyze(PROBLEM_0950)))
        self.assertIsNone(WS.solve(PROBLEM_0950))
        self.assertIsNone(NP.solve(PROBLEM_0950))

    def test_roof_leftover_numbers_are_unsupported(self):
        self.assertTrue(declined(PT.analyze(ROOF)))
        self.assertIsNone(WS.solve(ROOF))

    def test_fresh_required_declines_are_unsupported(self):
        for sentence in FRESH_DECLINES:
            self.assertTrue(declined(PT.analyze(sentence)), sentence)
            self.assertIsNone(WS.solve(sentence), sentence)

    def test_empty_text_is_declined(self):
        for text in ("", "   ", "\n", None, 105):
            self.assertTrue(declined(PT.analyze(text)), repr(text))

    def test_mathematical_templates_are_not_word_problems(self):
        for text in MATH_TEMPLATES:
            self.assertTrue(declined(PT.analyze(text)), text)

    def test_decline_format_is_stable(self):
        result = PT.analyze("")
        self.assertEqual(
            result,
            PT.PasteResult(False, None, [], None, PT.UNSUPPORTED),
        )


if __name__ == "__main__":
    unittest.main(verbosity=1 if "-v" not in sys.argv else 2)
