"""Algebra word problem 0931   [System of equations]

Problem : Kira is 4 times as old as Ava. In 8 years, Kira will be 2 times as old as Ava. How old is each now?
Let     : p = Kira's age, c = Ava's age
Equation: p = 4c;  p + 8 = 2(c + 8)
Solve   : Substitute p = 4c → p = 16, c = 4
Answer  : Kira 16, Ava 4

Status  : ready: ages_later_multiple answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0931'
KEY = 'system_of_equations/0931'
NAME = 'System of equations 0931'
CATEGORY = 'System of equations'
PROBLEM = 'Kira is 4 times as old as Ava. In 8 years, Kira will be 2 times as old as Ava. How old is each now?'
LET = "p = Kira's age, c = Ava's age"
EQUATION = 'p = 4c;  p + 8 = 2(c + 8)'
SOLVE = 'Substitute p = 4c → p = 16, c = 4'
ANSWER = 'Kira 16, Ava 4'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'ages_later_multiple'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Kira is {0} times as old as Ava. In {1} years, Kira will be {2} times as old as Ava. How old is each now?'
NUMBERS = ['4', '8', '2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
