"""Algebra word problem 0504   [Linear model]

Problem : For a taxi ride, 2 miles cost $104 and 7 miles cost $129. The cost is linear: C = m·x + b. Find m and b, then how many miles cost $159.
Let     : m = rate, b = fixed fee
Equation: 2m + b = 104;  7m + b = 129
Solve   : Subtract the equations → m = 5, b = 94
Answer  : m = 5, b = 94; 13 miles

Status  : ready: line_from_two_points answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0504'
KEY = 'linear_model/0504'
NAME = 'Linear model 0504'
CATEGORY = 'Linear model'
PROBLEM = 'For a taxi ride, 2 miles cost $104 and 7 miles cost $129. The cost is linear: C = m·x + b. Find m and b, then how many miles cost $159.'
LET = 'm = rate, b = fixed fee'
EQUATION = '2m + b = 104;  7m + b = 129'
SOLVE = 'Subtract the equations → m = 5, b = 94'
ANSWER = 'm = 5, b = 94; 13 miles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'line_from_two_points'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'For a taxi ride, {0} miles cost ${1} and {2} miles cost ${3}. The cost is linear: C = m·x + b. Find m and b, then how many miles cost ${4}.'
NUMBERS = ['2', '104', '7', '129', '159']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
