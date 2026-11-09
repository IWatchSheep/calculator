"""Algebra word problem 0562   [Mixture]

Problem : 50 lb of a blend of nuts selling for $10.20/lb is made from nuts costing $10/lb and $20/lb. How many pounds of each are used?
Let     : x = lb at $10; 50 − x = lb at $20
Equation: 10x + 20(50 − x) = 510
Solve   : 10x = 490 → x = 49
Answer  : 49 lb at $10 and 1 lb at $20

Status  : ready: price_blend answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0562'
KEY = 'mixture/0562'
NAME = 'Mixture 0562'
CATEGORY = 'Mixture'
PROBLEM = '50 lb of a blend of nuts selling for $10.20/lb is made from nuts costing $10/lb and $20/lb. How many pounds of each are used?'
LET = 'x = lb at $10; 50 − x = lb at $20'
EQUATION = '10x + 20(50 − x) = 510'
SOLVE = '10x = 490 → x = 49'
ANSWER = '49 lb at $10 and 1 lb at $20'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'price_blend'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} lb of a blend of nuts selling for ${1}/lb is made from nuts costing ${2}/lb and ${3}/lb. How many pounds of each are used?'
NUMBERS = ['50', '10.20', '10', '20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
