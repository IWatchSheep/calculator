"""Algebra word problem 0080   [Consecutive integers]

Problem : Three consecutive integers are such that 5 times the smallest is 2 more than the largest. Find the integers.
Let     : x = smallest
Equation: 5x = (x + 2) + 2
Solve   : 4x = 4 → x = 1
Answer  : 1, 2, 3

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0080'
KEY = 'consecutive_integers/0080'
NAME = 'Consecutive integers 0080'
CATEGORY = 'Consecutive integers'
PROBLEM = 'Three consecutive integers are such that 5 times the smallest is 2 more than the largest. Find the integers.'
LET = 'x = smallest'
EQUATION = '5x = (x + 2) + 2'
SOLVE = '4x = 4 → x = 1'
ANSWER = '1, 2, 3'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Three consecutive integers are such that {0} times the smallest is {1} more than the largest. Find the integers.'
NUMBERS = ['5', '2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
