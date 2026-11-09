"""Algebra word problem 0527   [Linear model]

Problem : A pool holds 2,600 L and drains at 360 L per minute. After how many minutes will 800 L remain?
Let     : t = minutes
Equation: 2600 − 360t = 800
Solve   : 360t = 1800 → t = 5
Answer  : 5 minutes

Status  : ready: drain_or_fill answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0527'
KEY = 'linear_model/0527'
NAME = 'Linear model 0527'
CATEGORY = 'Linear model'
PROBLEM = 'A pool holds 2,600 L and drains at 360 L per minute. After how many minutes will 800 L remain?'
LET = 't = minutes'
EQUATION = '2600 − 360t = 800'
SOLVE = '360t = 1800 → t = 5'
ANSWER = '5 minutes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'drain_or_fill'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A pool holds {0} L and drains at {1} L per minute. After how many minutes will {2} L remain?'
NUMBERS = ['2600', '360', '800']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
