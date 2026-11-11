"""Algebra word problem 0686   [Profit]

Problem : A candle shop has fixed costs of $2000. Each item costs $2 to make and sells for $17. How many items must be sold to make a profit of $9775?
Let     : n = items
Equation: 17n − (2000 + 2n) = 9775
Solve   : 15n = 11775 → n = 785
Answer  : 785 items

Status  : ready: archive_profit_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0686'
KEY = 'profit/0686'
NAME = 'Profit 0686'
CATEGORY = 'Profit'
PROBLEM = 'A candle shop has fixed costs of $2000. Each item costs $2 to make and sells for $17. How many items must be sold to make a profit of $9775?'
LET = 'n = items'
EQUATION = '17n − (2000 + 2n) = 9775'
SOLVE = '15n = 11775 → n = 785'
ANSWER = '785 items'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_profit_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A candle shop has fixed costs of ${0}. Each item costs ${1} to make and sells for ${2}. How many items must be sold to make a profit of ${3}?'
NUMBERS = ['2000', '2', '17', '9775']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
