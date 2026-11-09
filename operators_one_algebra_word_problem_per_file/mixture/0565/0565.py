"""Algebra word problem 0565   [Mixture]

Problem : A 20 L tank of 3% salt water is left to evaporate until it is 12% salt. How much water evaporates?
Let     : e = liters evaporated
Equation: 0.03(20) = 0.12(20 − e)
Solve   : 0.12e = 1.8 → e = 15
Answer  : 15 L

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0565'
KEY = 'mixture/0565'
NAME = 'Mixture 0565'
CATEGORY = 'Mixture'
PROBLEM = 'A 20 L tank of 3% salt water is left to evaporate until it is 12% salt. How much water evaporates?'
LET = 'e = liters evaporated'
EQUATION = '0.03(20) = 0.12(20 − e)'
SOLVE = '0.12e = 1.8 → e = 15'
ANSWER = '15 L'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A {0} L tank of {1}% salt water is left to evaporate until it is {2}% salt. How much water evaporates?'
NUMBERS = ['20', '3', '12']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
