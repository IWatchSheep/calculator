"""Row for the operator: Weight

Picture:      □ = ( □ □ ) ^ ( 3 / 5 ) / ( □ + □ ) ^ ( 1 / 5 )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/chirp_mass
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Chirp mass'
KEY = 'physics/physics/chirp_mass'
PATTERN = '□ = ( □ □ ) ^ ( 3 / 5 ) / ( □ + □ ) ^ ( 1 / 5 )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['m1', 'm2']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 0, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
WORDS = {0: ('chirp mass', 'kilograms'), 3: ('first mass', 'kilograms'), 4: ('second mass', 'kilograms')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'n'], [1, 'n']], [[2, 'n'], [1, 'bar']], [[2, 'n'], [1, 'd']], [[2, 'n']], [[2, 'bar']], [[2, 'hide']], [[2, 'd']], [[2, 'd']], [[2, 'd']], [[2, 'hide']], [], [], [[3, 'n']], [[3, 'bar']], [[3, 'd']], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '('), ('box', ''), ('box', ''), ('op', ')'), ('op', '^'), ('op', '('), ('op', '3'), ('op', '/'), ('op', '5'), ('op', ')'), ('op', '/'), ('op', '('), ('box', ''), ('op', '+'), ('box', ''), ('op', ')'), ('op', '^'), ('op', '('), ('op', '1'), ('op', '/'), ('op', '5'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
