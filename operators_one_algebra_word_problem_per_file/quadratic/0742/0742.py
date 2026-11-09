"""Algebra word problem 0742   [Quadratic]

Problem : The sum of the squares of two consecutive positive integers is 1625. Find the integers.
Let     : x = smaller integer
Equation: x² + (x + 1)² = 1625
Solve   : x² + x − 812 = 0 → x = 28 (the other root, -29, is rejected)
Answer  : 28 and 29

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0742'
KEY = 'quadratic/0742'
NAME = 'Quadratic 0742'
CATEGORY = 'Quadratic'
PROBLEM = 'The sum of the squares of two consecutive positive integers is 1625. Find the integers.'
LET = 'x = smaller integer'
EQUATION = 'x² + (x + 1)² = 1625'
SOLVE = 'x² + x − 812 = 0 → x = 28 (the other root, -29, is rejected)'
ANSWER = '28 and 29'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The sum of the squares of two consecutive positive integers is {0}. Find the integers.'
NUMBERS = ['1625']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
