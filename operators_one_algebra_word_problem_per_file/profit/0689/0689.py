"""Algebra word problem 0689   [Profit]

Problem : A T-shirt business has fixed costs of $100. Each item costs $2 to make and sells for $8. How many items must be sold to make a profit of $452?
Let     : n = items
Equation: 8n − (100 + 2n) = 452
Solve   : 6n = 552 → n = 92
Answer  : 92 items

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0689'
KEY = 'profit/0689'
NAME = 'Profit 0689'
CATEGORY = 'Profit'
PROBLEM = 'A T-shirt business has fixed costs of $100. Each item costs $2 to make and sells for $8. How many items must be sold to make a profit of $452?'
LET = 'n = items'
EQUATION = '8n − (100 + 2n) = 452'
SOLVE = '6n = 552 → n = 92'
ANSWER = '92 items'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A T-shirt business has fixed costs of ${0}. Each item costs ${1} to make and sells for ${2}. How many items must be sold to make a profit of ${3}?'
NUMBERS = ['100', '2', '8', '452']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
