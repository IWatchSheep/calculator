"""Algebra word problem 0894   [System of equations]

Problem : A test has 50 questions. Each correct answer earns 4 points and each wrong answer loses 1. Gus answered every question and scored 180. How many were correct?
Let     : c = correct, w = wrong
Equation: c + w = 50;  4c − w = 180
Solve   : Solve by elimination → c = 46, w = 4
Answer  : 46 correct, 4 wrong

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0894'
KEY = 'system_of_equations/0894'
NAME = 'System of equations 0894'
CATEGORY = 'System of equations'
PROBLEM = 'A test has 50 questions. Each correct answer earns 4 points and each wrong answer loses 1. Gus answered every question and scored 180. How many were correct?'
LET = 'c = correct, w = wrong'
EQUATION = 'c + w = 50;  4c − w = 180'
SOLVE = 'Solve by elimination → c = 46, w = 4'
ANSWER = '46 correct, 4 wrong'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A test has {0} questions. Each correct answer earns {1} points and each wrong answer loses {2}. Gus answered every question and scored {3}. How many were correct?'
NUMBERS = ['50', '4', '1', '180']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
