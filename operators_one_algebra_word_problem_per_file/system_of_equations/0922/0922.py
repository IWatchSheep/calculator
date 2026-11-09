"""Algebra word problem 0922   [System of equations]

Problem : The perimeter of a rectangle is 60 m and its length is 10 m more than its width. Find the length and width.
Let     : l = length, w = width
Equation: 2l + 2w = 60;  l = w + 10
Solve   : Substitute → l = 20, w = 10
Answer  : 20 m by 10 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0922'
KEY = 'system_of_equations/0922'
NAME = 'System of equations 0922'
CATEGORY = 'System of equations'
PROBLEM = 'The perimeter of a rectangle is 60 m and its length is 10 m more than its width. Find the length and width.'
LET = 'l = length, w = width'
EQUATION = '2l + 2w = 60;  l = w + 10'
SOLVE = 'Substitute → l = 20, w = 10'
ANSWER = '20 m by 10 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The perimeter of a rectangle is {0} m and its length is {1} m more than its width. Find the length and width.'
NUMBERS = ['60', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
