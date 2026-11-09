"""Algebra word problem 0274   [Geometry (area)]

Problem : If each side of a square is increased by 2 cm, its area increases by 92 cm². Find the original side length.
Let     : s = original side
Equation: (s + 2)² − s² = 92
Solve   : 4s = 88 → s = 22
Answer  : 22 cm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0274'
KEY = 'geometry_area/0274'
NAME = 'Geometry (area) 0274'
CATEGORY = 'Geometry (area)'
PROBLEM = 'If each side of a square is increased by 2 cm, its area increases by 92 cm². Find the original side length.'
LET = 's = original side'
EQUATION = '(s + 2)² − s² = 92'
SOLVE = '4s = 88 → s = 22'
ANSWER = '22 cm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'If each side of a square is increased by {0} cm, its area increases by {1} cm². Find the original side length.'
NUMBERS = ['2', '92']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
