"""Algebra word problem 0885   [System of equations]

Problem : Jade is 5 times as old as Emeka. In 5 years, Jade will be 4 times as old as Emeka. How old is each now?
Let     : p = Jade's age, c = Emeka's age
Equation: p = 5c;  p + 5 = 4(c + 5)
Solve   : Substitute p = 5c → p = 75, c = 15
Answer  : Jade 75, Emeka 15

Status  : ready: ages_later_multiple answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0885'
KEY = 'system_of_equations/0885'
NAME = 'System of equations 0885'
CATEGORY = 'System of equations'
PROBLEM = 'Jade is 5 times as old as Emeka. In 5 years, Jade will be 4 times as old as Emeka. How old is each now?'
LET = "p = Jade's age, c = Emeka's age"
EQUATION = 'p = 5c;  p + 5 = 4(c + 5)'
SOLVE = 'Substitute p = 5c → p = 75, c = 15'
ANSWER = 'Jade 75, Emeka 15'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'ages_later_multiple'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Jade is {0} times as old as Emeka. In {1} years, Jade will be {2} times as old as Emeka. How old is each now?'
NUMBERS = ['5', '5', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
