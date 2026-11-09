"""Algebra word problem 0744   [Quadratic]

Problem : Two numbers add up to 51 and multiply to 644. What are they?
Let     : x = one number; other = 51 − x
Equation: x(51 − x) = 644
Solve   : x² − 51x + 644 = 0 → x = 23 (the other root, 28, gives the same pair)
Answer  : 23 and 28

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0744'
KEY = 'quadratic/0744'
NAME = 'Quadratic 0744'
CATEGORY = 'Quadratic'
PROBLEM = 'Two numbers add up to 51 and multiply to 644. What are they?'
LET = 'x = one number; other = 51 − x'
EQUATION = 'x(51 − x) = 644'
SOLVE = 'x² − 51x + 644 = 0 → x = 23 (the other root, 28, gives the same pair)'
ANSWER = '23 and 28'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Two numbers add up to {0} and multiply to {1}. What are they?'
NUMBERS = ['51', '644']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
