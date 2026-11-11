"""Algebra word problem 0837   [Rational equation]

Problem : Jogging a route at 10 km/h takes 0.4 hours longer than cycling it at 15 km/h. How long is the route?
Let     : d = distance
Equation: d/10 − d/15 = 0.4
Solve   : Multiply by 30 → d = 12
Answer  : 12 km

Status  : ready: archive_rational_equation_4 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0837'
KEY = 'rational_equation/0837'
NAME = 'Rational equation 0837'
CATEGORY = 'Rational equation'
PROBLEM = 'Jogging a route at 10 km/h takes 0.4 hours longer than cycling it at 15 km/h. How long is the route?'
LET = 'd = distance'
EQUATION = 'd/10 − d/15 = 0.4'
SOLVE = 'Multiply by 30 → d = 12'
ANSWER = '12 km'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_rational_equation_4'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Jogging a route at {0} km/h takes {1} hours longer than cycling it at {2} km/h. How long is the route?'
NUMBERS = ['10', '0.4', '15']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
