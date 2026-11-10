"""Algebra word problem 0650   [Percent]

Problem : Kira spent 60% of a paycheck on rent and had $424 left. How much was the paycheck?
Let     : x = original amount
Equation: x − 0.6x = 424
Solve   : 0.4x = 424 → x = 1060
Answer  : $1060

Status  : ready: percent_spent_left answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0650'
KEY = 'percent/0650'
NAME = 'Percent 0650'
CATEGORY = 'Percent'
PROBLEM = 'Kira spent 60% of a paycheck on rent and had $424 left. How much was the paycheck?'
LET = 'x = original amount'
EQUATION = 'x − 0.6x = 424'
SOLVE = '0.4x = 424 → x = 1060'
ANSWER = '$1060'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_spent_left'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Kira spent {0}% of a paycheck on rent and had ${1} left. How much was the paycheck?'
NUMBERS = ['60', '424']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
