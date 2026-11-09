"""Thirty-seventh fresh set for word_solver.py: neighbours of the wordings fixed in batch 34 (temperature "how many hours" without whole / full, and a candle question that
is not the question about the candles), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

FRESH = [
    ("The temperature is 30°F and falling 4°F per hour. For how many full hours will it stay at or above 5°F?", [6]),
    ("One candle is 20 cm tall and burns 2 cm per hour. Another is 32 cm tall and burns 4 cm per hour. After how many hours will they be the same height?", [6]),
    ("When will they be the same height? One candle is 20 cm tall and burns 2 cm per hour. Another is 32 cm tall and burns 4 cm per hour.", [6]),
    ("One candle is 20 cm tall and burns 2 cm per hour, and another is 32 cm tall and burns 4 cm per hour. When will they be the same height?", [6]),
    ("The temperature is 30°F and falling 4°F per hour. For how many hours will it stay at or above 5°F?", None),
    ("The temperature is 30°F and falling 4°F per hour. For how many hours in a row will it stay at or above 5°F?", None),
    ("One candle is 20 cm tall and burns 2 cm per hour. Another is 32 cm tall and burns 4 cm per hour when they are the same height. How old is the candle?", None),
    ("One candle is 20 cm tall and burns 2 cm per hour. Another is 32 cm tall and burns 4 cm per hour. They were the same height last week. When will the shop open?", None),
    ("One candle is 20 cm tall and burns 2 cm per hour. Another is 32 cm tall and burns 4 cm per hour. They were the same height at noon. When will they be the same height?", None),
]
