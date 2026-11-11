"""Algebra word problem 0203   [Formula]

Problem : On a seesaw, weight × distance from the pivot must be equal on both sides. Ivan (35 kg) sits 1 m from the pivot. How far from the pivot must Pablo (70 kg) sit to balance?
Let     : d = distance
Equation: 35 × 1 = 70d
Solve   : 70d = 35 → d = 0.5
Answer  : 0.5 m

Status  : ready: seesaw_balance_distance answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0203'
KEY = 'formula/0203'
NAME = 'Formula 0203'
CATEGORY = 'Formula'
PROBLEM = 'On a seesaw, weight × distance from the pivot must be equal on both sides. Ivan (35 kg) sits 1 m from the pivot. How far from the pivot must Pablo (70 kg) sit to balance?'
LET = 'd = distance'
EQUATION = '35 × 1 = 70d'
SOLVE = '70d = 35 → d = 0.5'
ANSWER = '0.5 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'seesaw_balance_distance'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'On a seesaw, weight × distance from the pivot must be equal on both sides. Ivan ({0} kg) sits {1} m from the pivot. How far from the pivot must Pablo ({2} kg) sit to balance?'
NUMBERS = ['35', '1', '70']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
