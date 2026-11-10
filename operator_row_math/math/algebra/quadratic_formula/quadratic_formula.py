"""Row for the operator: Quadratic formula

Picture:      ( □ , □ ) = ( − □ ± √ ( □ ² − 4 × □ × □ ) ) / ( 2 × □ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/algebra/quadratic_formula
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Quadratic formula'
KEY = 'math/algebra/quadratic_formula'
PATTERN = '( □ , □ ) = ( − □ ± √ ( □ ² − 4 × □ × □ ) ) / ( 2 × □ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['a', 'b', 'c']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [1, 1, 0, 2, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
FRAC = [[], [], [], [], [], [], [[1, 'hide']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'hide']], [[1, 'bar']], [[1, 'hide']], [[1, 'd']], [[1, 'd']], [[1, 'd']], [[1, 'hide']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '('), ('out', ''), ('op', ','), ('out', ''), ('op', ')'), ('op', '='), ('op', '('), ('op', '−'), ('box', ''), ('op', '±'), ('op', '√'), ('op', '('), ('box', ''), ('op', '2'), ('op', '−'), ('op', '4'), ('op', '×'), ('box', ''), ('op', '×'), ('box', ''), ('op', ')'), ('op', ')'), ('op', '/'), ('op', '('), ('op', '2'), ('op', '×'), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
