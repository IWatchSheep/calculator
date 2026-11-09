"""Algebra word problem 0006   [Age]

Problem : Hiro is 2 years older than Maya. The sum of their ages is 24. How old is each?
Let     : x = Maya's age
Equation: x + (x + 2) = 24
Solve   : 2x = 22 → x = 11
Answer  : Maya is 11, Hiro is 13

Status  : ready: sum_difference answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0006'
KEY = 'age/0006'
NAME = 'Age 0006'
CATEGORY = 'Age'
PROBLEM = 'Hiro is 2 years older than Maya. The sum of their ages is 24. How old is each?'
LET = "x = Maya's age"
EQUATION = 'x + (x + 2) = 24'
SOLVE = '2x = 22 → x = 11'
ANSWER = 'Maya is 11, Hiro is 13'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'sum_difference'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Hiro is {0} years older than Maya. The sum of their ages is {1}. How old is each?'
NUMBERS = ['2', '24']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
