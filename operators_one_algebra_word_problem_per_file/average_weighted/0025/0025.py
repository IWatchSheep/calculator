"""Algebra word problem 0025   [Average (weighted)]

Problem : A course grade is 60% coursework and 40% final exam. Ivan has a coursework average of 97. What final exam score gives an overall grade of 85?
Let     : f = final exam score
Equation: 0.6(97) + 0.4f = 85
Solve   : 0.4f = 26.8 → f = 67
Answer  : 67

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0025'
KEY = 'average_weighted/0025'
NAME = 'Average (weighted) 0025'
CATEGORY = 'Average (weighted)'
PROBLEM = 'A course grade is 60% coursework and 40% final exam. Ivan has a coursework average of 97. What final exam score gives an overall grade of 85?'
LET = 'f = final exam score'
EQUATION = '0.6(97) + 0.4f = 85'
SOLVE = '0.4f = 26.8 → f = 67'
ANSWER = '67'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A course grade is {0}% coursework and {1}% final exam. Ivan has a coursework average of {2}. What final exam score gives an overall grade of {3}?'
NUMBERS = ['60', '40', '97', '85']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
