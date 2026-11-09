"""Algebra word problem 0545   [Mixture]

Problem : 40 lb of a blend of candy selling for $13.60/lb is made from candy costing $8/lb and $24/lb. How many pounds of each are used?
Let     : x = lb at $8; 40 − x = lb at $24
Equation: 8x + 24(40 − x) = 544
Solve   : 16x = 416 → x = 26
Answer  : 26 lb at $8 and 14 lb at $24

Status  : ready: price_blend answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0545'
KEY = 'mixture/0545'
NAME = 'Mixture 0545'
CATEGORY = 'Mixture'
PROBLEM = '40 lb of a blend of candy selling for $13.60/lb is made from candy costing $8/lb and $24/lb. How many pounds of each are used?'
LET = 'x = lb at $8; 40 − x = lb at $24'
EQUATION = '8x + 24(40 − x) = 544'
SOLVE = '16x = 416 → x = 26'
ANSWER = '26 lb at $8 and 14 lb at $24'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'price_blend'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} lb of a blend of candy selling for ${1}/lb is made from candy costing ${2}/lb and ${3}/lb. How many pounds of each are used?'
NUMBERS = ['40', '13.60', '8', '24']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
