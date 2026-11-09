"""Algebra word problem 0071   [Consecutive integers]

Problem : Three consecutive integers are such that 3 times the smallest is 76 more than the largest. Find the integers.
Let     : x = smallest
Equation: 3x = (x + 2) + 76
Solve   : 2x = 78 → x = 39
Answer  : 39, 40, 41

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0071'
KEY = 'consecutive_integers/0071'
NAME = 'Consecutive integers 0071'
CATEGORY = 'Consecutive integers'
PROBLEM = 'Three consecutive integers are such that 3 times the smallest is 76 more than the largest. Find the integers.'
LET = 'x = smallest'
EQUATION = '3x = (x + 2) + 76'
SOLVE = '2x = 78 → x = 39'
ANSWER = '39, 40, 41'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Three consecutive integers are such that {0} times the smallest is {1} more than the largest. Find the integers.'
NUMBERS = ['3', '76']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
