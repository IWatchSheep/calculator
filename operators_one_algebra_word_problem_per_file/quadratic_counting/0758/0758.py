"""Algebra word problem 0758   [Quadratic (counting)]

Problem : In a round-robin tournament each team plays every other team once, for 561 games. How many teams are there?
Let     : n = number of people/teams
Equation: n(n − 1)/2 = 561
Solve   : n² − n − 1122 = 0 → n = 34 (the other root, -33, is rejected)
Answer  : 34

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0758'
KEY = 'quadratic_counting/0758'
NAME = 'Quadratic (counting) 0758'
CATEGORY = 'Quadratic (counting)'
PROBLEM = 'In a round-robin tournament each team plays every other team once, for 561 games. How many teams are there?'
LET = 'n = number of people/teams'
EQUATION = 'n(n − 1)/2 = 561'
SOLVE = 'n² − n − 1122 = 0 → n = 34 (the other root, -33, is rejected)'
ANSWER = '34'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'In a round-robin tournament each team plays every other team once, for {0} games. How many teams are there?'
NUMBERS = ['561']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
