"""Algebra word problem 0723   [Proportion]

Problem : On a map, 1 cm represents 25 km. Two cities are 287.5 km apart. How far apart are they on the map?
Let     : x = map distance in cm
Equation: 1/25 = x/287.5
Solve   : x = 287.5/25 = 11.5
Answer  : 11.5 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0723'
KEY = 'proportion/0723'
NAME = 'Proportion 0723'
CATEGORY = 'Proportion'
PROBLEM = 'On a map, 1 cm represents 25 km. Two cities are 287.5 km apart. How far apart are they on the map?'
LET = 'x = map distance in cm'
EQUATION = '1/25 = x/287.5'
SOLVE = 'x = 287.5/25 = 11.5'
ANSWER = '11.5 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'On a map, {0} cm represents {1} km. Two cities are {2} km apart. How far apart are they on the map?'
NUMBERS = ['1', '25', '287.5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
