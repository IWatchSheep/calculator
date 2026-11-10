"""Row for the operator: Weight

Picture:      □ = √ ( □ □ / ( π ħ ) ) × exp ( − □ □ □ ² / ħ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/oscillator_ground_density
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Oscillator ground-state density'
KEY = 'physics/physics/oscillator_ground_density'
PATTERN = '□ = √ ( □ □ / ( π ħ ) ) × exp ( − □ □ □ ² / ħ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['m', 'omega', 'x']
KINDS = ['number', 'number', 'number']
SLOTS = [0, 1, 0, 1, 2]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('probability density', 'per metre'), 4: ('mass', 'kilograms'), 5: ('angular frequency', 'radians per second'), 9: ('reduced Planck constant', '1.054571817e-34 J s'), 18: ('position', 'metres from the centre')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [], [], [[1, 'n']], [[1, 'n']], [[1, 'bar']], [[1, 'hide']], [[1, 'd']], [[1, 'd']], [[1, 'hide']], [], [], [], [], [], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'n']], [[2, 'bar']], [[2, 'd']], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '√'), ('op', '('), ('box', ''), ('box', ''), ('op', '/'), ('op', '('), ('op', 'π'), ('op', 'ħ'), ('op', ')'), ('op', ')'), ('op', '×'), ('op', 'exp'), ('op', '('), ('op', '−'), ('box', ''), ('box', ''), ('box', ''), ('op', '2'), ('op', '/'), ('op', 'ħ'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
