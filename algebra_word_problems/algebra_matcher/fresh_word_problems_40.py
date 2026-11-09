"""Fortieth fresh set for word_solver.py: neighbours of the wordings fixed in batch 37 (the class-ratio question that says "originally", and a pipes problem whose
"together" does not open the drain), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

RATIO = "The ratio of boys to girls in a class is 3:4. After 6 more girls join, the ratio becomes 1:2. "
PIPES = "Pipe A fills a tank in 6 hours, pipe B in 3 hours, and a drain empties it in 12 hours. "

FRESH = [
    (RATIO + "How many students were there to begin with?", [21]),
    (PIPES + "With all three running, how long does it take to fill the tank?", [Fraction(12, 5)]),
    (PIPES + "The pipes and the drain are open together. How long does it take to fill the tank?", [Fraction(12, 5)]),
    (RATIO + "How many students are there now?", None),
    (RATIO + "How many students were there originally? How many students are there after they join?", None),
    (PIPES + "Both pipes are open at the same time. How long does it take to fill the tank?", None),
    (PIPES + "Both pipes work at once. How long does it take to fill the tank?", None),
]
