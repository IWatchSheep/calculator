"""Algebra word problem 0436   [Linear cost]

Problem : An electric bill is $12 per month plus $0.14 per kWh. This month's bill is $87.60. How many kWh were used?
Let     : k = kWh
Equation: 12 + 0.14k = 87.6
Solve   : 0.14k = 75.6 → k = 540
Answer  : 540 kWh

Status  : ready: archive_linear_cost_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0436'
KEY = 'linear_cost/0436'
NAME = 'Linear cost 0436'
CATEGORY = 'Linear cost'
PROBLEM = "An electric bill is $12 per month plus $0.14 per kWh. This month's bill is $87.60. How many kWh were used?"
LET = 'k = kWh'
EQUATION = '12 + 0.14k = 87.6'
SOLVE = '0.14k = 75.6 → k = 540'
ANSWER = '540 kWh'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_linear_cost_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "An electric bill is ${0} per month plus ${1} per kWh. This month's bill is ${2}. How many kWh were used?"
NUMBERS = ['12', '0.14', '87.60']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
