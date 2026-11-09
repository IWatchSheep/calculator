"""Algebra word problem 0581   [Number puzzle]

Problem : One-third of a number is 4 more than one-fifth of it. Find the number.
Let     : x = the number
Equation: x/3 − x/5 = 4
Solve   : (2/15)x = 4 → x = 30
Answer  : 30

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0581'
KEY = 'number_puzzle/0581'
NAME = 'Number puzzle 0581'
CATEGORY = 'Number puzzle'
PROBLEM = 'One-third of a number is 4 more than one-fifth of it. Find the number.'
LET = 'x = the number'
EQUATION = 'x/3 − x/5 = 4'
SOLVE = '(2/15)x = 4 → x = 30'
ANSWER = '30'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One-third of a number is {0} more than one-fifth of it. Find the number.'
NUMBERS = ['4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
