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
