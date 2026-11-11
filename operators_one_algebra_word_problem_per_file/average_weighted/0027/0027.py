"""Algebra word problem 0027   [Average (weighted)]

Problem : Class A has 14 students averaging 81. Class B averages 91. Together the classes average 85.4. How many students are in class B?
Let     : n = students in class B
Equation: (14×81 + 91n)/(14 + n) = 85.4
Solve   : Multiply both sides by the denominator and collect terms → n = 11
Answer  : 11 students

Status  : ready: archive_average_weighted_1 answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0027'
KEY = 'average_weighted/0027'
NAME = 'Average (weighted) 0027'
CATEGORY = 'Average (weighted)'
PROBLEM = 'Class A has 14 students averaging 81. Class B averages 91. Together the classes average 85.4. How many students are in class B?'
LET = 'n = students in class B'
EQUATION = '(14×81 + 91n)/(14 + n) = 85.4'
SOLVE = 'Multiply both sides by the denominator and collect terms → n = 11'
ANSWER = '11 students'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'archive_average_weighted_1'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'Class A has {0} students averaging {1}. Class B averages {2}. Together the classes average {3}. How many students are in class B?'
NUMBERS = ['14', '81', '91', '85.4']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
