"""Row for the operator: Euler-Mascheroni constant

Picture:      γ = lim (1 + 1/2 + … + 1 / □ − ln □)
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/constants_and_relations/euler_mascheroni_constant
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Euler-Mascheroni constant'
KEY = 'math/constants_and_relations/euler_mascheroni_constant'
PATTERN = 'γ = lim (1 + 1/2 + … + 1 / □ − ln □)'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = []    # what each box (left to right) is
KINDS = []    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'γ')]      # cards left of "="
RIGHT = [('op', 'lim (1 + 1/2 + … + 1 /'), ('box', ''), ('op', '− ln'), ('box', ''), ('op', ')')]    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
