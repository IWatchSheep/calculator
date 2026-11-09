"""Algebra word problem 0014   [Average]

Problem : Tara scored 94, 77, 83, 85, 92, 73 on 6 tests. What score is needed on the next test to average 86?
Let     : x = next score
Equation: (94 + 77 + 83 + 85 + 92 + 73 + x) / 7 = 86
Solve   : 504 + x = 602 → x = 98
Answer  : 98

Status  : ready: average_needed answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0014'
KEY = 'average/0014'
NAME = 'Average 0014'
CATEGORY = 'Average'
PROBLEM = 'Tara scored 94, 77, 83, 85, 92, 73 on 6 tests. What score is needed on the next test to average 86?'
LET = 'x = next score'
EQUATION = '(94 + 77 + 83 + 85 + 92 + 73 + x) / 7 = 86'
SOLVE = '504 + x = 602 → x = 98'
ANSWER = '98'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'average_needed'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Tara scored {0}, {1}, {2}, {3}, {4}, {5} on {6} tests. What score is needed on the next test to average {7}?'
NUMBERS = ['94', '77', '83', '85', '92', '73', '6', '86']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
