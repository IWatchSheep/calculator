"""Algebra word problem 0682   [Percent (markup)]

Problem : After a 75% markup, a watch is priced at $1,347.50. What was the wholesale cost?
Let     : c = cost
Equation: 1.75c = 1347.5
Solve   : 1.75c = 1347.5 → c = 770
Answer  : $770.00

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0682'
KEY = 'percent_markup/0682'
NAME = 'Percent (markup) 0682'
CATEGORY = 'Percent (markup)'
PROBLEM = 'After a 75% markup, a watch is priced at $1,347.50. What was the wholesale cost?'
LET = 'c = cost'
EQUATION = '1.75c = 1347.5'
SOLVE = '1.75c = 1347.5 → c = 770'
ANSWER = '$770.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'After a {0}% markup, a watch is priced at ${1}. What was the wholesale cost?'
NUMBERS = ['75', '1347.50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
