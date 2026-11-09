"""Algebra word problem 0584   [Number puzzle]

Problem : When 4 is subtracted from a number and the result is multiplied by 5, the answer is 60. Find the number.
Let     : x = the number
Equation: 5(x − 4) = 60
Solve   : 5x = 80 → x = 16
Answer  : 16

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0584'
KEY = 'number_puzzle/0584'
NAME = 'Number puzzle 0584'
CATEGORY = 'Number puzzle'
PROBLEM = 'When 4 is subtracted from a number and the result is multiplied by 5, the answer is 60. Find the number.'
LET = 'x = the number'
EQUATION = '5(x − 4) = 60'
SOLVE = '5x = 80 → x = 16'
ANSWER = '16'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'When {0} is subtracted from a number and the result is multiplied by {1}, the answer is {2}. Find the number.'
NUMBERS = ['4', '5', '60']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
