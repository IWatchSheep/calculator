"""Algebra word problem 0569   [Mixture]

Problem : 20 lb of a blend of coffee beans selling for $12.00/lb is made from coffee beans costing $6/lb and $18/lb. How many pounds of each are used?
Let     : x = lb at $6; 20 − x = lb at $18
Equation: 6x + 18(20 − x) = 240
Solve   : 12x = 120 → x = 10
Answer  : 10 lb at $6 and 10 lb at $18

Status  : ready: price_blend answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0569'
KEY = 'mixture/0569'
NAME = 'Mixture 0569'
CATEGORY = 'Mixture'
PROBLEM = '20 lb of a blend of coffee beans selling for $12.00/lb is made from coffee beans costing $6/lb and $18/lb. How many pounds of each are used?'
LET = 'x = lb at $6; 20 − x = lb at $18'
EQUATION = '6x + 18(20 − x) = 240'
SOLVE = '12x = 120 → x = 10'
ANSWER = '10 lb at $6 and 10 lb at $18'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'price_blend'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} lb of a blend of coffee beans selling for ${1}/lb is made from coffee beans costing ${2}/lb and ${3}/lb. How many pounds of each are used?'
NUMBERS = ['20', '12.00', '6', '18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
