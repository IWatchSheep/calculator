"""Algebra word problem 0755   [Quadratic (counting)]

Problem : At a party everyone shook hands with everyone else exactly once, for 10 handshakes. How many people were there?
Let     : n = number of people/teams
Equation: n(n − 1)/2 = 10
Solve   : n² − n − 20 = 0 → n = 5 (the other root, -4, is rejected)
Answer  : 5

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0755'
KEY = 'quadratic_counting/0755'
NAME = 'Quadratic (counting) 0755'
CATEGORY = 'Quadratic (counting)'
PROBLEM = 'At a party everyone shook hands with everyone else exactly once, for 10 handshakes. How many people were there?'
LET = 'n = number of people/teams'
EQUATION = 'n(n − 1)/2 = 10'
SOLVE = 'n² − n − 20 = 0 → n = 5 (the other root, -4, is rejected)'
ANSWER = '5'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'At a party everyone shook hands with everyone else exactly once, for {0} handshakes. How many people were there?'
NUMBERS = ['10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
