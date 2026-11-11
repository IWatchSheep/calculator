"""Algebra word problem 0978   [Work rate]

Problem : Quinn, Jamal, and Sam can each paint a room alone in 24, 20, and 30 hours. How long will it take all three together?
Let     : t = hours together
Equation: t/24 + t/20 + t/30 = 1
Solve   : Combine rates: t(1/24 + 1/20 + 1/30) = 1 → t = 8
Answer  : 8 hours

Status  : ready: three_painters_together answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0978'
KEY = 'work_rate/0978'
NAME = 'Work rate 0978'
CATEGORY = 'Work rate'
PROBLEM = 'Quinn, Jamal, and Sam can each paint a room alone in 24, 20, and 30 hours. How long will it take all three together?'
LET = 't = hours together'
EQUATION = 't/24 + t/20 + t/30 = 1'
SOLVE = 'Combine rates: t(1/24 + 1/20 + 1/30) = 1 → t = 8'
ANSWER = '8 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'three_painters_together'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Quinn, Jamal, and Sam can each paint a room alone in {0}, {1}, and {2} hours. How long will it take all three together?'
NUMBERS = ['24', '20', '30']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
