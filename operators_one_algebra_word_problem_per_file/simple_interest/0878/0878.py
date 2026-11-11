"""Algebra word problem 0878   [Simple interest]

Problem : $4,500.00 earns $720.00 in simple interest over 8 years. What is the annual interest rate?
Let     : r = rate (as a percent)
Equation: 4500 × (r/100) × 8 = 720
Solve   : 360r = 720 → r = 2
Answer  : 2%

Status  : ready: archive_simple_interest_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0878'
KEY = 'simple_interest/0878'
NAME = 'Simple interest 0878'
CATEGORY = 'Simple interest'
PROBLEM = '$4,500.00 earns $720.00 in simple interest over 8 years. What is the annual interest rate?'
LET = 'r = rate (as a percent)'
EQUATION = '4500 × (r/100) × 8 = 720'
SOLVE = '360r = 720 → r = 2'
ANSWER = '2%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_simple_interest_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '${0} earns ${1} in simple interest over {2} years. What is the annual interest rate?'
NUMBERS = ['4500.00', '720.00', '8']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
