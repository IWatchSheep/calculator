"""Algebra word problem 0081   [Consecutive integers]

Problem : The sum of 3 consecutive odd integers is 33. What are the integers?
Let     : x = the smallest integer
Equation: x + (x + 2) + (x + 4) = 33
Solve   : 3x + 6 = 33 → 3x = 27 → x = 9
Answer  : 9, 11, 13

Status  : ready: consecutive answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0081'
KEY = 'consecutive_integers/0081'
NAME = 'Consecutive integers 0081'
CATEGORY = 'Consecutive integers'
PROBLEM = 'The sum of 3 consecutive odd integers is 33. What are the integers?'
LET = 'x = the smallest integer'
EQUATION = 'x + (x + 2) + (x + 4) = 33'
SOLVE = '3x + 6 = 33 → 3x = 27 → x = 9'
ANSWER = '9, 11, 13'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'consecutive'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The sum of {0} consecutive odd integers is {1}. What are the integers?'
NUMBERS = ['3', '33']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
