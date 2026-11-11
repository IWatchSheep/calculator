"""Algebra word problem 0402   [Inverse variation]

Problem : A gear with 24 teeth turning at 40 rpm drives a gear with 20 teeth. Teeth × rpm is the same for both gears. How fast does the second gear turn?
Let     : r = rpm
Equation: 24 × 40 = 20r
Solve   : 20r = 960 → r = 48
Answer  : 48 rpm

Status  : ready: archive_inverse_variation_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0402'
KEY = 'inverse_variation/0402'
NAME = 'Inverse variation 0402'
CATEGORY = 'Inverse variation'
PROBLEM = 'A gear with 24 teeth turning at 40 rpm drives a gear with 20 teeth. Teeth × rpm is the same for both gears. How fast does the second gear turn?'
LET = 'r = rpm'
EQUATION = '24 × 40 = 20r'
SOLVE = '20r = 960 → r = 48'
ANSWER = '48 rpm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_inverse_variation_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A gear with {0} teeth turning at {1} rpm drives a gear with {2} teeth. Teeth × rpm is the same for both gears. How fast does the second gear turn?'
NUMBERS = ['24', '40', '20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
