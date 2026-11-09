"""Algebra word problem 0796   [Ratio]

Problem : A 48 m rope is cut into two pieces in the ratio 5:1. How long is each piece?
Let     : x = scale factor
Equation: 5x + x = 48
Solve   : 6x = 48 → x = 8
Answer  : 40 m and 8 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0796'
KEY = 'ratio/0796'
NAME = 'Ratio 0796'
CATEGORY = 'Ratio'
PROBLEM = 'A 48 m rope is cut into two pieces in the ratio 5:1. How long is each piece?'
LET = 'x = scale factor'
EQUATION = '5x + x = 48'
SOLVE = '6x = 48 → x = 8'
ANSWER = '40 m and 8 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} m rope is cut into two pieces in the ratio {1}:{2}. How long is each piece?'
NUMBERS = ['48', '5', '1']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
