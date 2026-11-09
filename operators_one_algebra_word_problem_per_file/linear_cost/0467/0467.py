"""Algebra word problem 0467   [Linear cost]

Problem : A plumber charges a $80 call-out fee plus $65 per hour. The bill was $210.00. How long did the job take?
Let     : h = hours
Equation: 80 + 65h = 210
Solve   : 65h = 130 → h = 2
Answer  : 2 hours

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0467'
KEY = 'linear_cost/0467'
NAME = 'Linear cost 0467'
CATEGORY = 'Linear cost'
PROBLEM = 'A plumber charges a $80 call-out fee plus $65 per hour. The bill was $210.00. How long did the job take?'
LET = 'h = hours'
EQUATION = '80 + 65h = 210'
SOLVE = '65h = 130 → h = 2'
ANSWER = '2 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A plumber charges a ${0} call-out fee plus ${1} per hour. The bill was ${2}. How long did the job take?'
NUMBERS = ['80', '65', '210.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
