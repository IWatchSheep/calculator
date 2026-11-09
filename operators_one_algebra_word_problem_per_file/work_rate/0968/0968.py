"""Algebra word problem 0968   [Work rate]

Problem : Gus, Rosa, and Bea can each paint a room alone in 12, 30, and 3 hours. How long will it take all three together?
Let     : t = hours together
Equation: t/12 + t/30 + t/3 = 1
Solve   : Combine rates: t(1/12 + 1/30 + 1/3) = 1 → t = 20/9
Answer  : 20/9 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0968'
KEY = 'work_rate/0968'
NAME = 'Work rate 0968'
CATEGORY = 'Work rate'
PROBLEM = 'Gus, Rosa, and Bea can each paint a room alone in 12, 30, and 3 hours. How long will it take all three together?'
LET = 't = hours together'
EQUATION = 't/12 + t/30 + t/3 = 1'
SOLVE = 'Combine rates: t(1/12 + 1/30 + 1/3) = 1 → t = 20/9'
ANSWER = '20/9 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Gus, Rosa, and Bea can each paint a room alone in {0}, {1}, and {2} hours. How long will it take all three together?'
NUMBERS = ['12', '30', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
