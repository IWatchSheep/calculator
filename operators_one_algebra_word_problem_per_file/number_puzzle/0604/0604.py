"""Algebra word problem 0604   [Number puzzle]

Problem : Four times a number, increased by 1, is 117. Find the number.
Let     : x = the number
Equation: 4x + 1 = 117
Solve   : 4x = 116 → x = 29
Answer  : 29

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0604'
KEY = 'number_puzzle/0604'
NAME = 'Number puzzle 0604'
CATEGORY = 'Number puzzle'
PROBLEM = 'Four times a number, increased by 1, is 117. Find the number.'
LET = 'x = the number'
EQUATION = '4x + 1 = 117'
SOLVE = '4x = 116 → x = 29'
ANSWER = '29'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Four times a number, increased by {0}, is {1}. Find the number.'
NUMBERS = ['1', '117']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
