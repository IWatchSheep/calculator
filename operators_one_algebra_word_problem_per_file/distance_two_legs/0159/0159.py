"""Algebra word problem 0159   [Distance (two legs)]

Problem : Pablo walked at 4 km/h and then rode a bus at 40 km/h. The whole trip was 13 km and took 1 hours. How long was the walk?
Let     : t = walking time (h)
Equation: 4t + 40(1 − t) = 13
Solve   : 36t = 27 → t = 0.75
Answer  : 0.75 h walking, 0.25 h on the bus

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0159'
KEY = 'distance_two_legs/0159'
NAME = 'Distance (two legs) 0159'
CATEGORY = 'Distance (two legs)'
PROBLEM = 'Pablo walked at 4 km/h and then rode a bus at 40 km/h. The whole trip was 13 km and took 1 hours. How long was the walk?'
LET = 't = walking time (h)'
EQUATION = '4t + 40(1 − t) = 13'
SOLVE = '36t = 27 → t = 0.75'
ANSWER = '0.75 h walking, 0.25 h on the bus'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Pablo walked at {0} km/h and then rode a bus at {1} km/h. The whole trip was {2} km and took {3} hours. How long was the walk?'
NUMBERS = ['4', '40', '13', '1']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
