"""Algebra word problem 0530   [Linear model]

Problem : For a plumber's bill, 1 hours cost $66 and 9 hours cost $178. The cost is linear: C = m·x + b. Find m and b, then how many hours cost $234.
Let     : m = rate, b = fixed fee
Equation: m + b = 66;  9m + b = 178
Solve   : Subtract the equations → m = 14, b = 52
Answer  : m = 14, b = 52; 13 hours

Status  : ready: line_from_two_points answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0530'
KEY = 'linear_model/0530'
NAME = 'Linear model 0530'
CATEGORY = 'Linear model'
PROBLEM = "For a plumber's bill, 1 hours cost $66 and 9 hours cost $178. The cost is linear: C = m·x + b. Find m and b, then how many hours cost $234."
LET = 'm = rate, b = fixed fee'
EQUATION = 'm + b = 66;  9m + b = 178'
SOLVE = 'Subtract the equations → m = 14, b = 52'
ANSWER = 'm = 14, b = 52; 13 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'line_from_two_points'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "For a plumber's bill, {0} hours cost ${1} and {2} hours cost ${3}. The cost is linear: C = m·x + b. Find m and b, then how many hours cost ${4}."
NUMBERS = ['1', '66', '9', '178', '234']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
