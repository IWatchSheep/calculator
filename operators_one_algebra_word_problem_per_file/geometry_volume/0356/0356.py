"""Algebra word problem 0356   [Geometry (volume)]

Problem : An aquarium 16 dm long and 4 dm wide holds 384 dm³ of water when full. How deep is it?
Let     : h = height
Equation: 16 × 4 × h = 384
Solve   : 64h = 384 → h = 6
Answer  : 6 dm

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0356'
KEY = 'geometry_volume/0356'
NAME = 'Geometry (volume) 0356'
CATEGORY = 'Geometry (volume)'
PROBLEM = 'An aquarium 16 dm long and 4 dm wide holds 384 dm³ of water when full. How deep is it?'
LET = 'h = height'
EQUATION = '16 × 4 × h = 384'
SOLVE = '64h = 384 → h = 6'
ANSWER = '6 dm'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'An aquarium {0} dm long and {1} dm wide holds {2} dm³ of water when full. How deep is it?'
NUMBERS = ['16', '4', '384']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
