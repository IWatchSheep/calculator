"""Algebra word problem 0397   [Inequality]

Problem : Gus's test scores are 61, 80, 75, 64. What is the lowest score on the next test that gives an average of at least 75?
Let     : x = next score
Equation: (61 + 80 + 75 + 64 + x)/5 ≥ 75
Solve   : x ≥ 95 → x = 95 (smallest whole number that works)
Answer  : 95

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0397'
KEY = 'inequality/0397'
NAME = 'Inequality 0397'
CATEGORY = 'Inequality'
PROBLEM = "Gus's test scores are 61, 80, 75, 64. What is the lowest score on the next test that gives an average of at least 75?"
LET = 'x = next score'
EQUATION = '(61 + 80 + 75 + 64 + x)/5 ≥ 75'
SOLVE = 'x ≥ 95 → x = 95 (smallest whole number that works)'
ANSWER = '95'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "Gus's test scores are {0}, {1}, {2}, {3}. What is the lowest score on the next test that gives an average of at least {4}?"
NUMBERS = ['61', '80', '75', '64', '75']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
