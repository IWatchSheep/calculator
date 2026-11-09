"""Algebra word problem 0916   [System of equations]

Problem : The sum of two numbers is 66 and their difference is 20. Find the numbers.
Let     : x = larger, y = smaller
Equation: x + y = 66;  x − y = 20
Solve   : 2x = 86 → x = 43, y = 23
Answer  : 43 and 23

Status  : ready: sum_difference answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0916'
KEY = 'system_of_equations/0916'
NAME = 'System of equations 0916'
CATEGORY = 'System of equations'
PROBLEM = 'The sum of two numbers is 66 and their difference is 20. Find the numbers.'
LET = 'x = larger, y = smaller'
EQUATION = 'x + y = 66;  x − y = 20'
SOLVE = '2x = 86 → x = 43, y = 23'
ANSWER = '43 and 23'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'sum_difference'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'The sum of two numbers is {0} and their difference is {1}. Find the numbers.'
NUMBERS = ['66', '20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
