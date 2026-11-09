"""Algebra word problem 0459   [Linear cost]

Problem : Notebooks cost $3.50 each. With a $2 coupon, Dev paid $33.00. How many notebooks were bought?
Let     : n = items
Equation: 3.5n − 2 = 33
Solve   : 3.5n = 35 → n = 10
Answer  : 10 notebooks

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0459'
KEY = 'linear_cost/0459'
NAME = 'Linear cost 0459'
CATEGORY = 'Linear cost'
PROBLEM = 'Notebooks cost $3.50 each. With a $2 coupon, Dev paid $33.00. How many notebooks were bought?'
LET = 'n = items'
EQUATION = '3.5n − 2 = 33'
SOLVE = '3.5n = 35 → n = 10'
ANSWER = '10 notebooks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Notebooks cost ${0} each. With a ${1} coupon, Dev paid ${2}. How many notebooks were bought?'
NUMBERS = ['3.50', '2', '33.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
