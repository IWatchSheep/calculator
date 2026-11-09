"""Algebra word problem 0362   [Inequality]

Problem : Elena has $160 and saves $40 a week. What is the fewest weeks needed to have at least $670?
Let     : w = weeks
Equation: 160 + 40w ≥ 670
Solve   : w ≥ 12.75 → w = 13 (smallest whole number that works)
Answer  : 13 weeks

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0362'
KEY = 'inequality/0362'
NAME = 'Inequality 0362'
CATEGORY = 'Inequality'
PROBLEM = 'Elena has $160 and saves $40 a week. What is the fewest weeks needed to have at least $670?'
LET = 'w = weeks'
EQUATION = '160 + 40w ≥ 670'
SOLVE = 'w ≥ 12.75 → w = 13 (smallest whole number that works)'
ANSWER = '13 weeks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Elena has ${0} and saves ${1} a week. What is the fewest weeks needed to have at least ${2}?'
NUMBERS = ['160', '40', '670']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
