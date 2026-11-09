"""Algebra word problem 0138   [Distance (opposite directions)]

Problem : Umar and Tara leave the same town at the same time, driving in opposite directions at 43 mph and 55 mph. After how many hours will they be 98 miles apart?
Let     : t = hours
Equation: 43t + 55t = 98
Solve   : 98t = 98 → t = 1
Answer  : 1 hour

Status  : ready: opposite_directions answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0138'
KEY = 'distance_opposite_directions/0138'
NAME = 'Distance (opposite directions) 0138'
CATEGORY = 'Distance (opposite directions)'
PROBLEM = 'Umar and Tara leave the same town at the same time, driving in opposite directions at 43 mph and 55 mph. After how many hours will they be 98 miles apart?'
LET = 't = hours'
EQUATION = '43t + 55t = 98'
SOLVE = '98t = 98 → t = 1'
ANSWER = '1 hour'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'opposite_directions'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Umar and Tara leave the same town at the same time, driving in opposite directions at {0} mph and {1} mph. After how many hours will they be {2} miles apart?'
NUMBERS = ['43', '55', '98']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
