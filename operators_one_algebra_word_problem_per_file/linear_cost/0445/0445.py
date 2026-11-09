"""Algebra word problem 0445   [Linear cost]

Problem : Bowling costs $6.00 per game plus $4.00 for shoe rental. Nia spent $22.00. How many games were bowled?
Let     : n = games
Equation: 4 + 6n = 22
Solve   : 6n = 18 → n = 3
Answer  : 3 games

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0445'
KEY = 'linear_cost/0445'
NAME = 'Linear cost 0445'
CATEGORY = 'Linear cost'
PROBLEM = 'Bowling costs $6.00 per game plus $4.00 for shoe rental. Nia spent $22.00. How many games were bowled?'
LET = 'n = games'
EQUATION = '4 + 6n = 22'
SOLVE = '6n = 18 → n = 3'
ANSWER = '3 games'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Bowling costs ${0} per game plus ${1} for shoe rental. Nia spent ${2}. How many games were bowled?'
NUMBERS = ['6.00', '4.00', '22.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
