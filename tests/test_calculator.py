"""Regression tests for the Tkinter addition calculator.

From the PyCharm project root, run:
    python -m unittest discover -s tests -v

A graphical desktop session is needed because these tests instantiate Tkinter.
"""

import contextlib
import io
import sys
import tkinter as tk
import unittest
from pathlib import Path

# Import the application's actual addition/addition.py without modifying it.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
from addition.addition import AdditionCalculator


class CalculatorRegressionTests(unittest.TestCase):
    def setUp(self):
        try:
            self.root = tk.Tk()
        except tk.TclError as exc:
            self.fail(f"Tkinter requires a graphical desktop to run these tests: {exc}")
        self.root.withdraw()  # Avoid leaving multiple visible test windows.
        self.calculator = AdditionCalculator(self.root)
        self.root.deiconify()
        self.root.update()

    def tearDown(self):
        self.root.destroy()

    def calculate_inputs(self, *numbers):
        app = self.calculator
        for index, number in enumerate(numbers):
            if index >= len(app.addends):
                app.add_addend_window()
            app.addends[index] = number
            app.addend_vars[index].set(number)
        with contextlib.redirect_stdout(io.StringIO()):
            app.calculate()
        return app.result_var.get()

    def press(self, sequence):
        with contextlib.redirect_stdout(io.StringIO()):
            for key in sequence:
                self.calculator.on_button_click(key)

    def test_integer_addition(self):
        self.assertEqual(self.calculate_inputs("12", "30"), "42")

    def test_decimal_addition(self):
        self.assertEqual(self.calculate_inputs("0.1", "0.2"), "0.3")

    def test_very_small_decimals_not_scientific(self):
        tiny_prefix = "0." + "0" * 23
        self.assertEqual(self.calculate_inputs(tiny_prefix + "1", tiny_prefix + "2"), tiny_prefix + "3")

    def test_three_addends(self):
        self.assertEqual(self.calculate_inputs("1", "2", "3"), "6")

    def test_decimal_carry_into_integer(self):
        self.assertEqual(self.calculate_inputs("999.99", "0.01"), "1000")

    def test_trailing_zeros(self):
        self.assertEqual(self.calculate_inputs("1.50", "2.50"), "4")

    def test_zero_decimals(self):
        self.assertEqual(self.calculate_inputs("0.000", "0.000"), "0")

    def test_integer_over_1000_digits(self):
        self.assertEqual(self.calculate_inputs("9" * 1100, "1"), "1" + "0" * 1100)

    def test_decimal_over_1000_digits(self):
        self.assertEqual(self.calculate_inputs("9" * 1100 + ".0", "1.0"), "1" + "0" * 1100)

    def test_1500_decimal_places(self):
        prefix = "0." + "0" * 1499
        self.assertEqual(self.calculate_inputs(prefix + "1", prefix + "2"), prefix + "3")

    def test_mixed_large_and_small_decimals(self):
        self.assertEqual(
            self.calculate_inputs("1." + "0" * 1100, "0." + "0" * 1099 + "1"),
            "1." + "0" * 1099 + "1",
        )

    def test_single_small_decimal(self):
        self.assertEqual(self.calculate_inputs("0.00000000000001"), "0.00000000000001")

    def test_keypad_input(self):
        self.press("12+3=")
        self.assertEqual(self.calculator.result_var.get(), "15")

    def test_continue_after_equals(self):
        self.press("12+3=+4=")
        self.assertEqual(self.calculator.result_var.get(), "19")

    def test_third_addend_does_not_shift_keypad(self):
        app = self.calculator
        self.root.update()
        zero_button = next(widget for widget in app.keypad_frame.winfo_children() if widget.cget("text") == "0")
        before = (app.keypad_frame.winfo_rooty(), zero_button.winfo_rooty(), self.root.winfo_height())
        self.press("1+2+")
        self.root.update()
        after = (app.keypad_frame.winfo_rooty(), zero_button.winfo_rooty(), self.root.winfo_height())
        self.assertEqual(len(app.addends), 3)
        self.assertEqual(before, after, "Adding a third input must not move the keypad or resize the window")

    def test_clear_restores_two_inputs(self):
        self.press("1+2+3=")
        self.press("C")
        self.assertEqual(self.calculator.addends, ["", ""])
        self.assertEqual(self.calculator.result_var.get(), "")


if __name__ == "__main__":
    unittest.main()
