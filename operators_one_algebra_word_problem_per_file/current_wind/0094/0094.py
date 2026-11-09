"""Algebra word problem 0094   [Current / wind]

Problem : A boat travels 40 km downstream in 2 hours and 16 km upstream in 2 hours. Find the speed of the boat in still water and the speed of the current.
Let     : b = boat speed, c = current speed
Equation: b + c = 20;  b − c = 8
Solve   : 2b = 28 → b = 14, c = 6
Answer  : Boat 14 km/h, current 6 km/h

Status  : ready: still_water_current answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0094'
KEY = 'current_wind/0094'
NAME = 'Current / wind 0094'
CATEGORY = 'Current / wind'
PROBLEM = 'A boat travels 40 km downstream in 2 hours and 16 km upstream in 2 hours. Find the speed of the boat in still water and the speed of the current.'
LET = 'b = boat speed, c = current speed'
EQUATION = 'b + c = 20;  b − c = 8'
SOLVE = '2b = 28 → b = 14, c = 6'
ANSWER = 'Boat 14 km/h, current 6 km/h'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'still_water_current'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A boat travels {0} km downstream in {1} hours and {2} km upstream in {3} hours. Find the speed of the boat in still water and the speed of the current.'
NUMBERS = ['40', '2', '16', '2']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
