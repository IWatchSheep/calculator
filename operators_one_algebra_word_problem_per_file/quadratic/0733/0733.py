"""Algebra word problem 0733   [Quadratic]

Problem : The product of two consecutive positive integers is 12. Find the integers.
Let     : x = smaller integer
Equation: x(x + 1) = 12
Solve   : x² + x − 12 = 0 → (x − 3)(x + 4) = 0 → x = 3
Answer  : 3 and 4

Status  : ready: consecutive_product answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0733'
KEY = 'quadratic/0733'
NAME = 'Quadratic 0733'
CATEGORY = 'Quadratic'
PROBLEM = 'The product of two consecutive positive integers is 12. Find the integers.'
LET = 'x = smaller integer'
EQUATION = 'x(x + 1) = 12'
SOLVE = 'x² + x − 12 = 0 → (x − 3)(x + 4) = 0 → x = 3'
ANSWER = '3 and 4'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'consecutive_product'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The product of two consecutive positive integers is {0}. Find the integers.'
NUMBERS = ['12']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
