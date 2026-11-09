"""Algebra word problem 0435   [Linear cost]

Problem : Zane gets $10 allowance a week plus $3 for each extra chore. Over 8 weeks that came to $92. How many extra chores were done?
Let     : n = chores
Equation: 10(8) + 3n = 92
Solve   : 3n = 12 → n = 4
Answer  : 4 chores

Status  : ready: base_plus_extra_over_time answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0435'
KEY = 'linear_cost/0435'
NAME = 'Linear cost 0435'
CATEGORY = 'Linear cost'
PROBLEM = 'Zane gets $10 allowance a week plus $3 for each extra chore. Over 8 weeks that came to $92. How many extra chores were done?'
LET = 'n = chores'
EQUATION = '10(8) + 3n = 92'
SOLVE = '3n = 12 → n = 4'
ANSWER = '4 chores'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'base_plus_extra_over_time'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Zane gets ${0} allowance a week plus ${1} for each extra chore. Over {2} weeks that came to ${3}. How many extra chores were done?'
NUMBERS = ['10', '3', '8', '92']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
