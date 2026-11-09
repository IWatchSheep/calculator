"""Algebra word problem 0438   [Linear cost]

Problem : A rental car costs $35 per day plus $0.50 per mile. A 4-day rental cost $385.00. How many miles were driven?
Let     : m = miles
Equation: 35(4) + 0.5m = 385
Solve   : m/2 = 245 → m = 245 × 2 = 490
Answer  : 490 miles

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0438'
KEY = 'linear_cost/0438'
NAME = 'Linear cost 0438'
CATEGORY = 'Linear cost'
PROBLEM = 'A rental car costs $35 per day plus $0.50 per mile. A 4-day rental cost $385.00. How many miles were driven?'
LET = 'm = miles'
EQUATION = '35(4) + 0.5m = 385'
SOLVE = 'm/2 = 245 → m = 245 × 2 = 490'
ANSWER = '490 miles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rental car costs ${0} per day plus ${1} per mile. A {2}-day rental cost ${3}. How many miles were driven?'
NUMBERS = ['35', '0.50', '4', '385.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
