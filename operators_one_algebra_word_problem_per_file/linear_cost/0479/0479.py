"""Algebra word problem 0479   [Linear cost]

Problem : An electric bill is $12 per month plus $0.18 per kWh. This month's bill is $157.80. How many kWh were used?
Let     : k = kWh
Equation: 12 + 0.18k = 157.8
Solve   : 0.18k = 145.8 → k = 810
Answer  : 810 kWh

Status  : ready: archive_linear_cost_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0479'
KEY = 'linear_cost/0479'
NAME = 'Linear cost 0479'
CATEGORY = 'Linear cost'
PROBLEM = "An electric bill is $12 per month plus $0.18 per kWh. This month's bill is $157.80. How many kWh were used?"
LET = 'k = kWh'
EQUATION = '12 + 0.18k = 157.8'
SOLVE = '0.18k = 145.8 → k = 810'
ANSWER = '810 kWh'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_linear_cost_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "An electric bill is ${0} per month plus ${1} per kWh. This month's bill is ${2}. How many kWh were used?"
NUMBERS = ['12', '0.18', '157.80']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
