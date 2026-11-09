"""Algebra word problem 0234   [Geometry (Pythagorean)]

Problem : A ramp is 41 ft long and covers a horizontal distance of 9 ft; how high does it rise?
Let     : h = height
Equation: 9² + h² = 41²
Solve   : h² − 1600 = 0 → h = 40 (the other root, -40, is rejected)
Answer  : 40 ft

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0234'
KEY = 'geometry_pythagorean/0234'
NAME = 'Geometry (Pythagorean) 0234'
CATEGORY = 'Geometry (Pythagorean)'
PROBLEM = 'A ramp is 41 ft long and covers a horizontal distance of 9 ft; how high does it rise?'
LET = 'h = height'
EQUATION = '9² + h² = 41²'
SOLVE = 'h² − 1600 = 0 → h = 40 (the other root, -40, is rejected)'
ANSWER = '40 ft'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A ramp is {0} ft long and covers a horizontal distance of {1} ft; how high does it rise?'
NUMBERS = ['41', '9']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
