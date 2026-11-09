"""Algebra word problem 0513   [Linear model]

Problem : A delivery van bought for $22,000.00 loses $3,800.00 in value each year. After how many years will it be worth $6,800.00?
Let     : y = years
Equation: 22000 − 3800y = 6800
Solve   : 3800y = 15200 → y = 4
Answer  : 4 years

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0513'
KEY = 'linear_model/0513'
NAME = 'Linear model 0513'
CATEGORY = 'Linear model'
PROBLEM = 'A delivery van bought for $22,000.00 loses $3,800.00 in value each year. After how many years will it be worth $6,800.00?'
LET = 'y = years'
EQUATION = '22000 − 3800y = 6800'
SOLVE = '3800y = 15200 → y = 4'
ANSWER = '4 years'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A delivery van bought for ${0} loses ${1} in value each year. After how many years will it be worth ${2}?'
NUMBERS = ['22000.00', '3800.00', '6800.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
