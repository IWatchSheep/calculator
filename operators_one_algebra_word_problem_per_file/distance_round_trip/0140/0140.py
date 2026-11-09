"""Algebra word problem 0140   [Distance (round trip)]

Problem : Tara drove to a lake at 45 mph and returned on the same road at 36 mph. The round trip took 8 hours. How far is the lake?
Let     : d = one-way distance
Equation: d/45 + d/36 = 8
Solve   : Multiply by 180 → d = 160
Answer  : 160 miles

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0140'
KEY = 'distance_round_trip/0140'
NAME = 'Distance (round trip) 0140'
CATEGORY = 'Distance (round trip)'
PROBLEM = 'Tara drove to a lake at 45 mph and returned on the same road at 36 mph. The round trip took 8 hours. How far is the lake?'
LET = 'd = one-way distance'
EQUATION = 'd/45 + d/36 = 8'
SOLVE = 'Multiply by 180 → d = 160'
ANSWER = '160 miles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Tara drove to a lake at {0} mph and returned on the same road at {1} mph. The round trip took {2} hours. How far is the lake?'
NUMBERS = ['45', '36', '8']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
