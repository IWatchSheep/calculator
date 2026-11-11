"""Python port of forming_chess (Rust Forming Strategies Chess).

See README.md and rules/rules.txt.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from board import (
    START_FEN,
    Board,
    Move,
    parse_sq,
    perft,
    piece_name,
    sq_name,
)
from evaluate import list1, list2
from lists34 import list3, list4

__all__ = [
    "START_FEN",
    "Board",
    "Move",
    "parse_sq",
    "perft",
    "piece_name",
    "sq_name",
    "list1",
    "list2",
    "list3",
    "list4",
]
