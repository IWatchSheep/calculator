"""Algebra word problem 0011   [Average]

Problem : Ava scored 87, 71, 73, 89, 97 on 5 tests. What score is needed on the next test to average 86?
Let     : x = next score
Equation: (87 + 71 + 73 + 89 + 97 + x) / 6 = 86
Solve   : 417 + x = 516 → x = 99
Answer  : 99

Status  : ready: average_needed answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0011'
KEY = 'average/0011'
NAME = 'Average 0011'
CATEGORY = 'Average'
PROBLEM = 'Ava scored 87, 71, 73, 89, 97 on 5 tests. What score is needed on the next test to average 86?'
LET = 'x = next score'
EQUATION = '(87 + 71 + 73 + 89 + 97 + x) / 6 = 86'
SOLVE = '417 + x = 516 → x = 99'
ANSWER = '99'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'average_needed'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Ava scored {0}, {1}, {2}, {3}, {4} on {5} tests. What score is needed on the next test to average {6}?'
NUMBERS = ['87', '71', '73', '89', '97', '5', '86']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
