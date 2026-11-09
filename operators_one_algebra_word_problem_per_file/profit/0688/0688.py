"""Algebra word problem 0688   [Profit]

Problem : A candle shop has fixed costs of $1650. Each item costs $5 to make and sells for $15. How many items must be sold to make a profit of $4890?
Let     : n = items
Equation: 15n − (1650 + 5n) = 4890
Solve   : 10n = 6540 → n = 654
Answer  : 654 items

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0688'
KEY = 'profit/0688'
NAME = 'Profit 0688'
CATEGORY = 'Profit'
PROBLEM = 'A candle shop has fixed costs of $1650. Each item costs $5 to make and sells for $15. How many items must be sold to make a profit of $4890?'
LET = 'n = items'
EQUATION = '15n − (1650 + 5n) = 4890'
SOLVE = '10n = 6540 → n = 654'
ANSWER = '654 items'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A candle shop has fixed costs of ${0}. Each item costs ${1} to make and sells for ${2}. How many items must be sold to make a profit of ${3}?'
NUMBERS = ['1650', '5', '15', '4890']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
