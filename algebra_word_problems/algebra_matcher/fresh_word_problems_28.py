"""Twenty-eighth fresh set for word_solver.py: neighbours of the wordings fixed in batch 25 (the book the deadline belongs to, a named kind of angle, the problem's own
statement of which side of a rectangle is longer), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("A 300-page novel has 60 pages already read. How many pages a day must be read to finish reading it in 8 days?", [30]),
    ("A 300-page novel has 60 pages already read. She must finish the novel in 8 days. How many pages a day must be read?", [30]),
    ("Where two lines cross, opposite angles are (4x + 10)° and (6x − 20)°. Find the acute angle.", [70]),
    ("Where two lines cross, opposite angles are (7x - 10)° and (4x + 50)°. Find the obtuse angle.", [130]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. The width is the longer side. What is its width?", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. The length is the smaller side. What is its length?", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its width?", [5]),
    ("A 300-page novel has 60 pages already read. How many pages a day must be read to finish the assignment in 8 days?", None),
    ("A 300-page novel has 60 pages already finished in 8 days. How many pages a day must be read to finish?", None),
    ("Where two lines cross, opposite angles are (4x + 10)° and (6x − 20)°. Find the obtuse angle.", None),
    ("Where two lines cross, the opposite angles form a right angle: (4x + 10)° and (6x − 20)°. Find x.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. The length is shorter than the length. What is its length?", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. The length is longer than the width and the width is longer than the length. What is its width?", None),
]
