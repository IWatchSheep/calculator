"""Twenty-ninth fresh set for word_solver.py: neighbours of the wordings fixed in batch 26 (a different job named in the question, "form a straight angle" as a
statement, more / less / wider / narrower, a statement inside the question), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("A 300-page novel has 60 pages already read. She must finish the novel in 8 days. How many pages a day must be read to finish reading it?", [30]),
    ("Where two lines cross, opposite angles are (3x + 0)° and (2x + 60)°. Find the straight angle.", [180]),
    ("Where two lines cross, opposite angles are (6x - 20)° and (4x + 10)°. Find the acute angle.", [70]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length if the length is less than the width?", [5]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. The length is the wider side. What is its length?", [12]),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. The width is the narrower side. What is its width?", [5]),
    ("A 300-page novel has 60 pages already read. She must finish the novel in 8 days. How many pages a day must be read to finish the homework?", None),
    ("A 300-page novel has 60 pages already read. How many pages a day must be read to finish the lab report? She must finish the novel in 8 days.", None),
    ("Where two lines cross, the opposite angles form a right angle: (3x + 0)° and (2x + 30)°. Find x.", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is the sum of its sides if the length is shorter than the width?", None),
    ("A rectangle has a perimeter of 34 m and an area of 60 m^2. What is its length if the length is less than the length?", None),
]
