"""Algebra word problem 0416   [Joint variation]

Problem : 6 workers working 12 hours a day finish a job in 6 days. How many days would 4 workers working 6 hours a day take?
Let     : d = days
Equation: 6 × 12 × 6 = 4 × 6 × d
Solve   : 24d = 432 → d = 18
Answer  : 18 days

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0416'
KEY = 'joint_variation/0416'
NAME = 'Joint variation 0416'
CATEGORY = 'Joint variation'
PROBLEM = '6 workers working 12 hours a day finish a job in 6 days. How many days would 4 workers working 6 hours a day take?'
LET = 'd = days'
EQUATION = '6 × 12 × 6 = 4 × 6 × d'
SOLVE = '24d = 432 → d = 18'
ANSWER = '18 days'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} workers working {1} hours a day finish a job in {2} days. How many days would {3} workers working {4} hours a day take?'
NUMBERS = ['6', '12', '6', '4', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
