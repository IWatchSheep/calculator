"""Row for the operator: Weight

Picture:      □ = h / ( m × c )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/electron_compton_wavelength
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Electron Compton wavelength'
KEY = 'physics/physics/electron_compton_wavelength'
PATTERN = '□ = h / ( m × c )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = []
KINDS = []
WORDS = {0: ('wavelength', 'metres'), 2: ('Planck constant', '6.626e-34 J s'), 5: ('electron mass', '9.1093837015e-31 kilograms'), 7: ('speed of light', '299792458 m/s')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[1, 'n']], [[1, 'bar']], [[1, 'hide']], [[1, 'd']], [[1, 'd']], [[1, 'd']], [[1, 'hide']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', 'h'), ('op', '/'), ('op', '('), ('op', 'm'), ('op', '×'), ('op', 'c'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
