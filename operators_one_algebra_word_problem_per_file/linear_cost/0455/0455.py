"""Algebra word problem 0455   [Linear cost]

Problem : A phone plan costs $30 a month and includes 15 GB of data. Each extra GB costs $8. The bill was $62. How much data was used?
Let     : g = GB used
Equation: 30 + 8(g − 15) = 62
Solve   : 8g = 152 → g = 19
Answer  : 19 GB

Status  : ready: plan_with_included answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0455'
KEY = 'linear_cost/0455'
NAME = 'Linear cost 0455'
CATEGORY = 'Linear cost'
PROBLEM = 'A phone plan costs $30 a month and includes 15 GB of data. Each extra GB costs $8. The bill was $62. How much data was used?'
LET = 'g = GB used'
EQUATION = '30 + 8(g − 15) = 62'
SOLVE = '8g = 152 → g = 19'
ANSWER = '19 GB'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'plan_with_included'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A phone plan costs ${0} a month and includes {1} GB of data. Each extra GB costs ${2}. The bill was ${3}. How much data was used?'
NUMBERS = ['30', '15', '8', '62']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
