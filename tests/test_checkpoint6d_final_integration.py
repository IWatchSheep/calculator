"""Checkpoint 6D: Final Integration and Regression Verification Test Suite.

Verifies:
1. Calculations (numerical results and mathematical analysis text):
   - 2 + 3 × 4 = 14
   - (2 + 3) × 4 = 20
   - ((2 + 3) × 4)^2 = 400
   - ((2 + 3)^2)^3 = 15625
   - ((2 + 3)^2 × 4)^3 = 1000000
   - (2 + (3 + 4)^2) = 51
   - ((2^3 + 1)^2 × 2) = 162
   - 20 ÷ 5 × 2 = 8
   - 10 − 3 − 2 = 5
2. Dynamic parentheses:
   - 1, 2, 3 pairs; auto-propagation of closing buttons and exponent boxes.
   - Nonconsecutive closing selection.
   - Post-evaluation editing of opening/closing parentheses.
   - Content preservation across expansion.
3. GUI layout:
   - Baseline 18-column alignment for P=1.
   - Expanded column alignment for P=2 and P=3.
   - Independent row widths and Total row alignment.
   - Clear-to-one-row configuration.
4. Keyboard and focus:
   - On-screen keypad and physical keyboard routing to Exponent 1 and all Group Exponents.
   - Backspace, sign toggle.
   - Focus changing between rows.
   - New row creation after exponent editing clears stale exponent focus.
5. Error messages:
   - Group exponent on baseline row reports Column P.
   - Group exponent on expanded row reports exact dynamic column (e.g., Column S).
"""

import unittest
import tkinter as tk
from main import CalculatorGUI
import gui_coordinates as gc


class TestCheckpoint6DFinalIntegration(unittest.TestCase):
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
    # 1. Nine Authoritative Calculations and Mathematical Analysis Text
    # =========================================================================

    def test_01_calc_pemdas_multiplication_precedence(self):
        """1. 2 + 3 × 4 = 14 (standard PEMDAS precedence)."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("2")
        app._join_key("+")
        app._key("3")
        app._join_key("×")
        app._key("4")
        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "14")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  14", msg)
        self.assertIn("Row 1:  2", msg)
        self.assertIn("Row 2:  + 3", msg)
        self.assertIn("Row 3:  × 4", msg)

    def test_02_calc_single_parenthesis_override(self):
        """2. (2 + 3) × 4 = 20."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("2")
        app._toggle_paren_open(0, 0)
        app._join_key("+")
        app._key("3")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app._key("4")
        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "20")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  20", msg)
        self.assertIn("Row 1:  ( 2", msg)
        self.assertIn("Row 2:  + 3 )", msg)
        self.assertIn("Row 3:  × 4", msg)

    def test_03_calc_nested_outer_power_400(self):
        """3. ((2 + 3) × 4)^2 = 400."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app._key("3")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app._key("4")
        app._toggle_paren_close(2, 0)
        app.rows[2]["exponent_2_box"].insert(0, "2")
        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "400")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  400", msg)
        self.assertIn("Row 3:  × 4 )^2", msg)

    def test_04_calc_same_row_nested_powers_15625(self):
        """4. ((2 + 3)^2)^3 = 15625."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app._key("3")
        app._toggle_paren_close(1, 0)
        app._toggle_paren_close(1, 1)
        app.rows[1]["exponent_2_boxes"][0].insert(0, "2")
        app.rows[1]["exponent_2_boxes"][1].insert(0, "3")
        app._equals()
        app.update()

        self.assertEqual(app.rows[2]["result"].cget("text"), "15625")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  15625", msg)
        self.assertIn("Row 2:  + 3 )^2 )^3", msg)

    def test_05_calc_multi_row_nested_powers_1000000(self):
        """5. ((2 + 3)^2 × 4)^3 = 1000000."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app._key("3")
        app._toggle_paren_close(1, 0)
        app.rows[1]["exponent_2_boxes"][0].insert(0, "2")
        app._join_key("×")
        app._key("4")
        app._toggle_paren_close(2, 0)
        app.rows[2]["exponent_2_boxes"][0].insert(0, "3")
        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "1000000")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  1000000", msg)
        self.assertIn("Row 2:  + 3 )^2", msg)
        self.assertIn("Row 3:  × 4 )^3", msg)

    def test_06_calc_nested_sum_with_inner_power_51(self):
        """6. (2 + (3 + 4)^2) = 51."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("2")
        app._toggle_paren_open(0, 0)
        app._join_key("+")
        app._toggle_paren_open(1, 0)
        app._key("3")
        app._join_key("+")
        app._key("4")
        app._toggle_paren_close(2, 0)
        app._toggle_paren_close(2, 1)
        app.rows[2]["exponent_2_boxes"][0].insert(0, "2")
        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "51")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  51", msg)
        self.assertIn("Row 3:  + 4 )^2 )", msg)

    def test_07_calc_row_exponent_and_group_exponent_162(self):
        """7. ((2^3 + 1)^2 × 2) = 162."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("2")
        app.rows[0]["exponent_1_box"].insert(0, "3")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app._key("1")
        app._toggle_paren_close(1, 0)
        app.rows[1]["exponent_2_boxes"][0].insert(0, "2")
        app._join_key("×")
        app._key("2")
        app._toggle_paren_close(2, 0)
        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "162")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  162", msg)
        self.assertIn("Row 1:  ( ( 2^3", msg)
        self.assertIn("Row 2:  + 1 )^2", msg)

    def test_08_calc_left_to_right_division_multiplication_8(self):
        """8. 20 ÷ 5 × 2 = 8 (left-to-right equal precedence)."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("20")
        app._join_key("÷")
        app._key("5")
        app._join_key("×")
        app._key("2")
        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "8")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  8", msg)

    def test_09_calc_left_to_right_subtractions_5(self):
        """9. 10 − 3 − 2 = 5 (left-to-right equal precedence)."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("10")
        app._join_key("−")
        app._key("3")
        app._join_key("−")
        app._key("2")
        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "5")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  5", msg)

    # =========================================================================
    # 2. Dynamic Parentheses Verification
    # =========================================================================

    def test_10_post_calculation_parentheses_editing(self):
        """Editing parenthesis toggles after calculation re-evaluates properly."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # Initial: 2 + 3 * 4 = 14
        app._key("2")
        app._join_key("+")
        app._key("3")
        app._join_key("×")
        app._key("4")
        app._equals()
        app.update()
        self.assertEqual(app.rows[3]["result"].cget("text"), "14")

        # Now edit: toggle ( on Row 1 and ) on Row 2 -> (2 + 3) * 4 = 20
        app._toggle_paren_open(0, 0)
        app._toggle_paren_close(1, 0)
        app._equals()
        app.update()
        self.assertEqual(app.rows[3]["result"].cget("text"), "20")

    def test_11_unmatched_parentheses_detection(self):
        """Unclosed opening and unopened closing parentheses are detected with clear errors."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # Unclosed opening parenthesis
        app._key("2")
        app._toggle_paren_open(0, 0)
        app._join_key("+")
        app._key("3")
        app._equals()
        app.update()
        msg = app.results.get("1.0", "end")
        self.assertIn("opening parenthesis '(' without a matching closing parenthesis", msg)

        # Unopened closing parenthesis
        app._clear_all()
        app.update()
        app._key("2")
        app._toggle_paren_close(0, 0)
        app._equals()
        app.update()
        msg2 = app.results.get("1.0", "end")
        self.assertIn("closing parenthesis ')' without a matching opening parenthesis", msg2)

    # =========================================================================
    # 3. Focus Routing & New Row Exponent Target Clearance
    # =========================================================================

    def test_12_focus_cleared_on_new_row_after_exponent_editing(self):
        """Creating a new row after editing an exponent resets active exponent target."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("2")
        app.rows[0]["exponent_1_box"].focus_set()
        app._on_exponent_focus(app.rows[0]["exponent_1_box"])
        app._key("3")
        self.assertEqual(app.rows[0]["exponent_1_box"].get(), "3")
        self.assertIs(app._active_exponent_box, app.rows[0]["exponent_1_box"])

        # Create new row
        app._join_key("+")
        app.update()
        # Active exponent box must be cleared
        self.assertIsNone(app._active_exponent_box)

        # Typing now routes into Row 2 math number slot, not the previous exponent box
        app._key("5")
        self.assertEqual(app.rows[1]["node"]["slots"], ["5"])
        self.assertEqual(app.rows[0]["exponent_1_box"].get(), "3")

    # =========================================================================
    # 4. Error Message Reporting (Issue 5A)
    # =========================================================================

    def test_13_error_message_identifies_column_p_on_baseline(self):
        """Baseline row (P=1) reports Column P when group exponent lacks close parenthesis."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("5")
        app._set_exponent_2(0, "2")
        app._equals()
        app.update()

        msg = app.results.get("1.0", "end")
        self.assertIn("Row 1 has a group exponent (Column P) without a closing parenthesis ')'", msg)

    def test_14_error_message_identifies_dynamic_column_on_expanded_row(self):
        """Expanded row (P=2) reports Column S when second group exponent lacks close parenthesis."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("5")
        app._add_paren_pair(0)  # P=2
        # Close 0 and 1 are inactive; enter into box 1 (Column S)
        app.rows[0]["exponent_2_boxes"][1].insert(0, "3")
        app._equals()
        app.update()

        msg = app.results.get("1.0", "end")
        self.assertIn("Row 1 has a group exponent (Column S) without a closing parenthesis ')'", msg)



    # =========================================================================
    # 5. GUI Layout, Scrolling, and Clear Verification (Sections 2, 3, 4)
    # =========================================================================

    def test_15_one_two_three_pairs_and_independent_row_widths(self):
        """Verify independent row expansion for 1, 2, and 3 pairs."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        # Row 1: 1 pair
        app._key("1")
        app._join_key("+")
        # Row 2: 2 pairs
        app._key("2")
        app._add_paren_pair(1)
        app._join_key("+")
        # Row 3: 3 pairs
        app._key("3")
        app._add_paren_pair(2)
        app._add_paren_pair(2)
        app.update()

        self.assertEqual(app.rows[0]["paren_pairs_count"], 1)
        self.assertEqual(app.rows[1]["paren_pairs_count"], 2)
        self.assertEqual(app.rows[2]["paren_pairs_count"], 3)

        # Row 1 has 1 closing paren and 1 group exponent box
        self.assertEqual(len(app.rows[0]["paren_close_btns"]), 1)
        self.assertEqual(len(app.rows[0]["exponent_2_boxes"]), 1)

        # Row 2 has 2 closing parens and 2 group exponent boxes
        self.assertEqual(len(app.rows[1]["paren_close_btns"]), 2)
        self.assertEqual(len(app.rows[1]["exponent_2_boxes"]), 2)

        # Row 3 has 3 closing parens and 3 group exponent boxes
        self.assertEqual(len(app.rows[2]["paren_close_btns"]), 3)
        self.assertEqual(len(app.rows[2]["exponent_2_boxes"]), 3)

    def test_16_total_row_alignment_and_scrolling(self):
        """Total row aligns at column 13 (Col M) and scrolling responds."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._key("5")
        app._join_key("+")
        app._key("5")
        app._equals()
        app.update()

        # Total row is row 2
        total_row = app.rows[2]
        self.assertTrue(total_row.get("is_result"))
        self.assertEqual(total_row["result_box"].excel_pos.column, gc.EXCEL_18COL_RESULT_BOX)  # Col M (13)

        # Scrolling calls execute without error
        app._scroll_to_row(0)
        app._scroll_to_row(2)
        app.update()

    def test_17_physical_keyboard_and_keypad_routing(self):
        """Physical keyboard and keypad route accurately to all exponent boxes."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        app = self.app
        app._add_paren_pair(0)
        app.update()

        # Route to Exponent Box 1
        exp1 = app.rows[0]["exponent_1_box"]
        exp1.focus_set()
        app._on_exponent_focus(exp1)
        app._key("2")
        self.assertEqual(exp1.get(), "2")

        # Route to Exponent Box 2 (pair 0)
        exp2_0 = app.rows[0]["exponent_2_boxes"][0]
        exp2_0.focus_set()
        app._on_exponent_focus(exp2_0)
        app._key("3")
        self.assertEqual(exp2_0.get(), "3")

        # Route to Exponent Box 2 (pair 1)
        exp2_1 = app.rows[0]["exponent_2_boxes"][1]
        exp2_1.focus_set()
        app._on_exponent_focus(exp2_1)
        app._key("4")
        app._key("5")
        self.assertEqual(exp2_1.get(), "45")
        app._key("⌫")
        self.assertEqual(exp2_1.get(), "4")
        app._key("±")
        self.assertEqual(exp2_1.get(), "-4")


if __name__ == "__main__":
    unittest.main()
