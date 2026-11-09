"""Algebra word problem 0477   [Linear cost]

Problem : Bags of chips cost $4.00 each. With a $10 coupon, Wren paid $10.00. How many bags of chips were bought?
Let     : n = items
Equation: 4n − 10 = 10
Solve   : 4n = 20 → n = 5
Answer  : 5 bags of chips

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0477'
KEY = 'linear_cost/0477'
NAME = 'Linear cost 0477'
CATEGORY = 'Linear cost'
PROBLEM = 'Bags of chips cost $4.00 each. With a $10 coupon, Wren paid $10.00. How many bags of chips were bought?'
LET = 'n = items'
EQUATION = '4n − 10 = 10'
SOLVE = '4n = 20 → n = 5'
ANSWER = '5 bags of chips'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Bags of chips cost ${0} each. With a ${1} coupon, Wren paid ${2}. How many bags of chips were bought?'
NUMBERS = ['4.00', '10', '10.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
