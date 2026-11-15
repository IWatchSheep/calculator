"""Focused unit tests for the common GUI coordinate convention."""
import os
import sys
import tkinter as tk
import unittest
from dataclasses import FrozenInstanceError

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from gui_coordinates import (ARROW_CENTER_POSITION, ARROW_GRID_POSITIONS,
                             GridPosition, LayoutRegion, arrow_at_position)
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

        # Center button is attached and positioned at row 2, column 2
        self.assertTrue(hasattr(card, "center_btn"))
        self.assertEqual(card.center_btn.grid_pos, ARROW_CENTER_POSITION)
        info = card.center_btn.grid_info()
        self.assertEqual(int(info["row"]), 1)     # zero-based row 1 = logical row 2
        self.assertEqual(int(info["column"]), 1)  # zero-based column 1 = logical column 2

        # Trigger callback
        card.center_btn.invoke()
        self.assertEqual(picked, [True])

        # Verify all 9 arrow buttons/center exist inside the grid frame
        grid_frame = card.winfo_children()[1]  # child 0: lead button, child 1: arrow grid
        self.assertTrue(hasattr(grid_frame, "arrow_buttons"))
        self.assertEqual(len(grid_frame.arrow_buttons), 9)

        for pos, btn_widget in grid_frame.arrow_buttons.items():
            btn_info = btn_widget.grid_info()
            self.assertEqual(int(btn_info["row"]), pos.row - 1)
            self.assertEqual(int(btn_info["column"]), pos.column - 1)
            if pos == ARROW_CENTER_POSITION:
                self.assertEqual(btn_widget.cget("text"), "□")
            else:
                self.assertEqual(btn_widget.cget("text"), ARROW_GRID_POSITIONS[pos])
                self.assertEqual(btn_widget.cget("relief"), "groove")


if __name__ == "__main__":
    unittest.main()
