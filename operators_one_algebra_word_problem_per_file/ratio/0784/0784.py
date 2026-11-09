"""Algebra word problem 0784   [Ratio]

Problem : A 10 m rope is cut into two pieces in the ratio 1:4. How long is each piece?
Let     : x = scale factor
Equation: x + 4x = 10
Solve   : 5x = 10 → x = 2
Answer  : 2 m and 8 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0784'
KEY = 'ratio/0784'
NAME = 'Ratio 0784'
CATEGORY = 'Ratio'
PROBLEM = 'A 10 m rope is cut into two pieces in the ratio 1:4. How long is each piece?'
LET = 'x = scale factor'
EQUATION = 'x + 4x = 10'
SOLVE = '5x = 10 → x = 2'
ANSWER = '2 m and 8 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} m rope is cut into two pieces in the ratio {1}:{2}. How long is each piece?'
NUMBERS = ['10', '1', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
