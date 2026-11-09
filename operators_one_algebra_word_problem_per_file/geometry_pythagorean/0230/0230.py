"""Algebra word problem 0230   [Geometry (Pythagorean)]

Problem : One leg of a right triangle is 5 cm longer than the other. The hypotenuse is 25 cm. Find the legs.
Let     : x = shorter leg
Equation: x² + (x + 5)² = 25²
Solve   : x² + 5x − 300 = 0 → x = 15 (the other root, -20, is rejected)
Answer  : 15 and 20

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0230'
KEY = 'geometry_pythagorean/0230'
NAME = 'Geometry (Pythagorean) 0230'
CATEGORY = 'Geometry (Pythagorean)'
PROBLEM = 'One leg of a right triangle is 5 cm longer than the other. The hypotenuse is 25 cm. Find the legs.'
LET = 'x = shorter leg'
EQUATION = 'x² + (x + 5)² = 25²'
SOLVE = 'x² + 5x − 300 = 0 → x = 15 (the other root, -20, is rejected)'
ANSWER = '15 and 20'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One leg of a right triangle is {0} cm longer than the other. The hypotenuse is {1} cm. Find the legs.'
NUMBERS = ['5', '25']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
