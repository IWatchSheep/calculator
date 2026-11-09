"""Algebra word problem 0003   [Age]

Problem : Ben is 8 years older than Sam. 32 years ago, Ben was twice as old as Sam. How old is each now?
Let     : x = Sam's age now
Equation: (x + 8) − 32 = 2(x − 32)
Solve   : x + -24 = 2x − 64 → x = 40
Answer  : Sam is 40, Ben is 48

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0003'
KEY = 'age/0003'
NAME = 'Age 0003'
CATEGORY = 'Age'
PROBLEM = 'Ben is 8 years older than Sam. 32 years ago, Ben was twice as old as Sam. How old is each now?'
LET = "x = Sam's age now"
EQUATION = '(x + 8) − 32 = 2(x − 32)'
SOLVE = 'x + -24 = 2x − 64 → x = 40'
ANSWER = 'Sam is 40, Ben is 48'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Ben is {0} years older than Sam. {1} years ago, Ben was twice as old as Sam. How old is each now?'
NUMBERS = ['8', '32']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
