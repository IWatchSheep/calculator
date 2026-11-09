"""Algebra word problem 0367   [Inequality]

Problem : A salesperson earns $400 a week plus 12% of sales. What is the least (whole-dollar) amount of sales needed to earn at least $1500?
Let     : s = sales
Equation: 400 + 0.12s ≥ 1500
Solve   : s ≥ 27500/3 → s = 9167 (smallest whole number that works)
Answer  : $9,167.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0367'
KEY = 'inequality/0367'
NAME = 'Inequality 0367'
CATEGORY = 'Inequality'
PROBLEM = 'A salesperson earns $400 a week plus 12% of sales. What is the least (whole-dollar) amount of sales needed to earn at least $1500?'
LET = 's = sales'
EQUATION = '400 + 0.12s ≥ 1500'
SOLVE = 's ≥ 27500/3 → s = 9167 (smallest whole number that works)'
ANSWER = '$9,167.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A salesperson earns ${0} a week plus {1}% of sales. What is the least (whole-dollar) amount of sales needed to earn at least ${2}?'
NUMBERS = ['400', '12', '1500']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
