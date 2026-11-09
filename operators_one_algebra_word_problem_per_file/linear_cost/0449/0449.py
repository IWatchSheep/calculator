"""Algebra word problem 0449   [Linear cost]

Problem : A venue charges $325 plus $18 per guest. The total was $1909. How many guests came?
Let     : n = guests
Equation: 325 + 18n = 1909
Solve   : 18n = 1584 → n = 88
Answer  : 88 guests

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0449'
KEY = 'linear_cost/0449'
NAME = 'Linear cost 0449'
CATEGORY = 'Linear cost'
PROBLEM = 'A venue charges $325 plus $18 per guest. The total was $1909. How many guests came?'
LET = 'n = guests'
EQUATION = '325 + 18n = 1909'
SOLVE = '18n = 1584 → n = 88'
ANSWER = '88 guests'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A venue charges ${0} plus ${1} per guest. The total was ${2}. How many guests came?'
NUMBERS = ['325', '18', '1909']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
