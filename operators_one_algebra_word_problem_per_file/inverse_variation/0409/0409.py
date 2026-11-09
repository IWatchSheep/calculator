"""Algebra word problem 0409   [Inverse variation]

Problem : 5 workers can build a wall in 24 days. At the same rate, how many days would 24 workers take?
Let     : d = days
Equation: 5 × 24 = 24 × d
Solve   : d = 120/24 = 5
Answer  : 5 days

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0409'
KEY = 'inverse_variation/0409'
NAME = 'Inverse variation 0409'
CATEGORY = 'Inverse variation'
PROBLEM = '5 workers can build a wall in 24 days. At the same rate, how many days would 24 workers take?'
LET = 'd = days'
EQUATION = '5 × 24 = 24 × d'
SOLVE = 'd = 120/24 = 5'
ANSWER = '5 days'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} workers can build a wall in {1} days. At the same rate, how many days would {2} workers take?'
NUMBERS = ['5', '24', '24']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
