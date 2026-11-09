"""Algebra word problem 0007   [Age]

Problem : Noah is 3 times as old as Ava. In 3 years, the sum of their ages will be 82. How old is each now?
Let     : x = Ava's age now; Noah = 3x
Equation: (x + 3) + (3x + 3) = 82
Solve   : 4x + 6 = 82 → x = 19
Answer  : Ava is 19, Noah is 57

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0007'
KEY = 'age/0007'
NAME = 'Age 0007'
CATEGORY = 'Age'
PROBLEM = 'Noah is 3 times as old as Ava. In 3 years, the sum of their ages will be 82. How old is each now?'
LET = "x = Ava's age now; Noah = 3x"
EQUATION = '(x + 3) + (3x + 3) = 82'
SOLVE = '4x + 6 = 82 → x = 19'
ANSWER = 'Ava is 19, Noah is 57'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Noah is {0} times as old as Ava. In {1} years, the sum of their ages will be {2}. How old is each now?'
NUMBERS = ['3', '3', '82']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
