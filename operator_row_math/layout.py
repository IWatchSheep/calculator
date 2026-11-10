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


# ----------------------------------------------------------------------------------------------------------------------------------------------
# fractions: a "/" in a formula is always written top to bottom, the numerator on the row above and the denominator on the row below a bar
# ----------------------------------------------------------------------------------------------------------------------------------------------
OPEN = {"(": ")", "[": "]", "{": "}", "\u2308": "\u2309", "\u230a": "\u230b"}
CLOSE = set(OPEN.values())
TOGGLE = {"|", "\u2016"}                                    # | and the norm bars open and close alternately
STOP = {"=", "+", "\u2212", "-", "\u00b1", ",", ";", ":", "\u2248", "\u2264", "\u2265", "<", ">", "\u2260", "\u2192", "\u21d2", "\u2194", "\u2208", "\u2209",
        "\u2282", "\u2286", "\u221d", "\u22a3", "\u2227", "\u2228", "\u2229", "\u222a", "/", "\u2243", "\u2245", "\u21c9"}
WORDS = {"and", "or", "for", "else", "when", "from", "to", "along", "with", "where", "if"}          # words in a formula end a numerator or denominator
TIMES = {"\u00d7", "\u00b7"}


def _matches(cards):
    stack, match, bars = [], {}, {}
    for i, (kind, text) in enumerate(cards):
        if kind != "op":
            continue
        if text in OPEN:
            stack.append((i, text))
        elif text in CLOSE:
            for p in range(len(stack) - 1, -1, -1):
                if OPEN[stack[p][1]] == text:
                    match[stack[p][0]] = i
                    match[i] = stack[p][0]
                    del stack[p:]
                    break
        elif text in TOGGLE:
            if text in bars:
                o = bars.pop(text)
                match[o] = i
                match[i] = o
            else:
                bars[text] = i
    return match


def group_fractions(cards, levels):
    """Which cards of a row are the numerator or the denominator of a fraction.

    cards = [(kind, text)], levels = their super/subscript levels.  Returns a list with one entry per card: [] for a card on the ordinary line, or a list of (group, part)
    for the fractions it is inside, outermost first, where part is "n" (numerator), "d" (denominator), "bar" (the "/" card, not drawn) or "hide" (the brackets that
    only wrapped a whole numerator or denominator, not drawn).  The numerator is everything before the "/" back to the nearest + - = , or opening bracket (a product
    stays in it); the denominator is the first factor after it: a bracketed group alone, otherwise a run of symbols (a product only when nothing after it is bracketed)."""
    n = len(cards)
    match = _matches(cards)
    is_open = lambda j: cards[j][0] == "op" and (cards[j][1] in OPEN or (cards[j][1] in TOGGLE and match.get(j, j) > j))        # noqa: E731
    is_close = lambda j: cards[j][0] == "op" and (cards[j][1] in CLOSE or (cards[j][1] in TOGGLE and match.get(j, j) < j))      # noqa: E731
    is_stop = lambda j: cards[j][0] == "op" and (cards[j][1] in STOP or (cards[j][1] in TOGGLE and j not in match))             # noqa: E731
    fractions = []
    for s, (kind, text) in enumerate(cards):
        if kind != "op" or text != "/":
            continue
        j, start = s - 1, s
        while j >= 0:
            if cards[j][0] == "op" and (cards[j][1] in STOP or cards[j][1] in WORDS or is_open(j)):
                break
            if is_close(j):
                start = match[j]
                j = start - 1
                continue
            start = j
            j -= 1
        if start == s:
            continue

        def factor(j):
            e = j
            while e < n:
                if cards[e][0] == "op" and (cards[e][1] in STOP or cards[e][1] in WORDS or cards[e][1] in TIMES or is_close(e)):
                    break
                e = match[e] + 1 if is_open(e) else e + 1
            return e

        d0 = s + 1
        if d0 >= n:
            continue
        if is_open(d0):
            end = match[d0] + 1
            while end < n and (levels[end] != 0 or (cards[end][0] == "op" and cards[end][1] == "\u2032")):
                end += 1
        else:
            end = factor(d0)
            while end < n and cards[end][0] == "op" and cards[end][1] in TIMES:
                nxt = factor(end + 1)
                if nxt == end + 1 or any(is_open(k) for k in range(end + 1, nxt)):
                    break
                end = nxt
        if end == d0:
            continue
        words = [cards[k] for k in list(range(start, s)) + list(range(d0, end))]
        if words and all(k == "op" and t.isalpha() and len(t) > 1 for k, t in words):
            continue                                       # "yes / no" is text, not a fraction
        hide = []
        for a, b in ((start, s), (d0, end)):
            if b - a >= 2 and cards[a] == ("op", "(") and match.get(a) == b - 1:
                hide += [a, b - 1]
        fractions.append((start, s, d0, end, hide))
    fracs = [[] for _ in range(n)]
    for gid, (start, s, d0, end, hide) in sorted(enumerate(fractions, 1), key=lambda x: -(x[1][3] - x[1][0])):
        gid = gid
        for i in range(start, end):
            if i == s:
                fracs[i].append((gid, "bar"))
            elif i in hide:
                fracs[i].append((gid, "hide"))
            else:
                fracs[i].append((gid, "n" if i < s else "d"))
    return fracs
