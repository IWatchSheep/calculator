"""Algebra word problem 0680   [Percent (commission)]

Problem : A salesperson gets $600 per week plus 15% of everything they sell. To earn $2,100.00 in a week, how much must they sell?
Let     : s = sales
Equation: 600 + 0.15s = 2100
Solve   : 0.15s = 1500 → s = 10000
Answer  : $10,000.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0680'
KEY = 'percent_commission/0680'
NAME = 'Percent (commission) 0680'
CATEGORY = 'Percent (commission)'
PROBLEM = 'A salesperson gets $600 per week plus 15% of everything they sell. To earn $2,100.00 in a week, how much must they sell?'
LET = 's = sales'
EQUATION = '600 + 0.15s = 2100'
SOLVE = '0.15s = 1500 → s = 10000'
ANSWER = '$10,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A salesperson gets ${0} per week plus {1}% of everything they sell. To earn ${2} in a week, how much must they sell?'
NUMBERS = ['600', '15', '2100.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
