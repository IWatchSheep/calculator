"""Algebra word problem 0389   [Inequality]

Problem : A salesperson earns $500 a week plus 12% of sales. What is the least (whole-dollar) amount of sales needed to earn at least $1500?
Let     : s = sales
Equation: 500 + 0.12s ≥ 1500
Solve   : s ≥ 25000/3 → s = 8334 (smallest whole number that works)
Answer  : $8,334.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0389'
KEY = 'inequality/0389'
NAME = 'Inequality 0389'
CATEGORY = 'Inequality'
PROBLEM = 'A salesperson earns $500 a week plus 12% of sales. What is the least (whole-dollar) amount of sales needed to earn at least $1500?'
LET = 's = sales'
EQUATION = '500 + 0.12s ≥ 1500'
SOLVE = 's ≥ 25000/3 → s = 8334 (smallest whole number that works)'
ANSWER = '$8,334.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A salesperson earns ${0} a week plus {1}% of sales. What is the least (whole-dollar) amount of sales needed to earn at least ${2}?'
NUMBERS = ['500', '12', '1500']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
