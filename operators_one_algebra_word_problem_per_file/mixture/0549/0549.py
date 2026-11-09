"""Algebra word problem 0549   [Mixture]

Problem : How many liters of a 40% acid solution must be mixed with a 70% acid solution to make 50 liters of a 65.8% acid solution?
Let     : x = liters of 40%; 50 − x = liters of 70%
Equation: 0.4x + 0.7(50 − x) = 0.658(50)
Solve   : 0.3x = 2.1 → x = 7
Answer  : 7 L of the 40% and 43 L of the 70%

Status  : ready: two_solution_mix answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0549'
KEY = 'mixture/0549'
NAME = 'Mixture 0549'
CATEGORY = 'Mixture'
PROBLEM = 'How many liters of a 40% acid solution must be mixed with a 70% acid solution to make 50 liters of a 65.8% acid solution?'
LET = 'x = liters of 40%; 50 − x = liters of 70%'
EQUATION = '0.4x + 0.7(50 − x) = 0.658(50)'
SOLVE = '0.3x = 2.1 → x = 7'
ANSWER = '7 L of the 40% and 43 L of the 70%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_solution_mix'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many liters of a {0}% acid solution must be mixed with a {1}% acid solution to make {2} liters of a {3}% acid solution?'
NUMBERS = ['40', '70', '50', '65.8']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
