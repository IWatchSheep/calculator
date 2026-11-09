"""Algebra word problem 0440   [Linear cost]

Problem : A taxi charges $3.00 plus $1.75 per mile. A ride costs $25.75. How many miles was the ride?
Let     : m = miles
Equation: 3 + 1.75m = 25.75
Solve   : 1.75m = 22.75 → m = 13
Answer  : 13 miles

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0440'
KEY = 'linear_cost/0440'
NAME = 'Linear cost 0440'
CATEGORY = 'Linear cost'
PROBLEM = 'A taxi charges $3.00 plus $1.75 per mile. A ride costs $25.75. How many miles was the ride?'
LET = 'm = miles'
EQUATION = '3 + 1.75m = 25.75'
SOLVE = '1.75m = 22.75 → m = 13'
ANSWER = '13 miles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A taxi charges ${0} plus ${1} per mile. A ride costs ${2}. How many miles was the ride?'
NUMBERS = ['3.00', '1.75', '25.75']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
