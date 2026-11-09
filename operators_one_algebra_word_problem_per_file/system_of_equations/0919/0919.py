"""Algebra word problem 0919   [System of equations]

Problem : A basketball team scored 61 points from 30 field goals, all 2-pointers and 3-pointers. How many of each?
Let     : x = 2-pointers, y = 3-pointers
Equation: x + y = 30;  2x + 3y = 61
Solve   : Solve by elimination → x = 29, y = 1
Answer  : 29 two-pointers, 1 three-pointers

Status  : ready: two_scores answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0919'
KEY = 'system_of_equations/0919'
NAME = 'System of equations 0919'
CATEGORY = 'System of equations'
PROBLEM = 'A basketball team scored 61 points from 30 field goals, all 2-pointers and 3-pointers. How many of each?'
LET = 'x = 2-pointers, y = 3-pointers'
EQUATION = 'x + y = 30;  2x + 3y = 61'
SOLVE = 'Solve by elimination → x = 29, y = 1'
ANSWER = '29 two-pointers, 1 three-pointers'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_scores'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A basketball team scored {0} points from {1} field goals, all {2}-pointers and {3}-pointers. How many of each?'
NUMBERS = ['61', '30', '2', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
