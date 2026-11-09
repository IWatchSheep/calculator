"""Algebra word problem 0089   [Current / wind]

Problem : A plane flies 2300 miles with the wind in 5 hours. Flying back against the same wind takes 5.75 hours. Find the plane's speed in still air and the wind speed.
Let     : p = plane speed, w = wind speed
Equation: p + w = 460;  p − w = 400
Solve   : 2p = 860 → p = 430, w = 30
Answer  : Plane 430 mph, wind 30 mph

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0089'
KEY = 'current_wind/0089'
NAME = 'Current / wind 0089'
CATEGORY = 'Current / wind'
PROBLEM = "A plane flies 2300 miles with the wind in 5 hours. Flying back against the same wind takes 5.75 hours. Find the plane's speed in still air and the wind speed."
LET = 'p = plane speed, w = wind speed'
EQUATION = 'p + w = 460;  p − w = 400'
SOLVE = '2p = 860 → p = 430, w = 30'
ANSWER = 'Plane 430 mph, wind 30 mph'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A plane flies {0} miles with the wind in {1} hours. Flying back against the same wind takes {2} hours. Find the plane's speed in still air and the wind speed."
NUMBERS = ['2300', '5', '5.75']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
