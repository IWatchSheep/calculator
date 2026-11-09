"""Algebra word problem 0425   [Linear cost]

Problem : Notebooks cost $3.50 each. With a $3 coupon, Hiro paid $46.00. How many notebooks were bought?
Let     : n = items
Equation: 3.5n − 3 = 46
Solve   : 3.5n = 49 → n = 14
Answer  : 14 notebooks

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0425'
KEY = 'linear_cost/0425'
NAME = 'Linear cost 0425'
CATEGORY = 'Linear cost'
PROBLEM = 'Notebooks cost $3.50 each. With a $3 coupon, Hiro paid $46.00. How many notebooks were bought?'
LET = 'n = items'
EQUATION = '3.5n − 3 = 46'
SOLVE = '3.5n = 49 → n = 14'
ANSWER = '14 notebooks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Notebooks cost ${0} each. With a ${1} coupon, Hiro paid ${2}. How many notebooks were bought?'
NUMBERS = ['3.50', '3', '46.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
