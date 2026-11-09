"""Algebra word problem 0492   [Linear model]

Problem : A tractor bought for $15,000.00 loses $500.00 in value each year. After how many years will it be worth $11,000.00?
Let     : y = years
Equation: 15000 − 500y = 11000
Solve   : 500y = 4000 → y = 8
Answer  : 8 years

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0492'
KEY = 'linear_model/0492'
NAME = 'Linear model 0492'
CATEGORY = 'Linear model'
PROBLEM = 'A tractor bought for $15,000.00 loses $500.00 in value each year. After how many years will it be worth $11,000.00?'
LET = 'y = years'
EQUATION = '15000 − 500y = 11000'
SOLVE = '500y = 4000 → y = 8'
ANSWER = '8 years'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A tractor bought for ${0} loses ${1} in value each year. After how many years will it be worth ${2}?'
NUMBERS = ['15000.00', '500.00', '11000.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
