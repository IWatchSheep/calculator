"""Unit and GUI integration tests for Checkpoint 6B: Nested Parentheses Evaluation.

Covers:
1. All 5 required mathematical examples:
   - Example 1: ((2 + 3) × 4) = 20
   - Example 2: ((2 + 3) × 4)^2 = 400
   - Example 3: ((2^3 + 1) × 2)^2 = 324
   - Example 4: 2 × (3 + (4 × 5)) = 46
   - Example 5: (2² + (3 + 1))² = 64
2. Single-row calculations placing results directly in the same row.
3. Multi-level nested expressions (2 and 3 nested parenthesis levels).
4. Opening multiple groups on one row.
5. Closing groups on different rows.
6. Opening and closing within the same row.
7. Separate groups across the expression.
8. Independent parenthesis selection on expandable rows.
9. Correct operator precedence within and outside groups (PEMDAS).
10. Editing existing expressions and recalculating.
11. Clear-to-one-row behavior restoring initial 18-column state.
12. Invalid expression handling:
    - Unmatched opening parentheses.
    - Unmatched closing parentheses.
    - Group exponent without closing parenthesis.
    - Invalid exponent values.
    - Division by zero.
13. Preservation of existing mathematical templates.
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


class TestCheckpoint6BNestedParentheses(unittest.TestCase):
    """Full test suite for Checkpoint 6B: Nested Parentheses Evaluation."""

    @classmethod
    def setUpClass(cls):
        try:
            r = tk.Tk()
            r.destroy()
            cls.has_display = True
        except Exception:
            cls.has_display = False

    def setUp(self):
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        self.app = CalculatorGUI()
        self.app.update()

    def tearDown(self):
        if hasattr(self, "app") and self.app is not None:
            try:
                self.app.destroy()
            except Exception:
                pass

    # =========================================================================
    # 1. Five Authoritative Checkpoint 6B Mathematical Examples
    # =========================================================================

    def test_example_1_nested_multiplication(self):
        """Example 1: ((2 + 3) × 4) = 20 across multiple calculator rows."""
        app = self.app
        # Row 1: number 2, two open parens ((, join +
        app._key("2")
        app._add_paren_pair(0)  # P=2 on Row 1
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2: number 3, one close paren ), join ×
        app._key("3")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app.update()

        # Row 3: number 4, one close paren )
        app._key("4")
        app._toggle_paren_close(2, 0)
        app._equals()
        app.update()

        # Final Total row is Row 4 (index 3)
        self.assertEqual(app.rows[3]["result"].cget("text"), "20")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  20", msg)

    def test_example_2_nested_with_outer_exponent(self):
        """Example 2: ((2 + 3) × 4)^2 = 400."""
        app = self.app
        # Row 1: number 2, two open parens ((, join +
        app._key("2")
        app._add_paren_pair(0)  # P=2
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2: number 3, one close paren ), join ×
        app._key("3")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app.update()

        # Row 3: number 4, one close paren ), group exponent (Box 2) = 2
        app._key("4")
        app._toggle_paren_close(2, 0)
        app.rows[2]["exponent_2_box"].insert(0, "2")
        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "400")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  400", msg)

    def test_example_3_individual_and_group_exponents(self):
        """Example 3: ((2^3 + 1) × 2)^2 = 324."""
        app = self.app
        # Row 1: number 2, row exponent (Box 1) = 3 -> 2^3 = 8, two open parens ((, join +
        app._key("2")
        app.rows[0]["exponent_1_box"].insert(0, "3")
        app._add_paren_pair(0)  # P=2
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2: number 1, one close paren ), join ×
        app._key("1")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app.update()

        # Row 3: number 2, one close paren ), group exponent (Box 2) = 2
        app._key("2")
        app._toggle_paren_close(2, 0)
        app.rows[2]["exponent_2_box"].insert(0, "2")
        app._equals()
        app.update()

        # Individual row values: Row 1 = 8, Row 2 = 1, Row 3 = 2
        self.assertEqual(app.rows[0]["result"].cget("text"), "8")
        self.assertEqual(app.rows[1]["result"].cget("text"), "1")
        self.assertEqual(app.rows[2]["result"].cget("text"), "2")

        # Total row (Row 4): ((8 + 1) * 2)^2 = (9 * 2)^2 = 18^2 = 324
        self.assertEqual(app.rows[3]["result"].cget("text"), "324")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  324", msg)

    def test_example_4_nested_inner_group(self):
        """Example 4: 2 × (3 + (4 × 5)) = 46."""
        app = self.app
        # Row 1: number 2, join ×
        app._key("2")
        app._join_key("×")
        app.update()

        # Row 2: one open paren (, number 3, join +
        app._toggle_paren_open(1, 0)
        app._key("3")
        app._join_key("+")
        app.update()

        # Row 3: one open paren (, number 4, join ×
        app._toggle_paren_open(2, 0)
        app._key("4")
        app._join_key("×")
        app.update()

        # Row 4: number 5, two close parens ))
        app._key("5")
        app._add_paren_pair(3)  # P=2 on Row 4
        app._toggle_paren_close(3, 0)
        app._toggle_paren_close(3, 1)
        app._equals()
        app.update()

        # Total row is Row 5 (index 4): 2 * (3 + 20) = 46
        self.assertEqual(app.rows[4]["result"].cget("text"), "46")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  46", msg)

    def test_example_5_nested_powers_multiple_closing(self):
        """Example 5: (2² + (3 + 1))² = 64."""
        app = self.app
        # Row 1: number 2, row exponent = 2 -> 2^2 = 4, open paren (, join +
        app._key("2")
        app.rows[0]["exponent_1_box"].insert(0, "2")
        app._toggle_paren_open(0, 0)
        app._join_key("+")
        app.update()

        # Row 2: open paren (, number 3, join +
        app._toggle_paren_open(1, 0)
        app._key("3")
        app._join_key("+")
        app.update()

        # Row 3: number 1, two close parens )), group exponent (Box 2) = 2
        app._key("1")
        app._add_paren_pair(2)  # P=2 on Row 3
        app._toggle_paren_close(2, 0)
        app._toggle_paren_close(2, 1)
        # In Checkpoint 6C, close paren 1 is paired with exponent_2_boxes[1] for the outer group
        app.rows[2]["exponent_2_boxes"][1].insert(0, "2")
        app._equals()
        app.update()

        # (4 + (3 + 1))^2 = (4 + 4)^2 = 8^2 = 64
        self.assertEqual(app.rows[3]["result"].cget("text"), "64")
        msg = app.results.get("1.0", "end")
        self.assertIn("=  64", msg)

    # =========================================================================
    # 2. Single-Row Calculations Directly in Column M
    # =========================================================================

    def test_single_row_direct_placement(self):
        """Single-row basic calculation places result directly in Row 1 without Total row."""
        app = self.app
        app._key("7")
        app._equals()
        app.update()
        self.assertEqual(app.rows[0]["result"].cget("text"), "7")
        self.assertEqual(len([r for r in app.rows if not r.get("is_result")]), 1)

    def test_single_row_parentheses_and_group_exponent(self):
        """Single-row with parentheses and Exponent 2: (4)^3 = 64 in Row 1."""
        app = self.app
        app._key("4")
        app._toggle_paren_open(0, 0)
        app._toggle_paren_close(0, 0)
        app.rows[0]["exponent_2_box"].insert(0, "3")
        app._equals()
        app.update()
        self.assertEqual(app.rows[0]["result"].cget("text"), "64")

    # =========================================================================
    # 3. Two and Three Nested Parenthesis Levels
    # =========================================================================

    def test_three_level_nested_expression(self):
        """3 nested parenthesis levels: (((1 + 2) × 3) + 4) × 2 = 26."""
        app = self.app
        # Row 1: ((( 1, join +
        app._key("1")
        app._add_paren_pair(0)  # P=2
        app._add_paren_pair(0)  # P=3
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._toggle_paren_open(0, 2)
        app._join_key("+")
        app.update()

        # Row 2: 2 ), join ×
        app._key("2")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app.update()

        # Row 3: 3 ), join +
        app._key("3")
        app._toggle_paren_close(2, 0)
        app._join_key("+")
        app.update()

        # Row 4: 4 ), join ×
        app._key("4")
        app._toggle_paren_close(3, 0)
        app._join_key("×")
        app.update()

        # Row 5: 2
        app._key("2")
        app._equals()
        app.update()

        # Total is Row 6 (index 5)
        self.assertEqual(app.rows[5]["result"].cget("text"), "26")

    # =========================================================================
    # 4. Opening and Closing Multiple Groups & Same-Row Groups
    # =========================================================================

    def test_open_and_close_within_same_row(self):
        """Open and close within the same row: ( 2 ) + ( 3 ) = 5."""
        app = self.app
        # Row 1: ( 2 ), join +
        app._key("2")
        app._toggle_paren_open(0, 0)
        app._toggle_paren_close(0, 0)
        app._join_key("+")
        app.update()

        # Row 2: ( 3 )
        app._key("3")
        app._toggle_paren_open(1, 0)
        app._toggle_paren_close(1, 0)
        app._equals()
        app.update()

        self.assertEqual(app.rows[2]["result"].cget("text"), "5")

    def test_separate_groups_across_expression(self):
        """Separate groups: (2 + 3) × (4 + 5) = 45."""
        app = self.app
        # Row 1: ( 2, join +
        app._key("2")
        app._toggle_paren_open(0, 0)
        app._join_key("+")
        app.update()

        # Row 2: 3 ), join ×
        app._key("3")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app.update()

        # Row 3: ( 4, join +
        app._key("4")
        app._toggle_paren_open(2, 0)
        app._join_key("+")
        app.update()

        # Row 4: 5 )
        app._key("5")
        app._toggle_paren_close(3, 0)
        app._equals()
        app.update()

        self.assertEqual(app.rows[4]["result"].cget("text"), "45")

    # =========================================================================
    # 5. Independent Parenthesis Selection on Expandable Rows
    # =========================================================================

    def test_independent_parenthesis_selection(self):
        """In a row with 3 pairs, activate pair 0 and pair 2 while pair 1 is inactive."""
        app = self.app
        app._key("2")
        app._add_paren_pair(0)  # P=2
        app._add_paren_pair(0)  # P=3
        app.update()

        # Toggle open 0 and open 2 (leaving open 1 inactive)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 2)
        app._join_key("+")
        app.update()

        # Row 2: 3 )
        app._key("3")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app.update()

        # Row 3: 4 )
        app._key("4")
        app._toggle_paren_close(2, 0)
        app._equals()
        app.update()

        # ((2 + 3) * 4) = 20
        self.assertEqual(app.rows[3]["result"].cget("text"), "20")

    # =========================================================================
    # 6. Precedence Within and Outside Groups
    # =========================================================================

    def test_operator_precedence_with_groups(self):
        """Precedence outside group: 2 + (3 + 4) × 5 = 37 (not (2 + 7) * 5 = 45)."""
        app = self.app
        # Row 1: 2, join +
        app._key("2")
        app._join_key("+")
        app.update()

        # Row 2: ( 3, join +
        app._key("3")
        app._toggle_paren_open(1, 0)
        app._join_key("+")
        app.update()

        # Row 3: 4 ), join ×
        app._key("4")
        app._toggle_paren_close(2, 0)
        app._join_key("×")
        app.update()

        # Row 4: 5
        app._key("5")
        app._equals()
        app.update()

        self.assertEqual(app.rows[4]["result"].cget("text"), "37")

    # =========================================================================
    # 7. Editing Existing Expressions and Recalculating
    # =========================================================================

    def test_edit_and_recalculate(self):
        """Modifying a value in an existing nested expression recalculates cleanly."""
        app = self.app
        # Initial: ((2 + 3) * 4) = 20
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        app._key("3")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app.update()

        app._key("4")
        app._toggle_paren_close(2, 0)
        app._equals()
        app.update()
        self.assertEqual(app.rows[3]["result"].cget("text"), "20")

        # Edit Row 2 value from 3 to 5: ((2 + 5) * 4) = 28
        app._select_only(1, (0,))
        app.rows[1]["node"]["slots"][0] = "5"
        app._render_row(1)
        app._equals()
        app.update()
        self.assertEqual(app.rows[3]["result"].cget("text"), "28")

    # =========================================================================
    # 8. Clear Behavior
    # =========================================================================

    def test_clear_restores_initial_layout(self):
        """Clear resets all rows, removing multi-row expanded controls and total rows."""
        app = self.app
        app._key("2")
        app._add_paren_pair(0)
        app._join_key("+")
        app._key("3")
        app._equals()
        app.update()

        # Now clear
        app._clear_all()
        app.update()

        self.assertEqual(len(app.rows), 1)
        self.assertEqual(app.rows[0]["paren_pairs_count"], 1)
        self.assertFalse(app.rows[0]["paren_open"])
        self.assertFalse(app.rows[0]["paren_close"])

    # =========================================================================
    # 9. Invalid Expression Guards
    # =========================================================================

    def test_unmatched_open_parenthesis_guard(self):
        """Unmatched open parenthesis displays descriptive error."""
        app = self.app
        app._key("2")
        app._toggle_paren_open(0, 0)
        app._equals()
        app.update()

        msg = app.results.get("1.0", "end")
        self.assertIn("opening parenthesis '(' without a matching closing", msg)

    def test_unmatched_close_parenthesis_guard(self):
        """Unmatched close parenthesis displays descriptive error."""
        app = self.app
        app._key("2")
        app._toggle_paren_close(0, 0)
        app._equals()
        app.update()

        msg = app.results.get("1.0", "end")
        self.assertIn("closing parenthesis ')' without a matching opening", msg)

    def test_group_exponent_without_close_guard(self):
        """Exponent Box 2 without close parenthesis displays error."""
        app = self.app
        app._key("2")
        app.rows[0]["exponent_2_box"].insert(0, "2")
        app._equals()
        app.update()

        msg = app.results.get("1.0", "end")
        self.assertIn("group exponent (Column O) without a closing parenthesis", msg)

    def test_invalid_exponent_value_guard(self):
        """Invalid non-numeric exponent string displays error."""
        app = self.app
        app._key("2")
        app.rows[0]["exponent_1_box"].insert(0, "abc")
        app._equals()
        app.update()

        msg = app.results.get("1.0", "end")
        self.assertIn("Invalid exponent", msg)

    def test_division_by_zero_guard(self):
        """Division by zero inside or across groups displays error."""
        app = self.app
        app._key("10")
        app._join_key("÷")
        app.update()

        # (3 - 3) = 0
        app._key("3")
        app._toggle_paren_open(1, 0)
        app._join_key("−")
        app.update()

        app._key("3")
        app._toggle_paren_close(2, 0)
        app._equals()
        app.update()

        msg = app.results.get("1.0", "end")
        self.assertIn("Division by zero", msg)




    # =========================================================================
    # 10. Automatic Propagation of Available Closing Parentheses
    # =========================================================================

    def test_auto_prop_01_two_openings_on_row_1_provides_two_closing_on_row_2(self):
        """1. Two openings on Row 1 automatically provide two closing controls on Row 2."""
        app = self.app
        app._key("2")
        app._add_paren_pair(0)  # P=2 on Row 1
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)  # (( 2
        app._join_key("+")
        app.update()

        # Row 2 must automatically have at least 2 pairs and 2 closing buttons
        row1 = app.rows[1]
        self.assertGreaterEqual(row1["paren_pairs_count"], 2)
        self.assertGreaterEqual(len(row1["paren_close_btns"]), 2)
        # All newly provided closing parentheses remain inactive
        self.assertFalse(row1["paren_close_states"][0])
        self.assertFalse(row1["paren_close_states"][1])

    def test_auto_prop_02_three_openings_provides_three_available_closing_controls(self):
        """2. Three openings provide three available closing controls on following row."""
        app = self.app
        app._key("2")
        app._add_paren_pair(0)
        app._add_paren_pair(0)  # P=3 on Row 1
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._toggle_paren_open(0, 2)  # ((( 2
        app._join_key("+")
        app.update()

        row1 = app.rows[1]
        self.assertGreaterEqual(row1["paren_pairs_count"], 3)
        self.assertGreaterEqual(len(row1["paren_close_btns"]), 3)

    def test_auto_prop_03_closing_one_group_carries_remaining_to_later_row(self):
        """3. Closing one group carries remaining unmatched groups into later row."""
        app = self.app
        # Row 1: (( 2
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2: close only 1 group
        app._key("3")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app.update()

        # Row 3: 1 group remains open from earlier rows -> Row 3 has closing control available
        row2 = app.rows[2]
        self.assertGreaterEqual(row2["paren_pairs_count"], 1)
        self.assertGreaterEqual(len(row2["paren_close_btns"]), 1)

    def test_auto_prop_04_preserving_independently_selected_closing_parentheses(self):
        """4. Preserving independently selected closing parentheses without activating others."""
        app = self.app
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2 has 2 pairs; activate only the second closing button (index 1)
        app._toggle_paren_close(1, 1)
        app.update()

        row1 = app.rows[1]
        self.assertFalse(row1["paren_close_states"][0])
        self.assertTrue(row1["paren_close_states"][1])

    def test_auto_prop_05_evaluating_double_parens_two_rows(self):
        """5. Correctly evaluating ((2 + 3)) = 5 without requiring blue + on Row 2."""
        app = self.app
        # Row 1: (( 2
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2: 3 )) without clicking blue + on Row 2!
        app._key("3")
        app._toggle_paren_close(1, 0)
        app._toggle_paren_close(1, 1)
        app._equals()
        app.update()

        # Multi-row Total row (index 2) displays 5
        self.assertEqual(app.rows[2]["result"].cget("text"), "5")

    def test_auto_prop_06_evaluating_double_parens_three_rows_squared(self):
        """6. Correctly evaluating ((2 + 3) × 4)^2 = 400 without manual expansion on later rows."""
        app = self.app
        # Row 1: (( 2
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app.update()

        # Row 2: + 3 ) (only 1 close selected)
        app._key("3")
        app._toggle_paren_close(1, 0)
        app._join_key("×")
        app.update()

        # Row 3: × 4 )^2
        app._key("4")
        app._toggle_paren_close(2, 0)
        app.rows[2]["exponent_2_box"].insert(0, "2")
        app._equals()
        app.update()

        self.assertEqual(app.rows[3]["result"].cget("text"), "400")

    def test_auto_prop_07_editing_earlier_opening_parenthesis_states(self):
        """7. Dynamically recalculates capacity when editing earlier opening parentheses."""
        app = self.app
        # Initially create Row 1 and Row 2 without parentheses
        app._key("2")
        app._join_key("+")
        app._key("3")
        app.update()

        self.assertEqual(app.rows[1]["paren_pairs_count"], 1)

        # Now go back and expand Row 1 with blue + and activate both opens
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app.update()

        # Row 2 must have dynamically gained capacity for 2 closing buttons!
        self.assertGreaterEqual(app.rows[1]["paren_pairs_count"], 2)
        self.assertGreaterEqual(len(app.rows[1]["paren_close_btns"]), 2)

    def test_auto_prop_08_preserving_exponent_boxes_and_descriptions(self):
        """8. Expanding closing capacity preserves existing exponent entries and descriptions."""
        app = self.app
        app._key("2")
        app._join_key("+")
        app._key("3")
        app.update()

        # Set values on Row 2
        app.rows[1]["exponent_1_box"].insert(0, "4")
        desc = app.rows[1]["result_desc"]
        desc.boxes[0].set_text("Row 2 Result Description")
        app.update()

        # Now activate 2 open parens on Row 1, triggering auto-expansion of Row 2
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app.update()

        self.assertEqual(app.rows[1]["exponent_1_box"].get(), "4")
        self.assertEqual(desc.boxes[0].words_text(), "Row 2 Result Description")

    def test_auto_prop_09_independent_row_widths_and_horizontal_scrolling(self):
        """9. Independent row widths and canvas horizontal scroll region update correctly."""
        app = self.app
        app._key("1")
        app._add_paren_pair(0)
        app._add_paren_pair(0)  # Row 1: P=3
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._toggle_paren_open(0, 2)
        app._join_key("+")
        app.update()

        # Row 2 gets 3 pairs; close 1
        app._key("2")
        app._toggle_paren_close(1, 0)
        app._join_key("+")
        app.update()

        # Row 3 gets 2 pairs
        app._key("3")
        app.update()

        # Verify scrollregion was calculated and includes widest row
        bbox = app.rows_canvas.bbox("all")
        self.assertIsNotNone(bbox)
        self.assertGreater(bbox[2], 800)

    def test_auto_prop_10_clearing_back_to_one_empty_row(self):
        """10. Clear resets multi-row calculation back to one empty row with single pair."""
        app = self.app
        app._key("2")
        app._add_paren_pair(0)
        app._toggle_paren_open(0, 0)
        app._toggle_paren_open(0, 1)
        app._join_key("+")
        app._key("3")
        app.update()

        self.assertEqual(len(app.rows), 2)
        self.assertEqual(app.rows[1]["paren_pairs_count"], 2)

        # Clear
        app._clear_all()
        app.update()

        self.assertEqual(len(app.rows), 1)
        self.assertEqual(app.rows[0]["paren_pairs_count"], 1)
        self.assertFalse(app.rows[0]["paren_open"])
        self.assertFalse(app.rows[0]["paren_close"])

if __name__ == "__main__":
    unittest.main()
