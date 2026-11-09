"""Algebra word problem 0678   [Percent (commission)]

Problem : Isla earns a weekly base pay of $750 plus 6% commission on sales. One week the total pay was $2,670.00. What were the sales?
Let     : s = sales
Equation: 750 + 0.06s = 2670
Solve   : 0.06s = 1920 → s = 32000
Answer  : $32,000.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0678'
KEY = 'percent_commission/0678'
NAME = 'Percent (commission) 0678'
CATEGORY = 'Percent (commission)'
PROBLEM = 'Isla earns a weekly base pay of $750 plus 6% commission on sales. One week the total pay was $2,670.00. What were the sales?'
LET = 's = sales'
EQUATION = '750 + 0.06s = 2670'
SOLVE = '0.06s = 1920 → s = 32000'
ANSWER = '$32,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Isla earns a weekly base pay of ${0} plus {1}% commission on sales. One week the total pay was ${2}. What were the sales?'
NUMBERS = ['750', '6', '2670.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
