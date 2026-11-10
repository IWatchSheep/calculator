"""Row for the operator: Heron's formula: area

Picture:      □ = √ ( □ ( □ − □ ) ( □ − □ ) ( □ − □ ) )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py geometry/geometry/heron_area
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = "Heron's formula: area"
KEY = 'geometry/geometry/heron_area'
PATTERN = '□ = √ ( □ ( □ − □ ) ( □ − □ ) ( □ − □ ) )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['s', 'a', 'b', 'c']    # what each box (left to right) is
KINDS = ['number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [0, 0, 1, 0, 2, 0, 3]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
WORDS = {0: ('area', 'square metres of the triangle'), 4: ('semi-perimeter', 'the answer of the row above, metres'), 6: ('semi-perimeter', 'the answer of the row above, metres'), 8: ('side a', 'metres'), 11: ('semi-perimeter', 'the answer of the row above, metres'), 13: ('side b', 'metres'), 16: ('semi-perimeter', 'the answer of the row above, metres'), 18: ('side c', 'metres')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', '√'), ('op', '('), ('box', ''), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', '('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')'), ('op', ')')]      # cards left of "="
RIGHT = []


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
