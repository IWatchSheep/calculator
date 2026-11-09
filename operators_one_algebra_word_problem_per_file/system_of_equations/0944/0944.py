"""Algebra word problem 0944   [System of equations]

Problem : Vera is 5 times as old as Xena. In 2 years, Vera will be 4 times as old as Xena. How old is each now?
Let     : p = Vera's age, c = Xena's age
Equation: p = 5c;  p + 2 = 4(c + 2)
Solve   : Substitute p = 5c → p = 30, c = 6
Answer  : Vera 30, Xena 6

Status  : ready: ages_later_multiple answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0944'
KEY = 'system_of_equations/0944'
NAME = 'System of equations 0944'
CATEGORY = 'System of equations'
PROBLEM = 'Vera is 5 times as old as Xena. In 2 years, Vera will be 4 times as old as Xena. How old is each now?'
LET = "p = Vera's age, c = Xena's age"
EQUATION = 'p = 5c;  p + 2 = 4(c + 2)'
SOLVE = 'Substitute p = 5c → p = 30, c = 6'
ANSWER = 'Vera 30, Xena 6'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'ages_later_multiple'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Vera is {0} times as old as Xena. In {1} years, Vera will be {2} times as old as Xena. How old is each now?'
NUMBERS = ['5', '2', '4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
