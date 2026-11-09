"""Algebra word problem 0609   [Number puzzle]

Problem : 4/5 of a number plus 20 is 44. Find the number.
Let     : x = the number
Equation: (4/5)x + 20 = 44
Solve   : (4/5)x = 24 → x = 30
Answer  : 30

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0609'
KEY = 'number_puzzle/0609'
NAME = 'Number puzzle 0609'
CATEGORY = 'Number puzzle'
PROBLEM = '4/5 of a number plus 20 is 44. Find the number.'
LET = 'x = the number'
EQUATION = '(4/5)x + 20 = 44'
SOLVE = '(4/5)x = 24 → x = 30'
ANSWER = '30'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0}/{1} of a number plus {2} is {3}. Find the number.'
NUMBERS = ['4', '5', '20', '44']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
