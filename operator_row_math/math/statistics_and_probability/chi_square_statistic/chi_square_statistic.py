"""Row for the operator: Chi-square statistic

Picture:      □ ² = Σ ( □ ᵢ − □ ᵢ ) ² / □ ᵢ
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/statistics_and_probability/chi_square_statistic
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Chi-square statistic'
KEY = 'math/statistics_and_probability/chi_square_statistic'
PATTERN = '□ ² = Σ ( □ ᵢ − □ ᵢ ) ² / □ ᵢ'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['observed', 'expected']    # what each box (left to right) is
KINDS = ['list', 'list']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, -1, 0, 0, 0, 0, 1, 0, 0, 1, 0, -1, 0, 0, 1]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('chi-square', 'how far the counts are from what was expected'), 5: ('observed counts', 'what you counted'), 8: ('expected counts', 'what the model predicted'), 13: ('expected counts', 'what the model predicted')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'bar']], [[1, 'd']], [[1, 'd']]]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '2'), ('op', '='), ('op', 'Σ'), ('op', '('), ('box', ''), ('op', 'i'), ('op', '−'), ('box', ''), ('op', 'i'), ('op', ')'), ('op', '2'), ('op', '/'), ('box', ''), ('op', 'i')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
