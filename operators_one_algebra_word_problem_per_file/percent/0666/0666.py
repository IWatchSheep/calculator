"""Algebra word problem 0666   [Percent]

Problem : Mateo spent 25% of a paycheck on rent and had $435 left. How much was the paycheck?
Let     : x = original amount
Equation: x − 0.25x = 435
Solve   : 0.75x = 435 → x = 580
Answer  : $580

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0666'
KEY = 'percent/0666'
NAME = 'Percent 0666'
CATEGORY = 'Percent'
PROBLEM = 'Mateo spent 25% of a paycheck on rent and had $435 left. How much was the paycheck?'
LET = 'x = original amount'
EQUATION = 'x − 0.25x = 435'
SOLVE = '0.75x = 435 → x = 580'
ANSWER = '$580'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Mateo spent {0}% of a paycheck on rent and had ${1} left. How much was the paycheck?'
NUMBERS = ['25', '435']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
