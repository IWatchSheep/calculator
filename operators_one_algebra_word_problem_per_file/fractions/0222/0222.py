"""Algebra word problem 0222   [Fractions]

Problem : A tank is 1/5 full. After 152 liters are added, it is 5/6 full. What is the tank's capacity?
Let     : c = capacity
Equation: (1/5)c + 152 = (5/6)c
Solve   : (19/30)c = 152 → c = 240
Answer  : 240

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0222'
KEY = 'fractions/0222'
NAME = 'Fractions 0222'
CATEGORY = 'Fractions'
PROBLEM = "A tank is 1/5 full. After 152 liters are added, it is 5/6 full. What is the tank's capacity?"
LET = 'c = capacity'
EQUATION = '(1/5)c + 152 = (5/6)c'
SOLVE = '(19/30)c = 152 → c = 240'
ANSWER = '240'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A tank is {0}/{1} full. After {2} liters are added, it is {3}/{4} full. What is the tank's capacity?"
NUMBERS = ['1', '5', '152', '5', '6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
