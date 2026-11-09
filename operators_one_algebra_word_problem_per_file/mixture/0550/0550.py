"""Algebra word problem 0550   [Mixture]

Problem : One alloy is 20% silver and another is 40% silver. How many kilograms of each are needed to make 20 kg of an alloy that is 25% silver?
Let     : x = kg of the 20% alloy
Equation: 0.2x + 0.4(20 − x) = 0.25(20)
Solve   : x/5 = 3 → x = 3 × 5 = 15
Answer  : 15 kg of 20%, 5 kg of 40%

Status  : ready: two_solution_mix answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0550'
KEY = 'mixture/0550'
NAME = 'Mixture 0550'
CATEGORY = 'Mixture'
PROBLEM = 'One alloy is 20% silver and another is 40% silver. How many kilograms of each are needed to make 20 kg of an alloy that is 25% silver?'
LET = 'x = kg of the 20% alloy'
EQUATION = '0.2x + 0.4(20 − x) = 0.25(20)'
SOLVE = 'x/5 = 3 → x = 3 × 5 = 15'
ANSWER = '15 kg of 20%, 5 kg of 40%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_solution_mix'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One alloy is {0}% silver and another is {1}% silver. How many kilograms of each are needed to make {2} kg of an alloy that is {3}% silver?'
NUMBERS = ['20', '40', '20', '25']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
