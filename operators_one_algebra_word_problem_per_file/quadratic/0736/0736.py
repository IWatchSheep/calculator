"""Algebra word problem 0736   [Quadratic]

Problem : The sum of two numbers is 43 and their product is 456. Find the numbers.
Let     : x = one number; other = 43 − x
Equation: x(43 − x) = 456
Solve   : x² − 43x + 456 = 0 → x = 19 (the other root, 24, gives the same pair)
Answer  : 19 and 24

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0736'
KEY = 'quadratic/0736'
NAME = 'Quadratic 0736'
CATEGORY = 'Quadratic'
PROBLEM = 'The sum of two numbers is 43 and their product is 456. Find the numbers.'
LET = 'x = one number; other = 43 − x'
EQUATION = 'x(43 − x) = 456'
SOLVE = 'x² − 43x + 456 = 0 → x = 19 (the other root, 24, gives the same pair)'
ANSWER = '19 and 24'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The sum of two numbers is {0} and their product is {1}. Find the numbers.'
NUMBERS = ['43', '456']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
