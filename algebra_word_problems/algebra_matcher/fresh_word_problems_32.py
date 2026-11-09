"""Thirty-second fresh set for word_solver.py: neighbours of the wordings fixed in batch 29 (a "which is ..." clause or an apposition such as "the longer one"
hanging on the side just named in the rectangle question), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length, which is the shorter side?", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find its width, which is the longer one.", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its width, the narrower side?", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find the length, which is less than the width.", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length, the longer one?", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its width, which is longer than a bus?", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find its length, which is the shorter side of the lot.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length, which is shorter than the length?", None),
]
