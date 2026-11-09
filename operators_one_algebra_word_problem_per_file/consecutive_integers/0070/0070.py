"""Algebra word problem 0070   [Consecutive integers]

Problem : The sum of 3 consecutive integers is 120. What are the integers?
Let     : x = the smallest integer
Equation: x + (x + 1) + (x + 2) = 120
Solve   : 3x + 3 = 120 → 3x = 117 → x = 39
Answer  : 39, 40, 41

Status  : ready: consecutive answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0070'
KEY = 'consecutive_integers/0070'
NAME = 'Consecutive integers 0070'
CATEGORY = 'Consecutive integers'
PROBLEM = 'The sum of 3 consecutive integers is 120. What are the integers?'
LET = 'x = the smallest integer'
EQUATION = 'x + (x + 1) + (x + 2) = 120'
SOLVE = '3x + 3 = 120 → 3x = 117 → x = 39'
ANSWER = '39, 40, 41'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'consecutive'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The sum of {0} consecutive integers is {1}. What are the integers?'
NUMBERS = ['3', '120']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
