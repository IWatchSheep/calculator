"""Row for the operator: Slope

Picture:      □ = ( □ ₂ − □ ₁ ) / ( □ ₂ − □ ₁ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py geometry/geometry/slope
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Slope'
KEY = 'geometry/geometry/slope'
PATTERN = '□ = ( □ ₂ − □ ₁ ) / ( □ ₂ − □ ₁ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['x1', 'y1', 'x2', 'y2']    # what each box (left to right) is
KINDS = ['number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [3, 1, 2, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '('), ('box', ''), ('op', '₂'), ('op', '−'), ('box', ''), ('op', '₁'), ('op', ')'), ('op', '/'), ('op', '('), ('box', ''), ('op', '₂'), ('op', '−'), ('box', ''), ('op', '₁'), ('op', ')')]      # cards left of "="
RIGHT = []


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
