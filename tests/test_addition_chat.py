"""Regression and functional tests for the Tkinter addition calculator with word chatbot."""

import contextlib
import io
import os
import shutil
import subprocess
import sys
import tkinter as tk
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
from addition_chat.addition import AdditionCalculator, WordSummerChatbot

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


class AdditionChatTests(unittest.TestCase):
    def setUp(self):
        try:
            self.root = tk.Tk()
        except tk.TclError as exc:
            self.fail(f"Tkinter requires a graphical desktop: {exc}")
        self.root.withdraw()
        self.calculator = AdditionCalculator(self.root)
        self.root.deiconify()
        self.root.focus_force()
        self.root.update()

    def press(self, sequence: str):
        """Simulate real GUI keypad button presses."""
        app = self.calculator
        buttons_by_text = {}
        for child in app.keypad_frame.winfo_children():
            if isinstance(child, tk.Button):
                buttons_by_text[child.cget("text")] = child

        with contextlib.redirect_stdout(io.StringIO()):
            for char in sequence:
                btn = buttons_by_text.get(char)
                if btn is not None:
                    btn.invoke()
                else:
                    self.calculator.on_button_click(char)
                self.root.update()

    def tearDown(self):
        self.root.destroy()

    def calculate_inputs(self, *items):
        """items can be either numbers, (number, word) tuples, or (number, word, context, ...) tuples."""
        app = self.calculator
        for index, item in enumerate(items):
            if isinstance(item, tuple):
                num = item[0]
                word = item[1] if len(item) > 1 else ""
                context = item[2] if len(item) > 2 else ""
                extras = item[3:] if len(item) > 3 else ()
            else:
                num, word, context, extras = item, "", "", ()

            if index >= len(app.addends):
                app.add_addend_window()
            app.addends[index] = str(num)
            app.addend_vars[index].set(str(num))
            app.addend_words[index] = str(word)
            app.addend_word_vars[index].set(str(word))
            app.addend_contexts[index] = str(context)
            app.addend_context_vars[index].set(str(context))

            for col_idx, extra_val in enumerate(extras):
                while col_idx >= len(app.extra_addend_words):
                    app.add_column()
                app.extra_addend_words[col_idx][index] = str(extra_val)
                app.extra_word_vars[col_idx][index].set(str(extra_val))

        with contextlib.redirect_stdout(io.StringIO()):
            app.calculate()
        return app.result_var.get(), app.result_word_var.get()

    def test_basic_addition_with_words_same_unit(self):
        num_res, word_res = self.calculate_inputs(("3", "apples"), ("2", "apples"))
        self.assertEqual(num_res, "5")
        self.assertEqual(word_res, "apples")

    def test_single_unit_singular(self):
        num_res, word_res = self.calculate_inputs(("0.5", "apple"), ("0.5", "apple"))
        self.assertEqual(num_res, "1")
        self.assertEqual(word_res, "apple")

    def test_category_aggregation_fruits(self):
        num_res, word_res = self.calculate_inputs(("2", "apples"), ("3", "oranges"))
        self.assertEqual(num_res, "5")
        self.assertEqual(word_res, "fruits (2 apples, 3 oranges)")

    def test_category_aggregation_animals(self):
        num_res, word_res = self.calculate_inputs(("1", "cat"), ("2", "dogs"))
        self.assertEqual(num_res, "3")
        self.assertEqual(word_res, "animals (1 cat, 2 dogs)")

    def test_two_distinct_items_uncategorized(self):
        num_res, word_res = self.calculate_inputs(("10", "widgets"), ("5", "gadgets"))
        self.assertEqual(num_res, "15")
        self.assertEqual(word_res, "widgets and gadgets")

    def test_three_addends_layout_stability(self):
        app = self.calculator
        self.root.update()
        zero_btn = next(w for w in app.keypad_frame.winfo_children() if w.cget("text") == "0")
        before = (app.bottom_container.winfo_rooty(), zero_btn.winfo_rooty())

        with contextlib.redirect_stdout(io.StringIO()):
            for k in "1+2+":
                app.on_button_click(k)
        self.root.update()
        after = (app.bottom_container.winfo_rooty(), zero_btn.winfo_rooty())

        self.assertEqual(len(app.addends), 3)
        self.assertEqual(len(app.addend_words), 3)
        self.assertEqual(len(app.addend_contexts), 3)
        self.assertEqual(before, after, "Adding a third addend must not shift the keypad container or the 0 button")

    def test_typewriter_input(self):
        app = self.calculator
        app.on_typewriter_char("c")
        app.on_typewriter_char("a")
        app.on_typewriter_char("t")
        self.assertEqual(app.addend_words[0], "cat")
        self.assertEqual(app.addend_word_vars[0].get(), "cat")

        app.on_typewriter_backspace()
        self.assertEqual(app.addend_words[0], "ca")

        app.on_typewriter_char(" ")
        self.assertEqual(app.addend_words[0], "ca ")

        app.on_typewriter_clear_word()
        self.assertEqual(app.addend_words[0], "")

    def test_dropdown_options_contain_premade_words(self):
        app = self.calculator
        self.assertIn("apples", app.word_options)
        self.assertIn("bananas", app.word_options)
        self.assertIn("dollars", app.word_options)
        self.assertIn("(Type custom word...)", app.word_options)

    def test_add_custom_word_persists_to_dropdown_options(self):
        app = self.calculator
        custom_term = "spaceships"
        self.assertNotIn(custom_term, app.word_options)

        # Enter custom term in row 0 and click save
        app.addend_words[0] = custom_term
        app.addend_word_vars[0].set(custom_term)
        app.save_custom_word(0)

        # Verify added to options
        self.assertIn(custom_term, app.word_options)
        # Verify all comboboxes refreshed with the new option
        for combo in app.addend_word_entries:
            self.assertIn(custom_term, combo["values"])

    def test_calculate_automatically_adds_new_custom_words_to_list(self):
        app = self.calculator
        term1 = "pineapples"
        term2 = "watermelons"
        self.calculate_inputs(("2", term1), ("3", term2))
        self.assertIn(term1, app.word_options)
        self.assertIn(term2, app.word_options)

    def test_clear_all_resets_words_and_numbers(self):
        self.calculate_inputs(("10", "apples"), ("20", "bananas"))
        self.calculator.clear_all()
        self.assertEqual(self.calculator.addends, ["", ""])
        self.assertEqual(self.calculator.addend_words, ["", ""])
        self.assertEqual(self.calculator.addend_contexts, ["", ""])
        self.assertEqual(self.calculator.result_var.get(), "")
        self.assertEqual(self.calculator.result_word_var.get(), "")

    # Regression and feature tests for Column 3 (Description / Context) and dynamic columns

    def test_third_column_addition_same_item_and_context(self):
        """User example: 2 pens in the drawer + 3 pens in the drawer -> 5 pens in the drawer."""
        num_res, word_res = self.calculate_inputs(
            ("2", "pens", "in the drawer"),
            ("3", "pens", "in the drawer"),
        )
        self.assertEqual(num_res, "5")
        self.assertEqual(word_res, "pens in the drawer")

    def test_third_column_single_unit_singular(self):
        num_res, word_res = self.calculate_inputs(
            ("0.5", "pen", "in the drawer"),
            ("0.5", "pen", "in the drawer"),
        )
        self.assertEqual(num_res, "1")
        self.assertEqual(word_res, "pen in the drawer")

    def test_third_column_different_contexts_same_item(self):
        num_res, word_res = self.calculate_inputs(
            ("2", "pens", "in the drawer"),
            ("3", "pens", "on the desk"),
        )
        self.assertEqual(num_res, "5")
        self.assertEqual(word_res, "pens (2 in the drawer, 3 on the desk)")

    def test_third_column_category_aggregation_with_context(self):
        num_res, word_res = self.calculate_inputs(
            ("2", "apples", "in the fridge"),
            ("3", "oranges", "on the counter"),
        )
        self.assertEqual(num_res, "5")
        self.assertEqual(word_res, "fruits (2 apples in the fridge, 3 oranges on the counter)")

    def test_third_column_dropdown_options(self):
        app = self.calculator
        self.assertIn("in the drawer", app.context_options)
        self.assertIn("on the table", app.context_options)
        self.assertIn("in the box", app.context_options)
        self.assertIn("(Type custom description...)", app.context_options)

    def test_third_column_add_custom_context_persists(self):
        app = self.calculator
        custom_ctx = "under the rug"
        self.assertNotIn(custom_ctx, app.context_options)

        app.addend_contexts[0] = custom_ctx
        app.addend_context_vars[0].set(custom_ctx)
        app.save_custom_context(0)

        self.assertIn(custom_ctx, app.context_options)
        for combo in app.addend_context_entries:
            self.assertIn(custom_ctx, combo["values"])

    def test_typewriter_input_into_third_column(self):
        app = self.calculator
        # Activate Column 3 (context)
        app._set_active_index(0, "word", col=1)
        app.on_typewriter_char("b")
        app.on_typewriter_char("o")
        app.on_typewriter_char("x")
        self.assertEqual(app.addend_contexts[0], "box")
        self.assertEqual(app.addend_context_vars[0].get(), "box")

        app.on_typewriter_backspace()
        self.assertEqual(app.addend_contexts[0], "bo")

        app.on_typewriter_clear_word()
        self.assertEqual(app.addend_contexts[0], "")

    def test_dynamic_add_column(self):
        app = self.calculator
        app.add_column("Extra Detail")
        self.assertEqual(len(app.extra_addend_words), 1)
        self.assertEqual(len(app.extra_word_entries[0]), 2)

        num_res, word_res = self.calculate_inputs(
            ("2", "pens", "in the drawer", "on Monday"),
            ("3", "pens", "in the drawer", "on Monday"),
        )
        self.assertEqual(num_res, "5")
        self.assertEqual(word_res, "pens in the drawer on Monday")

    def test_clear_all_resets_third_column_and_extra_columns(self):
        app = self.calculator
        app.add_column("Extra Detail")
        self.calculate_inputs(
            ("2", "pens", "in the drawer", "red"),
            ("3", "pens", "in the drawer", "blue"),
        )
        app.clear_all()
        self.assertEqual(app.addends, ["", ""])
        self.assertEqual(app.addend_words, ["", ""])
        self.assertEqual(app.addend_contexts, ["", ""])
        self.assertEqual(app.extra_addend_words[0], ["", ""])
        self.assertEqual(app.result_var.get(), "")
        self.assertEqual(app.result_word_var.get(), "")

    def test_word_summer_chatbot_direct_invocation(self):
        result = WordSummerChatbot.summarize(
            [("2", "pens", "in the drawer"), ("3", "pens", "in the drawer")],
            "5",
        )
        self.assertEqual(result, "pens in the drawer")

    # --- New Parentheses Regression Tests ---

    def test_parentheses_button_input(self):
        """1. Opening and closing parentheses buttons on keypad."""
        app = self.calculator
        buttons_by_text = {
            w.cget("text"): w
            for w in app.keypad_frame.winfo_children()
            if isinstance(w, tk.Button)
        }
        self.assertIn("(", buttons_by_text)
        self.assertIn(")", buttons_by_text)

        # Use invoke() on keypad buttons directly
        buttons_by_text["("].invoke()
        self.root.update()
        self.assertEqual(app.addends[0], "(")

        buttons_by_text["2"].invoke()
        self.root.update()
        self.assertEqual(app.addends[0], "(2")

        with contextlib.redirect_stdout(io.StringIO()):
            buttons_by_text["+"].invoke()
        self.root.update()
        self.assertEqual(app.current_index, 1)

        buttons_by_text["3"].invoke()
        self.root.update()
        buttons_by_text[")"].invoke()
        self.root.update()
        self.assertEqual(app.addends[1], "3)")

        with contextlib.redirect_stdout(io.StringIO()):
            buttons_by_text["="].invoke()
        self.root.update()
        self.assertEqual(app.result_var.get(), "5")

    def test_parentheses_physical_keyboard(self):
        """2. Parentheses entered using the physical keyboard."""
        app = self.calculator
        self.root.focus_force()
        self.root.update()
        for key in ["<Key-parenleft>", "<Key-2>", "<Key-plus>", "<Key-3>", "<Key-parenright>", "<Return>"]:
            self.root.event_generate(key)
            self.root.update()
        self.assertEqual(app.result_var.get(), "5")

    def test_nested_parentheses_with_words(self):
        """3. Nested parentheses with words (Example D)."""
        # User Example D: (2 pens in the drawer + (3 pens in the drawer + 4 pens in the drawer)) -> 9 pens in the drawer
        num_res, word_res = self.calculate_inputs(
            ("(2", "pens", "in the drawer"),
            ("(3", "pens", "in the drawer"),
            ("4))", "pens", "in the drawer"),
        )
        self.assertEqual(num_res, "9")
        self.assertEqual(word_res, "pens in the drawer")

        # Also verify with GUI press sequence
        self.calculator.clear_all()
        app = self.calculator
        app.addend_words[0] = "pens"
        app.addend_word_vars[0].set("pens")
        app.addend_contexts[0] = "in the drawer"
        app.addend_context_vars[0].set("in the drawer")
        self.press("2+")
        app.addend_words[1] = "pens"
        app.addend_word_vars[1].set("pens")
        app.addend_contexts[1] = "in the drawer"
        app.addend_context_vars[1].set("in the drawer")
        self.press("(3+")
        app.addend_words[2] = "pens"
        app.addend_word_vars[2].set("pens")
        app.addend_contexts[2] = "in the drawer"
        app.addend_context_vars[2].set("in the drawer")
        self.press("4)=")
        self.assertEqual(app.result_var.get(), "9")
        self.assertEqual(app.result_word_var.get(), "pens in the drawer")

    def test_multiple_parenthesized_groups(self):
        """4. Multiple parenthesized groups (Example E)."""
        # User Example E: (2 pens in the drawer + 3 pens in the drawer) + (4 pens in the drawer + 1 pen in the drawer) -> 10 pens in the drawer
        num_res, word_res = self.calculate_inputs(
            ("(2", "pens", "in the drawer"),
            ("3)", "pens", "in the drawer"),
            ("(4", "pens", "in the drawer"),
            ("1)", "pen", "in the drawer"),
        )
        self.assertEqual(num_res, "10")
        self.assertEqual(word_res, "pens in the drawer")

    def test_matching_items_and_contexts_parentheses(self):
        """5. Matching items and contexts with parentheses (Example A)."""
        # User Example A: (2 pens in the drawer + 3 pens in the drawer) -> 5 pens in the drawer
        num_res, word_res = self.calculate_inputs(
            ("(2", "pens", "in the drawer"),
            ("3)", "pens", "in the drawer"),
        )
        self.assertEqual(num_res, "5")
        self.assertEqual(word_res, "pens in the drawer")

    def test_different_contexts_with_parentheses(self):
        """6. Different contexts with parentheses (Example B)."""
        # User Example B: (2 pens in the drawer + 3 pens on the desk) -> 5 pens (2 in the drawer, 3 on the desk)
        num_res, word_res = self.calculate_inputs(
            ("(2", "pens", "in the drawer"),
            ("3)", "pens", "on the desk"),
        )
        self.assertEqual(num_res, "5")
        self.assertEqual(word_res, "pens (2 in the drawer, 3 on the desk)")

    def test_category_aggregation_with_parentheses(self):
        """7. Category aggregation with parentheses (Example C)."""
        # User Example C: (2 apples in the fridge + 3 oranges on the counter) -> 5 fruits (2 apples in the fridge, 3 oranges on the counter)
        num_res, word_res = self.calculate_inputs(
            ("(2", "apples", "in the fridge"),
            ("3)", "oranges", "on the counter"),
        )
        self.assertEqual(num_res, "5")
        self.assertEqual(word_res, "fruits (2 apples in the fridge, 3 oranges on the counter)")

    def test_decimal_quantities_inside_parentheses(self):
        """8. Decimal quantities inside parentheses."""
        # 0.1 + (0.2 + 0.3) -> 0.6 pens in the drawer
        num_res, word_res = self.calculate_inputs(
            ("0.1", "pens", "in the drawer"),
            ("(0.2", "pens", "in the drawer"),
            ("0.3)", "pens", "in the drawer"),
        )
        self.assertEqual(num_res, "0.6")
        self.assertEqual(word_res, "pens in the drawer")

        # Decimal category aggregation
        self.calculator.clear_all()
        num_res, word_res = self.calculate_inputs(
            ("(0.25", "apples", "in the fridge"),
            ("0.75)", "oranges", "on the counter"),
        )
        self.assertEqual(num_res, "1")
        self.assertEqual(word_res, "fruits (0.25 apples in the fridge, 0.75 oranges on the counter)")

        # Exact precision without scientific notation
        self.calculator.clear_all()
        tiny_a = "0.00000000000000000001"
        tiny_b = "0.00000000000000000002"
        tiny_res = "0.00000000000000000003"
        num_res, word_res = self.calculate_inputs(
            (f"({tiny_a}", "pens", "in the drawer"),
            (f"{tiny_b})", "pens", "in the drawer"),
        )
        self.assertEqual(num_res, tiny_res)
        self.assertEqual(word_res, "pens in the drawer")

    def test_singular_and_plural_handling_with_parentheses(self):
        """9. Singular and plural word handling with parentheses."""
        # Total = 1 -> singular "pen"
        num_res, word_res = self.calculate_inputs(
            ("(0.5", "pen", "in the drawer"),
            ("0.5)", "pen", "in the drawer"),
        )
        self.assertEqual(num_res, "1")
        self.assertEqual(word_res, "pen in the drawer")

        # Total = 2 -> plural "pens"
        self.calculator.clear_all()
        num_res, word_res = self.calculate_inputs(
            ("(1", "pen", "in the drawer"),
            ("1)", "pen", "in the drawer"),
        )
        self.assertEqual(num_res, "2")
        self.assertEqual(word_res, "pens in the drawer")

        # Fractional total != 1 -> plural "pens"
        self.calculator.clear_all()
        num_res, word_res = self.calculate_inputs(
            ("(0.2", "pen", "in the drawer"),
            ("0.3)", "pen", "in the drawer"),
        )
        self.assertEqual(num_res, "0.5")
        self.assertEqual(word_res, "pens in the drawer")

    def test_unmatched_parentheses(self):
        """10. Unmatched parentheses return Error and clear word result."""
        # Missing closing parenthesis
        num_res, word_res = self.calculate_inputs(
            ("2", "pens", "in the drawer"),
            ("(3 + 4", "pens", "in the drawer"),
        )
        self.assertEqual(num_res, "Error")
        self.assertEqual(word_res, "")

        # Unexpected closing parenthesis
        self.calculator.clear_all()
        num_res, word_res = self.calculate_inputs(
            ("2 + 3)", "pens", "in the drawer"),
        )
        self.assertEqual(num_res, "Error")
        self.assertEqual(word_res, "")

        # Keypad sequence with missing closing parenthesis
        self.calculator.clear_all()
        self.press("2+(3+4=")
        self.assertEqual(self.calculator.result_var.get(), "Error")
        self.assertEqual(self.calculator.result_word_var.get(), "")

    def test_empty_parentheses(self):
        """11. Empty parentheses return Error."""
        num_res, word_res = self.calculate_inputs(
            ("2 + ()", "pens", "in the drawer"),
        )
        self.assertEqual(num_res, "Error")
        self.assertEqual(word_res, "")

        self.calculator.clear_all()
        self.press("2+()=")
        self.assertEqual(self.calculator.result_var.get(), "Error")
        self.assertEqual(self.calculator.result_word_var.get(), "")

    def test_backspace_while_editing_parentheses(self):
        """12. Backspace while editing parentheses."""
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

        # Typewriter backspace when word column is active
        app._set_active_index(0, "word", col=0)
        app.on_typewriter_char("b")
        self.assertEqual(app.addend_words[0], "b")
        app.on_backspace()
        self.assertEqual(app.addend_words[0], "")

    def test_clear_after_entering_parentheses(self):
        """13. Clear after entering parentheses resets numbers, words, and results."""
        app = self.calculator
        self.calculate_inputs(
            ("(2", "pens", "in the drawer"),
            ("3)", "pens", "in the drawer"),
        )
        self.assertEqual(app.result_var.get(), "5")
        self.assertEqual(app.result_word_var.get(), "pens in the drawer")

        self.press("C")
        self.assertEqual(app.addends, ["", ""])
        self.assertEqual(app.addend_words, ["", ""])
        self.assertEqual(app.addend_contexts, ["", ""])
        self.assertEqual(app.result_var.get(), "")
        self.assertEqual(app.result_word_var.get(), "")
        self.assertEqual(app.current_index, 0)

    def test_continued_calculations_after_equals_with_parentheses(self):
        """14. Continuing calculations after pressing equals with parentheses."""
        self.press("(2+3)=+4=")
        self.assertEqual(self.calculator.result_var.get(), "9")

        self.press("+(1+2)=")
        self.assertEqual(self.calculator.result_var.get(), "12")

        # Continued addition with words
        self.calculator.clear_all()
        app = self.calculator
        self.calculate_inputs(
            ("(2", "pens", "in the drawer"),
            ("3)", "pens", "in the drawer"),
        )
        self.assertEqual(app.result_var.get(), "5")
        self.assertEqual(app.result_word_var.get(), "pens in the drawer")

        # Press + to continue: transfers result 5 into row 0, preserving item and context columns
        app.on_button_click("+")
        self.assertEqual(app.addends[0], "5")
        self.assertEqual(app.addend_words[0], "pens")
        self.assertEqual(app.addend_contexts[0], "in the drawer")
        self.assertEqual(app.current_index, 1)

        # Enter row 1 with parentheses
        app.addends[1] = "(4 + 1)"
        app.addend_vars[1].set("(4 + 1)")
        app.addend_words[1] = "pens"
        app.addend_word_vars[1].set("pens")
        app.addend_contexts[1] = "in the drawer"
        app.addend_context_vars[1].set("in the drawer")

        with contextlib.redirect_stdout(io.StringIO()):
            app.calculate()
        self.assertEqual(app.result_var.get(), "10")
        self.assertEqual(app.result_word_var.get(), "pens in the drawer")

    def test_additional_dynamic_columns_with_parentheses(self):
        """15. Additional dynamic columns combined with parentheses."""
        app = self.calculator
        app.add_column("Schedule")

        # Matching dynamic column
        num_res, word_res = self.calculate_inputs(
            ("(2", "pens", "in the drawer", "on Monday"),
            ("3)", "pens", "in the drawer", "on Monday"),
        )
        self.assertEqual(num_res, "5")
        self.assertEqual(word_res, "pens in the drawer on Monday")

        # Different dynamic column values
        self.calculator.clear_all()
        num_res, word_res = self.calculate_inputs(
            ("(2", "pens", "in the drawer", "on Monday"),
            ("3)", "pens", "in the drawer", "on Tuesday"),
        )
        self.assertEqual(num_res, "5")
        self.assertEqual(word_res, "pens (2 in the drawer on Monday, 3 in the drawer on Tuesday)")

    def test_keypad_stability_after_adding_parentheses_and_new_rows(self):
        """16. Keypad stability after adding parentheses and new rows."""
        app = self.calculator
        self.root.update()

        zero_btn = next(w for w in app.keypad_frame.winfo_children() if w.cget("text") == "0")
        open_paren_btn = next(w for w in app.keypad_frame.winfo_children() if w.cget("text") == "(")
        close_paren_btn = next(w for w in app.keypad_frame.winfo_children() if w.cget("text") == ")")

        # Verify grid layout positions
        self.assertEqual(int(zero_btn.grid_info()["row"]), 4)
        self.assertEqual(int(zero_btn.grid_info()["column"]), 0)
        self.assertEqual(int(zero_btn.grid_info()["columnspan"]), 2)

        self.assertEqual(int(open_paren_btn.grid_info()["row"]), 0)
        self.assertEqual(int(open_paren_btn.grid_info()["column"]), 0)
        self.assertEqual(int(open_paren_btn.grid_info()["columnspan"]), 2)

        self.assertEqual(int(close_paren_btn.grid_info()["row"]), 0)
        self.assertEqual(int(close_paren_btn.grid_info()["column"]), 2)
        self.assertEqual(int(close_paren_btn.grid_info()["columnspan"]), 2)

        before = (app.bottom_container.winfo_rooty(), zero_btn.winfo_rooty())

        # Type parenthesized expressions across 3, 4, and 5 rows
        with contextlib.redirect_stdout(io.StringIO()):
            for k in "(1+2)+(3+4)+5=":
                app.on_button_click(k)
        self.root.update()
        after = (app.bottom_container.winfo_rooty(), zero_btn.winfo_rooty())

        self.assertEqual(before, after, "Keypad container and 0 button must remain anchored when rows are added")
        self.assertGreaterEqual(len(app.addends), 3)


if __name__ == "__main__":
    unittest.main()
