"""Focused unit tests for the common GUI coordinate convention."""
import os
import sys
import tkinter as tk
import unittest
from dataclasses import FrozenInstanceError

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from gui_coordinates import (
    ARROW_CENTER_POSITION,
    ARROW_GRID_POSITIONS,
    CARD_9COL_ARROW_GRID_POS,
    CARD_9COL_ARROW_POSITIONS,
    CARD_9COL_CENTER_POS,
    CARD_9COL_CONTEXT_POS,
    CARD_9COL_LABEL_POS,
    CARD_9COL_LEAD_BUTTON_POS,
    CARD_9COL_TRAILING_BUTTON_POS,
    CARD_CENTER_POSITION,
    CARD_ARROW_GRID_POSITION,
    CARD_COMPONENT_POSITIONS,
    CARD_CONTEXT_POSITION,
    CARD_LABEL_POSITION,
    CARD_LEAD_BUTTON_POSITION,
    CARD_TRAILING_BUTTON_POSITION,
    MAIN_ROW_ALIASES,
    MAIN_ROW_COLUMNS,
    ROW_1_HELPER_SLOT_POS,
    ROW_1_MATH_ACTIONS_POS,
    ROW_1_MATH_EXPRESSION_POS,
    ROW_1_RESULT_CARD_POS,
    ROW_1_ROW_LABEL_POS,
    ROW_2_HELPER_SLOT_POS,
    ROW_2_MATH_ACTIONS_POS,
    ROW_2_MATH_EXPRESSION_POS,
    ROW_2_RESULT_CARD_POS,
    ROW_2_ROW_LABEL_POS,
    GridPosition,
    LayoutRegion,
    arrow_at_position,
    card_component_position,
    card_to_excel_position,
    excel_to_card_position,
    main_row_position,
    main_row_positions,
    EXCEL_TOTAL_COLUMNS,
    EXCEL_INITIAL_TOTAL_ROWS,
    EXCEL_ROWS_PER_CALCULATOR_ROW,
    EXCEL_CALCULATOR_ROW_STRIDE,
    EXCEL_COL_ROW_LABEL,
    EXCEL_COL_ACTIONS,
    EXCEL_COL_SLOT1_START,
    EXCEL_COL_SLOT1_END,
    EXCEL_COL_SLOT2_START,
    EXCEL_COL_SLOT2_END,
    EXCEL_COL_SLOT3_START,
    EXCEL_COL_SLOT3_END,
    excel_start_row,
    excel_heading_row,
    excel_spacer_before_heading_row,
    excel_spacer_after_heading_row,
    excel_workspace_position,
    excel_workspace_positions,
)
from gui_style import ARROW_BG, ARROWS, PALE_BLUE
from operator_row_math.row_builder import make_component


class TestGridPositionCoordinates(unittest.TestCase):
    """Test 1-based coordinate rules and basic properties."""

    def test_top_left_cell(self):
        """(1, 1) represents the top-left logical cell."""
        pos = GridPosition(row=1, column=1)
        self.assertEqual(pos.row, 1)
        self.assertEqual(pos.column, 1)
        self.assertEqual(pos.row_span, 1)
        self.assertEqual(pos.column_span, 1)
        self.assertTrue(pos.is_top_left)

        not_top_left_1 = GridPosition(row=1, column=2)
        self.assertFalse(not_top_left_1.is_top_left)
        not_top_left_2 = GridPosition(row=2, column=1)
        self.assertFalse(not_top_left_2.is_top_left)

    def test_moving_right_increases_column_by_one(self):
        """Moving right increases the column by one (or specified steps)."""
        pos = GridPosition(row=1, column=1)
        pos_right = pos.right()
        self.assertEqual(pos_right.row, 1)
        self.assertEqual(pos_right.column, 2)

        pos_right_3 = pos.right(3)
        self.assertEqual(pos_right_3.row, 1)
        self.assertEqual(pos_right_3.column, 4)

    def test_moving_down_increases_row_by_one(self):
        """Moving down increases the row by one (or specified steps)."""
        pos = GridPosition(row=1, column=1)
        pos_down = pos.down()
        self.assertEqual(pos_down.row, 2)
        self.assertEqual(pos_down.column, 1)

        pos_down_4 = pos.down(4)
        self.assertEqual(pos_down_4.row, 5)
        self.assertEqual(pos_down_4.column, 1)

    def test_moving_left_and_up(self):
        """Moving left decreases column; moving up decreases row."""
        pos = GridPosition(row=3, column=4)
        self.assertEqual(pos.left(), GridPosition(row=3, column=3))
        self.assertEqual(pos.left(2), GridPosition(row=3, column=2))
        self.assertEqual(pos.up(), GridPosition(row=2, column=4))
        self.assertEqual(pos.up(2), GridPosition(row=1, column=4))

    def test_moving_before_first_row_or_col_rejected(self):
        """Moving past row 1 or column 1 raises ValueError."""
        pos = GridPosition(row=1, column=1)
        with self.assertRaises(ValueError):
            pos.up()
        with self.assertRaises(ValueError):
            pos.left()
        with self.assertRaises(ValueError):
            pos.move(rows=-1, columns=0)
        with self.assertRaises(ValueError):
            pos.move(rows=0, columns=-1)

    def test_invalid_row_and_column_values_rejected(self):
        """Row and column must be integers >= 1."""
        # Value errors: 0 or negative
        with self.assertRaises(ValueError):
            GridPosition(row=0, column=1)
        with self.assertRaises(ValueError):
            GridPosition(row=1, column=0)
        with self.assertRaises(ValueError):
            GridPosition(row=-1, column=1)
        with self.assertRaises(ValueError):
            GridPosition(row=1, column=-5)

        # Type errors: floats, strings, None, booleans
        for bad_val in [1.5, "1", None, True, False, [1]]:
            with self.assertRaises(TypeError):
                GridPosition(row=bad_val, column=1)
            with self.assertRaises(TypeError):
                GridPosition(row=1, column=bad_val)

    def test_spans_must_be_positive_integers(self):
        """Row span and column span must be integers >= 1."""
        # Valid spans
        pos = GridPosition(row=2, column=3, row_span=2, column_span=4)
        self.assertEqual(pos.row_span, 2)
        self.assertEqual(pos.column_span, 4)
        self.assertEqual(pos.end_row, 3)
        self.assertEqual(pos.end_column, 6)

        # Value errors: <= 0
        with self.assertRaises(ValueError):
            GridPosition(row=1, column=1, row_span=0)
        with self.assertRaises(ValueError):
            GridPosition(row=1, column=1, column_span=0)
        with self.assertRaises(ValueError):
            GridPosition(row=1, column=1, row_span=-2)
        with self.assertRaises(ValueError):
            GridPosition(row=1, column=1, column_span=-1)

        # Type errors: floats, strings, booleans
        for bad_span in [2.5, "2", True, False, None]:
            with self.assertRaises(TypeError):
                GridPosition(row=1, column=1, row_span=bad_span)
            with self.assertRaises(TypeError):
                GridPosition(row=1, column=1, column_span=bad_span)


class TestGridPositionConversions(unittest.TestCase):
    """Test framework-specific zero-based conversion functions."""

    def test_to_zero_based(self):
        """Converts 1-based logical coordinates to 0-based coordinates."""
        top_left = GridPosition(row=1, column=1)
        self.assertEqual(top_left.to_zero_based(), (0, 0))

        cell = GridPosition(row=4, column=7)
        self.assertEqual(cell.to_zero_based(), (3, 6))

    def test_to_zero_based_span(self):
        """Converts to (zero_row, zero_column, row_span, column_span)."""
        pos = GridPosition(row=2, column=3, row_span=3, column_span=2)
        self.assertEqual(pos.to_zero_based_span(), (1, 2, 3, 2))

    def test_to_tkinter_grid(self):
        """Generates Tkinter grid(...) compatible parameter dictionary."""
        pos = GridPosition(row=3, column=5, row_span=2, column_span=4)
        self.assertEqual(
            pos.to_tkinter_grid(),
            {"row": 2, "column": 4, "rowspan": 2, "columnspan": 4},
        )

    def test_from_zero_based(self):
        """Constructs logical GridPosition from 0-based library coordinates."""
        pos = GridPosition.from_zero_based(0, 0)
        self.assertEqual(pos, GridPosition(row=1, column=1))

        pos2 = GridPosition.from_zero_based(2, 5, row_span=2, column_span=3)
        self.assertEqual(pos2, GridPosition(row=3, column=6, row_span=2, column_span=3))

        with self.assertRaises(ValueError):
            GridPosition.from_zero_based(-1, 0)
        with self.assertRaises(ValueError):
            GridPosition.from_zero_based(0, -1)
        with self.assertRaises(ValueError):
            GridPosition.from_zero_based(True, 0)  # bool rejected

    def test_from_tkinter_grid(self):
        """Reconstructs GridPosition from Tkinter grid arguments."""
        grid_kwargs = {"row": 0, "column": 1, "rowspan": 3, "columnspan": 1}
        pos = GridPosition.from_tkinter_grid(grid_kwargs, region=LayoutRegion.CARD_COMPONENT)
        self.assertEqual(pos.row, 1)
        self.assertEqual(pos.column, 2)
        self.assertEqual(pos.row_span, 3)
        self.assertEqual(pos.column_span, 1)
        self.assertEqual(pos.region, LayoutRegion.CARD_COMPONENT)

    def test_roundtrip_conversion(self):
        """Converting to zero-based and back preserves identical coordinates."""
        for r in range(1, 10):
            for c in range(1, 10):
                orig = GridPosition(row=r, column=c, row_span=r % 3 + 1, column_span=c % 2 + 1)
                zr, zc, rs, cs = orig.to_zero_based_span()
                rebuilt = GridPosition.from_zero_based(zr, zc, row_span=rs, column_span=cs)
                self.assertEqual(orig, rebuilt)


class TestLayoutRegionAndImmutability(unittest.TestCase):
    """Test parent containers, immutability, and serialization."""

    def test_immutability(self):
        """GridPosition is a frozen value object and cannot be mutated."""
        pos = GridPosition(row=1, column=1)
        with self.assertRaises(FrozenInstanceError):
            pos.row = 2  # type: ignore

    def test_layout_regions_disambiguation(self):
        """Identical coordinates in different layout regions are distinguished."""
        pos_a = GridPosition(row=1, column=1, region=LayoutRegion.KEYPAD)
        pos_b = GridPosition(row=1, column=1, region=LayoutRegion.ROWS_AREA)
        self.assertNotEqual(pos_a, pos_b)
        self.assertEqual(pos_a.region, LayoutRegion.KEYPAD)
        self.assertEqual(pos_b.region, LayoutRegion.ROWS_AREA)

    def test_overlap_detection(self):
        """Overlaps detected within same region, ignored across different regions."""
        p1 = GridPosition(row=1, column=1, row_span=2, column_span=2, region=LayoutRegion.KEYPAD)
        p2 = GridPosition(row=2, column=2, region=LayoutRegion.KEYPAD)
        p3 = GridPosition(row=3, column=3, region=LayoutRegion.KEYPAD)
        p4 = GridPosition(row=2, column=2, region=LayoutRegion.ROWS_AREA)

        self.assertTrue(p1.overlaps(p2))
        self.assertFalse(p1.overlaps(p3))
        # Different regions never overlap even if cell bounds intersect
        self.assertFalse(p1.overlaps(p4))

    def test_serialization_roundtrip(self):
        """Coordinate can be serialized to dict and reconstructed."""
        pos = GridPosition(row=3, column=5, row_span=2, column_span=3, region=LayoutRegion.TOOLBAR)
        d = pos.to_dict()
        self.assertEqual(d["row"], 3)
        self.assertEqual(d["column"], 5)
        self.assertEqual(d["row_span"], 2)
        self.assertEqual(d["column_span"], 3)
        self.assertEqual(d["region"], "toolbar")

        reconstructed = GridPosition.from_dict(d)
        self.assertEqual(reconstructed.row, pos.row)
        self.assertEqual(reconstructed.column, pos.column)
        self.assertEqual(reconstructed.row_span, pos.row_span)
        self.assertEqual(reconstructed.column_span, pos.column_span)
        self.assertEqual(reconstructed.region, "toolbar")


class TestArrowGridCoordinates(unittest.TestCase):
    """Test directional arrow grid positions, layout mappings, and widget construction."""

    def setUp(self):
        try:
            self.root = tk.Tk()
            self.root.withdraw()
        except tk.TclError:
            self.root = None

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.root = None

    def test_arrow_logical_positions(self):
        """Each arrow occupies the exact 1-based logical position from the layout specification."""
        expected = {
            (1, 1): "↖",
            (1, 2): "↑",
            (1, 3): "↗",
            (2, 1): "←",
            (2, 2): None,  # Center square
            (2, 3): "→",
            (3, 1): "↙",
            (3, 2): "↓",
            (3, 3): "↘",
        }
        for (r, c), sym in expected.items():
            pos = GridPosition(row=r, column=c, region=LayoutRegion.ARROW_GRID)
            self.assertIn(pos, ARROW_GRID_POSITIONS)
            self.assertEqual(ARROW_GRID_POSITIONS[pos], sym)
            self.assertEqual(arrow_at_position(r, c), sym)

        # Backward compatibility with ARROWS 2D array
        for r in range(1, 4):
            for c in range(1, 4):
                self.assertEqual(ARROWS[r - 1][c - 1], expected[(r, c)])

    def test_center_square_in_row_2_column_2(self):
        """The center square occupies row 2, column 2 in the arrow grid."""
        self.assertEqual(ARROW_CENTER_POSITION.row, 2)
        self.assertEqual(ARROW_CENTER_POSITION.column, 2)
        self.assertEqual(ARROW_CENTER_POSITION.region, LayoutRegion.ARROW_GRID)
        self.assertIsNone(ARROW_GRID_POSITIONS[ARROW_CENTER_POSITION])
        self.assertIsNone(arrow_at_position(2, 2))

    def test_all_nine_positions_are_unique(self):
        """All nine positions in the arrow grid are distinct in logical and 0-based coordinates."""
        self.assertEqual(len(ARROW_GRID_POSITIONS), 9)
        positions = list(ARROW_GRID_POSITIONS.keys())
        self.assertEqual(len(set(positions)), 9)

        # Ensure every position is in the ARROW_GRID region
        for pos in positions:
            self.assertEqual(pos.region, LayoutRegion.ARROW_GRID)
            self.assertIn(pos.row, (1, 2, 3))
            self.assertIn(pos.column, (1, 2, 3))

        # Check uniqueness of zero-based conversions
        zero_based = [pos.to_zero_based() for pos in positions]
        self.assertEqual(len(set(zero_based)), 9)

    def test_conversion_to_tkinter_coordinates(self):
        """Coordinate conversion to Tkinter 0-based grid parameters is correct."""
        for pos in ARROW_GRID_POSITIONS:
            tk_grid = pos.to_tkinter_grid()
            self.assertEqual(tk_grid["row"], pos.row - 1)
            self.assertEqual(tk_grid["column"], pos.column - 1)
            self.assertEqual(tk_grid["rowspan"], 1)
            self.assertEqual(tk_grid["columnspan"], 1)

            # Specific known cells
            if pos.row == 1 and pos.column == 1:
                self.assertEqual(tk_grid, {"row": 0, "column": 0, "rowspan": 1, "columnspan": 1})
            elif pos.row == 2 and pos.column == 2:
                self.assertEqual(tk_grid, {"row": 1, "column": 1, "rowspan": 1, "columnspan": 1})
            elif pos.row == 3 and pos.column == 3:
                self.assertEqual(tk_grid, {"row": 2, "column": 2, "rowspan": 1, "columnspan": 1})

    def test_existing_arrow_functionality_and_widget_structure(self):
        """Widget creation preserves center button, arrow styling, callbacks, and dimensions."""
        if self.root is None:
            self.skipTest("Tkinter display not available")

        picked = []
        card = make_component(
            self.root,
            center="□",
            kind="number",
            on_pick=lambda: picked.append(True),
        )

        # Center button is attached and positioned at row 2, column 4 of the card
        self.assertTrue(hasattr(card, "center_btn"))
        self.assertEqual(card.center_btn.grid_pos, CARD_9COL_CENTER_POS)
        info = card.center_btn.grid_info()
        self.assertEqual(int(info["row"]), 1)     # zero-based row 1 = logical row 2
        self.assertEqual(int(info["column"]), 3)  # zero-based column 3 = logical column 4

        # Trigger callback
        card.center_btn.invoke()
        self.assertEqual(picked, [True])

        # Verify all 9 arrow buttons/center exist on card.arrow_buttons
        self.assertTrue(hasattr(card, "arrow_buttons"))
        self.assertEqual(len(card.arrow_buttons), 9)

        for pos, btn_widget in card.arrow_buttons.items():
            btn_info = btn_widget.grid_info()
            self.assertEqual(int(btn_info["row"]), pos.row - 1)
            self.assertEqual(int(btn_info["column"]), pos.column - 1)
            if pos == CARD_9COL_CENTER_POS:
                self.assertEqual(btn_widget.cget("text"), "□")
            else:
                self.assertEqual(btn_widget.cget("text"), CARD_9COL_ARROW_POSITIONS[pos])
                self.assertEqual(btn_widget.cget("relief"), "groove")


class TestCardComponentCoordinates(unittest.TestCase):
    """Test the authoritative 9-column card component layout and widget placement."""

    def setUp(self):
        try:
            self.root = tk.Tk()
            self.root.withdraw()
        except tk.TclError:
            self.root = None

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.root = None

    def test_card_components_logical_coordinates(self):
        """Verify the exact 1-based coordinates and spans for the 9-column card layout."""
        expected = {
            "lead_button": (2, 1, 1, 1),
            "arrow_grid": (1, 3, 3, 3),
            "center_square": (2, 4, 1, 1),
            "label_entry": (2, 6, 1, 1),
            "context_entry": (2, 7, 1, 1),
            "trailing_button": (2, 9, 1, 1),
        }
        for name, (row, col, row_span, col_span) in expected.items():
            pos = CARD_COMPONENT_POSITIONS[name]
            self.assertEqual(pos.row, row)
            self.assertEqual(pos.column, col)
            self.assertEqual(pos.row_span, row_span)
            self.assertEqual(pos.column_span, col_span)
            self.assertEqual(pos.region, LayoutRegion.CARD_COMPONENT)
            self.assertEqual(card_component_position(name), pos)

        # Direct constant checks
        self.assertEqual(CARD_LEAD_BUTTON_POSITION, CARD_9COL_LEAD_BUTTON_POS)
        self.assertEqual(CARD_ARROW_GRID_POSITION, CARD_9COL_ARROW_GRID_POS)
        self.assertEqual(CARD_CENTER_POSITION, CARD_9COL_CENTER_POS)
        self.assertEqual(CARD_LABEL_POSITION, CARD_9COL_LABEL_POS)
        self.assertEqual(CARD_CONTEXT_POSITION, CARD_9COL_CONTEXT_POS)
        self.assertEqual(CARD_TRAILING_BUTTON_POSITION, CARD_9COL_TRAILING_BUTTON_POS)

        # Check friendly aliases
        self.assertEqual(CARD_COMPONENT_POSITIONS["blue_plus"], CARD_LEAD_BUTTON_POSITION)
        self.assertEqual(CARD_COMPONENT_POSITIONS["item_entry"], CARD_LABEL_POSITION)
        self.assertEqual(CARD_COMPONENT_POSITIONS["orange_plus"], CARD_TRAILING_BUTTON_POSITION)
        self.assertEqual(CARD_COMPONENT_POSITIONS["center"], CARD_CENTER_POSITION)

    def test_card_components_are_unique(self):
        """Discrete card components occupy distinct columns with empty spacer columns 2 and 8."""
        positions = [
            CARD_LEAD_BUTTON_POSITION,        # col 1
            CARD_LABEL_POSITION,              # col 6
            CARD_CONTEXT_POSITION,            # col 7
            CARD_TRAILING_BUTTON_POSITION,    # col 9
        ]
        columns = [p.column for p in positions]
        self.assertEqual(columns, [1, 6, 7, 9])
        self.assertEqual(len(set(columns)), 4)

        # Arrow columns are 3, 4, 5
        arrow_cols = {pos.column for pos in CARD_9COL_ARROW_POSITIONS}
        self.assertEqual(arrow_cols, {3, 4, 5})

        # Columns 2 and 8 are spacers and never occupied
        all_cols = set(columns) | arrow_cols
        self.assertNotIn(2, all_cols)
        self.assertNotIn(8, all_cols)
        self.assertEqual(all_cols, {1, 3, 4, 5, 6, 7, 9})

    def test_card_components_tkinter_grid_conversion(self):
        """Verify conversion to Tkinter zero-based grid parameters."""
        expected_tk = {
            "lead_button": {"row": 1, "column": 0, "rowspan": 1, "columnspan": 1},
            "arrow_grid": {"row": 0, "column": 2, "rowspan": 3, "columnspan": 3},
            "center_square": {"row": 1, "column": 3, "rowspan": 1, "columnspan": 1},
            "label_entry": {"row": 1, "column": 5, "rowspan": 1, "columnspan": 1},
            "context_entry": {"row": 1, "column": 6, "rowspan": 1, "columnspan": 1},
            "trailing_button": {"row": 1, "column": 8, "rowspan": 1, "columnspan": 1},
        }
        for name, tk_dict in expected_tk.items():
            pos = CARD_COMPONENT_POSITIONS[name]
            self.assertEqual(pos.to_tkinter_grid(), tk_dict)

    def test_make_component_surrounding_widgets_and_behavior(self):
        """make_component creates and positions all 9-column controls with preserved behavior."""
        if self.root is None:
            self.skipTest("Tkinter display not available")

        picked = []
        card = make_component(
            self.root,
            center="□",
            kind="number",
            lead="+",
            on_pick=lambda: picked.append("picked"),
            card_slot=3,
            calc_row=1,
        )

        # 1. Check card attributes
        self.assertTrue(hasattr(card, "card_controls"))
        self.assertTrue(hasattr(card, "arrow_buttons"))
        self.assertEqual(len(card.arrow_buttons), 9)

        # 2. Check Blue plus / lead button at Card row 2, col 1 (Tkinter row 1, col 0)
        self.assertTrue(hasattr(card, "lead_btn"))
        self.assertEqual(card.lead_btn.grid_pos, CARD_LEAD_BUTTON_POSITION)
        info_lead = card.lead_btn.grid_info()
        self.assertEqual(int(info_lead["row"]), 1)
        self.assertEqual(int(info_lead["column"]), 0)
        self.assertEqual(int(info_lead["rowspan"]), 1)
        self.assertEqual(card.lead_btn.cget("text"), "+")
        card.lead_btn.invoke()
        self.assertIn("picked", picked)

        # 3. Check Center square button at Card row 2, col 4 (Tkinter row 1, col 3)
        self.assertTrue(hasattr(card, "center_btn"))
        self.assertEqual(card.center_btn.grid_pos, CARD_CENTER_POSITION)
        info_center = card.center_btn.grid_info()
        self.assertEqual(int(info_center["row"]), 1)
        self.assertEqual(int(info_center["column"]), 3)
        self.assertEqual(card.center_btn.cget("text"), "□")

        # 4. Check Label placeholder button at Card row 2, col 6 (Tkinter row 1, col 5)
        self.assertTrue(hasattr(card, "label_btn"))
        self.assertEqual(card.label_btn.grid_pos, CARD_LABEL_POSITION)
        info_label = card.label_btn.grid_info()
        self.assertEqual(int(info_label["row"]), 1)
        self.assertEqual(int(info_label["column"]), 5)
        self.assertEqual(int(info_label["rowspan"]), 1)
        self.assertEqual(card.label_btn.cget("text"), "[Item]")

        # 5. Check Context placeholder button at Card row 2, col 7 (Tkinter row 1, col 6)
        self.assertTrue(hasattr(card, "context_btn"))
        self.assertEqual(card.context_btn.grid_pos, CARD_CONTEXT_POSITION)
        info_ctx = card.context_btn.grid_info()
        self.assertEqual(int(info_ctx["row"]), 1)
        self.assertEqual(int(info_ctx["column"]), 6)
        self.assertEqual(int(info_ctx["rowspan"]), 1)
        self.assertEqual(card.context_btn.cget("text"), "[Context]")

        # 6. Check Orange plus / trailing button at Card row 2, col 9 (Tkinter row 1, col 8)
        self.assertTrue(hasattr(card, "trailing_btn"))
        self.assertEqual(card.trailing_btn.grid_pos, CARD_TRAILING_BUTTON_POSITION)
        info_trailing = card.trailing_btn.grid_info()
        self.assertEqual(int(info_trailing["row"]), 1)
        self.assertEqual(int(info_trailing["column"]), 8)
        self.assertEqual(int(info_trailing["rowspan"]), 1)
        self.assertEqual(card.trailing_btn.cget("text"), "+")

        # 7. Check spacer columns (columns 1 and 7 in 0-based Tkinter) are empty
        occupied_cols = {int(w.grid_info()["column"]) for w in card.winfo_children()}
        self.assertNotIn(1, occupied_cols, "Tkinter column 1 (Card spacer 2) must remain empty")
        self.assertNotIn(7, occupied_cols, "Tkinter column 7 (Card spacer 8) must remain empty")

        # 8. Check global Excel coordinate traceability
        excel_center = card.to_excel_coordinate(card.center_btn)
        self.assertEqual(excel_center, GridPosition(row=2, column=28, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(card.to_excel_coordinate(card.lead_btn),
                         GridPosition(row=2, column=25, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(card.to_excel_coordinate(card.trailing_btn),
                         GridPosition(row=2, column=33, region=LayoutRegion.EXCEL_WORKSPACE))

    def test_make_component_with_word_entries(self):
        """make_component creates word_entry widgets at row 2, cols 6 & 7 with working callbacks."""
        if self.root is None:
            self.skipTest("Tkinter display not available")

        changed = []
        focused = []
        card = make_component(
            self.root,
            center="□",
            kind="helper",
            words=("apples", "in the basket"),
            on_words=lambda which, text: changed.append((which, text)),
            on_focus=lambda which: focused.append(which),
            card_slot=1,
            calc_row=2,
        )

        # In helper mode with words:
        self.assertTrue(hasattr(card, "label_box"))
        self.assertTrue(hasattr(card, "context_box"))
        self.assertEqual(card.label_box.grid_pos, CARD_LABEL_POSITION)
        self.assertEqual(card.context_box.grid_pos, CARD_CONTEXT_POSITION)

        info_lbl = card.label_box.grid_info()
        self.assertEqual(int(info_lbl["row"]), 1)
        self.assertEqual(int(info_lbl["column"]), 5)  # Tkinter col 5 = Card col 6
        self.assertEqual(int(info_lbl["rowspan"]), 1)

        info_ctx = card.context_box.grid_info()
        self.assertEqual(int(info_ctx["row"]), 1)
        self.assertEqual(int(info_ctx["column"]), 6)  # Tkinter col 6 = Card col 7
        self.assertEqual(int(info_ctx["rowspan"]), 1)

        self.assertEqual(card.label_box.get(), "apples")
        self.assertEqual(card.context_box.get(), "in the basket")

        # Global Excel traceability for Helper Card in calc_row 2 (rows 7..9, cols 3..11)
        self.assertEqual(card.to_excel_coordinate(card.label_box),
                         GridPosition(row=8, column=8, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(card.to_excel_coordinate(card.context_box),
                         GridPosition(row=8, column=9, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(card.to_excel_coordinate(card.center_btn),
                         GridPosition(row=8, column=6, region=LayoutRegion.EXCEL_WORKSPACE))

    def test_global_coordinate_translation_all_three_slots(self):
        """Verify local 9-column card positions translate to exact global Excel slots."""
        # Slot 1: Helper Card in calc_row 2 -> rows 7..9, cols 3..11
        for local_pos in CARD_9COL_ARROW_POSITIONS:
            g_pos = card_to_excel_position(local_pos, card_slot=1, calc_row=2)
            self.assertEqual(g_pos.region, LayoutRegion.EXCEL_WORKSPACE)
            self.assertEqual(g_pos.row, 7 + local_pos.row - 1)
            self.assertEqual(g_pos.column, 3 + local_pos.column - 1)
            slot, back_local = excel_to_card_position(g_pos)
            self.assertEqual(slot, 1)
            self.assertEqual(back_local, local_pos)

        # Slot 2: Math Expression in calc_row 1 -> rows 1..3, cols 13..21
        for local_pos in CARD_9COL_ARROW_POSITIONS:
            g_pos = card_to_excel_position(local_pos, card_slot=2, calc_row=1)
            self.assertEqual(g_pos.region, LayoutRegion.EXCEL_WORKSPACE)
            self.assertEqual(g_pos.row, 1 + local_pos.row - 1)
            self.assertEqual(g_pos.column, 13 + local_pos.column - 1)
            slot, back_local = excel_to_card_position(g_pos)
            self.assertEqual(slot, 2)
            self.assertEqual(back_local, local_pos)

        # Slot 3: Result Card in calc_row 1 -> rows 1..3, cols 25..33
        for local_pos in CARD_9COL_ARROW_POSITIONS:
            g_pos = card_to_excel_position(local_pos, card_slot=3, calc_row=1)
            self.assertEqual(g_pos.region, LayoutRegion.EXCEL_WORKSPACE)
            self.assertEqual(g_pos.row, 1 + local_pos.row - 1)
            self.assertEqual(g_pos.column, 25 + local_pos.column - 1)
            slot, back_local = excel_to_card_position(g_pos)
            self.assertEqual(slot, 3)
            self.assertEqual(back_local, local_pos)

    def test_card_spacer_columns_configured(self):
        """Spacer columns 2 and 8 are explicitly configured with minimum widths and no widgets."""
        if self.root is None:
            self.skipTest("Tkinter display not available")

        card = make_component(self.root, center="□", kind="number")
        col_info_1 = card.grid_columnconfigure(1)
        col_info_7 = card.grid_columnconfigure(7)
        self.assertGreaterEqual(col_info_1.get("minsize", 0), 8)
        self.assertGreaterEqual(col_info_7.get("minsize", 0), 8)


class TestMainRowCoordinates(unittest.TestCase):
    """Test 1-based coordinates for the main calculator row layout (LayoutRegion.ROWS_AREA)."""

    def setUp(self):
        try:
            self.root = tk.Tk()
            self.root.withdraw()
        except tk.TclError:
            self.root = None

    def tearDown(self):
        if self.root is not None:
            try:
                self.root.destroy()
            except Exception:
                pass
            self.root = None

    def test_main_row_column_definitions(self):
        """Logical columns 1..5 are defined with expected names and order."""
        expected_cols = {
            "row_label": 1,
            "helper_slot": 2,
            "math_expression": 3,
            "math_actions": 4,
            "result_card": 5,
        }
        self.assertEqual(MAIN_ROW_COLUMNS, expected_cols)
        self.assertEqual(len(MAIN_ROW_COLUMNS), 5)

    def test_row_1_and_row_2_named_positions(self):
        """Row 1 and 2 named constants have correct 1-based coordinates in ROWS_AREA."""
        # Row 1
        self.assertEqual(ROW_1_ROW_LABEL_POS, GridPosition(1, 1, region=LayoutRegion.ROWS_AREA))
        self.assertEqual(ROW_1_HELPER_SLOT_POS, GridPosition(1, 2, region=LayoutRegion.ROWS_AREA))
        self.assertEqual(ROW_1_MATH_EXPRESSION_POS, GridPosition(1, 3, region=LayoutRegion.ROWS_AREA))
        self.assertEqual(ROW_1_MATH_ACTIONS_POS, GridPosition(1, 4, region=LayoutRegion.ROWS_AREA))
        self.assertEqual(ROW_1_RESULT_CARD_POS, GridPosition(1, 5, region=LayoutRegion.ROWS_AREA))

        # Row 2
        self.assertEqual(ROW_2_ROW_LABEL_POS, GridPosition(2, 1, region=LayoutRegion.ROWS_AREA))
        self.assertEqual(ROW_2_HELPER_SLOT_POS, GridPosition(2, 2, region=LayoutRegion.ROWS_AREA))
        self.assertEqual(ROW_2_MATH_EXPRESSION_POS, GridPosition(2, 3, region=LayoutRegion.ROWS_AREA))
        self.assertEqual(ROW_2_MATH_ACTIONS_POS, GridPosition(2, 4, region=LayoutRegion.ROWS_AREA))
        self.assertEqual(ROW_2_RESULT_CARD_POS, GridPosition(2, 5, region=LayoutRegion.ROWS_AREA))

    def test_all_five_columns_unique_per_row(self):
        """All 5 columns have distinct coordinates within any given row."""
        for r in (1, 2, 3, 5, 10):
            mapping = main_row_positions(r)
            self.assertEqual(len(mapping), 5)
            cells = list(mapping.values())
            # All row indices match r
            self.assertTrue(all(pos.row == r for pos in cells))
            # Column indices are 1, 2, 3, 4, 5
            cols = [pos.column for pos in cells]
            self.assertEqual(cols, [1, 2, 3, 4, 5])
            # Set of cells has 5 distinct entries
            self.assertEqual(len(set(cells)), 5)

    def test_dynamic_row_scaling(self):
        """main_row_positions supports arbitrary row numbers >= 1."""
        pos_row_42 = main_row_positions(42)
        self.assertEqual(pos_row_42["row_label"], GridPosition(42, 1, region=LayoutRegion.ROWS_AREA))
        self.assertEqual(pos_row_42["result_card"], GridPosition(42, 5, region=LayoutRegion.ROWS_AREA))

        pos_row_100_expr = main_row_position(100, "math_expression")
        self.assertEqual(pos_row_100_expr, GridPosition(100, 3, region=LayoutRegion.ROWS_AREA))

    def test_alias_lookup(self):
        """main_row_position accepts both canonical keys and descriptive aliases."""
        self.assertEqual(main_row_position(1, "row"), ROW_1_ROW_LABEL_POS)
        self.assertEqual(main_row_position(1, "helper"), ROW_1_HELPER_SLOT_POS)
        self.assertEqual(main_row_position(1, "math"), ROW_1_MATH_EXPRESSION_POS)
        self.assertEqual(main_row_position(1, "actions"), ROW_1_MATH_ACTIONS_POS)
        self.assertEqual(main_row_position(1, "result"), ROW_1_RESULT_CARD_POS)

    def test_invalid_main_row_arguments(self):
        """Invalid row numbers or column names raise appropriate exceptions."""
        with self.assertRaises(ValueError):
            main_row_position(0, 1)
        with self.assertRaises(ValueError):
            main_row_position(-1, 1)
        with self.assertRaises(ValueError):
            main_row_position(1, 0)
        with self.assertRaises(ValueError):
            main_row_position(1, 6)
        with self.assertRaises(KeyError):
            main_row_position(1, "nonexistent_column")

    def test_tkinter_grid_conversion(self):
        """to_tkinter_grid converts 1-based logical coords to 0-based Tkinter kwargs."""
        for r in (1, 2, 3):
            mapping = main_row_positions(r)
            expected_tk_row = r - 1
            for idx, key in enumerate(["row_label", "helper_slot", "math_expression", "math_actions", "result_card"]):
                pos = mapping[key]
                tk_dict = pos.to_tkinter_grid()
                self.assertEqual(tk_dict["row"], expected_tk_row)
                self.assertEqual(tk_dict["column"], idx)
                self.assertEqual(tk_dict["rowspan"], 1)
                self.assertEqual(tk_dict["columnspan"], 1)

    def test_region_separation(self):
        """LayoutRegion.ROWS_AREA does not collide with CARD_COMPONENT or ARROW_GRID."""
        self.assertNotEqual(LayoutRegion.ROWS_AREA, LayoutRegion.CARD_COMPONENT)
        self.assertNotEqual(LayoutRegion.ROWS_AREA, LayoutRegion.ARROW_GRID)

        row_pos = GridPosition(1, 1, region=LayoutRegion.ROWS_AREA)
        card_pos = GridPosition(1, 1, region=LayoutRegion.CARD_COMPONENT)
        arrow_pos = GridPosition(1, 1, region=LayoutRegion.ARROW_GRID)

        self.assertNotEqual(row_pos, card_pos)
        self.assertNotEqual(row_pos, arrow_pos)

    def test_live_calculator_gui_row_layout(self):
        """CalculatorGUI instantiates rows with correct GridPosition attachments and Tkinter placements."""
        if self.root is None:
            self.skipTest("Tkinter display not available")

        # Import CalculatorGUI here to test actual application wiring
        from main import CalculatorGUI

        app = None
        try:
            app = CalculatorGUI()
            app.withdraw()  # keep hidden during headless tests

            # CalculatorGUI initializes with 2 rows
            self.assertEqual(len(app.rows), 2)

            for r_idx in range(2):
                row_data = app.rows[r_idx]
                r_num = r_idx + 1

                # Verify attached grid_positions dict
                self.assertIn("grid_positions", row_data)
                positions = row_data["grid_positions"]
                self.assertEqual(positions, main_row_positions(r_num))

                # Verify box (math_expression) in col 2 (0-based)
                self.assertIn("box", row_data)
                box = row_data["box"]
                self.assertTrue(hasattr(box, "grid_pos"))
                self.assertEqual(box.grid_pos, positions["math_expression"])
                b_info = box.grid_info()
                self.assertEqual(int(b_info["row"]), r_idx)
                self.assertEqual(int(b_info["column"]), 2)

                # Verify result card in col 4 (0-based)
                result_card = row_data.get("result_card", row_data["result"].master.master)
                self.assertTrue(hasattr(result_card, "grid_pos"))
                self.assertEqual(result_card.grid_pos, positions["result_card"])
                c_info = result_card.grid_info()
                self.assertEqual(int(c_info["row"]), r_idx)
                self.assertEqual(int(c_info["column"]), 4)

                # Verify row label frame in col 0 (0-based)
                labf = row_data["label_frame"]
                self.assertTrue(hasattr(labf, "grid_pos"))
                self.assertEqual(labf.grid_pos, positions["row_label"])
                l_info = labf.grid_info()
                self.assertEqual(int(l_info["row"]), r_idx)
                self.assertEqual(int(l_info["column"]), 0)

                # Verify actions frame in col 3 (0-based)
                col3 = row_data["actions_frame"]
                self.assertTrue(hasattr(col3, "grid_pos"))
                self.assertEqual(col3.grid_pos, positions["math_actions"])
                a_info = col3.grid_info()
                self.assertEqual(int(a_info["row"]), r_idx)
                self.assertEqual(int(a_info["column"]), 3)

            # Test adding a 3rd row dynamically
            new_r = app._add_row()
            self.assertEqual(new_r, 2)  # 0-indexed row 2 -> Row 3
            self.assertEqual(len(app.rows), 3)

            row_3 = app.rows[2]
            positions_3 = row_3["grid_positions"]
            self.assertEqual(positions_3, main_row_positions(3))

            box_3 = row_3["box"]
            self.assertEqual(box_3.grid_pos, positions_3["math_expression"])
            b3_info = box_3.grid_info()
            self.assertEqual(int(b3_info["row"]), 2)
            self.assertEqual(int(b3_info["column"]), 2)

        finally:
            if app is not None:
                try:
                    app.destroy()
                except Exception:
                    pass


class TestExcelWorkspaceCoordinates(unittest.TestCase):
    """Test the authoritative 9-row x 33-column Excel workspace coordinate specification."""

    def test_region_definition(self):
        """LayoutRegion.EXCEL_WORKSPACE is defined and distinct from other layout regions."""
        self.assertEqual(LayoutRegion.EXCEL_WORKSPACE, "excel_workspace")
        self.assertNotEqual(LayoutRegion.EXCEL_WORKSPACE, LayoutRegion.ROWS_AREA)
        self.assertNotEqual(LayoutRegion.EXCEL_WORKSPACE, LayoutRegion.CARD_COMPONENT)
        self.assertNotEqual(LayoutRegion.EXCEL_WORKSPACE, LayoutRegion.ARROW_GRID)

    def test_global_grid_dimensions(self):
        """Authoritative grid has 33 columns and 9 initial rows with 6-row stride."""
        self.assertEqual(EXCEL_TOTAL_COLUMNS, 33)
        self.assertEqual(EXCEL_INITIAL_TOTAL_ROWS, 9)
        self.assertEqual(EXCEL_ROWS_PER_CALCULATOR_ROW, 3)
        self.assertEqual(EXCEL_CALCULATOR_ROW_STRIDE, 6)

    def test_dynamic_start_row_formula(self):
        """Verify start_row = 6 * (k - 1) + 1 for calculator rows 1 through 4."""
        self.assertEqual(excel_start_row(1), 1)   # Calculator Row 1: Excel rows 1-3
        self.assertEqual(excel_start_row(2), 7)   # Calculator Row 2: Excel rows 7-9
        self.assertEqual(excel_start_row(3), 13)  # Calculator Row 3: Excel rows 13-15
        self.assertEqual(excel_start_row(4), 19)  # Calculator Row 4: Excel rows 19-21

    def test_intervening_heading_and_spacer_rows(self):
        """Verify heading row = 6 * k - 7 and surrounding spacer rows for k >= 2."""
        for k in (2, 3, 4):
            start = excel_start_row(k)
            heading = excel_heading_row(k)
            sp_before = excel_spacer_before_heading_row(k)
            sp_after = excel_spacer_after_heading_row(k)

            # Expected formula: heading = start - 2
            self.assertEqual(heading, start - 2)
            self.assertEqual(sp_before, heading - 1)
            self.assertEqual(sp_after, heading + 1)
            self.assertEqual(sp_after, start - 1)

        # Concrete values for rows 2, 3, 4
        self.assertEqual(excel_heading_row(2), 5)
        self.assertEqual(excel_spacer_before_heading_row(2), 4)
        self.assertEqual(excel_spacer_after_heading_row(2), 6)

        self.assertEqual(excel_heading_row(3), 11)
        self.assertEqual(excel_spacer_before_heading_row(3), 10)
        self.assertEqual(excel_spacer_after_heading_row(3), 12)

        self.assertEqual(excel_heading_row(4), 17)
        self.assertEqual(excel_spacer_before_heading_row(4), 16)
        self.assertEqual(excel_spacer_after_heading_row(4), 18)

    def test_row_1_positions_match_excel_sheet_exactly(self):
        """Verify every control in Calculator Row 1 matches my_excel_sheet.txt cells."""
        # Row 1 label: R1C1 (row_span=3)
        lbl = excel_workspace_position(1, "row_label")
        self.assertEqual((lbl.row, lbl.column, lbl.row_span, lbl.column_span), (1, 1, 3, 1))
        self.assertEqual(lbl.region, LayoutRegion.EXCEL_WORKSPACE)

        # Slot 1: Join note text: R1C3..R1C10 (column_span=8)
        jn = excel_workspace_position(1, "join_note_label")
        self.assertEqual((jn.row, jn.column, jn.row_span, jn.column_span), (1, 3, 1, 8))

        # Slot 1: Join note down arrow canvas: R3C6
        ja = excel_workspace_position(1, "join_note_arrow")
        self.assertEqual((ja.row, ja.column, ja.row_span, ja.column_span), (3, 6, 1, 1))

        # Slot 2 (Math Expression):
        # Lead button: R2C13
        self.assertEqual((excel_workspace_position(1, "math_lead_btn").row,
                          excel_workspace_position(1, "math_lead_btn").column), (2, 13))
        # Arrow grid: cols 15-17, rows 1-3
        self.assertEqual((excel_workspace_position(1, "math_arrow_nw").row,
                          excel_workspace_position(1, "math_arrow_nw").column), (1, 15))
        self.assertEqual((excel_workspace_position(1, "math_arrow_n").row,
                          excel_workspace_position(1, "math_arrow_n").column), (1, 16))
        self.assertEqual((excel_workspace_position(1, "math_arrow_ne").row,
                          excel_workspace_position(1, "math_arrow_ne").column), (1, 17))
        self.assertEqual((excel_workspace_position(1, "math_arrow_w").row,
                          excel_workspace_position(1, "math_arrow_w").column), (2, 15))
        self.assertEqual((excel_workspace_position(1, "math_center").row,
                          excel_workspace_position(1, "math_center").column), (2, 16))
        self.assertEqual((excel_workspace_position(1, "math_arrow_e").row,
                          excel_workspace_position(1, "math_arrow_e").column), (2, 17))
        self.assertEqual((excel_workspace_position(1, "math_arrow_sw").row,
                          excel_workspace_position(1, "math_arrow_sw").column), (3, 15))
        self.assertEqual((excel_workspace_position(1, "math_arrow_s").row,
                          excel_workspace_position(1, "math_arrow_s").column), (3, 16))
        self.assertEqual((excel_workspace_position(1, "math_arrow_se").row,
                          excel_workspace_position(1, "math_arrow_se").column), (3, 17))
        # Label & Context: R2C18, R2C19
        self.assertEqual((excel_workspace_position(1, "math_label").row,
                          excel_workspace_position(1, "math_label").column), (2, 18))
        self.assertEqual((excel_workspace_position(1, "math_context").row,
                          excel_workspace_position(1, "math_context").column), (2, 19))
        # Trailing button: R2C21
        self.assertEqual((excel_workspace_position(1, "math_trailing_btn").row,
                          excel_workspace_position(1, "math_trailing_btn").column), (2, 21))

        # Actions (Col 23):
        # Top: "math to put on the left" at R1C23
        self.assertEqual((excel_workspace_position(1, "action_math_left").row,
                          excel_workspace_position(1, "action_math_left").column), (1, 23))
        # Bottom: "clear math on the left" at R3C23
        self.assertEqual((excel_workspace_position(1, "action_clear_left").row,
                          excel_workspace_position(1, "action_clear_left").column), (3, 23))

        # Slot 3 (Result Card):
        # Lead button: R2C25
        self.assertEqual((excel_workspace_position(1, "result_lead_btn").row,
                          excel_workspace_position(1, "result_lead_btn").column), (2, 25))
        # Arrow grid: cols 27-29, rows 1-3
        self.assertEqual((excel_workspace_position(1, "result_arrow_nw").row,
                          excel_workspace_position(1, "result_arrow_nw").column), (1, 27))
        self.assertEqual((excel_workspace_position(1, "result_arrow_n").row,
                          excel_workspace_position(1, "result_arrow_n").column), (1, 28))
        self.assertEqual((excel_workspace_position(1, "result_arrow_ne").row,
                          excel_workspace_position(1, "result_arrow_ne").column), (1, 29))
        self.assertEqual((excel_workspace_position(1, "result_arrow_w").row,
                          excel_workspace_position(1, "result_arrow_w").column), (2, 27))
        self.assertEqual((excel_workspace_position(1, "result_center").row,
                          excel_workspace_position(1, "result_center").column), (2, 28))
        self.assertEqual((excel_workspace_position(1, "result_arrow_e").row,
                          excel_workspace_position(1, "result_arrow_e").column), (2, 29))
        self.assertEqual((excel_workspace_position(1, "result_arrow_sw").row,
                          excel_workspace_position(1, "result_arrow_sw").column), (3, 27))
        self.assertEqual((excel_workspace_position(1, "result_arrow_s").row,
                          excel_workspace_position(1, "result_arrow_s").column), (3, 28))
        self.assertEqual((excel_workspace_position(1, "result_arrow_se").row,
                          excel_workspace_position(1, "result_arrow_se").column), (3, 29))
        # Label & Context: R2C30, R2C31
        self.assertEqual((excel_workspace_position(1, "result_label").row,
                          excel_workspace_position(1, "result_label").column), (2, 30))
        self.assertEqual((excel_workspace_position(1, "result_context").row,
                          excel_workspace_position(1, "result_context").column), (2, 31))
        # Trailing button: R2C33
        self.assertEqual((excel_workspace_position(1, "result_trailing_btn").row,
                          excel_workspace_position(1, "result_trailing_btn").column), (2, 33))

    def test_row_2_positions_match_excel_sheet_exactly(self):
        """Verify every control in Calculator Row 2 matches my_excel_sheet.txt cells."""
        # Helper card heading: R5C3..R5C8
        hh = excel_workspace_position(2, "helper_heading")
        self.assertEqual((hh.row, hh.column, hh.row_span, hh.column_span), (5, 3, 1, 6))

        # Row 2 label: R7C1 (row_span=3, rows 7-9)
        lbl = excel_workspace_position(2, "row_label")
        self.assertEqual((lbl.row, lbl.column, lbl.row_span, lbl.column_span), (7, 1, 3, 1))

        # Slot 1 (Helper Card):
        # Lead button: R8C3
        self.assertEqual((excel_workspace_position(2, "helper_lead_btn").row,
                          excel_workspace_position(2, "helper_lead_btn").column), (8, 3))
        # Arrow grid: cols 5-7, rows 7-9
        self.assertEqual((excel_workspace_position(2, "helper_arrow_nw").row,
                          excel_workspace_position(2, "helper_arrow_nw").column), (7, 5))
        self.assertEqual((excel_workspace_position(2, "helper_arrow_n").row,
                          excel_workspace_position(2, "helper_arrow_n").column), (7, 6))
        self.assertEqual((excel_workspace_position(2, "helper_arrow_ne").row,
                          excel_workspace_position(2, "helper_arrow_ne").column), (7, 7))
        self.assertEqual((excel_workspace_position(2, "helper_arrow_w").row,
                          excel_workspace_position(2, "helper_arrow_w").column), (8, 5))
        self.assertEqual((excel_workspace_position(2, "helper_center").row,
                          excel_workspace_position(2, "helper_center").column), (8, 6))
        self.assertEqual((excel_workspace_position(2, "helper_arrow_e").row,
                          excel_workspace_position(2, "helper_arrow_e").column), (8, 7))
        self.assertEqual((excel_workspace_position(2, "helper_arrow_sw").row,
                          excel_workspace_position(2, "helper_arrow_sw").column), (9, 5))
        self.assertEqual((excel_workspace_position(2, "helper_arrow_s").row,
                          excel_workspace_position(2, "helper_arrow_s").column), (9, 6))
        self.assertEqual((excel_workspace_position(2, "helper_arrow_se").row,
                          excel_workspace_position(2, "helper_arrow_se").column), (9, 7))
        # Label & Context: R8C8, R8C9
        self.assertEqual((excel_workspace_position(2, "helper_label").row,
                          excel_workspace_position(2, "helper_label").column), (8, 8))
        self.assertEqual((excel_workspace_position(2, "helper_context").row,
                          excel_workspace_position(2, "helper_context").column), (8, 9))
        # Trailing button: R8C11
        self.assertEqual((excel_workspace_position(2, "helper_trailing_btn").row,
                          excel_workspace_position(2, "helper_trailing_btn").column), (8, 11))

        # Slot 2 (Math Expression):
        # Lead button: R8C13
        self.assertEqual((excel_workspace_position(2, "math_lead_btn").row,
                          excel_workspace_position(2, "math_lead_btn").column), (8, 13))
        # Center square: R8C16
        self.assertEqual((excel_workspace_position(2, "math_center").row,
                          excel_workspace_position(2, "math_center").column), (8, 16))

        # Actions (Col 23):
        self.assertEqual((excel_workspace_position(2, "action_math_left").row,
                          excel_workspace_position(2, "action_math_left").column), (7, 23))
        self.assertEqual((excel_workspace_position(2, "action_clear_left").row,
                          excel_workspace_position(2, "action_clear_left").column), (9, 23))

        # Slot 3 (Result Card):
        self.assertEqual((excel_workspace_position(2, "result_lead_btn").row,
                          excel_workspace_position(2, "result_lead_btn").column), (8, 25))
        self.assertEqual((excel_workspace_position(2, "result_center").row,
                          excel_workspace_position(2, "result_center").column), (8, 28))
        self.assertEqual((excel_workspace_position(2, "result_trailing_btn").row,
                          excel_workspace_position(2, "result_trailing_btn").column), (8, 33))

    def test_all_individual_controls_are_disjoint_and_non_overlapping(self):
        """Reject accidental overlapping controls across calculator rows 1 through 4."""
        for k in (1, 2, 3, 4):
            positions = excel_workspace_positions(k)
            occupied_cells: set[tuple[int, int]] = set()

            for name, pos in positions.items():
                for r in range(pos.row, pos.end_row + 1):
                    for c in range(pos.column, pos.end_column + 1):
                        cell = (r, c)
                        self.assertNotIn(
                            cell,
                            occupied_cells,
                            f"Collision detected in calculator row {k}: control {name!r} overlaps cell {cell}",
                        )
                        occupied_cells.add(cell)

            # All occupied columns must strictly be within 1..33
            for r, c in occupied_cells:
                self.assertTrue(1 <= c <= 33, f"Column {c} out of bounds 1..33")

    def test_inter_row_isolation_across_rows_1_to_4(self):
        """Verify no row-level overlap between calculator rows 1, 2, 3, and 4."""
        all_cells: dict[tuple[int, int], str] = {}
        for k in (1, 2, 3, 4):
            positions = excel_workspace_positions(k)
            for name, pos in positions.items():
                tag = f"row_{k}:{name}"
                for r in range(pos.row, pos.end_row + 1):
                    for c in range(pos.column, pos.end_column + 1):
                        cell = (r, c)
                        self.assertNotIn(
                            cell,
                            all_cells,
                            f"Inter-row collision at cell {cell} between {all_cells.get(cell)} and {tag}",
                        )
                        all_cells[cell] = tag

    def test_error_handling_for_invalid_arguments(self):
        """excel_start_row and excel_workspace_position validate inputs strictly."""
        with self.assertRaises(ValueError):
            excel_start_row(0)
        with self.assertRaises(ValueError):
            excel_start_row(-2)
        with self.assertRaises(ValueError):
            excel_start_row(True)

        with self.assertRaises(ValueError):
            excel_heading_row(1)  # No heading row for Calculator Row 1

        with self.assertRaises(ValueError):
            excel_workspace_position(2, "join_note_label")  # Join note only exists on row 1

        with self.assertRaises(ValueError):
            excel_workspace_position(1, "helper_heading")  # Helper heading only exists on row >= 2

        with self.assertRaises(KeyError):
            excel_workspace_position(1, "nonexistent_control_xyz")


if __name__ == "__main__":
    unittest.main()
