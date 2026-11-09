"""Algebra word problem 0220   [Fractions]

Problem : Uma spent 1/4 of their money on a game and then 1/5 of what was left on lunch, leaving $60. How much did they start with?
Let     : x = starting money
Equation: x × (3/4) × (4/5) = 60
Solve   : 0.6x = 60 → x = 100
Answer  : $100

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0220'
KEY = 'fractions/0220'
NAME = 'Fractions 0220'
CATEGORY = 'Fractions'
PROBLEM = 'Uma spent 1/4 of their money on a game and then 1/5 of what was left on lunch, leaving $60. How much did they start with?'
LET = 'x = starting money'
EQUATION = 'x × (3/4) × (4/5) = 60'
SOLVE = '0.6x = 60 → x = 100'
ANSWER = '$100'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Uma spent {0}/{1} of their money on a game and then {2}/{3} of what was left on lunch, leaving ${4}. How much did they start with?'
NUMBERS = ['1', '4', '1', '5', '60']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
