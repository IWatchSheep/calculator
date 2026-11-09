"""Algebra word problem 0486   [Linear model]

Problem : Sound travels about 343 m/s, so d = 343t. A storm is 2744 m away. How many seconds after the lightning flash will the thunder be heard?
Let     : t = seconds
Equation: 343t = 2744
Solve   : 343t = 2744 → t = 8
Answer  : 8 seconds

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0486'
KEY = 'linear_model/0486'
NAME = 'Linear model 0486'
CATEGORY = 'Linear model'
PROBLEM = 'Sound travels about 343 m/s, so d = 343t. A storm is 2744 m away. How many seconds after the lightning flash will the thunder be heard?'
LET = 't = seconds'
EQUATION = '343t = 2744'
SOLVE = '343t = 2744 → t = 8'
ANSWER = '8 seconds'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Sound travels about {0} m/s, so d = {1}t. A storm is {2} m away. How many seconds after the lightning flash will the thunder be heard?'
NUMBERS = ['343', '343', '2744']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
