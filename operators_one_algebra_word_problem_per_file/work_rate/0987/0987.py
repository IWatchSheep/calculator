"""Algebra word problem 0987   [Work rate]

Problem : Working together, Gus and Sam can finish a job in 3 hours. Gus alone takes 6 hours. How long would Sam take alone?
Let     : x = Sam's time alone
Equation: 3/6 + 3/x = 1
Solve   : 3/x = 1/2 → x = 6
Answer  : 6 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0987'
KEY = 'work_rate/0987'
NAME = 'Work rate 0987'
CATEGORY = 'Work rate'
PROBLEM = 'Working together, Gus and Sam can finish a job in 3 hours. Gus alone takes 6 hours. How long would Sam take alone?'
LET = "x = Sam's time alone"
EQUATION = '3/6 + 3/x = 1'
SOLVE = '3/x = 1/2 → x = 6'
ANSWER = '6 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Working together, Gus and Sam can finish a job in {0} hours. Gus alone takes {1} hours. How long would Sam take alone?'
NUMBERS = ['3', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
