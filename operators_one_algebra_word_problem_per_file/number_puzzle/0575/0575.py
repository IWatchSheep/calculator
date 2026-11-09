"""Algebra word problem 0575   [Number puzzle]

Problem : One-fourth of a number plus one-half of the same number is 48. Find the number.
Let     : x = the number
Equation: x/4 + x/2 = 48
Solve   : 0.75x = 48 → x = 64
Answer  : 64

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0575'
KEY = 'number_puzzle/0575'
NAME = 'Number puzzle 0575'
CATEGORY = 'Number puzzle'
PROBLEM = 'One-fourth of a number plus one-half of the same number is 48. Find the number.'
LET = 'x = the number'
EQUATION = 'x/4 + x/2 = 48'
SOLVE = '0.75x = 48 → x = 64'
ANSWER = '64'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One-fourth of a number plus one-half of the same number is {0}. Find the number.'
NUMBERS = ['48']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
