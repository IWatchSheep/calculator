"""Algebra word problem 0830   [Rational equation]

Problem : A field trip costs $200 for the bus plus $5 admission per student. The bus cost is shared equally, and each student pays $9.00 in total. How many students went?
Let     : n = students
Equation: 200/n + 5 = 9
Solve   : Subtract 5, then n = 200 ÷ 4 → n = 50
Answer  : 50 students

Status  : ready: shared_fixed_cost answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0830'
KEY = 'rational_equation/0830'
NAME = 'Rational equation 0830'
CATEGORY = 'Rational equation'
PROBLEM = 'A field trip costs $200 for the bus plus $5 admission per student. The bus cost is shared equally, and each student pays $9.00 in total. How many students went?'
LET = 'n = students'
EQUATION = '200/n + 5 = 9'
SOLVE = 'Subtract 5, then n = 200 ÷ 4 → n = 50'
ANSWER = '50 students'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'shared_fixed_cost'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A field trip costs ${0} for the bus plus ${1} admission per student. The bus cost is shared equally, and each student pays ${2} in total. How many students went?'
NUMBERS = ['200', '5', '9.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
