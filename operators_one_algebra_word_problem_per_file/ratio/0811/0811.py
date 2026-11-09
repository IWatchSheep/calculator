"""Algebra word problem 0811   [Ratio]

Problem : Zane and Wes invested in a business in the ratio 5:2. They share a profit of $50,750.00 in the same ratio. How much does each get?
Let     : k = one share
Equation: 5k + 2k = 50750
Solve   : 7k = 50750 → k = 7250
Answer  : Zane $36,250.00, Wes $14,500.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0811'
KEY = 'ratio/0811'
NAME = 'Ratio 0811'
CATEGORY = 'Ratio'
PROBLEM = 'Zane and Wes invested in a business in the ratio 5:2. They share a profit of $50,750.00 in the same ratio. How much does each get?'
LET = 'k = one share'
EQUATION = '5k + 2k = 50750'
SOLVE = '7k = 50750 → k = 7250'
ANSWER = 'Zane $36,250.00, Wes $14,500.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Zane and Wes invested in a business in the ratio {0}:{1}. They share a profit of ${2} in the same ratio. How much does each get?'
NUMBERS = ['5', '2', '50750.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
