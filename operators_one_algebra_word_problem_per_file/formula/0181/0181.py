"""Algebra word problem 0181   [Formula]

Problem : Using V = IR, find the current when the voltage is 12 V and the resistance is 4 Ω.
Let     : i = current
Equation: 4i = 12
Solve   : 4i = 12 → i = 3
Answer  : 3 A

Status  : ready: archive_formula_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0181'
KEY = 'formula/0181'
NAME = 'Formula 0181'
CATEGORY = 'Formula'
PROBLEM = 'Using V = IR, find the current when the voltage is 12 V and the resistance is 4 Ω.'
LET = 'i = current'
EQUATION = '4i = 12'
SOLVE = '4i = 12 → i = 3'
ANSWER = '3 A'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_formula_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Using V = IR, find the current when the voltage is {0} V and the resistance is {1} Ω.'
NUMBERS = ['12', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
