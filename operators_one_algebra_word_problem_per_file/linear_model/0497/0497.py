"""Algebra word problem 0497   [Linear model]

Problem : A club has raised $40 so far. At its bake sale it charges $15 per box of cookies. How many more boxes must it sell to reach its $940 goal?
Let     : n = sales
Equation: 40 + 15n = 940
Solve   : 15n = 900 → n = 60
Answer  : 60

Status  : ready: archive_linear_model_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0497'
KEY = 'linear_model/0497'
NAME = 'Linear model 0497'
CATEGORY = 'Linear model'
PROBLEM = 'A club has raised $40 so far. At its bake sale it charges $15 per box of cookies. How many more boxes must it sell to reach its $940 goal?'
LET = 'n = sales'
EQUATION = '40 + 15n = 940'
SOLVE = '15n = 900 → n = 60'
ANSWER = '60'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_linear_model_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A club has raised ${0} so far. At its bake sale it charges ${1} per box of cookies. How many more boxes must it sell to reach its ${2} goal?'
NUMBERS = ['40', '15', '940']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
