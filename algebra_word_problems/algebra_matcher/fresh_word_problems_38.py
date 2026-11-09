"""Thirty-eighth fresh set for word_solver.py: neighbours of the wordings fixed in batch 35 ("the same height as <something else>" and a request without a question word
in another sentence), written AFTER the fixes were finished, run once, untuned.
Each item: (problem, amounts increasing) or None = must decline."""

CANDLES = "One candle is 20 cm tall and burns 2 cm per hour. Another is 32 cm tall and burns 4 cm per hour. "

FRESH = [
    (CANDLES + "When will they be the same height as each other?", [6]),
    (CANDLES + "When will the first candle be the same height as the other candle?", [6]),
    (CANDLES + "Find when they will be the same height.", [6]),
    (CANDLES + "When will they be the same height as the bookshelf?", None),
    ("Determine the height of the room. " + CANDLES + "When will they be the same height?", None),
    (CANDLES + "When will they be the same height as each other and the wall?", None),
    ("Find the price of the candles. " + CANDLES + "When will they be the same height?", None),
]
