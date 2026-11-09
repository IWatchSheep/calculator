"""Algebra word problem 0379   [Inequality]

Problem : Emeka's test scores are 92, 93, 72, 74, 93. What is the lowest score on the next test that gives an average of at least 85?
Let     : x = next score
Equation: (92 + 93 + 72 + 74 + 93 + x)/6 ≥ 85
Solve   : x ≥ 86 → x = 86 (smallest whole number that works)
Answer  : 86

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0379'
KEY = 'inequality/0379'
NAME = 'Inequality 0379'
CATEGORY = 'Inequality'
PROBLEM = "Emeka's test scores are 92, 93, 72, 74, 93. What is the lowest score on the next test that gives an average of at least 85?"
LET = 'x = next score'
EQUATION = '(92 + 93 + 72 + 74 + 93 + x)/6 ≥ 85'
SOLVE = 'x ≥ 86 → x = 86 (smallest whole number that works)'
ANSWER = '86'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "Emeka's test scores are {0}, {1}, {2}, {3}, {4}. What is the lowest score on the next test that gives an average of at least {5}?"
NUMBERS = ['92', '93', '72', '74', '93', '85']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
