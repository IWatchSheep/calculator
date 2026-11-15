"""Logical GUI coordinate convention and layout definitions.

This module establishes a central, framework-independent, 1-based logical coordinate
convention to unify the visual layout of the Python calculator (Tkinter) and the
Rust calculator (egui / eframe), as well as aligning with spreadsheet-based layout
specifications.

Coordinate Convention Rules:
1. The first logical row is 1.
2. The first logical column is 1.
3. (row=1, column=1) is the top-left logical position.
4. Increasing the row number moves downward.
5. Increasing the column number moves rightward.
6. Rows and columns are strictly positive integers (>= 1).
7. Positions refer to logical layout cells, never screen pixel coordinates.
8. A GUI element may occupy more than one row or column using row_span and
   column_span (both must be integers >= 1).
9. Each control belongs to a clearly defined parent container or layout region,
   ensuring identical coordinates in different containers are never confused.
10. Conversion to zero-based indexing required internally by certain GUI libraries
    (e.g., Tkinter grid, 0-based arrays) is handled explicitly and reversibly.

Rust Translation Reference:
In the Rust calculator (`rust_calculator`), this convention maps directly to:

```rust
use serde::{Deserialize, Serialize};

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub struct GridPosition {
    pub row: usize,          // 1-based logical row (>= 1)
    pub column: usize,       // 1-based logical column (>= 1)
    pub row_span: usize,     // >= 1
    pub column_span: usize,  // >= 1
}

impl GridPosition {
    pub fn new(row: usize, column: usize) -> Self {
        assert!(row >= 1, "row must be >= 1");
        assert!(column >= 1, "column must be >= 1");
        Self { row, column, row_span: 1, column_span: 1 }
    }

    pub fn with_span(row: usize, column: usize, row_span: usize, column_span: usize) -> Self {
        assert!(row >= 1 && column >= 1 && row_span >= 1 && column_span >= 1);
        Self { row, column, row_span, column_span }
    }

    pub fn to_zero_based(&self) -> (usize, usize) {
        (self.row - 1, self.column - 1)
    }

    pub fn from_zero_based(zero_row: usize, zero_col: usize) -> Self {
        Self::new(zero_row + 1, zero_col + 1)
    }
}
```
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional, Tuple, Union


class LayoutRegion(str, Enum):
    """Identifies the parent layout container/region for a widget.

    This prevents coordinate confusion when identical local cell positions
    (e.g. row=1, column=1) are used inside different nested containers.
    """
    ROOT = "root"
    TOOLBAR = "toolbar"
    TARGET_BAR = "target_bar"
    ROWS_AREA = "rows_area"
    ROW_CONTAINER = "row_container"
    CARD_COMPONENT = "card_component"
    ARROW_GRID = "arrow_grid"
    RESULTS_AREA = "results_area"
    KEYPAD = "keypad"
    JOIN_BAR = "join_bar"
    TEMPLATES_PANEL = "templates_panel"
    DESCRIPTIVE_CONSOLE = "descriptive_console"
    INSPECTOR = "inspector"
    OPERATORS_POPUP = "operators_popup"
    ADVANCED_POPUP = "advanced_popup"
    TEMPLATE_GUIDE_POPUP = "template_guide_popup"
    WORD_DIAGRAM_POPUP = "word_diagram_popup"
    EXCEL_WORKSPACE = "excel_workspace"


RegionType = Union[LayoutRegion, str, None]


@dataclass(frozen=True)
class GridPosition:
    """A framework-independent logical grid cell coordinate.

    Attributes:
        row: 1-based logical row index (top row is 1, increasing downwards).
        column: 1-based logical column index (leftmost column is 1, increasing rightwards).
        row_span: Number of logical rows occupied (must be >= 1).
        column_span: Number of logical columns occupied (must be >= 1).
        region: Optional parent container or layout region disambiguating coordinates.
    """
    row: int
    column: int
    row_span: int = 1
    column_span: int = 1
    region: RegionType = None

    def __post_init__(self) -> None:
        # Validate row
        if isinstance(self.row, bool) or not isinstance(self.row, int):
            raise TypeError(f"row must be an integer, got {type(self.row).__name__}: {self.row!r}")
        if self.row < 1:
            raise ValueError(f"row must be >= 1 (1-based logical coordinate), got {self.row}")

        # Validate column
        if isinstance(self.column, bool) or not isinstance(self.column, int):
            raise TypeError(f"column must be an integer, got {type(self.column).__name__}: {self.column!r}")
        if self.column < 1:
            raise ValueError(f"column must be >= 1 (1-based logical coordinate), got {self.column}")

        # Validate row_span
        if isinstance(self.row_span, bool) or not isinstance(self.row_span, int):
            raise TypeError(f"row_span must be an integer, got {type(self.row_span).__name__}: {self.row_span!r}")
        if self.row_span < 1:
            raise ValueError(f"row_span must be >= 1 (positive span), got {self.row_span}")

        # Validate column_span
        if isinstance(self.column_span, bool) or not isinstance(self.column_span, int):
            raise TypeError(f"column_span must be an integer, got {type(self.column_span).__name__}: {self.column_span!r}")
        if self.column_span < 1:
            raise ValueError(f"column_span must be >= 1 (positive span), got {self.column_span}")

    @property
    def is_top_left(self) -> bool:
        """Returns True if this position represents the top-left logical cell (1, 1)."""
        return self.row == 1 and self.column == 1

    @property
    def end_row(self) -> int:
        """The last logical row index occupied by this position (inclusive)."""
        return self.row + self.row_span - 1

    @property
    def end_column(self) -> int:
        """The last logical column index occupied by this position (inclusive)."""
        return self.column + self.column_span - 1

    def move(self, rows: int = 0, columns: int = 0) -> GridPosition:
        """Return a new GridPosition shifted by the given number of rows and columns.

        Positive rows shift downward; positive columns shift rightward.
        Negative values shift upward/leftward, but cannot move before row 1 or column 1.
        """
        if isinstance(rows, bool) or not isinstance(rows, int):
            raise TypeError(f"rows delta must be an integer, got {type(rows).__name__}")
        if isinstance(columns, bool) or not isinstance(columns, int):
            raise TypeError(f"columns delta must be an integer, got {type(columns).__name__}")

        new_row = self.row + rows
        new_column = self.column + columns
        return GridPosition(
            row=new_row,
            column=new_column,
            row_span=self.row_span,
            column_span=self.column_span,
            region=self.region,
        )

    def right(self, steps: int = 1) -> GridPosition:
        """Move rightward by `steps` columns (column increases by steps)."""
        return self.move(columns=steps)

    def down(self, steps: int = 1) -> GridPosition:
        """Move downward by `steps` rows (row increases by steps)."""
        return self.move(rows=steps)

    def left(self, steps: int = 1) -> GridPosition:
        """Move leftward by `steps` columns (column decreases by steps)."""
        return self.move(columns=-steps)

    def up(self, steps: int = 1) -> GridPosition:
        """Move upward by `steps` rows (row decreases by steps)."""
        return self.move(rows=-steps)

    def with_span(self, row_span: int = 1, column_span: int = 1) -> GridPosition:
        """Return a new GridPosition with updated spans."""
        return GridPosition(
            row=self.row,
            column=self.column,
            row_span=row_span,
            column_span=column_span,
            region=self.region,
        )

    def with_region(self, region: RegionType) -> GridPosition:
        """Return a copy of this position associated with a layout region."""
        return GridPosition(
            row=self.row,
            column=self.column,
            row_span=self.row_span,
            column_span=self.column_span,
            region=region,
        )

    def overlaps(self, other: GridPosition) -> bool:
        """Check if this grid cell range overlaps with another.

        If regions are specified on both and differ, they do not overlap.
        """
        if self.region is not None and other.region is not None and self.region != other.region:
            return False
        row_disjoint = self.end_row < other.row or other.end_row < self.row
        col_disjoint = self.end_column < other.column or other.end_column < self.column
        return not (row_disjoint or col_disjoint)

    def to_zero_based(self) -> Tuple[int, int]:
        """Convert logical 1-based (row, column) to 0-based indices for GUI libraries."""
        return self.row - 1, self.column - 1

    def to_zero_based_span(self) -> Tuple[int, int, int, int]:
        """Convert to (zero_row, zero_column, row_span, column_span)."""
        return self.row - 1, self.column - 1, self.row_span, self.column_span

    def to_tkinter_grid(self) -> dict[str, int]:
        """Generate keyword arguments for Tkinter's Widget.grid(...) method."""
        return {
            "row": self.row - 1,
            "column": self.column - 1,
            "rowspan": self.row_span,
            "columnspan": self.column_span,
        }

    @classmethod
    def from_zero_based(
        cls,
        zero_row: int,
        zero_column: int,
        row_span: int = 1,
        column_span: int = 1,
        region: RegionType = None,
    ) -> GridPosition:
        """Construct a logical GridPosition from zero-based GUI coordinates."""
        if isinstance(zero_row, bool) or not isinstance(zero_row, int) or zero_row < 0:
            raise ValueError(f"zero_row must be an integer >= 0, got {zero_row!r}")
        if isinstance(zero_column, bool) or not isinstance(zero_column, int) or zero_column < 0:
            raise ValueError(f"zero_column must be an integer >= 0, got {zero_column!r}")
        return cls(
            row=zero_row + 1,
            column=zero_column + 1,
            row_span=row_span,
            column_span=column_span,
            region=region,
        )

    @classmethod
    def from_tkinter_grid(
        cls,
        grid_kwargs: dict[str, Any],
        region: RegionType = None,
    ) -> GridPosition:
        """Construct a logical GridPosition from a Tkinter grid parameter dictionary."""
        zero_row = grid_kwargs.get("row", 0)
        zero_column = grid_kwargs.get("column", 0)
        row_span = grid_kwargs.get("rowspan", 1)
        column_span = grid_kwargs.get("columnspan", 1)
        return cls.from_zero_based(
            zero_row=zero_row,
            zero_column=zero_column,
            row_span=row_span,
            column_span=column_span,
            region=region,
        )

    def to_dict(self) -> dict[str, Any]:
        """Serialize coordinate to a plain dictionary (useful for JSON / cross-process layout)."""
        data: dict[str, Any] = {
            "row": self.row,
            "column": self.column,
            "row_span": self.row_span,
            "column_span": self.column_span,
        }
        if self.region is not None:
            data["region"] = str(self.region.value if isinstance(self.region, Enum) else self.region)
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GridPosition:
        """Deserialize coordinate from a dictionary."""
        return cls(
            row=data["row"],
            column=data["column"],
            row_span=data.get("row_span", 1),
            column_span=data.get("column_span", 1),
            region=data.get("region"),
        )


# ==============================================================================
# Directional Arrow Grid (3x3) Layout Definitions
# ==============================================================================

ARROW_CENTER_POSITION = GridPosition(row=2, column=2, region=LayoutRegion.ARROW_GRID)

ARROW_GRID_POSITIONS: dict[GridPosition, Optional[str]] = {
    GridPosition(row=1, column=1, region=LayoutRegion.ARROW_GRID): "↖",
    GridPosition(row=1, column=2, region=LayoutRegion.ARROW_GRID): "↑",
    GridPosition(row=1, column=3, region=LayoutRegion.ARROW_GRID): "↗",
    GridPosition(row=2, column=1, region=LayoutRegion.ARROW_GRID): "←",
    ARROW_CENTER_POSITION: None,  # Center square box / operator center
    GridPosition(row=2, column=3, region=LayoutRegion.ARROW_GRID): "→",
    GridPosition(row=3, column=1, region=LayoutRegion.ARROW_GRID): "↙",
    GridPosition(row=3, column=2, region=LayoutRegion.ARROW_GRID): "↓",
    GridPosition(row=3, column=3, region=LayoutRegion.ARROW_GRID): "↘",
}


def arrow_at_position(row: int, column: int) -> Optional[str]:
    """Return the arrow symbol at 1-based (row, column) in the arrow grid, or None for center."""
    pos = GridPosition(row=row, column=column, region=LayoutRegion.ARROW_GRID)
    if pos not in ARROW_GRID_POSITIONS:
        raise KeyError(f"Position ({row}, {column}) is outside the 3x3 arrow grid")
    return ARROW_GRID_POSITIONS[pos]


# ==============================================================================
# Surrounding Card Component Layout Definitions
# ==============================================================================

# 9-Column Card Component Layout (Matching Excel Workspace Specification)
CARD_COL_LEAD_BTN: int = 1
CARD_COL_SPACER1: int = 2
CARD_COL_ARROW_LEFT: int = 3
CARD_COL_ARROW_MID: int = 4
CARD_COL_ARROW_RIGHT: int = 5
CARD_COL_LABEL: int = 6
CARD_COL_CONTEXT: int = 7
CARD_COL_SPACER2: int = 8
CARD_COL_TRAILING_BTN: int = 9

CARD_TOTAL_COLUMNS: int = 9
CARD_TOTAL_ROWS: int = 3
CARD_MIDDLE_ROW: int = 2

# Authoritative 9-Column Card Positions in LayoutRegion.CARD_COMPONENT
CARD_9COL_LEAD_BUTTON_POS = GridPosition(
    row=2, column=CARD_COL_LEAD_BTN, row_span=1, column_span=1, region=LayoutRegion.CARD_COMPONENT
)
CARD_9COL_ARROW_GRID_POS = GridPosition(
    row=1, column=CARD_COL_ARROW_LEFT, row_span=3, column_span=3, region=LayoutRegion.CARD_COMPONENT
)
CARD_9COL_CENTER_POS = GridPosition(
    row=2, column=CARD_COL_ARROW_MID, row_span=1, column_span=1, region=LayoutRegion.CARD_COMPONENT
)
CARD_9COL_LABEL_POS = GridPosition(
    row=2, column=CARD_COL_LABEL, row_span=1, column_span=1, region=LayoutRegion.CARD_COMPONENT
)
CARD_9COL_CONTEXT_POS = GridPosition(
    row=2, column=CARD_COL_CONTEXT, row_span=1, column_span=1, region=LayoutRegion.CARD_COMPONENT
)
CARD_9COL_TRAILING_BUTTON_POS = GridPosition(
    row=2, column=CARD_COL_TRAILING_BTN, row_span=1, column_span=1, region=LayoutRegion.CARD_COMPONENT
)

# Canonical 9-column references
CARD_LEAD_BUTTON_POSITION = CARD_9COL_LEAD_BUTTON_POS
CARD_ARROW_GRID_POSITION = CARD_9COL_ARROW_GRID_POS
CARD_LABEL_POSITION = CARD_9COL_LABEL_POS
CARD_CONTEXT_POSITION = CARD_9COL_CONTEXT_POS
CARD_TRAILING_BUTTON_POSITION = CARD_9COL_TRAILING_BUTTON_POS
CARD_CENTER_POSITION = CARD_9COL_CENTER_POS

# 9-column arrow grid positions within the card (rows 1..3, columns 3..5)
CARD_9COL_ARROW_POSITIONS: dict[GridPosition, str] = {
    GridPosition(1, 3, region=LayoutRegion.CARD_COMPONENT): "↖",
    GridPosition(1, 4, region=LayoutRegion.CARD_COMPONENT): "↑",
    GridPosition(1, 5, region=LayoutRegion.CARD_COMPONENT): "↗",
    GridPosition(2, 3, region=LayoutRegion.CARD_COMPONENT): "←",
    GridPosition(2, 4, region=LayoutRegion.CARD_COMPONENT): "",  # Center square
    GridPosition(2, 5, region=LayoutRegion.CARD_COMPONENT): "→",
    GridPosition(3, 3, region=LayoutRegion.CARD_COMPONENT): "↙",
    GridPosition(3, 4, region=LayoutRegion.CARD_COMPONENT): "↓",
    GridPosition(3, 5, region=LayoutRegion.CARD_COMPONENT): "↘",
}


class _CardComponentPositions(dict):
    """Bidirectional mapping for card component positions.

    Supports lookup by canonical string names, friendly aliases, and by GridPosition:
        CARD_COMPONENT_POSITIONS["lead_button"] -> GridPosition(...)
        CARD_COMPONENT_POSITIONS[GridPosition(...)] -> "lead_button"
    """

    def __init__(self, canonical_items: dict[str, GridPosition], aliases: dict[str, str]) -> None:
        super().__init__(canonical_items)
        self._aliases = aliases
        self._by_pos = {pos: name for name, pos in canonical_items.items()}

    def __getitem__(self, key: Any) -> Any:
        if isinstance(key, GridPosition):
            return self._by_pos[key]
        if isinstance(key, str) and key in self._aliases:
            key = self._aliases[key]
        return super().__getitem__(key)

    def __contains__(self, key: Any) -> bool:
        if isinstance(key, GridPosition):
            return key in self._by_pos
        if isinstance(key, str) and key in self._aliases:
            return True
        return super().__contains__(key)

    def get(self, key: Any, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default


CARD_COMPONENT_POSITIONS = _CardComponentPositions(
    canonical_items={
        "lead_button": CARD_LEAD_BUTTON_POSITION,
        "arrow_grid": CARD_ARROW_GRID_POSITION,
        "center_square": CARD_CENTER_POSITION,
        "label_entry": CARD_LABEL_POSITION,
        "context_entry": CARD_CONTEXT_POSITION,
        "trailing_button": CARD_TRAILING_BUTTON_POSITION,
    },
    aliases={
        "blue_plus": "lead_button",
        "item_entry": "label_entry",
        "orange_plus": "trailing_button",
        "center": "center_square",
        "center_btn": "center_square",
    },
)


def card_component_position(name: str) -> GridPosition:
    """Return the GridPosition for a named card component."""
    if name not in CARD_COMPONENT_POSITIONS:
        raise KeyError(
            f"Unknown card component {name!r}, valid components: {list(CARD_COMPONENT_POSITIONS.keys())}"
        )
    return CARD_COMPONENT_POSITIONS[name]


# ==============================================================================
# Main Row Layout Definitions (Rows Area)
# ==============================================================================

ROW_COL_LABEL = 1
ROW_COL_HELPER = 2
ROW_COL_MATH = 3
ROW_COL_ACTIONS = 4
ROW_COL_RESULT = 5

MAIN_ROW_COLUMNS: dict[str, int] = {
    "row_label": ROW_COL_LABEL,
    "helper_slot": ROW_COL_HELPER,
    "math_expression": ROW_COL_MATH,
    "math_actions": ROW_COL_ACTIONS,
    "result_card": ROW_COL_RESULT,
}

MAIN_ROW_ALIASES: dict[str, str] = {
    "row": "row_label",
    "label": "row_label",
    "row_label": "row_label",
    "helper": "helper_slot",
    "helper_slot": "helper_slot",
    "join_note": "helper_slot",
    "math": "math_expression",
    "math_expression": "math_expression",
    "actions": "math_actions",
    "math_actions": "math_actions",
    "result": "result_card",
    "result_card": "result_card",
}


def main_row_position(
    row: int,
    column: int | str,
    row_span: int = 1,
    column_span: int = 1,
) -> GridPosition:
    """Return a 1-based GridPosition in LayoutRegion.ROWS_AREA.

    `row` must be an integer >= 1.
    `column` can be an integer (1..5) or a column name:
        1 or "row_label" / "label"
        2 or "helper_slot" / "helper" / "join_note"
        3 or "math_expression" / "math"
        4 or "math_actions" / "actions"
        5 or "result_card" / "result"
    """
    if isinstance(row, bool) or not isinstance(row, int) or row < 1:
        raise ValueError(f"row must be an integer >= 1, got {row!r}")

    if isinstance(column, str):
        canonical = MAIN_ROW_ALIASES.get(column, column)
        if canonical not in MAIN_ROW_COLUMNS:
            raise KeyError(
                f"Unknown main row column {column!r}, valid columns: {list(MAIN_ROW_COLUMNS.keys())}"
            )
        col_idx = MAIN_ROW_COLUMNS[canonical]
    else:
        if isinstance(column, bool) or not isinstance(column, int) or not (1 <= column <= 5):
            raise ValueError(f"column must be an integer 1..5, got {column!r}")
        col_idx = column

    return GridPosition(
        row=row,
        column=col_idx,
        row_span=row_span,
        column_span=column_span,
        region=LayoutRegion.ROWS_AREA,
    )


def main_row_positions(row: int) -> dict[str, GridPosition]:
    """Return a dictionary of all five logical GridPositions for a given 1-based row index."""
    if isinstance(row, bool) or not isinstance(row, int) or row < 1:
        raise ValueError(f"row must be an integer >= 1, got {row!r}")
    return {
        name: GridPosition(
            row=row,
            column=col_idx,
            row_span=1,
            column_span=1,
            region=LayoutRegion.ROWS_AREA,
        )
        for name, col_idx in MAIN_ROW_COLUMNS.items()
    }


# Named positions for the first two initial calculator rows
ROW_1_LABEL_POS = main_row_position(1, ROW_COL_LABEL)
ROW_1_JOIN_NOTE_POS = main_row_position(1, ROW_COL_HELPER)
ROW_1_MATH_POS = main_row_position(1, ROW_COL_MATH)
ROW_1_ACTIONS_POS = main_row_position(1, ROW_COL_ACTIONS)
ROW_1_RESULT_POS = main_row_position(1, ROW_COL_RESULT)

ROW_1_ROW_LABEL_POS = ROW_1_LABEL_POS
ROW_1_HELPER_SLOT_POS = ROW_1_JOIN_NOTE_POS
ROW_1_MATH_EXPRESSION_POS = ROW_1_MATH_POS
ROW_1_MATH_ACTIONS_POS = ROW_1_ACTIONS_POS
ROW_1_RESULT_CARD_POS = ROW_1_RESULT_POS

ROW_2_LABEL_POS = main_row_position(2, ROW_COL_LABEL)
ROW_2_HELPER_POS = main_row_position(2, ROW_COL_HELPER)
ROW_2_MATH_POS = main_row_position(2, ROW_COL_MATH)
ROW_2_ACTIONS_POS = main_row_position(2, ROW_COL_ACTIONS)
ROW_2_RESULT_POS = main_row_position(2, ROW_COL_RESULT)

ROW_2_ROW_LABEL_POS = ROW_2_LABEL_POS
ROW_2_HELPER_SLOT_POS = ROW_2_HELPER_POS
ROW_2_MATH_EXPRESSION_POS = ROW_2_MATH_POS
ROW_2_MATH_ACTIONS_POS = ROW_2_ACTIONS_POS
ROW_2_RESULT_CARD_POS = ROW_2_RESULT_POS


# ==============================================================================
# Authoritative Excel Workspace Coordinate Specification (33 Columns x N Rows)
# ==============================================================================

EXCEL_TOTAL_COLUMNS: int = 33
EXCEL_INITIAL_TOTAL_ROWS: int = 9
EXCEL_ROWS_PER_CALCULATOR_ROW: int = 3
EXCEL_CALCULATOR_ROW_STRIDE: int = 6

# Global Column Assignments (1..33)
EXCEL_COL_ROW_LABEL: int = 1
EXCEL_COL_MARGIN: int = 2

# Card Slot 1 (Helper Card / Join Note): Columns 3..11 (9 Columns)
EXCEL_COL_SLOT1_START: int = 3
EXCEL_COL_SLOT1_END: int = 11
EXCEL_COL_SLOT1_LEAD_BTN: int = 3
EXCEL_COL_SLOT1_SPACER1: int = 4
EXCEL_COL_SLOT1_ARROW_COL1: int = 5
EXCEL_COL_SLOT1_ARROW_COL2: int = 6
EXCEL_COL_SLOT1_ARROW_COL3: int = 7
EXCEL_COL_SLOT1_LABEL: int = 8
EXCEL_COL_SLOT1_CONTEXT: int = 9
EXCEL_COL_SLOT1_SPACER2: int = 10
EXCEL_COL_SLOT1_TRAILING_BTN: int = 11

# Spacer between Slot 1 and Slot 2
EXCEL_COL_SPACER_SLOT1_SLOT2: int = 12

# Card Slot 2 (Mathematical Expression): Columns 13..21 (9 Columns)
EXCEL_COL_SLOT2_START: int = 13
EXCEL_COL_SLOT2_END: int = 21
EXCEL_COL_SLOT2_LEAD_BTN: int = 13
EXCEL_COL_SLOT2_SPACER1: int = 14
EXCEL_COL_SLOT2_ARROW_COL1: int = 15
EXCEL_COL_SLOT2_ARROW_COL2: int = 16
EXCEL_COL_SLOT2_ARROW_COL3: int = 17
EXCEL_COL_SLOT2_LABEL: int = 18
EXCEL_COL_SLOT2_CONTEXT: int = 19
EXCEL_COL_SLOT2_SPACER2: int = 20
EXCEL_COL_SLOT2_TRAILING_BTN: int = 21

# Spacer between Slot 2 and Actions
EXCEL_COL_SPACER_SLOT2_ACTIONS: int = 22

# Actions Slot (Left-side mathematical actions): Column 23 (1 Column)
EXCEL_COL_ACTIONS: int = 23

# Spacer between Actions and Slot 3
EXCEL_COL_SPACER_ACTIONS_SLOT3: int = 24

# Card Slot 3 (Result Card): Columns 25..33 (9 Columns)
EXCEL_COL_SLOT3_START: int = 25
EXCEL_COL_SLOT3_END: int = 33
EXCEL_COL_SLOT3_LEAD_BTN: int = 25
EXCEL_COL_SLOT3_SPACER1: int = 26
EXCEL_COL_SLOT3_ARROW_COL1: int = 27
EXCEL_COL_SLOT3_ARROW_COL2: int = 28
EXCEL_COL_SLOT3_ARROW_COL3: int = 29
EXCEL_COL_SLOT3_LABEL: int = 30
EXCEL_COL_SLOT3_CONTEXT: int = 31
EXCEL_COL_SLOT3_SPACER2: int = 32
EXCEL_COL_SLOT3_TRAILING_BTN: int = 33

# Mapping of relative 9-column card offsets
EXCEL_CARD_RELATIVE_COLUMNS: dict[str, int] = {
    "lead_btn": 1,
    "spacer_1": 2,
    "arrow_col1": 3,
    "arrow_col2": 4,
    "center": 4,
    "arrow_col3": 5,
    "label": 6,
    "context": 7,
    "spacer_2": 8,
    "trailing_btn": 9,
}

EXCEL_CARD_SLOT_BASE_COLUMNS: dict[int, int] = {
    1: EXCEL_COL_SLOT1_START,
    2: EXCEL_COL_SLOT2_START,
    3: EXCEL_COL_SLOT3_START,
}


def excel_start_row(calc_row: int) -> int:
    """Return the 1-based starting Excel row for calculator row k.

    Formula: start_row = 6 * (calc_row - 1) + 1
    k=1 -> 1  (rows 1..3)
    k=2 -> 7  (rows 7..9)
    k=3 -> 13 (rows 13..15)
    k=4 -> 19 (rows 19..21)
    """
    if isinstance(calc_row, bool) or not isinstance(calc_row, int) or calc_row < 1:
        raise ValueError(f"calc_row must be an integer >= 1, got {calc_row!r}")
    return 6 * (calc_row - 1) + 1


def excel_heading_row(calc_row: int) -> int:
    """Return the 1-based Excel heading row preceding calculator row k (k >= 2).

    Formula: heading_row = excel_start_row(k) - 2 = 6 * k - 7
    k=2 -> 5  ('helper card (slot 1)')
    k=3 -> 11 ('helper card (slot 2)')
    k=4 -> 17 ('helper card (slot 3)')
    """
    if isinstance(calc_row, bool) or not isinstance(calc_row, int) or calc_row < 2:
        raise ValueError(f"calc_row must be an integer >= 2 for heading rows, got {calc_row!r}")
    return excel_start_row(calc_row) - 2


def excel_spacer_before_heading_row(calc_row: int) -> int:
    """Return the 1-based empty spacer row preceding the helper heading (k >= 2)."""
    return excel_heading_row(calc_row) - 1


def excel_spacer_after_heading_row(calc_row: int) -> int:
    """Return the 1-based empty spacer row following the helper heading (k >= 2)."""
    return excel_heading_row(calc_row) + 1


# Canonical control mapping definitions within a 3-row calculator band
EXCEL_ARROW_OFFSETS: dict[str, tuple[int, int]] = {
    "arrow_nw": (0, 0),
    "arrow_n": (0, 1),
    "arrow_ne": (0, 2),
    "arrow_w": (1, 0),
    "center": (1, 1),
    "arrow_e": (1, 2),
    "arrow_sw": (2, 0),
    "arrow_s": (2, 1),
    "arrow_se": (2, 2),
}


def excel_workspace_position(
    calc_row: int,
    control_name: str,
    row_span: int = 1,
    column_span: int = 1,
) -> GridPosition:
    """Return the authoritative 1-based GridPosition in LayoutRegion.EXCEL_WORKSPACE.

    Parameters:
        calc_row: 1-based calculator row index (1, 2, 3, ...).
        control_name: Name of the control to locate.
        row_span: Number of logical rows occupied (default 1).
        column_span: Number of logical columns occupied (default 1).
    """
    if isinstance(calc_row, bool) or not isinstance(calc_row, int) or calc_row < 1:
        raise ValueError(f"calc_row must be an integer >= 1, got {calc_row!r}")

    r0 = excel_start_row(calc_row)
    name = control_name.strip().lower()

    # 1. Row Indicator Label
    if name in ("row_label", "label_frame", "row_indicator"):
        return GridPosition(row=r0, column=EXCEL_COL_ROW_LABEL, row_span=3, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    # 2. Slot 1 (Join Note for row 1; Helper Card for row >= 2)
    if name in ("join_note_label", "slot1_join_note"):
        if calc_row != 1:
            raise ValueError(f"join_note_label only exists on calculator row 1, not row {calc_row}")
        return GridPosition(row=r0, column=EXCEL_COL_SLOT1_START, row_span=1, column_span=8,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("join_note_arrow", "join_note_down_arrow", "slot1_down_arrow"):
        if calc_row != 1:
            raise ValueError(f"join_note_arrow only exists on calculator row 1, not row {calc_row}")
        return GridPosition(row=r0 + 2, column=EXCEL_COL_SLOT1_ARROW_COL2, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("helper_heading", "slot1_heading"):
        if calc_row < 2:
            raise ValueError(f"helper_heading only exists on calculator row >= 2, not row {calc_row}")
        return GridPosition(row=excel_heading_row(calc_row), column=EXCEL_COL_SLOT1_START,
                            row_span=1, column_span=6, region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot1_container", "helper_container"):
        return GridPosition(row=r0, column=EXCEL_COL_SLOT1_START, row_span=3, column_span=9,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot1_lead_btn", "helper_lead_btn"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT1_LEAD_BTN, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot1_label", "helper_label"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT1_LABEL, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot1_context", "helper_context"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT1_CONTEXT, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot1_trailing_btn", "helper_trailing_btn"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT1_TRAILING_BTN, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    for arrow_key, (dr, dc) in EXCEL_ARROW_OFFSETS.items():
        if name in (f"slot1_{arrow_key}", f"helper_{arrow_key}"):
            return GridPosition(row=r0 + dr, column=EXCEL_COL_SLOT1_ARROW_COL1 + dc, row_span=1, column_span=1,
                                region=LayoutRegion.EXCEL_WORKSPACE)

    # 3. Slot 2 (Mathematical Expression Area / Card)
    if name in ("slot2_container", "math_viewport", "math_container", "math_slot"):
        return GridPosition(row=r0, column=EXCEL_COL_SLOT2_START, row_span=3, column_span=9,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot2_lead_btn", "math_lead_btn"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT2_LEAD_BTN, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot2_label", "math_label"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT2_LABEL, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot2_context", "math_context"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT2_CONTEXT, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot2_trailing_btn", "math_trailing_btn"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT2_TRAILING_BTN, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    for arrow_key, (dr, dc) in EXCEL_ARROW_OFFSETS.items():
        if name in (f"slot2_{arrow_key}", f"math_{arrow_key}"):
            return GridPosition(row=r0 + dr, column=EXCEL_COL_SLOT2_ARROW_COL1 + dc, row_span=1, column_span=1,
                                region=LayoutRegion.EXCEL_WORKSPACE)

    # 4. Actions Slot (Column 23)
    if name in ("action_math_left", "action_top", "math_to_put_on_the_left"):
        return GridPosition(row=r0, column=EXCEL_COL_ACTIONS, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("action_clear_left", "action_bottom", "clear_math_on_the_left"):
        return GridPosition(row=r0 + 2, column=EXCEL_COL_ACTIONS, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    # 5. Slot 3 (Result Card)
    if name in ("slot3_container", "result_container", "result_card"):
        return GridPosition(row=r0, column=EXCEL_COL_SLOT3_START, row_span=3, column_span=9,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot3_lead_btn", "result_lead_btn"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT3_LEAD_BTN, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot3_label", "result_label"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT3_LABEL, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot3_context", "result_context"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT3_CONTEXT, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    if name in ("slot3_trailing_btn", "result_trailing_btn"):
        return GridPosition(row=r0 + 1, column=EXCEL_COL_SLOT3_TRAILING_BTN, row_span=1, column_span=1,
                            region=LayoutRegion.EXCEL_WORKSPACE)

    for arrow_key, (dr, dc) in EXCEL_ARROW_OFFSETS.items():
        if name in (f"slot3_{arrow_key}", f"result_{arrow_key}"):
            return GridPosition(row=r0 + dr, column=EXCEL_COL_SLOT3_ARROW_COL1 + dc, row_span=1, column_span=1,
                                region=LayoutRegion.EXCEL_WORKSPACE)

    raise KeyError(f"Unknown Excel workspace control {control_name!r} for calculator row {calc_row}")


def excel_workspace_positions(calc_row: int) -> dict[str, GridPosition]:
    """Return all canonical GridPositions for visible controls in calculator row k."""
    r0 = excel_start_row(calc_row)
    pos: dict[str, GridPosition] = {
        "row_label": excel_workspace_position(calc_row, "row_label"),
    }

    # Slot 1
    if calc_row == 1:
        pos["join_note_label"] = excel_workspace_position(calc_row, "join_note_label")
        pos["join_note_arrow"] = excel_workspace_position(calc_row, "join_note_arrow")
    else:
        pos["helper_heading"] = excel_workspace_position(calc_row, "helper_heading")
        pos["helper_lead_btn"] = excel_workspace_position(calc_row, "helper_lead_btn")
        for k in EXCEL_ARROW_OFFSETS:
            pos[f"helper_{k}"] = excel_workspace_position(calc_row, f"helper_{k}")
        pos["helper_label"] = excel_workspace_position(calc_row, "helper_label")
        pos["helper_context"] = excel_workspace_position(calc_row, "helper_context")
        pos["helper_trailing_btn"] = excel_workspace_position(calc_row, "helper_trailing_btn")

    # Slot 2 (Math Expression)
    pos["math_lead_btn"] = excel_workspace_position(calc_row, "math_lead_btn")
    for k in EXCEL_ARROW_OFFSETS:
        pos[f"math_{k}"] = excel_workspace_position(calc_row, f"math_{k}")
    pos["math_label"] = excel_workspace_position(calc_row, "math_label")
    pos["math_context"] = excel_workspace_position(calc_row, "math_context")
    pos["math_trailing_btn"] = excel_workspace_position(calc_row, "math_trailing_btn")

    # Actions
    pos["action_math_left"] = excel_workspace_position(calc_row, "action_math_left")
    pos["action_clear_left"] = excel_workspace_position(calc_row, "action_clear_left")

    # Slot 3 (Result Card)
    pos["result_lead_btn"] = excel_workspace_position(calc_row, "result_lead_btn")
    for k in EXCEL_ARROW_OFFSETS:
        pos[f"result_{k}"] = excel_workspace_position(calc_row, f"result_{k}")
    pos["result_label"] = excel_workspace_position(calc_row, "result_label")
    pos["result_context"] = excel_workspace_position(calc_row, "result_context")
    pos["result_trailing_btn"] = excel_workspace_position(calc_row, "result_trailing_btn")

    return pos

def card_to_excel_position(
    local_pos: GridPosition,
    card_slot: int = 1,
    calc_row: int = 1,
) -> GridPosition:
    """Translate a local 9-column card GridPosition to global Excel workspace coordinates.

    card_slot:
        1: Helper card (Excel columns 3..11)
        2: Math expression slot (Excel columns 13..21)
        3: Result card (Excel columns 25..33)
    calc_row:
        1-based calculator row index k >= 1.
    """
    if card_slot not in EXCEL_CARD_SLOT_BASE_COLUMNS:
        raise ValueError(f"card_slot must be 1, 2, or 3, got {card_slot!r}")
    if isinstance(calc_row, bool) or not isinstance(calc_row, int) or calc_row < 1:
        raise ValueError(f"calc_row must be an integer >= 1, got {calc_row!r}")

    base_col = EXCEL_CARD_SLOT_BASE_COLUMNS[card_slot]
    base_row = excel_start_row(calc_row)

    global_col = base_col + local_pos.column - 1
    global_row = base_row + local_pos.row - 1

    return GridPosition(
        row=global_row,
        column=global_col,
        row_span=local_pos.row_span,
        column_span=local_pos.column_span,
        region=LayoutRegion.EXCEL_WORKSPACE,
    )


def excel_to_card_position(excel_pos: GridPosition) -> tuple[int, GridPosition]:
    """Translate a global Excel workspace coordinate to (card_slot, local_card_position)."""
    col = excel_pos.column
    if EXCEL_COL_SLOT1_START <= col <= EXCEL_COL_SLOT1_END:
        slot = 1
        base_col = EXCEL_COL_SLOT1_START
    elif EXCEL_COL_SLOT2_START <= col <= EXCEL_COL_SLOT2_END:
        slot = 2
        base_col = EXCEL_COL_SLOT2_START
    elif EXCEL_COL_SLOT3_START <= col <= EXCEL_COL_SLOT3_END:
        slot = 3
        base_col = EXCEL_COL_SLOT3_START
    else:
        raise ValueError(f"Excel column {col} does not fall within card slots 1, 2, or 3")

    local_col = col - base_col + 1
    local_row = (excel_pos.row - 1) % EXCEL_CALCULATOR_ROW_STRIDE + 1
    if local_row > 3:
        raise ValueError(f"Excel row {excel_pos.row} is outside the 3-row card band")

    return slot, GridPosition(
        row=local_row,
        column=local_col,
        row_span=excel_pos.row_span,
        column_span=excel_pos.column_span,
        region=LayoutRegion.CARD_COMPONENT,
    )
