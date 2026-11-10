"""Row for the operator: Identity matrix

Picture:      I ᵢⱼ = 1 when i = j , 0 otherwise with □
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/linear_algebra/identity_matrix
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Identity matrix'
KEY = 'math/linear_algebra/identity_matrix'
PATTERN = 'I ᵢⱼ = 1 when i = j , 0 otherwise with □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['n']    # what each box (left to right) is
KINDS = ['number']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'I'), ('op', 'ij'), ('op', '='), ('op', '1'), ('op', 'when'), ('op', 'i'), ('op', '='), ('op', 'j'), ('op', ','), ('op', '0'), ('op', 'otherwise'), ('op', 'with'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))
