"""Algebra word problem 0470   [Linear cost]

Problem : A venue charges $575 plus $12 per guest. The total was $1511. How many guests came?
Let     : n = guests
Equation: 575 + 12n = 1511
Solve   : 12n = 936 → n = 78
Answer  : 78 guests

Status  : ready: fixed_plus_rate answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0470'
KEY = 'linear_cost/0470'
NAME = 'Linear cost 0470'
CATEGORY = 'Linear cost'
PROBLEM = 'A venue charges $575 plus $12 per guest. The total was $1511. How many guests came?'
LET = 'n = guests'
EQUATION = '575 + 12n = 1511'
SOLVE = '12n = 936 → n = 78'
ANSWER = '78 guests'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fixed_plus_rate'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A venue charges ${0} plus ${1} per guest. The total was ${2}. How many guests came?'
NUMBERS = ['575', '12', '1511']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
