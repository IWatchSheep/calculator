"""Forty-third fresh set for word_solver.py: neighbours of the wordings fixed in batch 40 (a sealed / capped / plugged drain and an "all open" that is not the three
devices), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

PIPES = "Pipe A fills a tank in 6 hours, pipe B in 3 hours, and a drain empties it in 12 hours. "
ASK = " How long does it take to fill the tank?"

FRESH = [
    (PIPES + "With all running, how long does it take to fill the tank?", [Fraction(12, 5)]),
    (PIPES + "All working." + ASK, [Fraction(12, 5)]),
    (PIPES + "All three are open but the drain is covered." + ASK, None),
    (PIPES + "All three are open but the drain is bolted." + ASK, None),
    (PIPES + "The tank, all open to the public, is in use." + ASK, None),
    (PIPES + "The park is all open to visitors." + ASK, None),
    (PIPES + "With all open to swimmers, how long does it take to fill the tank?", None),
]
