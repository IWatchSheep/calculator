"""Algebra word problem 0503   [Linear model]

Problem : A hot-air balloon at 5500 ft descends 200 ft per minute. Another at 2200 ft rises 900 ft per minute. When are they at the same height?
Let     : t = minutes
Equation: 5500 − 200t = 2200 + 900t
Solve   : 1100t = 3300 → t = 3
Answer  : 3 minutes

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0503'
KEY = 'linear_model/0503'
NAME = 'Linear model 0503'
CATEGORY = 'Linear model'
PROBLEM = 'A hot-air balloon at 5500 ft descends 200 ft per minute. Another at 2200 ft rises 900 ft per minute. When are they at the same height?'
LET = 't = minutes'
EQUATION = '5500 − 200t = 2200 + 900t'
SOLVE = '1100t = 3300 → t = 3'
ANSWER = '3 minutes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A hot-air balloon at {0} ft descends {1} ft per minute. Another at {2} ft rises {3} ft per minute. When are they at the same height?'
NUMBERS = ['5500', '200', '2200', '900']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
