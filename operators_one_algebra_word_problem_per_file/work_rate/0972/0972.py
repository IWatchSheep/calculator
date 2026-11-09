"""Algebra word problem 0972   [Work rate]

Problem : Working together, Noah and Victor can finish a job in 6 hours. Noah alone takes 12 hours. How long would Victor take alone?
Let     : x = Victor's time alone
Equation: 6/12 + 6/x = 1
Solve   : 6/x = 1/2 → x = 12
Answer  : 12 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0972'
KEY = 'work_rate/0972'
NAME = 'Work rate 0972'
CATEGORY = 'Work rate'
PROBLEM = 'Working together, Noah and Victor can finish a job in 6 hours. Noah alone takes 12 hours. How long would Victor take alone?'
LET = "x = Victor's time alone"
EQUATION = '6/12 + 6/x = 1'
SOLVE = '6/x = 1/2 → x = 12'
ANSWER = '12 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Working together, Noah and Victor can finish a job in {0} hours. Noah alone takes {1} hours. How long would Victor take alone?'
NUMBERS = ['6', '12']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
