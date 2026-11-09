"""Algebra word problem 0533   [Mixture]

Problem : How many liters of a 25% juice drink must be mixed with a 50% juice drink to make 100 liters of a 39% juice drink?
Let     : x = liters of 25%; 100 − x = liters of 50%
Equation: 0.25x + 0.5(100 − x) = 0.39(100)
Solve   : 0.25x = 11 → x = 44
Answer  : 44 L of the 25% and 56 L of the 50%

Status  : ready: two_solution_mix answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0533'
KEY = 'mixture/0533'
NAME = 'Mixture 0533'
CATEGORY = 'Mixture'
PROBLEM = 'How many liters of a 25% juice drink must be mixed with a 50% juice drink to make 100 liters of a 39% juice drink?'
LET = 'x = liters of 25%; 100 − x = liters of 50%'
EQUATION = '0.25x + 0.5(100 − x) = 0.39(100)'
SOLVE = '0.25x = 11 → x = 44'
ANSWER = '44 L of the 25% and 56 L of the 50%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_solution_mix'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'How many liters of a {0}% juice drink must be mixed with a {1}% juice drink to make {2} liters of a {3}% juice drink?'
NUMBERS = ['25', '50', '100', '39']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
