"""Algebra word problem 0589   [Number puzzle]

Problem : A number divided by 5, then increased by 9, gives 13. Find the number.
Let     : x = the number
Equation: x/5 + 9 = 13
Solve   : x/5 = 4 → x = 4 × 5 = 20
Answer  : 20

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0589'
KEY = 'number_puzzle/0589'
NAME = 'Number puzzle 0589'
CATEGORY = 'Number puzzle'
PROBLEM = 'A number divided by 5, then increased by 9, gives 13. Find the number.'
LET = 'x = the number'
EQUATION = 'x/5 + 9 = 13'
SOLVE = 'x/5 = 4 → x = 4 × 5 = 20'
ANSWER = '20'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A number divided by {0}, then increased by {1}, gives {2}. Find the number.'
NUMBERS = ['5', '9', '13']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
