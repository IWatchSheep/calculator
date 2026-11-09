"""Algebra word problem 0725   [Proportion (similar triangles)]

Problem : A 5 ft person casts a 2 ft shadow. At the same time a tree casts a 30 ft shadow. How tall is the tree?
Let     : h = height
Equation: 5/2 = h/30
Solve   : h/30 = 2.5 → h = 2.5 × 30 = 75
Answer  : 75

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0725'
KEY = 'proportion_similar_triangles/0725'
NAME = 'Proportion (similar triangles) 0725'
CATEGORY = 'Proportion (similar triangles)'
PROBLEM = 'A 5 ft person casts a 2 ft shadow. At the same time a tree casts a 30 ft shadow. How tall is the tree?'
LET = 'h = height'
EQUATION = '5/2 = h/30'
SOLVE = 'h/30 = 2.5 → h = 2.5 × 30 = 75'
ANSWER = '75'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} ft person casts a {1} ft shadow. At the same time a tree casts a {2} ft shadow. How tall is the tree?'
NUMBERS = ['5', '2', '30']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
