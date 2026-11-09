"""Algebra word problem 0452   [Linear cost]

Problem : An electric bill is $8 per month plus $0.11 per kWh. This month's bill is $79.50. How many kWh were used?
Let     : k = kWh
Equation: 8 + 0.11k = 79.5
Solve   : 0.11k = 71.5 → k = 650
Answer  : 650 kWh

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0452'
KEY = 'linear_cost/0452'
NAME = 'Linear cost 0452'
CATEGORY = 'Linear cost'
PROBLEM = "An electric bill is $8 per month plus $0.11 per kWh. This month's bill is $79.50. How many kWh were used?"
LET = 'k = kWh'
EQUATION = '8 + 0.11k = 79.5'
SOLVE = '0.11k = 71.5 → k = 650'
ANSWER = '650 kWh'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "An electric bill is ${0} per month plus ${1} per kWh. This month's bill is ${2}. How many kWh were used?"
NUMBERS = ['8', '0.11', '79.50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
