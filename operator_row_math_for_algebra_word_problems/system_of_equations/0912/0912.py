"""Row for the algebra word problem: System of equations 0912

Picture:      □ x + □ y = □ ; □ x + □ y = □   (the equation of the problem; each box is a number of the problem text; the answer is right of =)
Calculation:  reference - the problem is stored; no solver answers it yet
Try it:       python operator_row_math_for_algebra_word_problems/preview.py system_of_equations/0912
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'System of equations 0912'
KEY = 'system_of_equations/0912'
LIBRARY_KEY = 'system_of_equations/0912'    # the problem in operators_one_algebra_word_problem_per_file (its compute(...) feeds the result box)
PATTERN = '□ x + □ y = □ ; □ x + □ y = □  ->  answer □'
# "ready"     = the boxes on the left feed compute() and the answer shows right of "="
# "reference" = the problem and its steps are stored, but no solver answers it yet
CALC = 'reference'
INPUTS = ['number 1', 'number 2', 'number 3', 'number 4', 'number 5', 'number 6']    # what each box (left to right, as in the equation) is: which number of the problem text it holds
BOX_INDEX = [0, 1, 2, 3, 4, 5]    # the place of each box's number in the problem text (NUMBERS of the problem file); the other text numbers stay as written
DEFAULTS = ['3', '5', '22', '3', '4', '20']    # the boxes' numbers as written in the stored problem
KINDS = ['number', 'number', 'number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
FRAC = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript (one row down), 0 = on the line
LEFT = [('box', ''), ('op', 'x'), ('op', '+'), ('box', ''), ('op', 'y'), ('op', '='), ('box', ''), ('op', ';'), ('box', ''), ('op', 'x'), ('op', '+'), ('box', ''), ('op', 'y'), ('op', '='), ('box', '')]      # cards left of "="
RIGHT = [('box', '')]    # cards right of "="  (the result box = Row 1's number card: the answer)


def place(parent, stacked=False):
    """Create this problem's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=LEVELS, fracs=FRAC)
