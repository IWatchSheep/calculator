"""Algebra word problem 0720   [Proportion]

Problem : A shade of green uses blue and yellow paint in the ratio 3:4. If 18 L of blue is used, how much yellow is needed?
Let     : y = liters of yellow
Equation: 3/4 = 18/y
Solve   : Cross-multiply → y = 24
Answer  : 24 L

Status  : ready: ratio_split answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0720'
KEY = 'proportion/0720'
NAME = 'Proportion 0720'
CATEGORY = 'Proportion'
PROBLEM = 'A shade of green uses blue and yellow paint in the ratio 3:4. If 18 L of blue is used, how much yellow is needed?'
LET = 'y = liters of yellow'
EQUATION = '3/4 = 18/y'
SOLVE = 'Cross-multiply → y = 24'
ANSWER = '24 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'ratio_split'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A shade of green uses blue and yellow paint in the ratio {0}:{1}. If {2} L of blue is used, how much yellow is needed?'
NUMBERS = ['3', '4', '18']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
