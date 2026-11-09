"""Thirty-fifth fresh set for word_solver.py: neighbours of the crash fixed in batch 32 (a rectangle question that does not say "find" or "what": "How long is the
shorter side?", "Calculate the sides.", "The sides please."), written AFTER the fix was finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline.  None of them may raise an error."""

FRESH = [
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. How long is the shorter side?", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. How wide is the longer side?", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. How long is the longer side?", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Calculate the sides.", [5, 12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Sides?", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. The sides please.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. How long is it?", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. How long is the shorter side of the garden?", None),
]
