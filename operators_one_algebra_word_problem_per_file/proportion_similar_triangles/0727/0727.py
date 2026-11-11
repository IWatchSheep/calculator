"""Algebra word problem 0727   [Proportion (similar triangles)]

Problem : A 7 ft person casts a 11 ft shadow. At the same time a tree casts a 44 ft shadow. How tall is the tree?
Let     : h = height
Equation: 7/11 = h/44
Solve   : h/44 = 7/11 → h = 7/11 × 44 = 28
Answer  : 28

Status  : ready: archive_proportion_similar_triangles_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0727'
KEY = 'proportion_similar_triangles/0727'
NAME = 'Proportion (similar triangles) 0727'
CATEGORY = 'Proportion (similar triangles)'
PROBLEM = 'A 7 ft person casts a 11 ft shadow. At the same time a tree casts a 44 ft shadow. How tall is the tree?'
LET = 'h = height'
EQUATION = '7/11 = h/44'
SOLVE = 'h/44 = 7/11 → h = 7/11 × 44 = 28'
ANSWER = '28'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_proportion_similar_triangles_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} ft person casts a {1} ft shadow. At the same time a tree casts a {2} ft shadow. How tall is the tree?'
NUMBERS = ['7', '11', '44']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
