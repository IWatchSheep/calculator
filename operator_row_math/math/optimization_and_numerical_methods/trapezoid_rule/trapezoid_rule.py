"""Row for the operator: Trapezoid rule

Picture:      ∫ ₐ ᵇ □ ≈ □ · ( f ( □ ) / 2 + Σ f ( □ ᵢ ) + f ( □ ) / 2 )
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/trapezoid_rule
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Trapezoid rule'
KEY = 'math/optimization_and_numerical_methods/trapezoid_rule'
PATTERN = '∫ ₐ ᵇ □ ≈ □ · ( f ( □ ) / 2 + Σ f ( □ ᵢ ) + f ( □ ) / 2 )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'a', 'b']    # what each box (left to right) is
KINDS = ['function', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
FRAC = [[], [], [], [], [], [], [], [], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'bar']], [[1, 'd']], [], [], [], [], [], [], [], [], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'bar']], [[2, 'd']], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '∫'), ('op', 'a'), ('op', 'b'), ('box', ''), ('op', '≈'), ('dec', ''), ('op', '·'), ('op', '('), ('op', 'f'), ('op', '('), ('box', ''), ('op', ')'), ('op', '/'), ('op', '2'), ('op', '+'), ('op', 'Σ'), ('op', 'f'), ('op', '('), ('dec', ''), ('op', 'i'), ('op', ')'), ('op', '+'), ('op', 'f'), ('op', '('), ('box', ''), ('op', ')'), ('op', '/'), ('op', '2'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
