"""Algebra word problem 0836   [Rational equation]

Problem : A field trip costs $300 for the bus plus $8 admission per student. The bus cost is shared equally, and each student pays $23.00 in total. How many students went?
Let     : n = students
Equation: 300/n + 8 = 23
Solve   : Subtract 8, then n = 300 ÷ 15 → n = 20
Answer  : 20 students

Status  : ready: shared_fixed_cost answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0836'
KEY = 'rational_equation/0836'
NAME = 'Rational equation 0836'
CATEGORY = 'Rational equation'
PROBLEM = 'A field trip costs $300 for the bus plus $8 admission per student. The bus cost is shared equally, and each student pays $23.00 in total. How many students went?'
LET = 'n = students'
EQUATION = '300/n + 8 = 23'
SOLVE = 'Subtract 8, then n = 300 ÷ 15 → n = 20'
ANSWER = '20 students'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'shared_fixed_cost'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A field trip costs ${0} for the bus plus ${1} admission per student. The bus cost is shared equally, and each student pays ${2} in total. How many students went?'
NUMBERS = ['300', '8', '23.00']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
