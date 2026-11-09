"""Algebra word problem 0167   [Exponential]

Problem : A rumor spreads so that the number of people who have heard it triples every 4 days. It starts with 30 people. When will 810 people have heard it?
Let     : t = days
Equation: 30 × 3^(t/4) = 810
Solve   : 3^(t/4) = 27 → t/4 = 3 → t = 12
Answer  : 12 days

Status  : ready: periodic_growth answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0167'
KEY = 'exponential/0167'
NAME = 'Exponential 0167'
CATEGORY = 'Exponential'
PROBLEM = 'A rumor spreads so that the number of people who have heard it triples every 4 days. It starts with 30 people. When will 810 people have heard it?'
LET = 't = days'
EQUATION = '30 × 3^(t/4) = 810'
SOLVE = '3^(t/4) = 27 → t/4 = 3 → t = 12'
ANSWER = '12 days'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'periodic_growth'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rumor spreads so that the number of people who have heard it triples every {0} days. It starts with {1} people. When will {2} people have heard it?'
NUMBERS = ['4', '30', '810']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
