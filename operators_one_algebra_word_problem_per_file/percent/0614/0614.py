"""Algebra word problem 0614   [Percent]

Problem : A town's population changed from 2500 to 4000. What was the percent change?
Let     : p = percent change
Equation: 2500(1 + p/100) = 4000
Solve   : 1 + p/100 = 1.6 → p = 60
Answer  : +60% (increase)

Status  : ready: percent_change_between answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0614'
KEY = 'percent/0614'
NAME = 'Percent 0614'
CATEGORY = 'Percent'
PROBLEM = "A town's population changed from 2500 to 4000. What was the percent change?"
LET = 'p = percent change'
EQUATION = '2500(1 + p/100) = 4000'
SOLVE = '1 + p/100 = 1.6 → p = 60'
ANSWER = '+60% (increase)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change_between'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A town's population changed from {0} to {1}. What was the percent change?"
NUMBERS = ['2500', '4000']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
