"""Algebra word problem 0401   [Inverse variation]

Problem : 12 workers can build a wall in 10 days. At the same rate, how many days would 3 workers take?
Let     : d = days
Equation: 12 × 10 = 3 × d
Solve   : d = 120/3 = 40
Answer  : 40 days

Status  : ready: archive_inverse_variation_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0401'
KEY = 'inverse_variation/0401'
NAME = 'Inverse variation 0401'
CATEGORY = 'Inverse variation'
PROBLEM = '12 workers can build a wall in 10 days. At the same rate, how many days would 3 workers take?'
LET = 'd = days'
EQUATION = '12 × 10 = 3 × d'
SOLVE = 'd = 120/3 = 40'
ANSWER = '40 days'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_inverse_variation_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} workers can build a wall in {1} days. At the same rate, how many days would {2} workers take?'
NUMBERS = ['12', '10', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
