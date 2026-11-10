"""Row for the operator: Conditional probability

Picture:      P ( □ | □ ) = P ( □ ∩ □ ) / P ( □ ) with □
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/statistics_and_probability/conditional_probability
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Conditional probability'
KEY = 'math/statistics_and_probability/conditional_probability'
PATTERN = 'P ( □ | □ ) = P ( □ ∩ □ ) / P ( □ ) with □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['p_a_and_b', 'p_b']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [1, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'P'), ('op', '('), ('dec', ''), ('op', '|'), ('dec', ''), ('op', ')'), ('op', '='), ('op', 'P'), ('op', '('), ('dec', ''), ('op', '∩'), ('dec', ''), ('op', ')'), ('op', '/'), ('op', 'P'), ('op', '('), ('box', ''), ('op', ')'), ('op', 'with'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
