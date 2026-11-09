"""Algebra word problem 0145   [Distance (round trip)]

Problem : A cyclist rides 280 km to a town and returns 10 km/h faster. The whole trip takes 7.5 hours. How fast was the outbound ride?
Let     : s = outbound speed
Equation: 280/s + 280/(s + 10) = 7.5
Solve   : Clear denominators → quadratic → s = 70 (reject negative)
Answer  : 70 km/h

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0145'
KEY = 'distance_round_trip/0145'
NAME = 'Distance (round trip) 0145'
CATEGORY = 'Distance (round trip)'
PROBLEM = 'A cyclist rides 280 km to a town and returns 10 km/h faster. The whole trip takes 7.5 hours. How fast was the outbound ride?'
LET = 's = outbound speed'
EQUATION = '280/s + 280/(s + 10) = 7.5'
SOLVE = 'Clear denominators → quadratic → s = 70 (reject negative)'
ANSWER = '70 km/h'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A cyclist rides {0} km to a town and returns {1} km/h faster. The whole trip takes {2} hours. How fast was the outbound ride?'
NUMBERS = ['280', '10', '7.5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
