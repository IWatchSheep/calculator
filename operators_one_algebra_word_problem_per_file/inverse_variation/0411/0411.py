"""Algebra word problem 0411   [Inverse variation]

Problem : A gear with 24 teeth turning at 30 rpm drives a gear with 8 teeth. Teeth × rpm is the same for both gears. How fast does the second gear turn?
Let     : r = rpm
Equation: 24 × 30 = 8r
Solve   : 8r = 720 → r = 90
Answer  : 90 rpm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0411'
KEY = 'inverse_variation/0411'
NAME = 'Inverse variation 0411'
CATEGORY = 'Inverse variation'
PROBLEM = 'A gear with 24 teeth turning at 30 rpm drives a gear with 8 teeth. Teeth × rpm is the same for both gears. How fast does the second gear turn?'
LET = 'r = rpm'
EQUATION = '24 × 30 = 8r'
SOLVE = '8r = 720 → r = 90'
ANSWER = '90 rpm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A gear with {0} teeth turning at {1} rpm drives a gear with {2} teeth. Teeth × rpm is the same for both gears. How fast does the second gear turn?'
NUMBERS = ['24', '30', '8']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
