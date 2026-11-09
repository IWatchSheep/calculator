"""Algebra word problem 0813   [Rational equation]

Problem : A plane flies 1590 miles with a 40 mph tailwind in the same time it flies 1350 miles into the same wind as a headwind. What is the plane's speed in still air?
Let     : p = plane speed
Equation: 1590/(p + 40) = 1350/(p − 40)
Solve   : Cross-multiply → p = 490
Answer  : 490 mph

Status  : ready: wind_same_time answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0813'
KEY = 'rational_equation/0813'
NAME = 'Rational equation 0813'
CATEGORY = 'Rational equation'
PROBLEM = "A plane flies 1590 miles with a 40 mph tailwind in the same time it flies 1350 miles into the same wind as a headwind. What is the plane's speed in still air?"
LET = 'p = plane speed'
EQUATION = '1590/(p + 40) = 1350/(p − 40)'
SOLVE = 'Cross-multiply → p = 490'
ANSWER = '490 mph'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'wind_same_time'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A plane flies {0} miles with a {1} mph tailwind in the same time it flies {2} miles into the same wind as a headwind. What is the plane's speed in still air?"
NUMBERS = ['1590', '40', '1350']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
