"""Algebra word problem 0137   [Distance (opposite directions)]

Problem : Kira and Wes leave the same town at the same time, driving in opposite directions at 55 mph and 57 mph. After how many hours will they be 112 miles apart?
Let     : t = hours
Equation: 55t + 57t = 112
Solve   : 112t = 112 → t = 1
Answer  : 1 hour

Status  : ready: opposite_directions answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0137'
KEY = 'distance_opposite_directions/0137'
NAME = 'Distance (opposite directions) 0137'
CATEGORY = 'Distance (opposite directions)'
PROBLEM = 'Kira and Wes leave the same town at the same time, driving in opposite directions at 55 mph and 57 mph. After how many hours will they be 112 miles apart?'
LET = 't = hours'
EQUATION = '55t + 57t = 112'
SOLVE = '112t = 112 → t = 1'
ANSWER = '1 hour'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'opposite_directions'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Kira and Wes leave the same town at the same time, driving in opposite directions at {0} mph and {1} mph. After how many hours will they be {2} miles apart?'
NUMBERS = ['55', '57', '112']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
