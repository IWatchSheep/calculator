"""Algebra word problem 0526   [Linear model]

Problem : A club has raised $220 so far. At its bake sale it charges $8 per box of cookies. How many more boxes must it sell to reach its $588 goal?
Let     : n = sales
Equation: 220 + 8n = 588
Solve   : 8n = 368 → n = 46
Answer  : 46

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0526'
KEY = 'linear_model/0526'
NAME = 'Linear model 0526'
CATEGORY = 'Linear model'
PROBLEM = 'A club has raised $220 so far. At its bake sale it charges $8 per box of cookies. How many more boxes must it sell to reach its $588 goal?'
LET = 'n = sales'
EQUATION = '220 + 8n = 588'
SOLVE = '8n = 368 → n = 46'
ANSWER = '46'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A club has raised ${0} so far. At its bake sale it charges ${1} per box of cookies. How many more boxes must it sell to reach its ${2} goal?'
NUMBERS = ['220', '8', '588']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
