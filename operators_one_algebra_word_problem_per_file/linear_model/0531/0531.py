"""Algebra word problem 0531   [Linear model]

Problem : Town A has 34,000 people and grows by 500 a year. Town B has 67,000 people and shrinks by 1000 a year. In how many years will they be equal?
Let     : y = years
Equation: 34000 + 500y = 67000 − 1000y
Solve   : 1500y = 33000 → y = 22
Answer  : 22 years

Status  : ready: two_changing_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0531'
KEY = 'linear_model/0531'
NAME = 'Linear model 0531'
CATEGORY = 'Linear model'
PROBLEM = 'Town A has 34,000 people and grows by 500 a year. Town B has 67,000 people and shrinks by 1000 a year. In how many years will they be equal?'
LET = 'y = years'
EQUATION = '34000 + 500y = 67000 − 1000y'
SOLVE = '1500y = 33000 → y = 22'
ANSWER = '22 years'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_changing_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Town A has {0} people and grows by {1} a year. Town B has {2} people and shrinks by {3} a year. In how many years will they be equal?'
NUMBERS = ['34000', '500', '67000', '1000']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
