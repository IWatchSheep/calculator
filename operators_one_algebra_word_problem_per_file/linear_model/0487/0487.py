"""Algebra word problem 0487   [Linear model]

Problem : A tractor bought for $23,000.00 loses $1,600.00 in value each year. After how many years will it be worth $16,600.00?
Let     : y = years
Equation: 23000 − 1600y = 16600
Solve   : 1600y = 6400 → y = 4
Answer  : 4 years

Status  : ready: archive_linear_model_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0487'
KEY = 'linear_model/0487'
NAME = 'Linear model 0487'
CATEGORY = 'Linear model'
PROBLEM = 'A tractor bought for $23,000.00 loses $1,600.00 in value each year. After how many years will it be worth $16,600.00?'
LET = 'y = years'
EQUATION = '23000 − 1600y = 16600'
SOLVE = '1600y = 6400 → y = 4'
ANSWER = '4 years'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_linear_model_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A tractor bought for ${0} loses ${1} in value each year. After how many years will it be worth ${2}?'
NUMBERS = ['23000.00', '1600.00', '16600.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
