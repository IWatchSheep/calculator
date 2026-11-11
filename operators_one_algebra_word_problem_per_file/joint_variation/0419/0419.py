"""Algebra word problem 0419   [Joint variation]

Problem : 3 workers working 6 hours a day finish a job in 6 days. How many days would 2 workers working 9 hours a day take?
Let     : d = days
Equation: 3 × 6 × 6 = 2 × 9 × d
Solve   : 18d = 108 → d = 6
Answer  : 6 days

Status  : ready: archive_joint_variation_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0419'
KEY = 'joint_variation/0419'
NAME = 'Joint variation 0419'
CATEGORY = 'Joint variation'
PROBLEM = '3 workers working 6 hours a day finish a job in 6 days. How many days would 2 workers working 9 hours a day take?'
LET = 'd = days'
EQUATION = '3 × 6 × 6 = 2 × 9 × d'
SOLVE = '18d = 108 → d = 6'
ANSWER = '6 days'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_joint_variation_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} workers working {1} hours a day finish a job in {2} days. How many days would {3} workers working {4} hours a day take?'
NUMBERS = ['3', '6', '6', '2', '9']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
