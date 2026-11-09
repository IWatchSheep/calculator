"""Algebra word problem 0139   [Distance (opposite directions)]

Problem : Kofi and Emeka leave the same town at the same time, driving in opposite directions at 49 mph and 51 mph. After how many hours will they be 300 miles apart?
Let     : t = hours
Equation: 49t + 51t = 300
Solve   : 100t = 300 → t = 3
Answer  : 3 hours

Status  : ready: opposite_directions answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0139'
KEY = 'distance_opposite_directions/0139'
NAME = 'Distance (opposite directions) 0139'
CATEGORY = 'Distance (opposite directions)'
PROBLEM = 'Kofi and Emeka leave the same town at the same time, driving in opposite directions at 49 mph and 51 mph. After how many hours will they be 300 miles apart?'
LET = 't = hours'
EQUATION = '49t + 51t = 300'
SOLVE = '100t = 300 → t = 3'
ANSWER = '3 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'opposite_directions'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Kofi and Emeka leave the same town at the same time, driving in opposite directions at {0} mph and {1} mph. After how many hours will they be {2} miles apart?'
NUMBERS = ['49', '51', '300']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
