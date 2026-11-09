"""Algebra word problem 0054   [Clock]

Problem : At what time between 9:00 and 10:00 are the hour and minute hands of a clock exactly together?
Let     : m = minutes after 9:00
Equation: 6m = 270 + 0.5m
Solve   : 5.5m = 270 → m = 540/11
Answer  : 540/11 ≈ 49.09 minutes after 9:00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0054'
KEY = 'clock/0054'
NAME = 'Clock 0054'
CATEGORY = 'Clock'
PROBLEM = 'At what time between 9:00 and 10:00 are the hour and minute hands of a clock exactly together?'
LET = 'm = minutes after 9:00'
EQUATION = '6m = 270 + 0.5m'
SOLVE = '5.5m = 270 → m = 540/11'
ANSWER = '540/11 ≈ 49.09 minutes after 9:00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'At what time between {0}:{1} and {2}:{3} are the hour and minute hands of a clock exactly together?'
NUMBERS = ['9', '00', '10', '00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
