"""Algebra word problem 0757   [Quadratic (counting)]

Problem : In a round-robin tournament each team plays every other team once, for 45 games. How many teams are there?
Let     : n = number of people/teams
Equation: n(n − 1)/2 = 45
Solve   : n² − n − 90 = 0 → n = 10 (the other root, -9, is rejected)
Answer  : 10

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0757'
KEY = 'quadratic_counting/0757'
NAME = 'Quadratic (counting) 0757'
CATEGORY = 'Quadratic (counting)'
PROBLEM = 'In a round-robin tournament each team plays every other team once, for 45 games. How many teams are there?'
LET = 'n = number of people/teams'
EQUATION = 'n(n − 1)/2 = 45'
SOLVE = 'n² − n − 90 = 0 → n = 10 (the other root, -9, is rejected)'
ANSWER = '10'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'In a round-robin tournament each team plays every other team once, for {0} games. How many teams are there?'
NUMBERS = ['45']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
