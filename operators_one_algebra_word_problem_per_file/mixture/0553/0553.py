"""Algebra word problem 0553   [Mixture]

Problem : 20 lb of a blend of candy selling for $15.90/lb is made from candy costing $4/lb and $18/lb. How many pounds of each are used?
Let     : x = lb at $4; 20 − x = lb at $18
Equation: 4x + 18(20 − x) = 318
Solve   : 14x = 42 → x = 3
Answer  : 3 lb at $4 and 17 lb at $18

Status  : ready: price_blend answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0553'
KEY = 'mixture/0553'
NAME = 'Mixture 0553'
CATEGORY = 'Mixture'
PROBLEM = '20 lb of a blend of candy selling for $15.90/lb is made from candy costing $4/lb and $18/lb. How many pounds of each are used?'
LET = 'x = lb at $4; 20 − x = lb at $18'
EQUATION = '4x + 18(20 − x) = 318'
SOLVE = '14x = 42 → x = 3'
ANSWER = '3 lb at $4 and 17 lb at $18'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'price_blend'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} lb of a blend of candy selling for ${1}/lb is made from candy costing ${2}/lb and ${3}/lb. How many pounds of each are used?'
NUMBERS = ['20', '15.90', '4', '18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
