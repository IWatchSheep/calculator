"""Row for the operator: Navier–Stokes: y momentum

Picture:      ρ ( ∂ v / ∂ t + u ∂ v / ∂ x + v ∂ v / ∂ y + w ∂ v / ∂ z ) = − ∂ p / ∂ y + μ ( ∂ ² v / ∂ x ² + ∂ ² v / ∂ y ² + ∂ ² v / ∂ z ² ) + f y
Calculation:  reference only (formula, no calculation yet)
Try it:       python operator_row_math/preview.py physics/physics/navier_stokes_y_momentum
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Navier–Stokes: y momentum'
KEY = 'physics/physics/navier_stokes_y_momentum'
PATTERN = 'ρ ( ∂ v / ∂ t + u ∂ v / ∂ x + v ∂ v / ∂ y + w ∂ v / ∂ z ) = − ∂ p / ∂ y + μ ( ∂ ² v / ∂ x ² + ∂ ² v / ∂ y ² + ∂ ² v / ∂ z ² ) + f y'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'reference'
INPUTS = []    # what each box (left to right) is
KINDS = []    # what to type in each box (see advanced_input.KINDS)
NOTE = 'Formula only. Needs the velocity field. One of the five rows.'    # formula only: what the row says (no box is added and compute() is unchanged)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 1]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('density', 'mass of fluid in each unit of volume (kg/m³)'), 2: ('change in time', 'how fast the velocity v changes at one point (∂v/∂t)'), 6: ('time', 'seconds'), 8: ('velocity along x', 'carries the fluid along x, so v changes along x too'), 15: ('velocity along y', 'carries the fluid along y, so v changes along y too'), 22: ('velocity along z', 'carries the fluid along z, so v changes along z too'), 29: ('balance', "left side: density × the fluid's acceleration; right side: the forces on it"), 31: ('pressure change', 'the push on the fluid along y comes from pressure that changes along y'), 32: ('pressure', 'force on each unit of area (Pa)'), 37: ('viscosity', 'how sticky the fluid is, its internal friction (Pa·s)'), 39: ('second derivative', 'how v curves along x: friction smooths it out'), 47: ('second derivative', 'how v curves along y: friction smooths it out'), 55: ('second derivative', 'how v curves along z: friction smooths it out'), 64: ('outside force', 'pushes on each volume of fluid from outside, such as gravity (N/m³)'), 65: ('direction', 'the outside force along y')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
STACK_EXPONENTS = True    # an exponent card shares the column of the symbol it powers (one grid row up) instead of having a column of its own
FRAC = [[], [], [[1, 'n']], [[1, 'n']], [[1, 'bar']], [[1, 'd']], [[1, 'd']], [], [], [[2, 'n']], [[2, 'n']], [[2, 'bar']], [[2, 'd']], [[2, 'd']], [], [], [[3, 'n']], [[3, 'n']], [[3, 'bar']], [[3, 'd']], [[3, 'd']], [], [], [[4, 'n']], [[4, 'n']], [[4, 'bar']], [[4, 'd']], [[4, 'd']], [], [], [], [[5, 'n']], [[5, 'n']], [[5, 'bar']], [[5, 'd']], [[5, 'd']], [], [], [], [[6, 'n']], [[6, 'n']], [[6, 'n']], [[6, 'bar']], [[6, 'd']], [[6, 'd']], [[6, 'd']], [], [[7, 'n']], [[7, 'n']], [[7, 'n']], [[7, 'bar']], [[7, 'd']], [[7, 'd']], [[7, 'd']], [], [[8, 'n']], [[8, 'n']], [[8, 'n']], [[8, 'bar']], [[8, 'd']], [[8, 'd']], [[8, 'd']], [], [], [], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'ρ'), ('op', '('), ('op', '∂'), ('op', 'v'), ('op', '/'), ('op', '∂'), ('op', 't'), ('op', '+'), ('op', 'u'), ('op', '∂'), ('op', 'v'), ('op', '/'), ('op', '∂'), ('op', 'x'), ('op', '+'), ('op', 'v'), ('op', '∂'), ('op', 'v'), ('op', '/'), ('op', '∂'), ('op', 'y'), ('op', '+'), ('op', 'w'), ('op', '∂'), ('op', 'v'), ('op', '/'), ('op', '∂'), ('op', 'z'), ('op', ')'), ('op', '='), ('op', '−'), ('op', '∂'), ('op', 'p'), ('op', '/'), ('op', '∂'), ('op', 'y'), ('op', '+'), ('op', 'μ'), ('op', '('), ('op', '∂'), ('op', '2'), ('op', 'v'), ('op', '/'), ('op', '∂'), ('op', 'x'), ('op', '2'), ('op', '+'), ('op', '∂'), ('op', '2'), ('op', 'v'), ('op', '/'), ('op', '∂'), ('op', 'y'), ('op', '2'), ('op', '+'), ('op', '∂'), ('op', '2'), ('op', 'v'), ('op', '/'), ('op', '∂'), ('op', 'z'), ('op', '2'), ('op', ')'), ('op', '+'), ('op', 'f'), ('op', 'y')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"), stack_exponents=True)
