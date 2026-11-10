"""Row for the operator: Discrete Fourier transform

Picture:      □ ₖ = Σ ₙ □ ₙ · e ^ ( − 2 π i · □ □ / □ )
Calculation:  type the boxes with the number pad or Advanced Input (lists, matrices, functions...)
Try it:       python operator_row_math/preview.py math/transforms_and_differential_equations/discrete_fourier_transform
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Discrete Fourier transform'
KEY = 'math/transforms_and_differential_equations/discrete_fourier_transform'
PATTERN = '□ ₖ = Σ ₙ □ ₙ · e ^ ( − 2 π i · □ □ / □ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'advanced'
INPUTS = ['x']    # what each box (left to right) is
KINDS = ['list']    # what to type in each box (see advanced_input.KINDS)
LEVELS = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line
WORDS = {0: ('transform', 'X at frequency k'), 1: ('frequency index', 'which frequency this value is'), 4: ('sample index', 'which sample is being added'), 5: ('samples', 'the list of values'), 6: ('sample index', 'which sample'), 8: ('base of the exponential', 'about 2.718'), 12: ('two', 'the 2 in 2 pi'), 13: ('pi', 'the circle constant'), 14: ('imaginary unit', 'the square root of minus 1'), 16: ('frequency index', 'k'), 17: ('sample index', 'n'), 19: ('length', 'N, how many samples')}    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used
FRAC = [[], [], [], [], [], [], [], [], [], [], [], [], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'n']], [[1, 'bar']], [[1, 'd']], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', 'k'), ('op', '='), ('op', 'Σ'), ('op', 'n'), ('box', ''), ('op', 'n'), ('op', '·'), ('op', 'e'), ('op', '^'), ('op', '('), ('op', '−'), ('op', '2'), ('op', 'π'), ('op', 'i'), ('op', '·'), ('dec', ''), ('dec', ''), ('op', '/'), ('dec', ''), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"), fracs=globals().get("FRAC"))
