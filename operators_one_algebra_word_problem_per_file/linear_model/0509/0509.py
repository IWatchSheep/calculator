"""Algebra word problem 0509   [Linear model]

Problem : A club has raised $30 so far. At its car wash it charges $12 per car. How many more cars must it sell to reach its $486 goal?
Let     : n = sales
Equation: 30 + 12n = 486
Solve   : 12n = 456 → n = 38
Answer  : 38

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0509'
KEY = 'linear_model/0509'
NAME = 'Linear model 0509'
CATEGORY = 'Linear model'
PROBLEM = 'A club has raised $30 so far. At its car wash it charges $12 per car. How many more cars must it sell to reach its $486 goal?'
LET = 'n = sales'
EQUATION = '30 + 12n = 486'
SOLVE = '12n = 456 → n = 38'
ANSWER = '38'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A club has raised ${0} so far. At its car wash it charges ${1} per car. How many more cars must it sell to reach its ${2} goal?'
NUMBERS = ['30', '12', '486']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
