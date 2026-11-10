"""Row for the operator: Fourier series

Picture:      f ( □ ) = Σ □ ₙ cos ( n □ ) + □ ₙ sin ( n □ ) with □ , □
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/transforms_and_differential_equations/fourier_series
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Fourier series'
KEY = 'math/transforms_and_differential_equations/fourier_series'
PATTERN = 'f ( □ ) = Σ □ ₙ cos ( n □ ) + □ ₙ sin ( n □ ) with □ , □'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['f', 'n']    # what each box (left to right) is
KINDS = ['function', 'number']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('the function', 'the periodic function being expanded'), 2: ('the variable', 'x, the position along one period'), 6: ('cosine coefficient', 'a sub n'), 7: ('the index', 'n, which harmonic'), 11: ('the variable', 'x'), 14: ('sine coefficient', 'b sub n'), 15: ('the index', 'n'), 19: ('the variable', 'x')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', 'f'), ('op', '('), ('dec', ''), ('op', ')'), ('op', '='), ('op', 'Σ'), ('dec', ''), ('op', 'n'), ('op', 'cos'), ('op', '('), ('op', 'n'), ('dec', ''), ('op', ')'), ('op', '+'), ('dec', ''), ('op', 'n'), ('op', 'sin'), ('op', '('), ('op', 'n'), ('dec', ''), ('op', ')'), ('op', 'with'), ('box', ''), ('op', ','), ('box', '')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
