"""Row for the algebra word problem: Distance (toward each other) 0154

Picture:      □ ( t + □ ) + □ t = □   (the equation of the problem; each box is a number of the problem text; the answer is right of =)
Calculation:  reference - the problem is stored; no solver answers it yet
Try it:       python operator_row_math_for_algebra_word_problems/preview.py distance_toward_each_other/0154
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Distance (toward each other) 0154'
KEY = 'distance_toward_each_other/0154'
LIBRARY_KEY = 'distance_toward_each_other/0154'    # the problem in operators_one_algebra_word_problem_per_file (its compute(...) feeds the result box)
PATTERN = '□ ( t + □ ) + □ t = □  ->  answer □'
# "ready"     = the boxes on the left feed compute() and the answer shows right of "="
# "reference" = the problem and its steps are stored, but no solver answers it yet
CALC = 'reference'
INPUTS = ['number 2', 'number 3', 'number 4', 'number 1']    # what each box (left to right, as in the equation) is: which number of the problem text it holds
BOX_INDEX = [1, 2, 3, 0]    # the place of each box's number in the problem text (NUMBERS of the problem file); the other text numbers stay as written
DEFAULTS = ['59', '2', '66', '618']    # the boxes' numbers as written in the stored problem
KINDS = ['number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('box', ''), ('op', '('), ('op', 't'), ('op', '+'), ('box', ''), ('op', ')'), ('op', '+'), ('box', ''), ('op', 't'), ('op', '='), ('box', '')]      # cards left of "="
RIGHT = [('box', '')]    # cards right of "="  (the result box = Row 1's number card: the answer)


def place(parent, stacked=False):
    """Create this problem's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
