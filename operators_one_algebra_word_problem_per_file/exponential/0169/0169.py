"""Algebra word problem 0169   [Exponential]

Problem : A bacteria culture starts with 300 cells and doubles every 4 hours. When will it reach 4,800 cells?
Let     : t = hours
Equation: 300 × 2^(t/4) = 4800
Solve   : 2^(t/4) = 16 = 2^4 → t/4 = 4 → t = 16
Answer  : 16 hours

Status  : ready: periodic_growth answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0169'
KEY = 'exponential/0169'
NAME = 'Exponential 0169'
CATEGORY = 'Exponential'
PROBLEM = 'A bacteria culture starts with 300 cells and doubles every 4 hours. When will it reach 4,800 cells?'
LET = 't = hours'
EQUATION = '300 × 2^(t/4) = 4800'
SOLVE = '2^(t/4) = 16 = 2^4 → t/4 = 4 → t = 16'
ANSWER = '16 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'periodic_growth'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A bacteria culture starts with {0} cells and doubles every {1} hours. When will it reach {2} cells?'
NUMBERS = ['300', '4', '4800']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
