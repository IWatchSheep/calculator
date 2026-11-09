"""Algebra word problem 0090   [Current / wind]

Problem : A boat travels 58 km downstream in 2 hours and 15 km upstream in 3 hours. Find the speed of the boat in still water and the speed of the current.
Let     : b = boat speed, c = current speed
Equation: b + c = 29;  b − c = 5
Solve   : 2b = 34 → b = 17, c = 12
Answer  : Boat 17 km/h, current 12 km/h

Status  : ready: still_water_current answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0090'
KEY = 'current_wind/0090'
NAME = 'Current / wind 0090'
CATEGORY = 'Current / wind'
PROBLEM = 'A boat travels 58 km downstream in 2 hours and 15 km upstream in 3 hours. Find the speed of the boat in still water and the speed of the current.'
LET = 'b = boat speed, c = current speed'
EQUATION = 'b + c = 29;  b − c = 5'
SOLVE = '2b = 34 → b = 17, c = 12'
ANSWER = 'Boat 17 km/h, current 12 km/h'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'still_water_current'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A boat travels {0} km downstream in {1} hours and {2} km upstream in {3} hours. Find the speed of the boat in still water and the speed of the current.'
NUMBERS = ['58', '2', '15', '3']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
