"""Algebra word problem 0518   [Linear model]

Problem : Town A has 32,000 people and grows by 2600 a year. Town B has 70,000 people and shrinks by 1200 a year. In how many years will they be equal?
Let     : y = years
Equation: 32000 + 2600y = 70000 − 1200y
Solve   : 3800y = 38000 → y = 10
Answer  : 10 years

Status  : ready: two_changing_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0518'
KEY = 'linear_model/0518'
NAME = 'Linear model 0518'
CATEGORY = 'Linear model'
PROBLEM = 'Town A has 32,000 people and grows by 2600 a year. Town B has 70,000 people and shrinks by 1200 a year. In how many years will they be equal?'
LET = 'y = years'
EQUATION = '32000 + 2600y = 70000 − 1200y'
SOLVE = '3800y = 38000 → y = 10'
ANSWER = '10 years'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_changing_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Town A has {0} people and grows by {1} a year. Town B has {2} people and shrinks by {3} a year. In how many years will they be equal?'
NUMBERS = ['32000', '2600', '70000', '1200']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
