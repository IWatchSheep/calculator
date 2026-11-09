"""Algebra word problem 0821   [Rational equation]

Problem : Jogging a route at 8 km/h takes 10/3 hours longer than cycling it at 18 km/h. How long is the route?
Let     : d = distance
Equation: d/8 − d/18 = 10/3
Solve   : Multiply by 72 → d = 48
Answer  : 48 km

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0821'
KEY = 'rational_equation/0821'
NAME = 'Rational equation 0821'
CATEGORY = 'Rational equation'
PROBLEM = 'Jogging a route at 8 km/h takes 10/3 hours longer than cycling it at 18 km/h. How long is the route?'
LET = 'd = distance'
EQUATION = 'd/8 − d/18 = 10/3'
SOLVE = 'Multiply by 72 → d = 48'
ANSWER = '48 km'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Jogging a route at {0} km/h takes {1}/{2} hours longer than cycling it at {3} km/h. How long is the route?'
NUMBERS = ['8', '10', '3', '18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
