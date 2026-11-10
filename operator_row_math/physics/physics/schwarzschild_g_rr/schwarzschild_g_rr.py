"""Row for the operator: Weight

Picture:      □ = 1 / ( 1 − □ / □ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/schwarzschild_g_rr
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Schwarzschild g_rr'
KEY = 'physics/physics/schwarzschild_g_rr'
PATTERN = '□ = 1 / ( 1 − □ / □ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['r', 'Rs']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [1, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
WORDS = {0: ('g_rr', 'the radial coefficient'), 7: ('Schwarzschild radius', 'metres, 2GM/c2'), 9: ('radius', 'metres from the centre')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[1, 'n']], [[1, 'bar']], [[1, 'hide']], [[1, 'd']], [[1, 'd']], [[1, 'd'], [2, 'n']], [[1, 'd'], [2, 'bar']], [[1, 'd'], [2, 'd']], [[1, 'hide']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '1'), ('op', '/'), ('op', '('), ('op', '1'), ('op', '−'), ('box', ''), ('op', '/'), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
