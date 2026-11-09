"""Algebra word problem 0582   [Number puzzle]

Problem : A number divided by 9, then increased by 9, gives 10. Find the number.
Let     : x = the number
Equation: x/9 + 9 = 10
Solve   : x/9 = 1 → x = 1 × 9 = 9
Answer  : 9

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0582'
KEY = 'number_puzzle/0582'
NAME = 'Number puzzle 0582'
CATEGORY = 'Number puzzle'
PROBLEM = 'A number divided by 9, then increased by 9, gives 10. Find the number.'
LET = 'x = the number'
EQUATION = 'x/9 + 9 = 10'
SOLVE = 'x/9 = 1 → x = 1 × 9 = 9'
ANSWER = '9'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A number divided by {0}, then increased by {1}, gives {2}. Find the number.'
NUMBERS = ['9', '9', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
