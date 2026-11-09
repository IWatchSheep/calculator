"""Algebra word problem 0724   [Proportion]

Problem : A model car is built at a 1:100 scale. The real car is 500 cm long. How long is the model?
Let     : x = model length
Equation: 1/100 = x/500
Solve   : x/500 = 0.01 → x = 0.01 × 500 = 5
Answer  : 5

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0724'
KEY = 'proportion/0724'
NAME = 'Proportion 0724'
CATEGORY = 'Proportion'
PROBLEM = 'A model car is built at a 1:100 scale. The real car is 500 cm long. How long is the model?'
LET = 'x = model length'
EQUATION = '1/100 = x/500'
SOLVE = 'x/500 = 0.01 → x = 0.01 × 500 = 5'
ANSWER = '5'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A model car is built at a {0}:{1} scale. The real car is {2} cm long. How long is the model?'
NUMBERS = ['1', '100', '500']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
