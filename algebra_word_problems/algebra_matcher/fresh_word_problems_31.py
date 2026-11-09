"""Thirty-first fresh set for word_solver.py: neighbours of the wordings fixed in batch 28 (a comparison word that is not a comparison of the two sides, a bare
"It is shorter.", a statement and its question in one sentence), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its width? It is less than the length.", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. It is more than the width. What is its length?", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. The longer side is the length. What is its length?", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. The width is shorter than the length, so what is its width?", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its width? It is longer than a tennis court.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length? It is less than 20 m.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length? It is more beautiful than the width.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length? It is longer.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. The width is the smaller of the two sides in a garden. What is its width?", None),
]
