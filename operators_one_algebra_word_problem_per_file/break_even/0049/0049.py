"""Algebra word problem 0049   [Break-even]

Problem : Buying a pressure washer costs $200. Renting one costs $25 once plus $25 per use. After how many uses does renting cost the same as buying?
Let     : n = uses
Equation: 25 + 25n = 200
Solve   : 25n = 175 → n = 7
Answer  : 7 uses

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0049'
KEY = 'break_even/0049'
NAME = 'Break-even 0049'
CATEGORY = 'Break-even'
PROBLEM = 'Buying a pressure washer costs $200. Renting one costs $25 once plus $25 per use. After how many uses does renting cost the same as buying?'
LET = 'n = uses'
EQUATION = '25 + 25n = 200'
SOLVE = '25n = 175 → n = 7'
ANSWER = '7 uses'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Buying a pressure washer costs ${0}. Renting one costs ${1} once plus ${2} per use. After how many uses does renting cost the same as buying?'
NUMBERS = ['200', '25', '25']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
