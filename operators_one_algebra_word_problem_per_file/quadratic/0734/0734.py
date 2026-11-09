"""Algebra word problem 0734   [Quadratic]

Problem : Two numbers add up to 56 and multiply to 780. What are they?
Let     : x = one number; other = 56 − x
Equation: x(56 − x) = 780
Solve   : x² − 56x + 780 = 0 → x = 26 (the other root, 30, gives the same pair)
Answer  : 26 and 30

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0734'
KEY = 'quadratic/0734'
NAME = 'Quadratic 0734'
CATEGORY = 'Quadratic'
PROBLEM = 'Two numbers add up to 56 and multiply to 780. What are they?'
LET = 'x = one number; other = 56 − x'
EQUATION = 'x(56 − x) = 780'
SOLVE = 'x² − 56x + 780 = 0 → x = 26 (the other root, 30, gives the same pair)'
ANSWER = '26 and 30'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two numbers add up to {0} and multiply to {1}. What are they?'
NUMBERS = ['56', '780']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
