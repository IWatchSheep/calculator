"""Algebra word problem 0800   [Ratio]

Problem : A 40 m rope is cut into two pieces in the ratio 2:3. How long is each piece?
Let     : x = scale factor
Equation: 2x + 3x = 40
Solve   : 5x = 40 → x = 8
Answer  : 16 m and 24 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0800'
KEY = 'ratio/0800'
NAME = 'Ratio 0800'
CATEGORY = 'Ratio'
PROBLEM = 'A 40 m rope is cut into two pieces in the ratio 2:3. How long is each piece?'
LET = 'x = scale factor'
EQUATION = '2x + 3x = 40'
SOLVE = '5x = 40 → x = 8'
ANSWER = '16 m and 24 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} m rope is cut into two pieces in the ratio {1}:{2}. How long is each piece?'
NUMBERS = ['40', '2', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
