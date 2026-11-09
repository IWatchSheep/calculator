"""Algebra word problem 0570   [Number puzzle]

Problem : 6 times the difference of a number and 6 is 174. What is the number?
Let     : x = the number
Equation: 6(x − 6) = 174
Solve   : 6x = 210 → x = 35
Answer  : 35

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0570'
KEY = 'number_puzzle/0570'
NAME = 'Number puzzle 0570'
CATEGORY = 'Number puzzle'
PROBLEM = '6 times the difference of a number and 6 is 174. What is the number?'
LET = 'x = the number'
EQUATION = '6(x − 6) = 174'
SOLVE = '6x = 210 → x = 35'
ANSWER = '35'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} times the difference of a number and {1} is {2}. What is the number?'
NUMBERS = ['6', '6', '174']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
