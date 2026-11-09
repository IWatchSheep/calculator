"""Algebra word problem 0573   [Number puzzle]

Problem : If you divide a number by 7 and add 1, you get -3. What was the number?
Let     : x = the number
Equation: x/7 + 1 = -3
Solve   : x/7 = -4 → x = -4 × 7 = -28
Answer  : -28

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0573'
KEY = 'number_puzzle/0573'
NAME = 'Number puzzle 0573'
CATEGORY = 'Number puzzle'
PROBLEM = 'If you divide a number by 7 and add 1, you get -3. What was the number?'
LET = 'x = the number'
EQUATION = 'x/7 + 1 = -3'
SOLVE = 'x/7 = -4 → x = -4 × 7 = -28'
ANSWER = '-28'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'If you divide a number by {0} and add {1}, you get -{2}. What was the number?'
NUMBERS = ['7', '1', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
