"""Algebra word problem 0013   [Average]

Problem : Oscar scored 93, 81, 67, 64 on 4 tests. What score is needed on the next test to average 79?
Let     : x = next score
Equation: (93 + 81 + 67 + 64 + x) / 5 = 79
Solve   : 305 + x = 395 → x = 90
Answer  : 90

Status  : ready: average_needed answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0013'
KEY = 'average/0013'
NAME = 'Average 0013'
CATEGORY = 'Average'
PROBLEM = 'Oscar scored 93, 81, 67, 64 on 4 tests. What score is needed on the next test to average 79?'
LET = 'x = next score'
EQUATION = '(93 + 81 + 67 + 64 + x) / 5 = 79'
SOLVE = '305 + x = 395 → x = 90'
ANSWER = '90'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'average_needed'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Oscar scored {0}, {1}, {2}, {3} on {4} tests. What score is needed on the next test to average {5}?'
NUMBERS = ['93', '81', '67', '64', '4', '79']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
