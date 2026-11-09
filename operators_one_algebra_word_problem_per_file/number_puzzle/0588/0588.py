"""Algebra word problem 0588   [Number puzzle]

Problem : 1/2 of a number plus 27 is 33. Find the number.
Let     : x = the number
Equation: (1/2)x + 27 = 33
Solve   : (1/2)x = 6 → x = 12
Answer  : 12

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0588'
KEY = 'number_puzzle/0588'
NAME = 'Number puzzle 0588'
CATEGORY = 'Number puzzle'
PROBLEM = '1/2 of a number plus 27 is 33. Find the number.'
LET = 'x = the number'
EQUATION = '(1/2)x + 27 = 33'
SOLVE = '(1/2)x = 6 → x = 12'
ANSWER = '12'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0}/{1} of a number plus {2} is {3}. Find the number.'
NUMBERS = ['1', '2', '27', '33']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
