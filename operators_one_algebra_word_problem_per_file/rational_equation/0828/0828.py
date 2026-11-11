"""Algebra word problem 0828   [Rational equation]

Problem : Jogging a route at 8 km/h takes 2.25 hours longer than cycling it at 20 km/h. How long is the route?
Let     : d = distance
Equation: d/8 − d/20 = 2.25
Solve   : Multiply by 40 → d = 30
Answer  : 30 km

Status  : ready: archive_rational_equation_4 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0828'
KEY = 'rational_equation/0828'
NAME = 'Rational equation 0828'
CATEGORY = 'Rational equation'
PROBLEM = 'Jogging a route at 8 km/h takes 2.25 hours longer than cycling it at 20 km/h. How long is the route?'
LET = 'd = distance'
EQUATION = 'd/8 − d/20 = 2.25'
SOLVE = 'Multiply by 40 → d = 30'
ANSWER = '30 km'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_rational_equation_4'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Jogging a route at {0} km/h takes {1} hours longer than cycling it at {2} km/h. How long is the route?'
NUMBERS = ['8', '2.25', '20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
