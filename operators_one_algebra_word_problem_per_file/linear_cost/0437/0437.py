"""Algebra word problem 0437   [Linear cost]

Problem : A plumber charges a $90 call-out fee plus $70 per hour. The bill was $370.00. How long did the job take?
Let     : h = hours
Equation: 90 + 70h = 370
Solve   : 70h = 280 → h = 4
Answer  : 4 hours

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0437'
KEY = 'linear_cost/0437'
NAME = 'Linear cost 0437'
CATEGORY = 'Linear cost'
PROBLEM = 'A plumber charges a $90 call-out fee plus $70 per hour. The bill was $370.00. How long did the job take?'
LET = 'h = hours'
EQUATION = '90 + 70h = 370'
SOLVE = '70h = 280 → h = 4'
ANSWER = '4 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A plumber charges a ${0} call-out fee plus ${1} per hour. The bill was ${2}. How long did the job take?'
NUMBERS = ['90', '70', '370.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
