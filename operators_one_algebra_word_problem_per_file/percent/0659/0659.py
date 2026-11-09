"""Algebra word problem 0659   [Percent]

Problem : After a 25% discount, a bicycle costs $258.75. What was the original price?
Let     : p = original price
Equation: 0.75p = 258.75
Solve   : p = 258.75 ÷ 0.75 = 345
Answer  : $345.00

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0659'
KEY = 'percent/0659'
NAME = 'Percent 0659'
CATEGORY = 'Percent'
PROBLEM = 'After a 25% discount, a bicycle costs $258.75. What was the original price?'
LET = 'p = original price'
EQUATION = '0.75p = 258.75'
SOLVE = 'p = 258.75 ÷ 0.75 = 345'
ANSWER = '$345.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'After a {0}% discount, a bicycle costs ${1}. What was the original price?'
NUMBERS = ['25', '258.75']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
