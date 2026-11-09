"""Algebra word problem 0005   [Age]

Problem : Uma is 3 times as old as Yusuf. In 10 years, the sum of their ages will be 68. How old is each now?
Let     : x = Yusuf's age now; Uma = 3x
Equation: (x + 10) + (3x + 10) = 68
Solve   : 4x + 20 = 68 → x = 12
Answer  : Yusuf is 12, Uma is 36

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0005'
KEY = 'age/0005'
NAME = 'Age 0005'
CATEGORY = 'Age'
PROBLEM = 'Uma is 3 times as old as Yusuf. In 10 years, the sum of their ages will be 68. How old is each now?'
LET = "x = Yusuf's age now; Uma = 3x"
EQUATION = '(x + 10) + (3x + 10) = 68'
SOLVE = '4x + 20 = 68 → x = 12'
ANSWER = 'Yusuf is 12, Uma is 36'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Uma is {0} times as old as Yusuf. In {1} years, the sum of their ages will be {2}. How old is each now?'
NUMBERS = ['3', '10', '68']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
