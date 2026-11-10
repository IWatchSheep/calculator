"""Forty-fifth fresh set for word_solver.py: neighbours of the batch-41 fixes (a time clause has to end its sentence; a sentence that gives no time, asks nothing and does
not open the devices is something else going on), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

PIPES = "Pipe A fills a tank in 8 hours, pipe B in 8 hours, and a drain empties it in 16 hours. "
ASK = " How long does it take to fill the tank?"

FRESH = [
    (PIPES + "All three are open." + ASK, [Fraction(16, 3)]),
    (PIPES + "With all three open, how long does it take to fill the tank?", [Fraction(16, 3)]),
    ("Pipe A fills a tank in 8 hours, pipe B in 8 hours, and a drain empties it in 16 hours and is partly blocked. All three are open." + ASK, None),
    ("Pipe A fills a tank in 8 hours, pipe B in 8 hours, and a drain empties it in 16 hours, but it is clogged. All three are open." + ASK, None),
    ("Pipe A fills a tank in 8 hours and pipe B in 8 hours. A drain empties it in 16 hours when it is rusty. All three are open." + ASK, None),
    (PIPES + "All three are open. A little water also seeps out through the floor." + ASK, None),
    (PIPES + "Water is also lost to evaporation. All three are open." + ASK, None),
    (PIPES + "All three are open. Rain falls into the tank as well." + ASK, None),
    (PIPES + "The tank is very old. All three are open." + ASK, None),
]
