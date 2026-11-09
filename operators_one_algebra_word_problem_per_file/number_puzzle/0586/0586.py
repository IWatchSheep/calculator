"""Algebra word problem 0586   [Number puzzle]

Problem : 9 times a number, increased by 31, is 229. Find the number.
Let     : x = the number
Equation: 9x + 31 = 229
Solve   : 9x = 198 → x = 22
Answer  : 22

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0586'
KEY = 'number_puzzle/0586'
NAME = 'Number puzzle 0586'
CATEGORY = 'Number puzzle'
PROBLEM = '9 times a number, increased by 31, is 229. Find the number.'
LET = 'x = the number'
EQUATION = '9x + 31 = 229'
SOLVE = '9x = 198 → x = 22'
ANSWER = '22'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} times a number, increased by {1}, is {2}. Find the number.'
NUMBERS = ['9', '31', '229']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
