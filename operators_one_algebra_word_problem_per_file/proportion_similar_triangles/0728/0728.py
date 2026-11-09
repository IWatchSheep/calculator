"""Algebra word problem 0728   [Proportion (similar triangles)]

Problem : At noon a 4 m post casts a 10 m shadow, and a building nearby casts a 150 m shadow. How tall is the building?
Let     : h = height
Equation: 4/10 = h/150
Solve   : h/150 = 0.4 → h = 0.4 × 150 = 60
Answer  : 60

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0728'
KEY = 'proportion_similar_triangles/0728'
NAME = 'Proportion (similar triangles) 0728'
CATEGORY = 'Proportion (similar triangles)'
PROBLEM = 'At noon a 4 m post casts a 10 m shadow, and a building nearby casts a 150 m shadow. How tall is the building?'
LET = 'h = height'
EQUATION = '4/10 = h/150'
SOLVE = 'h/150 = 0.4 → h = 0.4 × 150 = 60'
ANSWER = '60'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'At noon a {0} m post casts a {1} m shadow, and a building nearby casts a {2} m shadow. How tall is the building?'
NUMBERS = ['4', '10', '150']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
