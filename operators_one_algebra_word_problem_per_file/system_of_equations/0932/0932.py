"""Algebra word problem 0932   [System of equations]

Problem : A farm has spiders and beetles. There are 17 bugs and 110 legs. How many of each are there?
Let     : x = spiders, y = beetles
Equation: x + y = 17;  8x + 6y = 110
Solve   : 8x + 6(17 − x) = 110 → x = 4, y = 13
Answer  : 4 spiders and 13 beetles

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0932'
KEY = 'system_of_equations/0932'
NAME = 'System of equations 0932'
CATEGORY = 'System of equations'
PROBLEM = 'A farm has spiders and beetles. There are 17 bugs and 110 legs. How many of each are there?'
LET = 'x = spiders, y = beetles'
EQUATION = 'x + y = 17;  8x + 6y = 110'
SOLVE = '8x + 6(17 − x) = 110 → x = 4, y = 13'
ANSWER = '4 spiders and 13 beetles'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A farm has spiders and beetles. There are {0} bugs and {1} legs. How many of each are there?'
NUMBERS = ['17', '110']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
