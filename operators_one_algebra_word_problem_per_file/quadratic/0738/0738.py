"""Algebra word problem 0738   [Quadratic]

Problem : The product of two consecutive positive integers is 210. Find the integers.
Let     : x = smaller integer
Equation: x(x + 1) = 210
Solve   : x² + x − 210 = 0 → (x − 14)(x + 15) = 0 → x = 14
Answer  : 14 and 15

Status  : ready: consecutive_product answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0738'
KEY = 'quadratic/0738'
NAME = 'Quadratic 0738'
CATEGORY = 'Quadratic'
PROBLEM = 'The product of two consecutive positive integers is 210. Find the integers.'
LET = 'x = smaller integer'
EQUATION = 'x(x + 1) = 210'
SOLVE = 'x² + x − 210 = 0 → (x − 14)(x + 15) = 0 → x = 14'
ANSWER = '14 and 15'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'consecutive_product'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The product of two consecutive positive integers is {0}. Find the integers.'
NUMBERS = ['210']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
