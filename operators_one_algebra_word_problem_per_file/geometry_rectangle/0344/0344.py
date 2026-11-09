"""Algebra word problem 0344   [Geometry (rectangle)]

Problem : The length of a rectangle is 5 more than 3 times its width. The perimeter is 170 cm. Find the dimensions.
Let     : w = width
Equation: 2w + 2(3w + 5) = 170
Solve   : 8w + 10 = 170 → w = 20
Answer  : Width 20 cm, length 65 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0344'
KEY = 'geometry_rectangle/0344'
NAME = 'Geometry (rectangle) 0344'
CATEGORY = 'Geometry (rectangle)'
PROBLEM = 'The length of a rectangle is 5 more than 3 times its width. The perimeter is 170 cm. Find the dimensions.'
LET = 'w = width'
EQUATION = '2w + 2(3w + 5) = 170'
SOLVE = '8w + 10 = 170 → w = 20'
ANSWER = 'Width 20 cm, length 65 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The length of a rectangle is {0} more than {1} times its width. The perimeter is {2} cm. Find the dimensions.'
NUMBERS = ['5', '3', '170']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
