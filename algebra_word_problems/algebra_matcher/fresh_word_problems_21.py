"""Twenty-first fresh set for word_solver.py: wordings for the three families added with the 'score' fix (percent_change_between,
ages_later_multiple, shared_fixed_cost), written AFTER all three were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("A bike's price went from $400 to $340. What is the percent change?", [-15]),
    ("The school's enrollment changed from 800 to 1,000 students. By what percent did it change?", [25]),
    ("Ben is 4 times as old as Cara. In 6 years, Ben will be 2 times as old as Cara. How old is each now?", [3, 12]),
    ("Ben is 3 times as old as Cara. In 10 years, Ben will be twice as old as Cara. How old is each now?", [10, 30]),
    ("A class trip costs $480 for the van plus $10 admission per kid. Each kid pays $22 in total. How many kids?", [40]),
    ("A concert bus costs $600 plus $5 per ticket. The bus is split equally and each person pays $25 in total. How many people?", [30]),
    ("A bike's price went from $400 to $340. What is the percent decrease?", None),
    ("A bike's price went from $0 to $340. What is the percent change?", None),
    ("Ben is 4 times as old as Cara. 6 years ago, Ben was 6 times as old as Cara. How old is each now?", None),
    ("Ben is 4 times as old as Cara. In 6 years, Ben will be 4 times as old as Cara. How old is each now?", None),
    ("A class trip costs $480 for the van plus $10 admission per kid. Each kid pays $22 in total. How much is the van per kid?", None),
    ("A class trip costs $480 for the van plus $10 admission per kid. Each kid pays $24 in total. How many kids?", None),
]
