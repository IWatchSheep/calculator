"""Row for the algebra word problem: System of equations (3 variables) 0950

Picture:      a + b + c = □ ; 2 a + b = □ ; b + 2 c = □   (the equation of the problem; each box is a number of the problem text; the answer is right of =)
Calculation:  reference - the problem is stored; no solver answers it yet
Try it:       python operator_row_math_for_algebra_word_problems/preview.py system_of_equations_3_variables/0950
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'System of equations (3 variables) 0950'
KEY = 'system_of_equations_3_variables/0950'
LIBRARY_KEY = 'system_of_equations_3_variables/0950'    # the problem in operators_one_algebra_word_problem_per_file (its compute(...) feeds the result box)
PATTERN = 'a + b + c = □ ; 2 a + b = □ ; b + 2 c = □  ->  answer □'
# "ready"     = the boxes on the left feed compute() and the answer shows right of "="
# "reference" = the problem and its steps are stored, but no solver answers it yet
CALC = 'reference'
INPUTS = ['number 1', 'number 2', 'number 3']    # what each box (left to right, as in the equation) is: which number of the problem text it holds
BOX_INDEX = [0, 1, 2]    # the place of each box's number in the problem text (NUMBERS of the problem file); the other text numbers stay as written
DEFAULTS = ['4.05', '3.40', '4.70']    # the boxes' numbers as written in the stored problem
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEVELS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript (one row down), 0 = on the line
LEFT = [('op', 'a'), ('op', '+'), ('op', 'b'), ('op', '+'), ('op', 'c'), ('op', '='), ('box', ''), ('op', ';'), ('op', '2'), ('op', 'a'), ('op', '+'), ('op', 'b'), ('op', '='), ('box', ''), ('op', ';'), ('op', 'b'), ('op', '+'), ('op', '2'), ('op', 'c'), ('op', '='), ('box', '')]      # cards left of "="
RIGHT = [('box', '')]    # cards right of "="  (the result box = Row 1's number card: the answer)


def place(parent, stacked=False):
    """Create this problem's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=LEVELS)
