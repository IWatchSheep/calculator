"""Algebra word problem 0100   [Digits]

Problem : In a two-digit number, the units digit is 9 times the tens digit. The number is 9 more than the sum of its digits. Find the number.
Let     : t = tens digit; units digit = 9t
Equation: (10t + 9t) − (t + 9t) = 9
Solve   : 9t = 9 → t = 1
Answer  : 19

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0100'
KEY = 'digits/0100'
NAME = 'Digits 0100'
CATEGORY = 'Digits'
PROBLEM = 'In a two-digit number, the units digit is 9 times the tens digit. The number is 9 more than the sum of its digits. Find the number.'
LET = 't = tens digit; units digit = 9t'
EQUATION = '(10t + 9t) − (t + 9t) = 9'
SOLVE = '9t = 9 → t = 1'
ANSWER = '19'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'In a two-digit number, the units digit is {0} times the tens digit. The number is {1} more than the sum of its digits. Find the number.'
NUMBERS = ['9', '9']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
