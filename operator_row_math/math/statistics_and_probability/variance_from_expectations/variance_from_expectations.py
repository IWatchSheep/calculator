"""Row for the operator: Variance: from the expectations

Picture:      □ = □ − ( □ ) ²
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/statistics_and_probability/variance_from_expectations
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Variance: from the expectations'
KEY = 'math/statistics_and_probability/variance_from_expectations'
PATTERN = '□ = □ − ( □ ) ²'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['ex2', 'ex']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 0, 0, 0, 0, 0, 0, -1]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('variance', 'how spread out the values are'), 2: ('expectation of the square', 'the answer of Row 2'), 5: ('expectation', 'the answer of Row 1'), 7: ('two', 'square that average')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '−'), ('op', '('), ('box', ''), ('op', ')'), ('op', '2')]      # cards left of "="
RIGHT = []


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
