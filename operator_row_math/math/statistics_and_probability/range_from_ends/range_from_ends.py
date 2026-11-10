"""Row for the operator: Range: from the ends

Picture:      □ = □ − □
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py math/statistics_and_probability/range_from_ends
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Range: from the ends'
KEY = 'math/statistics_and_probability/range_from_ends'
PATTERN = '□ = □ − □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['maximum', 'minimum']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
WORDS = {0: ('range', 'largest minus smallest'), 2: ('maximum', 'the answer of Row 1'), 4: ('minimum', 'the answer of Row 2')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('box', ''), ('op', '−'), ('box', '')]      # cards left of "="
RIGHT = []


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
