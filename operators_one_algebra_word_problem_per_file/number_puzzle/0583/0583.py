"""Algebra word problem 0583   [Number puzzle]

Problem : The second of three numbers is 2 times the first. The third is 16 more than the second. Their sum is 101. Find the numbers.
Let     : x = first number
Equation: x + 2x + (2x + 16) = 101
Solve   : 5x = 85 → x = 17
Answer  : 17, 34, 50

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0583'
KEY = 'number_puzzle/0583'
NAME = 'Number puzzle 0583'
CATEGORY = 'Number puzzle'
PROBLEM = 'The second of three numbers is 2 times the first. The third is 16 more than the second. Their sum is 101. Find the numbers.'
LET = 'x = first number'
EQUATION = 'x + 2x + (2x + 16) = 101'
SOLVE = '5x = 85 → x = 17'
ANSWER = '17, 34, 50'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The second of three numbers is {0} times the first. The third is {1} more than the second. Their sum is {2}. Find the numbers.'
NUMBERS = ['2', '16', '101']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
