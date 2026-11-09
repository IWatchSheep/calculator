"""Algebra word problem 0026   [Average (weighted)]

Problem : Class A has 16 students averaging 80. Class B averages 66. Together the classes average 71.6. How many students are in class B?
Let     : n = students in class B
Equation: (16×80 + 66n)/(16 + n) = 71.6
Solve   : Multiply both sides by the denominator and collect terms → n = 24
Answer  : 24 students

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0026'
KEY = 'average_weighted/0026'
NAME = 'Average (weighted) 0026'
CATEGORY = 'Average (weighted)'
PROBLEM = 'Class A has 16 students averaging 80. Class B averages 66. Together the classes average 71.6. How many students are in class B?'
LET = 'n = students in class B'
EQUATION = '(16×80 + 66n)/(16 + n) = 71.6'
SOLVE = 'Multiply both sides by the denominator and collect terms → n = 24'
ANSWER = '24 students'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Class A has {0} students averaging {1}. Class B averages {2}. Together the classes average {3}. How many students are in class B?'
NUMBERS = ['16', '80', '66', '71.6']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
