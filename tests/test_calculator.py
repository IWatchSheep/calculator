"""Regression tests for the Tkinter addition calculator.

From the PyCharm project root, run:
    python -m unittest discover -s tests -v

A graphical desktop session is needed because these tests instantiate Tkinter.
On headless Linux systems, tests can run via virtual display (Xvfb / pyvirtualdisplay)
or using: xvfb-run -a python -m unittest discover -s tests -v
"""

import contextlib
import io
import os
import shutil
import subprocess
import sys
import tkinter as tk
import unittest
from pathlib import Path

# Import the application's actual addition/addition.py without modifying it.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
from addition.addition import AdditionCalculator

_virtual_display = None


def setUpModule():
    """Start a virtual display on headless Linux/POSIX systems if no display is active."""
    global _virtual_display
    if os.name == "posix" and not os.environ.get("DISPLAY") and not os.environ.get("WAYLAND_DISPLAY"):
        try:
            from pyvirtualdisplay import Display
            _virtual_display = Display(visible=False, size=(1024, 768))
            _virtual_display.start()
        except Exception:
            if shutil.which("Xvfb"):
                try:
                    for disp_num in range(99, 110):
                        disp_str = f":{disp_num}"
                        if not os.path.exists(f"/tmp/.X11-unix/X{disp_num}"):
                            proc = subprocess.Popen(
                                ["Xvfb", disp_str, "-screen", "0", "1024x768x24"],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL,
                            )
                            os.environ["DISPLAY"] = disp_str
                            _virtual_display = proc
                            break
                except Exception:
                    pass


def tearDownModule():
    """Clean up virtual display if one was started."""
    global _virtual_display
    if _virtual_display is not None:
        try:
            if hasattr(_virtual_display, "stop"):
                _virtual_display.stop()
            elif hasattr(_virtual_display, "terminate"):
                _virtual_display.terminate()
                _virtual_display.wait(timeout=2)
        except Exception:
            pass
        _virtual_display = None


class CalculatorRegressionTests(unittest.TestCase):
    def setUp(self):
        try:
            self.root = tk.Tk()
        except tk.TclError as exc:
            self.fail(f"Tkinter requires a graphical desktop to run these tests: {exc}")
        self.root.withdraw()  # Avoid leaving multiple visible test windows.
        self.calculator = AdditionCalculator(self.root)
        self.root.deiconify()
        self.root.focus_force()
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

    def press_buttons(self, sequence):
        """Simulate physical button widget clicks by finding keypad Button widgets and invoking them."""
        buttons_by_text = {
            w.cget("text"): w
            for w in self.calculator.keypad_frame.winfo_children()
            if isinstance(w, tk.Button)
        }
        with contextlib.redirect_stdout(io.StringIO()):
            for char in sequence:
                btn = buttons_by_text.get(char)
                if btn is not None:
                    btn.invoke()
                else:
                    self.calculator.on_button_click(char)
                self.root.update()

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
        self.root.focus_force()
        self.root.update()
        for key in ["<Key-parenleft>", "<Key-2>", "<Key-plus>", "<Key-3>", "<Key-parenright>", "<Return>"]:
            self.root.event_generate(key)
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

    # Automated GUI button click simulations

    def test_gui_button_clicks_nested_parentheses(self):
        """Simulate real GUI button clicks for nested parentheses calculation."""
        self.press_buttons("2+(3+(4+5))=")
        self.assertEqual(self.calculator.result_var.get(), "14")

    def test_gui_button_clicks_decimal_addition(self):
        """Simulate real GUI button clicks for decimal addition in parentheses."""
        self.press_buttons("0.1+(0.2+0.3)=")
        self.assertEqual(self.calculator.result_var.get(), "0.6")

    def test_gui_button_clicks_clear(self):
        """Simulate real GUI button clicks for calculation followed by C button."""
        self.press_buttons("(2+3)=")
        self.assertEqual(self.calculator.result_var.get(), "5")
        self.press_buttons("C")
        self.assertEqual(self.calculator.result_var.get(), "")
        self.assertEqual(self.calculator.addends, ["", ""])

    def test_gui_button_clicks_error_handling(self):
        """Simulate real GUI button clicks for invalid syntax and recovery."""
        self.press_buttons("2+()=")
        self.assertEqual(self.calculator.result_var.get(), "Error")
        self.press_buttons("C")
        self.assertEqual(self.calculator.result_var.get(), "")
        self.assertEqual(self.calculator.addends, ["", ""])

    # Keypad and 0 button positioning stability across multiple addend rows

    def test_keypad_and_zero_button_stability_multiple_rows(self):
        """Keypad container and 0 button remain anchored when 3, 4, 5, or more addend rows are created."""
        app = self.calculator
        self.root.update()
        zero_btn = next(w for w in app.keypad_frame.winfo_children() if w.cget("text") == "0")
        initial_keypad_y = app.keypad_frame.winfo_rooty()
        initial_zero_pos = (zero_btn.winfo_rootx(), zero_btn.winfo_rooty())
        initial_height = self.root.winfo_height()

        # Add 3rd, 4th, 5th, and 6th addends
        self.press("1+2+3+4+5+")
        self.root.update()
        self.assertEqual(len(app.addends), 6)
        self.assertEqual(app.keypad_frame.winfo_rooty(), initial_keypad_y, "Keypad frame y must not shift with multiple addends")
        self.assertEqual((zero_btn.winfo_rootx(), zero_btn.winfo_rooty()), initial_zero_pos, "0 button position must not shift with multiple addends")
        self.assertEqual(self.root.winfo_height(), initial_height, "Window height must not grow when new addends scroll inside canvas")

        # Each addend row removal requires backspacing the character and the empty window
        while len(app.addends) > 2:
            app.on_backspace()
            self.root.update()
        self.assertEqual(len(app.addends), 2)
        self.assertEqual((zero_btn.winfo_rootx(), zero_btn.winfo_rooty()), initial_zero_pos, "0 button must remain stable when addends are removed")

    def test_keypad_stability_with_parentheses_and_equals(self):
        """Keypad and 0 button remain stable across parenthesized inputs, equals, and continuations."""
        app = self.calculator
        self.root.update()
        zero_btn = next(w for w in app.keypad_frame.winfo_children() if w.cget("text") == "0")
        initial_zero_pos = (zero_btn.winfo_rootx(), zero_btn.winfo_rooty())
        initial_keypad_y = app.keypad_frame.winfo_rooty()

        self.press_buttons("(1+2)+(3+4)=")
        self.root.update()
        self.assertEqual(app.result_var.get(), "10")
        self.assertEqual(app.keypad_frame.winfo_rooty(), initial_keypad_y)
        self.assertEqual((zero_btn.winfo_rootx(), zero_btn.winfo_rooty()), initial_zero_pos)

        self.press_buttons("+5=")
        self.root.update()
        self.assertEqual(app.result_var.get(), "15")
        self.assertEqual(app.keypad_frame.winfo_rooty(), initial_keypad_y)
        self.assertEqual((zero_btn.winfo_rootx(), zero_btn.winfo_rooty()), initial_zero_pos)


if __name__ == "__main__":
    unittest.main()
