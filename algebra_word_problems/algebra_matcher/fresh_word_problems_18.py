"""Eighteenth fresh set for word_solver.py: written AFTER the spelled-number fix that fresh set 17 found in add_to_blend, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

FRESH = [
    ("A caterer charges $80 plus $9 per person. The invoice came to $350. How many people ate?", [30]),
    ("A printer charges a $15 setup fee plus $2 per poster. The job cost $63. How many posters were printed?", [24]),
    ("Plant A is 30 cm tall and grows by 4 cm a week. Plant B is 70 cm tall and grows by 2 cm a week. When are they equal?", [20]),
    ("Class A has 40 students and gains 3 a year. Class B has 70 students and loses 2 a year. When are they the same size?", [6]),
    ("How many liters of juice worth $6 per liter must be added to 10 liters of juice worth $2 per liter to make a mix worth $3 per liter?", [Fraction(10, 3)]),
    ("How many ounces of saffron worth $30 per ounce must be added to 8 oz of saffron worth $20 per ounce to make a mix worth $25 per ounce?", [8]),
    ("A printer charges a $15 setup fee plus $2 per poster, with two free posters. The job cost $63. How many posters were printed?", None),
    ("Class A has 40 students and gains 3 a year. Class B has 70 students and loses 2 a year. When are they the same size after two years?", None),
    ("How many pounds of rice worth $4 per pound must be added to 9 lb of rice worth $2 per pound to make a mix worth $2 per pound?", None),
]
