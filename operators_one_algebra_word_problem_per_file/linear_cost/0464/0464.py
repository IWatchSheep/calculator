"""Algebra word problem 0464   [Linear cost]

Problem : Caleb earns $18/hour for the first 40 hours and time-and-a-half after that. Last week's pay was $801.00. How many overtime hours were worked?
Let     : h = overtime hours
Equation: 40(18) + 27h = 801
Solve   : 27h = 81 → h = 3
Answer  : 3 overtime hours (43 hours total)

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0464'
KEY = 'linear_cost/0464'
NAME = 'Linear cost 0464'
CATEGORY = 'Linear cost'
PROBLEM = "Caleb earns $18/hour for the first 40 hours and time-and-a-half after that. Last week's pay was $801.00. How many overtime hours were worked?"
LET = 'h = overtime hours'
EQUATION = '40(18) + 27h = 801'
SOLVE = '27h = 81 → h = 3'
ANSWER = '3 overtime hours (43 hours total)'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = "Caleb earns ${0}/hour for the first {1} hours and time-and-a-half after that. Last week's pay was ${2}. How many overtime hours were worked?"
NUMBERS = ['18', '40', '801.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
