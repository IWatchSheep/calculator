"""Algebra word problem 0792   [Ratio]

Problem : Caleb and Quinn invested in a business in the ratio 6:4. They share a profit of $82,500.00 in the same ratio. How much does each get?
Let     : k = one share
Equation: 6k + 4k = 82500
Solve   : 10k = 82500 → k = 8250
Answer  : Caleb $49,500.00, Quinn $33,000.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0792'
KEY = 'ratio/0792'
NAME = 'Ratio 0792'
CATEGORY = 'Ratio'
PROBLEM = 'Caleb and Quinn invested in a business in the ratio 6:4. They share a profit of $82,500.00 in the same ratio. How much does each get?'
LET = 'k = one share'
EQUATION = '6k + 4k = 82500'
SOLVE = '10k = 82500 → k = 8250'
ANSWER = 'Caleb $49,500.00, Quinn $33,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Caleb and Quinn invested in a business in the ratio {0}:{1}. They share a profit of ${2} in the same ratio. How much does each get?'
NUMBERS = ['6', '4', '82500.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
