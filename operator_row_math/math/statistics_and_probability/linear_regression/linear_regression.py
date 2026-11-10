"""Row for the operator: Linear regression

Picture:      □ = □ □ + □ with □ , □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/statistics_and_probability/linear_regression
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Linear regression'
KEY = 'math/statistics_and_probability/linear_regression'
PATTERN = '□ = □ □ + □ with □ , □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['x', 'y']    # what each box (left to right) is
KINDS = ['list', 'list']    # what to type in each box (see advanced_input.KINDS)
WORDS = {0: ('predicted value', 'y on the fitted line'), 2: ('slope', 'how much y changes for one step in x'), 3: ('input', 'x, the variable along the line'), 5: ('intercept', 'y when x is 0'), 7: ('the x values', 'one list of inputs'), 9: ('the y values', 'one list of outputs, paired with the x values')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('dec', ''), ('op', '='), ('dec', ''), ('dec', ''), ('op', '+'), ('dec', ''), ('op', 'with'), ('box', ''), ('op', ','), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
