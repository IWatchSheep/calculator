"""Algebra word problem 0649   [Percent]

Problem : A town's population changed from 2000 to 1200. What was the percent change?
Let     : p = percent change
Equation: 2000(1 + p/100) = 1200
Solve   : 1 + p/100 = 0.6 → p = -40
Answer  : -40% (decrease)

Status  : ready: percent_change_between answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0649'
KEY = 'percent/0649'
NAME = 'Percent 0649'
CATEGORY = 'Percent'
PROBLEM = "A town's population changed from 2000 to 1200. What was the percent change?"
LET = 'p = percent change'
EQUATION = '2000(1 + p/100) = 1200'
SOLVE = '1 + p/100 = 0.6 → p = -40'
ANSWER = '-40% (decrease)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change_between'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A town's population changed from {0} to {1}. What was the percent change?"
NUMBERS = ['2000', '1200']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
