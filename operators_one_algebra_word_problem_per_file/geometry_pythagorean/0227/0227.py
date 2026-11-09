"""Algebra word problem 0227   [Geometry (Pythagorean)]

Problem : A 29 ft ladder leans against a wall with its foot 20 ft from the wall. How high up the wall does it reach?
Let     : h = height
Equation: 20² + h² = 29²
Solve   : h² − 441 = 0 → h = 21 (the other root, -21, is rejected)
Answer  : 21 ft

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0227'
KEY = 'geometry_pythagorean/0227'
NAME = 'Geometry (Pythagorean) 0227'
CATEGORY = 'Geometry (Pythagorean)'
PROBLEM = 'A 29 ft ladder leans against a wall with its foot 20 ft from the wall. How high up the wall does it reach?'
LET = 'h = height'
EQUATION = '20² + h² = 29²'
SOLVE = 'h² − 441 = 0 → h = 21 (the other root, -21, is rejected)'
ANSWER = '21 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} ft ladder leans against a wall with its foot {1} ft from the wall. How high up the wall does it reach?'
NUMBERS = ['29', '20']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
