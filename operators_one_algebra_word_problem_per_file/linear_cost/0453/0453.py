"""Algebra word problem 0453   [Linear cost]

Problem : Notebooks cost $4.50 each. With a $10 coupon, Bea paid $8.00. How many notebooks were bought?
Let     : n = items
Equation: 4.5n − 10 = 8
Solve   : 4.5n = 18 → n = 4
Answer  : 4 notebooks

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0453'
KEY = 'linear_cost/0453'
NAME = 'Linear cost 0453'
CATEGORY = 'Linear cost'
PROBLEM = 'Notebooks cost $4.50 each. With a $10 coupon, Bea paid $8.00. How many notebooks were bought?'
LET = 'n = items'
EQUATION = '4.5n − 10 = 8'
SOLVE = '4.5n = 18 → n = 4'
ANSWER = '4 notebooks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Notebooks cost ${0} each. With a ${1} coupon, Bea paid ${2}. How many notebooks were bought?'
NUMBERS = ['4.50', '10', '8.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
