"""Row for the operator: Null space

Picture:      null ( □ ) = { □ : □ · □ = 0 }
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/linear_algebra/null_space
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Null space'
KEY = 'math/linear_algebra/null_space'
PATTERN = 'null ( □ ) = { □ : □ · □ = 0 }'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['A']    # what each box (left to right) is
KINDS = ['matrix']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'null'), ('op', '('), ('box', ''), ('op', ')'), ('op', '='), ('op', '{'), ('dec', ''), ('op', ':'), ('box', ''), ('op', '·'), ('dec', ''), ('op', '='), ('op', '0'), ('op', '}')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
