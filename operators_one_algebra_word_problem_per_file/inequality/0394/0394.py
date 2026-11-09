"""Algebra word problem 0394   [Inequality]

Problem : Ivan has $70 and saves $20 a week. What is the fewest weeks needed to have at least $670?
Let     : w = weeks
Equation: 70 + 20w ≥ 670
Solve   : w ≥ 30 → w = 30 (smallest whole number that works)
Answer  : 30 weeks

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0394'
KEY = 'inequality/0394'
NAME = 'Inequality 0394'
CATEGORY = 'Inequality'
PROBLEM = 'Ivan has $70 and saves $20 a week. What is the fewest weeks needed to have at least $670?'
LET = 'w = weeks'
EQUATION = '70 + 20w ≥ 670'
SOLVE = 'w ≥ 30 → w = 30 (smallest whole number that works)'
ANSWER = '30 weeks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Ivan has ${0} and saves ${1} a week. What is the fewest weeks needed to have at least ${2}?'
NUMBERS = ['70', '20', '670']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
