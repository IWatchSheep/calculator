"""Thirty-third fresh set for word_solver.py: neighbours of the wordings fixed in batch 30 (a "which is ..." clause or an apposition on the named rectangle side with NO
comma, and the same words after BOTH sides), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its width which is the narrower side?", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find the length which is the longer side.", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length the shorter one?", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find its width the longer side.", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find its width and length, which is the shorter side.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find its length and width the longer one.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length which is shorter than a house?", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its width which is the longer side of the lot?", None),
]
