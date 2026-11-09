"""Algebra word problem 0447   [Linear cost]

Problem : Bowling costs $6.00 per game plus $3.00 for shoe rental. Theo spent $9.00. How many games were bowled?
Let     : n = games
Equation: 3 + 6n = 9
Solve   : 6n = 6 → n = 1
Answer  : 1 game

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0447'
KEY = 'linear_cost/0447'
NAME = 'Linear cost 0447'
CATEGORY = 'Linear cost'
PROBLEM = 'Bowling costs $6.00 per game plus $3.00 for shoe rental. Theo spent $9.00. How many games were bowled?'
LET = 'n = games'
EQUATION = '3 + 6n = 9'
SOLVE = '6n = 6 → n = 1'
ANSWER = '1 game'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Bowling costs ${0} per game plus ${1} for shoe rental. Theo spent ${2}. How many games were bowled?'
NUMBERS = ['6.00', '3.00', '9.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
