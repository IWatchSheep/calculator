"""Algebra word problem 0446   [Linear cost]

Problem : A plumber charges a $100 call-out fee plus $70 per hour. The bill was $345.00. How long did the job take?
Let     : h = hours
Equation: 100 + 70h = 345
Solve   : 70h = 245 → h = 3.5
Answer  : 3.5 hours

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0446'
KEY = 'linear_cost/0446'
NAME = 'Linear cost 0446'
CATEGORY = 'Linear cost'
PROBLEM = 'A plumber charges a $100 call-out fee plus $70 per hour. The bill was $345.00. How long did the job take?'
LET = 'h = hours'
EQUATION = '100 + 70h = 345'
SOLVE = '70h = 245 → h = 3.5'
ANSWER = '3.5 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A plumber charges a ${0} call-out fee plus ${1} per hour. The bill was ${2}. How long did the job take?'
NUMBERS = ['100', '70', '345.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
