"""Algebra word problem 0036   [Break-even]

Problem : It costs $250 to set up a print run plus $15 per poster. Posters sell for $17 each. How many must be sold to break even?
Let     : n = number of posters
Equation: 17n = 250 + 15n
Solve   : 2n = 250 → n = 125
Answer  : 125 posters

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0036'
KEY = 'break_even/0036'
NAME = 'Break-even 0036'
CATEGORY = 'Break-even'
PROBLEM = 'It costs $250 to set up a print run plus $15 per poster. Posters sell for $17 each. How many must be sold to break even?'
LET = 'n = number of posters'
EQUATION = '17n = 250 + 15n'
SOLVE = '2n = 250 → n = 125'
ANSWER = '125 posters'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'It costs ${0} to set up a print run plus ${1} per poster. Posters sell for ${2} each. How many must be sold to break even?'
NUMBERS = ['250', '15', '17']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
