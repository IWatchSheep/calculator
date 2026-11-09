"""Algebra word problem 0461   [Linear cost]

Problem : A taxi charges $4.00 plus $1.50 per mile. A ride costs $16.00. How many miles was the ride?
Let     : m = miles
Equation: 4 + 1.5m = 16
Solve   : 1.5m = 12 → m = 8
Answer  : 8 miles

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0461'
KEY = 'linear_cost/0461'
NAME = 'Linear cost 0461'
CATEGORY = 'Linear cost'
PROBLEM = 'A taxi charges $4.00 plus $1.50 per mile. A ride costs $16.00. How many miles was the ride?'
LET = 'm = miles'
EQUATION = '4 + 1.5m = 16'
SOLVE = '1.5m = 12 → m = 8'
ANSWER = '8 miles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A taxi charges ${0} plus ${1} per mile. A ride costs ${2}. How many miles was the ride?'
NUMBERS = ['4.00', '1.50', '16.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
