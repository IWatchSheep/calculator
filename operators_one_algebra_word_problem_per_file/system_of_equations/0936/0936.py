"""Algebra word problem 0936   [System of equations]

Problem : A test has 50 questions. Each correct answer earns 4 points and each wrong answer loses 1. Noah answered every question and scored 75. How many were correct?
Let     : c = correct, w = wrong
Equation: c + w = 50;  4c − w = 75
Solve   : Solve by elimination → c = 25, w = 25
Answer  : 25 correct, 25 wrong

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0936'
KEY = 'system_of_equations/0936'
NAME = 'System of equations 0936'
CATEGORY = 'System of equations'
PROBLEM = 'A test has 50 questions. Each correct answer earns 4 points and each wrong answer loses 1. Noah answered every question and scored 75. How many were correct?'
LET = 'c = correct, w = wrong'
EQUATION = 'c + w = 50;  4c − w = 75'
SOLVE = 'Solve by elimination → c = 25, w = 25'
ANSWER = '25 correct, 25 wrong'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A test has {0} questions. Each correct answer earns {1} points and each wrong answer loses {2}. Noah answered every question and scored {3}. How many were correct?'
NUMBERS = ['50', '4', '1', '75']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
