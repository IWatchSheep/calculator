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
    CARD_ARROW_GRID_POSITION,
    CARD_COMPONENT_POSITIONS,
    CARD_CONTEXT_POSITION,
    CARD_LABEL_POSITION,
    CARD_LEAD_BUTTON_POSITION,
    CARD_TRAILING_BUTTON_POSITION,
    GridPosition,
    LayoutRegion,
    arrow_at_position,
    card_component_position,
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


class TestCardComponentCoordinates(unittest.TestCase):
    """Test the five surrounding card components' coordinates, spans, and widget mapping."""

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
        """Verify the exact 1-based coordinates and spans for all five card components."""
        expected = {
            "lead_button": (1, 1, 3, 1),
            "arrow_grid": (1, 2, 3, 1),
            "label_entry": (1, 3, 3, 1),
            "context_entry": (1, 4, 3, 1),
            "trailing_button": (1, 5, 3, 1),
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
        self.assertEqual(CARD_LEAD_BUTTON_POSITION, CARD_COMPONENT_POSITIONS["lead_button"])
        self.assertEqual(CARD_ARROW_GRID_POSITION, CARD_COMPONENT_POSITIONS["arrow_grid"])
        self.assertEqual(CARD_LABEL_POSITION, CARD_COMPONENT_POSITIONS["label_entry"])
        self.assertEqual(CARD_CONTEXT_POSITION, CARD_COMPONENT_POSITIONS["context_entry"])
        self.assertEqual(CARD_TRAILING_BUTTON_POSITION, CARD_COMPONENT_POSITIONS["trailing_button"])

        # Check friendly aliases
        self.assertEqual(CARD_COMPONENT_POSITIONS["blue_plus"], CARD_LEAD_BUTTON_POSITION)
        self.assertEqual(CARD_COMPONENT_POSITIONS["item_entry"], CARD_LABEL_POSITION)
        self.assertEqual(CARD_COMPONENT_POSITIONS["orange_plus"], CARD_TRAILING_BUTTON_POSITION)

        # Reverse lookup by GridPosition
        self.assertEqual(CARD_COMPONENT_POSITIONS[CARD_LEAD_BUTTON_POSITION], "lead_button")
        self.assertEqual(CARD_COMPONENT_POSITIONS[CARD_ARROW_GRID_POSITION], "arrow_grid")
        self.assertEqual(CARD_COMPONENT_POSITIONS[CARD_LABEL_POSITION], "label_entry")
        self.assertEqual(CARD_COMPONENT_POSITIONS[CARD_CONTEXT_POSITION], "context_entry")
        self.assertEqual(CARD_COMPONENT_POSITIONS[CARD_TRAILING_BUTTON_POSITION], "trailing_button")

    def test_card_components_are_unique(self):
        """All five components have distinct, non-overlapping columns."""
        positions = [
            CARD_LEAD_BUTTON_POSITION,
            CARD_ARROW_GRID_POSITION,
            CARD_LABEL_POSITION,
            CARD_CONTEXT_POSITION,
            CARD_TRAILING_BUTTON_POSITION,
        ]
        self.assertEqual(len(positions), 5)
        self.assertEqual(len(set(positions)), 5)
        columns = [p.column for p in positions]
        self.assertEqual(columns, [1, 2, 3, 4, 5])

        # Verify no two components overlap
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                self.assertFalse(positions[i].overlaps(positions[j]))

    def test_card_components_tkinter_grid_conversion(self):
        """Verify conversion to Tkinter zero-based grid parameters."""
        expected_tk = {
            "lead_button": {"row": 0, "column": 0, "rowspan": 3, "columnspan": 1},
            "arrow_grid": {"row": 0, "column": 1, "rowspan": 3, "columnspan": 1},
            "label_entry": {"row": 0, "column": 2, "rowspan": 3, "columnspan": 1},
            "context_entry": {"row": 0, "column": 3, "rowspan": 3, "columnspan": 1},
            "trailing_button": {"row": 0, "column": 4, "rowspan": 3, "columnspan": 1},
        }
        for name, tk_dict in expected_tk.items():
            pos = CARD_COMPONENT_POSITIONS[name]
            self.assertEqual(pos.to_tkinter_grid(), tk_dict)

    def test_nested_arrow_grid_isolation(self):
        """Arrow grid outer container is in CARD_COMPONENT, inner arrows in ARROW_GRID."""
        self.assertEqual(CARD_ARROW_GRID_POSITION.region, LayoutRegion.CARD_COMPONENT)
        self.assertEqual(ARROW_CENTER_POSITION.region, LayoutRegion.ARROW_GRID)
        # Even though both have coordinates in row 1-3, col 2, different regions never overlap
        self.assertFalse(CARD_ARROW_GRID_POSITION.overlaps(ARROW_CENTER_POSITION))

    def test_make_component_surrounding_widgets_and_behavior(self):
        """make_component creates and positions all five components with preserved behavior."""
        if self.root is None:
            self.skipTest("Tkinter display not available")

        picked = []
        card = make_component(
            self.root,
            center="□",
            kind="number",
            lead="+",
            on_pick=lambda: picked.append("picked"),
        )

        # 1. Check card_controls dictionary
        self.assertTrue(hasattr(card, "card_controls"))
        self.assertEqual(len(card.card_controls), 5)

        # 2. Check Blue plus / lead button
        self.assertTrue(hasattr(card, "lead_btn"))
        self.assertEqual(card.lead_btn.grid_pos, CARD_LEAD_BUTTON_POSITION)
        info_lead = card.lead_btn.grid_info()
        self.assertEqual(int(info_lead["row"]), 0)
        self.assertEqual(int(info_lead["column"]), 0)
        self.assertEqual(int(info_lead["rowspan"]), 3)
        self.assertEqual(card.lead_btn.cget("text"), "+")
        card.lead_btn.invoke()
        self.assertIn("picked", picked)

        # 3. Check Directional arrow grid container
        grid_frame = card.card_controls[CARD_ARROW_GRID_POSITION]
        self.assertEqual(grid_frame.grid_pos, CARD_ARROW_GRID_POSITION)
        info_grid = grid_frame.grid_info()
        self.assertEqual(int(info_grid["row"]), 0)
        self.assertEqual(int(info_grid["column"]), 1)
        self.assertEqual(int(info_grid["rowspan"]), 3)

        # 4. Check Label placeholder button (words=None)
        self.assertTrue(hasattr(card, "label_btn"))
        self.assertEqual(card.label_btn.grid_pos, CARD_LABEL_POSITION)
        info_label = card.label_btn.grid_info()
        self.assertEqual(int(info_label["row"]), 0)
        self.assertEqual(int(info_label["column"]), 2)
        self.assertEqual(int(info_label["rowspan"]), 3)
        self.assertEqual(card.label_btn.cget("text"), "[Item]")

        # 5. Check Context placeholder button (words=None)
        self.assertTrue(hasattr(card, "context_btn"))
        self.assertEqual(card.context_btn.grid_pos, CARD_CONTEXT_POSITION)
        info_ctx = card.context_btn.grid_info()
        self.assertEqual(int(info_ctx["row"]), 0)
        self.assertEqual(int(info_ctx["column"]), 3)
        self.assertEqual(int(info_ctx["rowspan"]), 3)
        self.assertEqual(card.context_btn.cget("text"), "[Context]")

        # 6. Check Orange plus / trailing button
        self.assertTrue(hasattr(card, "trailing_btn"))
        self.assertEqual(card.trailing_btn.grid_pos, CARD_TRAILING_BUTTON_POSITION)
        info_trailing = card.trailing_btn.grid_info()
        self.assertEqual(int(info_trailing["row"]), 0)
        self.assertEqual(int(info_trailing["column"]), 4)
        self.assertEqual(int(info_trailing["rowspan"]), 3)
        self.assertEqual(card.trailing_btn.cget("text"), "+")

    def test_make_component_with_word_entries(self):
        """make_component creates word_entry widgets when words is provided."""
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
        )

        # In helper mode with words:
        self.assertTrue(hasattr(card, "label_box"))
        self.assertTrue(hasattr(card, "context_box"))
        self.assertEqual(card.label_box.grid_pos, CARD_LABEL_POSITION)
        self.assertEqual(card.context_box.grid_pos, CARD_CONTEXT_POSITION)

        info_lbl = card.label_box.grid_info()
        self.assertEqual(int(info_lbl["row"]), 0)
        self.assertEqual(int(info_lbl["column"]), 2)
        self.assertEqual(int(info_lbl["rowspan"]), 3)

        info_ctx = card.context_box.grid_info()
        self.assertEqual(int(info_ctx["row"]), 0)
        self.assertEqual(int(info_ctx["column"]), 3)
        self.assertEqual(int(info_ctx["rowspan"]), 3)

        self.assertEqual(card.label_box.get(), "apples")
        self.assertEqual(card.context_box.get(), "in the basket")


if __name__ == "__main__":
    unittest.main()
