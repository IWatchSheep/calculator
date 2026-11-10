"""Row for the operator: Weight

Picture:      □ = 4 ( G □ ) ^ ( 5 / 3 ) ( π □ ) ^ ( 2 / 3 ) / ( c ^ 4 □ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/gravitational_wave_strain
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Gravitational-wave strain'
KEY = 'physics/physics/gravitational_wave_strain'
PATTERN = '□ = 4 ( G □ ) ^ ( 5 / 3 ) ( π □ ) ^ ( 2 / 3 ) / ( c ^ 4 □ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['chirp_mass', 'f_gw', 'distance']    # what each box (left to right) is
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
WORDS = {0: ('strain h', 'dimensionless, face-on'), 4: ('gravitational constant', '6.674e-11 N m2/kg2'), 5: ('chirp mass', 'kilograms'), 15: ('wave frequency', 'hertz'), 25: ('speed of light', '299792458 m/s'), 28: ('distance', 'metres to the binary')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n'], [1, 'n']], [[3, 'n'], [1, 'bar']], [[3, 'n'], [1, 'd']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n']], [[3, 'n'], [2, 'n']], [[3, 'n'], [2, 'bar']], [[3, 'n'], [2, 'd']], [[3, 'n']], [[3, 'bar']], [[3, 'hide']], [[3, 'd']], [[3, 'd']], [[3, 'd']], [[3, 'd']], [[3, 'hide']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '4'), ('op', '('), ('op', 'G'), ('box', ''), ('op', ')'), ('op', '^'), ('op', '('), ('op', '5'), ('op', '/'), ('op', '3'), ('op', ')'), ('op', '('), ('op', 'π'), ('box', ''), ('op', ')'), ('op', '^'), ('op', '('), ('op', '2'), ('op', '/'), ('op', '3'), ('op', ')'), ('op', '/'), ('op', '('), ('op', 'c'), ('op', '^'), ('op', '4'), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
