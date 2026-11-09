"""Algebra word problem 0684   [Percent (markup)]

Problem : After a 100% markup, a phone case is priced at $590.00. What was the wholesale cost?
Let     : c = cost
Equation: 2c = 590
Solve   : 2c = 590 → c = 295
Answer  : $295.00

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0684'
KEY = 'percent_markup/0684'
NAME = 'Percent (markup) 0684'
CATEGORY = 'Percent (markup)'
PROBLEM = 'After a 100% markup, a phone case is priced at $590.00. What was the wholesale cost?'
LET = 'c = cost'
EQUATION = '2c = 590'
SOLVE = '2c = 590 → c = 295'
ANSWER = '$295.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'After a {0}% markup, a phone case is priced at ${1}. What was the wholesale cost?'
NUMBERS = ['100', '590.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
