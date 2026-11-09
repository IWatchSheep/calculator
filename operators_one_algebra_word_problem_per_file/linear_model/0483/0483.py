"""Algebra word problem 0483   [Linear model]

Problem : Plant A is 13 cm tall and grows 3 cm a week. Plant B is 28 cm tall and grows 1 cm a week. After how many weeks will they be the same height?
Let     : w = weeks
Equation: 13 + 3w = 28 + w
Solve   : 2w = 15 → w = 7.5
Answer  : 7.5 weeks

Status  : ready: two_changing_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0483'
KEY = 'linear_model/0483'
NAME = 'Linear model 0483'
CATEGORY = 'Linear model'
PROBLEM = 'Plant A is 13 cm tall and grows 3 cm a week. Plant B is 28 cm tall and grows 1 cm a week. After how many weeks will they be the same height?'
LET = 'w = weeks'
EQUATION = '13 + 3w = 28 + w'
SOLVE = '2w = 15 → w = 7.5'
ANSWER = '7.5 weeks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_changing_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Plant A is {0} cm tall and grows {1} cm a week. Plant B is {2} cm tall and grows {3} cm a week. After how many weeks will they be the same height?'
NUMBERS = ['13', '3', '28', '1']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
