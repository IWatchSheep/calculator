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

    # Parentheses regression tests

    def test_parentheses_buttons(self):
        """1. Opening and closing parentheses buttons on keypad."""
        app = self.calculator
        open_btn = next(w for w in app.keypad_frame.winfo_children() if w.cget("text") == "(")
        close_btn = next(w for w in app.keypad_frame.winfo_children() if w.cget("text") == ")")
        open_btn.invoke()
        self.assertEqual(app.addends[0], "(")
        self.press("7")
        close_btn.invoke()
        self.assertEqual(app.addends[0], "(7)")

    def test_parentheses_physical_keyboard(self):
        """2. Parentheses entered using the physical keyboard."""
        app = self.calculator
        self.root.event_generate("<Key-parenleft>")
        self.root.event_generate("2")
        self.root.event_generate("+")
        self.root.event_generate("3")
        self.root.event_generate("<Key-parenright>")
        self.root.event_generate("<Return>")
        self.root.update()
        self.assertEqual(app.result_var.get(), "5")

    def test_nested_parentheses(self):
        """3. Nested parentheses expressions."""
        self.press("2+(3+(4+5))=")
        self.assertEqual(self.calculator.result_var.get(), "14")
        self.calculator.clear_all()
        self.assertEqual(self.calculate_inputs("((2 + 3))"), "5")

    def test_multiple_groups_of_parentheses(self):
        """4. Multiple groups of parentheses."""
        self.press("(1+2)+(3+4)=")
        self.assertEqual(self.calculator.result_var.get(), "10")
        self.calculator.clear_all()
        self.assertEqual(self.calculate_inputs("(1 + 2)", "(3 + 4)"), "10")

    def test_decimal_addition_inside_parentheses(self):
        """5. Decimal addition inside parentheses."""
        self.press("0.1+(0.2+0.3)=")
        self.assertEqual(self.calculator.result_var.get(), "0.6")
        self.calculator.clear_all()
        self.assertEqual(self.calculate_inputs("0.1 + (0.2 + 0.3)"), "0.6")
        self.calculator.clear_all()
        self.assertEqual(self.calculate_inputs("(0.25 + 0.75)", "(1.5 + 2.5)"), "5")

    def test_missing_closing_parentheses(self):
        """6. Missing closing parentheses returns Error."""
        self.press("2+(3+4=")
        self.assertEqual(self.calculator.result_var.get(), "Error")
        self.calculator.clear_all()
        self.assertEqual(self.calculate_inputs("2 + (3 + 4"), "Error")

    def test_unexpected_closing_parentheses(self):
        """7. Unexpected closing parentheses returns Error."""
        self.press("2+3)=")
        self.assertEqual(self.calculator.result_var.get(), "Error")
        self.calculator.clear_all()
        self.assertEqual(self.calculate_inputs("2 + 3)"), "Error")

    def test_empty_parentheses(self):
        """8. Empty parentheses returns Error."""
        self.press("2+()=")
        self.assertEqual(self.calculator.result_var.get(), "Error")
        self.calculator.clear_all()
        self.assertEqual(self.calculate_inputs("2 + ()"), "Error")

    def test_backspace_when_entering_parentheses(self):
        """9. Backspace when entering parentheses."""
        app = self.calculator
        self.press("(")
        self.assertEqual(app.addends[0], "(")
        app.on_backspace()
        self.assertEqual(app.addends[0], "")
        self.press("(2+")
        self.assertEqual(app.addends[1], "")
        self.press("3)")
        self.assertEqual(app.addends[1], "3)")
        app.on_backspace()
        self.assertEqual(app.addends[1], "3")

    def test_clear_after_entering_parentheses(self):
        """10. Clear after entering parentheses."""
        app = self.calculator
        self.press("(1+2)+(3+4)=")
        self.assertEqual(app.result_var.get(), "10")
        self.press("C")
        self.assertEqual(app.addends, ["", ""])
        self.assertEqual(app.result_var.get(), "")
        self.assertEqual(app.current_index, 0)

    def test_continue_after_equals_with_parentheses(self):
        """11. Continuing calculations after pressing equals."""
        self.press("(2+3)=+4=")
        self.assertEqual(self.calculator.result_var.get(), "9")
        self.press("+(1+2)=")
        self.assertEqual(self.calculator.result_var.get(), "12")

    def test_stable_keypad_position_after_using_parentheses(self):
        """12. Stable keypad position after using parentheses."""
        app = self.calculator
        self.root.update()
        zero_button = next(w for w in app.keypad_frame.winfo_children() if w.cget("text") == "0")
        before = (app.keypad_frame.winfo_rooty(), zero_button.winfo_rooty(), self.root.winfo_height())
        self.press("(1+2)+")
        self.root.update()
        after = (app.keypad_frame.winfo_rooty(), zero_button.winfo_rooty(), self.root.winfo_height())
        self.assertEqual(before, after, "Using parentheses and adding addends must not shift keypad or resize window")

    def test_original_addition_without_parentheses(self):
        """13. Original addition calculations without parentheses."""
        self.assertEqual(self.calculate_inputs("12", "30"), "42")
        self.calculator.clear_all()
        self.press("100+250=")
        self.assertEqual(self.calculator.result_var.get(), "350")
        self.calculator.clear_all()
        self.assertEqual(self.calculate_inputs("10.5", "20.25"), "30.75")

    def test_stability_when_adding_third_addend_with_parentheses(self):
        """14. Stability when adding a third addend with parentheses."""
        app = self.calculator
        self.root.update()
        zero_button = next(w for w in app.keypad_frame.winfo_children() if w.cget("text") == "0")
        before = (app.keypad_frame.winfo_rooty(), zero_button.winfo_rooty(), self.root.winfo_height())
        self.press("1+(2+3)+")
        self.root.update()
        after = (app.keypad_frame.winfo_rooty(), zero_button.winfo_rooty(), self.root.winfo_height())
        self.assertGreaterEqual(len(app.addends), 3)
        self.assertEqual(before, after, "Keypad must stay stable when three or more inputs with parentheses are entered")


if __name__ == "__main__":
    unittest.main()
