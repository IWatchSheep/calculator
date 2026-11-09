"""Algebra word problem 0892   [System of equations]

Problem : The sum of two numbers is 126 and their difference is 100. Find the numbers.
Let     : x = larger, y = smaller
Equation: x + y = 126;  x − y = 100
Solve   : 2x = 226 → x = 113, y = 13
Answer  : 113 and 13

Status  : ready: sum_difference answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0892'
KEY = 'system_of_equations/0892'
NAME = 'System of equations 0892'
CATEGORY = 'System of equations'
PROBLEM = 'The sum of two numbers is 126 and their difference is 100. Find the numbers.'
LET = 'x = larger, y = smaller'
EQUATION = 'x + y = 126;  x − y = 100'
SOLVE = '2x = 226 → x = 113, y = 13'
ANSWER = '113 and 13'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'sum_difference'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The sum of two numbers is {0} and their difference is {1}. Find the numbers.'
NUMBERS = ['126', '100']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
