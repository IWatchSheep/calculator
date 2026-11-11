"""Algebra word problem 0458   [Linear cost]

Problem : A parking garage charges $4 for the first hour and $1.50 for each additional hour. A driver paid $20.50. How many hours did they park?
Let     : h = total hours
Equation: 4 + 1.5(h − 1) = 20.5
Solve   : 1.5h = 18 → h = 12
Answer  : 12 hours

Status  : ready: archive_linear_cost_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0458'
KEY = 'linear_cost/0458'
NAME = 'Linear cost 0458'
CATEGORY = 'Linear cost'
PROBLEM = 'A parking garage charges $4 for the first hour and $1.50 for each additional hour. A driver paid $20.50. How many hours did they park?'
LET = 'h = total hours'
EQUATION = '4 + 1.5(h − 1) = 20.5'
SOLVE = '1.5h = 18 → h = 12'
ANSWER = '12 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_linear_cost_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A parking garage charges ${0} for the first hour and ${1} for each additional hour. A driver paid ${2}. How many hours did they park?'
NUMBERS = ['4', '1.50', '20.50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
