"""Algebra word problem 0184   [Formula]

Problem : On a seesaw, weight × distance from the pivot must be equal on both sides. Jade (69 kg) sits 3 m from the pivot. How far from the pivot must Theo (36 kg) sit to balance?
Let     : d = distance
Equation: 69 × 3 = 36d
Solve   : 36d = 207 → d = 5.75
Answer  : 5.75 m

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0184'
KEY = 'formula/0184'
NAME = 'Formula 0184'
CATEGORY = 'Formula'
PROBLEM = 'On a seesaw, weight × distance from the pivot must be equal on both sides. Jade (69 kg) sits 3 m from the pivot. How far from the pivot must Theo (36 kg) sit to balance?'
LET = 'd = distance'
EQUATION = '69 × 3 = 36d'
SOLVE = '36d = 207 → d = 5.75'
ANSWER = '5.75 m'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'On a seesaw, weight × distance from the pivot must be equal on both sides. Jade ({0} kg) sits {1} m from the pivot. How far from the pivot must Theo ({2} kg) sit to balance?'
NUMBERS = ['69', '3', '36']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
