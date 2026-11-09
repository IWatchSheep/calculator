"""Algebra word problem 0225   [Geometry (Pythagorean)]

Problem : A 10 ft ladder leans against a wall with its foot 6 ft from the wall. How high up the wall does it reach?
Let     : h = height
Equation: 6² + h² = 10²
Solve   : h² − 64 = 0 → h = 8 (the other root, -8, is rejected)
Answer  : 8 ft

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0225'
KEY = 'geometry_pythagorean/0225'
NAME = 'Geometry (Pythagorean) 0225'
CATEGORY = 'Geometry (Pythagorean)'
PROBLEM = 'A 10 ft ladder leans against a wall with its foot 6 ft from the wall. How high up the wall does it reach?'
LET = 'h = height'
EQUATION = '6² + h² = 10²'
SOLVE = 'h² − 64 = 0 → h = 8 (the other root, -8, is rejected)'
ANSWER = '8 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} ft ladder leans against a wall with its foot {1} ft from the wall. How high up the wall does it reach?'
NUMBERS = ['10', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
