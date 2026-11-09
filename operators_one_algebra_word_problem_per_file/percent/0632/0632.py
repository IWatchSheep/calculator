"""Algebra word problem 0632   [Percent]

Problem : What percent of 70 is 28?
Let     : p = percent
Equation: (p/100)(70) = 28
Solve   : 0.7p = 28 → p = 40
Answer  : 40%

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0632'
KEY = 'percent/0632'
NAME = 'Percent 0632'
CATEGORY = 'Percent'
PROBLEM = 'What percent of 70 is 28?'
LET = 'p = percent'
EQUATION = '(p/100)(70) = 28'
SOLVE = '0.7p = 28 → p = 40'
ANSWER = '40%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'What percent of {0} is {1}?'
NUMBERS = ['70', '28']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
