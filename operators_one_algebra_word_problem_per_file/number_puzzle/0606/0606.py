"""Algebra word problem 0606   [Number puzzle]

Problem : 7 times a number minus 16 equals 2 times the number plus 34. Find the number.
Let     : x = the number
Equation: 7x − 16 = 2x + 34
Solve   : 5x = 50 → x = 10
Answer  : 10

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0606'
KEY = 'number_puzzle/0606'
NAME = 'Number puzzle 0606'
CATEGORY = 'Number puzzle'
PROBLEM = '7 times a number minus 16 equals 2 times the number plus 34. Find the number.'
LET = 'x = the number'
EQUATION = '7x − 16 = 2x + 34'
SOLVE = '5x = 50 → x = 10'
ANSWER = '10'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} times a number minus {1} equals {2} times the number plus {3}. Find the number.'
NUMBERS = ['7', '16', '2', '34']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
