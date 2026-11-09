"""Algebra word problem 0616   [Percent]

Problem : In a two-candidate election, the winner got 58% of the votes and won by 3392 votes. How many votes were cast?
Let     : v = total votes
Equation: 0.58v − 0.42v = 3392
Solve   : 0.16v = 3392 → v = 21200
Answer  : 21,200 votes

Status  : ready: election_margin answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0616'
KEY = 'percent/0616'
NAME = 'Percent 0616'
CATEGORY = 'Percent'
PROBLEM = 'In a two-candidate election, the winner got 58% of the votes and won by 3392 votes. How many votes were cast?'
LET = 'v = total votes'
EQUATION = '0.58v − 0.42v = 3392'
SOLVE = '0.16v = 3392 → v = 21200'
ANSWER = '21,200 votes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'election_margin'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'In a two-candidate election, the winner got {0}% of the votes and won by {1} votes. How many votes were cast?'
NUMBERS = ['58', '3392']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
