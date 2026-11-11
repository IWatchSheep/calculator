"""Algebra word problem 0141   [Distance (round trip)]

Problem : A cyclist rides 225 km to a town and returns 5 km/h faster. The whole trip takes 9.5 hours. How fast was the outbound ride?
Let     : s = outbound speed
Equation: 225/s + 225/(s + 5) = 9.5
Solve   : Clear denominators → quadratic → s = 45 (reject negative)
Answer  : 45 km/h

Status  : ready: archive_distance_round_trip_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0141'
KEY = 'distance_round_trip/0141'
NAME = 'Distance (round trip) 0141'
CATEGORY = 'Distance (round trip)'
PROBLEM = 'A cyclist rides 225 km to a town and returns 5 km/h faster. The whole trip takes 9.5 hours. How fast was the outbound ride?'
LET = 's = outbound speed'
EQUATION = '225/s + 225/(s + 5) = 9.5'
SOLVE = 'Clear denominators → quadratic → s = 45 (reject negative)'
ANSWER = '45 km/h'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_distance_round_trip_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A cyclist rides {0} km to a town and returns {1} km/h faster. The whole trip takes {2} hours. How fast was the outbound ride?'
NUMBERS = ['225', '5', '9.5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
