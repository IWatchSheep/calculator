"""Algebra word problem 0915   [System of equations]

Problem : A shop sold 18 kg of two teas, one at $6/kg and one at $12/kg, for $144. How many kg of each?
Let     : x = kg at $6, y = kg at $12
Equation: x + y = 18;  6x + 12y = 144
Solve   : Solve by elimination → x = 12, y = 6
Answer  : 12 kg at $6, 6 kg at $12

Status  : ready: two_prices_known_count answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0915'
KEY = 'system_of_equations/0915'
NAME = 'System of equations 0915'
CATEGORY = 'System of equations'
PROBLEM = 'A shop sold 18 kg of two teas, one at $6/kg and one at $12/kg, for $144. How many kg of each?'
LET = 'x = kg at $6, y = kg at $12'
EQUATION = 'x + y = 18;  6x + 12y = 144'
SOLVE = 'Solve by elimination → x = 12, y = 6'
ANSWER = '12 kg at $6, 6 kg at $12'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'two_prices_known_count'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A shop sold {0} kg of two teas, one at ${1}/kg and one at ${2}/kg, for ${3}. How many kg of each?'
NUMBERS = ['18', '6', '12', '144']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
