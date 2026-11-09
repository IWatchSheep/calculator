"""Algebra word problem 0624   [Percent]

Problem : 20% of the students in a club are boys. There are 136 girls. How many students are in the club?
Let     : n = total students
Equation: 0.8n = 136
Solve   : 0.8n = 136 → n = 170
Answer  : 170 students

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0624'
KEY = 'percent/0624'
NAME = 'Percent 0624'
CATEGORY = 'Percent'
PROBLEM = '20% of the students in a club are boys. There are 136 girls. How many students are in the club?'
LET = 'n = total students'
EQUATION = '0.8n = 136'
SOLVE = '0.8n = 136 → n = 170'
ANSWER = '170 students'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = '{0}% of the students in a club are boys. There are {1} girls. How many students are in the club?'
NUMBERS = ['20', '136']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
