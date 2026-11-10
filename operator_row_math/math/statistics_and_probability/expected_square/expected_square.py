"""Row for the operator: Variance

Picture:      □ = Σ □ ² · □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/statistics_and_probability/expected_square
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Expected square'
KEY = 'math/statistics_and_probability/expected_square'
PATTERN = '□ = Σ □ ² · □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['values', 'probs']    # what each box (left to right) is
KINDS = ['list', 'list']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 0, 0, 0, -1, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('expectation of the square', 'E of X squared'), 3: ('the values', 'the same numbers as the row above'), 4: ('two', 'square each value'), 6: ('the probabilities', 'the same chances as the row above')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', 'Σ'), ('box', ''), ('op', '2'), ('op', '·'), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
