"""Algebra word problem 0561   [Mixture]

Problem : How many liters of a 50% alcohol solution must be mixed with a 60% alcohol solution to make 30 liters of a 54% alcohol solution?
Let     : x = liters of 50%; 30 − x = liters of 60%
Equation: 0.5x + 0.6(30 − x) = 0.54(30)
Solve   : 0.1x = 1.8 → x = 18
Answer  : 18 L of the 50% and 12 L of the 60%

Status  : ready: two_solution_mix answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0561'
KEY = 'mixture/0561'
NAME = 'Mixture 0561'
CATEGORY = 'Mixture'
PROBLEM = 'How many liters of a 50% alcohol solution must be mixed with a 60% alcohol solution to make 30 liters of a 54% alcohol solution?'
LET = 'x = liters of 50%; 30 − x = liters of 60%'
EQUATION = '0.5x + 0.6(30 − x) = 0.54(30)'
SOLVE = '0.1x = 1.8 → x = 18'
ANSWER = '18 L of the 50% and 12 L of the 60%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_solution_mix'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many liters of a {0}% alcohol solution must be mixed with a {1}% alcohol solution to make {2} liters of a {3}% alcohol solution?'
NUMBERS = ['50', '60', '30', '54']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
