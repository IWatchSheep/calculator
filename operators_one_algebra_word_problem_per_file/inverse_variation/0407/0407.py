"""Algebra word problem 0407   [Inverse variation]

Problem : At 75 km/h a trip takes 2 hours. Time varies inversely with speed. How long would it take at 30 km/h?
Let     : t = hours
Equation: 75 × 2 = 30t
Solve   : 30t = 150 → t = 5
Answer  : 5 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0407'
KEY = 'inverse_variation/0407'
NAME = 'Inverse variation 0407'
CATEGORY = 'Inverse variation'
PROBLEM = 'At 75 km/h a trip takes 2 hours. Time varies inversely with speed. How long would it take at 30 km/h?'
LET = 't = hours'
EQUATION = '75 × 2 = 30t'
SOLVE = '30t = 150 → t = 5'
ANSWER = '5 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'At {0} km/h a trip takes {1} hours. Time varies inversely with speed. How long would it take at {2} km/h?'
NUMBERS = ['75', '2', '30']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
