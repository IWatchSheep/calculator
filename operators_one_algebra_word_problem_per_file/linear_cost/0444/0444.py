"""Algebra word problem 0444   [Linear cost]

Problem : A phone plan costs $50 a month and includes 10 GB of data. Each extra GB costs $5. The bill was $65. How much data was used?
Let     : g = GB used
Equation: 50 + 5(g − 10) = 65
Solve   : 5g = 65 → g = 13
Answer  : 13 GB

Status  : ready: plan_with_included answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0444'
KEY = 'linear_cost/0444'
NAME = 'Linear cost 0444'
CATEGORY = 'Linear cost'
PROBLEM = 'A phone plan costs $50 a month and includes 10 GB of data. Each extra GB costs $5. The bill was $65. How much data was used?'
LET = 'g = GB used'
EQUATION = '50 + 5(g − 10) = 65'
SOLVE = '5g = 65 → g = 13'
ANSWER = '13 GB'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'plan_with_included'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A phone plan costs ${0} a month and includes {1} GB of data. Each extra GB costs ${2}. The bill was ${3}. How much data was used?'
NUMBERS = ['50', '10', '5', '65']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
