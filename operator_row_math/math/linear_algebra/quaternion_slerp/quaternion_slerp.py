"""Row for the operator: Unit vector

Picture:      slerp ( □ , □ , □ ) = □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/linear_algebra/quaternion_slerp
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Quaternion blend'
KEY = 'math/linear_algebra/quaternion_slerp'
PATTERN = 'slerp ( □ , □ , □ ) = □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['q0', 'q1', 't']    # what each box (left to right) is
KINDS = ['list', 'list', 'number']    # what to type in each box (see advanced_input.KINDS)
WORDS = {2: ('start orientation', 'w, x, y, z'), 4: ('end orientation', 'w, x, y, z'), 6: ('blend', '0 is the start, 1 is the end')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'slerp'), ('op', '('), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = [('box', '')]    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
