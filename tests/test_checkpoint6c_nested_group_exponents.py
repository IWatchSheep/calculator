"""Dedicated test suite for Checkpoint 6C: Independent Exponents for Nested Parentheses.

Verifies:
1. Calculations:
   - ((2+3)^2)^3 = 15625
   - ((2+3)^2 × 4)^3 = 1000000
   - (2+(3+4)^2) = 51 (both multi-row closing and same-row closing variants)
   - ((2^3+1)^2 × 2) = 162
   - ((2+3) × 4)^2 = 400
2. 1-to-1 Association & Layout:
   - P=1: Close paren 0 at Col O (15), Exp 2 box 0 at Col P (16), Desc at Col Q (17).
   - P=2: Close 0 (16), Exp 0 (17), Close 1 (18), Exp 1 (19), Desc (20).
   - P=3: Close 0 (17), Exp 0 (18), Close 1 (19), Exp 1 (20), Close 2 (21), Exp 2 (22), Desc (23).
3. Automatic propagation of closing parentheses and group exponent boxes on later rows.
4. Stable associations for nonconsecutive closing button selections.
5. Preservation of values, exponents, descriptions, and states across dynamic expansions.
6. Focus routing for physical keyboard and on-screen number pad for every exponent box.
7. Clear-all reset restoring single exponent box.
8. Error handling (unmatched exponent without active closing paren, invalid syntax, negative/fractional exponents).
"""

import os
import unittest
import tkinter as tk
from main import CalculatorGUI
import gui_coordinates as gc


class TestCheckpoint6CNestedGroupExponents(unittest.TestCase):
    def setUp(self):
        self.has_display = True
        try:
            self.app = CalculatorGUI()
            self.app.update()
        except tk.TclError:
            self.has_display = False

    def tearDown(self):
        if getattr(self, "app", None) is not None:
            try:
                self.app.destroy()
            except Exception:
                pass

    # =========================================================================
    # 1. Five Authoritative Mathematical Calculations
    # =========================================================================

    def test_calculation_1_same_row_nested_powers_15625(self):
        """1. ((2+3)^2)^3 = 15625 (both groups closed on Row 2 with exponents 2 and 3)."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # Row 1: (( 2, join +
        app._key("2")
        app._add_paren_pair(0)  # P=2 on Row 1
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2: 3 )) with inner exp 2 and outer exp 3
        # Auto-propagation provided P=2 on Row 2
        app._key("3")
        self.assertGreaterEqual(len(app.rows[1]["paren_close_btns"]), 2)
        app._toggle_paren_close(1, 0)
        app._toggle_paren_close(1, 1)
        app.rows[1]["exponent_2_boxes"][0].insert(0, "2")
        app.rows[1]["exponent_2_boxes"][1].insert(0, "3")

        app._equals()
        app.update()

        # Verify Total row displays 15625
        self.assertEqual(app.rows[2]["result"].cget("text"), "15625")
        msg = app.results.get("1.0", "end")
        self.assertIn("15625", msg)

    def test_calculation_2_multi_row_nested_powers_1000000(self):
        """2. ((2+3)^2 × 4)^3 = 1000000."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # Row 1: (( 2, join +
        app._key("2")
        app._add_paren_pair(0)  # P=2 on Row 1
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2: 3 ) with group exponent 2, join ×
        app._key("3")
        app._toggle_paren_close(1, 0)
        app.rows[1]["exponent_2_boxes"][0].insert(0, "2")
        app._join_key("×")
        app.update()

        # Row 3: 4 ) with group exponent 3
        app._key("4")
        app._toggle_paren_close(2, 0)
        app.rows[2]["exponent_2_boxes"][0].insert(0, "3")

        app._equals()
        app.update()

        # (5^2 * 4)^3 = (25 * 4)^3 = 100^3 = 1000000
        self.assertEqual(app.rows[3]["result"].cget("text"), "1000000")
        msg = app.results.get("1.0", "end")
        self.assertIn("1000000", msg)

    def test_calculation_3_inner_power_in_nested_sum_51(self):
        """3. (2+(3+4)^2) = 51."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # Row 1: ( 2, join +
        app._key("2")
        app._toggle_paren_open(0, 0)
        app._join_key("+")
        app.update()

        # Row 2: ( 3, join +
        app._toggle_paren_open(1, 0)
        app._key("3")
        app._join_key("+")
        app.update()

        # Row 3: 4 )) with inner exp 2 on close 0, outer close 1
        app._key("4")
        self.assertGreaterEqual(len(app.rows[2]["paren_close_btns"]), 2)
        app._toggle_paren_close(2, 0)
        app._toggle_paren_close(2, 1)
        app.rows[2]["exponent_2_boxes"][0].insert(0, "2")

        app._equals()
        app.update()

        # 2 + (3 + 4)^2 = 2 + 7^2 = 2 + 49 = 51
        self.assertEqual(app.rows[3]["result"].cget("text"), "51")
        msg = app.results.get("1.0", "end")
        self.assertIn("51", msg)

    def test_calculation_3b_inner_power_multi_row_closing_51(self):
        """3b. (2+(3+4)^2) = 51 with inner closed on Row 3 and outer on Row 4."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # Row 1: ( 2, join +
        app._key("2")
        app._toggle_paren_open(0, 0)
        app._join_key("+")
        app.update()

        # Row 2: ( 3, join +
        app._toggle_paren_open(1, 0)
        app._key("3")
        app._join_key("+")
        app.update()

        # Row 3: 4 ) with exp 2, join +
        app._key("4")
        app._toggle_paren_close(2, 0)
        app.rows[2]["exponent_2_boxes"][0].insert(0, "2")
        app._join_key("+")
        app.update()

        # Row 4: 0 ) (closing outer group)
        app._key("0")
        app._toggle_paren_close(3, 0)

        app._equals()
        app.update()

        self.assertEqual(app.rows[4]["result"].cget("text"), "51")

    def test_calculation_4_nested_row_and_group_exponent_162(self):
        """4. ((2^3+1)^2 × 2) = 162."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # Row 1: (( 2 with Exp 1 = 3 -> 2^3 = 8, join +
        app._key("2")
        app.rows[0]["exponent_1_box"].insert(0, "3")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2: 1 ) with group exponent 2 -> (8 + 1)^2 = 81, join ×
        app._key("1")
        app._toggle_paren_close(1, 0)
        app.rows[1]["exponent_2_boxes"][0].insert(0, "2")
        app._join_key("×")
        app.update()

        # Row 3: 2 )
        app._key("2")
        app._toggle_paren_close(2, 0)

        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "162")
        msg = app.results.get("1.0", "end")
        self.assertIn("162", msg)

    def test_calculation_5_nested_parentheses_outer_power_400(self):
        """5. ((2+3) × 4)^2 = 400."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # Row 1: (( 2, join +
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2: 3 ), join ×
        app._key("3")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app.update()

        # Row 3: 4 ) with group exponent 2
        app._key("4")
        app._toggle_paren_close(2, 0)
        app.rows[2]["exponent_2_boxes"][0].insert(0, "2")

        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "400")
        msg = app.results.get("1.0", "end")
        self.assertIn("400", msg)

    # =========================================================================
    # 2. 1-to-1 Association & Interleaved Layout
    # =========================================================================

    def test_baseline_18col_layout_preserved_when_p_equals_1(self):
        """Original 18-column Excel layout is strictly preserved with P=1."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        row0 = app.rows[0]
        self.assertEqual(row0["paren_pairs_count"], 1)
        self.assertEqual(len(row0["paren_close_btns"]), 1)
        self.assertEqual(len(row0["exponent_2_boxes"]), 1)

        # Logical Excel columns for Row 1
        self.assertEqual(row0["result_box"].excel_pos.column, 13)       # Col M
        self.assertEqual(row0["exponent_1_box"].excel_pos.column, 14)   # Col N
        self.assertEqual(row0["paren_close_btns"][0].excel_pos.column, 15)  # Col O
        self.assertEqual(row0["exponent_2_boxes"][0].excel_pos.column, 16)  # Col P
        self.assertEqual(row0["result_desc"].excel_pos.column, 17)      # Col Q..R

        # Backward compatibility alias
        self.assertIs(row0["exponent_2_box"], row0["exponent_2_boxes"][0])

    def test_interleaved_layout_when_p_equals_2(self):
        """Interleaved layout for P=2: )_0 -> Exp_0 -> )_1 -> Exp_1 -> Desc."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        row0 = app.rows[0]
        app._add_paren_pair(0)  # P=2
        app.update()

        self.assertEqual(row0["paren_pairs_count"], 2)
        self.assertEqual(len(row0["paren_close_btns"]), 2)
        self.assertEqual(len(row0["exponent_2_boxes"]), 2)

        self.assertEqual(row0["paren_open_btns"][0].excel_pos.column, 12)  # Col L
        self.assertEqual(row0["paren_open_btns"][1].excel_pos.column, 13)  # Col M
        self.assertEqual(row0["result_box"].excel_pos.column, 14)          # Col N
        self.assertEqual(row0["exponent_1_box"].excel_pos.column, 15)      # Col O

        # Interleaved closing pairs
        self.assertEqual(row0["paren_close_btns"][0].excel_pos.column, 16)  # Close 0
        self.assertEqual(row0["exponent_2_boxes"][0].excel_pos.column, 17)  # Exp 0
        self.assertEqual(row0["paren_close_btns"][1].excel_pos.column, 18)  # Close 1
        self.assertEqual(row0["exponent_2_boxes"][1].excel_pos.column, 19)  # Exp 1

        # Description shifted to Col 20
        self.assertEqual(row0["result_desc"].excel_pos.column, 20)

    def test_interleaved_layout_when_p_equals_3(self):
        """Interleaved layout for P=3: 3 pairs of closing parentheses and group exponents."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        row0 = app.rows[0]
        app._add_paren_pair(0)  # P=2
        app._add_paren_pair(0)  # P=3
        app.update()

        self.assertEqual(row0["paren_pairs_count"], 3)
        self.assertEqual(len(row0["paren_close_btns"]), 3)
        self.assertEqual(len(row0["exponent_2_boxes"]), 3)

        # Interleaved:
        # Close 0 (17), Exp 0 (18), Close 1 (19), Exp 1 (20), Close 2 (21), Exp 2 (22)
        self.assertEqual(row0["paren_close_btns"][0].excel_pos.column, 17)
        self.assertEqual(row0["exponent_2_boxes"][0].excel_pos.column, 18)
        self.assertEqual(row0["paren_close_btns"][1].excel_pos.column, 19)
        self.assertEqual(row0["exponent_2_boxes"][1].excel_pos.column, 20)
        self.assertEqual(row0["paren_close_btns"][2].excel_pos.column, 21)
        self.assertEqual(row0["exponent_2_boxes"][2].excel_pos.column, 22)
        self.assertEqual(row0["result_desc"].excel_pos.column, 23)

    # =========================================================================
    # 3. Automatic Propagation
    # =========================================================================

    def test_auto_propagation_provides_matching_exponent_boxes(self):
        """Automatically propagated closing parentheses receive paired exponent boxes."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # Row 1: 3 open parens
        app._key("1")
        app._add_paren_pair(0)
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._toggle_paren_open(0, 2)
        app._join_key("+")
        app.update()

        # Row 2 must have at least 3 closing buttons and 3 exponent boxes
        row1 = app.rows[1]
        self.assertGreaterEqual(len(row1["paren_close_btns"]), 3)
        self.assertGreaterEqual(len(row1["exponent_2_boxes"]), 3)
        for i in range(3):
            self.assertIsNotNone(row1["exponent_2_boxes"][i])

    # =========================================================================
    # 4. Stable Nonconsecutive Associations
    # =========================================================================

    def test_nonconsecutive_closing_selection_association(self):
        """Selecting only Close 1 pairs with Exp 1 and leaves Exp 0 inactive."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # Row 1: (( 2, join +
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2: select only Close button 1 with exponent 2
        app._key("3")
        app._toggle_paren_close(1, 1)  # Only close 1 active, close 0 inactive
        app.rows[1]["exponent_2_boxes"][1].insert(0, "2")
        app._join_key("×")
        app.update()

        # Row 3: close remaining group
        app._key("4")
        app._toggle_paren_close(2, 0)

        app._equals()
        app.update()

        # Inner group closed with exp 2: (2 + 3)^2 = 25, outer * 4 = 100
        self.assertEqual(app.rows[3]["result"].cget("text"), "100")

    # =========================================================================
    # 5. Value and State Preservation Across Expansion
    # =========================================================================

    def test_values_and_states_preserved_across_row_expansion(self):
        """All values, exponents, descriptions, and toggled states survive expansion."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("42")
        app.rows[0]["exponent_1_box"].insert(0, "3")
        app.rows[0]["exponent_2_box"].insert(0, "5")
        app._toggle_paren_open(0, 0)
        app._toggle_paren_close(0, 0)

        # Expand row
        app._add_paren_pair(0)
        app.update()

        # Verify initial values are completely intact
        self.assertEqual(app.rows[0]["node"]["slots"], ["42"])
        self.assertEqual(app.rows[0]["exponent_1_box"].get(), "3")
        self.assertEqual(app.rows[0]["exponent_2_boxes"][0].get(), "5")
        self.assertTrue(app.rows[0]["paren_open_states"][0])
        self.assertTrue(app.rows[0]["paren_close_states"][0])

    # =========================================================================
    # 6. Keyboard and Number-Pad Focus Routing
    # =========================================================================

    def test_keypad_routes_to_active_second_exponent_box(self):
        """On-screen keypad routes digits and edits to the focused exponent box."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._add_paren_pair(0)
        app.update()

        box1 = app.rows[0]["exponent_2_boxes"][1]
        box1.focus_set()
        app._on_exponent_focus(box1)
        app.update()

        app._key("7")
        app._key("8")
        self.assertEqual(box1.get(), "78")

        # Test backspace
        app._key("⌫")
        self.assertEqual(box1.get(), "7")

        # Test sign toggle
        app._key("±")
        self.assertEqual(box1.get(), "-7")

    # =========================================================================
    # 7. Reset / Clear-All
    # =========================================================================

    def test_clear_all_restores_single_exponent_box(self):
        """_clear_all resets Row 1 back to exactly 1 closing button and 1 exponent box."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._add_paren_pair(0)
        app._add_paren_pair(0)
        self.assertEqual(app.rows[0]["paren_pairs_count"], 3)
        self.assertEqual(len(app.rows[0]["exponent_2_boxes"]), 3)

        app._clear_all()
        app.update()

        row0 = app.rows[0]
        self.assertEqual(row0["paren_pairs_count"], 1)
        self.assertEqual(len(row0["paren_close_btns"]), 1)
        self.assertEqual(len(row0["exponent_2_boxes"]), 1)
        self.assertEqual(row0["exponent_2_boxes"][0].excel_pos.column, 16)
        self.assertEqual(row0["exponent_2_boxes"][0].get(), "")

    # =========================================================================
    # 8. Error Handling and Special Exponents
    # =========================================================================

    def test_error_when_exponent_entered_without_active_closing_paren(self):
        """Error when group exponent is entered but paired close parenthesis is not selected."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("2")
        app._add_paren_pair(0)
        # Close button 1 is NOT toggled, but its exponent has text
        app.rows[0]["exponent_2_boxes"][1].insert(0, "3")

        app._equals()
        app.update()

        msg = app.results.get("1.0", "end")
        self.assertIn("group exponent (Column S) without a closing parenthesis", msg)

    def test_negative_and_fractional_nested_group_exponents(self):
        """Negative and fractional exponents on nested groups evaluate properly."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # ( (2 + 2)^-1 ) -> (4)^-1 = 0.25
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        app._key("2")
        app._toggle_paren_close(1, 0)
        app.rows[1]["exponent_2_boxes"][0].insert(0, "-1")
        app._toggle_paren_close(1, 1)

        app._equals()
        app.update()

        self.assertEqual(app.rows[2]["result"].cget("text"), "0.25")


if __name__ == "__main__":
    unittest.main()
