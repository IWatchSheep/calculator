"""Row for the operator: Arithmetic series sum

Picture:      □ = ( □ / 2 ) × ( 2 × □ + ( □ − 1 ) × □ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/algebra/arithmetic_series_sum
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Arithmetic series sum'
KEY = 'math/algebra/arithmetic_series_sum'
PATTERN = '□ = ( □ / 2 ) × ( 2 × □ + ( □ − 1 ) × □ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['a1', 'd', 'n']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [2, 0, 2, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
FRAC = [[], [], [], [[1, 'n']], [[1, 'bar']], [[1, 'd']], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '('), ('box', ''), ('op', '/'), ('op', '2'), ('op', ')'), ('op', '×'), ('op', '('), ('op', '2'), ('op', '×'), ('box', ''), ('op', '+'), ('op', '('), ('box', ''), ('op', '−'), ('op', '1'), ('op', ')'), ('op', '×'), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))
