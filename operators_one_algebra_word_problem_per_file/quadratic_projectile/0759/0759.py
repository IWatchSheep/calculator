"""Algebra word problem 0759   [Quadratic (projectile)]

Problem : A rocket is launched upward from a height of 96 ft at 16 ft/s. Its height is h = −16t² + 16t + 96. After how many seconds does it hit the ground?
Let     : t = seconds
Equation: −16t² + 16t + 96 = 0
Solve   : Factor/quadratic formula → t = 3 (other root t = -2 rejected)
Answer  : 3 seconds

Status  : reference only: no solver answers it yet (compute(...) raises)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = '0759'
KEY = 'quadratic_projectile/0759'
NAME = 'Quadratic (projectile) 0759'
CATEGORY = 'Quadratic (projectile)'
PROBLEM = 'A rocket is launched upward from a height of 96 ft at 16 ft/s. Its height is h = −16t² + 16t + 96. After how many seconds does it hit the ground?'
LET = 't = seconds'
EQUATION = '−16t² + 16t + 96 = 0'
SOLVE = 'Factor/quadratic formula → t = 3 (other root t = -2 rejected)'
ANSWER = '3 seconds'
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = None
FAMILY = None
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = 'A rocket is launched upward from a height of {0} ft at {1} ft/s. Its height is h = −{2}t² + {3}t + {4}. After how many seconds does it hit the ground?'
NUMBERS = ['96', '16', '16', '16', '96']


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
