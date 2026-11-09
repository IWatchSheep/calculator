"""Forty-first fresh set for word_solver.py: neighbours of the wordings fixed in batch 38 (an "all" that is not the three devices, a second "how many" in the same
sentence), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

RATIO = "The ratio of boys to girls in a class is 3:4. After 6 more girls join, the ratio becomes 1:2. "
PIPES = "Pipe A fills a tank in 6 hours, pipe B in 3 hours, and a drain empties it in 12 hours. "

FRESH = [
    (PIPES + "All three are running. How long does it take to fill the tank?", [Fraction(12, 5)]),
    (PIPES + "With all of them open, how long does it take to fill the tank?", [Fraction(12, 5)]),
    (RATIO + "How many students were there at first?", [21]),
    (PIPES + "The taps are all together. How long does it take to fill the tank?", None),
    (PIPES + "The lamps are all on. How long does it take to fill the tank?", None),
    (PIPES + "The pipes are all open. How long does it take to fill the tank?", None),
    (RATIO + "How many students were there originally and how many girls?", None),
    (RATIO + "How many students were there originally, and how many boys were there?", None),
]
