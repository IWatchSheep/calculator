"""Algebra word problem 0074   [Consecutive integers]

Problem : The sum of 4 consecutive odd integers is 160. What are the integers?
Let     : x = the smallest integer
Equation: x + (x + 2) + (x + 4) + (x + 6) = 160
Solve   : 4x + 12 = 160 → 4x = 148 → x = 37
Answer  : 37, 39, 41, 43

Status  : ready: consecutive answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0074'
KEY = 'consecutive_integers/0074'
NAME = 'Consecutive integers 0074'
CATEGORY = 'Consecutive integers'
PROBLEM = 'The sum of 4 consecutive odd integers is 160. What are the integers?'
LET = 'x = the smallest integer'
EQUATION = 'x + (x + 2) + (x + 4) + (x + 6) = 160'
SOLVE = '4x + 12 = 160 → 4x = 148 → x = 37'
ANSWER = '37, 39, 41, 43'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'consecutive'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The sum of {0} consecutive odd integers is {1}. What are the integers?'
NUMBERS = ['4', '160']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
