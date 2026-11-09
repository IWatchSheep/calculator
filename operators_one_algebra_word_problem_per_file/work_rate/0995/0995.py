"""Algebra word problem 0995   [Work rate]

Problem : Working together, Hiro and Nia can finish a job in 3 hours. Hiro alone takes 4 hours. How long would Nia take alone?
Let     : x = Nia's time alone
Equation: 3/4 + 3/x = 1
Solve   : 3/x = 1/4 → x = 12
Answer  : 12 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0995'
KEY = 'work_rate/0995'
NAME = 'Work rate 0995'
CATEGORY = 'Work rate'
PROBLEM = 'Working together, Hiro and Nia can finish a job in 3 hours. Hiro alone takes 4 hours. How long would Nia take alone?'
LET = "x = Nia's time alone"
EQUATION = '3/4 + 3/x = 1'
SOLVE = '3/x = 1/4 → x = 12'
ANSWER = '12 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Working together, Hiro and Nia can finish a job in {0} hours. Hiro alone takes {1} hours. How long would Nia take alone?'
NUMBERS = ['3', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
