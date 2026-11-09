"""Algebra word problem 0482   [Linear model]

Problem : For a taxi ride, 4 miles cost $46 and 11 miles cost $88. The cost is linear: C = m·x + b. Find m and b, then how many miles cost $136.
Let     : m = rate, b = fixed fee
Equation: 4m + b = 46;  11m + b = 88
Solve   : Subtract the equations → m = 6, b = 22
Answer  : m = 6, b = 22; 19 miles

Status  : ready: line_from_two_points answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0482'
KEY = 'linear_model/0482'
NAME = 'Linear model 0482'
CATEGORY = 'Linear model'
PROBLEM = 'For a taxi ride, 4 miles cost $46 and 11 miles cost $88. The cost is linear: C = m·x + b. Find m and b, then how many miles cost $136.'
LET = 'm = rate, b = fixed fee'
EQUATION = '4m + b = 46;  11m + b = 88'
SOLVE = 'Subtract the equations → m = 6, b = 22'
ANSWER = 'm = 6, b = 22; 19 miles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'line_from_two_points'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'For a taxi ride, {0} miles cost ${1} and {2} miles cost ${3}. The cost is linear: C = m·x + b. Find m and b, then how many miles cost ${4}.'
NUMBERS = ['4', '46', '11', '88', '136']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
