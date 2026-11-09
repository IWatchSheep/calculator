"""Twenty-fifth fresh set for word_solver.py: wordings for the three families added together (measured things changing until equal, an allowance
plus extra work over some weeks, distance / speed / time), written AFTER all three were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

FRESH = [
    ("Tree A is 120 cm tall and grows 15 cm a year. Tree B is 90 cm tall and grows 20 cm a year. After how many years will they be the same height?", [6]),
    ("Bean A is 2.5 cm tall and grows 1.5 cm a day. Bean B is 8 cm tall and grows 0.5 cm a day. After how many days will they be the same height?", [Fraction(11, 2)]),
    ("Mia earns $12 pay a week plus $5 for each extra shift. Over 6 weeks she received $152. How many extra shifts were worked?", [16]),
    ("Sam gets $20 allowance a month plus $2 for each extra task. For 3 months the total was $76. How many extra tasks were done?", [8]),
    ("How far does a train go in 3 hours at 90 km/h?", [270]),
    ("A runner covers 21 km in 3 hours. What is the speed?", [7]),
    ("How many hours to drive 300 miles at 60 mph?", [5]),
    ("Tree A is 120 cm tall and grows 15 cm a year. Tree B is 90 cm tall and grows 20 cm a year. How tall will they be when they are the same height?", None),
    ("Tree A is 120 cm tall and grows 20 cm a year. Tree B is 90 cm tall and grows 15 cm a year. After how many years will they be the same height?", None),
    ("Mia earns $12 pay a week plus $5 for each extra shift. Over 6 weeks she received $152. How much did the extra shifts pay?", None),
    ("How long does it take to travel 300 miles at 60 km/h?", None),
    ("How long does it take to travel 300 miles at 60 mph in 2 hours?", None),
]
