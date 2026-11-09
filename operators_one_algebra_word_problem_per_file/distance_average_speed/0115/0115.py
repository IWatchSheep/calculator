"""Algebra word problem 0115   [Distance (average speed)]

Problem : Kofi drove 1 hour at 30 mph and then some hours at 55 mph. The average speed for the whole trip was 50 mph. How long was the second part?
Let     : t = hours at 55 mph
Equation: (30×1 + 55t)/(1 + t) = 50
Solve   : Multiply both sides by the denominator and collect terms → t = 4
Answer  : 4 hours

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0115'
KEY = 'distance_average_speed/0115'
NAME = 'Distance (average speed) 0115'
CATEGORY = 'Distance (average speed)'
PROBLEM = 'Kofi drove 1 hour at 30 mph and then some hours at 55 mph. The average speed for the whole trip was 50 mph. How long was the second part?'
LET = 't = hours at 55 mph'
EQUATION = '(30×1 + 55t)/(1 + t) = 50'
SOLVE = 'Multiply both sides by the denominator and collect terms → t = 4'
ANSWER = '4 hours'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Kofi drove {0} hour at {1} mph and then some hours at {2} mph. The average speed for the whole trip was {3} mph. How long was the second part?'
NUMBERS = ['1', '30', '55', '50']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
