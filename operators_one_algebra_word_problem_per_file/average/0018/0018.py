"""Algebra word problem 0018   [Average]

Problem : Maya scored 62, 75, 94 on 3 tests. What score is needed on the next test to average 79?
Let     : x = next score
Equation: (62 + 75 + 94 + x) / 4 = 79
Solve   : 231 + x = 316 → x = 85
Answer  : 85

Status  : ready: average_needed answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0018'
KEY = 'average/0018'
NAME = 'Average 0018'
CATEGORY = 'Average'
PROBLEM = 'Maya scored 62, 75, 94 on 3 tests. What score is needed on the next test to average 79?'
LET = 'x = next score'
EQUATION = '(62 + 75 + 94 + x) / 4 = 79'
SOLVE = '231 + x = 316 → x = 85'
ANSWER = '85'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'average_needed'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Maya scored {0}, {1}, {2} on {3} tests. What score is needed on the next test to average {4}?'
NUMBERS = ['62', '75', '94', '3', '79']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
