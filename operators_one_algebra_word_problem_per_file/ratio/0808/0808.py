"""Algebra word problem 0808   [Ratio]

Problem : A mix uses red, blue, and yellow paint in the ratio 7:4:2. The total is 390 mL. How much of each is used?
Let     : k = one part
Equation: 7k + 4k + 2k = 390
Solve   : 13k = 390 → k = 30
Answer  : 210, 120, 60 mL

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0808'
KEY = 'ratio/0808'
NAME = 'Ratio 0808'
CATEGORY = 'Ratio'
PROBLEM = 'A mix uses red, blue, and yellow paint in the ratio 7:4:2. The total is 390 mL. How much of each is used?'
LET = 'k = one part'
EQUATION = '7k + 4k + 2k = 390'
SOLVE = '13k = 390 → k = 30'
ANSWER = '210, 120, 60 mL'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A mix uses red, blue, and yellow paint in the ratio {0}:{1}:{2}. The total is {3} mL. How much of each is used?'
NUMBERS = ['7', '4', '2', '390']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
