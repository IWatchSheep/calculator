"""Row for the operator: Rydberg formula

Picture:      1 / □ = R × □ ² × ( 1 / □ ² − 1 / □ ² )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/rydberg_formula
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Rydberg formula'
KEY = 'physics/physics/rydberg_formula'
PATTERN = '1 / □ = R × □ ² × ( 1 / □ ² − 1 / □ ² )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['n1', 'n2']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '1'), ('op', '/'), ('out', ''), ('op', '='), ('op', 'R'), ('op', '×'), ('dec', ''), ('op', '²'), ('op', '×'), ('op', '('), ('op', '1'), ('op', '/'), ('box', ''), ('op', '²'), ('op', '−'), ('op', '1'), ('op', '/'), ('box', ''), ('op', '²'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
