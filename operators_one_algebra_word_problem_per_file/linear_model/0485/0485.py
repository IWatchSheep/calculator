"""Algebra word problem 0485   [Linear model]

Problem : One candle is 13 cm tall and burns 2 cm per hour. Another is 22 cm tall and burns 4 cm per hour. When will they be the same height?
Let     : t = hours
Equation: 13 − 2t = 22 − 4t
Solve   : 2t = 9 → t = 4.5
Answer  : 4.5 hours

Status  : ready: two_candles_equal answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0485'
KEY = 'linear_model/0485'
NAME = 'Linear model 0485'
CATEGORY = 'Linear model'
PROBLEM = 'One candle is 13 cm tall and burns 2 cm per hour. Another is 22 cm tall and burns 4 cm per hour. When will they be the same height?'
LET = 't = hours'
EQUATION = '13 − 2t = 22 − 4t'
SOLVE = '2t = 9 → t = 4.5'
ANSWER = '4.5 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_candles_equal'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One candle is {0} cm tall and burns {1} cm per hour. Another is {2} cm tall and burns {3} cm per hour. When will they be the same height?'
NUMBERS = ['13', '2', '22', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
