"""Algebra word problem 0515   [Linear model]

Problem : A hot-air balloon at 6900 ft descends 650 ft per minute. Another at 1400 ft rises 450 ft per minute. When are they at the same height?
Let     : t = minutes
Equation: 6900 − 650t = 1400 + 450t
Solve   : 1100t = 5500 → t = 5
Answer  : 5 minutes

Status  : ready: archive_linear_model_3 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0515'
KEY = 'linear_model/0515'
NAME = 'Linear model 0515'
CATEGORY = 'Linear model'
PROBLEM = 'A hot-air balloon at 6900 ft descends 650 ft per minute. Another at 1400 ft rises 450 ft per minute. When are they at the same height?'
LET = 't = minutes'
EQUATION = '6900 − 650t = 1400 + 450t'
SOLVE = '1100t = 5500 → t = 5'
ANSWER = '5 minutes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_linear_model_3'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A hot-air balloon at {0} ft descends {1} ft per minute. Another at {2} ft rises {3} ft per minute. When are they at the same height?'
NUMBERS = ['6900', '650', '1400', '450']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
