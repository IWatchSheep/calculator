"""Algebra word problem 0544   [Mixture]

Problem : One alloy is 10% silver and another is 50% silver. How many kilograms of each are needed to make 20 kg of an alloy that is 16% silver?
Let     : x = kg of the 10% alloy
Equation: 0.1x + 0.5(20 − x) = 0.16(20)
Solve   : 0.4x = 6.8 → x = 17
Answer  : 17 kg of 10%, 3 kg of 50%

Status  : ready: two_solution_mix answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0544'
KEY = 'mixture/0544'
NAME = 'Mixture 0544'
CATEGORY = 'Mixture'
PROBLEM = 'One alloy is 10% silver and another is 50% silver. How many kilograms of each are needed to make 20 kg of an alloy that is 16% silver?'
LET = 'x = kg of the 10% alloy'
EQUATION = '0.1x + 0.5(20 − x) = 0.16(20)'
SOLVE = '0.4x = 6.8 → x = 17'
ANSWER = '17 kg of 10%, 3 kg of 50%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_solution_mix'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One alloy is {0}% silver and another is {1}% silver. How many kilograms of each are needed to make {2} kg of an alloy that is {3}% silver?'
NUMBERS = ['10', '50', '20', '16']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
