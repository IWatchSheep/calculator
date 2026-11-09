"""Algebra word problem 0753   [Quadratic]

Problem : The product of two consecutive positive odd integers is 35. Find the integers.
Let     : x = smaller integer
Equation: x(x + 2) = 35
Solve   : x² + 2x − 35 = 0 → (x − 5)(x + 7) = 0 → x = 5
Answer  : 5 and 7

Status  : ready: consecutive_product answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0753'
KEY = 'quadratic/0753'
NAME = 'Quadratic 0753'
CATEGORY = 'Quadratic'
PROBLEM = 'The product of two consecutive positive odd integers is 35. Find the integers.'
LET = 'x = smaller integer'
EQUATION = 'x(x + 2) = 35'
SOLVE = 'x² + 2x − 35 = 0 → (x − 5)(x + 7) = 0 → x = 5'
ANSWER = '5 and 7'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'consecutive_product'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The product of two consecutive positive odd integers is {0}. Find the integers.'
NUMBERS = ['35']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
