"""Algebra word problem 0694   [Proportion]

Problem : A recipe uses 0.5 cups of flour for 4 servings. How many cups are needed for 8 servings?
Let     : x = cups needed
Equation: 0.5/4 = x/8
Solve   : x = 0.5 × 8 / 4 = 1
Answer  : 1 cup

Status  : ready: proportion answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0694'
KEY = 'proportion/0694'
NAME = 'Proportion 0694'
CATEGORY = 'Proportion'
PROBLEM = 'A recipe uses 0.5 cups of flour for 4 servings. How many cups are needed for 8 servings?'
LET = 'x = cups needed'
EQUATION = '0.5/4 = x/8'
SOLVE = 'x = 0.5 × 8 / 4 = 1'
ANSWER = '1 cup'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'proportion'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A recipe uses {0} cups of flour for {1} servings. How many cups are needed for {2} servings?'
NUMBERS = ['0.5', '4', '8']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
