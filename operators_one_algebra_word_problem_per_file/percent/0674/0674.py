"""Algebra word problem 0674   [Percent]

Problem : A town's population changed from 6500 to 11700. What was the percent change?
Let     : p = percent change
Equation: 6500(1 + p/100) = 11700
Solve   : 1 + p/100 = 1.8 → p = 80
Answer  : +80% (increase)

Status  : ready: percent_change_between answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0674'
KEY = 'percent/0674'
NAME = 'Percent 0674'
CATEGORY = 'Percent'
PROBLEM = "A town's population changed from 6500 to 11700. What was the percent change?"
LET = 'p = percent change'
EQUATION = '6500(1 + p/100) = 11700'
SOLVE = '1 + p/100 = 1.8 → p = 80'
ANSWER = '+80% (increase)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change_between'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A town's population changed from {0} to {1}. What was the percent change?"
NUMBERS = ['6500', '11700']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
