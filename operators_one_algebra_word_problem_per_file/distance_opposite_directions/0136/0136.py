"""Algebra word problem 0136   [Distance (opposite directions)]

Problem : Zoe and Sam leave the same town at the same time, driving in opposite directions at 31 mph and 34 mph. After how many hours will they be 260 miles apart?
Let     : t = hours
Equation: 31t + 34t = 260
Solve   : 65t = 260 → t = 4
Answer  : 4 hours

Status  : ready: opposite_directions answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0136'
KEY = 'distance_opposite_directions/0136'
NAME = 'Distance (opposite directions) 0136'
CATEGORY = 'Distance (opposite directions)'
PROBLEM = 'Zoe and Sam leave the same town at the same time, driving in opposite directions at 31 mph and 34 mph. After how many hours will they be 260 miles apart?'
LET = 't = hours'
EQUATION = '31t + 34t = 260'
SOLVE = '65t = 260 → t = 4'
ANSWER = '4 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'opposite_directions'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Zoe and Sam leave the same town at the same time, driving in opposite directions at {0} mph and {1} mph. After how many hours will they be {2} miles apart?'
NUMBERS = ['31', '34', '260']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
