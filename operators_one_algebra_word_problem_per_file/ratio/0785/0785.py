"""Algebra word problem 0785   [Ratio]

Problem : A 105 cm board is cut into two pieces. One piece is 7 cm longer than the other. How long is each piece?
Let     : x = shorter piece
Equation: x + (x + 7) = 105
Solve   : 2x = 98 → x = 49
Answer  : 49 cm and 56 cm

Status  : ready: sum_difference answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0785'
KEY = 'ratio/0785'
NAME = 'Ratio 0785'
CATEGORY = 'Ratio'
PROBLEM = 'A 105 cm board is cut into two pieces. One piece is 7 cm longer than the other. How long is each piece?'
LET = 'x = shorter piece'
EQUATION = 'x + (x + 7) = 105'
SOLVE = '2x = 98 → x = 49'
ANSWER = '49 cm and 56 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'sum_difference'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} cm board is cut into two pieces. One piece is {1} cm longer than the other. How long is each piece?'
NUMBERS = ['105', '7']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
