"""Algebra word problem 0920   [System of equations]

Problem : A farm has chickens and pigs. There are 48 heads and 138 legs. How many of each are there?
Let     : x = chickens, y = pigs
Equation: x + y = 48;  2x + 4y = 138
Solve   : 2x + 4(48 − x) = 138 → x = 27, y = 21
Answer  : 27 chickens and 21 pigs

Status  : ready: heads_and_feet answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0920'
KEY = 'system_of_equations/0920'
NAME = 'System of equations 0920'
CATEGORY = 'System of equations'
PROBLEM = 'A farm has chickens and pigs. There are 48 heads and 138 legs. How many of each are there?'
LET = 'x = chickens, y = pigs'
EQUATION = 'x + y = 48;  2x + 4y = 138'
SOLVE = '2x + 4(48 − x) = 138 → x = 27, y = 21'
ANSWER = '27 chickens and 21 pigs'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'heads_and_feet'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A farm has chickens and pigs. There are {0} heads and {1} legs. How many of each are there?'
NUMBERS = ['48', '138']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
