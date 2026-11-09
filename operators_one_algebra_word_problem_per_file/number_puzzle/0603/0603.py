"""Algebra word problem 0603   [Number puzzle]

Problem : If you divide a number by 5 and add 10, you get 26. What was the number?
Let     : x = the number
Equation: x/5 + 10 = 26
Solve   : x/5 = 16 → x = 16 × 5 = 80
Answer  : 80

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0603'
KEY = 'number_puzzle/0603'
NAME = 'Number puzzle 0603'
CATEGORY = 'Number puzzle'
PROBLEM = 'If you divide a number by 5 and add 10, you get 26. What was the number?'
LET = 'x = the number'
EQUATION = 'x/5 + 10 = 26'
SOLVE = 'x/5 = 16 → x = 16 × 5 = 80'
ANSWER = '80'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'If you divide a number by {0} and add {1}, you get {2}. What was the number?'
NUMBERS = ['5', '10', '26']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
