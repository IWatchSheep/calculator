"""Algebra word problem 0644   [Percent]

Problem : 30 out of 150 students passed. What percent passed?
Let     : p = percent
Equation: (p/100)(150) = 30
Solve   : 1.5p = 30 → p = 20
Answer  : 20%

Status  : ready: archive_percent_2 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0644'
KEY = 'percent/0644'
NAME = 'Percent 0644'
CATEGORY = 'Percent'
PROBLEM = '30 out of 150 students passed. What percent passed?'
LET = 'p = percent'
EQUATION = '(p/100)(150) = 30'
SOLVE = '1.5p = 30 → p = 20'
ANSWER = '20%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_percent_2'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0} out of {1} students passed. What percent passed?'
NUMBERS = ['30', '150']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
