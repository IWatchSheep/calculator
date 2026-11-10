"""Forty-sixth fresh set for word_solver.py: neighbours of the batch-42 fixes (the "all open" statement and the question may carry nothing else: no extra water in or out
said inside them), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

PIPES = "Pipe A fills a tank in 5 hours, pipe B in 20 hours, and a drain empties it in 10 hours. "
ASK = " How long does it take to fill the tank?"

FRESH = [
    (PIPES + "All three are open." + ASK, [Fraction(20, 3)]),
    (PIPES + "All three are open, how long does it take to fill the tank?", [Fraction(20, 3)]),
    (PIPES + "How long does it take to fill the tank with all three open?", [Fraction(20, 3)]),
    (PIPES + "All three are open, and some water is lost to a crack." + ASK, None),
    (PIPES + "All three are open while it is raining." + ASK, None),
    (PIPES + "All three are open. How long does it take to fill the tank when a hose also pours in?", None),
    (PIPES + "With all three open, how long does it take to fill the tank as water also seeps out?", None),
    (PIPES + "All three are open. How long does it take to fill the tank, and does rain add to it?", None),
    (PIPES + "All three are open and a fourth pipe is dripping." + ASK, None),
]
