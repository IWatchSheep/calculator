"""Algebra word problem 0053   [Clock]

Problem : At what time between 1:00 and 2:00 are the hour and minute hands of a clock exactly together?
Let     : m = minutes after 1:00
Equation: 6m = 30 + 0.5m
Solve   : 5.5m = 30 → m = 60/11
Answer  : 60/11 ≈ 5.45 minutes after 1:00

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0053'
KEY = 'clock/0053'
NAME = 'Clock 0053'
CATEGORY = 'Clock'
PROBLEM = 'At what time between 1:00 and 2:00 are the hour and minute hands of a clock exactly together?'
LET = 'm = minutes after 1:00'
EQUATION = '6m = 30 + 0.5m'
SOLVE = '5.5m = 30 → m = 60/11'
ANSWER = '60/11 ≈ 5.45 minutes after 1:00'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'At what time between {0}:{1} and {2}:{3} are the hour and minute hands of a clock exactly together?'
NUMBERS = ['1', '00', '2', '00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
