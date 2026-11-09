"""Algebra word problem 0601   [Number puzzle]

Problem : 6 times a number minus 11 equals 2 times the number plus 41. Find the number.
Let     : x = the number
Equation: 6x − 11 = 2x + 41
Solve   : 4x = 52 → x = 13
Answer  : 13

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0601'
KEY = 'number_puzzle/0601'
NAME = 'Number puzzle 0601'
CATEGORY = 'Number puzzle'
PROBLEM = '6 times a number minus 11 equals 2 times the number plus 41. Find the number.'
LET = 'x = the number'
EQUATION = '6x − 11 = 2x + 41'
SOLVE = '4x = 52 → x = 13'
ANSWER = '13'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} times a number minus {1} equals {2} times the number plus {3}. Find the number.'
NUMBERS = ['6', '11', '2', '41']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
