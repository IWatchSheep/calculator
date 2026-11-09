"""Algebra word problem 0037   [Break-even]

Problem : Buying a carpet cleaner costs $550. Renting one costs $25 once plus $15 per use. After how many uses does renting cost the same as buying?
Let     : n = uses
Equation: 25 + 15n = 550
Solve   : 15n = 525 → n = 35
Answer  : 35 uses

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0037'
KEY = 'break_even/0037'
NAME = 'Break-even 0037'
CATEGORY = 'Break-even'
PROBLEM = 'Buying a carpet cleaner costs $550. Renting one costs $25 once plus $15 per use. After how many uses does renting cost the same as buying?'
LET = 'n = uses'
EQUATION = '25 + 15n = 550'
SOLVE = '15n = 525 → n = 35'
ANSWER = '35 uses'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Buying a carpet cleaner costs ${0}. Renting one costs ${1} once plus ${2} per use. After how many uses does renting cost the same as buying?'
NUMBERS = ['550', '25', '15']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
