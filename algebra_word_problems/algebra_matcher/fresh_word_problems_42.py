"""Forty-second fresh set for word_solver.py: neighbours of the wordings fixed in batch 39 (an "all three" that is stopped, off, broken, negated or only a count),
written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""
from fractions import Fraction

PIPES = "Pipe A fills a tank in 6 hours, pipe B in 3 hours, and a drain empties it in 12 hours. "
ASK = " How long does it take to fill the tank?"

FRESH = [
    (PIPES + "All three are flowing." + ASK, [Fraction(12, 5)]),
    (PIPES + "All the pipes and the drain are working." + ASK, [Fraction(12, 5)]),
    (PIPES + "With all three open, how long does it take to fill the tank?", [Fraction(12, 5)]),
    (PIPES + "All three are idle." + ASK, None),
    (PIPES + "All three are not working." + ASK, None),
    (PIPES + "Both pipes and the drain are closed." + ASK, None),
    (PIPES + "All three are jammed." + ASK, None),
    (PIPES + "The class has all three students." + ASK, None),
    (PIPES + "Everything is open except the drain." + ASK, None),
]
