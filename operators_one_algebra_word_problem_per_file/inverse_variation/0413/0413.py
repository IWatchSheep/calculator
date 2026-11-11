"""Algebra word problem 0413   [Inverse variation]

Problem : 4 workers can build a wall in 15 days. At the same rate, how many days would 10 workers take?
Let     : d = days
Equation: 4 × 15 = 10 × d
Solve   : d = 60/10 = 6
Answer  : 6 days

Status  : ready: archive_inverse_variation_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0413'
KEY = 'inverse_variation/0413'
NAME = 'Inverse variation 0413'
CATEGORY = 'Inverse variation'
PROBLEM = '4 workers can build a wall in 15 days. At the same rate, how many days would 10 workers take?'
LET = 'd = days'
EQUATION = '4 × 15 = 10 × d'
SOLVE = 'd = 60/10 = 6'
ANSWER = '6 days'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_inverse_variation_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} workers can build a wall in {1} days. At the same rate, how many days would {2} workers take?'
NUMBERS = ['4', '15', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
