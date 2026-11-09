"""Algebra word problem 0656   [Percent]

Problem : A test has 80 questions. Theo scored 95%. How many questions were answered correctly?
Let     : c = correct answers
Equation: c/80 = 0.95
Solve   : c/80 = 0.95 → c = 0.95 × 80 = 76
Answer  : 76 questions

Status  : ready: percent_of_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0656'
KEY = 'percent/0656'
NAME = 'Percent 0656'
CATEGORY = 'Percent'
PROBLEM = 'A test has 80 questions. Theo scored 95%. How many questions were answered correctly?'
LET = 'c = correct answers'
EQUATION = 'c/80 = 0.95'
SOLVE = 'c/80 = 0.95 → c = 0.95 × 80 = 76'
ANSWER = '76 questions'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_of_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A test has {0} questions. Theo scored {1}%. How many questions were answered correctly?'
NUMBERS = ['80', '95']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
