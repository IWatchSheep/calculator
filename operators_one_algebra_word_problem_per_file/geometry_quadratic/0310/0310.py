"""Algebra word problem 0310   [Geometry (quadratic)]

Problem : A farmer has 48 m of fencing to build a rectangular pen against a barn wall (no fence on the wall side). The pen must have an area of 216 m². What dimensions work?
Let     : w = each side perpendicular to the wall
Equation: w(48 − 2w) = 216
Solve   : w² − 24w + 108 = 0 → w = 6 (the other root, 18, also works)
Answer  : Two answers: 18 m × 12 m, or 6 m × 36 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0310'
KEY = 'geometry_quadratic/0310'
NAME = 'Geometry (quadratic) 0310'
CATEGORY = 'Geometry (quadratic)'
PROBLEM = 'A farmer has 48 m of fencing to build a rectangular pen against a barn wall (no fence on the wall side). The pen must have an area of 216 m². What dimensions work?'
LET = 'w = each side perpendicular to the wall'
EQUATION = 'w(48 − 2w) = 216'
SOLVE = 'w² − 24w + 108 = 0 → w = 6 (the other root, 18, also works)'
ANSWER = 'Two answers: 18 m × 12 m, or 6 m × 36 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A farmer has {0} m of fencing to build a rectangular pen against a barn wall (no fence on the wall side). The pen must have an area of {1} m². What dimensions work?'
NUMBERS = ['48', '216']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
