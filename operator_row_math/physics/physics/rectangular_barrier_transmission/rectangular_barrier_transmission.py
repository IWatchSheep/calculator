"""Row for the operator: Weight

Picture:      □ = 1 / ( 1 + □ ² × sinh ² ( □ × √ ( 2 × □ × ( □ − □ ) ) / ħ ) / ( 4 × □ × ( □ − □ ) ) )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/rectangular_barrier_transmission
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Rectangular-barrier transmission'
KEY = 'physics/physics/rectangular_barrier_transmission'
PATTERN = '□ = 1 / ( 1 + □ ² × sinh ² ( □ × √ ( 2 × □ × ( □ − □ ) ) / ħ ) / ( 4 × □ × ( □ − □ ) ) )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['E', 'V', 'L', 'm']
KINDS = ['number', 'number', 'number', 'number']
SLOTS = [1, 2, 3, 1, 0, 0, 1, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('transmission', 'probability, 0 to 1'), 7: ('barrier height', 'joules'), 13: ('barrier thickness', 'metres'), 19: ('mass', 'kilograms'), 24: ('energy', 'joules, below the barrier'), 28: ('reduced Planck constant', '1.054571817e-34 J s')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[1, 'n']], [[1, 'bar']], [[1, 'hide']], [[1, 'd']], [[1, 'd']], [[1, 'd'], [3, 'n']], [[1, 'd'], [3, 'n']], [[1, 'd'], [3, 'n']], [[1, 'd'], [3, 'n']], [[1, 'd'], [3, 'n']], [[1, 'd'], [3, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'n']], [[1, 'd'], [3, 'n'], [2, 'bar']], [[1, 'd'], [3, 'n'], [2, 'd']], [[1, 'd'], [3, 'n']], [[1, 'd'], [3, 'bar']], [[1, 'd'], [3, 'hide']], [[1, 'd'], [3, 'd']], [[1, 'd'], [3, 'd']], [[1, 'd'], [3, 'd']], [[1, 'd'], [3, 'd']], [[1, 'd'], [3, 'd']], [[1, 'd'], [3, 'd']], [[1, 'd'], [3, 'd']], [[1, 'd'], [3, 'd']], [[1, 'd'], [3, 'd']], [[1, 'd'], [3, 'hide']], [[1, 'hide']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '1'), ('op', '/'), ('op', '('), ('op', '1'), ('op', '+'), ('box', ''), ('op', '2'), ('op', '×'), ('op', 'sinh'), ('op', '2'), ('op', '('), ('box', ''), ('op', '×'), ('op', '√'), ('op', '('), ('op', '2'), ('op', '×'), ('box', ''), ('op', '×'), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', ')'), ('op', '/'), ('op', 'ħ'), ('op', ')'), ('op', '/'), ('op', '('), ('op', '4'), ('op', '×'), ('box', ''), ('op', '×'), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', ')'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
