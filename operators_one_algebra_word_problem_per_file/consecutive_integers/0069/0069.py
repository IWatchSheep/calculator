"""Algebra word problem 0069   [Consecutive integers]

Problem : Three consecutive integers are such that 3 times the smallest is 4 more than the largest. Find the integers.
Let     : x = smallest
Equation: 3x = (x + 2) + 4
Solve   : 2x = 6 → x = 3
Answer  : 3, 4, 5

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0069'
KEY = 'consecutive_integers/0069'
NAME = 'Consecutive integers 0069'
CATEGORY = 'Consecutive integers'
PROBLEM = 'Three consecutive integers are such that 3 times the smallest is 4 more than the largest. Find the integers.'
LET = 'x = smallest'
EQUATION = '3x = (x + 2) + 4'
SOLVE = '2x = 6 → x = 3'
ANSWER = '3, 4, 5'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Three consecutive integers are such that {0} times the smallest is {1} more than the largest. Find the integers.'
NUMBERS = ['3', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
