"""Algebra word problem 0142   [Distance (round trip)]

Problem : Bea drove to a lake at 60 mph and returned on the same road at 30 mph. The round trip took 10 hours. How far is the lake?
Let     : d = one-way distance
Equation: d/60 + d/30 = 10
Solve   : Multiply by 60 → d = 200
Answer  : 200 miles

Status  : ready: round_trip_lake_distance answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0142'
KEY = 'distance_round_trip/0142'
NAME = 'Distance (round trip) 0142'
CATEGORY = 'Distance (round trip)'
PROBLEM = 'Bea drove to a lake at 60 mph and returned on the same road at 30 mph. The round trip took 10 hours. How far is the lake?'
LET = 'd = one-way distance'
EQUATION = 'd/60 + d/30 = 10'
SOLVE = 'Multiply by 60 → d = 200'
ANSWER = '200 miles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'round_trip_lake_distance'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Bea drove to a lake at {0} mph and returned on the same road at {1} mph. The round trip took {2} hours. How far is the lake?'
NUMBERS = ['60', '30', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
