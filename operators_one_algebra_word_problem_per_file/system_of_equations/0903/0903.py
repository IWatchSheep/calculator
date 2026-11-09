"""Algebra word problem 0903   [System of equations]

Problem : The perimeter of a rectangle is 124 m and its length is 18 m more than its width. Find the length and width.
Let     : l = length, w = width
Equation: 2l + 2w = 124;  l = w + 18
Solve   : Substitute → l = 40, w = 22
Answer  : 40 m by 22 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0903'
KEY = 'system_of_equations/0903'
NAME = 'System of equations 0903'
CATEGORY = 'System of equations'
PROBLEM = 'The perimeter of a rectangle is 124 m and its length is 18 m more than its width. Find the length and width.'
LET = 'l = length, w = width'
EQUATION = '2l + 2w = 124;  l = w + 18'
SOLVE = 'Substitute → l = 40, w = 22'
ANSWER = '40 m by 22 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The perimeter of a rectangle is {0} m and its length is {1} m more than its width. Find the length and width.'
NUMBERS = ['124', '18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
