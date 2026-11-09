"""Algebra word problem 0424   [Linear cost]

Problem : Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $120. How many extra chores were done?
Let     : n = chores
Equation: 10(8) + 4n = 120
Solve   : 4n = 40 → n = 10
Answer  : 10 chores

Status  : ready: base_plus_extra_over_time answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0424'
KEY = 'linear_cost/0424'
NAME = 'Linear cost 0424'
CATEGORY = 'Linear cost'
PROBLEM = 'Umar gets $10 allowance a week plus $4 for each extra chore. Over 8 weeks that came to $120. How many extra chores were done?'
LET = 'n = chores'
EQUATION = '10(8) + 4n = 120'
SOLVE = '4n = 40 → n = 10'
ANSWER = '10 chores'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'base_plus_extra_over_time'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Umar gets ${0} allowance a week plus ${1} for each extra chore. Over {2} weeks that came to ${3}. How many extra chores were done?'
NUMBERS = ['10', '4', '8', '120']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
