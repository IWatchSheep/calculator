"""Row for the operator: Lagrange interpolation

Picture:      L ( □ ) = Σ ᵢ □ ᵢ ∏ { □ = i } ( □ − □ ⱼ ) / ( □ ᵢ − □ ⱼ )
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/lagrange_interpolation
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Lagrange interpolation'
KEY = 'math/optimization_and_numerical_methods/lagrange_interpolation'
PATTERN = 'L ( □ ) = Σ ᵢ □ ᵢ ∏ { □ = i } ( □ − □ ⱼ ) / ( □ ᵢ − □ ⱼ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['xs', 'ys', 'x']    # what each box (left to right) is
KINDS = ['list', 'list', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [2, 1, 2, 0, 0, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'L'), ('op', '('), ('box', ''), ('op', ')'), ('op', '='), ('op', 'Σ'), ('op', 'i'), ('box', ''), ('op', 'i'), ('op', '∏'), ('op', '{'), ('dec', ''), ('op', '='), ('op', 'i'), ('op', '}'), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', 'j'), ('op', ')'), ('op', '/'), ('op', '('), ('box', ''), ('op', 'i'), ('op', '−'), ('box', ''), ('op', 'j'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))
