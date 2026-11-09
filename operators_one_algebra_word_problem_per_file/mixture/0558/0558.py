"""Algebra word problem 0558   [Mixture]

Problem : How many pounds of peanuts worth $12/lb must be added to 12 lb of peanuts worth $6/lb to make a mix worth $9/lb?
Let     : x = pounds added
Equation: 6(12) + 12x = 9(12 + x)
Solve   : 3x = 36 → x = 12
Answer  : 12 lb

Status  : ready: add_to_blend answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0558'
KEY = 'mixture/0558'
NAME = 'Mixture 0558'
CATEGORY = 'Mixture'
PROBLEM = 'How many pounds of peanuts worth $12/lb must be added to 12 lb of peanuts worth $6/lb to make a mix worth $9/lb?'
LET = 'x = pounds added'
EQUATION = '6(12) + 12x = 9(12 + x)'
SOLVE = '3x = 36 → x = 12'
ANSWER = '12 lb'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'add_to_blend'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many pounds of peanuts worth ${0}/lb must be added to {1} lb of peanuts worth ${2}/lb to make a mix worth ${3}/lb?'
NUMBERS = ['12', '12', '6', '9']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
