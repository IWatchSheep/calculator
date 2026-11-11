"""Algebra word problem 0970   [Work rate]

Problem : Working together, Rhea and Emeka can finish a job in 4 hours. Rhea alone takes 12 hours. How long would Emeka take alone?
Let     : x = Emeka's time alone
Equation: 4/12 + 4/x = 1
Solve   : 4/x = 2/3 → x = 6
Answer  : 6 hours

Status  : ready: partner_alone_from_together answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0970'
KEY = 'work_rate/0970'
NAME = 'Work rate 0970'
CATEGORY = 'Work rate'
PROBLEM = 'Working together, Rhea and Emeka can finish a job in 4 hours. Rhea alone takes 12 hours. How long would Emeka take alone?'
LET = "x = Emeka's time alone"
EQUATION = '4/12 + 4/x = 1'
SOLVE = '4/x = 2/3 → x = 6'
ANSWER = '6 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'partner_alone_from_together'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Working together, Rhea and Emeka can finish a job in {0} hours. Rhea alone takes {1} hours. How long would Emeka take alone?'
NUMBERS = ['4', '12']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
