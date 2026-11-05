"""Regression and functional tests for the Tkinter addition calculator with word chatbot."""

import contextlib
import io
import sys
import tkinter as tk
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
from addition_chat.addition import AdditionCalculator, WordSummerChatbot


class AdditionChatTests(unittest.TestCase):
    def setUp(self):
        try:
            self.root = tk.Tk()
        except tk.TclError as exc:
            self.fail(f"Tkinter requires a graphical desktop: {exc}")
        self.root.withdraw()
        self.calculator = AdditionCalculator(self.root)
        self.root.deiconify()
        self.root.update()

    def tearDown(self):
        self.root.destroy()

    def calculate_inputs(self, *items):
        """items can be either numbers or (number, word) tuples"""
        app = self.calculator
        for index, item in enumerate(items):
            if isinstance(item, tuple):
                num, word = item
            else:
                num, word = item, ""
            if index >= len(app.addends):
                app.add_addend_window()
            app.addends[index] = str(num)
            app.addend_vars[index].set(str(num))
            app.addend_words[index] = str(word)
            app.addend_word_vars[index].set(str(word))

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
        self.assertEqual(self.calculator.result_var.get(), "")
        self.assertEqual(self.calculator.result_word_var.get(), "")


if __name__ == "__main__":
    unittest.main()
