"""Algebra word problem 0190   [Formula]

Problem : Solve P = 2l + 2w for w when P = 138 and l = 65.
Let     : w = width
Equation: 2(65) + 2w = 138
Solve   : 2w = 8 → w = 4
Answer  : 4

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0190'
KEY = 'formula/0190'
NAME = 'Formula 0190'
CATEGORY = 'Formula'
PROBLEM = 'Solve P = 2l + 2w for w when P = 138 and l = 65.'
LET = 'w = width'
EQUATION = '2(65) + 2w = 138'
SOLVE = '2w = 8 → w = 4'
ANSWER = '4'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Solve P = {0}l + {1}w for w when P = {2} and l = {3}.'
NUMBERS = ['2', '2', '138', '65']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
