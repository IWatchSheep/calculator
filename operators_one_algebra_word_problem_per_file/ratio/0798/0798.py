"""Algebra word problem 0798   [Ratio]

Problem : A 69 cm board is cut into two pieces. One piece is 21 cm longer than the other. How long is each piece?
Let     : x = shorter piece
Equation: x + (x + 21) = 69
Solve   : 2x = 48 → x = 24
Answer  : 24 cm and 45 cm

Status  : ready: sum_difference answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0798'
KEY = 'ratio/0798'
NAME = 'Ratio 0798'
CATEGORY = 'Ratio'
PROBLEM = 'A 69 cm board is cut into two pieces. One piece is 21 cm longer than the other. How long is each piece?'
LET = 'x = shorter piece'
EQUATION = 'x + (x + 21) = 69'
SOLVE = '2x = 48 → x = 24'
ANSWER = '24 cm and 45 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'sum_difference'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} cm board is cut into two pieces. One piece is {1} cm longer than the other. How long is each piece?'
NUMBERS = ['69', '21']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
