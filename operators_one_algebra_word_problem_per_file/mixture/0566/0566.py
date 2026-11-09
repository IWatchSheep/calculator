"""Algebra word problem 0566   [Mixture]

Problem : One alloy is 10% copper and another is 90% copper. How many kilograms of each are needed to make 20 kg of an alloy that is 54% copper?
Let     : x = kg of the 10% alloy
Equation: 0.1x + 0.9(20 − x) = 0.54(20)
Solve   : 0.8x = 7.2 → x = 9
Answer  : 9 kg of 10%, 11 kg of 90%

Status  : ready: two_solution_mix answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0566'
KEY = 'mixture/0566'
NAME = 'Mixture 0566'
CATEGORY = 'Mixture'
PROBLEM = 'One alloy is 10% copper and another is 90% copper. How many kilograms of each are needed to make 20 kg of an alloy that is 54% copper?'
LET = 'x = kg of the 10% alloy'
EQUATION = '0.1x + 0.9(20 − x) = 0.54(20)'
SOLVE = '0.8x = 7.2 → x = 9'
ANSWER = '9 kg of 10%, 11 kg of 90%'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_solution_mix'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'One alloy is {0}% copper and another is {1}% copper. How many kilograms of each are needed to make {2} kg of an alloy that is {3}% copper?'
NUMBERS = ['10', '90', '20', '54']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
