"""Algebra word problem 0418   [Joint variation]

Problem : 4 workers working 12 hours a day finish a job in 10 days. How many days would 10 workers working 6 hours a day take?
Let     : d = days
Equation: 4 × 12 × 10 = 10 × 6 × d
Solve   : 60d = 480 → d = 8
Answer  : 8 days

Status  : ready: archive_joint_variation_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0418'
KEY = 'joint_variation/0418'
NAME = 'Joint variation 0418'
CATEGORY = 'Joint variation'
PROBLEM = '4 workers working 12 hours a day finish a job in 10 days. How many days would 10 workers working 6 hours a day take?'
LET = 'd = days'
EQUATION = '4 × 12 × 10 = 10 × 6 × d'
SOLVE = '60d = 480 → d = 8'
ANSWER = '8 days'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_joint_variation_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} workers working {1} hours a day finish a job in {2} days. How many days would {3} workers working {4} hours a day take?'
NUMBERS = ['4', '12', '10', '10', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
