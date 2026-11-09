"""Algebra word problem 0556   [Mixture]

Problem : A 60 L tank of 8% salt water is left to evaporate until it is 10% salt. How much water evaporates?
Let     : e = liters evaporated
Equation: 0.08(60) = 0.1(60 − e)
Solve   : e/10 = 1.2 → e = 1.2 × 10 = 12
Answer  : 12 L

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0556'
KEY = 'mixture/0556'
NAME = 'Mixture 0556'
CATEGORY = 'Mixture'
PROBLEM = 'A 60 L tank of 8% salt water is left to evaporate until it is 10% salt. How much water evaporates?'
LET = 'e = liters evaporated'
EQUATION = '0.08(60) = 0.1(60 − e)'
SOLVE = 'e/10 = 1.2 → e = 1.2 × 10 = 12'
ANSWER = '12 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} L tank of {1}% salt water is left to evaporate until it is {2}% salt. How much water evaporates?'
NUMBERS = ['60', '8', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
