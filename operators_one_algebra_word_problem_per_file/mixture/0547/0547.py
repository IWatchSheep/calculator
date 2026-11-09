"""Algebra word problem 0547   [Mixture]

Problem : How many liters of a 60% acid solution must be mixed with a 70% acid solution to make 40 liters of a 65% acid solution?
Let     : x = liters of 60%; 40 − x = liters of 70%
Equation: 0.6x + 0.7(40 − x) = 0.65(40)
Solve   : 0.1x = 2 → x = 20
Answer  : 20 L of the 60% and 20 L of the 70%

Status  : ready: two_solution_mix answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0547'
KEY = 'mixture/0547'
NAME = 'Mixture 0547'
CATEGORY = 'Mixture'
PROBLEM = 'How many liters of a 60% acid solution must be mixed with a 70% acid solution to make 40 liters of a 65% acid solution?'
LET = 'x = liters of 60%; 40 − x = liters of 70%'
EQUATION = '0.6x + 0.7(40 − x) = 0.65(40)'
SOLVE = '0.1x = 2 → x = 20'
ANSWER = '20 L of the 60% and 20 L of the 70%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_solution_mix'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many liters of a {0}% acid solution must be mixed with a {1}% acid solution to make {2} liters of a {3}% acid solution?'
NUMBERS = ['60', '70', '40', '65']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
