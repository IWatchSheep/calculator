"""Algebra word problem 0747   [Quadratic]

Problem : The product of two consecutive positive even integers is 168. Find the integers.
Let     : x = smaller integer
Equation: x(x + 2) = 168
Solve   : x² + 2x − 168 = 0 → (x − 12)(x + 14) = 0 → x = 12
Answer  : 12 and 14

Status  : ready: consecutive_product answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0747'
KEY = 'quadratic/0747'
NAME = 'Quadratic 0747'
CATEGORY = 'Quadratic'
PROBLEM = 'The product of two consecutive positive even integers is 168. Find the integers.'
LET = 'x = smaller integer'
EQUATION = 'x(x + 2) = 168'
SOLVE = 'x² + 2x − 168 = 0 → (x − 12)(x + 14) = 0 → x = 12'
ANSWER = '12 and 14'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'consecutive_product'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The product of two consecutive positive even integers is {0}. Find the integers.'
NUMBERS = ['168']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
