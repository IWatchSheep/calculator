"""Algebra word problem 0797   [Ratio]

Problem : A mix uses flour, sugar, and butter in the ratio 5:1:2. The total is 32 g. How much of each is used?
Let     : k = one part
Equation: 5k + k + 2k = 32
Solve   : 8k = 32 → k = 4
Answer  : 20, 4, 8 g

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0797'
KEY = 'ratio/0797'
NAME = 'Ratio 0797'
CATEGORY = 'Ratio'
PROBLEM = 'A mix uses flour, sugar, and butter in the ratio 5:1:2. The total is 32 g. How much of each is used?'
LET = 'k = one part'
EQUATION = '5k + k + 2k = 32'
SOLVE = '8k = 32 → k = 4'
ANSWER = '20, 4, 8 g'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A mix uses flour, sugar, and butter in the ratio {0}:{1}:{2}. The total is {3} g. How much of each is used?'
NUMBERS = ['5', '1', '2', '32']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
