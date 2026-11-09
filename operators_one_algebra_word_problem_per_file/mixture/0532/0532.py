"""Algebra word problem 0532   [Mixture]

Problem : How many pounds of coffee worth $10/lb must be added to 14 lb of coffee worth $8/lb to make a mix worth $9/lb?
Let     : x = pounds added
Equation: 8(14) + 10x = 9(14 + x)
Solve   : Collect like terms → x = 14
Answer  : 14 lb

Status  : ready: add_to_blend answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0532'
KEY = 'mixture/0532'
NAME = 'Mixture 0532'
CATEGORY = 'Mixture'
PROBLEM = 'How many pounds of coffee worth $10/lb must be added to 14 lb of coffee worth $8/lb to make a mix worth $9/lb?'
LET = 'x = pounds added'
EQUATION = '8(14) + 10x = 9(14 + x)'
SOLVE = 'Collect like terms → x = 14'
ANSWER = '14 lb'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'add_to_blend'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many pounds of coffee worth ${0}/lb must be added to {1} lb of coffee worth ${2}/lb to make a mix worth ${3}/lb?'
NUMBERS = ['10', '14', '8', '9']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
