"""Algebra word problem 0004   [Age]

Problem : Dana is 2 times as old as Aiden. In 6 years, the sum of their ages will be 33. How old is each now?
Let     : x = Aiden's age now; Dana = 2x
Equation: (x + 6) + (2x + 6) = 33
Solve   : 3x + 12 = 33 → x = 7
Answer  : Aiden is 7, Dana is 14

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0004'
KEY = 'age/0004'
NAME = 'Age 0004'
CATEGORY = 'Age'
PROBLEM = 'Dana is 2 times as old as Aiden. In 6 years, the sum of their ages will be 33. How old is each now?'
LET = "x = Aiden's age now; Dana = 2x"
EQUATION = '(x + 6) + (2x + 6) = 33'
SOLVE = '3x + 12 = 33 → x = 7'
ANSWER = 'Aiden is 7, Dana is 14'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Dana is {0} times as old as Aiden. In {1} years, the sum of their ages will be {2}. How old is each now?'
NUMBERS = ['2', '6', '33']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
