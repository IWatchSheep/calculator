"""Algebra word problem 0925   [System of equations]

Problem : A test has 30 questions. Each correct answer earns 5 points and each wrong answer loses 2. Zoe answered every question and scored 52. How many were correct?
Let     : c = correct, w = wrong
Equation: c + w = 30;  5c − 2w = 52
Solve   : Solve by elimination → c = 16, w = 14
Answer  : 16 correct, 14 wrong

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0925'
KEY = 'system_of_equations/0925'
NAME = 'System of equations 0925'
CATEGORY = 'System of equations'
PROBLEM = 'A test has 30 questions. Each correct answer earns 5 points and each wrong answer loses 2. Zoe answered every question and scored 52. How many were correct?'
LET = 'c = correct, w = wrong'
EQUATION = 'c + w = 30;  5c − 2w = 52'
SOLVE = 'Solve by elimination → c = 16, w = 14'
ANSWER = '16 correct, 14 wrong'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A test has {0} questions. Each correct answer earns {1} points and each wrong answer loses {2}. Zoe answered every question and scored {3}. How many were correct?'
NUMBERS = ['30', '5', '2', '52']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
