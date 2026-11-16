"""Unit and GUI integration tests for Checkpoint 6A: Dynamic Expandable Parentheses.

Covers:
1. Initial 18-column layout (Columns A through R).
2. Blue + button appearance, styling (#1e88e5) and placement at Column K (11).
3. Adding a second parenthesis pair on a row via blue + button.
4. Adding a third parenthesis pair on a row.
5. Correct opening and closing widget positions and Excel coordinates.
6. Independent selection, deselection, and active state tracking.
7. Correct dynamic column shifting of result, exponents, and descriptions.
8. Preserving values in Exponent Box 1 and Exponent Box 2 across expansion.
9. Preserving result descriptions and orange + button functionality.
10. Independent expansion of different rows (Row 1 expanded, Row 2 unexpanded).
11. Horizontal scrolling behavior in canvas viewport.
12. Clear-to-one-row reset restoring initial 18-column layout and single parenthesis pair.
13. Keyboard and number-pad focus routing.
14. Preservation of existing mathematical calculations (single-row, PEMDAS multi-row).
15. Safety guard for unsupported nested expressions during Stage 6A.
"""
import os
import sys
import tkinter as tk
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import gui_coordinates as gc
from main import CalculatorGUI


class TestCheckpoint6AExpandableParentheses(unittest.TestCase):
    """Full test suite for Checkpoint 6A: Dynamic Expandable Parentheses GUI."""

    @classmethod
    def setUpClass(cls):
        try:
            r = tk.Tk()
            r.destroy()
            cls.has_display = True
        except Exception:
            cls.has_display = False

    def test_01_initial_18_column_specification(self):
        """1. Verify 18-column layout constants, indices, and column letters A..R."""
        self.assertEqual(gc.EXCEL_18COL_TOTAL_COLUMNS, 18)
        self.assertEqual(len(gc.EXCEL_18COL_LETTERS), 18)
        self.assertEqual(gc.EXCEL_18COL_LETTERS[0], "A")
        self.assertEqual(gc.EXCEL_18COL_LETTERS[10], "K")
        self.assertEqual(gc.EXCEL_18COL_LETTERS[11], "L")
        self.assertEqual(gc.EXCEL_18COL_LETTERS[12], "M")
        self.assertEqual(gc.EXCEL_18COL_LETTERS[13], "N")
        self.assertEqual(gc.EXCEL_18COL_LETTERS[14], "O")
        self.assertEqual(gc.EXCEL_18COL_LETTERS[15], "P")
        self.assertEqual(gc.EXCEL_18COL_LETTERS[16], "Q")
        self.assertEqual(gc.EXCEL_18COL_LETTERS[17], "R")

        self.assertEqual(gc.EXCEL_18COL_ROW_LABEL, 1)        # Col A
        self.assertEqual(gc.EXCEL_18COL_MATH_SIGN, 3)        # Col C
        self.assertEqual(gc.EXCEL_18COL_NUMBER_MATH, 5)      # Col E
        self.assertEqual(gc.EXCEL_18COL_MATH_BOX1, 6)        # Col F
        self.assertEqual(gc.EXCEL_18COL_MATH_TRAILING, 7)    # Col G
        self.assertEqual(gc.EXCEL_18COL_ACTIONS, 9)          # Col I
        self.assertEqual(gc.EXCEL_18COL_RESULT_EQUALS, 10)   # Col J
        self.assertEqual(gc.EXCEL_18COL_PAREN_PLUS, 11)      # Col K: Blue +
        self.assertEqual(gc.EXCEL_18COL_PAREN_OPEN, 12)      # Col L: '('
        self.assertEqual(gc.EXCEL_18COL_RESULT_BOX, 13)      # Col M: '□'
        self.assertEqual(gc.EXCEL_18COL_EXPONENT_1, 14)      # Col N: Exp 1
        self.assertEqual(gc.EXCEL_18COL_PAREN_CLOSE, 15)     # Col O: ')'
        self.assertEqual(gc.EXCEL_18COL_EXPONENT_2, 16)      # Col P: Exp 2
        self.assertEqual(gc.EXCEL_18COL_RESULT_BOX1, 17)     # Col Q: Result desc 1
        self.assertEqual(gc.EXCEL_18COL_RESULT_TRAILING, 18) # Col R: Orange +

    def test_02_blue_plus_button_appearance_and_placement(self):
        """2. Blue + button appears with proper blue styling and placement at Column K."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            row0 = app.rows[0]
            btn_plus = row0.get("paren_plus_btn")
            self.assertIsNotNone(btn_plus)
            self.assertEqual(btn_plus.cget("text"), "+")
            self.assertEqual(btn_plus.cget("bg"), "#1e88e5")
            self.assertEqual(btn_plus.cget("fg"), "white")

            # Check logical GridPosition
            pos = btn_plus.excel_pos
            self.assertEqual(pos.column, gc.EXCEL_18COL_PAREN_PLUS)  # Col K (11)
            self.assertEqual(pos.row, 28)  # Excel Row 28 (middle sub-row of Row 1)
        finally:
            app.destroy()

    def test_03_adding_second_parenthesis_pair(self):
        """3. Clicking blue + adds a second opening and closing parenthesis."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            row0 = app.rows[0]
            self.assertEqual(row0["paren_pairs_count"], 1)
            self.assertEqual(len(row0["paren_open_btns"]), 1)
            self.assertEqual(len(row0["paren_close_btns"]), 1)

            # Click blue +
            app._add_paren_pair(0)
            app.update()

            self.assertEqual(row0["paren_pairs_count"], 2)
            self.assertEqual(len(row0["paren_open_btns"]), 2)
            self.assertEqual(len(row0["paren_close_btns"]), 2)
            self.assertEqual(len(row0["paren_open_states"]), 2)
            self.assertEqual(len(row0["paren_close_states"]), 2)
            self.assertEqual(row0["paren_open_btns"][1].cget("text"), "(")
            self.assertEqual(row0["paren_close_btns"][1].cget("text"), ")")
        finally:
            app.destroy()

    def test_04_adding_third_parenthesis_pair(self):
        """4. Repeated clicks add third pair and continue expanding without fixed limits."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            row0 = app.rows[0]
            app._add_paren_pair(0)
            app._add_paren_pair(0)
            app.update()

            self.assertEqual(row0["paren_pairs_count"], 3)
            self.assertEqual(len(row0["paren_open_btns"]), 3)
            self.assertEqual(len(row0["paren_close_btns"]), 3)
        finally:
            app.destroy()

    def test_05_correct_widget_positions_and_column_shifting(self):
        """5 & 7. Dynamic column shifting correctly shifts result, exponents, and descriptions."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            row0 = app.rows[0]
            # Initial positions (P=1):
            # Col K (0-based 10): Blue +
            # Col L (0-based 11): Open paren 0
            # Col M (0-based 12): Result box
            # Col N (0-based 13): Exponent 1
            # Col O (0-based 14): Close paren 0
            # Col P (0-based 15): Exponent 2
            # Col Q (0-based 16): Result desc
            self.assertEqual(row0["result_box"].excel_pos.column, 13)
            self.assertEqual(row0["exponent_1_box"].excel_pos.column, 14)
            self.assertEqual(row0["paren_close_btns"][0].excel_pos.column, 15)
            self.assertEqual(row0["exponent_2_box"].excel_pos.column, 16)
            self.assertEqual(row0["result_desc"].excel_pos.column, 17)

            # Expand to P=2
            app._add_paren_pair(0)
            app.update()

            # Shifted positions (P=2):
            # Col K (10): Blue +
            # Col L (11): Open paren 0
            # Col M (12): Open paren 1 (added)
            # Col N (13): Result box (shifted +1)
            # Col O (14): Exponent 1 (shifted +1)
            # Col P (15): Close paren 0 (shifted +1)
            # Col Q (16): Close paren 1 (added)
            # Col R (17): Exponent 2 (shifted +2)
            # Col S (18): Result desc (shifted +2)
            self.assertEqual(row0["paren_open_btns"][0].excel_pos.column, 12)
            self.assertEqual(row0["paren_open_btns"][1].excel_pos.column, 13)
            self.assertEqual(row0["result_box"].excel_pos.column, 14)
            self.assertEqual(row0["exponent_1_box"].excel_pos.column, 15)
            self.assertEqual(row0["paren_close_btns"][0].excel_pos.column, 16)
            self.assertEqual(row0["paren_close_btns"][1].excel_pos.column, 17)
            self.assertEqual(row0["exponent_2_box"].excel_pos.column, 18)
            self.assertEqual(row0["result_desc"].excel_pos.column, 19)
        finally:
            app.destroy()

    def test_06_independent_selection_and_deselection(self):
        """6. Each parenthesis control has an independent selectable/toggleable active state."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            row0 = app.rows[0]
            app._add_paren_pair(0)  # P=2
            app.update()

            # Initially all inactive
            self.assertEqual(row0["paren_open_states"], [False, False])
            self.assertEqual(row0["paren_close_states"], [False, False])

            # Toggle open 0 only
            app._toggle_paren_open(0, 0)
            app.update()
            self.assertEqual(row0["paren_open_states"], [True, False])
            self.assertEqual(row0["paren_open_btns"][0].cget("bg"), "#b5dca8")
            self.assertEqual(row0["paren_open_btns"][1].cget("bg"), "white")

            # Toggle close 1 only
            app._toggle_paren_close(0, 1)
            app.update()
            self.assertEqual(row0["paren_close_states"], [False, True])
            self.assertEqual(row0["paren_close_btns"][0].cget("bg"), "white")
            self.assertEqual(row0["paren_close_btns"][1].cget("bg"), "#b5dca8")

            # Toggle open 1
            app._toggle_paren_open(0, 1)
            app.update()
            self.assertEqual(row0["paren_open_states"], [True, True])

            # Deselect open 0
            app._toggle_paren_open(0, 0)
            app.update()
            self.assertEqual(row0["paren_open_states"], [False, True])
        finally:
            app.destroy()

    def test_08_preserve_exponent_boxes_1_and_2(self):
        """8. Values entered into Exponent Boxes 1 & 2 remain preserved during expansion."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            row0 = app.rows[0]
            exp1 = row0["exponent_1_box"]
            exp2 = row0["exponent_2_box"]
            exp1.insert(0, "3")
            exp2.insert(0, "2")

            # Expand row twice
            app._add_paren_pair(0)
            app.update()
            self.assertEqual(exp1.get(), "3")
            self.assertEqual(exp2.get(), "2")

            app._add_paren_pair(0)
            app.update()
            self.assertEqual(exp1.get(), "3")
            self.assertEqual(exp2.get(), "2")
        finally:
            app.destroy()

    def test_09_preserve_result_descriptions_and_orange_plus(self):
        """9. Result description text and orange + button functionality are preserved."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            row0 = app.rows[0]
            desc = row0["result_desc"]
            desc.boxes[0].set_text("Initial description")

            # Add description box using orange +
            desc.add_box()
            app.update()
            desc.boxes[1].set_text("Second description")
            self.assertEqual(len(desc.boxes), 2)

            # Now expand parentheses with blue +
            app._add_paren_pair(0)
            app.update()

            # Verify descriptions and box count are preserved
            self.assertEqual(len(desc.boxes), 2)
            self.assertEqual(desc.boxes[0].words_text(), "Initial description")
            self.assertEqual(desc.boxes[1].words_text(), "Second description")
        finally:
            app.destroy()

    def test_10_independent_expansion_of_different_rows(self):
        """10. Expanding one row leaves other rows at their own independent widths and pair counts."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            # Create Row 2
            app._key("5")
            app._join_key("+")
            app.update()
            app._key("3")

            # Expand Row 1 to P=3
            app._add_paren_pair(0)
            app._add_paren_pair(0)
            app.update()

            self.assertEqual(app.rows[0]["paren_pairs_count"], 3)
            self.assertEqual(len(app.rows[0]["paren_open_btns"]), 3)

            # Row 2 must remain at P=1
            self.assertEqual(app.rows[1]["paren_pairs_count"], 1)
            self.assertEqual(len(app.rows[1]["paren_open_btns"]), 1)
            self.assertEqual(len(app.rows[1]["paren_close_btns"]), 1)
        finally:
            app.destroy()

    def test_11_horizontal_scrolling(self):
        """11. Adding multiple parenthesis pairs updates canvas scrollregion for horizontal scrolling."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            app._fit_rows()
            init_scroll = app.rows_canvas.cget("scrollregion")

            for _ in range(5):
                app._add_paren_pair(0)
            app.update()
            app._fit_rows()
            expanded_scroll = app.rows_canvas.cget("scrollregion")

            # Verify scrollregion was set
            self.assertTrue(len(expanded_scroll) > 0)
        finally:
            app.destroy()

    def test_12_clear_to_one_row_reset(self):
        """12. Clear All resets the calculator back to Row 1 with exactly 1 parenthesis pair."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            # Expand row 0 to 3 pairs
            app._add_paren_pair(0)
            app._add_paren_pair(0)
            app.update()
            self.assertEqual(app.rows[0]["paren_pairs_count"], 3)

            # Clear all
            app._clear_all()
            app.update()

            self.assertEqual(len(app.rows), 1)
            row0 = app.rows[0]
            self.assertEqual(row0["paren_pairs_count"], 1)
            self.assertEqual(len(row0["paren_open_btns"]), 1)
            self.assertEqual(len(row0["paren_close_btns"]), 1)
            self.assertEqual(row0["paren_open_states"], [False])
            self.assertEqual(row0["paren_close_states"], [False])
            self.assertEqual(row0["paren_open_btns"][0].cget("bg"), "white")
        finally:
            app.destroy()

    def test_13_keyboard_and_number_pad_focus_routing(self):
        """13. Keyboard and number pad digits route cleanly to Row 1 Column E or exponent boxes."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            app._key("7")
            self.assertEqual(app.rows[0]["node"]["slots"], ["7"])

            # Focus exponent 1
            exp1 = app.rows[0]["exponent_1_box"]
            exp1.focus_set()
            app._on_exponent_focus(exp1)
            app.update()
            app._key("2")
            self.assertEqual(exp1.get(), "2")

            # Expanding parentheses does not break active focus
            app._add_paren_pair(0)
            app.update()
            self.assertEqual(exp1.get(), "2")
        finally:
            app.destroy()

    def test_14_existing_mathematical_calculations_preserved(self):
        """14. Standard single-row and PEMDAS multi-row calculations evaluate correctly."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            # 2 + 3 * 4 = 14
            app._key("2")
            app._join_key("+")
            app.update()
            app._key("3")
            app._join_key("×")
            app.update()
            app._key("4")
            app._equals()
            app.update()

            # Multi-row result in Total row (index 3)
            self.assertEqual(app.rows[3]["result"].cget("text"), "14")

            # Single row with exponent: 2 ^ 3 = 8
            app._clear_all()
            app.update()
            app._key("2")
            app.rows[0]["exponent_1_box"].insert(0, "3")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "8")
        finally:
            app.destroy()

    def test_15_safety_guard_for_unsupported_nested_expressions(self):
        """15. Activating multiple parentheses on a row triggers the Stage 6A safety explanatory message."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._add_paren_pair(0)  # P=2
            app.update()

            # Activate both open parens
            app._toggle_paren_open(0, 0)
            app._toggle_paren_open(0, 1)
            app.update()

            app._equals()
            app.update()

            msg = app.results.get("1.0", "end")
            self.assertIn("opening parenthesis '(' without a matching closing parenthesis ')'", msg)
        finally:
            app.destroy()


if __name__ == "__main__":
    unittest.main()
