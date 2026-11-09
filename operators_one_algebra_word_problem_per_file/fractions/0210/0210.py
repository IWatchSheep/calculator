"""Algebra word problem 0210   [Fractions]

Problem : Maya spent 1/6 of their money on a game and then 1/5 of what was left on lunch, leaving $360. How much did they start with?
Let     : x = starting money
Equation: x × (5/6) × (4/5) = 360
Solve   : (2/3)x = 360 → x = 540
Answer  : $540

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0210'
KEY = 'fractions/0210'
NAME = 'Fractions 0210'
CATEGORY = 'Fractions'
PROBLEM = 'Maya spent 1/6 of their money on a game and then 1/5 of what was left on lunch, leaving $360. How much did they start with?'
LET = 'x = starting money'
EQUATION = 'x × (5/6) × (4/5) = 360'
SOLVE = '(2/3)x = 360 → x = 540'
ANSWER = '$540'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Maya spent {0}/{1} of their money on a game and then {2}/{3} of what was left on lunch, leaving ${4}. How much did they start with?'
NUMBERS = ['1', '6', '1', '5', '360']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
