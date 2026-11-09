"""Thirty-ninth fresh set for word_solver.py: wordings for the three families added together (class_ratio_after_join, kinematics_time, pipes_and_drain),
written AFTER all three were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

FRESH = [
    ("The ratio of boys to girls in a class is 3:4. After 6 more girls join, the ratio becomes 1:2. How many students were there originally?", [21]),
    ("The ratio of cats to dogs at a shelter is 2:3. After 4 more cats arrive, the ratio becomes 1:1. How many animals were there originally?", [20]),
    ("Using v = u + at, how long does it take a car to go from 10 m/s to 40 m/s with acceleration 3 m/s²?", [10]),
    ("Using v = u + at, how long does it take a cyclist to go from 2 ft/s to 17 ft/s with acceleration 3 ft/s²?", [5]),
    ("Pipe A fills a tank in 6 hours, pipe B in 3 hours, and a drain empties it in 12 hours. With all three open, how long does it take to fill the tank?", [Fraction(12, 5)]),
    ("Tap A fills a tub in 10 minutes, tap B in 15 minutes, and a leak empties it in 30 minutes. With all three open, how long does it take to fill the tub?", [Fraction(15, 2)]),
    ("The ratio of boys to girls in a class is 3:4. After 6 more girls join, the ratio becomes 1:2. How many girls were there originally?", None),
    ("The ratio of boys to girls in a class is 3:4. After 6 more girls leave, the ratio becomes 1:2. How many students were there originally?", None),
    ("Using v = u + at, how long does it take a car to go from 10 m/s to 40 km/h with acceleration 3 m/s²?", None),
    ("Using v = u + at, how long does it take a car to go from 40 m/s to 10 m/s with acceleration 3 m/s²?", None),
    ("Pipe A fills a pool in 6 hours, pipe B in 3 hours, and a drain empties it in 2 hours. With all three open, how long does it take to fill the pool?", None),
    ("Pipe A fills a pool in 6 hours, pipe B in 3 hours, and a drain empties it in 12 hours. With all three open, how long does it take to empty the pool?", None),
]
