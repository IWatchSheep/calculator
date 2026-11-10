"""Row for the algebra word problem: Rational equation 0818

Picture:      □ /( □ − c) = □ /(23 + c)   (the equation of the problem; each box is a number of the problem text; the answer is right of =)
Calculation:  reference - the problem is stored; no solver answers it yet
Try it:       python operator_row_math_for_algebra_word_problems/preview.py rational_equation/0818
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Rational equation 0818'
KEY = 'rational_equation/0818'
LIBRARY_KEY = 'rational_equation/0818'    # the problem in operators_one_algebra_word_problem_per_file (its compute(...) feeds the result box)
PATTERN = '□ /( □ − c) = □ /(23 + c)  ->  answer □'
# "ready"     = the boxes on the left feed compute() and the answer shows right of "="
# "reference" = the problem and its steps are stored, but no solver answers it yet
CALC = 'reference'
INPUTS = ['number 1', 'number 3', 'number 2']    # what each box (left to right, as in the equation) is: which number of the problem text it holds
BOX_INDEX = [0, 2, 1]    # the place of each box's number in the problem text (NUMBERS of the problem file); the other text numbers stay as written
DEFAULTS = ['52', '23', '132']    # the boxes' numbers as written in the stored problem
KINDS = ['number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('box', ''), ('op', '/('), ('box', ''), ('op', '− c) ='), ('box', ''), ('op', '/(23 + c)')]      # cards left of "="
RIGHT = [('box', '')]    # cards right of "="  (the result box = Row 1's number card: the answer)


def place(parent, stacked=False):
    """Create this problem's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
