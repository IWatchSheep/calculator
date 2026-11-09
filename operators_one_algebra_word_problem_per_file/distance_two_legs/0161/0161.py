"""Algebra word problem 0161   [Distance (two legs)]

Problem : Quinn walked at 3 km/h and then rode a bus at 30 km/h. The whole trip was 10.5 km and took 1.25 hours. How long was the walk?
Let     : t = walking time (h)
Equation: 3t + 30(1.25 − t) = 10.5
Solve   : 27t = 27 → t = 1
Answer  : 1 h walking, 0.25 h on the bus

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0161'
KEY = 'distance_two_legs/0161'
NAME = 'Distance (two legs) 0161'
CATEGORY = 'Distance (two legs)'
PROBLEM = 'Quinn walked at 3 km/h and then rode a bus at 30 km/h. The whole trip was 10.5 km and took 1.25 hours. How long was the walk?'
LET = 't = walking time (h)'
EQUATION = '3t + 30(1.25 − t) = 10.5'
SOLVE = '27t = 27 → t = 1'
ANSWER = '1 h walking, 0.25 h on the bus'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Quinn walked at {0} km/h and then rode a bus at {1} km/h. The whole trip was {2} km and took {3} hours. How long was the walk?'
NUMBERS = ['3', '30', '10.5', '1.25']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
