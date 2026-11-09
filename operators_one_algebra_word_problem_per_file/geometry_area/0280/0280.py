"""Algebra word problem 0280   [Geometry (area)]

Problem : If each side of a square is increased by 8 cm, its area increases by 464 cm². Find the original side length.
Let     : s = original side
Equation: (s + 8)² − s² = 464
Solve   : 16s = 400 → s = 25
Answer  : 25 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0280'
KEY = 'geometry_area/0280'
NAME = 'Geometry (area) 0280'
CATEGORY = 'Geometry (area)'
PROBLEM = 'If each side of a square is increased by 8 cm, its area increases by 464 cm². Find the original side length.'
LET = 's = original side'
EQUATION = '(s + 8)² − s² = 464'
SOLVE = '16s = 400 → s = 25'
ANSWER = '25 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'If each side of a square is increased by {0} cm, its area increases by {1} cm². Find the original side length.'
NUMBERS = ['8', '464']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
