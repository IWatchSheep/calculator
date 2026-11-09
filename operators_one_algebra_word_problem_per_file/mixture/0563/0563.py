"""Algebra word problem 0563   [Mixture]

Problem : One alloy is 25% silver and another is 75% silver. How many kilograms of each are needed to make 40 kg of an alloy that is 67.5% silver?
Let     : x = kg of the 25% alloy
Equation: 0.25x + 0.75(40 − x) = 0.675(40)
Solve   : x/2 = 3 → x = 3 × 2 = 6
Answer  : 6 kg of 25%, 34 kg of 75%

Status  : ready: two_solution_mix answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0563'
KEY = 'mixture/0563'
NAME = 'Mixture 0563'
CATEGORY = 'Mixture'
PROBLEM = 'One alloy is 25% silver and another is 75% silver. How many kilograms of each are needed to make 40 kg of an alloy that is 67.5% silver?'
LET = 'x = kg of the 25% alloy'
EQUATION = '0.25x + 0.75(40 − x) = 0.675(40)'
SOLVE = 'x/2 = 3 → x = 3 × 2 = 6'
ANSWER = '6 kg of 25%, 34 kg of 75%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_solution_mix'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One alloy is {0}% silver and another is {1}% silver. How many kilograms of each are needed to make {2} kg of an alloy that is {3}% silver?'
NUMBERS = ['25', '75', '40', '67.5']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
