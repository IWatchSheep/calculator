"""Algebra word problem 0615   [Percent]

Problem : After adding a 20% tip, a dinner bill came to $195.18. What was the bill before the tip?
Let     : b = bill before tip
Equation: 1.2b = 195.18
Solve   : 1.2b = 195.18 → b = 162.65
Answer  : $162.65

Status  : ready: percent_change answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0615'
KEY = 'percent/0615'
NAME = 'Percent 0615'
CATEGORY = 'Percent'
PROBLEM = 'After adding a 20% tip, a dinner bill came to $195.18. What was the bill before the tip?'
LET = 'b = bill before tip'
EQUATION = '1.2b = 195.18'
SOLVE = '1.2b = 195.18 → b = 162.65'
ANSWER = '$162.65'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_change'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'After adding a {0}% tip, a dinner bill came to ${1}. What was the bill before the tip?'
NUMBERS = ['20', '195.18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
