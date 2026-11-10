"""Row for the operator: Rydberg formula

Picture:      1 / □ = R × Z ² × ( 1 / □ ² − 1 / □ ² )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/rydberg_formula
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Rydberg formula'
KEY = 'physics/physics/rydberg_formula'
PATTERN = '1 / □ = R × Z ² × ( 1 / □ ² − 1 / □ ² )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['n1', 'n2']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {2: ('wavelength', 'metres of the emitted light'), 4: ('Rydberg constant', '1.097e7 per metre'), 6: ('atomic number', '1 for hydrogen'), 12: ('lower level', '1, 2, 3, ...'), 17: ('upper level', 'greater than n1')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[[1, 'n']], [[1, 'bar']], [[1, 'd']], [], [], [], [], [], [], [], [[2, 'n']], [[2, 'bar']], [[2, 'd']], [[2, 'd']], [], [[3, 'n']], [[3, 'bar']], [[3, 'd']], [[3, 'd']], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '1'), ('op', '/'), ('out', ''), ('op', '='), ('op', 'R'), ('op', '×'), ('op', 'Z'), ('op', '2'), ('op', '×'), ('op', '('), ('op', '1'), ('op', '/'), ('box', ''), ('op', '2'), ('op', '−'), ('op', '1'), ('op', '/'), ('box', ''), ('op', '2'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
