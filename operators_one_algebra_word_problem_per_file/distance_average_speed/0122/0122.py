"""Algebra word problem 0122   [Distance (average speed)]

Problem : A car goes from A to B at 30 km/h. How fast must it return so that the average speed for the round trip is 45 km/h?
Let     : v = return speed
Equation: 2/(1/30 + 1/v) = 45
Solve   : Rearrange: 1/v = 2/45 − 1/30 → v = 90
Answer  : 90 km/h

Status  : ready: archive_distance_average_speed_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0122'
KEY = 'distance_average_speed/0122'
NAME = 'Distance (average speed) 0122'
CATEGORY = 'Distance (average speed)'
PROBLEM = 'A car goes from A to B at 30 km/h. How fast must it return so that the average speed for the round trip is 45 km/h?'
LET = 'v = return speed'
EQUATION = '2/(1/30 + 1/v) = 45'
SOLVE = 'Rearrange: 1/v = 2/45 − 1/30 → v = 90'
ANSWER = '90 km/h'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_distance_average_speed_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A car goes from A to B at {0} km/h. How fast must it return so that the average speed for the round trip is {1} km/h?'
NUMBERS = ['30', '45']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
