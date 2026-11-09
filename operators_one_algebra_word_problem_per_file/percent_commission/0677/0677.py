"""Algebra word problem 0677   [Percent (commission)]

Problem : Theo earns a weekly base pay of $400 plus 2% commission on sales. One week the total pay was $560.00. What were the sales?
Let     : s = sales
Equation: 400 + 0.02s = 560
Solve   : s/50 = 160 → s = 160 × 50 = 8000
Answer  : $8,000.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0677'
KEY = 'percent_commission/0677'
NAME = 'Percent (commission) 0677'
CATEGORY = 'Percent (commission)'
PROBLEM = 'Theo earns a weekly base pay of $400 plus 2% commission on sales. One week the total pay was $560.00. What were the sales?'
LET = 's = sales'
EQUATION = '400 + 0.02s = 560'
SOLVE = 's/50 = 160 → s = 160 × 50 = 8000'
ANSWER = '$8,000.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Theo earns a weekly base pay of ${0} plus {1}% commission on sales. One week the total pay was ${2}. What were the sales?'
NUMBERS = ['400', '2', '560.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
