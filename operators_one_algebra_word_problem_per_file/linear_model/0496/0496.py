"""Algebra word problem 0496   [Linear model]

Problem : A pool holds 4,500 L and drains at 50 L per minute. After how many minutes will 800 L remain?
Let     : t = minutes
Equation: 4500 − 50t = 800
Solve   : 50t = 3700 → t = 74
Answer  : 74 minutes

Status  : ready: drain_or_fill answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0496'
KEY = 'linear_model/0496'
NAME = 'Linear model 0496'
CATEGORY = 'Linear model'
PROBLEM = 'A pool holds 4,500 L and drains at 50 L per minute. After how many minutes will 800 L remain?'
LET = 't = minutes'
EQUATION = '4500 − 50t = 800'
SOLVE = '50t = 3700 → t = 74'
ANSWER = '74 minutes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'drain_or_fill'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A pool holds {0} L and drains at {1} L per minute. After how many minutes will {2} L remain?'
NUMBERS = ['4500', '50', '800']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
