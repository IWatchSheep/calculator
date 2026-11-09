"""Algebra word problem 0534   [Mixture]

Problem : One alloy is 25% nickel and another is 75% nickel. How many kilograms of each are needed to make 25 kg of an alloy that is 31% nickel?
Let     : x = kg of the 25% alloy
Equation: 0.25x + 0.75(25 − x) = 0.31(25)
Solve   : x/2 = 11 → x = 11 × 2 = 22
Answer  : 22 kg of 25%, 3 kg of 75%

Status  : ready: two_solution_mix answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0534'
KEY = 'mixture/0534'
NAME = 'Mixture 0534'
CATEGORY = 'Mixture'
PROBLEM = 'One alloy is 25% nickel and another is 75% nickel. How many kilograms of each are needed to make 25 kg of an alloy that is 31% nickel?'
LET = 'x = kg of the 25% alloy'
EQUATION = '0.25x + 0.75(25 − x) = 0.31(25)'
SOLVE = 'x/2 = 11 → x = 11 × 2 = 22'
ANSWER = '22 kg of 25%, 3 kg of 75%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_solution_mix'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One alloy is {0}% nickel and another is {1}% nickel. How many kilograms of each are needed to make {2} kg of an alloy that is {3}% nickel?'
NUMBERS = ['25', '75', '25', '31']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
