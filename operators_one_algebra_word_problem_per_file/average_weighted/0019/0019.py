"""Algebra word problem 0019   [Average (weighted)]

Problem : Class A has 13 students averaging 75. Class B averages 93. Together the classes average 84. How many students are in class B?
Let     : n = students in class B
Equation: (13×75 + 93n)/(13 + n) = 84
Solve   : Multiply both sides by the denominator and collect terms → n = 13
Answer  : 13 students

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0019'
KEY = 'average_weighted/0019'
NAME = 'Average (weighted) 0019'
CATEGORY = 'Average (weighted)'
PROBLEM = 'Class A has 13 students averaging 75. Class B averages 93. Together the classes average 84. How many students are in class B?'
LET = 'n = students in class B'
EQUATION = '(13×75 + 93n)/(13 + n) = 84'
SOLVE = 'Multiply both sides by the denominator and collect terms → n = 13'
ANSWER = '13 students'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Class A has {0} students averaging {1}. Class B averages {2}. Together the classes average {3}. How many students are in class B?'
NUMBERS = ['13', '75', '93', '84']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
