"""Algebra word problem 0226   [Geometry (Pythagorean)]

Problem : One leg of a right triangle is 23 cm longer than the other. The hypotenuse is 37 cm. Find the legs.
Let     : x = shorter leg
Equation: x² + (x + 23)² = 37²
Solve   : x² + 23x − 420 = 0 → x = 12 (the other root, -35, is rejected)
Answer  : 12 and 35

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0226'
KEY = 'geometry_pythagorean/0226'
NAME = 'Geometry (Pythagorean) 0226'
CATEGORY = 'Geometry (Pythagorean)'
PROBLEM = 'One leg of a right triangle is 23 cm longer than the other. The hypotenuse is 37 cm. Find the legs.'
LET = 'x = shorter leg'
EQUATION = 'x² + (x + 23)² = 37²'
SOLVE = 'x² + 23x − 420 = 0 → x = 12 (the other root, -35, is rejected)'
ANSWER = '12 and 35'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One leg of a right triangle is {0} cm longer than the other. The hypotenuse is {1} cm. Find the legs.'
NUMBERS = ['23', '37']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
