"""Row for the operator: Cross product

Picture:      □ × □ = ( □ ₂ □ ₃ − □ ₃ □ ₂ , □ ₃ □ ₁ − □ ₁ □ ₃ , □ ₁ □ ₂ − □ ₂ □ ₁ )
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/linear_algebra/cross_product
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Cross product'
KEY = 'math/linear_algebra/cross_product'
PATTERN = '□ × □ = ( □ ₂ □ ₃ − □ ₃ □ ₂ , □ ₃ □ ₁ − □ ₁ □ ₃ , □ ₁ □ ₂ − □ ₂ □ ₁ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['a', 'b']    # what each box (left to right) is
KINDS = ['list', 'list']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('box', ''), ('op', '×'), ('box', ''), ('op', '='), ('op', '('), ('dec', ''), ('op', '₂'), ('dec', ''), ('op', '₃'), ('op', '−'), ('dec', ''), ('op', '₃'), ('dec', ''), ('op', '₂'), ('op', ','), ('dec', ''), ('op', '₃'), ('dec', ''), ('op', '₁'), ('op', '−'), ('dec', ''), ('op', '₁'), ('dec', ''), ('op', '₃'), ('op', ','), ('dec', ''), ('op', '₁'), ('dec', ''), ('op', '₂'), ('op', '−'), ('dec', ''), ('op', '₂'), ('dec', ''), ('op', '₁'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
