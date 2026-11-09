"""Algebra word problem 0165   [Exponential]

Problem : A bacteria culture starts with 1000 cells and doubles every 20 minutes. When will it reach 4,000 cells?
Let     : t = minutes
Equation: 1000 × 2^(t/20) = 4000
Solve   : 2^(t/20) = 4 = 2^2 → t/20 = 2 → t = 40
Answer  : 40 minutes

Status  : ready: periodic_growth answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0165'
KEY = 'exponential/0165'
NAME = 'Exponential 0165'
CATEGORY = 'Exponential'
PROBLEM = 'A bacteria culture starts with 1000 cells and doubles every 20 minutes. When will it reach 4,000 cells?'
LET = 't = minutes'
EQUATION = '1000 × 2^(t/20) = 4000'
SOLVE = '2^(t/20) = 4 = 2^2 → t/20 = 2 → t = 40'
ANSWER = '40 minutes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'periodic_growth'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A bacteria culture starts with {0} cells and doubles every {1} minutes. When will it reach {2} cells?'
NUMBERS = ['1000', '20', '4000']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
