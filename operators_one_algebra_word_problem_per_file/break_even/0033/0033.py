"""Algebra word problem 0033   [Break-even]

Problem : Buying a pressure washer costs $500. Renting one costs $50 once plus $50 per use. After how many uses does renting cost the same as buying?
Let     : n = uses
Equation: 50 + 50n = 500
Solve   : 50n = 450 → n = 9
Answer  : 9 uses

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0033'
KEY = 'break_even/0033'
NAME = 'Break-even 0033'
CATEGORY = 'Break-even'
PROBLEM = 'Buying a pressure washer costs $500. Renting one costs $50 once plus $50 per use. After how many uses does renting cost the same as buying?'
LET = 'n = uses'
EQUATION = '50 + 50n = 500'
SOLVE = '50n = 450 → n = 9'
ANSWER = '9 uses'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Buying a pressure washer costs ${0}. Renting one costs ${1} once plus ${2} per use. After how many uses does renting cost the same as buying?'
NUMBERS = ['500', '50', '50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
