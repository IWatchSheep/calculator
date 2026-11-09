"""Algebra word problem 0681   [Percent (commission)]

Problem : Nia earns a weekly base pay of $500 plus 15% commission on sales. One week the total pay was $2,900.00. What were the sales?
Let     : s = sales
Equation: 500 + 0.15s = 2900
Solve   : 0.15s = 2400 → s = 16000
Answer  : $16,000.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0681'
KEY = 'percent_commission/0681'
NAME = 'Percent (commission) 0681'
CATEGORY = 'Percent (commission)'
PROBLEM = 'Nia earns a weekly base pay of $500 plus 15% commission on sales. One week the total pay was $2,900.00. What were the sales?'
LET = 's = sales'
EQUATION = '500 + 0.15s = 2900'
SOLVE = '0.15s = 2400 → s = 16000'
ANSWER = '$16,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Nia earns a weekly base pay of ${0} plus {1}% commission on sales. One week the total pay was ${2}. What were the sales?'
NUMBERS = ['500', '15', '2900.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
