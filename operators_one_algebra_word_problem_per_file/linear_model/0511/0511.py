"""Algebra word problem 0511   [Linear model]

Problem : Town A has 40,000 people and grows by 1000 a year. Town B has 49,000 people and shrinks by 800 a year. In how many years will they be equal?
Let     : y = years
Equation: 40000 + 1000y = 49000 − 800y
Solve   : 1800y = 9000 → y = 5
Answer  : 5 years

Status  : ready: two_changing_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0511'
KEY = 'linear_model/0511'
NAME = 'Linear model 0511'
CATEGORY = 'Linear model'
PROBLEM = 'Town A has 40,000 people and grows by 1000 a year. Town B has 49,000 people and shrinks by 800 a year. In how many years will they be equal?'
LET = 'y = years'
EQUATION = '40000 + 1000y = 49000 − 800y'
SOLVE = '1800y = 9000 → y = 5'
ANSWER = '5 years'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_changing_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Town A has {0} people and grows by {1} a year. Town B has {2} people and shrinks by {3} a year. In how many years will they be equal?'
NUMBERS = ['40000', '1000', '49000', '800']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
