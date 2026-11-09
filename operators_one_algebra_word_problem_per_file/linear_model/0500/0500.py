"""Algebra word problem 0500   [Linear model]

Problem : A phone at 90% battery loses 4% per hour. After how many hours will it be at 10%?
Let     : h = hours
Equation: 90 − 4h = 10
Solve   : 4h = 80 → h = 20
Answer  : 20 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0500'
KEY = 'linear_model/0500'
NAME = 'Linear model 0500'
CATEGORY = 'Linear model'
PROBLEM = 'A phone at 90% battery loses 4% per hour. After how many hours will it be at 10%?'
LET = 'h = hours'
EQUATION = '90 − 4h = 10'
SOLVE = '4h = 80 → h = 20'
ANSWER = '20 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A phone at {0}% battery loses {1}% per hour. After how many hours will it be at {2}%?'
NUMBERS = ['90', '4', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
