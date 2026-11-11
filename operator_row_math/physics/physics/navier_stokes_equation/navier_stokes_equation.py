"""Row for the operator: Navier–Stokes equation

Picture:      ρ ( ∂ u / ∂ t + ( u · ∇ ) u ) = − ∇ p + μ ∇ ² u + f
Calculation:  reference only (formula, no calculation yet)
Try it:       python operator_row_math/preview.py physics/physics/navier_stokes_equation
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Navier–Stokes equation'
KEY = 'physics/physics/navier_stokes_equation'
PATTERN = 'ρ ( ∂ u / ∂ t + ( u · ∇ ) u ) = − ∇ p + μ ∇ ² u + f'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'reference'
INPUTS = []    # what each box (left to right) is
KINDS = []    # what to type in each box (see advanced_input.KINDS)
NOTE = 'Formula only. Needs the velocity field. The five rows already show the equation.'    # formula only: what the row says (no box is added and compute() is unchanged)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('density', 'mass of fluid in each unit of volume (kg/m³)'), 2: ('change in time', 'how fast the velocity u changes at one point (∂u/∂t)'), 6: ('time', 'seconds'), 9: ('velocity', 'speed and direction of the fluid, u = (u, v, w)'), 11: ('gradient', 'how a quantity changes from place to place'), 15: ('balance', "left side: density × the fluid's acceleration; right side: the forces on it"), 17: ('gradient', 'the direction in which the pressure rises fastest'), 18: ('pressure', 'force on each unit of area (Pa)'), 20: ('viscosity', 'how sticky the fluid is, its internal friction (Pa·s)'), 21: ('Laplacian', '∇² adds up the second derivatives: how different u is from its neighbours'), 25: ('outside force', 'pushes on each volume of fluid from outside, such as gravity (N/m³)')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
STACK_EXPONENTS = True    # an exponent card shares the column of the symbol it powers (one grid row up) instead of having a column of its own
FRAC = [[], [], [[1, 'n']], [[1, 'n']], [[1, 'bar']], [[1, 'd']], [[1, 'd']], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'ρ'), ('op', '('), ('op', '∂'), ('op', 'u'), ('op', '/'), ('op', '∂'), ('op', 't'), ('op', '+'), ('op', '('), ('op', 'u'), ('op', '·'), ('op', '∇'), ('op', ')'), ('op', 'u'), ('op', ')'), ('op', '='), ('op', '−'), ('op', '∇'), ('op', 'p'), ('op', '+'), ('op', 'μ'), ('op', '∇'), ('op', '2'), ('op', 'u'), ('op', '+'), ('op', 'f')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"), stack_exponents=True)
