"""Forty-seventh fresh set for word_solver.py: neighbours of the batch-43 fix (once the question has named the thing being filled it has to end), written AFTER the fix
was finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

PIPES = "Pipe A fills a pool in 4 hours, pipe B in 12 hours, and a drain empties it in 6 hours. "

FRESH = [
    (PIPES + "All three are open. How long does it take to fill the pool?", [Fraction(6)]),
    (PIPES + "With everything open, how long does it take to fill the empty pool?", [Fraction(6)]),
    (PIPES + "All three are open. How long does it take to fill it?", [Fraction(6)]),
    (PIPES + "All three are open. How long does it take to fill the pool during a heat wave?", None),
    (PIPES + "All three are open. How long does it take to fill the pool beneath a sprinkler?", None),
    (PIPES + "All three are open. How long does it take to fill the pool on a windy day?", None),
    (PIPES + "All three are open. How long does it take to fill the pool amidst a flood?", None),
    (PIPES + "All three are open. How long does it take to fill the pool near a leaking pipe?", None),
    (PIPES + "All three are open. How long does it take to fill the pool overnight?", None),
]
