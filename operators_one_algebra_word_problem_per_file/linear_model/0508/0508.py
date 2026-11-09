"""Algebra word problem 0508   [Linear model]

Problem : A tractor bought for $17,000.00 loses $1,100.00 in value each year. After how many years will it be worth $10,400.00?
Let     : y = years
Equation: 17000 − 1100y = 10400
Solve   : 1100y = 6600 → y = 6
Answer  : 6 years

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0508'
KEY = 'linear_model/0508'
NAME = 'Linear model 0508'
CATEGORY = 'Linear model'
PROBLEM = 'A tractor bought for $17,000.00 loses $1,100.00 in value each year. After how many years will it be worth $10,400.00?'
LET = 'y = years'
EQUATION = '17000 − 1100y = 10400'
SOLVE = '1100y = 6600 → y = 6'
ANSWER = '6 years'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A tractor bought for ${0} loses ${1} in value each year. After how many years will it be worth ${2}?'
NUMBERS = ['17000.00', '1100.00', '10400.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
