"""Algebra word problem 0687   [Profit]

Problem : A candle shop has fixed costs of $750. Each item costs $12 to make and sells for $27. How many items must be sold to make a profit of $1350?
Let     : n = items
Equation: 27n − (750 + 12n) = 1350
Solve   : 15n = 2100 → n = 140
Answer  : 140 items

Status  : ready: archive_profit_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0687'
KEY = 'profit/0687'
NAME = 'Profit 0687'
CATEGORY = 'Profit'
PROBLEM = 'A candle shop has fixed costs of $750. Each item costs $12 to make and sells for $27. How many items must be sold to make a profit of $1350?'
LET = 'n = items'
EQUATION = '27n − (750 + 12n) = 1350'
SOLVE = '15n = 2100 → n = 140'
ANSWER = '140 items'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_profit_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A candle shop has fixed costs of ${0}. Each item costs ${1} to make and sells for ${2}. How many items must be sold to make a profit of ${3}?'
NUMBERS = ['750', '12', '27', '1350']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
