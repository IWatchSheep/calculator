"""Algebra word problem 0135   [Distance (opposite directions)]

Problem : Omar and Lena leave the same town at the same time, driving in opposite directions at 30 mph and 36 mph. After how many hours will they be 165 miles apart?
Let     : t = hours
Equation: 30t + 36t = 165
Solve   : 66t = 165 → t = 2.5
Answer  : 2.5 hours

Status  : ready: opposite_directions answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0135'
KEY = 'distance_opposite_directions/0135'
NAME = 'Distance (opposite directions) 0135'
CATEGORY = 'Distance (opposite directions)'
PROBLEM = 'Omar and Lena leave the same town at the same time, driving in opposite directions at 30 mph and 36 mph. After how many hours will they be 165 miles apart?'
LET = 't = hours'
EQUATION = '30t + 36t = 165'
SOLVE = '66t = 165 → t = 2.5'
ANSWER = '2.5 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'opposite_directions'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Omar and Lena leave the same town at the same time, driving in opposite directions at {0} mph and {1} mph. After how many hours will they be {2} miles apart?'
NUMBERS = ['30', '36', '165']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
