"""Stage 1a of the paste-text operator: a thin call into the existing solvers.

analyze(text) asks word_solver.solve() first, then number_puzzle.solve() if that
returns None. It returns the solver's own family, equation, reading and values.
It does not invent role labels, guess with the trained matcher, place a row, or
touch the GUI.

    analyze("Wren is 4 times as old as Jamal. In 5 years, the sum of their ages will be 105. How old is each now?")
    -> PasteResult(supported=True, family='times_as_old_future_sum',
                   values=[19, 76], equation='(x + 5) + (4*x + 5) = 105', ...)

    analyze("not a problem")
    -> PasteResult(supported=False, family=None, values=[], equation=None,
                   reading='Unsupported problem — no matching solution found.')

Standard library only. Stage 1b (Templates-box button) is not built.
"""
from collections import namedtuple

import number_puzzle as NP
import word_solver as WS

UNSUPPORTED = "Unsupported problem — no matching solution found."

PasteResult = namedtuple("PasteResult", "supported family values equation reading")


def _decline():
    return PasteResult(False, None, [], None, UNSUPPORTED)


def analyze(text):
    """PasteResult for pasted algebra-word-problem text.

    word_solver.solve() first. If that is None, number_puzzle.solve().
    A decline is returned when the text is empty, is not a string, or neither
    solver claims it. Values stay fractions.Fraction; readings stay the
    solvers' own strings.
    """
    if not isinstance(text, str) or not text.strip():
        return _decline()
    result = WS.solve(text)
    if result is not None:
        return PasteResult(True, result.family, list(result.values), result.equation, result.reading)
    puzzle = NP.solve(text)
    if puzzle is not None:
        return PasteResult(True, "number_puzzle", [puzzle.answer], puzzle.equation, puzzle.reading)
    return _decline()
