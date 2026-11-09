"""Thirty-sixth fresh set for word_solver.py: wordings for the three families added together (temperature_whole_hours, two_candles_equal, transversal_equal_angles),
written AFTER all three were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("The temperature is 40°F and falling 6°F per hour. For how many whole hours will it stay at or above 10°F?", [5]),
    ("The temperature is 40°F and falling 6°F per hour. For how many whole hours will it stay above 10°F?", [4]),
    ("One candle is 30 cm tall and burns 3 cm per hour. Another is 42 cm tall and burns 5 cm per hour. When will they be the same height?", [6]),
    ("One candle is 9 cm tall and burns 1.5 cm per hour. Another is 15 cm tall and burns 3 cm per hour. When will they be the same height?", [4]),
    ("Two parallel lines are cut by a transversal. A pair of corresponding angles measure (3x + 15)° and (5x - 25)°. Find x and the angle.", [20, 75]),
    ("Two parallel lines are cut by a transversal. A pair of alternate interior angles measure (4x - 10)° and (2x + 30)°. Find the angle.", [70]),
    ("The temperature is 40°F and rising 6°F per hour. For how many whole hours will it stay at or above 10°F?", None),
    ("The temperature is 40°F and falling 6°F per hour. For how many whole hours will it stay at or below 10°F?", None),
    ("One candle is 6 cm tall and burns 3 cm per hour. Another is 24 cm tall and burns 9 cm per hour. When will they be the same height?", None),
    ("One candle is 30 cm tall and burns 3 cm per hour. Another is 42 cm tall and burns 5 cm per hour. How tall will they be when they are the same height?", None),
    ("Two parallel lines are cut by a transversal. A pair of same-side interior angles measure (3x + 15)° and (5x - 25)°. Find x and the angle.", None),
    ("Two parallel lines are cut by a transversal. A pair of corresponding angles measure (3x + 15)° and (3x - 25)°. Find x and the angle.", None),
]
