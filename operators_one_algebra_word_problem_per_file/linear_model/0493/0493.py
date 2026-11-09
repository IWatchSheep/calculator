"""Algebra word problem 0493   [Linear model]

Problem : A 548-page book has 116 pages already read. How many pages a day must be read to finish in 18 days?
Let     : p = pages per day
Equation: 116 + 18p = 548
Solve   : 18p = 432 → p = 24
Answer  : 24 pages per day

Status  : ready: pages_per_day answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0493'
KEY = 'linear_model/0493'
NAME = 'Linear model 0493'
CATEGORY = 'Linear model'
PROBLEM = 'A 548-page book has 116 pages already read. How many pages a day must be read to finish in 18 days?'
LET = 'p = pages per day'
EQUATION = '116 + 18p = 548'
SOLVE = '18p = 432 → p = 24'
ANSWER = '24 pages per day'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'pages_per_day'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0}-page book has {1} pages already read. How many pages a day must be read to finish in {2} days?'
NUMBERS = ['548', '116', '18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
