"""Algebra word problem 0505   [Linear model]

Problem : A phone at 85% battery loses 15% per hour. After how many hours will it be at 10%?
Let     : h = hours
Equation: 85 − 15h = 10
Solve   : 15h = 75 → h = 5
Answer  : 5 hours

Status  : ready: archive_linear_model_4 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0505'
KEY = 'linear_model/0505'
NAME = 'Linear model 0505'
CATEGORY = 'Linear model'
PROBLEM = 'A phone at 85% battery loses 15% per hour. After how many hours will it be at 10%?'
LET = 'h = hours'
EQUATION = '85 − 15h = 10'
SOLVE = '15h = 75 → h = 5'
ANSWER = '5 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_linear_model_4'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A phone at {0}% battery loses {1}% per hour. After how many hours will it be at {2}%?'
NUMBERS = ['85', '15', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
