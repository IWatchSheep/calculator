"""Algebra word problem 0029   [Break-even]

Problem : Electric utility plan A costs $38.00 plus $0.15 per kWh. Plan B costs $26.50 plus $0.20 per kWh. For how many kWhs do they cost the same?
Let     : x = number of kWhs
Equation: 38 + 0.15x = 26.5 + 0.2x
Solve   : 0.05x = 11.5 → x = 230
Answer  : 230 kWhs

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0029'
KEY = 'break_even/0029'
NAME = 'Break-even 0029'
CATEGORY = 'Break-even'
PROBLEM = 'Electric utility plan A costs $38.00 plus $0.15 per kWh. Plan B costs $26.50 plus $0.20 per kWh. For how many kWhs do they cost the same?'
LET = 'x = number of kWhs'
EQUATION = '38 + 0.15x = 26.5 + 0.2x'
SOLVE = '0.05x = 11.5 → x = 230'
ANSWER = '230 kWhs'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Electric utility plan A costs ${0} plus ${1} per kWh. Plan B costs ${2} plus ${3} per kWh. For how many kWhs do they cost the same?'
NUMBERS = ['38.00', '0.15', '26.50', '0.20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
