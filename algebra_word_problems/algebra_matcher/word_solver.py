"""Solves five families of algebra word problems directly from the wording, with a role for every number.

    sum_difference   two numbers with a sum and a difference / "one is 8 bigger than the other"
                     (also a board cut in two, and two ages)
    consecutive      the sum of k consecutive [even|odd] integers
    work_together    two workers' separate times -> time together
    percent_change   a price after a percent rise (raise, markup, tax, tip) or fall (discount, off)
    proportion       "3 kg cost $7.50, how much do 8 kg cost?"  (direct proportion, three numbers)

How it stays safe (the rule from number_puzzle.py): a family only answers when
  1. its wording pattern matches,
  2. EVERY number in the problem was given a role by the pattern (a leftover number means decline), and
  3. the answer passes a sanity check (a count of people is whole, a time is positive ...).
Anything else returns None, so the matcher can take over.  A wrong role must never become a wrong answer.

    solve("Rent went up 5% to $1,260 a month. What was the old rent?")
    -> Result(family='percent_change', values=[Fraction(1200, 1)], equation='1.05x = 1260', ...)

Standard library only.
"""
import re
from collections import namedtuple
from fractions import Fraction

import number_puzzle as NP

Result = namedtuple("Result", "family values equation reading")

NUM = r"(\d+(?:\.\d+)?)"
_SMALL = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
_KWORD = "(?:" + "|".join(_SMALL) + r"|\d+)"


def fr(text):
    """'7.50' -> Fraction(15, 2);  'three' -> 3"""
    return Fraction(_SMALL[text]) if text in _SMALL else Fraction(text)


def clean(problem):
    """Lower-case text with $ and thousands commas removed, 'percent' -> '%'.  Returns (text, money_positions)."""
    t = problem.strip().replace("’", "'").replace("−", "-")
    t = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", t)
    t = re.sub(r"\bper\s?cent\b|\bpercent\b", "%", t, flags=re.I)
    return t.lower()


def digit_numbers(problem):
    """Every number written in digits, in order, as (value, is_money, start, end) taken from the cleaned text."""
    t = clean(problem)
    return [(Fraction(m.group(2)), bool(m.group(1)), m.start(), m.end()) for m in re.finditer(r"(\$)?\s?(\d+(?:\.\d+)?)", t)]


def n_numbers(problem):
    return len(digit_numbers(problem))


def show(v):
    v = Fraction(v)
    if v.denominator == 1:
        return str(v.numerator)
    f = float(v)
    s = ("%.4f" % f).rstrip("0").rstrip(".")
    return s


def show_exact(v):
    """The value as an exact fraction, never a rounded decimal."""
    v = Fraction(v)
    return str(v.numerator) if v.denominator == 1 else "%d/%d" % (v.numerator, v.denominator)


def show_answer(v, money):
    """Exact value for the reading. Money that is not a whole number of cents also shows the nearest cent."""
    v = Fraction(v)
    text = show_exact(v)
    if not money:
        return text
    cents = Fraction(round(v * 100), 100)
    if cents == v:
        return text
    return "%s (%s to the nearest cent)" % (text, show(cents))


def solve_linear(lhs, rhs):
    """lhs = rhs where both are NP.Lin; the exact value of x, or None."""
    d = lhs.a - rhs.a
    if d == 0:
        return None
    return (rhs.b - lhs.b) / d


def x_plus(*terms):
    """Build a Lin from (coefficient, constant) pairs added together."""
    out = NP.Lin(0, 0)
    for a, b in terms:
        out = out + NP.Lin(a, b)
    return out


# ---------------------------------------------------------------------------------------------------------
# 1. two numbers with a sum and a difference
# ---------------------------------------------------------------------------------------------------------
_MORE = r"(?:more|bigger|larger|greater|longer|higher|taller|heavier|older)"
_SUM_DIFF = [
    # "The sum of two numbers is 235 and their difference is 103."
    (re.compile(r"\bthe sum of two numbers is " + NUM + r" and their difference is " + NUM), lambda S, D, *_: (S, D)),
    # "Find two numbers that add to 50 if one is 8 bigger than the other."
    (re.compile(r"\btwo numbers (?:that |which )?(?:add|sum|total)(?: up)?(?: to| is| are)? " + NUM + r"\b.*?\bone (?:of them )?is " + NUM + r" " + _MORE + r" than the other"), lambda S, D, *_: (S, D)),
    # "A 93 cm board is cut into two pieces. One piece is 25 cm longer than the other."
    (re.compile(r"\ba " + NUM + r" ?(?:cm|m|mm|km|ft|feet|foot|in|inch|inches|yd|yards?|meters?|metres?)\b (?:board|rope|wire|stick|ribbon|pipe|string|rod|plank|pole|cable|bar) is (?:cut|divided|broken|split) into two (?:pieces|parts)\b.*?\bone (?:piece|part) is " + NUM + r" (?:cm|m|mm|km|ft|feet|foot|in|inch|inches|yd|yards?|meters?|metres?) " + _MORE + r" than the other"), lambda S, D, *_: (S, D)),
]
_AGE_SUM = re.compile(r"\b([a-z']+) is " + NUM + r" years? older than ([a-z']+)\. the sum of their ages is " + NUM)


def sum_difference(problem):
    t = clean(problem)
    if n_numbers(problem) not in (2,):
        return None
    for rx, roles in _SUM_DIFF:
        m = rx.search(t)
        if m and len(m.groups()) == 2:
            S, D = fr(m.group(1)), fr(m.group(2))
            big, small = (S + D) / 2, (S - D) / 2
            if D <= 0 or small <= 0:
                return None
            return Result("sum_difference", [big, small], "x + y = %s;  x - y = %s" % (show(S), show(D)),
                          "two numbers with sum %s and difference %s: larger = %s, smaller = %s" % (show(S), show(D), show(big), show(small)))
    return None


def age_sum(problem):
    t = clean(problem)
    m = _AGE_SUM.search(t)
    if not m or n_numbers(problem) != 2:
        return None
    older, d, younger, S = m.group(1), fr(m.group(2)), m.group(3), fr(m.group(4))
    y = (S - d) / 2
    if y <= 0 or y.denominator != 1:
        return None
    return Result("sum_difference", [y, y + d], "x + (x + %s) = %s" % (show(d), show(S)),
                  "%s is %s older than %s, ages add to %s: %s is %s, %s is %s" % (older, show(d), younger, show(S), younger, show(y), older, show(y + d)))


# ---------------------------------------------------------------------------------------------------------
# 2. consecutive integers
# ---------------------------------------------------------------------------------------------------------
_CONSEC = [
    re.compile(r"\b(?:the )?(?:sum|total) of (" + _KWORD + r") consecutive (even |odd )?(?:whole )?(?:integers|numbers) (?:is|equals|=) " + NUM),
    re.compile(r"\b(?:add up|adding|add) (" + _KWORD + r") (even |odd )?(?:consecutive )?(?:integers|numbers) in a row.*?\b(?:get|equals?|is|total) " + NUM),
    re.compile(r"\b(" + _KWORD + r") (even |odd )?(?:consecutive )?(?:integers|numbers) in a row (?:sum|add|total)(?: up)?(?: to| is)? " + NUM),
    re.compile(r"\b(" + _KWORD + r") consecutive (even |odd )?(?:integers|numbers) (?:sum|add|total)(?: up)?(?: to)? " + NUM),
]


def consecutive(problem):
    t = clean(problem)
    for rx in _CONSEC:
        m = rx.search(t)
        if not m:
            continue
        k_text = m.group(1)
        k = int(fr(k_text))
        kind = (m.group(2) or "").strip()
        S = fr(m.group(3))
        expected = 1 + (1 if k_text.isdigit() else 0)
        if n_numbers(problem) != expected or k < 2 or k > 10:
            return None
        step = 2 if kind else 1
        offset = step * k * (k - 1) // 2
        x = (S - offset) / k
        if x.denominator != 1:
            return None
        x = int(x)
        if kind == "even" and x % 2 or kind == "odd" and x % 2 == 0:
            return None
        vals = [Fraction(x + step * i) for i in range(k)]
        terms = " + ".join(["x"] + ["(x + %d)" % (step * i) for i in range(1, k)])
        return Result("consecutive", vals, "%s = %s" % (terms, show(S)),
                      "%d consecutive %sintegers add to %s: %dx + %d = %s, so x = %d" % (k, kind + " " if kind else "", show(S), k, offset, show(S), x))
    return None


# ---------------------------------------------------------------------------------------------------------
# 3. two workers, separate times -> together
# ---------------------------------------------------------------------------------------------------------
_TIME_UNIT = r"(hours?|hrs?|minutes?|mins?|days?|weeks?)"
_TOGETHER = r"\b(together|both|team(?:s|ed)? up|combined|at the same time|jointly)\b"
_ONE_WORKER = r"\b(alone|the other|each other|one of them)\b"


def _time_unit(word):
    word = re.sub(r"s$", "", word)
    return {"hr": "hour", "hour": "hour", "min": "minute", "minute": "minute", "day": "day", "week": "week"}.get(word, word)


def work_together(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 2:
        return None
    # "alone" in the setup is fine ("Tom paints a fence alone in 6 hours"). Decline only when the
    # question itself asks for one worker's time, or when one rate is a drain rather than a worker.
    questions = [x for x in re.split(r"(?<=[.!?])\s+", t) if x.strip().endswith("?")]
    if len(questions) != 1 or not re.search(_TOGETHER, questions[0]) or re.search(_ONE_WORKER, questions[0]):
        return None
    # a together-word BEFORE the question means the setup already gives the combined time (or says the workers
    # team up); then one of the two numbers is not a separate worker's time, so decline
    if re.search(_TOGETHER, t[:t.index(questions[0])]):
        return None
    if re.search(r"\b(?:drain|leak|empt|plug|overflow)\w*|\bout of\b", t) or "%" in t or "$" in problem:
        return None
    units = []
    for i, (_v, _money, _start, end) in enumerate(nums):
        m = re.match(r"\s*" + _TIME_UNIT + r"\b", t[end:])
        if m:
            units.append(_time_unit(m.group(1)))
        elif i == 1 and units and re.search(r"\bin\s+\d+(?:\.\d+)?$", t[:end]):
            units.append(units[0])          # "in 6 hours, Sue in 3" — the second time keeps the first unit
        else:
            return None
    if units[0] != units[1]:
        return None
    if not re.search(r"\bhow (?:long|many (?:hours|minutes|days|weeks)|much time)\b", questions[0]):
        return None
    a, b = nums[0][0], nums[1][0]
    if a <= 0 or b <= 0:
        return None
    tt = a * b / (a + b)
    return Result("work_together", [tt], "t/%s + t/%s = 1" % (show(a), show(b)),
                  "one takes %s and the other %s %ss; together t/%s + t/%s = 1, so t = %s %ss" % (show(a), show(b), units[0], show(a), show(b), show_exact(tt), units[0]))


# ---------------------------------------------------------------------------------------------------------
# 4. a price after a percent change
# ---------------------------------------------------------------------------------------------------------
_UP = r"\b(raise|raised|markup|marked up|marks up|mark up|increase|increased|went up|goes up|rose|risen|tax|tip|gratuity|adds|added|surcharge|service charge|inflation)\b"
_DOWN = r"\b(discount|discounted|off|marked down|mark down|reduced|reduction|decrease|decreased|dropped|fell|cheaper|sale)\b"
_ASK_BEFORE = r"\b(before|original|old|wholesale|without|initial|earlier|itself|what did (?:the )?(?:store|shop|company|owner|dealer|\w+) (?:pay|spend)|what was the cost)\b"


def percent_change(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 2 or t.count("%") != 1:
        return None
    pct = [n for n in nums if t[n[3]:n[3] + 2].strip().startswith("%")]
    other = [n for n in nums if n not in pct]
    if len(pct) != 1 or len(other) != 1:
        return None
    if re.search(r"\b(interest|commission|per month|each month|a year|annual|compound|profit|loss|of which|out of|sav(?:e|es|ed|ing|ings)|gain(?:ed)?|lost|difference|fee)\b", t):
        return None
    if re.search(r"(?:\bby|\bof) \$\d|\$\d[0-9.]* (?:off|more|less|extra|extra)", problem.lower().replace(",", "")):
        return None
    up, down = bool(re.search(_UP, t)), bool(re.search(_DOWN, t))
    if up == down:
        return None
    sentences = [x for x in re.split(r"(?<=[.!?])\s+", t) if x.strip().endswith("?")]
    if len(sentences) != 1 or not re.search(_ASK_BEFORE, sentences[0]):
        return None
    r, P = pct[0][0], other[0][0]
    factor = Fraction(100 + (r if up else -r), 100)
    if factor <= 0:
        return None
    x = P / factor                                 # exact; the nearest cent is only for the reading
    f = show(factor)
    money = other[0][1] or "$" in problem
    return Result("percent_change", [x], "%sx = %s" % (f, show(P)),
                  "%s%% %s the old value to give %s: %sx = %s, so x = %s" % (show(r), "added to" if up else "taken off", show(P), f, show(P), show_answer(x, money)))


# ---------------------------------------------------------------------------------------------------------
# 5. direct proportion with three numbers
# ---------------------------------------------------------------------------------------------------------
_REJECT_PROP = re.compile(r"\b(inverse|inversely|workers?|men|pipes?|taps?|pumps?|faster|slower|speeds?|km/h|kmh|mph|kph|ratio|average|mean|angle|degrees?|scale|map|similar|shadow|tall|height)\b|%|:")


def unit_after(t, end):
    m = re.match(r"\s*(?:of\s+)?([a-z]+)", t[end:])
    if not m:
        return ""
    u = m.group(1)
    u = {"hrs": "hour", "hr": "hour", "kilograms": "kg", "kilogram": "kg", "kgs": "kg", "pounds": "lb", "lbs": "lb"}.get(u, u)
    return re.sub(r"(?<=[a-z])s$", "", u) if len(u) > 3 else u


def proportion(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or _REJECT_PROP.search(t):
        return None
    q = re.search(r"\bhow (?:much|many|long|far)\b", t)
    if not q:
        return None
    # roles by position: the known pair comes BEFORE the question, the quantity asked about comes AFTER it
    if not (nums[0][2] < q.start() and nums[1][2] < q.start() and nums[2][2] > q.start()):
        return None
    if re.search(r"\d\s+and\s+\d|\btogether\b|\bper (?:minute|hour|second|day|week)\b", t):
        return None
    if re.search(r"(?:/|=|\bfirst\b|after that|overtime|split|among|times as|more than|less than|plus|minus|\bis \d)", t):
        return None
    if not re.search(r"\b(cost|costs|price|pay|pays|paid|earn|earns|for|per|rate|varies directly|needs|need|uses|use|travels|travel|drives|weigh|weighs|buy|gets|makes)\b", t):
        return None
    units = ["$" if n[1] else unit_after(t, n[3]) for n in nums]
    u1, u2, u3 = units
    if not (u1 and u2 and u3) or u1 == u2:
        return None
    (a, _, _, _), (b, _, _, _), (c, _, _, _) = nums
    if u3 == u1:
        x, rule = b * c / a, "%s per %s" % (show(b / a), u1)
    elif u3 == u2:
        x, rule = a * c / b, "%s per %s" % (show(a / b), u2)
    else:
        return None
    if x <= 0 or a == 0 or b == 0:
        return None
    return Result("proportion", [x], "%s/%s = x/%s" % (show(a), show(b), show(c)) if u3 == u2 else "%s/%s = x/%s" % (show(b), show(a), show(c)),
                  "%s: %s, so x = %s" % ("direct proportion", rule, show(x)))


# ---------------------------------------------------------------------------------------------------------
FAMILIES = [sum_difference, age_sum, consecutive, work_together, percent_change, proportion]


def solve(problem):
    """Result for the first family that matches and passes every check; otherwise None.
    If two different families both claim the problem with different answers, decline."""
    found = []
    for fam in FAMILIES:
        try:
            r = fam(problem)
        except (ZeroDivisionError, ValueError, KeyError, IndexError):
            r = None
        if r is not None:
            found.append(r)
    if not found:
        return None
    if any(f.values != found[0].values for f in found[1:]):
        return None
    return found[0]


def answer_text(r):
    return " and ".join(show_exact(v) for v in r.values)


if __name__ == "__main__":
    import sys
    r = solve(" ".join(sys.argv[1:]))
    print("no family claims this problem" if r is None else "%s: %s  ->  %s\n  %s" % (r.family, r.equation, answer_text(r), r.reading))
