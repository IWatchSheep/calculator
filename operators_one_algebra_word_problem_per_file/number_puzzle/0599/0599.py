"""Algebra word problem 0599   [Number puzzle]

Problem : 2 times the difference of a number and 9 is 48. What is the number?
Let     : x = the number
Equation: 2(x − 9) = 48
Solve   : 2x = 66 → x = 33
Answer  : 33

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0599'
KEY = 'number_puzzle/0599'
NAME = 'Number puzzle 0599'
CATEGORY = 'Number puzzle'
PROBLEM = '2 times the difference of a number and 9 is 48. What is the number?'
LET = 'x = the number'
EQUATION = '2(x − 9) = 48'
SOLVE = '2x = 66 → x = 33'
ANSWER = '33'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} times the difference of a number and {1} is {2}. What is the number?'
NUMBERS = ['2', '9', '48']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
