"""Algebra word problem 0369   [Inequality]

Problem : A salesperson earns $500 a week plus 10% of sales. What is the least (whole-dollar) amount of sales needed to earn at least $900?
Let     : s = sales
Equation: 500 + 0.1s ≥ 900
Solve   : s ≥ 4000 → s = 4000 (smallest whole number that works)
Answer  : $4,000.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0369'
KEY = 'inequality/0369'
NAME = 'Inequality 0369'
CATEGORY = 'Inequality'
PROBLEM = 'A salesperson earns $500 a week plus 10% of sales. What is the least (whole-dollar) amount of sales needed to earn at least $900?'
LET = 's = sales'
EQUATION = '500 + 0.1s ≥ 900'
SOLVE = 's ≥ 4000 → s = 4000 (smallest whole number that works)'
ANSWER = '$4,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A salesperson earns ${0} a week plus {1}% of sales. What is the least (whole-dollar) amount of sales needed to earn at least ${2}?'
NUMBERS = ['500', '10', '900']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
