"""Algebra word problem 0667   [Percent]

Problem : In a two-candidate election, the winner got 56% of the votes and won by 4200 votes. How many votes were cast?
Let     : v = total votes
Equation: 0.56v − 0.44v = 4200
Solve   : 0.12v = 4200 → v = 35000
Answer  : 35,000 votes

Status  : ready: election_margin answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0667'
KEY = 'percent/0667'
NAME = 'Percent 0667'
CATEGORY = 'Percent'
PROBLEM = 'In a two-candidate election, the winner got 56% of the votes and won by 4200 votes. How many votes were cast?'
LET = 'v = total votes'
EQUATION = '0.56v − 0.44v = 4200'
SOLVE = '0.12v = 4200 → v = 35000'
ANSWER = '35,000 votes'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'election_margin'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'In a two-candidate election, the winner got {0}% of the votes and won by {1} votes. How many votes were cast?'
NUMBERS = ['56', '4200']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
