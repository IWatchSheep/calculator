"""Algebra word problem 0478   [Linear cost]

Problem : A taxi charges $4.00 plus $2.00 per mile. A ride costs $10.00. How many miles was the ride?
Let     : m = miles
Equation: 4 + 2m = 10
Solve   : 2m = 6 → m = 3
Answer  : 3 miles

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0478'
KEY = 'linear_cost/0478'
NAME = 'Linear cost 0478'
CATEGORY = 'Linear cost'
PROBLEM = 'A taxi charges $4.00 plus $2.00 per mile. A ride costs $10.00. How many miles was the ride?'
LET = 'm = miles'
EQUATION = '4 + 2m = 10'
SOLVE = '2m = 6 → m = 3'
ANSWER = '3 miles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A taxi charges ${0} plus ${1} per mile. A ride costs ${2}. How many miles was the ride?'
NUMBERS = ['4.00', '2.00', '10.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
