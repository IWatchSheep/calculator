"""Row for the operator: Jacobi iteration

Picture:      □ ᵢ ⁽ᵏ⁺¹⁾ = ( □ ᵢ − Σ { □ = i } □ ᵢⱼ □ ⱼ ⁽ᵏ⁾ ) / □ ᵢᵢ
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/jacobi_iteration
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Jacobi iteration'
KEY = 'math/optimization_and_numerical_methods/jacobi_iteration'
PATTERN = '□ ᵢ ⁽ᵏ⁺¹⁾ = ( □ ᵢ − Σ { □ = i } □ ᵢⱼ □ ⱼ ⁽ᵏ⁾ ) / □ ᵢᵢ'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['A', 'b']    # what each box (left to right) is
KINDS = ['matrix', 'list']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [1, 0, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', 'ᵢ'), ('op', '⁽ᵏ⁺¹⁾'), ('op', '='), ('op', '('), ('box', ''), ('op', 'ᵢ'), ('op', '−'), ('op', 'Σ'), ('op', '{'), ('dec', ''), ('op', '='), ('op', 'i'), ('op', '}'), ('box', ''), ('op', 'ᵢⱼ'), ('dec', ''), ('op', 'ⱼ'), ('op', '⁽ᵏ⁾'), ('op', ')'), ('op', '/'), ('box', ''), ('op', 'ᵢᵢ')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
