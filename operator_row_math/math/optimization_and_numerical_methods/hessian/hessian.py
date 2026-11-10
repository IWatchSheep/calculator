"""Row for the operator: Hessian

Picture:      H = [ ∂ ² □ / ∂ □ ∂ □ ] with □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/optimization_and_numerical_methods/hessian
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Hessian'
KEY = 'math/optimization_and_numerical_methods/hessian'
PATTERN = 'H = [ ∂ ² □ / ∂ □ ∂ □ ] with □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'point']    # what each box (left to right) is
KINDS = ['multi', 'list']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
FRAC = [[], [], [], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'bar']], [[1, 'd']], [[1, 'd']], [[1, 'd']], [[1, 'd']], [], [], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'H'), ('op', '='), ('op', '['), ('op', '∂'), ('op', '2'), ('box', ''), ('op', '/'), ('op', '∂'), ('dec', ''), ('op', '∂'), ('dec', ''), ('op', ']'), ('op', 'with'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
