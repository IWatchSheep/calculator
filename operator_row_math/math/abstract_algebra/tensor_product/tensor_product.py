"""Row for the operator: Tensor product

Picture:      ( □ ⊗ □ ) = ( □ ₁ □ ₁ , □ ₁ □ ₂ , … , □ ₘ □ ₙ )
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/abstract_algebra/tensor_product
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Tensor product'
KEY = 'math/abstract_algebra/tensor_product'
PATTERN = '( □ ⊗ □ ) = ( □ ₁ □ ₁ , □ ₁ □ ₂ , … , □ ₘ □ ₙ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['a', 'b']    # what each box (left to right) is
KINDS = ['list', 'list']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '('), ('box', ''), ('op', '⊗'), ('box', ''), ('op', ')'), ('op', '='), ('op', '('), ('dec', ''), ('op', '1'), ('dec', ''), ('op', '1'), ('op', ','), ('dec', ''), ('op', '1'), ('dec', ''), ('op', '2'), ('op', ','), ('op', '…'), ('op', ','), ('dec', ''), ('op', 'm'), ('dec', ''), ('op', 'n'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))
