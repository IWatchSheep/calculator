"""Algebra word problem 0117   [Distance (average speed)]

Problem : Aiden drove 2 hours at 60 mph and then some hours at 45 mph. The average speed for the whole trip was 55 mph. How long was the second part?
Let     : t = hours at 45 mph
Equation: (60×2 + 45t)/(2 + t) = 55
Solve   : Multiply both sides by the denominator and collect terms → t = 1
Answer  : 1 hour

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0117'
KEY = 'distance_average_speed/0117'
NAME = 'Distance (average speed) 0117'
CATEGORY = 'Distance (average speed)'
PROBLEM = 'Aiden drove 2 hours at 60 mph and then some hours at 45 mph. The average speed for the whole trip was 55 mph. How long was the second part?'
LET = 't = hours at 45 mph'
EQUATION = '(60×2 + 45t)/(2 + t) = 55'
SOLVE = 'Multiply both sides by the denominator and collect terms → t = 1'
ANSWER = '1 hour'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Aiden drove {0} hours at {1} mph and then some hours at {2} mph. The average speed for the whole trip was {3} mph. How long was the second part?'
NUMBERS = ['2', '60', '45', '55']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
