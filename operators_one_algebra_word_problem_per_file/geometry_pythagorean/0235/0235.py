"""Algebra word problem 0235   [Geometry (Pythagorean)]

Problem : One leg of a right triangle is 1 cm longer than the other. The hypotenuse is 29 cm. Find the legs.
Let     : x = shorter leg
Equation: x² + (x + 1)² = 29²
Solve   : x² + x − 420 = 0 → x = 20 (the other root, -21, is rejected)
Answer  : 20 and 21

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0235'
KEY = 'geometry_pythagorean/0235'
NAME = 'Geometry (Pythagorean) 0235'
CATEGORY = 'Geometry (Pythagorean)'
PROBLEM = 'One leg of a right triangle is 1 cm longer than the other. The hypotenuse is 29 cm. Find the legs.'
LET = 'x = shorter leg'
EQUATION = 'x² + (x + 1)² = 29²'
SOLVE = 'x² + x − 420 = 0 → x = 20 (the other root, -21, is rejected)'
ANSWER = '20 and 21'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One leg of a right triangle is {0} cm longer than the other. The hypotenuse is {1} cm. Find the legs.'
NUMBERS = ['1', '29']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
