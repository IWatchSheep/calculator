"""Algebra word problem 0124   [Distance (average speed)]

Problem : Sofia drove 3 hours at 60 mph and then some hours at 75 mph. The average speed for the whole trip was 66 mph. How long was the second part?
Let     : t = hours at 75 mph
Equation: (60×3 + 75t)/(3 + t) = 66
Solve   : Multiply both sides by the denominator and collect terms → t = 2
Answer  : 2 hours

Status  : ready: average_speed_two_leg_unknown_time answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0124'
KEY = 'distance_average_speed/0124'
NAME = 'Distance (average speed) 0124'
CATEGORY = 'Distance (average speed)'
PROBLEM = 'Sofia drove 3 hours at 60 mph and then some hours at 75 mph. The average speed for the whole trip was 66 mph. How long was the second part?'
LET = 't = hours at 75 mph'
EQUATION = '(60×3 + 75t)/(3 + t) = 66'
SOLVE = 'Multiply both sides by the denominator and collect terms → t = 2'
ANSWER = '2 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'average_speed_two_leg_unknown_time'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Sofia drove {0} hours at {1} mph and then some hours at {2} mph. The average speed for the whole trip was {3} mph. How long was the second part?'
NUMBERS = ['3', '60', '75', '66']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
