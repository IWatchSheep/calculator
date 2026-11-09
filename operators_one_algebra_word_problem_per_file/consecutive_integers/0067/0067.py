"""Algebra word problem 0067   [Consecutive integers]

Problem : Of three consecutive even integers, the sum of the smallest and largest is 8. Find all three.
Let     : x = smallest
Equation: x + (x + 4) = 8
Solve   : 2x = 4 → x = 2
Answer  : 2, 4, 6

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0067'
KEY = 'consecutive_integers/0067'
NAME = 'Consecutive integers 0067'
CATEGORY = 'Consecutive integers'
PROBLEM = 'Of three consecutive even integers, the sum of the smallest and largest is 8. Find all three.'
LET = 'x = smallest'
EQUATION = 'x + (x + 4) = 8'
SOLVE = '2x = 4 → x = 2'
ANSWER = '2, 4, 6'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Of three consecutive even integers, the sum of the smallest and largest is {0}. Find all three.'
NUMBERS = ['8']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
