"""Algebra word problem 0794   [Ratio]

Problem : Finn and Jade invested in a business in the ratio 4:2. They share a profit of $10,500.00 in the same ratio. How much does each get?
Let     : k = one share
Equation: 4k + 2k = 10500
Solve   : 6k = 10500 → k = 1750
Answer  : Finn $7,000.00, Jade $3,500.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0794'
KEY = 'ratio/0794'
NAME = 'Ratio 0794'
CATEGORY = 'Ratio'
PROBLEM = 'Finn and Jade invested in a business in the ratio 4:2. They share a profit of $10,500.00 in the same ratio. How much does each get?'
LET = 'k = one share'
EQUATION = '4k + 2k = 10500'
SOLVE = '6k = 10500 → k = 1750'
ANSWER = 'Finn $7,000.00, Jade $3,500.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Finn and Jade invested in a business in the ratio {0}:{1}. They share a profit of ${2} in the same ratio. How much does each get?'
NUMBERS = ['4', '2', '10500.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
