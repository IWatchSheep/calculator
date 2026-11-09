"""Algebra word problem 0471   [Linear cost]

Problem : An electric bill is $15 per month plus $0.18 per kWh. This month's bill is $92.40. How many kWh were used?
Let     : k = kWh
Equation: 15 + 0.18k = 92.4
Solve   : 0.18k = 77.4 → k = 430
Answer  : 430 kWh

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0471'
KEY = 'linear_cost/0471'
NAME = 'Linear cost 0471'
CATEGORY = 'Linear cost'
PROBLEM = "An electric bill is $15 per month plus $0.18 per kWh. This month's bill is $92.40. How many kWh were used?"
LET = 'k = kWh'
EQUATION = '15 + 0.18k = 92.4'
SOLVE = '0.18k = 77.4 → k = 430'
ANSWER = '430 kWh'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "An electric bill is ${0} per month plus ${1} per kWh. This month's bill is ${2}. How many kWh were used?"
NUMBERS = ['15', '0.18', '92.40']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
