"""Algebra word problem 0001   [Age]

Problem : Wren is 4 times as old as Jamal. In 5 years, the sum of their ages will be 105. How old is each now?
Let     : x = Jamal's age now; Wren = 4x
Equation: (x + 5) + (4x + 5) = 105
Solve   : 5x + 10 = 105 → x = 19
Answer  : Jamal is 19, Wren is 76

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0001'
KEY = 'age/0001'
NAME = 'Age 0001'
CATEGORY = 'Age'
PROBLEM = 'Wren is 4 times as old as Jamal. In 5 years, the sum of their ages will be 105. How old is each now?'
LET = "x = Jamal's age now; Wren = 4x"
EQUATION = '(x + 5) + (4x + 5) = 105'
SOLVE = '5x + 10 = 105 → x = 19'
ANSWER = 'Jamal is 19, Wren is 76'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Wren is {0} times as old as Jamal. In {1} years, the sum of their ages will be {2}. How old is each now?'
NUMBERS = ['4', '5', '105']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
