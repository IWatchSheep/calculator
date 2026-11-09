"""Algebra word problem 0214   [Fractions]

Problem : A tank is 2/5 full. After 200 liters are added, it is 9/10 full. What is the tank's capacity?
Let     : c = capacity
Equation: (2/5)c + 200 = (9/10)c
Solve   : c/2 = 200 → c = 200 × 2 = 400
Answer  : 400

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0214'
KEY = 'fractions/0214'
NAME = 'Fractions 0214'
CATEGORY = 'Fractions'
PROBLEM = "A tank is 2/5 full. After 200 liters are added, it is 9/10 full. What is the tank's capacity?"
LET = 'c = capacity'
EQUATION = '(2/5)c + 200 = (9/10)c'
SOLVE = 'c/2 = 200 → c = 200 × 2 = 400'
ANSWER = '400'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "A tank is {0}/{1} full. After {2} liters are added, it is {3}/{4} full. What is the tank's capacity?"
NUMBERS = ['2', '5', '200', '9', '10']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
