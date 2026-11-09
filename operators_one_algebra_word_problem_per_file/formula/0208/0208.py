"""Algebra word problem 0208   [Formula]

Problem : Using V = IR, find the resistance (in ohms) when the voltage is 12 V and the current is 2 A.
Let     : r = resistance
Equation: 2r = 12
Solve   : 2r = 12 → r = 6
Answer  : 6 Ω

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0208'
KEY = 'formula/0208'
NAME = 'Formula 0208'
CATEGORY = 'Formula'
PROBLEM = 'Using V = IR, find the resistance (in ohms) when the voltage is 12 V and the current is 2 A.'
LET = 'r = resistance'
EQUATION = '2r = 12'
SOLVE = '2r = 12 → r = 6'
ANSWER = '6 Ω'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Using V = IR, find the resistance (in ohms) when the voltage is {0} V and the current is {1} A.'
NUMBERS = ['12', '2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
