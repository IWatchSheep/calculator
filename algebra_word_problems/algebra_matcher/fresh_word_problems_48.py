"""Forty-eighth fresh set for word_solver.py: neighbours of the batch-44 fix (the words between "how long" and "fill" may only be the plain question words), written AFTER the fix
was finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

PIPES = "Pipe A fills a cistern in 3 hours, pipe B in 6 hours, and a drain empties it in 9 hours. "

FRESH = [
    (PIPES + "All three are open. How long does it take to fill the cistern?", [Fraction(18, 7)]),
    (PIPES + "With all three open, how long will it take to fill the cistern?", [Fraction(18, 7)]),
    (PIPES + "All three are open. How long would it take them to fill the cistern?", [Fraction(18, 7)]),
    (PIPES + "All three are open. How long does it take on a cold night to fill the cistern?", None),
    (PIPES + "All three are open. How long, in the rain, does it take to fill the cistern?", None),
    (PIPES + "All three are open. How long does it take before noon to fill the cistern?", None),
    (PIPES + "All three are open. How long does it take when a hose is added to fill the cistern?", None),
    (PIPES + "All three are open. How long does it take amid a flood to fill the cistern?", None),
    (PIPES + "All three are open. How long, with snow melting, does it take to fill the cistern?", None),
]
