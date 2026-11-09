"""Forty-fourth fresh set for word_solver.py: neighbours of the batch-40 / batch-41 fixes (a statement about the drain's state in another sentence or in the same
sentence), written AFTER the fixes were finished, run once, untuned.  (Fresh set 43 found a real hole, "the drain is covered", so it is a development set now.)
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

PIPES = "Pipe A fills a tank in 6 hours, pipe B in 3 hours, and a drain empties it in 12 hours. "
ASK = " How long does it take to fill the tank?"

FRESH = [
    (PIPES + "All three are open." + ASK, [Fraction(12, 5)]),
    (PIPES + "With all three running, how long does it take to fill the tank?", [Fraction(12, 5)]),
    (PIPES + "All three are open. The drain has a grate on it." + ASK, None),
    (PIPES + "All three are open. The leak is pinched shut." + ASK, None),
    (PIPES + "All three are open though the drain is jammed." + ASK, None),
    (PIPES + "The drain is covered with a lid. All three are open." + ASK, None),
    (PIPES + "The outlet is small. All three are open." + ASK, None),
    (PIPES + "All three are open and the drain is full of leaves." + ASK, None),
    (PIPES + "All three are open and the drain is silted up." + ASK, None),
]
