"""Thirty-fourth fresh set for word_solver.py: neighbours of the wordings fixed in batch 31 ("the length of the shorter side", a phrase that does not end on the
comparison, a clause in the middle of the question), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find the length of the shorter side.", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is the width of the longer side?", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its width, the longer side, and its length?", [5, 12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find the width, the narrower side, and the length.", [5, 12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is the length of the narrower one?", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find the width of the longer side of the garden.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length, the shorter side of the plot?", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find the length of the longer side and the width.", None),
]
