"""Algebra word problem 0463   [Linear cost]

Problem : A parking garage charges $3 for the first hour and $3.00 for each additional hour. A driver paid $15.00. How many hours did they park?
Let     : h = total hours
Equation: 3 + 3(h − 1) = 15
Solve   : 3h = 15 → h = 5
Answer  : 5 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0463'
KEY = 'linear_cost/0463'
NAME = 'Linear cost 0463'
CATEGORY = 'Linear cost'
PROBLEM = 'A parking garage charges $3 for the first hour and $3.00 for each additional hour. A driver paid $15.00. How many hours did they park?'
LET = 'h = total hours'
EQUATION = '3 + 3(h − 1) = 15'
SOLVE = '3h = 15 → h = 5'
ANSWER = '5 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A parking garage charges ${0} for the first hour and ${1} for each additional hour. A driver paid ${2}. How many hours did they park?'
NUMBERS = ['3', '3.00', '15.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
