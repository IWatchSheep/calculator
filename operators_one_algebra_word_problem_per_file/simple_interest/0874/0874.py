"""Algebra word problem 0874   [Simple interest]

Problem : $15,000.00 earns $5,400.00 in simple interest over 9 years. What is the annual interest rate?
Let     : r = rate (as a percent)
Equation: 15000 × (r/100) × 9 = 5400
Solve   : 1350r = 5400 → r = 4
Answer  : 4%

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0874'
KEY = 'simple_interest/0874'
NAME = 'Simple interest 0874'
CATEGORY = 'Simple interest'
PROBLEM = '$15,000.00 earns $5,400.00 in simple interest over 9 years. What is the annual interest rate?'
LET = 'r = rate (as a percent)'
EQUATION = '15000 × (r/100) × 9 = 5400'
SOLVE = '1350r = 5400 → r = 4'
ANSWER = '4%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '${0} earns ${1} in simple interest over {2} years. What is the annual interest rate?'
NUMBERS = ['15000.00', '5400.00', '9']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
