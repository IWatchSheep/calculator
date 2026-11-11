"""Algebra word problem 0148   [Distance (round trip)]

Problem : Aiden drove to a lake at 30 mph and returned on the same road at 20 mph. The round trip took 5 hours. How far is the lake?
Let     : d = one-way distance
Equation: d/30 + d/20 = 5
Solve   : Multiply by 60 → d = 60
Answer  : 60 miles

Status  : ready: round_trip_lake_distance answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0148'
KEY = 'distance_round_trip/0148'
NAME = 'Distance (round trip) 0148'
CATEGORY = 'Distance (round trip)'
PROBLEM = 'Aiden drove to a lake at 30 mph and returned on the same road at 20 mph. The round trip took 5 hours. How far is the lake?'
LET = 'd = one-way distance'
EQUATION = 'd/30 + d/20 = 5'
SOLVE = 'Multiply by 60 → d = 60'
ANSWER = '60 miles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'round_trip_lake_distance'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Aiden drove to a lake at {0} mph and returned on the same road at {1} mph. The round trip took {2} hours. How far is the lake?'
NUMBERS = ['30', '20', '5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
