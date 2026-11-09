"""Algebra word problem 0805   [Ratio]

Problem : Aiden and Quinn invested in a business in the ratio 1:3. They share a profit of $10,000.00 in the same ratio. How much does each get?
Let     : k = one share
Equation: k + 3k = 10000
Solve   : 4k = 10000 → k = 2500
Answer  : Aiden $2,500.00, Quinn $7,500.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0805'
KEY = 'ratio/0805'
NAME = 'Ratio 0805'
CATEGORY = 'Ratio'
PROBLEM = 'Aiden and Quinn invested in a business in the ratio 1:3. They share a profit of $10,000.00 in the same ratio. How much does each get?'
LET = 'k = one share'
EQUATION = 'k + 3k = 10000'
SOLVE = '4k = 10000 → k = 2500'
ANSWER = 'Aiden $2,500.00, Quinn $7,500.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Aiden and Quinn invested in a business in the ratio {0}:{1}. They share a profit of ${2} in the same ratio. How much does each get?'
NUMBERS = ['1', '3', '10000.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
