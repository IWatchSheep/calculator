"""Algebra word problem 0647   [Percent]

Problem : A test has 40 questions. Pablo scored 95%. How many questions were answered correctly?
Let     : c = correct answers
Equation: c/40 = 0.95
Solve   : c/40 = 0.95 → c = 0.95 × 40 = 38
Answer  : 38 questions

Status  : ready: percent_of_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0647'
KEY = 'percent/0647'
NAME = 'Percent 0647'
CATEGORY = 'Percent'
PROBLEM = 'A test has 40 questions. Pablo scored 95%. How many questions were answered correctly?'
LET = 'c = correct answers'
EQUATION = 'c/40 = 0.95'
SOLVE = 'c/40 = 0.95 → c = 0.95 × 40 = 38'
ANSWER = '38 questions'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'percent_of_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A test has {0} questions. Pablo scored {1}%. How many questions were answered correctly?'
NUMBERS = ['40', '95']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
