"""Algebra word problem 0933   [System of equations]

Problem : A shop sold 33 kg of two teas, one at $4/kg and one at $12/kg, for $188. How many kg of each?
Let     : x = kg at $4, y = kg at $12
Equation: x + y = 33;  4x + 12y = 188
Solve   : Solve by elimination → x = 26, y = 7
Answer  : 26 kg at $4, 7 kg at $12

Status  : ready: two_prices_known_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0933'
KEY = 'system_of_equations/0933'
NAME = 'System of equations 0933'
CATEGORY = 'System of equations'
PROBLEM = 'A shop sold 33 kg of two teas, one at $4/kg and one at $12/kg, for $188. How many kg of each?'
LET = 'x = kg at $4, y = kg at $12'
EQUATION = 'x + y = 33;  4x + 12y = 188'
SOLVE = 'Solve by elimination → x = 26, y = 7'
ANSWER = '26 kg at $4, 7 kg at $12'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_prices_known_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A shop sold {0} kg of two teas, one at ${1}/kg and one at ${2}/kg, for ${3}. How many kg of each?'
NUMBERS = ['33', '4', '12', '188']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
