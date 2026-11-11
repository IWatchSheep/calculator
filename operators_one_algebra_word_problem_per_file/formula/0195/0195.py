"""Algebra word problem 0195   [Formula]

Problem : On a seesaw, weight × distance from the pivot must be equal on both sides. Sofia (66 kg) sits 6 m from the pivot. How far from the pivot must Mateo (22 kg) sit to balance?
Let     : d = distance
Equation: 66 × 6 = 22d
Solve   : 22d = 396 → d = 18
Answer  : 18 m

Status  : ready: seesaw_balance_distance answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0195'
KEY = 'formula/0195'
NAME = 'Formula 0195'
CATEGORY = 'Formula'
PROBLEM = 'On a seesaw, weight × distance from the pivot must be equal on both sides. Sofia (66 kg) sits 6 m from the pivot. How far from the pivot must Mateo (22 kg) sit to balance?'
LET = 'd = distance'
EQUATION = '66 × 6 = 22d'
SOLVE = '22d = 396 → d = 18'
ANSWER = '18 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'seesaw_balance_distance'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'On a seesaw, weight × distance from the pivot must be equal on both sides. Sofia ({0} kg) sits {1} m from the pivot. How far from the pivot must Mateo ({2} kg) sit to balance?'
NUMBERS = ['66', '6', '22']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
