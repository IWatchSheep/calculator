"""Thirtieth fresh set for word_solver.py: neighbours of the wordings fixed in batch 27 ("finishing", another deadline such as today or by Friday, a comparison whose
subject is "it" or "one"), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("A 240-page book has 40 pages already read. She must finish the book in 8 days. How many pages a day must be read while finishing it?", [25]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its width? It is the narrower side.", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. It is the wider side. What is its length?", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. The shorter one is the length. What is its length?", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length? It is less than the width.", [5]),
    ("A 240-page book has 40 pages already read. She must finish the book in 8 days. How many pages a day must be read while finishing the report?", None),
    ("A 240-page book has 40 pages already read. How many pages a day must be read to finish it in 8 days by Friday?", None),
    ("A 240-page book has 40 pages already read. She must finish the book in 8 days. How many pages a day must be read to finish it tonight?", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length? It is the same as the width.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. Find its length and width. It is longer than the width.", None),
]
