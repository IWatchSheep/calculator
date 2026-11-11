"""Row for the operator: Weight

Picture:      □ = a0 / ( 2 × □ ) × ( 3 × □ ² − □ × ( □ + 1 ) )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/hydrogen_mean_radius
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Hydrogen mean radius'
KEY = 'physics/physics/hydrogen_mean_radius'
PATTERN = '□ = a0 / ( 2 × □ ) × ( 3 × □ ² − □ × ( □ + 1 ) )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['n', 'l', 'Z']
KINDS = ['number', 'number', 'number']
SLOTS = [2, 0, 1, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('mean radius', 'metres'), 2: ('Bohr radius of hydrogen', '5.29177210903e-11 m'), 7: ('atomic number', '1 for hydrogen, 2 for He+'), 13: ('level', '1, 2, 3, …'), 16: ('angular momentum', '0, 1, …, up to n − 1')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [[1, 'n']], [[1, 'bar']], [[1, 'hide']], [[1, 'd']], [[1, 'd']], [[1, 'd']], [[1, 'hide']], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', 'a0'), ('op', '/'), ('op', '('), ('op', '2'), ('op', '×'), ('box', ''), ('op', ')'), ('op', '×'), ('op', '('), ('op', '3'), ('op', '×'), ('box', ''), ('op', '2'), ('op', '−'), ('box', ''), ('op', '×'), ('op', '('), ('box', ''), ('op', '+'), ('op', '1'), ('op', ')'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
