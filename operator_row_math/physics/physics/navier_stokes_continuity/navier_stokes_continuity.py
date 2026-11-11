"""Row for the operator: Navier–Stokes: continuity (incompressible)

Picture:      ∂ u / ∂ x + ∂ v / ∂ y + ∂ w / ∂ z = 0
Calculation:  reference only (formula, no calculation yet)
Try it:       python operator_row_math/preview.py physics/physics/navier_stokes_continuity
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Navier–Stokes: continuity (incompressible)'
KEY = 'physics/physics/navier_stokes_continuity'
PATTERN = '∂ u / ∂ x + ∂ v / ∂ y + ∂ w / ∂ z = 0'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'reference'
INPUTS = []    # what each box (left to right) is
KINDS = []    # what to type in each box (see advanced_input.KINDS)
NOTE = 'Formula only. Needs the velocity field. One of the five Navier–Stokes rows.'    # formula only: what the row says (no box is added and compute() is unchanged)
WORDS = {0: ('change of u', 'how much u changes along x'), 6: ('change of v', 'how much v changes along y'), 12: ('change of w', 'how much w changes along z'), 17: ('equals zero', 'the flow neither squeezes nor creates fluid')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
STACK_EXPONENTS = True    # an exponent card shares the column of the symbol it powers (one grid row up) instead of having a column of its own
FRAC = [[[1, 'n']], [[1, 'n']], [[1, 'bar']], [[1, 'd']], [[1, 'd']], [], [[2, 'n']], [[2, 'n']], [[2, 'bar']], [[2, 'd']], [[2, 'd']], [], [[3, 'n']], [[3, 'n']], [[3, 'bar']], [[3, 'd']], [[3, 'd']], [], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '∂'), ('op', 'u'), ('op', '/'), ('op', '∂'), ('op', 'x'), ('op', '+'), ('op', '∂'), ('op', 'v'), ('op', '/'), ('op', '∂'), ('op', 'y'), ('op', '+'), ('op', '∂'), ('op', 'w'), ('op', '/'), ('op', '∂'), ('op', 'z'), ('op', '='), ('op', '0')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"), stack_exponents=True)
