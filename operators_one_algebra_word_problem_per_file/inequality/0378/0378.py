"""Algebra word problem 0378   [Inequality]

Problem : Jade has $110 and saves $40 a week. What is the fewest weeks needed to have at least $510?
Let     : w = weeks
Equation: 110 + 40w ≥ 510
Solve   : w ≥ 10 → w = 10 (smallest whole number that works)
Answer  : 10 weeks

Status  : ready: fewest_weeks_to_have_at_least answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0378'
KEY = 'inequality/0378'
NAME = 'Inequality 0378'
CATEGORY = 'Inequality'
PROBLEM = 'Jade has $110 and saves $40 a week. What is the fewest weeks needed to have at least $510?'
LET = 'w = weeks'
EQUATION = '110 + 40w ≥ 510'
SOLVE = 'w ≥ 10 → w = 10 (smallest whole number that works)'
ANSWER = '10 weeks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'fewest_weeks_to_have_at_least'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Jade has ${0} and saves ${1} a week. What is the fewest weeks needed to have at least ${2}?'
NUMBERS = ['110', '40', '510']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
