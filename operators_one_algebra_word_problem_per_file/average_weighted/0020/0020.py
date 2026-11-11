"""Algebra word problem 0020   [Average (weighted)]

Problem : A course grade is 75% coursework and 25% final exam. Elena has a coursework average of 96. What final exam score gives an overall grade of 86?
Let     : f = final exam score
Equation: 0.75(96) + 0.25f = 86
Solve   : f/4 = 14 → f = 14 × 4 = 56
Answer  : 56

Status  : ready: course_grade_final_exam answers it (compute(...) solves it with any numbers the solver accepts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0020'
KEY = 'average_weighted/0020'
NAME = 'Average (weighted) 0020'
CATEGORY = 'Average (weighted)'
PROBLEM = 'A course grade is 75% coursework and 25% final exam. Elena has a coursework average of 96. What final exam score gives an overall grade of 86?'
LET = 'f = final exam score'
EQUATION = '0.75(96) + 0.25f = 86'
SOLVE = 'f/4 = 14 → f = 14 × 4 = 56'
ANSWER = '56'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = 'word_solver'
FAMILY = 'course_grade_final_exam'
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A course grade is {0}% coursework and {1}% final exam. Elena has a coursework average of {2}. What final exam score gives an overall grade of {3}?'
NUMBERS = ['75', '25', '96', '86']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
