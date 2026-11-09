"""Algebra word problem 0634   [Percent]

Problem : A town's population changed from 32000 to 40000. What was the percent change?
Let     : p = percent change
Equation: 32000(1 + p/100) = 40000
Solve   : 1 + p/100 = 1.25 → p = 25
Answer  : +25% (increase)

Status  : ready: percent_change_between answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0634'
KEY = 'percent/0634'
NAME = 'Percent 0634'
CATEGORY = 'Percent'
PROBLEM = "A town's population changed from 32000 to 40000. What was the percent change?"
LET = 'p = percent change'
EQUATION = '32000(1 + p/100) = 40000'
SOLVE = '1 + p/100 = 1.25 → p = 25'
ANSWER = '+25% (increase)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change_between'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A town's population changed from {0} to {1}. What was the percent change?"
NUMBERS = ['32000', '40000']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
