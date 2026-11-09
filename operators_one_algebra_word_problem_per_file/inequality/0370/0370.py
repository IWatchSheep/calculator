"""Algebra word problem 0370   [Inequality]

Problem : Isla has $10 and saves $15 a week. What is the fewest weeks needed to have at least $920?
Let     : w = weeks
Equation: 10 + 15w ≥ 920
Solve   : w ≥ 182/3 → w = 61 (smallest whole number that works)
Answer  : 61 weeks

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0370'
KEY = 'inequality/0370'
NAME = 'Inequality 0370'
CATEGORY = 'Inequality'
PROBLEM = 'Isla has $10 and saves $15 a week. What is the fewest weeks needed to have at least $920?'
LET = 'w = weeks'
EQUATION = '10 + 15w ≥ 920'
SOLVE = 'w ≥ 182/3 → w = 61 (smallest whole number that works)'
ANSWER = '61 weeks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Isla has ${0} and saves ${1} a week. What is the fewest weeks needed to have at least ${2}?'
NUMBERS = ['10', '15', '920']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
