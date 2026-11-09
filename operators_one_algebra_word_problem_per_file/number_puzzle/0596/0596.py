"""Algebra word problem 0596   [Number puzzle]

Problem : One-fourth of a number is 2 more than one-fifth of it. Find the number.
Let     : x = the number
Equation: x/4 − x/5 = 2
Solve   : x/20 = 2 → x = 2 × 20 = 40
Answer  : 40

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0596'
KEY = 'number_puzzle/0596'
NAME = 'Number puzzle 0596'
CATEGORY = 'Number puzzle'
PROBLEM = 'One-fourth of a number is 2 more than one-fifth of it. Find the number.'
LET = 'x = the number'
EQUATION = 'x/4 − x/5 = 2'
SOLVE = 'x/20 = 2 → x = 2 × 20 = 40'
ANSWER = '40'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One-fourth of a number is {0} more than one-fifth of it. Find the number.'
NUMBERS = ['2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
