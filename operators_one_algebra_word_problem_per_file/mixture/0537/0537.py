"""Algebra word problem 0537   [Mixture]

Problem : 50 lb of a blend of coffee beans selling for $13.60/lb is made from coffee beans costing $8/lb and $15/lb. How many pounds of each are used?
Let     : x = lb at $8; 50 − x = lb at $15
Equation: 8x + 15(50 − x) = 680
Solve   : 7x = 70 → x = 10
Answer  : 10 lb at $8 and 40 lb at $15

Status  : ready: price_blend answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0537'
KEY = 'mixture/0537'
NAME = 'Mixture 0537'
CATEGORY = 'Mixture'
PROBLEM = '50 lb of a blend of coffee beans selling for $13.60/lb is made from coffee beans costing $8/lb and $15/lb. How many pounds of each are used?'
LET = 'x = lb at $8; 50 − x = lb at $15'
EQUATION = '8x + 15(50 − x) = 680'
SOLVE = '7x = 70 → x = 10'
ANSWER = '10 lb at $8 and 40 lb at $15'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'price_blend'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} lb of a blend of coffee beans selling for ${1}/lb is made from coffee beans costing ${2}/lb and ${3}/lb. How many pounds of each are used?'
NUMBERS = ['50', '13.60', '8', '15']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
