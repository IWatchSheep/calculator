"""Algebra word problem 0047   [Break-even]

Problem : Buying a pressure washer costs $1275. Renting costs $25 per use. After how many uses would renting cost the same as buying?
Let     : n = uses
Equation: 25n = 1275
Solve   : 25n = 1275 → n = 51
Answer  : 51 uses

Status  : ready: rent_per_use_equals_buy answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0047'
KEY = 'break_even/0047'
NAME = 'Break-even 0047'
CATEGORY = 'Break-even'
PROBLEM = 'Buying a pressure washer costs $1275. Renting costs $25 per use. After how many uses would renting cost the same as buying?'
LET = 'n = uses'
EQUATION = '25n = 1275'
SOLVE = '25n = 1275 → n = 51'
ANSWER = '51 uses'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'rent_per_use_equals_buy'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Buying a pressure washer costs ${0}. Renting costs ${1} per use. After how many uses would renting cost the same as buying?'
NUMBERS = ['1275', '25']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
