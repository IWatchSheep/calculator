"""Algebra word problem 0580   [Number puzzle]

Problem : 9 times a number minus 9 equals 3 times the number plus 117. Find the number.
Let     : x = the number
Equation: 9x − 9 = 3x + 117
Solve   : 6x = 126 → x = 21
Answer  : 21

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0580'
KEY = 'number_puzzle/0580'
NAME = 'Number puzzle 0580'
CATEGORY = 'Number puzzle'
PROBLEM = '9 times a number minus 9 equals 3 times the number plus 117. Find the number.'
LET = 'x = the number'
EQUATION = '9x − 9 = 3x + 117'
SOLVE = '6x = 126 → x = 21'
ANSWER = '21'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} times a number minus {1} equals {2} times the number plus {3}. Find the number.'
NUMBERS = ['9', '9', '3', '117']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
