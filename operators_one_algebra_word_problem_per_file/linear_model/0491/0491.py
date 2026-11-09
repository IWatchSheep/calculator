"""Algebra word problem 0491   [Linear model]

Problem : Plant A is 4 cm tall and grows 3 cm a week. Plant B is 24 cm tall and grows 1 cm a week. After how many weeks will they be the same height?
Let     : w = weeks
Equation: 4 + 3w = 24 + w
Solve   : 2w = 20 → w = 10
Answer  : 10 weeks

Status  : ready: two_changing_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0491'
KEY = 'linear_model/0491'
NAME = 'Linear model 0491'
CATEGORY = 'Linear model'
PROBLEM = 'Plant A is 4 cm tall and grows 3 cm a week. Plant B is 24 cm tall and grows 1 cm a week. After how many weeks will they be the same height?'
LET = 'w = weeks'
EQUATION = '4 + 3w = 24 + w'
SOLVE = '2w = 20 → w = 10'
ANSWER = '10 weeks'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_changing_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Plant A is {0} cm tall and grows {1} cm a week. Plant B is {2} cm tall and grows {3} cm a week. After how many weeks will they be the same height?'
NUMBERS = ['4', '3', '24', '1']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
