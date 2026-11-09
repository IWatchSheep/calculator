"""Algebra word problem 0016   [Average]

Problem : Mateo scored 60, 94, 80, 60, 98, 62 on 6 tests. What score is needed on the next test to average 76?
Let     : x = next score
Equation: (60 + 94 + 80 + 60 + 98 + 62 + x) / 7 = 76
Solve   : 454 + x = 532 → x = 78
Answer  : 78

Status  : ready: average_needed answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0016'
KEY = 'average/0016'
NAME = 'Average 0016'
CATEGORY = 'Average'
PROBLEM = 'Mateo scored 60, 94, 80, 60, 98, 62 on 6 tests. What score is needed on the next test to average 76?'
LET = 'x = next score'
EQUATION = '(60 + 94 + 80 + 60 + 98 + 62 + x) / 7 = 76'
SOLVE = '454 + x = 532 → x = 78'
ANSWER = '78'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'average_needed'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Mateo scored {0}, {1}, {2}, {3}, {4}, {5} on {6} tests. What score is needed on the next test to average {7}?'
NUMBERS = ['60', '94', '80', '60', '98', '62', '6', '76']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
