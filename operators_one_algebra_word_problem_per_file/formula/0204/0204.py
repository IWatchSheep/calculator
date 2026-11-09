"""Algebra word problem 0204   [Formula]

Problem : Using V = IR, find the resistance (in ohms) when the voltage is 50 V and the current is 5 A.
Let     : r = resistance
Equation: 5r = 50
Solve   : 5r = 50 → r = 10
Answer  : 10 Ω

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0204'
KEY = 'formula/0204'
NAME = 'Formula 0204'
CATEGORY = 'Formula'
PROBLEM = 'Using V = IR, find the resistance (in ohms) when the voltage is 50 V and the current is 5 A.'
LET = 'r = resistance'
EQUATION = '5r = 50'
SOLVE = '5r = 50 → r = 10'
ANSWER = '10 Ω'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Using V = IR, find the resistance (in ohms) when the voltage is {0} V and the current is {1} A.'
NUMBERS = ['50', '5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
