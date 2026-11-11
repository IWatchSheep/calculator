"""Algebra word problem 0121   [Distance (average speed)]

Problem : Emeka drove 1 hour at 50 mph and then some hours at 45 mph. The average speed for the whole trip was 46 mph. How long was the second part?
Let     : t = hours at 45 mph
Equation: (50×1 + 45t)/(1 + t) = 46
Solve   : Multiply both sides by the denominator and collect terms → t = 4
Answer  : 4 hours

Status  : ready: average_speed_two_leg_unknown_time answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0121'
KEY = 'distance_average_speed/0121'
NAME = 'Distance (average speed) 0121'
CATEGORY = 'Distance (average speed)'
PROBLEM = 'Emeka drove 1 hour at 50 mph and then some hours at 45 mph. The average speed for the whole trip was 46 mph. How long was the second part?'
LET = 't = hours at 45 mph'
EQUATION = '(50×1 + 45t)/(1 + t) = 46'
SOLVE = 'Multiply both sides by the denominator and collect terms → t = 4'
ANSWER = '4 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'average_speed_two_leg_unknown_time'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Emeka drove {0} hour at {1} mph and then some hours at {2} mph. The average speed for the whole trip was {3} mph. How long was the second part?'
NUMBERS = ['1', '50', '45', '46']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
