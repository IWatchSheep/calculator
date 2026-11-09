"""Algebra word problem 0490   [Linear model]

Problem : A phone at 90% battery loses 5% per hour. After how many hours will it be at 20%?
Let     : h = hours
Equation: 90 − 5h = 20
Solve   : 5h = 70 → h = 14
Answer  : 14 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0490'
KEY = 'linear_model/0490'
NAME = 'Linear model 0490'
CATEGORY = 'Linear model'
PROBLEM = 'A phone at 90% battery loses 5% per hour. After how many hours will it be at 20%?'
LET = 'h = hours'
EQUATION = '90 − 5h = 20'
SOLVE = '5h = 70 → h = 14'
ANSWER = '14 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A phone at {0}% battery loses {1}% per hour. After how many hours will it be at {2}%?'
NUMBERS = ['90', '5', '20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
