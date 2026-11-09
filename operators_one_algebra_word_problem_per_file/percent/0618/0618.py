"""Algebra word problem 0618   [Percent]

Problem : Yara spent 75% of a paycheck on rent and had $280 left. How much was the paycheck?
Let     : x = original amount
Equation: x − 0.75x = 280
Solve   : x/4 = 280 → x = 280 × 4 = 1120
Answer  : $1120

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0618'
KEY = 'percent/0618'
NAME = 'Percent 0618'
CATEGORY = 'Percent'
PROBLEM = 'Yara spent 75% of a paycheck on rent and had $280 left. How much was the paycheck?'
LET = 'x = original amount'
EQUATION = 'x − 0.75x = 280'
SOLVE = 'x/4 = 280 → x = 280 × 4 = 1120'
ANSWER = '$1120'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Yara spent {0}% of a paycheck on rent and had ${1} left. How much was the paycheck?'
NUMBERS = ['75', '280']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
