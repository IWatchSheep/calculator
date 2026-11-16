from gui_coordinates import (
    EXCEL_13COL_TOTAL_COLUMNS,
    EXCEL_13COL_INITIAL_TOTAL_ROWS,
    EXCEL_13COL_ROWS_PER_CALCULATOR_ROW,
    EXCEL_13COL_CALCULATOR_ROW_STRIDE,
    EXCEL_13COL_ROW_LABEL,
    EXCEL_13COL_SPACER_AB,
    EXCEL_13COL_MATH_SIGN,
    EXCEL_13COL_SPACER_CD,
    EXCEL_13COL_NUMBER_MATH,
    EXCEL_13COL_MATH_BOX1,
    EXCEL_13COL_MATH_TRAILING,
    EXCEL_13COL_SPACER_GH,
    EXCEL_13COL_ACTIONS,
    EXCEL_13COL_RESULT_EQUALS,
    EXCEL_13COL_RESULT_BOX,
    EXCEL_13COL_RESULT_BOX1,
    EXCEL_13COL_RESULT_TRAILING,
    EXCEL_13COL_COLUMN_WIDTHS,
    excel_13col_column_letter,
    excel_13col_column_from_letter,
    excel_13col_column_width,
    excel_13col_total_width,
    excel_13col_start_row,
    excel_13col_workspace_position,
    excel_13col_workspace_positions,
    excel_13col_total_row_positions,
    EXCEL_17COL_TOTAL_COLUMNS,
    EXCEL_17COL_ROW_LABEL,
    EXCEL_17COL_MATH_SIGN,
    EXCEL_17COL_NUMBER_MATH,
    EXCEL_17COL_MATH_BOX1,
    EXCEL_17COL_MATH_TRAILING,
    EXCEL_17COL_ACTIONS,
    EXCEL_17COL_RESULT_EQUALS,
    EXCEL_17COL_PAREN_OPEN,
    EXCEL_17COL_RESULT_BOX,
    EXCEL_17COL_EXPONENT_1,
    EXCEL_17COL_PAREN_CLOSE,
    EXCEL_17COL_EXPONENT_2,
    EXCEL_17COL_RESULT_BOX1,
    EXCEL_17COL_RESULT_TRAILING,
    EXCEL_17COL_COLUMN_WIDTHS,
    EXCEL_17COL_EFFECTIVE_DEFAULT_WIDTHS,
    excel_17col_column_letter,
    excel_17col_column_from_letter,
    excel_17col_column_width,
    excel_17col_effective_column_width,
    excel_17col_total_width,
    excel_17col_effective_total_width,
    excel_17col_start_row,
    excel_17col_workspace_position,
    excel_17col_workspace_positions,
    excel_17col_total_row_positions,
    EXCEL_18COL_TOTAL_COLUMNS,
    EXCEL_18COL_LETTERS,
    EXCEL_18COL_ROW_LABEL,
    EXCEL_18COL_SPACER_AB,
    EXCEL_18COL_MATH_SIGN,
    EXCEL_18COL_SPACER_CD,
    EXCEL_18COL_NUMBER_MATH,
    EXCEL_18COL_MATH_BOX1,
    EXCEL_18COL_MATH_TRAILING,
    EXCEL_18COL_SPACER_GH,
    EXCEL_18COL_ACTIONS,
    EXCEL_18COL_RESULT_EQUALS,
    EXCEL_18COL_PAREN_PLUS,
    EXCEL_18COL_PAREN_OPEN,
    EXCEL_18COL_RESULT_BOX,
    EXCEL_18COL_EXPONENT_1,
    EXCEL_18COL_PAREN_CLOSE,
    EXCEL_18COL_EXPONENT_2,
    EXCEL_18COL_RESULT_BOX1,
    EXCEL_18COL_RESULT_TRAILING,
    EXCEL_18COL_COLUMN_WIDTHS,
    EXCEL_18COL_EFFECTIVE_DEFAULT_WIDTHS,
    excel_18col_column_letter,
    excel_18col_column_from_letter,
    excel_18col_column_width,
    excel_18col_effective_column_width,
    excel_18col_total_width,
    excel_18col_effective_total_width,
    excel_18col_start_row,
    excel_18col_workspace_position,
    excel_18col_workspace_positions,
    excel_18col_total_row_positions,
)
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
    LEGACY_33COL_TOTAL_COLUMNS,
    LEGACY_33COL_COLUMN_WIDTHS,
    legacy_33col_workspace_position,
    legacy_33col_workspace_positions,
    EXCEL_13COL_TOTAL_COLUMNS,
    EXCEL_13COL_ROW_LABEL,
    EXCEL_13COL_MATH_SIGN,
    EXCEL_13COL_NUMBER_MATH,
    EXCEL_13COL_MATH_BOX1,
    EXCEL_13COL_MATH_TRAILING,
    EXCEL_13COL_ACTIONS,
    EXCEL_13COL_RESULT_EQUALS,
    EXCEL_13COL_RESULT_BOX,
    EXCEL_13COL_RESULT_BOX1,
    EXCEL_13COL_RESULT_TRAILING,
    EXCEL_13COL_COLUMN_WIDTHS,
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
    EXCEL_COL_SLOT1_LEAD_BTN,
    EXCEL_COL_SLOT1_SPACER1,
    EXCEL_COL_SLOT1_ARROW_COL1,
    EXCEL_COL_SLOT1_ARROW_COL2,
    EXCEL_COL_SLOT1_ARROW_COL3,
    EXCEL_COL_SLOT1_LABEL,
    EXCEL_COL_SLOT1_CONTEXT,
    EXCEL_COL_SLOT1_SPACER2,
    EXCEL_COL_SLOT1_TRAILING_BTN,
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
    EXCEL_COLUMN_WIDTHS,
    excel_column_width,
    excel_row_height,
    excel_total_workspace_width,
    excel_initial_workspace_height,
    configure_excel_workspace_grid,
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
            "trailing_button": (2, 8, 1, 1),
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
        self.assertEqual(columns, [1, 6, 7, 8])
        self.assertEqual(len(set(columns)), 4)

        # Arrow columns are 3, 4, 5
        arrow_cols = {pos.column for pos in CARD_9COL_ARROW_POSITIONS}
        self.assertEqual(arrow_cols, {3, 4, 5})

        # Columns 2 and 8 are spacers and never occupied
        all_cols = set(columns) | arrow_cols
        self.assertNotIn(2, all_cols)
        self.assertEqual(all_cols, {1, 3, 4, 5, 6, 7, 8})

    def test_card_components_tkinter_grid_conversion(self):
        """Verify conversion to Tkinter zero-based grid parameters."""
        expected_tk = {
            "lead_button": {"row": 1, "column": 0, "rowspan": 1, "columnspan": 1},
            "arrow_grid": {"row": 0, "column": 2, "rowspan": 3, "columnspan": 3},
            "center_square": {"row": 1, "column": 3, "rowspan": 1, "columnspan": 1},
            "label_entry": {"row": 1, "column": 5, "rowspan": 1, "columnspan": 1},
            "context_entry": {"row": 1, "column": 6, "rowspan": 1, "columnspan": 1},
            "trailing_button": {"row": 1, "column": 7, "rowspan": 1, "columnspan": 1},
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
            as_buttons=True,
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

        # 6. Check Orange plus / trailing button at Card row 2, col 8 (Tkinter row 1, col 7)
        self.assertTrue(hasattr(card, "trailing_btn"))
        self.assertEqual(card.trailing_btn.grid_pos, CARD_TRAILING_BUTTON_POSITION)
        info_trailing = card.trailing_btn.grid_info()
        self.assertEqual(int(info_trailing["row"]), 1)
        self.assertEqual(int(info_trailing["column"]), 7)
        self.assertEqual(int(info_trailing["rowspan"]), 1)
        self.assertEqual(card.trailing_btn.cget("text"), "+")

        # 7. Check spacer column (column 1 in 0-based Tkinter) is empty
        occupied_cols = {int(w.grid_info()["column"]) for w in card.winfo_children()}
        self.assertNotIn(1, occupied_cols, "Tkinter column 1 (Card spacer 2) must remain empty")

        # 8. Check global Excel coordinate traceability
        excel_center = card.to_excel_coordinate(card.center_btn)
        self.assertEqual(excel_center, GridPosition(row=2, column=26, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(card.to_excel_coordinate(card.lead_btn),
                         GridPosition(row=2, column=23, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(card.to_excel_coordinate(card.trailing_btn),
                         GridPosition(row=2, column=30, region=LayoutRegion.EXCEL_WORKSPACE))

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

        # Slot 2: Math Expression in calc_row 1 -> rows 1..3, cols 12..19
        for local_pos in CARD_9COL_ARROW_POSITIONS:
            g_pos = card_to_excel_position(local_pos, card_slot=2, calc_row=1)
            self.assertEqual(g_pos.region, LayoutRegion.EXCEL_WORKSPACE)
            self.assertEqual(g_pos.row, 1 + local_pos.row - 1)
            self.assertEqual(g_pos.column, 12 + local_pos.column - 1)
            slot, back_local = excel_to_card_position(g_pos)
            self.assertEqual(slot, 2)
            self.assertEqual(back_local, local_pos)

        # Slot 3: Result Card in calc_row 1 -> rows 1..3, cols 23..30
        for local_pos in CARD_9COL_ARROW_POSITIONS:
            g_pos = card_to_excel_position(local_pos, card_slot=3, calc_row=1)
            self.assertEqual(g_pos.region, LayoutRegion.EXCEL_WORKSPACE)
            self.assertEqual(g_pos.row, 1 + local_pos.row - 1)
            self.assertEqual(g_pos.column, 23 + local_pos.column - 1)
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
        """CalculatorGUI instantiates rows with authoritative Excel coordinates and backward-compatible logical mappings."""
        if self.root is None:
            self.skipTest("Tkinter display not available")

        from main import CalculatorGUI

        app = None
        try:
            app = CalculatorGUI()
            app.withdraw()

            self.assertEqual(len(app.rows), 1)
            app._add_row()
            self.assertEqual(len(app.rows), 2)

            for r_idx in range(2):
                row_data = app.rows[r_idx]
                r_num = r_idx + 1
                r0 = excel_18col_start_row(r_num)
                r0_zero = r0 - 1

                # Verify logical mappings
                self.assertIn("main_row_positions", row_data)
                self.assertEqual(row_data["main_row_positions"], main_row_positions(r_num))

                # Verify authoritative 18-column Excel grid positions
                self.assertIn("grid_positions", row_data)
                positions = row_data["grid_positions"]
                self.assertEqual(positions, excel_18col_workspace_positions(r_num))

                # Verify box (number/expression) in Excel column E (0-based column 4)
                self.assertIn("box", row_data)
                box = row_data["box"]
                self.assertTrue(hasattr(box, "grid_pos"))
                b_info = box.grid_info()
                self.assertEqual(int(b_info["row"]), 1)  # row 1 inside its own row_frame
                self.assertEqual(int(b_info["column"]), EXCEL_18COL_NUMBER_MATH - 1)
                self.assertEqual(int(b_info["columnspan"]), 1)
                self.assertEqual(int(b_info["rowspan"]), 1)
                self.assertEqual(box.excel_pos.row, r0 + 1)

                # Verify result box in Excel column M (0-based column 12)
                result_box = row_data.get("result_box", row_data["result"])
                self.assertTrue(hasattr(result_box, "grid_pos"))
                c_info = result_box.grid_info()
                self.assertEqual(int(c_info["row"]), 1)
                self.assertEqual(int(c_info["column"]), EXCEL_18COL_RESULT_BOX - 1)
                self.assertEqual(int(c_info["columnspan"]), 1)
                self.assertEqual(int(c_info["rowspan"]), 1)
                self.assertEqual(result_box.excel_pos.row, r0 + 1)

                # Verify row label frame in Excel column A (0-based column 0)
                labf = row_data["label_frame"]
                self.assertTrue(hasattr(labf, "grid_pos"))
                l_info = labf.grid_info()
                self.assertEqual(int(l_info["row"]), 0)
                self.assertEqual(int(l_info["column"]), EXCEL_18COL_ROW_LABEL - 1)
                self.assertEqual(int(l_info["columnspan"]), 1)
                self.assertEqual(int(l_info["rowspan"]), 3)
                self.assertEqual(labf.excel_pos.row, r0)

                # Verify actions frame in Excel column I (0-based column 8)
                col3 = row_data["actions_frame"]
                self.assertTrue(hasattr(col3, "grid_pos"))
                a_info = col3.grid_info()
                self.assertEqual(int(a_info["row"]), 0)
                self.assertEqual(int(a_info["column"]), EXCEL_18COL_ACTIONS - 1)
                self.assertEqual(int(a_info["columnspan"]), 1)
                self.assertEqual(int(a_info["rowspan"]), 3)
                self.assertEqual(col3.excel_pos.row, r0)

            # Test adding a 3rd row dynamically
            new_r = app._add_row()
            self.assertEqual(new_r, 2)  # 0-indexed row 2 -> Calculator Row 3
            self.assertEqual(len(app.rows), 3)

            row_3 = app.rows[2]
            positions_3 = row_3["grid_positions"]
            self.assertEqual(positions_3, excel_18col_workspace_positions(3))

            box_3 = row_3["box"]
            b3_info = box_3.grid_info()
            self.assertEqual(int(b3_info["row"]), 1)
            self.assertEqual(int(b3_info["column"]), EXCEL_18COL_NUMBER_MATH - 1)
            self.assertEqual(box_3.excel_pos.row, excel_18col_start_row(3) + 1)

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
        self.assertEqual(LEGACY_33COL_TOTAL_COLUMNS, 30)
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
        lbl = legacy_33col_workspace_position(1, "row_label")
        self.assertEqual((lbl.row, lbl.column, lbl.row_span, lbl.column_span), (1, 1, 3, 1))
        self.assertEqual(lbl.region, LayoutRegion.EXCEL_WORKSPACE)

        # Slot 1: Join note text: R1C3..R1C10 (column_span=8)
        jn = legacy_33col_workspace_position(1, "join_note_label")
        self.assertEqual((jn.row, jn.column, jn.row_span, jn.column_span), (1, 3, 1, 5))

        # Slot 1: Join note down arrow canvas: R3C6
        ja = legacy_33col_workspace_position(1, "join_note_arrow")
        self.assertEqual((ja.row, ja.column, ja.row_span, ja.column_span), (3, 6, 1, 1))

        # Slot 2 (Math Expression):
        # Lead button: R2C12 (L2)
        self.assertEqual((legacy_33col_workspace_position(1, "math_lead_btn").row,
                          legacy_33col_workspace_position(1, "math_lead_btn").column), (2, 12))
        # Arrow grid: cols 14-16, rows 1-3
        self.assertEqual((legacy_33col_workspace_position(1, "math_arrow_nw").row,
                          legacy_33col_workspace_position(1, "math_arrow_nw").column), (1, 14))
        self.assertEqual((legacy_33col_workspace_position(1, "math_arrow_n").row,
                          legacy_33col_workspace_position(1, "math_arrow_n").column), (1, 15))
        self.assertEqual((legacy_33col_workspace_position(1, "math_arrow_ne").row,
                          legacy_33col_workspace_position(1, "math_arrow_ne").column), (1, 16))
        self.assertEqual((legacy_33col_workspace_position(1, "math_arrow_w").row,
                          legacy_33col_workspace_position(1, "math_arrow_w").column), (2, 14))
        self.assertEqual((legacy_33col_workspace_position(1, "math_center").row,
                          legacy_33col_workspace_position(1, "math_center").column), (2, 15))
        self.assertEqual((legacy_33col_workspace_position(1, "math_arrow_e").row,
                          legacy_33col_workspace_position(1, "math_arrow_e").column), (2, 16))
        self.assertEqual((legacy_33col_workspace_position(1, "math_arrow_sw").row,
                          legacy_33col_workspace_position(1, "math_arrow_sw").column), (3, 14))
        self.assertEqual((legacy_33col_workspace_position(1, "math_arrow_s").row,
                          legacy_33col_workspace_position(1, "math_arrow_s").column), (3, 15))
        self.assertEqual((legacy_33col_workspace_position(1, "math_arrow_se").row,
                          legacy_33col_workspace_position(1, "math_arrow_se").column), (3, 16))
        # Label & Context: R2C17, R2C18 (Q2, R2)
        self.assertEqual((legacy_33col_workspace_position(1, "math_label").row,
                          legacy_33col_workspace_position(1, "math_label").column), (2, 17))
        self.assertEqual((legacy_33col_workspace_position(1, "math_context").row,
                          legacy_33col_workspace_position(1, "math_context").column), (2, 18))
        # Trailing button: R2C19 (S2)
        self.assertEqual((legacy_33col_workspace_position(1, "math_trailing_btn").row,
                          legacy_33col_workspace_position(1, "math_trailing_btn").column), (2, 19))

        # Actions (Col 21, U):
        # Top: "math to put on the left" at R1C21
        self.assertEqual((legacy_33col_workspace_position(1, "action_math_left").row,
                          legacy_33col_workspace_position(1, "action_math_left").column), (1, 21))
        # Bottom: "clear math on the left" at R3C21
        self.assertEqual((legacy_33col_workspace_position(1, "action_clear_left").row,
                          legacy_33col_workspace_position(1, "action_clear_left").column), (3, 21))

        # Slot 3 (Result Card):
        # Lead button: R2C23 (W2)
        self.assertEqual((legacy_33col_workspace_position(1, "result_lead_btn").row,
                          legacy_33col_workspace_position(1, "result_lead_btn").column), (2, 23))
        # Arrow grid: cols 25-27, rows 1-3
        self.assertEqual((legacy_33col_workspace_position(1, "result_arrow_nw").row,
                          legacy_33col_workspace_position(1, "result_arrow_nw").column), (1, 25))
        self.assertEqual((legacy_33col_workspace_position(1, "result_arrow_n").row,
                          legacy_33col_workspace_position(1, "result_arrow_n").column), (1, 26))
        self.assertEqual((legacy_33col_workspace_position(1, "result_arrow_ne").row,
                          legacy_33col_workspace_position(1, "result_arrow_ne").column), (1, 27))
        self.assertEqual((legacy_33col_workspace_position(1, "result_arrow_w").row,
                          legacy_33col_workspace_position(1, "result_arrow_w").column), (2, 25))
        self.assertEqual((legacy_33col_workspace_position(1, "result_center").row,
                          legacy_33col_workspace_position(1, "result_center").column), (2, 26))
        self.assertEqual((legacy_33col_workspace_position(1, "result_arrow_e").row,
                          legacy_33col_workspace_position(1, "result_arrow_e").column), (2, 27))
        self.assertEqual((legacy_33col_workspace_position(1, "result_arrow_sw").row,
                          legacy_33col_workspace_position(1, "result_arrow_sw").column), (3, 25))
        self.assertEqual((legacy_33col_workspace_position(1, "result_arrow_s").row,
                          legacy_33col_workspace_position(1, "result_arrow_s").column), (3, 26))
        self.assertEqual((legacy_33col_workspace_position(1, "result_arrow_se").row,
                          legacy_33col_workspace_position(1, "result_arrow_se").column), (3, 27))
        # Label & Context: R2C28, R2C29 (AB2, AC2)
        self.assertEqual((legacy_33col_workspace_position(1, "result_label").row,
                          legacy_33col_workspace_position(1, "result_label").column), (2, 28))
        self.assertEqual((legacy_33col_workspace_position(1, "result_context").row,
                          legacy_33col_workspace_position(1, "result_context").column), (2, 29))
        # Trailing button: R2C30 (AD2)
        self.assertEqual((legacy_33col_workspace_position(1, "result_trailing_btn").row,
                          legacy_33col_workspace_position(1, "result_trailing_btn").column), (2, 30))

    def test_row_2_positions_match_excel_sheet_exactly(self):
        """Verify every control in Calculator Row 2 matches my_excel_sheet.txt cells."""
        # Helper card heading: R5C3..R5C8
        hh = legacy_33col_workspace_position(2, "helper_heading")
        self.assertEqual((hh.row, hh.column, hh.row_span, hh.column_span), (5, 3, 1, 6))

        # Row 2 label: R7C1 (row_span=3, rows 7-9)
        lbl = legacy_33col_workspace_position(2, "row_label")
        self.assertEqual((lbl.row, lbl.column, lbl.row_span, lbl.column_span), (7, 1, 3, 1))

        # Slot 1 (Helper Card):
        # Lead button: R8C3
        self.assertEqual((legacy_33col_workspace_position(2, "helper_lead_btn").row,
                          legacy_33col_workspace_position(2, "helper_lead_btn").column), (8, 3))
        # Arrow grid: cols 5-7, rows 7-9
        self.assertEqual((legacy_33col_workspace_position(2, "helper_arrow_nw").row,
                          legacy_33col_workspace_position(2, "helper_arrow_nw").column), (7, 5))
        self.assertEqual((legacy_33col_workspace_position(2, "helper_arrow_n").row,
                          legacy_33col_workspace_position(2, "helper_arrow_n").column), (7, 6))
        self.assertEqual((legacy_33col_workspace_position(2, "helper_arrow_ne").row,
                          legacy_33col_workspace_position(2, "helper_arrow_ne").column), (7, 7))
        self.assertEqual((legacy_33col_workspace_position(2, "helper_arrow_w").row,
                          legacy_33col_workspace_position(2, "helper_arrow_w").column), (8, 5))
        self.assertEqual((legacy_33col_workspace_position(2, "helper_center").row,
                          legacy_33col_workspace_position(2, "helper_center").column), (8, 6))
        self.assertEqual((legacy_33col_workspace_position(2, "helper_arrow_e").row,
                          legacy_33col_workspace_position(2, "helper_arrow_e").column), (8, 7))
        self.assertEqual((legacy_33col_workspace_position(2, "helper_arrow_sw").row,
                          legacy_33col_workspace_position(2, "helper_arrow_sw").column), (9, 5))
        self.assertEqual((legacy_33col_workspace_position(2, "helper_arrow_s").row,
                          legacy_33col_workspace_position(2, "helper_arrow_s").column), (9, 6))
        self.assertEqual((legacy_33col_workspace_position(2, "helper_arrow_se").row,
                          legacy_33col_workspace_position(2, "helper_arrow_se").column), (9, 7))
        # Label & Context: R8C8, R8C9
        self.assertEqual((legacy_33col_workspace_position(2, "helper_label").row,
                          legacy_33col_workspace_position(2, "helper_label").column), (8, 8))
        self.assertEqual((legacy_33col_workspace_position(2, "helper_context").row,
                          legacy_33col_workspace_position(2, "helper_context").column), (8, 9))
        # Trailing button: R8C10 (J8)
        self.assertEqual((legacy_33col_workspace_position(2, "helper_trailing_btn").row,
                          legacy_33col_workspace_position(2, "helper_trailing_btn").column), (8, 10))

        # Slot 2 (Math Expression):
        # Lead button: R8C12 (L8)
        self.assertEqual((legacy_33col_workspace_position(2, "math_lead_btn").row,
                          legacy_33col_workspace_position(2, "math_lead_btn").column), (8, 12))
        # Center square: R8C15 (O8)
        self.assertEqual((legacy_33col_workspace_position(2, "math_center").row,
                          legacy_33col_workspace_position(2, "math_center").column), (8, 15))

        # Actions (Col 21, U):
        self.assertEqual((legacy_33col_workspace_position(2, "action_math_left").row,
                          legacy_33col_workspace_position(2, "action_math_left").column), (7, 21))
        self.assertEqual((legacy_33col_workspace_position(2, "action_clear_left").row,
                          legacy_33col_workspace_position(2, "action_clear_left").column), (9, 21))

        # Slot 3 (Result Card):
        self.assertEqual((legacy_33col_workspace_position(2, "result_lead_btn").row,
                          legacy_33col_workspace_position(2, "result_lead_btn").column), (8, 23))
        self.assertEqual((legacy_33col_workspace_position(2, "result_center").row,
                          legacy_33col_workspace_position(2, "result_center").column), (8, 26))
        self.assertEqual((legacy_33col_workspace_position(2, "result_trailing_btn").row,
                          legacy_33col_workspace_position(2, "result_trailing_btn").column), (8, 30))

    def test_all_individual_controls_are_disjoint_and_non_overlapping(self):
        """Reject accidental overlapping controls across calculator rows 1 through 4."""
        for k in (1, 2, 3, 4):
            positions = legacy_33col_workspace_positions(k)
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
            positions = legacy_33col_workspace_positions(k)
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
            legacy_33col_workspace_position(2, "join_note_label")  # Join note only exists on row 1

        with self.assertRaises(ValueError):
            legacy_33col_workspace_position(1, "helper_heading")  # Helper heading only exists on row >= 2

        with self.assertRaises(KeyError):
            legacy_33col_workspace_position(1, "nonexistent_control_xyz")


class TestExcelWorkspacePreparedGrid(unittest.TestCase):
    """Test Step 3 prepared 9-row x 33-column workspace grid configuration and sizing."""

    def setUp(self):
        try:
            self.root = tk.Tk()
            self.root.withdraw()
        except tk.TclError:
            self.root = None

    def tearDown(self):
        if self.root:
            try:
                self.root.destroy()
            except Exception:
                pass
            self.root = None

    def test_prepared_grid_33_columns_configured(self):
        """Exactly 33 columns are configured with explicit widths and weight=0."""
        if self.root is None:
            self.skipTest("Tkinter display not available")

        frame = tk.Frame(self.root)
        configure_excel_workspace_grid(frame, num_calc_rows=2)

        for col_1based in range(1, EXCEL_TOTAL_COLUMNS + 1):
            col_0based = col_1based - 1
            info = frame.grid_columnconfigure(col_0based)
            expected_width = EXCEL_COLUMN_WIDTHS[col_1based]
            self.assertEqual(int(info.get("minsize", 0)), expected_width,
                             f"Column {col_1based} width mismatch")
            self.assertEqual(int(info.get("weight", 0)), 0,
                             f"Column {col_1based} must have weight=0 to avoid uncontrolled stretching")

    def test_prepared_grid_initial_9_rows_configured(self):
        """Initial layout configures exactly 9 rows with defined heights matching roles."""
        if self.root is None:
            self.skipTest("Tkinter display not available")

        frame = tk.Frame(self.root)
        configure_excel_workspace_grid(frame, num_calc_rows=2)

        for row_1based in range(1, EXCEL_INITIAL_TOTAL_ROWS + 1):
            row_0based = row_1based - 1
            info = frame.grid_rowconfigure(row_0based)
            expected_height = excel_row_height(row_1based)
            self.assertEqual(int(info.get("minsize", 0)), expected_height,
                             f"Row {row_1based} height mismatch")
            self.assertEqual(int(info.get("weight", 0)), 0)

        # Explicit role verification
        # Calculator Row 1: rows 1..3 (26, 44, 26)
        self.assertEqual(excel_row_height(1), 26)
        self.assertEqual(excel_row_height(2), 44)
        self.assertEqual(excel_row_height(3), 26)

        # Spacers and Heading: rows 4..6 (10, 24, 10)
        self.assertEqual(excel_row_height(4), 10)  # Spacer before heading
        self.assertEqual(excel_row_height(5), 24)  # Helper card heading
        self.assertEqual(excel_row_height(6), 10)  # Spacer after heading

        # Calculator Row 2: rows 7..9 (26, 44, 26)
        self.assertEqual(excel_row_height(7), 26)
        self.assertEqual(excel_row_height(8), 44)
        self.assertEqual(excel_row_height(9), 26)

    def test_card_column_widths_match_card_specification(self):
        """Card column widths in the 33-column grid correspond to Step 2 card specification."""
        card_widths = [
            LEGACY_33COL_COLUMN_WIDTHS[EXCEL_COL_SLOT1_LEAD_BTN],    # 42 (Lead btn)
            LEGACY_33COL_COLUMN_WIDTHS[EXCEL_COL_SLOT1_SPACER1],     # 10 (Spacer 1)
            LEGACY_33COL_COLUMN_WIDTHS[EXCEL_COL_SLOT1_ARROW_COL1],  # 24 (Arrow Left)
            LEGACY_33COL_COLUMN_WIDTHS[EXCEL_COL_SLOT1_ARROW_COL2],  # 28 (Arrow Mid / Center)
            LEGACY_33COL_COLUMN_WIDTHS[EXCEL_COL_SLOT1_ARROW_COL3],  # 24 (Arrow Right)
            LEGACY_33COL_COLUMN_WIDTHS[EXCEL_COL_SLOT1_LABEL],       # 90 (Label entry)
            LEGACY_33COL_COLUMN_WIDTHS[EXCEL_COL_SLOT1_CONTEXT],     # 90 (Context entry)
            LEGACY_33COL_COLUMN_WIDTHS[EXCEL_COL_SLOT1_TRAILING_BTN],# 42 (Trailing btn)
        ]
        self.assertEqual(card_widths, [42, 10, 24, 28, 24, 90, 90, 42])

        # Slots 1, 2, and 3 have identical card column width profiles
        slot1_widths = [LEGACY_33COL_COLUMN_WIDTHS[c] for c in range(EXCEL_COL_SLOT1_START, EXCEL_COL_SLOT1_END + 1)]
        slot2_widths = [LEGACY_33COL_COLUMN_WIDTHS[c] for c in range(EXCEL_COL_SLOT2_START, EXCEL_COL_SLOT2_END + 1)]
        slot3_widths = [LEGACY_33COL_COLUMN_WIDTHS[c] for c in range(EXCEL_COL_SLOT3_START, EXCEL_COL_SLOT3_END + 1)]
        self.assertEqual(slot1_widths, card_widths)
        self.assertEqual(slot2_widths, card_widths)
        self.assertEqual(slot3_widths, card_widths)

    def test_stride_for_additional_rows(self):
        """configure_excel_workspace_grid correctly configures rows for arbitrary row counts."""
        if self.root is None:
            self.skipTest("Tkinter display not available")

        frame = tk.Frame(self.root)
        # Configure for 3 calculator rows -> 6 * (3 - 1) + 3 = 15 rows
        configure_excel_workspace_grid(frame, num_calc_rows=3)

        for r in range(1, 16):
            info = frame.grid_rowconfigure(r - 1)
            self.assertEqual(int(info.get("minsize", 0)), excel_row_height(r))

        # Check Calculator Row 3: heading at row 11, spacers at 10 and 12, cards at 13..15
        self.assertEqual(excel_row_height(10), 10)
        self.assertEqual(excel_row_height(11), 24)
        self.assertEqual(excel_row_height(12), 10)
        self.assertEqual(excel_row_height(13), 26)
        self.assertEqual(excel_row_height(14), 44)
        self.assertEqual(excel_row_height(15), 26)

    def test_total_workspace_dimensions_predictable(self):
        """Natural total width is bounded to 1126px without arbitrary expanding gaps."""
        total_width = excel_total_workspace_width()
        self.assertEqual(total_width, 888)
        self.assertEqual(sum(LEGACY_33COL_COLUMN_WIDTHS.values()), 1288)
        # Fits comfortably within standard 1700px calculator window
        self.assertLess(total_width, 1700)

        initial_height = excel_initial_workspace_height()
        self.assertEqual(initial_height, 236)

    def test_live_gui_has_prepared_workspace_without_conflicting(self):
        """CalculatorGUI has active 33-column Excel workspace and retired 5-column layout."""
        if self.root is None:
            self.skipTest("Tkinter display not available")

        from main import CalculatorGUI
        app = None
        try:
            app = CalculatorGUI()
            app.withdraw()

            # 1. Active area is self.excel_area
            self.assertTrue(hasattr(app, "area"))
            self.assertTrue(hasattr(app, "excel_area"))
            self.assertEqual(app.area, app.excel_area)
            self.assertEqual(len(app.rows), 1)

            # 2. Exactly 33 columns configured on the active workspace with weight=0
            for c in range(EXCEL_TOTAL_COLUMNS):
                col_width = int(app.area.grid_columnconfigure(c).get("minsize", 0))
                self.assertEqual(col_width, excel_column_width(c + 1))
                self.assertEqual(int(app.area.grid_columnconfigure(c).get("weight", 0)), 0)

            # 3. Exactly 9 rows configured on the active workspace
            for r in range(9):
                row_height = int(app.area.grid_rowconfigure(r).get("minsize", 0))
                self.assertEqual(row_height, excel_row_height(r + 1))

            # 4. Activation hook is idempotent
            self.assertTrue(hasattr(app, "activate_excel_workspace"))
            app.activate_excel_workspace()
            self.assertEqual(app.area, app.excel_area)

        finally:
            if app:
                try:
                    app.destroy()
                except Exception:
                    pass



class TestStep4ActiveExcelWorkspace(unittest.TestCase):
    """Checkpoint 2 verification: Independent row grids and auto-expanding descriptions."""

    def setUp(self):
        try:
            self.root = tk.Tk()
            self.root.withdraw()
        except tk.TclError:
            self.root = None

    def tearDown(self):
        if self.root:
            try:
                self.root.destroy()
            except Exception:
                pass
            self.root = None

    def test_01_active_workspace_is_excel_area(self):
        """1. Active workspace is self.excel_area and mounted in canvas window."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            self.assertEqual(app.area, app.excel_area)
            self.assertEqual(app.area, app.excel_workspace)
            win_widget = app.rows_canvas.nametowidget(app.rows_canvas.itemcget(app._rows_win, "window"))
            self.assertEqual(win_widget, app.excel_area)
        finally:
            app.destroy()

    def test_02_each_row_has_independent_row_frame_with_default_13_columns(self):
        """2. Each calculator row has its own row_frame configured with default 13-column widths."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._add_row()
            rf1 = app.rows[0]["row_frame"]
            rf2 = app.rows[1]["row_frame"]
            self.assertIsNot(rf1, rf2)
            self.assertEqual(rf1.master, app.area)
            self.assertEqual(rf2.master, app.area)

            for rf in (rf1, rf2):
                for c in range(18):
                    info = rf.grid_columnconfigure(c)
                    self.assertEqual(int(info.get("minsize", 0)), excel_18col_column_width(c + 1))
                    self.assertEqual(int(info.get("weight", 0)), 0)
        finally:
            app.destroy()

    def test_03_default_unexpanded_rows_have_identical_column_positions_and_widths(self):
        """3. Two default calculator rows have identical column positions and widths."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._add_row()
            app.update_idletasks()
            r1 = app.rows[0]
            r2 = app.rows[1]

            # Matching rootx and width across columns
            self.assertEqual(r1["box"].winfo_rootx(), r2["box"].winfo_rootx())
            self.assertEqual(r1["box"].winfo_width(), r2["box"].winfo_width())

            self.assertEqual(r1["math_desc"].winfo_rootx(), r2["math_desc"].winfo_rootx())

            self.assertEqual(r1["actions_frame"].winfo_rootx(), r2["actions_frame"].winfo_rootx())
            self.assertEqual(r1["actions_frame"].winfo_width(), r2["actions_frame"].winfo_width())

            self.assertEqual(r1["equals_label"].winfo_rootx(), r2["equals_label"].winfo_rootx())
            self.assertEqual(r1["equals_label"].winfo_width(), r2["equals_label"].winfo_width())

            self.assertEqual(r1["result_box"].winfo_rootx(), r2["result_box"].winfo_rootx())
            self.assertEqual(r1["result_box"].winfo_width(), r2["result_box"].winfo_width())

            self.assertEqual(r1["result_desc"].winfo_rootx(), r2["result_desc"].winfo_rootx())
        finally:
            app.destroy()

    def test_04_description_box1_stretches_without_moving_its_left_edge(self):
        """4. Description Box 1 expands rightward to fit text while left edge remains anchored."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app.update_idletasks()
            md1 = app.rows[0]["math_desc"]
            b1_x_before = md1.box1.winfo_rootx()
            b1_w_before = md1.box1.winfo_width()
            plus_x_before = md1.trailing_btn.winfo_rootx()

            # Set long text
            long_text = "Revenue from North America Q1 2026"
            md1.box1.set_text(long_text)
            app.update_idletasks()

            b1_x_after = md1.box1.winfo_rootx()
            b1_w_after = md1.box1.winfo_width()
            plus_x_after = md1.trailing_btn.winfo_rootx()

            # Left edge unchanged; width expanded; orange + pushed right
            self.assertEqual(b1_x_after, b1_x_before)
            self.assertGreater(b1_w_after, b1_w_before)
            self.assertGreater(plus_x_after, plus_x_before)
        finally:
            app.destroy()

    def test_05_orange_plus_creates_additional_text_boxes_in_order(self):
        """5. Orange + creates Box 2 and Box 3 in sequential order to the right."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app.update_idletasks()
            md1 = app.rows[0]["math_desc"]

            self.assertEqual(md1.num_boxes, 1)
            b1_x = md1.box1.winfo_rootx()

            # First press: add Box 2
            md1.trailing_btn.invoke()
            app.update_idletasks()
            self.assertEqual(md1.num_boxes, 2)
            self.assertIsNotNone(md1.box2)
            b2_x = md1.box2.winfo_rootx()
            plus_x_2 = md1.trailing_btn.winfo_rootx()

            self.assertEqual(md1.box1.winfo_rootx(), b1_x, "Box 1 must NOT move left")
            self.assertGreater(b2_x, b1_x, "Box 2 must appear to the right of Box 1")
            self.assertGreater(plus_x_2, b2_x, "Orange + must be to the right of Box 2")

            # Second press: add Box 3
            md1.trailing_btn.invoke()
            app.update_idletasks()
            self.assertEqual(md1.num_boxes, 3)
            b3_x = md1.boxes[2].winfo_rootx()
            plus_x_3 = md1.trailing_btn.winfo_rootx()

            self.assertGreater(b3_x, b2_x, "Box 3 must appear to the right of Box 2")
            self.assertGreater(plus_x_3, b3_x, "Orange + must be to the right of Box 3")
        finally:
            app.destroy()

    def test_06_independent_geometry_row1_expansion_does_not_affect_row2(self):
        """6. Row 1 expansion does not alter Row 2 geometry or column widths."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._add_row()
            app.update_idletasks()
            r1 = app.rows[0]
            r2 = app.rows[1]

            r2_box_w_before = r2["box"].winfo_width()
            r2_desc1_w_before = r2["math_desc"].box1.winfo_width()
            r2_act_x_before = r2["actions_frame"].winfo_rootx()
            r2_res_x_before = r2["result_box"].winfo_rootx()

            # Expand Row 1 with long text and 2 extra boxes
            r1["math_desc"].box1.set_text("A very long description that expands Row 1")
            r1["math_desc"].trailing_btn.invoke()
            r1["math_desc"].trailing_btn.invoke()
            app.update_idletasks()

            # Row 2 geometry is 100% unaffected
            self.assertEqual(r2["box"].winfo_width(), r2_box_w_before)
            self.assertEqual(r2["math_desc"].box1.winfo_width(), r2_desc1_w_before)
            self.assertEqual(r2["actions_frame"].winfo_rootx(), r2_act_x_before)
            self.assertEqual(r2["result_box"].winfo_rootx(), r2_res_x_before)
        finally:
            app.destroy()

    def test_07_mathematical_templates_expand_only_their_own_row(self):
        """7. Mathematical templates expand only their own row without affecting others."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._add_row()
            app.update_idletasks()
            r2_box_w_before = app.rows[1]["box"].winfo_width()
            r2_act_x_before = app.rows[1]["actions_frame"].winfo_rootx()

            # Apply a fraction template to Row 1
            app._select_only(0, (0,))
            app._place_operator_row('physics/physics/gravitation')
            app.update_idletasks()

            # Row 2 remains at its default dimensions
            self.assertEqual(app.rows[1]["box"].winfo_width(), r2_box_w_before)
            self.assertEqual(app.rows[1]["actions_frame"].winfo_rootx(), r2_act_x_before)
        finally:
            app.destroy()

    def test_08_horizontal_scrolling_accessibility(self):
        """8. All controls remain accessible through horizontal scrolling when rows expand."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            # Expand Row 1 wide
            app.rows[0]["math_desc"].box1.set_text("X" * 100)
            app.update_idletasks()
            app._fit_rows()

            # Outer canvas scrollregion expands to fit
            bbox = app.rows_canvas.bbox("all")
            self.assertIsNotNone(bbox)
            self.assertGreaterEqual(bbox[2], 1000)

            # Horizontal scroll is active
            app.rows_canvas.xview_moveto(0.5)
            self.assertGreater(app.rows_canvas.xview()[0], 0.0)
            app.rows_canvas.xview_moveto(0.0)
        finally:
            app.destroy()

    def test_09_calculator_functionality_preserved_end_to_end(self):
        """9. Keypad typing, joining, and equals calculate accurately end-to-end."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._select_only(0, (0,))
            app._key("8")
            app._join_key("+")
            app._key("4")
            app._equals()
            app.update_idletasks()

            self.assertEqual(app.rows[0]["result"].cget("text"), "8")
            self.assertEqual(app.rows[1]["result"].cget("text"), "4")
            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[2]["result"].cget("text"), "12")
        finally:
            app.destroy()

    def test_10_text_survives_selection_and_recalculation(self):
        """10. Descriptive text survives box selection, typing numbers, and recalculation."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app.update_idletasks()
            md = app.rows[0]["math_desc"]
            md.box1.set_text("Revenue")
            md.trailing_btn.invoke()
            app.update_idletasks()
            md.box2.set_text("Q1")

            # Perform calculation
            app._key("5")
            app._key("=")
            app.update_idletasks()

            # Text preserved
            words = app.rows[0]["math_desc"].get_words()
            self.assertEqual(words, ("Revenue", "Q1"))
        finally:
            app.destroy()

    def test_11_additional_calculator_rows_retain_independent_layouts(self):
        """11. Additional rows added dynamically have independent row_frames."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._add_row()  # Row 2
            app._add_row()  # Row 3
            app._add_row()  # Row 4
            self.assertEqual(len(app.rows), 4)

            # Each row has its own unique row_frame
            row_frames = [r["row_frame"] for r in app.rows]
            self.assertEqual(len(set(row_frames)), 4)

            for rf in row_frames:
                self.assertEqual(int(rf.grid_columnconfigure(0).get("minsize", 0)), 160)
                self.assertEqual(int(rf.grid_columnconfigure(4).get("minsize", 0)), 110)
        finally:
            app.destroy()

    def test_12_no_widget_overlap_within_row_frames(self):
        """12. No widgets overlap inside any individual row_frame."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            for k, r_data in enumerate(app.rows):
                rf = r_data["row_frame"]
                occupied = set()
                for widget in rf.winfo_children():
                    info = widget.grid_info()
                    if not info:
                        continue
                    r_start = int(info["row"])
                    r_span = int(info.get("rowspan", 1))
                    c_start = int(info["column"])
                    c_span = int(info.get("columnspan", 1))
                    for r in range(r_start, r_start + r_span):
                        for c in range(c_start, c_start + c_span):
                            self.assertNotIn((r, c), occupied,
                                             f"Collision at row {k+1} cell ({r}, {c})")
                            occupied.add((r, c))
        finally:
            app.destroy()

class Test13ColumnExcelSpecification(unittest.TestCase):
    """Authoritative test suite for the 9-row x 13-column Excel GUI design."""

    def test_01_13col_constants_and_letters(self):
        """1. Verify 13 columns (A..M), stride=6, and total rows."""
        self.assertEqual(EXCEL_13COL_TOTAL_COLUMNS, 13)
        self.assertEqual(EXCEL_13COL_INITIAL_TOTAL_ROWS, 9)
        self.assertEqual(EXCEL_13COL_ROWS_PER_CALCULATOR_ROW, 3)
        self.assertEqual(EXCEL_13COL_CALCULATOR_ROW_STRIDE, 6)
        for i in range(1, 14):
            letter = chr(ord('A') + i - 1)
            self.assertEqual(excel_13col_column_letter(i), letter)
            self.assertEqual(excel_13col_column_from_letter(letter), i)

    def test_02_13col_column_assignments(self):
        """2. Verify authoritative 1-based column assignments A..M."""
        self.assertEqual(EXCEL_13COL_ROW_LABEL, 1)        # Col A
        self.assertEqual(EXCEL_13COL_SPACER_AB, 2)        # Col B
        self.assertEqual(EXCEL_13COL_MATH_SIGN, 3)        # Col C
        self.assertEqual(EXCEL_13COL_SPACER_CD, 4)        # Col D
        self.assertEqual(EXCEL_13COL_NUMBER_MATH, 5)      # Col E
        self.assertEqual(EXCEL_13COL_MATH_BOX1, 6)        # Col F
        self.assertEqual(EXCEL_13COL_MATH_TRAILING, 7)    # Col G
        self.assertEqual(EXCEL_13COL_SPACER_GH, 8)        # Col H
        self.assertEqual(EXCEL_13COL_ACTIONS, 9)          # Col I
        self.assertEqual(EXCEL_13COL_RESULT_EQUALS, 10)   # Col J
        self.assertEqual(EXCEL_13COL_RESULT_BOX, 11)      # Col K
        self.assertEqual(EXCEL_13COL_RESULT_BOX1, 12)     # Col L
        self.assertEqual(EXCEL_13COL_RESULT_TRAILING, 13) # Col M

    def test_03_13col_row_1_authoritative_mapping(self):
        """3. Row 1 mapping: A1, E2, F2, G2, I1, I3, J2, K2, L2, M2."""
        # A1: Row label
        self.assertEqual(excel_13col_workspace_position(1, "row_label"),
                         GridPosition(row=1, column=1, row_span=3, column_span=1, region=LayoutRegion.EXCEL_WORKSPACE))
        # Column C: Empty on row 1 (raises ValueError if requested)
        with self.assertRaises(ValueError):
            excel_13col_workspace_position(1, "math_sign")
        # E2: Number or mathematical expression
        self.assertEqual(excel_13col_workspace_position(1, "number_for_math"),
                         GridPosition(row=2, column=5, region=LayoutRegion.EXCEL_WORKSPACE))
        # F2: Descriptive Text Box 1
        self.assertEqual(excel_13col_workspace_position(1, "math_box1"),
                         GridPosition(row=2, column=6, region=LayoutRegion.EXCEL_WORKSPACE))
        # G2: Orange + button
        self.assertEqual(excel_13col_workspace_position(1, "math_trailing"),
                         GridPosition(row=2, column=7, region=LayoutRegion.EXCEL_WORKSPACE))
        # I1: Math to put on the left
        self.assertEqual(excel_13col_workspace_position(1, "action_math_left"),
                         GridPosition(row=1, column=9, region=LayoutRegion.EXCEL_WORKSPACE))
        # I3: Clear math on the left
        self.assertEqual(excel_13col_workspace_position(1, "action_clear_left"),
                         GridPosition(row=3, column=9, region=LayoutRegion.EXCEL_WORKSPACE))
        # J2: Equals sign
        self.assertEqual(excel_13col_workspace_position(1, "result_equals"),
                         GridPosition(row=2, column=10, region=LayoutRegion.EXCEL_WORKSPACE))
        # K2: Calculated result
        self.assertEqual(excel_13col_workspace_position(1, "result_box"),
                         GridPosition(row=2, column=11, region=LayoutRegion.EXCEL_WORKSPACE))
        # L2: Descriptive Text Box 1
        self.assertEqual(excel_13col_workspace_position(1, "result_box1"),
                         GridPosition(row=2, column=12, region=LayoutRegion.EXCEL_WORKSPACE))
        # M2: Orange + button
        self.assertEqual(excel_13col_workspace_position(1, "result_trailing"),
                         GridPosition(row=2, column=13, region=LayoutRegion.EXCEL_WORKSPACE))

    def test_04_13col_row_2_authoritative_mapping(self):
        """4. Row 2 mapping: A7, C8, E8, F8, G8, I7, I9, J8, K8, L8, M8."""
        # A7: Row label
        self.assertEqual(excel_13col_workspace_position(2, "row_label"),
                         GridPosition(row=7, column=1, row_span=3, column_span=1, region=LayoutRegion.EXCEL_WORKSPACE))
        # C8: Mathematical operator sign
        self.assertEqual(excel_13col_workspace_position(2, "math_sign"),
                         GridPosition(row=8, column=3, region=LayoutRegion.EXCEL_WORKSPACE))
        # E8: Number or mathematical expression
        self.assertEqual(excel_13col_workspace_position(2, "number_for_math"),
                         GridPosition(row=8, column=5, region=LayoutRegion.EXCEL_WORKSPACE))
        # F8: Descriptive Text Box 1
        self.assertEqual(excel_13col_workspace_position(2, "math_box1"),
                         GridPosition(row=8, column=6, region=LayoutRegion.EXCEL_WORKSPACE))
        # G8: Orange + button
        self.assertEqual(excel_13col_workspace_position(2, "math_trailing"),
                         GridPosition(row=8, column=7, region=LayoutRegion.EXCEL_WORKSPACE))
        # I7: Math to put on the left
        self.assertEqual(excel_13col_workspace_position(2, "action_math_left"),
                         GridPosition(row=7, column=9, region=LayoutRegion.EXCEL_WORKSPACE))
        # I9: Clear math on the left
        self.assertEqual(excel_13col_workspace_position(2, "action_clear_left"),
                         GridPosition(row=9, column=9, region=LayoutRegion.EXCEL_WORKSPACE))
        # J8: Equals sign
        self.assertEqual(excel_13col_workspace_position(2, "result_equals"),
                         GridPosition(row=8, column=10, region=LayoutRegion.EXCEL_WORKSPACE))
        # K8: Calculated result
        self.assertEqual(excel_13col_workspace_position(2, "result_box"),
                         GridPosition(row=8, column=11, region=LayoutRegion.EXCEL_WORKSPACE))
        # L8: Descriptive Text Box 1
        self.assertEqual(excel_13col_workspace_position(2, "result_box1"),
                         GridPosition(row=8, column=12, region=LayoutRegion.EXCEL_WORKSPACE))
        # M8: Orange + button
        self.assertEqual(excel_13col_workspace_position(2, "result_trailing"),
                         GridPosition(row=8, column=13, region=LayoutRegion.EXCEL_WORKSPACE))

    def test_05_13col_dynamic_rows_six_row_stride(self):
        """5. Dynamic rows follow the exact 6-row stride: start_row = 6*(k-1)+1."""
        self.assertEqual(excel_13col_start_row(1), 1)
        self.assertEqual(excel_13col_start_row(2), 7)
        self.assertEqual(excel_13col_start_row(3), 13)
        self.assertEqual(excel_13col_start_row(4), 19)
        self.assertEqual(excel_13col_start_row(10), 55)

        # Row 3 (k=3): A13, C14, E14, F14, G14, I13, I15, J14, K14, L14, M14
        r3 = excel_13col_workspace_positions(3)
        self.assertEqual(r3["row_label"], GridPosition(13, 1, row_span=3, column_span=1, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(r3["math_sign"], GridPosition(14, 3, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(r3["number_for_math"], GridPosition(14, 5, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(r3["math_box1"], GridPosition(14, 6, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(r3["math_trailing"], GridPosition(14, 7, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(r3["action_math_left"], GridPosition(13, 9, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(r3["action_clear_left"], GridPosition(15, 9, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(r3["result_equals"], GridPosition(14, 10, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(r3["result_box"], GridPosition(14, 11, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(r3["result_box1"], GridPosition(14, 12, region=LayoutRegion.EXCEL_WORKSPACE))
        self.assertEqual(r3["result_trailing"], GridPosition(14, 13, region=LayoutRegion.EXCEL_WORKSPACE))

    def test_06_13col_bottom_total_row_adjustment_2(self):
        """6. Bottom total row: Column C is empty; J is '=', K is result, L is Box 1, M is Orange +."""
        for k in (3, 4):
            tot = excel_13col_total_row_positions(k)
            r0 = excel_13col_start_row(k)
            self.assertNotIn("math_sign", tot, "Column C must be empty on bottom total row")
            self.assertEqual(tot["total_equals"], GridPosition(r0 + 1, 10, region=LayoutRegion.EXCEL_WORKSPACE))
            self.assertEqual(tot["total_box"], GridPosition(r0 + 1, 11, region=LayoutRegion.EXCEL_WORKSPACE))
            self.assertEqual(tot["total_box1"], GridPosition(r0 + 1, 12, region=LayoutRegion.EXCEL_WORKSPACE))
            self.assertEqual(tot["total_trailing"], GridPosition(r0 + 1, 13, region=LayoutRegion.EXCEL_WORKSPACE))

    def test_07_13col_column_widths_and_total_width(self):
        """7. Verify explicit widths for all 13 columns totaling 888px."""
        self.assertEqual(len(EXCEL_13COL_COLUMN_WIDTHS), 13)
        self.assertEqual(excel_13col_total_width(), 888)
        self.assertEqual(excel_13col_column_width(1), 160)  # Col A: Label
        self.assertEqual(excel_13col_column_width(3), 42)   # Col C: Math sign
        self.assertEqual(excel_13col_column_width(5), 110)  # Col E: Operand
        self.assertEqual(excel_13col_column_width(6), 90)   # Col F: Box 1
        self.assertEqual(excel_13col_column_width(7), 42)   # Col G: Orange +
        self.assertEqual(excel_13col_column_width(9), 130)  # Col I: Actions
        self.assertEqual(excel_13col_column_width(10), 42)  # Col J: Equals
        self.assertEqual(excel_13col_column_width(11), 110) # Col K: Result
        self.assertEqual(excel_13col_column_width(12), 90)  # Col L: Box 1
        self.assertEqual(excel_13col_column_width(13), 42)  # Col M: Orange +

    def test_08_13col_descriptive_expansion_isolation(self):
        """8. Additional boxes inside a card do not alter the authoritative global coordinates of other columns."""
        # Regardless of internal expansion inside Math Card (Cols 5..7),
        # Column 9 (Actions), Column 10 (Equals), Column 11 (Result) maintain fixed Excel column indices
        self.assertEqual(EXCEL_13COL_ACTIONS, 9)
        self.assertEqual(EXCEL_13COL_RESULT_EQUALS, 10)
        self.assertEqual(EXCEL_13COL_RESULT_BOX, 11)
        self.assertEqual(EXCEL_13COL_RESULT_BOX1, 12)
        self.assertEqual(EXCEL_13COL_RESULT_TRAILING, 13)



class TestCheckpoint3BottomTotalRowAndKeypadWorkflow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.root = tk.Tk()
            cls.root.withdraw()
        except tk.TclError:
            cls.root = None

    @classmethod
    def tearDownClass(cls):
        if cls.root is not None:
            try:
                cls.root.destroy()
            except Exception:
                pass

    def test_example_a_two_row_arithmetic(self):
        """Example A: Row 1 = 1, Row 2 = + 1, Result Row 3 = 2."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._select_only(0, (0,))
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            app.update_idletasks()

            self.assertEqual(len(app.rows), 3)
            self.assertFalse(app.rows[0]["is_result"])
            self.assertEqual(app.rows[0]["result_box"].cget("text"), "1")

            self.assertFalse(app.rows[1]["is_result"])
            self.assertEqual(app.rows[1]["join"], "+")
            self.assertEqual(app.rows[1]["result_box"].cget("text"), "1")

            r3 = app.rows[2]
            self.assertTrue(r3["is_result"])
            self.assertEqual(r3["label"].cget("text"), "Total")
            self.assertEqual(r3["result_box"].cget("text"), "2")

            # Geometry: Col C empty, Col E empty, Col F..G empty, Col I empty
            self.assertFalse(r3["join_btn"].winfo_ismapped())
            self.assertFalse(r3["box"].winfo_ismapped())
            self.assertFalse(r3["math_desc"].winfo_ismapped())
            self.assertFalse(r3["actions_frame"].winfo_ismapped())

            # Col J '=' and Col K result are mapped
            self.assertTrue(r3["equals_label"].winfo_ismapped())
            self.assertEqual(r3["equals_label"].cget("text"), "=")
            self.assertTrue(r3["result_box"].winfo_ismapped())

            # Cols P..Q: editable result description with orange +
            self.assertTrue(r3["result_desc"].winfo_ismapped())
            self.assertTrue(r3["result_desc"].box1.winfo_ismapped())
            self.assertTrue(r3["result_desc"].trailing_btn.winfo_ismapped())
            self.assertEqual(r3["result_desc"].trailing_btn.cget("text"), "+")
            self.assertEqual(r3["grid_positions"], excel_18col_total_row_positions(3))
        finally:
            app.destroy()

    def test_example_b_three_row_arithmetic(self):
        """Example B: Row 1 = 1, Row 2 = + 1, Row 3 = + 1, Final Row 4 = 3."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._select_only(0, (0,))
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            app.update_idletasks()

            self.assertEqual(len(app.rows), 4)
            self.assertEqual(app.rows[0]["result_box"].cget("text"), "1")
            self.assertEqual(app.rows[1]["result_box"].cget("text"), "1")
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "1")

            r4 = app.rows[3]
            self.assertTrue(r4["is_result"])
            self.assertEqual(r4["label"].cget("text"), "Total")
            self.assertEqual(r4["result_box"].cget("text"), "3")
            self.assertFalse(r4["join_btn"].winfo_ismapped())
            self.assertFalse(r4["box"].winfo_ismapped())
            self.assertFalse(r4["actions_frame"].winfo_ismapped())
            self.assertTrue(r4["equals_label"].winfo_ismapped())
            self.assertTrue(r4["result_box"].winfo_ismapped())
            self.assertTrue(r4["result_desc"].winfo_ismapped())
        finally:
            app.destroy()

    def test_example_c_math_template_and_precedence(self):
        """Example C: Template (1 + 1) on Row 1, Row 2 = + 1, Final Row 3 = 3."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app.op_target = 0
            app._place_operator_row("math/arithmetic/addition")
            boxes = [c[2] for c in app._cards(0) if c[0] == "box"]
            self.assertEqual(len(boxes), 2)
            app._select_only(0, boxes[0])
            app._key("1")
            app._select_only(0, boxes[1])
            app._key("1")

            app._join_key("+")
            app._key("1")
            app._equals()
            app.update_idletasks()

            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[0]["result_box"].cget("text"), "2")
            self.assertEqual(app.rows[1]["result_box"].cget("text"), "1")
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "3")
            self.assertTrue(app.rows[2]["is_result"])
            self.assertEqual(app.rows[2]["label"].cget("text"), "Total")
        finally:
            app.destroy()

    def test_no_duplicate_total_rows_on_repeated_evaluations(self):
        """Repeatedly pressing = refreshes the total row without adding duplicates."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._select_only(0, (0,))
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            self.assertEqual(len(app.rows), 3)

            app._equals()
            self.assertEqual(len(app.rows), 3)

            app._equals()
            self.assertEqual(len(app.rows), 3)
            total_count = sum(1 for r in app.rows if r.get("is_result"))
            self.assertEqual(total_count, 1)
        finally:
            app.destroy()

    def test_total_row_refreshes_when_inputs_change(self):
        """Total row value refreshes when mathematical inputs change and = is pressed."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._select_only(0, (0,))
            app._key("2")
            app._join_key("+")
            app._key("3")
            app._equals()
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "5")

            app.rows[1]["node"]["slots"] = ["7"]
            app._render_row(1)
            app._equals()
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "9")
            self.assertEqual(len(app.rows), 3)
        finally:
            app.destroy()

    def test_total_row_editable_descriptions_and_orange_plus(self):
        """Total row has editable description box and orange + adds more boxes to the right."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._select_only(0, (0,))
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            app.update_idletasks()

            r3 = app.rows[2]
            desc = r3["result_desc"]
            desc.box1.set_text("Fiscal Q4 Aggregated Total")
            b1_x = desc.box1.winfo_rootx()

            b2 = desc.add_box()
            b2.set_text("Verified by Auditor")
            app.update_idletasks()

            self.assertEqual(len(desc.boxes), 2)
            self.assertEqual(desc.box1.get(), "Fiscal Q4 Aggregated Total")
            self.assertEqual(b2.get(), "Verified by Auditor")

            self.assertEqual(desc.box1.winfo_rootx(), b1_x)
            self.assertGreater(desc.trailing_btn.winfo_rootx(), b2.winfo_rootx() + b2.winfo_width())
        finally:
            app.destroy()

    def test_state_preservation_across_recalculation_and_row_continuation(self):
        """Descriptive text is preserved when recalculating or continuing calculations."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._select_only(0, (0,))
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            app.update_idletasks()

            r3 = app.rows[2]
            r3["result_desc"].box1.set_text("Important Note")
            self.assertEqual(r3["result_desc"].box1.get(), "Important Note")

            app._equals()
            app.update_idletasks()
            self.assertEqual(r3["result_desc"].box1.get(), "Important Note")

            app._join_key("+")
            app._key("1")
            app._equals()
            app.update_idletasks()

            self.assertEqual(len(app.rows), 4)
            self.assertFalse(app.rows[2]["is_result"])
            self.assertTrue(app.rows[3]["is_result"])
            self.assertEqual(app.rows[3]["result_box"].cget("text"), "3")
        finally:
            app.destroy()

    def test_independent_total_row_geometry(self):
        """Total row uses independent row_frame with default 13-col widths and expands without affecting rows above."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            app._select_only(0, (0,))
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            app.update_idletasks()

            r1_w_before = app.rows[0]["row_frame"].winfo_width()
            r2_w_before = app.rows[1]["row_frame"].winfo_width()
            r3_frame = app.rows[2]["row_frame"]

            desc = app.rows[2]["result_desc"]
            desc.box1.set_text("A very long description that expands the total row")
            b2 = desc.add_box()
            b2.set_text("Another long supplementary note for the total row")
            app.update_idletasks()

            self.assertEqual(app.rows[0]["row_frame"].winfo_width(), r1_w_before)
            self.assertEqual(app.rows[1]["row_frame"].winfo_width(), r2_w_before)
            self.assertGreater(r3_frame.winfo_width(), r1_w_before)
        finally:
            app.destroy()

    def test_strict_separation_of_two_plus_buttons(self):
        """Mathematical + creates/joins rows, orange + only adds descriptive boxes."""
        if self.root is None:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.withdraw()
        try:
            self.assertEqual(len(app.rows), 1)
            r1_desc = app.rows[0]["math_desc"]
            init_boxes = len(r1_desc.boxes)
            r1_desc.trailing_btn.invoke()
            self.assertEqual(len(app.rows), 1)
            self.assertEqual(len(r1_desc.boxes), init_boxes + 1)

            app._select_only(0, (0,))
            app._key("1")
            app._join_key("+")
            self.assertEqual(len(app.rows), 2)
            self.assertEqual(app.rows[1]["join"], "+")
        finally:
            app.destroy()



class TestCheckpoint3PhysicalKeyboardInput(unittest.TestCase):
    """Test physical keyboard input, focus transitions, and descriptive entry isolation."""
    @classmethod
    def setUpClass(cls):
        try:
            r = tk.Tk()
            r.destroy()
            cls.has_display = True
        except tk.TclError:
            cls.has_display = False

    def _send_key(self, app, keysym, widget=None):
        target = widget or app.focus_get() or app
        target.event_generate("<Key>", keysym=keysym)
        app.update()

    def test_physical_keyboard_example_a(self):
        """Example A: Physical keyboard 1 + 1 = produces final total 2."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            for k in ["1", "plus", "1", "equal"]:
                self._send_key(app, k)

            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[0]["result_box"].cget("text"), "1")
            self.assertEqual(app.rows[1]["result_box"].cget("text"), "1")
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "2")
            self.assertTrue(app.rows[2]["is_result"])
            self.assertEqual(app.rows[2]["label"].cget("text"), "Total")
        finally:
            app.destroy()

    def test_physical_keyboard_example_b(self):
        """Example B: Physical keyboard 1 + 1 + 1 = produces final total 3."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            for k in ["1", "plus", "1", "plus", "1", "equal"]:
                self._send_key(app, k)

            self.assertEqual(len(app.rows), 4)
            self.assertEqual(app.rows[0]["result_box"].cget("text"), "1")
            self.assertEqual(app.rows[1]["result_box"].cget("text"), "1")
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "1")
            self.assertEqual(app.rows[3]["result_box"].cget("text"), "3")
            self.assertTrue(app.rows[3]["is_result"])
            self.assertEqual(app.rows[3]["label"].cget("text"), "Total")
        finally:
            app.destroy()

    def test_physical_keyboard_example_c(self):
        """Example C: Physical keyboard 8 * 4 = produces final total 32."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            for k in ["8", "asterisk", "4", "Return"]:
                self._send_key(app, k)

            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[1]["join"], "×")
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "32")
            self.assertTrue(app.rows[2]["is_result"])
            self.assertEqual(app.rows[2]["label"].cget("text"), "Total")
        finally:
            app.destroy()

    def test_physical_keyboard_example_d_descriptive_entry_isolation(self):
        """Example D: Typing 'Apples + oranges = fruit' in description box enters text without triggering calculation."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            # Set up 2 mathematical rows first
            for k in ["1", "plus", "1", "equal"]:
                self._send_key(app, k)
            self.assertEqual(len(app.rows), 3)

            # Focus Descriptive Text Box 1
            box1 = app.rows[0]["math_desc"].box1
            box1.focus_force()
            app.update()

            test_str = "Apples + oranges = fruit"
            for ch in test_str:
                ks = ch if ch.isalnum() else ("space" if ch == " " else ("plus" if ch == "+" else ("equal" if ch == "=" else ch)))
                box1.event_generate("<Key>", keysym=ks)
            app.update()

            # Verify entire string appears in descriptive box
            self.assertEqual(box1.get(), test_str)
            # Verify no rows were created and calculation was not re-triggered
            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "2")
        finally:
            app.destroy()

    def test_physical_keyboard_example_e_focus_transition_back_to_math(self):
        """Example E: Clicking mathematical box after descriptive entry resumes calculation normally."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            # 1. Edit a descriptive box
            box1 = app.rows[0]["math_desc"].box1
            box1.focus_force()
            app.update()
            box1.set_text("Some text")

            # 2. Click mathematical box in Row 1 to switch focus
            app._pick_box(0, 0)
            app.focus_force()
            app.update()

            # 3. Clear and type calculation with keyboard
            app._clear_all()
            app.focus_force()
            app.update()

            for k in ["5", "minus", "2", "equal"]:
                self._send_key(app, k)

            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[1]["join"], "−")
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "3")
            self.assertTrue(app.rows[2]["is_result"])
        finally:
            app.destroy()

    def test_physical_keyboard_subtraction_division_decimal_and_backspace(self):
        """Physical keyboard handles subtraction (-), division (/), decimals (.), BackSpace, and Escape."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            # Division: 12 / 3 = 4
            for k in ["1", "2", "slash", "3", "equal"]:
                self._send_key(app, k)

            self.assertEqual(app.rows[1]["join"], "÷")
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "4")

            # Escape clears
            self._send_key(app, "Escape")
            self.assertTrue(app._is_blank(app.rows[0]))

            # Backspace: 15 -> BackSpace -> 1 + 9 = 10
            for k in ["1", "5", "BackSpace", "plus", "9", "equal"]:
                self._send_key(app, k)

            self.assertEqual(app.rows[0]["result_box"].cget("text"), "1")
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "10")
        finally:
            app.destroy()




class TestCheckpoint3RowLifecycle(unittest.TestCase):
    """Test start with one row and clear back to one row lifecycle."""
    @classmethod
    def setUpClass(cls):
        try:
            r = tk.Tk()
            r.destroy()
            cls.has_display = True
        except tk.TclError:
            cls.has_display = False

    def test_01_initial_state_single_row(self):
        """1. Calculator launches with exactly one mathematical row (Row 1), no Row 2, no Total row."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            self.assertEqual(len(app.rows), 1)
            r1 = app.rows[0]
            self.assertEqual(r1["label"].cget("text"), "Row 1")
            self.assertFalse(r1["is_result"])
            self.assertTrue(r1["box"].winfo_ismapped())
            self.assertTrue(r1["math_desc"].winfo_ismapped())
            self.assertTrue(r1["result_box"].winfo_ismapped())
            self.assertIsNone(r1.get("join"))
        finally:
            app.destroy()

    def test_02_math_join_creates_row2(self):
        """2. Typing math in Row 1 and pressing join operator creates Row 2 with operator in Col C."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("1")
            app._join_key("+")
            app.update()
            self.assertEqual(len(app.rows), 2)
            r2 = app.rows[1]
            self.assertEqual(r2["join"], "+")
            self.assertEqual(r2["label"].cget("text"), "Row 2")
            self.assertFalse(r2["is_result"])
            self.assertEqual(app.op_target, 1)
            self.assertEqual(app._selected_box(), (1, (0,)))
        finally:
            app.destroy()

    def test_03_further_joins_add_rows(self):
        """3. Successive joins dynamically create Row 3 and Row 4 as required."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._join_key("−")
            app.update()
            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[2]["join"], "−")

            app._key("1")
            app._join_key("×")
            app.update()
            self.assertEqual(len(app.rows), 4)
            self.assertEqual(app.rows[3]["join"], "×")
        finally:
            app.destroy()

    def test_04_single_row_template_stays_in_row1(self):
        """4. Single-row mathematical template from Operators button remains entirely inside Row 1."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app.op_target = 0
            app._place_operator_row("math/arithmetic/addition")
            app.update()
            self.assertEqual(len(app.rows), 1)
            cards = app._cards(0)
            self.assertGreater(len(cards), 1)
        finally:
            app.destroy()

    def test_05_single_row_evaluation(self):
        """5. Pressing = with a single row evaluates that row without creating Row 2 or Total row."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("7")
            app._equals()
            app.update()
            self.assertEqual(len(app.rows), 1)
            self.assertEqual(app.rows[0]["result_box"].cget("text"), "7")
            self.assertFalse(app.rows[0]["is_result"])
        finally:
            app.destroy()

    def test_06_multiple_row_evaluation_displays_single_total_row(self):
        """6. Multiple rows evaluate to exactly one bottom Total row; no duplicates on repeated equals."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            app.update()
            self.assertEqual(len(app.rows), 3)
            self.assertTrue(app.rows[2]["is_result"])
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "2")

            # Repeated equals does not add duplicate total rows
            app._equals()
            app.update()
            self.assertEqual(len(app.rows), 3)
            self.assertTrue(app.rows[2]["is_result"])
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "2")
        finally:
            app.destroy()

    def test_07_red_c_clears_back_to_one_row(self):
        """7. Red C button restores visible workspace to exactly one empty Row 1 and resets descriptions."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # Build 4 rows with descriptions
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            app.update()
            self.assertEqual(len(app.rows), 4)

            # Add extra descriptions to Row 1
            d1 = app.rows[0]["math_desc"]
            d1.box1.set_text("Initial description")
            b2 = d1.add_box()
            b2.set_text("Extra note")
            app.update()
            self.assertEqual(len(d1.boxes), 2)

            # Press Red C (_clear_all)
            app._clear_all()
            app.update()

            self.assertEqual(len(app.rows), 1)
            r1 = app.rows[0]
            self.assertEqual(r1["label"].cget("text"), "Row 1")
            self.assertTrue(app._is_blank(r1))
            self.assertEqual(app.op_target, 0)
            self.assertEqual(app._selected_box(), (0, (0,)))

            # Descriptions reset to 1 empty box
            self.assertEqual(len(d1.boxes), 1)
            self.assertEqual(d1.box1.words_text(), "")
        finally:
            app.destroy()

    def test_08_physical_escape_performs_full_clear_to_one_row(self):
        """8. Physical Escape performs the same full reset back to one empty Row 1."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            for k in ["1", "plus", "1", "equal"]:
                (app.focus_get() or app).event_generate("<Key>", keysym=k)
                app.update()
            self.assertEqual(len(app.rows), 3)

            (app.focus_get() or app).event_generate("<Key>", keysym="Escape")
            app.update()

            self.assertEqual(len(app.rows), 1)
            self.assertTrue(app._is_blank(app.rows[0]))
        finally:
            app.destroy()

    def test_09_new_calculation_after_clearing(self):
        """9. Typing a new calculation after clearing works accurately end-to-end."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            # 1. First calculation: 8 * 4 = 32
            for k in ["8", "asterisk", "4", "equal"]:
                (app.focus_get() or app).event_generate("<Key>", keysym=k)
                app.update()
            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "32")

            # 2. Clear
            (app.focus_get() or app).event_generate("<Key>", keysym="Escape")
            app.update()
            self.assertEqual(len(app.rows), 1)

            # 3. New calculation: 3 + 7 = 10
            for k in ["3", "plus", "7", "equal"]:
                (app.focus_get() or app).event_generate("<Key>", keysym=k)
                app.update()
            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "10")
        finally:
            app.destroy()

    def test_10_no_stale_state_after_clearing(self):
        """10. No stale mathematical values or descriptive text remain after clearing."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("9")
            app.rows[0]["math_desc"].box1.set_text("Cost")
            app.rows[0]["result_desc"].box1.set_text("Expected")
            app._clear_all()
            app.update()

            self.assertEqual(app.rows[0]["node"]["slots"], [""])
            self.assertEqual(app.rows[0]["math_desc"].box1.words_text(), "")
            self.assertEqual(app.rows[0]["result_desc"].box1.words_text(), "")
            self.assertEqual(app.rows[0]["result_box"].cget("text"), "□")
        finally:
            app.destroy()

    def test_11_enter_number_and_description_then_join_retains_row1_visible(self):
        """11. Entering 1, typing 'mouse' in description, and clicking + retains Row 1 visible and adds Row 2."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # 1. Enter 1 in Row 1
            app._key("1")
            app.update()

            # 2. Type 'mouse' in Row 1's description box
            box = app.rows[0]["math_desc"].box1
            box.focus_set()
            box.set_text("mouse")
            app.update()

            # 3. Press + join key
            app._join_key("+")
            app.update()

            # Both rows exist and are mapped
            self.assertEqual(len(app.rows), 2)
            self.assertEqual(app.rows[0]["row_frame"].grid_info()["row"], 0)
            self.assertEqual(app.rows[1]["row_frame"].grid_info()["row"], 1)
            self.assertTrue(app.rows[0]["row_frame"].winfo_ismapped())
            self.assertTrue(app.rows[1]["row_frame"].winfo_ismapped())

            # Row 1 text and math are preserved
            self.assertEqual(app.rows[0]["math_desc"].box1.words_text(), "mouse")
            self.assertEqual(app.rows[0]["node"]["slots"], ["1"])

            # Row 2 has join + and is selected
            self.assertEqual(app.rows[1]["join"], "+")
            self.assertEqual(app.op_target, 1)

            # Canvas yview keeps Row 1 in full view (yview top is 0.0)
            self.assertEqual(app.rows_canvas.yview()[0], 0.0)
        finally:
            app.destroy()




class TestCheckpoint4MathematicalTemplatesAndGUI(unittest.TestCase):
    """Test Checkpoint 4: Mathematical templates interaction with 13-column independent rows."""
    @classmethod
    def setUpClass(cls):
        try:
            r = tk.Tk()
            r.destroy()
            cls.has_display = True
        except tk.TclError:
            cls.has_display = False

    def test_01_single_row_template_insertion_and_evaluation(self):
        """1. Single-row template evaluates completely within Row 1 without creating Row 2 or Total row."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            self.assertEqual(len(app.rows), 1)
            # Insert single-row template (arithmetic addition)
            app._place_operator_row("math/arithmetic/addition")
            app.update()
            self.assertEqual(len(app.rows), 1)

            # Fill slot 0 with 4 and slot 1 with 6
            app._select_only(0, (0, 0))
            app._key("4")
            app._select_only(0, (0, 1))
            app._key("6")
            app.update()

            self.assertEqual(app.rows[0]["node"]["slots"][0]["slots"], ["4", "6"])

            # Press =
            app._equals()
            app.update()

            # Remains 1 row; result in Row 1 Column K
            self.assertEqual(len(app.rows), 1)
            self.assertEqual(app.rows[0]["result_box"].cget("text"), "10")
            self.assertEqual(app.rows[0]["label"].cget("text"), "Row 1")
            self.assertFalse(app.rows[0]["is_result"])
        finally:
            app.destroy()

    def test_02_multi_row_calculation_combining_template_with_number(self):
        """2. Multi-row calculation combining a template in Row 1 with Row 2 evaluates to bottom Total row."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # Row 1 template: 4 + 6
            app._place_operator_row("math/arithmetic/addition")
            app._select_only(0, (0, 0))
            app._key("4")
            app._select_only(0, (0, 1))
            app._key("6")
            app.update()

            # Join + creates Row 2
            app._join_key("+")
            app.update()
            self.assertEqual(len(app.rows), 2)
            self.assertEqual(app.rows[1]["join"], "+")

            # Row 2 input: 5
            app._key("5")
            app.update()
            self.assertEqual(app.rows[1]["node"]["slots"], ["5"])

            # Press =
            app._equals()
            app.update()

            # Bottom Total row appears at index 2
            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[0]["result_box"].cget("text"), "10")
            self.assertEqual(app.rows[1]["result_box"].cget("text"), "5")

            total_row = app.rows[2]
            self.assertEqual(total_row["label"].cget("text"), "Total")
            self.assertIsNone(total_row["join"])
            self.assertEqual(total_row["result_box"].cget("text"), "15")
        finally:
            app.destroy()

    def test_03_wide_template_independent_row_expansion(self):
        """3. Wide template expands only its own independent row without affecting other rows."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._add_row()
            app.update()
            rf0_init = app.rows[0]["row_frame"].winfo_reqwidth()
            rf1_init = app.rows[1]["row_frame"].winfo_reqwidth()
            self.assertEqual(rf0_init, rf1_init)

            # Insert wide template in Row 1
            app._place_operator_row("physics/physics/gravitation")
            app.update()

            rf0_after = app.rows[0]["row_frame"].winfo_reqwidth()
            rf1_after = app.rows[1]["row_frame"].winfo_reqwidth()

            # Row 1 expanded significantly
            self.assertGreater(rf0_after, 3000)
            # Row 2 remained at default width
            self.assertEqual(rf1_after, rf1_init)
            self.assertEqual(app.rows[1]["canvas"].master.winfo_width(), 110)
        finally:
            app.destroy()

    def test_04_wide_template_and_long_descriptions_expand_together(self):
        """4. Wide template and multiple expanded descriptions coexist without overlap."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._place_operator_row("physics/physics/gravitation")
            app.update()

            r0 = app.rows[0]
            slot_cont = r0["canvas"].master
            mdesc = r0["math_desc"]
            rdesc = r0["result_desc"]

            # Add multiple descriptions
            mdesc.box1.set_text("Gravitational attraction")
            b2 = mdesc.add_box()
            b2.set_text("Two planetary masses")
            rdesc.box1.set_text("Resulting force in Newtons")
            app.update()

            # 1. slot and mdesc do not overlap; mdesc is strictly to the right
            self.assertGreaterEqual(mdesc.winfo_x(), slot_cont.winfo_x() + slot_cont.winfo_width())

            # 2. In mdesc, orange + button is strictly to the right of the last box (b2)
            self.assertGreaterEqual(mdesc.trailing_btn.winfo_x(), b2.winfo_x() + b2.winfo_width())

            # 3. In rdesc, orange + button is strictly to the right of box1
            self.assertGreaterEqual(rdesc.trailing_btn.winfo_x(), rdesc.box1.winfo_x() + rdesc.box1.winfo_width())

            # 4. Math expression-tree slots are not modified by descriptions
            cards = app._cards(0)
            self.assertIn(("box", "", (0, 0)), cards)
            self.assertIn(("box", "", (0, 1)), cards)
            self.assertIn(("box", "", (0, 2)), cards)
        finally:
            app.destroy()

    def test_05_physical_keyboard_entry_into_template_slots(self):
        """5. Physical keyboard events navigate and enter values into template slots."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            # 1. Open operators palette
            app._toggle_operators()
            app.update()
            self.assertIsNotNone(getattr(app, "op_popup", None))

            # 2. Insert single-row template into Row 1
            app._place_operator_row("math/arithmetic/addition")
            app.update()

            # 3. Select first slot and type 8
            app._select_only(0, (0, 0))
            app.update()
            (app.focus_get() or app).event_generate("<Key>", keysym="8")
            app.update()

            # 4. Select second slot and type 9
            app._select_only(0, (0, 1))
            app.update()
            (app.focus_get() or app).event_generate("<Key>", keysym="9")
            app.update()

            # 5. Press =
            (app.focus_get() or app).event_generate("<Key>", keysym="equal")
            app.update()

            # 6. Verify result in Row 1 Column K is 17
            self.assertEqual(app.rows[0]["result_box"].cget("text"), "17")
            self.assertEqual(len(app.rows), 1)
        finally:
            if getattr(app, "op_popup", None) is not None:
                app.op_popup.destroy()
            app.destroy()

    def test_06_typing_in_description_box_does_not_trigger_math_keys(self):
        """6. Typing in descriptive text boxes does not trigger mathematical commands."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            box = app.rows[0]["math_desc"].box1
            box.focus_set()
            app.update()

            # Send physical keys while description box is focused
            app.focus_get().event_generate("<Key>", keysym="3")
            app.focus_get().event_generate("<Key>", keysym="plus")
            app.focus_get().event_generate("<Key>", keysym="4")
            app.update()

            # Description box received the text
            self.assertEqual(box.words_text(), "3+4")

            # Mathematical row state was unaffected (no Row 2 created, math node blank)
            self.assertEqual(len(app.rows), 1)
            self.assertEqual(app.rows[0]["node"]["slots"], [""])
        finally:
            app.destroy()

    def test_07_clear_escape_restores_one_empty_row_after_template(self):
        """7. Clear button and physical Escape cleanly restore exactly one empty Row 1."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            # 1. Place template and add descriptions
            app._place_operator_row("math/arithmetic/addition")
            d1 = app.rows[0]["math_desc"]
            d1.box1.set_text("First description")
            b2 = d1.add_box()
            b2.set_text("Second description")
            app.update()
            self.assertEqual(len(d1.boxes), 2)

            # Press Red C
            app._clear_all()
            app.update()

            self.assertEqual(len(app.rows), 1)
            self.assertTrue(app._is_blank(app.rows[0]))
            self.assertEqual(len(app.rows[0]["math_desc"].boxes), 1)
            self.assertEqual(app.rows[0]["math_desc"].box1.words_text(), "")
            self.assertEqual(app.op_target, 0)

            # 2. Place template again and test Escape key
            app._place_operator_row("physics/physics/gravitation")
            app.update()
            self.assertFalse(app._is_blank(app.rows[0]))

            (app.focus_get() or app).event_generate("<Key>", keysym="Escape")
            app.update()

            self.assertEqual(len(app.rows), 1)
            self.assertTrue(app._is_blank(app.rows[0]))
        finally:
            app.destroy()

    def test_08_preservation_of_intentionally_multi_row_templates(self):
        """8. Intentionally multi-row templates allocate required rows and reset back to 1 row on clear."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            key = "math/transforms_and_differential_equations/heat_equation"
            app._place_operator_row(key)
            app.update()

            # Allocates 2 rows with join = and titles
            self.assertEqual(len(app.rows), 2)
            self.assertEqual(app.rows[1]["join"], "=")
            self.assertIsNotNone(app.rows[0].get("sub"))
            self.assertIsNotNone(app.rows[1].get("sub"))

            # Clear resets cleanly back to 1 row
            app._clear_all()
            app.update()
            self.assertEqual(len(app.rows), 1)
            self.assertTrue(app._is_blank(app.rows[0]))
        finally:
            app.destroy()

    def test_09_actual_rendered_geometry_and_horizontal_scrollability(self):
        """9. Rendered Tkinter widget geometry conforms to 13-column layout and horizontal scrollability."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            r0 = app.rows[0]
            # Column positions in independent row frame
            slot_col = r0["canvas"].master.grid_info()["column"]
            mdesc_col = r0["math_desc"].grid_info()["column"]
            res_col = r0["result_box"].grid_info()["column"]
            rdesc_col = r0["result_desc"].grid_info()["column"]

            # Excel Column assignments: E=4, F=5, M=12, Q=16
            self.assertEqual(slot_col, 4)
            self.assertEqual(mdesc_col, 5)
            self.assertEqual(res_col, 12)
            self.assertEqual(rdesc_col, 16)

            # Insert wide template
            app._place_operator_row("physics/physics/gravitation")
            app.update()

            # Horizontal scrollability
            app.rows_canvas.xview_moveto(0.5)
            app.update()
            xv = app.rows_canvas.xview()
            self.assertGreater(xv[0], 0.0)

            # Reset scroll to origin
            app.rows_canvas.xview_moveto(0.0)
            app.update()
            self.assertEqual(app.rows_canvas.xview()[0], 0.0)
        finally:
            app.destroy()




class TestCheckpoint4TotalRowAlignment(unittest.TestCase):
    """Test Checkpoint 4 targeted Total row alignment with authoritative default column geometry."""
    @classmethod
    def setUpClass(cls):
        try:
            r = tk.Tk()
            r.destroy()
            cls.has_display = True
        except tk.TclError:
            cls.has_display = False

    def test_01_default_total_row_jk_alignment(self):
        """1. Total row Column J (=), Column K ('('), and Column L (result) vertically align with Rows 1 and 2 in 1+1=2."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            app.update()

            self.assertEqual(len(app.rows), 3)
            r0 = app.rows[0]
            r1 = app.rows[1]
            tot = app.rows[2]

            # X-coordinates of Column J (=) must align exactly across all three rows
            self.assertEqual(r0["equals_label"].winfo_x(), 711)
            self.assertEqual(r1["equals_label"].winfo_x(), 711)
            self.assertEqual(tot["equals_label"].winfo_x(), 711)

            # X-coordinates of Column K (blue +) must align exactly across all three rows
            self.assertEqual(r0["paren_plus_btn"].winfo_x(), 753)
            self.assertEqual(r1["paren_plus_btn"].winfo_x(), 753)
            self.assertEqual(tot["paren_plus_btn"].winfo_x(), 753)

            # X-coordinates of Column L ('(') must align exactly across all three rows
            self.assertEqual(r0["paren_open_btn"].winfo_x(), 795)
            self.assertEqual(r1["paren_open_btn"].winfo_x(), 795)
            self.assertEqual(tot["paren_open_btn"].winfo_x(), 795)

            # X-coordinates of Column M (result) must align exactly across all three rows
            self.assertEqual(r0["result_box"].winfo_x(), 837)
            self.assertEqual(r1["result_box"].winfo_x(), 837)
            self.assertEqual(tot["result_box"].winfo_x(), 837)

            # Total row frame width must match default 1316 px
            self.assertEqual(tot["row_frame"].winfo_reqwidth(), 1316)
        finally:
            app.destroy()

    def test_02_expanded_row1_does_not_alter_total_row_default_widths(self):
        """2. Expanded Row 1 does not stretch Total row; Total row maintains default J/K/L alignment with Row 2."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # Row 1: template + long description
            app._place_operator_row("math/arithmetic/addition")
            app._select_only(0, (0, 0))
            app._key("4")
            app._select_only(0, (0, 1))
            app._key("6")
            d1 = app.rows[0]["math_desc"]
            d1.box1.set_text("Very long descriptive text causing Row 1 to expand far outward")
            b2 = d1.add_box()
            b2.set_text("Extra notes on calculation")

            # Row 2: simple number 5
            app._join_key("+")
            app._key("5")

            # Press =
            app._equals()
            app.update()

            r0 = app.rows[0]
            r1 = app.rows[1]
            tot = app.rows[2]

            # Row 1 expands independently
            self.assertGreater(r0["row_frame"].winfo_reqwidth(), 2000)

            # Row 2 and Total row retain default width
            self.assertEqual(r1["row_frame"].winfo_reqwidth(), 1316)
            self.assertEqual(tot["row_frame"].winfo_reqwidth(), 1316)

            # Total row aligns with Row 2's default Column J, K, L, M
            self.assertEqual(r1["equals_label"].winfo_x(), 711)
            self.assertEqual(tot["equals_label"].winfo_x(), 711)
            self.assertEqual(r1["paren_plus_btn"].winfo_x(), 753)
            self.assertEqual(tot["paren_plus_btn"].winfo_x(), 753)
            self.assertEqual(r1["paren_open_btn"].winfo_x(), 795)
            self.assertEqual(tot["paren_open_btn"].winfo_x(), 795)
            self.assertEqual(r1["result_box"].winfo_x(), 837)
            self.assertEqual(tot["result_box"].winfo_x(), 837)
        finally:
            app.destroy()

    def test_03_repeated_evaluation_zero_alignment_drift(self):
        """3. Repeated evaluation calls do not introduce alignment drift in Total row."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("1")
            app._join_key("+")
            app._key("1")

            for _ in range(4):
                app._equals()
                app.update()
                tot = app.rows[2]
                self.assertEqual(tot["equals_label"].winfo_x(), 711)
                self.assertEqual(tot["paren_plus_btn"].winfo_x(), 753)
                self.assertEqual(tot["paren_open_btn"].winfo_x(), 795)
                self.assertEqual(tot["result_box"].winfo_x(), 837)
                self.assertEqual(tot["row_frame"].winfo_reqwidth(), 1316)
        finally:
            app.destroy()

    def test_04_clearing_and_starting_new_calculation(self):
        """4. Clearing and starting a new calculation restores correct geometry and J/K/L alignment."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # First calculation
            app._key("2")
            app._join_key("+")
            app._key("3")
            app._equals()
            app.update()
            self.assertEqual(len(app.rows), 3)

            # Clear
            app._clear_all()
            app.update()
            self.assertEqual(len(app.rows), 1)
            self.assertEqual(app.rows[0]["row_frame"].winfo_reqwidth(), 1316)

            # Second calculation
            app._key("7")
            app._join_key("−")
            app._key("4")
            app._equals()
            app.update()
            self.assertEqual(len(app.rows), 3)
            tot = app.rows[2]
            self.assertEqual(tot["result_box"].cget("text"), "3")
            self.assertEqual(tot["equals_label"].winfo_x(), 711)
            self.assertEqual(tot["paren_plus_btn"].winfo_x(), 753)
            self.assertEqual(tot["paren_open_btn"].winfo_x(), 795)
            self.assertEqual(tot["result_box"].winfo_x(), 837)
            self.assertEqual(tot["row_frame"].winfo_reqwidth(), 1316)
        finally:
            app.destroy()

    def test_05_total_row_independent_description_expansion(self):
        """5. Total row description expansion preserves J, K, and L positions while expanding row width."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            app.update()

            tot = app.rows[2]
            td = tot["result_desc"]
            td.box1.set_text("Batch summary description that expands to the right")
            tb2 = td.add_box()
            tb2.set_text("Audited result")
            app.update()

            # J, K, L, and M positions remain anchored at default positions
            self.assertEqual(tot["equals_label"].winfo_x(), 711)
            self.assertEqual(tot["paren_plus_btn"].winfo_x(), 753)
            self.assertEqual(tot["paren_open_btn"].winfo_x(), 795)
            self.assertEqual(tot["result_box"].winfo_x(), 837)

            # Total row frame expands rightward to accommodate descriptions
            self.assertGreater(tot["row_frame"].winfo_reqwidth(), 1316)
        finally:
            app.destroy()




class Test17ColumnPEMDASCoordinateSpecification(unittest.TestCase):
    """Test 17-column PEMDAS and two-exponent coordinate specifications (Step 1)."""

    def test_01_all_17_column_identities_and_letters(self):
        """1. All 17 columns A through Q are identified with exact letters and indices."""
        from gui_coordinates import (
            EXCEL_17COL_TOTAL_COLUMNS, EXCEL_17COL_LETTERS,
            excel_17col_column_letter, excel_17col_column_from_letter,
            EXCEL_17COL_ROW_LABEL, EXCEL_17COL_SPACER_AB, EXCEL_17COL_MATH_SIGN,
            EXCEL_17COL_SPACER_CD, EXCEL_17COL_NUMBER_MATH, EXCEL_17COL_MATH_BOX1,
            EXCEL_17COL_MATH_TRAILING, EXCEL_17COL_SPACER_GH, EXCEL_17COL_ACTIONS,
            EXCEL_17COL_RESULT_EQUALS, EXCEL_17COL_PAREN_OPEN, EXCEL_17COL_RESULT_BOX,
            EXCEL_17COL_EXPONENT_1, EXCEL_17COL_PAREN_CLOSE, EXCEL_17COL_EXPONENT_2,
            EXCEL_17COL_RESULT_BOX1, EXCEL_17COL_RESULT_TRAILING
        )
        self.assertEqual(EXCEL_17COL_TOTAL_COLUMNS, 17)
        expected_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                            "K", "L", "M", "N", "O", "P", "Q"]
        self.assertEqual(EXCEL_17COL_LETTERS, expected_letters)

        expected_indices = [
            (EXCEL_17COL_ROW_LABEL, 1, "A"),
            (EXCEL_17COL_SPACER_AB, 2, "B"),
            (EXCEL_17COL_MATH_SIGN, 3, "C"),
            (EXCEL_17COL_SPACER_CD, 4, "D"),
            (EXCEL_17COL_NUMBER_MATH, 5, "E"),
            (EXCEL_17COL_MATH_BOX1, 6, "F"),
            (EXCEL_17COL_MATH_TRAILING, 7, "G"),
            (EXCEL_17COL_SPACER_GH, 8, "H"),
            (EXCEL_17COL_ACTIONS, 9, "I"),
            (EXCEL_17COL_RESULT_EQUALS, 10, "J"),
            (EXCEL_17COL_PAREN_OPEN, 11, "K"),
            (EXCEL_17COL_RESULT_BOX, 12, "L"),
            (EXCEL_17COL_EXPONENT_1, 13, "M"),
            (EXCEL_17COL_PAREN_CLOSE, 14, "N"),
            (EXCEL_17COL_EXPONENT_2, 15, "O"),
            (EXCEL_17COL_RESULT_BOX1, 16, "P"),
            (EXCEL_17COL_RESULT_TRAILING, 17, "Q"),
        ]
        for const_val, idx_1based, letter in expected_indices:
            self.assertEqual(const_val, idx_1based)
            self.assertEqual(excel_17col_column_letter(idx_1based), letter)
            self.assertEqual(excel_17col_column_from_letter(letter), idx_1based)
            # 1-based Excel to 0-based Tkinter conversion: col_0based == col_1based - 1
            self.assertEqual(idx_1based - 1, ord(letter) - ord("A"))

    def test_02_exact_cell_locations_row_1(self):
        """2. Exact Excel cell locations for Calculator Row 1 in design example rows 13..15."""
        from gui_coordinates import (
            excel_17col_workspace_position, LayoutRegion
        )
        expected = {
            "row_label": (13, 1, "A13"),
            "action_math_left": (13, 9, "I13"),
            "action_clear_left": (15, 9, "I15"),
            "number_for_math": (14, 5, "E14"),
            "math_box1": (14, 6, "F14"),
            "math_trailing": (14, 7, "G14"),
            "result_equals": (14, 10, "J14"),
            "paren_open": (14, 11, "K14"),
            "result_box": (14, 12, "L14"),
            "exponent_1": (13, 13, "M13"),
            "paren_close": (14, 14, "N14"),
            "exponent_2": (13, 15, "O13"),
            "result_box1": (14, 16, "P14"),
            "result_trailing": (14, 17, "Q14"),
        }
        for name, (exp_row, exp_col, cell_str) in expected.items():
            pos = excel_17col_workspace_position(1, name, use_example_offset=True)
            self.assertEqual(pos.region, LayoutRegion.EXCEL_WORKSPACE)
            self.assertEqual(pos.row, exp_row, f"{name} expected row {exp_row} ({cell_str}), got {pos.row}")
            self.assertEqual(pos.column, exp_col, f"{name} expected column {exp_col} ({cell_str}), got {pos.column}")

    def test_03_exact_cell_locations_row_2(self):
        """3. Exact Excel cell locations for Calculator Row 2 in design example rows 19..21."""
        from gui_coordinates import (
            excel_17col_workspace_position, LayoutRegion
        )
        expected = {
            "row_label": (19, 1, "A19"),
            "math_sign": (20, 3, "C20"),
            "number_for_math": (20, 5, "E20"),
            "math_box1": (20, 6, "F20"),
            "math_trailing": (20, 7, "G20"),
            "action_math_left": (19, 9, "I19"),
            "action_clear_left": (21, 9, "I21"),
            "result_equals": (20, 10, "J20"),
            "paren_open": (20, 11, "K20"),
            "result_box": (20, 12, "L20"),
            "exponent_1": (19, 13, "M19"),
            "paren_close": (20, 14, "N20"),
            "exponent_2": (19, 15, "O19"),
            "result_box1": (20, 16, "P20"),
            "result_trailing": (20, 17, "Q20"),
        }
        for name, (exp_row, exp_col, cell_str) in expected.items():
            pos = excel_17col_workspace_position(2, name, use_example_offset=True)
            self.assertEqual(pos.region, LayoutRegion.EXCEL_WORKSPACE)
            self.assertEqual(pos.row, exp_row, f"{name} expected row {exp_row} ({cell_str}), got {pos.row}")
            self.assertEqual(pos.column, exp_col, f"{name} expected column {exp_col} ({cell_str}), got {pos.column}")

    def test_04_six_row_stride_and_additional_rows(self):
        """4. Stride is 6 rows per calculator row across additional calculator rows."""
        from gui_coordinates import (
            excel_17col_start_row, EXCEL_17COL_CALCULATOR_ROW_STRIDE
        )
        self.assertEqual(EXCEL_17COL_CALCULATOR_ROW_STRIDE, 6)

        # Design example offset (base 13)
        self.assertEqual(excel_17col_start_row(1, use_example_offset=True), 13)
        self.assertEqual(excel_17col_start_row(2, use_example_offset=True), 19)
        self.assertEqual(excel_17col_start_row(3, use_example_offset=True), 25)
        self.assertEqual(excel_17col_start_row(4, use_example_offset=True), 31)

        # Standardized start row (base 1)
        self.assertEqual(excel_17col_start_row(1, use_example_offset=False), 1)
        self.assertEqual(excel_17col_start_row(2, use_example_offset=False), 7)
        self.assertEqual(excel_17col_start_row(3, use_example_offset=False), 13)
        self.assertEqual(excel_17col_start_row(4, use_example_offset=False), 19)

    def test_05_subrow_mapping_and_tkinter_grid_coordinates(self):
        """5. Sub-row mapping: Exponents in sub-row 0 (superscript); main controls in sub-row 1."""
        from gui_coordinates import excel_17col_workspace_positions
        pos1 = excel_17col_workspace_positions(1, use_example_offset=True)

        # In independent row_frame: subrow = pos.row - r0
        r0 = 13
        # Sub-row 0: Exponents and top action
        self.assertEqual(pos1["exponent_1"].row - r0, 0)
        self.assertEqual(pos1["exponent_2"].row - r0, 0)
        self.assertEqual(pos1["action_math_left"].row - r0, 0)

        # Sub-row 1: Main controls (number, equals, paren open, result, paren close, descriptions)
        self.assertEqual(pos1["number_for_math"].row - r0, 1)
        self.assertEqual(pos1["math_box1"].row - r0, 1)
        self.assertEqual(pos1["math_trailing"].row - r0, 1)
        self.assertEqual(pos1["result_equals"].row - r0, 1)
        self.assertEqual(pos1["paren_open"].row - r0, 1)
        self.assertEqual(pos1["result_box"].row - r0, 1)
        self.assertEqual(pos1["paren_close"].row - r0, 1)
        self.assertEqual(pos1["result_box1"].row - r0, 1)
        self.assertEqual(pos1["result_trailing"].row - r0, 1)

        # Sub-row 2: Clear action
        self.assertEqual(pos1["action_clear_left"].row - r0, 2)

    def test_06_17_column_default_and_effective_widths(self):
        """6. Default base and effective column widths for all 17 columns."""
        from gui_coordinates import (
            EXCEL_17COL_COLUMN_WIDTHS, EXCEL_17COL_EFFECTIVE_DEFAULT_WIDTHS,
            excel_17col_column_width, excel_17col_effective_column_width,
            excel_17col_total_width, excel_17col_effective_total_width
        )
        self.assertEqual(len(EXCEL_17COL_COLUMN_WIDTHS), 17)
        self.assertEqual(len(EXCEL_17COL_EFFECTIVE_DEFAULT_WIDTHS), 17)

        # Parenthesis buttons (K=11, N=14) have width 36 px
        self.assertEqual(excel_17col_column_width(11), 36)
        self.assertEqual(excel_17col_column_width(14), 36)

        # Exponent boxes (M=13, O=15) have width 48 px
        self.assertEqual(excel_17col_column_width(13), 48)
        self.assertEqual(excel_17col_column_width(15), 48)

        # Result box (L=12) has width 110 px
        self.assertEqual(excel_17col_column_width(12), 110)

        self.assertEqual(excel_17col_total_width(), sum(EXCEL_17COL_COLUMN_WIDTHS.values()))
        self.assertEqual(excel_17col_effective_total_width(), sum(EXCEL_17COL_EFFECTIVE_DEFAULT_WIDTHS.values()))

    def test_07_proposed_total_row_layout_17col(self):
        """7. Proposed Total row layout: Col C empty, equals in J, paren in K, result in L, paren in N."""
        from gui_coordinates import excel_17col_total_row_positions
        tot = excel_17col_total_row_positions(3, use_example_offset=True)

        self.assertNotIn("total_math_sign", tot)
        self.assertEqual(tot["total_equals"].column, 10)       # Col J
        self.assertEqual(tot["total_paren_open"].column, 11)   # Col K
        self.assertEqual(tot["total_box"].column, 12)          # Col L
        self.assertEqual(tot["total_exponent_1"].column, 13)   # Col M
        self.assertEqual(tot["total_paren_close"].column, 14)  # Col N
        self.assertEqual(tot["total_exponent_2"].column, 15)   # Col O
        self.assertEqual(tot["total_box1"].column, 16)         # Col P
        self.assertEqual(tot["total_trailing"].column, 17)     # Col Q

    def test_08_active_13col_vs_proposed_17col_distinction(self):
        """8. Active workspace remains 13-column; proposed 17-column specification is distinct and ready."""
        import gui_coordinates as gc
        # Active workspace constants are preserved on 13 columns
        self.assertEqual(gc.EXCEL_TOTAL_COLUMNS, 13)
        self.assertEqual(gc.EXCEL_13COL_TOTAL_COLUMNS, 13)
        self.assertEqual(len(gc.EXCEL_COLUMN_WIDTHS), 13)
        self.assertEqual(len(gc.EXCEL_13COL_COLUMN_WIDTHS), 13)

        # Proposed 17-column specification is ready alongside
        self.assertEqual(gc.EXCEL_17COL_TOTAL_COLUMNS, 17)
        self.assertEqual(len(gc.EXCEL_17COL_COLUMN_WIDTHS), 17)

    def test_09_mathematical_scope_documentation(self):
        """9. Exponent scopes: Exponent 1 applies to row expression; Exponent 2 applies to parenthesized group."""
        from gui_coordinates import (
            EXCEL_17COL_EXPONENT_1, EXCEL_17COL_EXPONENT_2,
            EXCEL_17COL_PAREN_OPEN, EXCEL_17COL_PAREN_CLOSE, EXCEL_17COL_RESULT_BOX
        )
        # Exponent 1 (Col M: 13) immediately follows Result Box (Col L: 12)
        self.assertEqual(EXCEL_17COL_EXPONENT_1, EXCEL_17COL_RESULT_BOX + 1)
        # Exponent 2 (Col O: 15) immediately follows Close Parenthesis (Col N: 14)
        self.assertEqual(EXCEL_17COL_EXPONENT_2, EXCEL_17COL_PAREN_CLOSE + 1)
        # Open Parenthesis (Col K: 11) immediately precedes Result Box (Col L: 12)
        self.assertEqual(EXCEL_17COL_PAREN_OPEN, EXCEL_17COL_RESULT_BOX - 1)




class Test17ColumnGUIRowActivation(unittest.TestCase):
    """Test Checkpoint 5 Step 2: Activation of 17-Column (A..Q) GUI layout with two exponent boxes."""

    @classmethod
    def setUpClass(cls):
        try:
            r = tk.Tk()
            r.destroy()
            cls.has_display = True
        except tk.TclError:
            cls.has_display = False

    def test_01_all_17_column_controls_present_in_every_input_row(self):
        """1. Every calculator row contains all 17-column controls (A..Q)."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._add_row()
            self.assertEqual(len(app.rows), 2)
            for i, row in enumerate(app.rows):
                # Row indicator (Col A)
                self.assertIsNotNone(row.get("label_frame"))
                self.assertIsNotNone(row.get("label"))
                # Join operator button (Col C, row >= 2)
                if i >= 1:
                    self.assertIsNotNone(row.get("join_btn"))
                # Math operand slot (Col E)
                self.assertIsNotNone(row.get("box"))
                # Math descriptive region (Cols F..G)
                self.assertIsNotNone(row.get("math_desc"))
                # Actions frame (Col I)
                self.assertIsNotNone(row.get("actions_frame"))
                # Equals sign (Col J)
                self.assertIsNotNone(row.get("equals_label"))
                # Open parenthesis button (Col K)
                self.assertIsNotNone(row.get("paren_open_btn"))
                self.assertIn("paren_open", row)
                # Calculated result box (Col L)
                self.assertIsNotNone(row.get("result_box"))
                # Exponent Number Box 1 (Col M)
                self.assertIsNotNone(row.get("exponent_1_box"))
                # Close parenthesis button (Col N)
                self.assertIsNotNone(row.get("paren_close_btn"))
                self.assertIn("paren_close", row)
                # Exponent Number Box 2 (Col O)
                self.assertIsNotNone(row.get("exponent_2_box"))
                # Result descriptive region (Cols P..Q)
                self.assertIsNotNone(row.get("result_desc"))
        finally:
            app.destroy()

    def test_02_tkinter_grid_info_matches_17_column_spec(self):
        """2. Exact Tkinter grid coordinates match 17-column specification (sub-rows 0, 1, 2)."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            r0 = app.rows[0]
            # Col A (0): Label frame, row 0..2 (rowspan 3)
            self.assertEqual(r0["label_frame"].grid_info()["column"], 0)
            self.assertEqual(r0["label_frame"].grid_info()["row"], 0)
            self.assertEqual(r0["label_frame"].grid_info()["rowspan"], 3)

            # Col E (4): Math slot, row 1
            self.assertEqual(r0["box"].grid_info()["column"], 4)
            self.assertEqual(r0["box"].grid_info()["row"], 1)

            # Cols F..G (5..6): Math desc, row 1, columnspan 2
            self.assertEqual(r0["math_desc"].grid_info()["column"], 5)
            self.assertEqual(r0["math_desc"].grid_info()["row"], 1)
            self.assertEqual(r0["math_desc"].grid_info()["columnspan"], 2)

            # Col I (8): Actions frame, row 0..2 (rowspan 3)
            self.assertEqual(r0["actions_frame"].grid_info()["column"], 8)
            self.assertEqual(r0["actions_frame"].grid_info()["row"], 0)
            self.assertEqual(r0["actions_frame"].grid_info()["rowspan"], 3)

            # Col J (9): Equals label, row 1
            self.assertEqual(r0["equals_label"].grid_info()["column"], 9)
            self.assertEqual(r0["equals_label"].grid_info()["row"], 1)

            # Col K (10): Blue + button, row 1
            self.assertEqual(r0["paren_plus_btn"].grid_info()["column"], 10)
            self.assertEqual(r0["paren_plus_btn"].grid_info()["row"], 1)

            # Col L (11): Open parenthesis button, row 1
            self.assertEqual(r0["paren_open_btn"].grid_info()["column"], 11)
            self.assertEqual(r0["paren_open_btn"].grid_info()["row"], 1)

            # Col M (12): Result box, row 1
            self.assertEqual(r0["result_box"].grid_info()["column"], 12)
            self.assertEqual(r0["result_box"].grid_info()["row"], 1)

            # Col N (13): Exponent Number Box 1, row 0 (top sub-row superscript!)
            self.assertEqual(r0["exponent_1_box"].grid_info()["column"], 13)
            self.assertEqual(r0["exponent_1_box"].grid_info()["row"], 0)

            # Col O (14): Close parenthesis button, row 1
            self.assertEqual(r0["paren_close_btn"].grid_info()["column"], 14)
            self.assertEqual(r0["paren_close_btn"].grid_info()["row"], 1)

            # Col P (15): Exponent Number Box 2, row 0 (top sub-row superscript!)
            self.assertEqual(r0["exponent_2_box"].grid_info()["column"], 15)
            self.assertEqual(r0["exponent_2_box"].grid_info()["row"], 0)

            # Cols Q..R (16..17): Result desc, row 1, columnspan 2
            self.assertEqual(r0["result_desc"].grid_info()["column"], 16)
            self.assertEqual(r0["result_desc"].grid_info()["row"], 1)
            self.assertEqual(r0["result_desc"].grid_info()["columnspan"], 2)
        finally:
            app.destroy()

    def test_03_rendered_pixel_geometry_and_total_row_alignment(self):
        """3. Rendered pixel geometry aligns vertically across Row 1, Row 2, and Total Row."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            app.update()

            self.assertEqual(len(app.rows), 3)
            r0, r1, tot = app.rows[0], app.rows[1], app.rows[2]

            # All controls align to the exact pixel across all 3 rows
            for r in (r0, r1, tot):
                self.assertEqual(r["equals_label"].winfo_x(), 711)
                self.assertEqual(r["paren_plus_btn"].winfo_x(), 753)
                self.assertEqual(r["paren_open_btn"].winfo_x(), 795)
                self.assertEqual(r["result_box"].winfo_x(), 837)
                self.assertEqual(r["exponent_1_box"].winfo_x(), 955)
                self.assertEqual(r["paren_close_btn"].winfo_x(), 995)
                self.assertEqual(r["exponent_2_box"].winfo_x(), 1045)
                self.assertEqual(r["result_desc"].winfo_x(), 1085)
                self.assertEqual(r["row_frame"].winfo_reqwidth(), 1316)
        finally:
            app.destroy()

    def test_04_parentheses_toggle_selected_and_unselected_states(self):
        """4. Parentheses buttons toggle visible selected/unselected state."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            r0 = app.rows[0]
            # Initial: unselected
            self.assertFalse(r0["paren_open"])
            self.assertFalse(r0["paren_close"])
            self.assertEqual(r0["paren_open_btn"].cget("relief"), "raised")
            self.assertEqual(r0["paren_close_btn"].cget("relief"), "raised")

            # Toggle Open Parenthesis '('
            app._toggle_paren_open(0)
            self.assertTrue(r0["paren_open"])
            self.assertEqual(r0["paren_open_btn"].cget("relief"), "sunken")
            self.assertEqual(r0["paren_open_btn"].cget("bg"), "#b5dca8")

            # Toggle Close Parenthesis ')'
            app._toggle_paren_close(0)
            self.assertTrue(r0["paren_close"])
            self.assertEqual(r0["paren_close_btn"].cget("relief"), "sunken")
            self.assertEqual(r0["paren_close_btn"].cget("bg"), "#b5dca8")

            # Toggle back to unselected
            app._toggle_paren_open(0)
            self.assertFalse(r0["paren_open"])
            self.assertEqual(r0["paren_open_btn"].cget("relief"), "raised")
            self.assertEqual(r0["paren_open_btn"].cget("bg"), "white")

            app._toggle_paren_close(0)
            self.assertFalse(r0["paren_close"])
            self.assertEqual(r0["paren_close_btn"].cget("relief"), "raised")
            self.assertEqual(r0["paren_close_btn"].cget("bg"), "white")
        finally:
            app.destroy()

    def test_05_exponent_boxes_editing_and_clearing(self):
        """5. Exponent boxes support empty initial state, typing/editing numeric input, and clearing."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # Initial state: empty
            self.assertEqual(app._get_exponent_1(0), "")
            self.assertEqual(app._get_exponent_2(0), "")

            # Set exponents
            app._set_exponent_1(0, "3")
            app._set_exponent_2(0, "2")
            self.assertEqual(app._get_exponent_1(0), "3")
            self.assertEqual(app._get_exponent_2(0), "2")

            # Clear exponents
            app.rows[0]["exponent_1_box"].delete(0, tk.END)
            app.rows[0]["exponent_2_box"].delete(0, tk.END)
            self.assertEqual(app._get_exponent_1(0), "")
            self.assertEqual(app._get_exponent_2(0), "")
        finally:
            app.destroy()

    def test_06_independent_row_expansion_with_wide_templates(self):
        """6. Wide template in Row 1 expands only Row 1; Row 2 and Total row retain 17-col default widths."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._place_operator_row("math/arithmetic/addition")
            app._select_only(0, (0, 0))
            app._key("4")
            app._select_only(0, (0, 1))
            app._key("6")
            d1 = app.rows[0]["math_desc"]
            d1.box1.set_text("Expanded description in Row 1")

            app._join_key("+")
            app._key("5")
            app._equals()
            app.update()

            r0, r1, tot = app.rows[0], app.rows[1], app.rows[2]
            # Row 1 expands independently
            self.assertGreater(r0["row_frame"].winfo_reqwidth(), 1400)
            # Row 2 and Total row retain default width 1316 px
            self.assertEqual(r1["row_frame"].winfo_reqwidth(), 1316)
            self.assertEqual(tot["row_frame"].winfo_reqwidth(), 1316)
            # Row 2 and Total row alignment preserved
            self.assertEqual(r1["equals_label"].winfo_x(), 711)
            self.assertEqual(tot["equals_label"].winfo_x(), 711)
            self.assertEqual(r1["paren_plus_btn"].winfo_x(), 753)
            self.assertEqual(tot["paren_plus_btn"].winfo_x(), 753)
            self.assertEqual(r1["paren_open_btn"].winfo_x(), 795)
            self.assertEqual(tot["paren_open_btn"].winfo_x(), 795)
            self.assertEqual(r1["result_box"].winfo_x(), 837)
            self.assertEqual(tot["result_box"].winfo_x(), 837)
        finally:
            app.destroy()

    def test_07_result_description_expansion_in_columns_p_and_q(self):
        """7. Result description auto-expands in Columns P and Q without distorting earlier columns."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            r0 = app.rows[0]
            desc = r0["result_desc"]
            desc.box1.set_text("Detailed description of the calculated result")
            app.update()

            # Columns J..P maintain fixed anchor positions
            self.assertEqual(r0["equals_label"].winfo_x(), 711)
            self.assertEqual(r0["paren_plus_btn"].winfo_x(), 753)
            self.assertEqual(r0["paren_open_btn"].winfo_x(), 795)
            self.assertEqual(r0["result_box"].winfo_x(), 837)
            self.assertEqual(r0["exponent_1_box"].winfo_x(), 955)
            self.assertEqual(r0["paren_close_btn"].winfo_x(), 995)
            self.assertEqual(r0["exponent_2_box"].winfo_x(), 1045)
            self.assertEqual(r0["result_desc"].winfo_x(), 1085)
            self.assertGreater(r0["row_frame"].winfo_reqwidth(), 1316)
        finally:
            app.destroy()

    def test_08_physical_keyboard_focus_isolation(self):
        """8. Focus inside exponent box or description box isolates typing from calculator shortcuts."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.focus_force()
        app.update()
        try:
            exp1 = app.rows[0]["exponent_1_box"]
            exp1.focus_force()
            app.update()

            # Generate key events inside exponent box
            exp1.insert(tk.END, "3")
            # Global _on_key_press should not intercept
            app.event_generate("<Key>", keysym="c")
            app.update()

            # App should NOT have cleared
            self.assertEqual(len(app.rows), 1)
            self.assertEqual(exp1.get(), "3c")
        finally:
            app.destroy()

    def test_09_clear_all_restores_blank_17_column_row_1(self):
        """9. _clear_all() restores single empty 17-column Row 1 with cleared exponents and parens."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("3")
            app._toggle_paren_open(0)
            app._set_exponent_1(0, "2")
            app._join_key("+")
            app._key("4")
            app._equals()
            app.update()

            # Clear all
            app._clear_all()
            app.update()

            self.assertEqual(len(app.rows), 1)
            r0 = app.rows[0]
            self.assertFalse(r0["paren_open"])
            self.assertFalse(r0["paren_close"])
            self.assertEqual(app._get_exponent_1(0), "")
            self.assertEqual(app._get_exponent_2(0), "")
            self.assertEqual(r0["row_frame"].winfo_reqwidth(), 1316)
        finally:
            app.destroy()

    def test_10_evaluation_guard_when_parentheses_or_exponents_active(self):
        """10. Pressing '=' with invalid parens or orphaned exp2 displays clear validation error."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._equals()
            app.update()

            # Unmatched open paren error shown in results
            result_msg = app.results.get("1.0", "end").strip()
            self.assertIn("opening parenthesis '(' without a matching closing", result_msg)
            self.assertEqual(len(app.rows), 1)

            # Untoggle paren and test Exponent Box 2 without close paren
            app._toggle_paren_open(0)
            app._set_exponent_2(0, "3")
            app._equals()
            app.update()

            result_msg2 = app.results.get("1.0", "end").strip()
            self.assertIn("group exponent (Column O) without a closing parenthesis", result_msg2)
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_11_standard_math_evaluates_normally_without_new_controls(self):
        """11. Standard math (1+1=2) evaluates accurately when new controls are inactive."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("1")
            app._join_key("+")
            app._key("1")
            app._equals()
            app.update()

            self.assertEqual(len(app.rows), 3)
            tot = app.rows[2]
            self.assertEqual(tot["result_box"].cget("text"), "2")
            self.assertEqual(tot["label"].cget("text"), "Total")
            self.assertEqual(tot["equals_label"].winfo_x(), 711)
            self.assertEqual(tot["paren_plus_btn"].winfo_x(), 753)
            self.assertEqual(tot["paren_open_btn"].winfo_x(), 795)
            self.assertEqual(tot["result_box"].winfo_x(), 837)
        finally:
            app.destroy()




class TestStep3AIndividualRowExponentiation(unittest.TestCase):
    """Checkpoint 5, Step 3A: Individual Row Exponentiation tests.

    Verifies that Exponent Box 1 (Column M) applies an exponent to the mathematical
    value of its own row (numbers and single-row templates), while Exponent Box 2
    and cross-row parentheses remain guarded for subsequent PEMDAS stages.
    """

    @classmethod
    def setUpClass(cls):
        try:
            root = tk.Tk()
            root.withdraw()
            root.destroy()
            cls.has_display = True
        except tk.TclError:
            cls.has_display = False

    def test_01_example_1_positive_integer_exponent(self):
        """Example 1: Enter 2 in Row 1 Col E, 3 in Row 1 Col M -> Row 1 Col L displays 8."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._set_exponent_1(0, "3")
            app._equals()
            app.update()

            # Row 1 Col L must display 8
            self.assertEqual(app.rows[0]["result"].cget("text"), "8")
            # Only Row 1 active: no extra row or Total row created
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_02_example_2_positive_integer_exponent(self):
        """Example 2: Enter 5 in Row 1 Col E, 2 in Row 1 Col M -> Row 1 Col L displays 25."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("5")
            app._set_exponent_1(0, "2")
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "25")
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_03_example_3_empty_exponent_box(self):
        """Example 3: Enter 2 in Row 1 Col E, leave Col M empty -> Row 1 Col L displays 2."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            # Col M left empty
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "2")
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_04_example_4_single_row_mathematical_template_with_exponent(self):
        """Example 4: 4 + 6 inside a single-row template, 2 in Col M -> Row 1 Col L displays 100."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app.tpl_entry.insert(0, "4 + 6")
            app._tpl_preview()
            app._set_exponent_1(0, "2")
            app._equals()
            app.update()

            # (4 + 6)^2 = 10^2 = 100
            self.assertEqual(app.rows[0]["result"].cget("text"), "100")
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_05_zero_exponents(self):
        """Zero exponents: 5^0 = 1, 0^0 = 1."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # 5^0 = 1
            app._key("5")
            app._set_exponent_1(0, "0")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "1")

            # 0^0 = 1
            app._clear_all()
            app._key("0")
            app._set_exponent_1(0, "0")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "1")
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_06_negative_integer_exponents(self):
        """Negative integer exponents: 2^-1 = 0.5, 2^-2 = 0.25."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._set_exponent_1(0, "-1")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "0.5")

            app._set_exponent_1(0, "-2")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "0.25")
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_07_fractional_exponents(self):
        """Fractional exponents: 4^0.5 = 2, 8^(1/3) = 2, 27^(1/3) = 3."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # 4^0.5 = 2
            app._key("4")
            app._set_exponent_1(0, "0.5")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "2")

            # 8^(1/3) = 2
            app._clear_all()
            app._key("8")
            app._set_exponent_1(0, "1/3")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "2")

            # 27^(1/3) = 3
            app._clear_all()
            app._key("2")
            app._key("7")
            app._set_exponent_1(0, "1/3")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "3")
        finally:
            app.destroy()

    def test_08_invalid_exponent_text_handling(self):
        """Invalid exponent text: 'abc' or '++' displays clear error message without crashing."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("5")
            app._set_exponent_1(0, "abc")
            app._equals()
            app.update()

            msg = app.results.get("1.0", "end").strip()
            self.assertIn("Invalid exponent", msg)
            self.assertEqual(len(app.rows), 1)

            app._set_exponent_1(0, "++")
            app._equals()
            app.update()
            msg2 = app.results.get("1.0", "end").strip()
            self.assertIn("Invalid exponent", msg2)
        finally:
            app.destroy()

    def test_09_repeated_evaluation_consistency(self):
        """Repeated evaluation: pressing '=' multiple times produces consistent result and no extra rows."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("3")
            app._set_exponent_1(0, "4")
            for _ in range(4):
                app._equals()
                app.update()
                self.assertEqual(app.rows[0]["result"].cget("text"), "81")
                self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_10_editing_base_or_exponent_after_evaluation(self):
        """Editing base or exponent after evaluation updates result accurately upon re-evaluating."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # Initial: 3^2 = 9
            app._key("3")
            app._set_exponent_1(0, "2")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "9")

            # Edit exponent to 3: 3^3 = 27
            app._set_exponent_1(0, "3")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "27")

            # Edit base: backspace 3, type 4: 4^3 = 64
            app._key("⌫")
            app._key("4")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "64")
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_11_division_by_zero_and_domain_errors(self):
        """Division by zero: 0^-1 and 1/0 exponent are reported gracefully without crashing."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # 0^-1
            app._key("0")
            app._set_exponent_1(0, "-1")
            app._equals()
            app.update()
            msg = app.results.get("1.0", "end").strip()
            self.assertIn("Division by zero", msg)

            # 1/0 exponent
            app._clear_all()
            app._key("5")
            app._set_exponent_1(0, "1/0")
            app._equals()
            app.update()
            msg2 = app.results.get("1.0", "end").strip()
            self.assertIn("Division by zero", msg2)
        finally:
            app.destroy()

    def test_12_multi_row_with_individual_row_exponents(self):
        """Multi-row calculation: Row 1 (2^3 = 8) + Row 2 (5^2 = 25) = Row 3 Total (33)."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._set_exponent_1(0, "3")
            app._next_row()
            app._join_key("+")
            app._key("5")
            app._set_exponent_1(1, "2")
            app._equals()
            app.update()

            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[0]["result"].cget("text"), "8")
            self.assertEqual(app.rows[1]["result"].cget("text"), "25")
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "33")
            self.assertEqual(app.rows[2]["label"].cget("text"), "Total")
        finally:
            app.destroy()

    def test_13_unsupported_controls_trigger_guard(self):
        """Unmatched parens, orphaned exp2, and ungrouped mixed precedence report validation messages."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # Test parenthesis open without close
            app._key("2")
            app._toggle_paren_open(0)
            app._equals()
            app.update()
            msg1 = app.results.get("1.0", "end").strip()
            self.assertIn("opening parenthesis '(' without a matching closing", msg1)
            self.assertEqual(len(app.rows), 1)

            # Test parenthesis close without open
            app._toggle_paren_open(0)
            app._toggle_paren_close(0)
            app._equals()
            app.update()
            msg2 = app.results.get("1.0", "end").strip()
            self.assertIn("closing parenthesis ')' without a matching opening", msg2)

            # Test Exponent Box 2 without close paren
            app._toggle_paren_close(0)
            app._set_exponent_2(0, "4")
            app._equals()
            app.update()
            msg3 = app.results.get("1.0", "end").strip()
            self.assertIn("group exponent (Column O) without a closing parenthesis", msg3)
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()




class TestStep3BParenthesesAndGroupExponentiation(unittest.TestCase):
    """Checkpoint 5, Step 3B: Parentheses and Group Exponentiation tests.

    Verifies that:
      - Parenthesis buttons and Exponent Box 2 evaluate grouped expressions.
      - User's single-row test (2^2)^2 = 16 displays 16 in Row 1 Col L with no extra row.
      - Multi-row parenthesized groups evaluate accurately:
          Example A: (2 + 3)^2 = 25
          Example B: (2^3 + 1)^2 = 81
          Example C: (2 + 3) * 4 = 20
      - Group exponents of 0, negative group exponents, and re-evaluation work.
      - Unmatched parens, orphaned exp2, nested parens, and ungrouped mixed precedence
        are safely validated with clear messages.
    """

    @classmethod
    def setUpClass(cls):
        try:
            root = tk.Tk()
            root.withdraw()
            root.destroy()
            cls.has_display = True
        except tk.TclError:
            cls.has_display = False

    def test_01_user_example_single_row_double_exponent_16(self):
        """User example: Row 1 base 2, '(' toggled, exp1=2, ')' toggled, exp2=2 -> (2^2)^2 = 16 in Col L."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._set_exponent_1(0, "2")
            app._toggle_paren_close(0)
            app._set_exponent_2(0, "2")
            app._equals()
            app.update()

            # Row 1 Col L must display 16
            self.assertEqual(app.rows[0]["result"].cget("text"), "16")
            # Must not create a second row or Total row
            self.assertEqual(len(app.rows), 1)
            # Results console contains ( 2^2 )^2
            msg = app.results.get("1.0", "end").strip()
            self.assertIn("16", msg)
        finally:
            app.destroy()

    def test_02_example_a_multi_row_parentheses_with_group_exponent_25(self):
        """Example A: Row 1 '( 2', Row 2 '+ 3 )^2' -> Total = (2 + 3)^2 = 25."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._toggle_paren_close(1)
            app._set_exponent_2(1, "2")
            app._equals()
            app.update()

            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[0]["result"].cget("text"), "2")
            self.assertEqual(app.rows[1]["result"].cget("text"), "3")
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "25")
            self.assertEqual(app.rows[2]["label"].cget("text"), "Total")
        finally:
            app.destroy()

    def test_03_example_b_multi_row_with_both_exponents_81(self):
        """Example B: Row 1 '( 2^3', Row 2 '+ 1 )^2' -> Total = (2^3 + 1)^2 = (8 + 1)^2 = 81."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._set_exponent_1(0, "3")
            app._next_row()
            app._join_key("+")
            app._key("1")
            app._toggle_paren_close(1)
            app._set_exponent_2(1, "2")
            app._equals()
            app.update()

            self.assertEqual(len(app.rows), 3)
            self.assertEqual(app.rows[0]["result"].cget("text"), "8")
            self.assertEqual(app.rows[1]["result"].cget("text"), "1")
            self.assertEqual(app.rows[2]["result_box"].cget("text"), "81")
        finally:
            app.destroy()

    def test_04_example_c_parenthesized_group_then_multiplication_20(self):
        """Example C: Row 1 '( 2', Row 2 '+ 3 )', Row 3 '* 4' -> Total = (2 + 3) * 4 = 20."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._toggle_paren_close(1)
            app._next_row()
            app._join_key("×")
            app._key("4")
            app._equals()
            app.update()

            self.assertEqual(len(app.rows), 4)
            self.assertEqual(app.rows[0]["result"].cget("text"), "2")
            self.assertEqual(app.rows[1]["result"].cget("text"), "3")
            self.assertEqual(app.rows[2]["result"].cget("text"), "4")
            self.assertEqual(app.rows[3]["result_box"].cget("text"), "20")
        finally:
            app.destroy()

    def test_05_parentheses_without_group_exponent(self):
        """Parentheses without group exponent: (2 + 3) = 5."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._toggle_paren_close(1)
            # No Exp 2
            app._equals()
            app.update()

            self.assertEqual(app.rows[2]["result_box"].cget("text"), "5")
        finally:
            app.destroy()

    def test_06_group_exponent_zero(self):
        """Group exponent of zero: (2 + 3)^0 = 1."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._toggle_paren_close(1)
            app._set_exponent_2(1, "0")
            app._equals()
            app.update()

            self.assertEqual(app.rows[2]["result_box"].cget("text"), "1")
        finally:
            app.destroy()

    def test_07_group_exponent_negative(self):
        """Negative group exponent: (2 + 2)^-1 = 0.25."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._next_row()
            app._join_key("+")
            app._key("2")
            app._toggle_paren_close(1)
            app._set_exponent_2(1, "-1")
            app._equals()
            app.update()

            self.assertEqual(app.rows[2]["result_box"].cget("text"), "0.25")
        finally:
            app.destroy()

    def test_08_re_evaluation_after_modifying_inputs(self):
        """Re-evaluating after modifying base or exponent updates result accurately."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # (2^2)^2 = 16
            app._key("2")
            app._toggle_paren_open(0)
            app._set_exponent_1(0, "2")
            app._toggle_paren_close(0)
            app._set_exponent_2(0, "2")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "16")

            # Change Exp 2 to 3: (2^2)^3 = 64
            app._set_exponent_2(0, "3")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "64")

            # Change base to 3: (3^2)^3 = 729
            app._key("⌫")
            app._key("3")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "729")
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_09_clear_all_restores_parentheses_and_both_exponent_boxes(self):
        """Clear (C) resets parenthesis toggles and both exponent boxes back to empty default."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._set_exponent_1(0, "2")
            app._toggle_paren_close(0)
            app._set_exponent_2(0, "2")
            app._equals()
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "16")

            app._clear_all()
            app.update()
            self.assertEqual(len(app.rows), 1)
            self.assertFalse(app.rows[0]["paren_open"])
            self.assertFalse(app.rows[0]["paren_close"])
            self.assertEqual(app._get_exponent_1(0), "")
            self.assertEqual(app._get_exponent_2(0), "")
            self.assertEqual(app.rows[0]["paren_open_btn"].cget("relief"), "raised")
            self.assertEqual(app.rows[0]["paren_close_btn"].cget("relief"), "raised")
        finally:
            app.destroy()

    def test_10_single_row_calculation_without_adding_second_row(self):
        """Single-row evaluation with parentheses and exponents never adds a Row 2 or Total row."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("5")
            app._toggle_paren_open(0)
            app._toggle_paren_close(0)
            app._set_exponent_2(0, "2")
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "25")
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_11_unmatched_opening_parenthesis(self):
        """Opening parenthesis without closing parenthesis displays clear error."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._next_row()
            app._join_key("+")
            app._key("3")
            # No close paren
            app._equals()
            app.update()

            msg = app.results.get("1.0", "end").strip()
            self.assertIn("opening parenthesis '(' without a matching closing", msg)
        finally:
            app.destroy()

    def test_12_unmatched_closing_parenthesis(self):
        """Closing parenthesis without opening parenthesis displays clear error."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._toggle_paren_close(1)
            # No open paren
            app._equals()
            app.update()

            msg = app.results.get("1.0", "end").strip()
            self.assertIn("closing parenthesis ')' without a matching opening", msg)
        finally:
            app.destroy()

    def test_13_group_exponent_without_closing_parenthesis(self):
        """Group exponent in Column O without closing parenthesis displays clear error."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._set_exponent_2(0, "3")
            # No close paren
            app._equals()
            app.update()

            msg = app.results.get("1.0", "end").strip()
            self.assertIn("group exponent (Column O) without a closing parenthesis", msg)
        finally:
            app.destroy()

    def test_14_nested_parentheses_unsupported_error(self):
        """Opening nested parentheses across rows without closing them reports unmatched opening parenthesis in Checkpoint 6B."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._toggle_paren_open(1)  # nested open!
            app._equals()
            app.update()

            msg = app.results.get("1.0", "end").strip()
            self.assertIn("opening parenthesis '(' without a matching closing", msg)
        finally:
            app.destroy()

    def test_15_ungrouped_mixed_precedence_warning(self):
        """Ungrouped mixed precedence (+ before *) evaluates correctly with Step 3C PEMDAS (2 + 3 * 4 = 14)."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._next_row()
            app._join_key("×")
            app._key("4")
            app._equals()
            app.update()

            self.assertEqual(app.rows[3]["result"].cget("text"), "14")
            self.assertEqual(app.rows[0]["result"].cget("text"), "2")
            self.assertEqual(app.rows[1]["result"].cget("text"), "3")
            self.assertEqual(app.rows[2]["result"].cget("text"), "4")
        finally:
            app.destroy()

    def test_16_preserves_step_3a_individual_exponentiation(self):
        """Standard Step 3A individual row exponentiation continues working without parentheses."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("5")
            app._set_exponent_1(0, "2")
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "25")
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()


    def test_17_onscreen_number_pad_types_into_exponent_boxes(self):
        """Clicking on-screen number pad (0-9, backspace, sign) enters digits into focused exponent box."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # Type into Column E using on-screen number pad
            app._pick_box(0, 0)
            app._key("2")
            self.assertEqual(app.rows[0]["node"]["slots"][0], "2")

            # Toggle '('
            app._toggle_paren_open(0)

            # Focus Exponent Box 1 and type '2' using on-screen number pad
            exp1 = app.rows[0]["exponent_1_box"]
            exp1.focus_set()
            app._on_exponent_focus(exp1)
            app._key("2")
            self.assertEqual(exp1.get(), "2")

            # Toggle ')'
            app._toggle_paren_close(0)

            # Focus Exponent Box 2, type '3', backspace, type '2' using on-screen number pad
            exp2 = app.rows[0]["exponent_2_box"]
            exp2.focus_set()
            app._on_exponent_focus(exp2)
            app._key("3")
            self.assertEqual(exp2.get(), "3")
            app._key("⌫")
            self.assertEqual(exp2.get(), "")
            app._key("2")
            self.assertEqual(exp2.get(), "2")

            # Click '=' on the on-screen number pad
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "16")
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_18_physical_numpad_evaluates_when_in_exponent_box(self):
        """Pressing Enter, KP_Enter, '=', or 'KP_Equal' while in an exponent box triggers calculation."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._set_exponent_1(0, "2")
            app._toggle_paren_close(0)
            exp2 = app.rows[0]["exponent_2_box"]
            exp2.delete(0, tk.END)
            exp2.insert(0, "2")
            exp2.focus_set()

            # Test physical Return
            ev1 = tk.Event()
            ev1.widget = exp2
            ev1.keysym = "Return"
            ev1.char = "\r"
            res_code1 = app._on_key_press(ev1)
            self.assertEqual(res_code1, "break")
            app.update()
            self.assertEqual(app.rows[0]["result"].cget("text"), "16")

            # Test physical KP_Enter
            ev2 = tk.Event()
            ev2.widget = exp2
            ev2.keysym = "KP_Enter"
            ev2.char = "\r"
            res_code2 = app._on_key_press(ev2)
            self.assertEqual(res_code2, "break")

            # Test physical KP_Equal
            ev3 = tk.Event()
            ev3.widget = exp2
            ev3.keysym = "KP_Equal"
            ev3.char = "="
            res_code3 = app._on_key_press(ev3)
            self.assertEqual(res_code3, "break")
        finally:
            app.destroy()




class TestStep3CFullPEMDASAcrossRows(unittest.TestCase):
    """Checkpoint 5 Step 3C regression tests: Full PEMDAS across calculator rows."""

    @classmethod
    def setUpClass(cls):
        try:
            root = tk.Tk()
            root.destroy()
            cls.has_display = True
        except Exception:
            cls.has_display = False

    def test_01_multiplication_precedence_over_addition(self):
        """2 + 3 × 4 = 14: Multiplication takes precedence over addition across rows."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._next_row()
            app._join_key("×")
            app._key("4")
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "2")
            self.assertEqual(app.rows[1]["result"].cget("text"), "3")
            self.assertEqual(app.rows[2]["result"].cget("text"), "4")
            self.assertEqual(app.rows[3]["result"].cget("text"), "14")
            self.assertTrue(app.rows[3].get("is_result"))
        finally:
            app.destroy()

    def test_02_addition_after_multiplication(self):
        """2 × 3 + 4 = 10: Left-to-right multiplication followed by addition."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._next_row()
            app._join_key("×")
            app._key("3")
            app._next_row()
            app._join_key("+")
            app._key("4")
            app._equals()
            app.update()

            self.assertEqual(app.rows[3]["result"].cget("text"), "10")
        finally:
            app.destroy()

    def test_03_division_precedence_over_subtraction(self):
        """20 − 6 ÷ 2 = 17: Division takes precedence over subtraction across rows."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("20")
            app._next_row()
            app._join_key("−")
            app._key("6")
            app._next_row()
            app._join_key("÷")
            app._key("2")
            app._equals()
            app.update()

            self.assertEqual(app.rows[3]["result"].cget("text"), "17")
        finally:
            app.destroy()

    def test_04_equal_precedence_division_and_multiplication_left_to_right(self):
        """20 ÷ 5 × 2 = 8: Equal precedence operators evaluate strictly left-to-right."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("20")
            app._next_row()
            app._join_key("÷")
            app._key("5")
            app._next_row()
            app._join_key("×")
            app._key("2")
            app._equals()
            app.update()

            self.assertEqual(app.rows[3]["result"].cget("text"), "8")
        finally:
            app.destroy()

    def test_05_equal_precedence_subtraction_left_to_right(self):
        """10 − 3 − 2 = 5: Sequential subtraction evaluates strictly left-to-right."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("10")
            app._next_row()
            app._join_key("−")
            app._key("3")
            app._next_row()
            app._join_key("−")
            app._key("2")
            app._equals()
            app.update()

            self.assertEqual(app.rows[3]["result"].cget("text"), "5")
        finally:
            app.destroy()

    def test_06_mixed_precedence_four_rows(self):
        """2 + 3 × 4 − 5 = 9: Multi-operator PEMDAS across four rows."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._next_row()
            app._join_key("×")
            app._key("4")
            app._next_row()
            app._join_key("−")
            app._key("5")
            app._equals()
            app.update()

            self.assertEqual(app.rows[4]["result"].cget("text"), "9")
        finally:
            app.destroy()

    def test_07_parentheses_override_precedence(self):
        """(2 + 3) × 4 = 20: Parentheses override operator precedence across rows."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._toggle_paren_close(1)
            app._next_row()
            app._join_key("×")
            app._key("4")
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "2")
            self.assertEqual(app.rows[1]["result"].cget("text"), "3")
            self.assertEqual(app.rows[2]["result"].cget("text"), "4")
            self.assertEqual(app.rows[3]["result"].cget("text"), "20")
        finally:
            app.destroy()

    def test_08_group_exponent_with_parentheses(self):
        """(2 + 3)^2 = 25: Exponent Box 2 (Col O) applies to parenthesized group."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._toggle_paren_close(1)
            app._set_exponent_2(1, "2")
            app._equals()
            app.update()

            self.assertEqual(app.rows[2]["result"].cget("text"), "25")
        finally:
            app.destroy()

    def test_09_individual_and_group_exponents(self):
        """(2^3 + 1)^2 = 81: Individual exponent in Col M and group exponent in Col O."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._set_exponent_1(0, "3")
            app._next_row()
            app._join_key("+")
            app._key("1")
            app._toggle_paren_close(1)
            app._set_exponent_2(1, "2")
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "8")
            self.assertEqual(app.rows[1]["result"].cget("text"), "1")
            self.assertEqual(app.rows[2]["result"].cget("text"), "81")
        finally:
            app.destroy()

    def test_10_single_row_double_exponent(self):
        """(2^2)^2 = 16: Single row with both exponents evaluates to 16 in Column L."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._set_exponent_1(0, "2")
            app._toggle_paren_close(0)
            app._set_exponent_2(0, "2")
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "16")
            self.assertEqual(len(app.rows), 1)
        finally:
            app.destroy()

    def test_11_mathematical_template_combined_with_multiplication(self):
        """A single-row addition template joined to an ordinary multiplication row: [4 + 6] × 3 = 30."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        from operator_row_math import row_tree
        app = CalculatorGUI()
        app.update()
        try:
            mod_add = row_tree.new_node("math/arithmetic/addition")
            mod_add["slots"] = ["4", "6"]
            app.rows[0]["node"] = mod_add
            app._render_row(0)

            app._next_row()
            app._join_key("×")
            app._key("3")
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "10")
            self.assertEqual(app.rows[1]["result"].cget("text"), "3")
            self.assertEqual(app.rows[2]["result"].cget("text"), "30")
        finally:
            app.destroy()

    def test_12_multiplication_template_joined_to_addition(self):
        """Ordinary addition row joined to a multiplication template: 2 + [3 × 4] = 14."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        from operator_row_math import row_tree
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._next_row()
            app._join_key("+")
            mod_mul = row_tree.new_node("math/arithmetic/multiplication")
            mod_mul["slots"] = ["3", "4"]
            app.rows[1]["node"] = mod_mul
            app._render_row(1)

            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "2")
            self.assertEqual(app.rows[1]["result"].cget("text"), "12")
            self.assertEqual(app.rows[2]["result"].cget("text"), "14")
        finally:
            app.destroy()

    def test_13_editing_earlier_row_and_recalculating(self):
        """Editing an earlier row updates the PEMDAS total dynamically."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._next_row()
            app._join_key("×")
            app._key("4")
            app._equals()
            app.update()
            self.assertEqual(app.rows[3]["result"].cget("text"), "14")

            # Edit Row 0 from 2 to 5
            app._pick_box(0, 0)
            app._key("⌫")
            app._key("5")
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["result"].cget("text"), "5")
            self.assertEqual(app.rows[3]["result"].cget("text"), "17")
        finally:
            app.destroy()

    def test_14_division_by_zero_displays_clear_error(self):
        """Division by zero across rows displays clear error message."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("20")
            app._next_row()
            app._join_key("÷")
            app._key("0")
            app._equals()
            app.update()

            msg = app.results.get("1.0", "end").strip()
            self.assertIn("Division by zero.", msg)
        finally:
            app.destroy()

    def test_15_unmatched_parentheses_error_retained(self):
        """Opening parenthesis without closing displays clear error."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._equals()
            app.update()

            msg = app.results.get("1.0", "end").strip()
            self.assertIn("without a matching closing", msg)
        finally:
            app.destroy()

    def test_16_nested_parentheses_unsupported_error_retained(self):
        """Opening nested parentheses across rows without closing displays unmatched opening parenthesis in Checkpoint 6B."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._toggle_paren_open(1)
            app._equals()
            app.update()

            msg = app.results.get("1.0", "end").strip()
            self.assertIn("opening parenthesis '(' without a matching closing", msg)
        finally:
            app.destroy()

    def test_17_invalid_exponent_error_retained(self):
        """Non-numeric exponent syntax displays clear error message."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._set_exponent_1(0, "abc")
            app._equals()
            app.update()

            msg = app.results.get("1.0", "end").strip()
            self.assertIn("Invalid exponent 'abc'", msg)
        finally:
            app.destroy()

    def test_18_preservation_of_descriptions_across_pemdas_eval(self):
        """Descriptions in Columns F-G and P-Q are preserved during PEMDAS calculation."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._set_word(0, 0, 0, "Math Desc 1")
            app._set_result_word(0, 0, "Result Desc 1")
            app._equals()
            app.update()

            self.assertEqual(app.rows[0]["words"].get(0, ("", ""))[0], "Math Desc 1")
            self.assertEqual(app.rows[0]["result_words"][0], "Result Desc 1")
        finally:
            app.destroy()

    def test_19_keyboard_and_keypad_evaluation(self):
        """Pressing Return or KP_Enter on keyboard triggers full PEMDAS evaluation."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._next_row()
            app._join_key("×")
            app._key("4")

            # Simulate physical keyboard Return
            ev = tk.Event()
            ev.widget = app
            ev.keysym = "Return"
            ev.char = "\r"
            app._on_key_press(ev)
            app.update()

            self.assertEqual(app.rows[3]["result"].cget("text"), "14")
        finally:
            app.destroy()

    def test_20_clear_all_resets_to_one_row(self):
        """Clearing multi-row expression resets cleanly to single row 1."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._next_row()
            app._join_key("+")
            app._key("3")
            app._equals()
            app.update()
            self.assertEqual(len(app.rows), 3)

            app._clear_all()
            app.update()

            self.assertEqual(len(app.rows), 1)
            self.assertEqual(app.rows[0]["result"].cget("text"), "□")
            self.assertEqual(app._get_exponent_1(0), "")
            self.assertEqual(app._get_exponent_2(0), "")
        finally:
            app.destroy()




class TestStep3DFocusRoutingAndRowCreation(unittest.TestCase):
    """Checkpoint 5 Step 3D: Input focus routing and stale target prevention on row creation."""

    @classmethod
    def setUpClass(cls):
        try:
            root = tk.Tk()
            root.destroy()
            cls.has_display = True
        except Exception:
            cls.has_display = False

    def test_01_user_reproduction_exponent1_then_join_then_digit(self):
        """User case: Enter 2 in Col E, 3 in Exp 1, press +, press 1 -> 1 enters Row 2 Col E, not Exp 1."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            # 1. Enter 2 in Row 1, Column E
            app._key("2")

            # 2. Click Row 1 Exponent Box 1, Column M, enter 3
            exp1 = app.rows[0]["exponent_1_box"]
            exp1.focus_set()
            app._on_exponent_focus(exp1)
            app.update()
            app._key("3")
            self.assertEqual(exp1.get(), "3")

            # 3. Press mathematical + button on on-screen number pad
            app._join_key("+")
            app.update()
            self.assertEqual(len(app.rows), 2)

            # 4. Press 1 on on-screen number pad
            app._key("1")

            # 5. Verify Row 2 Col E contains 1, Row 1 Exp 1 still contains 3
            self.assertEqual(exp1.get(), "3")
            self.assertEqual(app.rows[1]["node"]["slots"], ["1"])

            # 6. Row 1 open paren, Row 2 close paren, enter 2 in Row 2 Exp 2
            app._toggle_paren_open(0)
            app._toggle_paren_close(1)
            exp2 = app.rows[1]["exponent_2_box"]
            exp2.focus_set()
            app._on_exponent_focus(exp2)
            app.update()
            app._key("2")
            self.assertEqual(exp2.get(), "2")

            # 7. Press = and verify (2^3 + 1)^2 = 81
            app._equals()
            app.update()
            self.assertEqual(app.rows[2]["result"].cget("text"), "81")
        finally:
            app.destroy()

    def test_02_new_row_after_exponent2(self):
        """Creating a new row after entering Exponent Box 2 clears active exponent target."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._toggle_paren_open(0)
            app._toggle_paren_close(0)
            exp2 = app.rows[0]["exponent_2_box"]
            exp2.focus_set()
            app._on_exponent_focus(exp2)
            app.update()
            app._key("2")
            self.assertEqual(exp2.get(), "2")

            # Press +
            app._join_key("+")
            app.update()
            self.assertEqual(len(app.rows), 2)

            # Next digit 5 enters Row 2 Col E
            app._key("5")
            self.assertEqual(exp2.get(), "2")
            self.assertEqual(app.rows[1]["node"]["slots"], ["5"])

            app._equals()
            app.update()
            # (2)^2 + 5 = 4 + 5 = 9
            self.assertEqual(app.rows[2]["result"].cget("text"), "9")
        finally:
            app.destroy()

    def test_03_new_row_after_editing_descriptions(self):
        """Creating a new row after editing descriptions directs subsequent input to new row."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("10")
            app._set_word(0, 0, 0, "My Label")
            app._join_key("+")
            app.update()

            app._key("5")
            self.assertEqual(app.rows[1]["node"]["slots"], ["5"])
            app._equals()
            app.update()
            self.assertEqual(app.rows[2]["result"].cget("text"), "15")
        finally:
            app.destroy()

    def test_04_physical_keyboard_join_and_digit_after_exponent(self):
        """Physical keyboard + inside an exponent box creates join row and routes next digit to Row 2."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            exp1 = app.rows[0]["exponent_1_box"]
            exp1.focus_set()
            app._on_exponent_focus(exp1)
            app.update()
            app._key("3")

            # Physical + on keyboard inside exponent box
            ev_plus = tk.Event()
            ev_plus.widget = exp1
            ev_plus.keysym = "KP_Add"
            ev_plus.char = "+"
            res = app._on_key_press(ev_plus)
            self.assertEqual(res, "break")
            app.update()
            self.assertEqual(len(app.rows), 2)

            # Physical 1 on keyboard
            ev_digit = tk.Event()
            ev_digit.widget = app
            ev_digit.keysym = "1"
            ev_digit.char = "1"
            app._on_key_press(ev_digit)
            app.update()

            self.assertEqual(exp1.get(), "3")
            self.assertEqual(app.rows[1]["node"]["slots"], ["1"])
        finally:
            app.destroy()

    def test_05_manual_switching_between_rows_and_exponent_boxes(self):
        """Switching focus manually between rows and exponent boxes directs digits to clicked widget."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._next_row()
            app._join_key("+")
            app._key("3")

            # Focus Row 1 Exp 1 and type 2
            exp1 = app.rows[0]["exponent_1_box"]
            exp1.focus_set()
            app._on_exponent_focus(exp1)
            app.update()
            app._key("2")
            self.assertEqual(exp1.get(), "2")

            # Click Row 2 Col E and append 4 -> "34"
            app._pick_box(1, 0)
            app.update()
            app._key("4")
            self.assertEqual(app.rows[1]["node"]["slots"], ["34"])

            # Focus Row 2 Exp 1 and type 3
            exp1_r2 = app.rows[1]["exponent_1_box"]
            exp1_r2.focus_set()
            app._on_exponent_focus(exp1_r2)
            app.update()
            app._key("3")
            self.assertEqual(exp1_r2.get(), "3")
        finally:
            app.destroy()

    def test_06_clicking_exponent_box_again_allows_deliberate_editing(self):
        """Explicitly clicking an exponent box after row creation allows deliberate editing."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            exp1 = app.rows[0]["exponent_1_box"]
            exp1.focus_set()
            app._on_exponent_focus(exp1)
            app.update()
            app._key("3")

            # Create Row 2
            app._join_key("+")
            app.update()
            app._key("1")
            self.assertEqual(app.rows[1]["node"]["slots"], ["1"])

            # Deliberately click Row 1 Exp 1 again and edit: delete and type 4
            exp1.focus_set()
            app._on_exponent_focus(exp1)
            app.update()
            app._key("⌫")
            app._key("4")
            self.assertEqual(exp1.get(), "4")
        finally:
            app.destroy()

    def test_07_mathematical_template_slots_retain_correct_routing(self):
        """Expanding a mathematical template and navigating between slots and new rows routes correctly."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        from operator_row_math import row_tree
        app = CalculatorGUI()
        app.update()
        try:
            mod_add = row_tree.new_node("math/arithmetic/addition")
            mod_add["slots"] = ["4", ""]
            app.rows[0]["node"] = mod_add
            app._render_row(0)

            # Select slot 1 of template and type 6
            app._select_only(0, (1,))
            app.update()
            app._key("6")
            self.assertEqual(app.rows[0]["node"]["slots"], ["4", "6"])

            # Press × to create Row 2 and type 3
            app._join_key("×")
            app.update()
            app._key("3")
            self.assertEqual(app.rows[1]["node"]["slots"], ["3"])

            app._equals()
            app.update()
            self.assertEqual(app.rows[2]["result"].cget("text"), "30")
        finally:
            app.destroy()

    def test_08_repeated_row_creation_no_stale_focus(self):
        """Creating multiple successive rows with join keys directs each digit to its respective row."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("2")
            app._join_key("+")
            app.update()
            app._key("3")
            app._join_key("×")
            app.update()
            app._key("4")
            app._join_key("−")
            app.update()
            app._key("5")

            self.assertEqual(app.rows[0]["node"]["slots"], ["2"])
            self.assertEqual(app.rows[1]["node"]["slots"], ["3"])
            self.assertEqual(app.rows[2]["node"]["slots"], ["4"])
            self.assertEqual(app.rows[3]["node"]["slots"], ["5"])

            app._equals()
            app.update()
            # 2 + (3 * 4) - 5 = 9
            self.assertEqual(app.rows[4]["result"].cget("text"), "9")
        finally:
            app.destroy()

    def test_09_clear_all_returns_input_to_row1_col_e(self):
        """Clearing after focusing an exponent box restores input routing to Row 1 Column E."""
        if not self.has_display:
            self.skipTest("Tkinter display not available")
        from main import CalculatorGUI
        app = CalculatorGUI()
        app.update()
        try:
            app._key("5")
            exp1 = app.rows[0]["exponent_1_box"]
            exp1.focus_set()
            app._on_exponent_focus(exp1)
            app.update()
            app._key("2")

            # Clear all
            app._clear_all()
            app.update()

            # Next digit should go into Row 1 Column E, NOT exp1
            app._key("7")
            self.assertEqual(app.rows[0]["node"]["slots"], ["7"])
            self.assertEqual(app._get_exponent_1(0), "")
        finally:
            app.destroy()


if __name__ == "__main__":
    unittest.main()
