"""Algebra word problem 0420   [Linear cost]

Problem : A venue charges $100 plus $15 per guest. The total was $865. How many guests came?
Let     : n = guests
Equation: 100 + 15n = 865
Solve   : 15n = 765 → n = 51
Answer  : 51 guests

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0420'
KEY = 'linear_cost/0420'
NAME = 'Linear cost 0420'
CATEGORY = 'Linear cost'
PROBLEM = 'A venue charges $100 plus $15 per guest. The total was $865. How many guests came?'
LET = 'n = guests'
EQUATION = '100 + 15n = 865'
SOLVE = '15n = 765 → n = 51'
ANSWER = '51 guests'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A venue charges ${0} plus ${1} per guest. The total was ${2}. How many guests came?'
NUMBERS = ['100', '15', '865']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
