"""Algebra word problem 0201   [Formula]

Problem : Using F = (9/5)C + 32, what Celsius temperature equals 167°F?
Let     : C = degrees Celsius
Equation: (9/5)c + 32 = 167
Solve   : 1.8c = 135 → c = 75
Answer  : 75°C

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0201'
KEY = 'formula/0201'
NAME = 'Formula 0201'
CATEGORY = 'Formula'
PROBLEM = 'Using F = (9/5)C + 32, what Celsius temperature equals 167°F?'
LET = 'C = degrees Celsius'
EQUATION = '(9/5)c + 32 = 167'
SOLVE = '1.8c = 135 → c = 75'
ANSWER = '75°C'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Using F = ({0}/{1})C + {2}, what Celsius temperature equals {3}°F?'
NUMBERS = ['9', '5', '32', '167']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
