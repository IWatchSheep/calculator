"""Algebra word problem 0810   [Ratio]

Problem : An estate of $88,500.00 is split among three heirs. Theo gets 3 times as much as Kira, and Umar gets $1,000.00 more than Kira. How much does each receive?
Let     : x = Kira's share
Equation: 3x + x + (x + 1000) = 88500
Solve   : 5x = 87500 → x = 17500
Answer  : Theo $52,500.00, Kira $17,500.00, Umar $18,500.00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0810'
KEY = 'ratio/0810'
NAME = 'Ratio 0810'
CATEGORY = 'Ratio'
PROBLEM = 'An estate of $88,500.00 is split among three heirs. Theo gets 3 times as much as Kira, and Umar gets $1,000.00 more than Kira. How much does each receive?'
LET = "x = Kira's share"
EQUATION = '3x + x + (x + 1000) = 88500'
SOLVE = '5x = 87500 → x = 17500'
ANSWER = 'Theo $52,500.00, Kira $17,500.00, Umar $18,500.00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An estate of ${0} is split among three heirs. Theo gets {1} times as much as Kira, and Umar gets ${2} more than Kira. How much does each receive?'
NUMBERS = ['88500.00', '3', '1000.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
