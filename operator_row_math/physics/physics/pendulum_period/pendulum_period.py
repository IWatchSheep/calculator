"""Row for the operator: Pendulum period

Picture:      □ = 2 π √ ( □ / g )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/pendulum_period
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Pendulum period'
KEY = 'physics/physics/pendulum_period'
PATTERN = '□ = 2 π √ ( □ / g )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['L']    # what each box (left to right) is
KINDS = ['number']    # what to type in each box (see advanced_input.KINDS)
FRAC = [[], [], [], [], [], [], [[1, 'n']], [[1, 'bar']], [[1, 'd']], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '2'), ('op', 'π'), ('op', '√'), ('op', '('), ('box', ''), ('op', '/'), ('op', 'g'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
