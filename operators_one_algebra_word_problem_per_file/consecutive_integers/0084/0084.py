"""Algebra word problem 0084   [Consecutive integers]

Problem : The sum of 4 consecutive even integers is 244. What are the integers?
Let     : x = the smallest integer
Equation: x + (x + 2) + (x + 4) + (x + 6) = 244
Solve   : 4x + 12 = 244 → 4x = 232 → x = 58
Answer  : 58, 60, 62, 64

Status  : ready: consecutive answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0084'
KEY = 'consecutive_integers/0084'
NAME = 'Consecutive integers 0084'
CATEGORY = 'Consecutive integers'
PROBLEM = 'The sum of 4 consecutive even integers is 244. What are the integers?'
LET = 'x = the smallest integer'
EQUATION = 'x + (x + 2) + (x + 4) + (x + 6) = 244'
SOLVE = '4x + 12 = 244 → 4x = 232 → x = 58'
ANSWER = '58, 60, 62, 64'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'consecutive'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The sum of {0} consecutive even integers is {1}. What are the integers?'
NUMBERS = ['4', '244']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
