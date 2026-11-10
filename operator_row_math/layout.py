"""Where a card sits on the grid of a row.

Every card is its own column.  A card can also sit on another ROW of the grid: an exponent is one row up (level -1), a subscript or the lower limit of a sigma
one row down (level +1), everything else on the main line (level 0).  The picture writes these as superscript / subscript characters (r\u00b2, a\u2099, \u03a3\u2099),
so the level of a token is read from its character: level_of("\u00b2") == -1, level_of("\u2099") == 1, level_of("+") == 0.
"""
import unicodedata


def level_of(token):
    """-1 for a superscript token, +1 for a subscript token, 0 for anything else."""
    marks = {unicodedata.decomposition(c).split(" ")[0] if unicodedata.decomposition(c) else "" for c in token}
    if marks == {"<super>"}:
        return -1
    if marks == {"<sub>"}:
        return 1
    return 0


def shown(token):
    """What the card shows: an exponent or subscript is shown as the ordinary characters (2, not \u00b2), since it has its own cell."""
    return unicodedata.normalize("NFKC", token) if level_of(token) else token
