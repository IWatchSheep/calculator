"""Sixth fresh set for word_solver.py: written AFTER the two-solution mixture family was finished, run once, untuned.
Each item: (problem, amounts) or None = must decline.  Amounts are the two amounts asked for, increasing."""
from fractions import Fraction

FRESH = [
    ("How many liters of a 20% acid solution must be mixed with a 60% acid solution to make 40 liters of a 30% acid solution?", [10, 30]),
    ("A chemist needs 50 mL of a 14% solution. She has a 10% solution and a 20% solution. How much of each should she use?", [20, 30]),
    ("How many kilograms of a 30% silver alloy and a 70% silver alloy are needed to make 20 kg of a 45% silver alloy?", [Fraction(15, 2), Fraction(25, 2)]),
    ("A jeweler melts a 40% gold alloy with a 90% gold alloy to get 100 g of a 65% gold alloy. How many grams of each?", [50, 50]),
    ("How many liters of water must be added to 10 liters of a 40% solution to make it 25%?", None),
    ("How many liters of a 20% solution must be added to 10 liters of a 50% solution to make a 40% solution?", None),
    ("How many pounds of coffee at $6 per pound must be mixed with coffee at $10 per pound to make 40 lb worth $7 per pound?", None),
    ("How many liters of a 10% solution and a 30% solution make 10 liters of a 40% solution?", None),
    ("Mixing 5 liters of a 20% solution with 5 liters of a 40% solution gives what percent?", None),
    ("A 30% solution and a 60% solution make 12 liters of 50% solution, with three times as much of the stronger one. How much of each?", None),
]
