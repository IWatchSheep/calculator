"""Algebra word problem 0716   [Proportion]

Problem : A recipe uses 1 cups of rice for 6 servings. How many cups are needed for 15 servings?
Let     : x = cups needed
Equation: 1/6 = x/15
Solve   : x = 1 × 15 / 6 = 2.5
Answer  : 2.5 cups

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0716'
KEY = 'proportion/0716'
NAME = 'Proportion 0716'
CATEGORY = 'Proportion'
PROBLEM = 'A recipe uses 1 cups of rice for 6 servings. How many cups are needed for 15 servings?'
LET = 'x = cups needed'
EQUATION = '1/6 = x/15'
SOLVE = 'x = 1 × 15 / 6 = 2.5'
ANSWER = '2.5 cups'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A recipe uses {0} cups of rice for {1} servings. How many cups are needed for {2} servings?'
NUMBERS = ['1', '6', '15']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
