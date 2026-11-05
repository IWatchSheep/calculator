"""Tests for the shared addition-and-parentheses expression evaluator."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from calculator_core.expression import evaluate_addition


class ExpressionTests(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(evaluate_addition("2 + 3"), "5")

    def test_parentheses(self):
        self.assertEqual(evaluate_addition("2 + (3 + 4)"), "9")

    def test_nested_parentheses(self):
        self.assertEqual(evaluate_addition("2 + (3 + (4 + 5))"), "14")

    def test_multiple_groups(self):
        self.assertEqual(evaluate_addition("(1 + 2) + (3 + 4)"), "10")

    def test_decimal_precision(self):
        self.assertEqual(evaluate_addition("0.1 + (0.2 + 0.3)"), "0.6")

    def test_very_small_decimal(self):
        self.assertEqual(evaluate_addition("0.000000000000000000000001 + 0.000000000000000000000002"),
                         "0.000000000000000000000003")

    def test_large_number(self):
        self.assertEqual(evaluate_addition("(" + "9" * 1100 + ") + 1"), "1" + "0" * 1100)

    def test_1500_decimal_places(self):
        prefix = "0." + "0" * 1499
        self.assertEqual(evaluate_addition(prefix + "1 + " + prefix + "2"), prefix + "3")

    def test_trailing_zeros(self):
        self.assertEqual(evaluate_addition("1.50 + 2.50"), "4")

    def test_whitespace(self):
        self.assertEqual(evaluate_addition("  2 + ( 3 + 4 )  "), "9")

    def test_missing_closing_parenthesis(self):
        with self.assertRaises(ValueError):
            evaluate_addition("2 + (3 + 4")

    def test_extra_closing_parenthesis(self):
        with self.assertRaises(ValueError):
            evaluate_addition("2 + 3)")

    def test_empty_parentheses(self):
        with self.assertRaises(ValueError):
            evaluate_addition("2 + ()")

    def test_incomplete_expression(self):
        with self.assertRaises(ValueError):
            evaluate_addition("2 +")

    def test_subtraction_not_supported_yet(self):
        with self.assertRaises(ValueError):
            evaluate_addition("5 - 3")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            evaluate_addition("   ")

    def test_no_implicit_multiplication(self):
        with self.assertRaises(ValueError):
            evaluate_addition("2(3 + 4)")


if __name__ == "__main__":
    unittest.main()
