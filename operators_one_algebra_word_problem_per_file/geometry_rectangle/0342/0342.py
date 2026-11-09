"""Algebra word problem 0342   [Geometry (rectangle)]

Problem : The length of a rectangle is 2 more than its width. The perimeter is 132 cm. Find the dimensions.
Let     : w = width
Equation: 2w + 2(w + 2) = 132
Solve   : 4w + 4 = 132 → w = 32
Answer  : Width 32 cm, length 34 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0342'
KEY = 'geometry_rectangle/0342'
NAME = 'Geometry (rectangle) 0342'
CATEGORY = 'Geometry (rectangle)'
PROBLEM = 'The length of a rectangle is 2 more than its width. The perimeter is 132 cm. Find the dimensions.'
LET = 'w = width'
EQUATION = '2w + 2(w + 2) = 132'
SOLVE = '4w + 4 = 132 → w = 32'
ANSWER = 'Width 32 cm, length 34 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The length of a rectangle is {0} more than its width. The perimeter is {1} cm. Find the dimensions.'
NUMBERS = ['2', '132']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
