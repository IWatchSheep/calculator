"""Algebra word problem 0865   [Simple interest]

Problem : How many years will it take $2,000.00 to earn $480.00 in simple interest at 4% per year?
Let     : t = years
Equation: 2000 × 0.04 × t = 480
Solve   : 80t = 480 → t = 6
Answer  : 6 years

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0865'
KEY = 'simple_interest/0865'
NAME = 'Simple interest 0865'
CATEGORY = 'Simple interest'
PROBLEM = 'How many years will it take $2,000.00 to earn $480.00 in simple interest at 4% per year?'
LET = 't = years'
EQUATION = '2000 × 0.04 × t = 480'
SOLVE = '80t = 480 → t = 6'
ANSWER = '6 years'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many years will it take ${0} to earn ${1} in simple interest at {2}% per year?'
NUMBERS = ['2000.00', '480.00', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
