"""Algebra word problem 0405   [Inverse variation]

Problem : At 60 km/h a trip takes 5 hours. Time varies inversely with speed. How long would it take at 120 km/h?
Let     : t = hours
Equation: 60 × 5 = 120t
Solve   : 120t = 300 → t = 2.5
Answer  : 2.5 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0405'
KEY = 'inverse_variation/0405'
NAME = 'Inverse variation 0405'
CATEGORY = 'Inverse variation'
PROBLEM = 'At 60 km/h a trip takes 5 hours. Time varies inversely with speed. How long would it take at 120 km/h?'
LET = 't = hours'
EQUATION = '60 × 5 = 120t'
SOLVE = '120t = 300 → t = 2.5'
ANSWER = '2.5 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'At {0} km/h a trip takes {1} hours. Time varies inversely with speed. How long would it take at {2} km/h?'
NUMBERS = ['60', '5', '120']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
