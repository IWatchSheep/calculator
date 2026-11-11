"""Algebra word problem 0412   [Inverse variation]

Problem : At 72 km/h a trip takes 5 hours. Time varies inversely with speed. How long would it take at 120 km/h?
Let     : t = hours
Equation: 72 × 5 = 120t
Solve   : 120t = 360 → t = 3
Answer  : 3 hours

Status  : ready: archive_inverse_variation_3 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0412'
KEY = 'inverse_variation/0412'
NAME = 'Inverse variation 0412'
CATEGORY = 'Inverse variation'
PROBLEM = 'At 72 km/h a trip takes 5 hours. Time varies inversely with speed. How long would it take at 120 km/h?'
LET = 't = hours'
EQUATION = '72 × 5 = 120t'
SOLVE = '120t = 360 → t = 3'
ANSWER = '3 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_inverse_variation_3'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'At {0} km/h a trip takes {1} hours. Time varies inversely with speed. How long would it take at {2} km/h?'
NUMBERS = ['72', '5', '120']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
