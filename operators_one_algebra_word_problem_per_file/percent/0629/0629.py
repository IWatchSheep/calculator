"""Algebra word problem 0629   [Percent]

Problem : Rhea spent 40% of a paycheck on rent and had $192 left. How much was the paycheck?
Let     : x = original amount
Equation: x − 0.4x = 192
Solve   : 0.6x = 192 → x = 320
Answer  : $320

Status  : ready: percent_spent_left answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0629'
KEY = 'percent/0629'
NAME = 'Percent 0629'
CATEGORY = 'Percent'
PROBLEM = 'Rhea spent 40% of a paycheck on rent and had $192 left. How much was the paycheck?'
LET = 'x = original amount'
EQUATION = 'x − 0.4x = 192'
SOLVE = '0.6x = 192 → x = 320'
ANSWER = '$320'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_spent_left'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Rhea spent {0}% of a paycheck on rent and had ${1} left. How much was the paycheck?'
NUMBERS = ['40', '192']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
