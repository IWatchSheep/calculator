"""Algebra word problem 0441   [Linear cost]

Problem : Bags of chips cost $7.50 each. With a $10 coupon, Kira paid $12.50. How many bags of chips were bought?
Let     : n = items
Equation: 7.5n − 10 = 12.5
Solve   : 7.5n = 22.5 → n = 3
Answer  : 3 bags of chips

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0441'
KEY = 'linear_cost/0441'
NAME = 'Linear cost 0441'
CATEGORY = 'Linear cost'
PROBLEM = 'Bags of chips cost $7.50 each. With a $10 coupon, Kira paid $12.50. How many bags of chips were bought?'
LET = 'n = items'
EQUATION = '7.5n − 10 = 12.5'
SOLVE = '7.5n = 22.5 → n = 3'
ANSWER = '3 bags of chips'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Bags of chips cost ${0} each. With a ${1} coupon, Kira paid ${2}. How many bags of chips were bought?'
NUMBERS = ['7.50', '10', '12.50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
