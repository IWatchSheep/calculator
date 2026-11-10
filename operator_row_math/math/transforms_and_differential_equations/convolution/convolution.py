"""Row for the operator: Convolution

Picture:      ( □ * □ ) [ □ ] = Σ ⱼ □ [ □ ] · □ [ □ − □ ]
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/transforms_and_differential_equations/convolution
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Convolution'
KEY = 'math/transforms_and_differential_equations/convolution'
PATTERN = '( □ * □ ) [ □ ] = Σ ⱼ □ [ □ ] · □ [ □ − □ ]'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'g']    # what each box (left to right) is
KINDS = ['list', 'list']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 1, 0, 1]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {1: ('first signal', 'f'), 3: ('second signal', 'g'), 6: ('output index', 'k, which place in the result'), 10: ('sum index', 'j'), 11: ('first signal', 'f'), 13: ('sum index', 'j'), 16: ('second signal', 'g'), 18: ('output index', 'k'), 20: ('sum index', 'j')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', '('), ('box', ''), ('op', '*'), ('box', ''), ('op', ')'), ('op', '['), ('dec', ''), ('op', ']'), ('op', '='), ('op', 'Σ'), ('op', 'j'), ('box', ''), ('op', '['), ('dec', ''), ('op', ']'), ('op', '·'), ('box', ''), ('op', '['), ('dec', ''), ('op', '−'), ('dec', ''), ('op', ']')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
