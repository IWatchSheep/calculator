"""Algebra word problem 0574   [Number puzzle]

Problem : Five times a number, decreased by 19, is 106. Find the number.
Let     : x = the number
Equation: 5x − 19 = 106
Solve   : 5x = 125 → x = 25
Answer  : 25

Status  : ready: number_puzzle answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0574'
KEY = 'number_puzzle/0574'
NAME = 'Number puzzle 0574'
CATEGORY = 'Number puzzle'
PROBLEM = 'Five times a number, decreased by 19, is 106. Find the number.'
LET = 'x = the number'
EQUATION = '5x − 19 = 106'
SOLVE = '5x = 125 → x = 25'
ANSWER = '25'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'number_puzzle'
FAMILY = 'number_puzzle'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Five times a number, decreased by {0}, is {1}. Find the number.'
NUMBERS = ['19', '106']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
