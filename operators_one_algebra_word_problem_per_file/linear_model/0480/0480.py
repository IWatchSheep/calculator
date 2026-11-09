"""Algebra word problem 0480   [Linear model]

Problem : Town A has 18,000 people and grows by 2000 a year. Town B has 63,000 people and shrinks by 500 a year. In how many years will they be equal?
Let     : y = years
Equation: 18000 + 2000y = 63000 − 500y
Solve   : 2500y = 45000 → y = 18
Answer  : 18 years

Status  : ready: two_changing_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0480'
KEY = 'linear_model/0480'
NAME = 'Linear model 0480'
CATEGORY = 'Linear model'
PROBLEM = 'Town A has 18,000 people and grows by 2000 a year. Town B has 63,000 people and shrinks by 500 a year. In how many years will they be equal?'
LET = 'y = years'
EQUATION = '18000 + 2000y = 63000 − 500y'
SOLVE = '2500y = 45000 → y = 18'
ANSWER = '18 years'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_changing_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Town A has {0} people and grows by {1} a year. Town B has {2} people and shrinks by {3} a year. In how many years will they be equal?'
NUMBERS = ['18000', '2000', '63000', '500']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
