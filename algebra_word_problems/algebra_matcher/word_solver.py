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
# a number written as a word: "two coats", "twice", "another" (the ordinal "second" is not the unit "seconds")
_SPELLED = r"\b(?:two|three|four|five|six|seven|eight|nine|ten|twice|double|triple|half|another|second)\b"
# workers multiplied or rates changed: "two teams", "three such pairs", "twice as fast", "half the time"
# a count hidden in a word: "both coats", "a pair of phones", "a couple of coats"
_GROUPED = r"\b(?:both|pairs?|couple)\b"
# "both pairs", "both teams" multiply the workers; the bare "Running both, how long" is how a printer problem asks for the total
_BOTH_GROUPS = r"\bboth\s+(?:pairs?|teams?|crews?|groups?|sets?|copies)\b"
_SPELLED_REPEAT = (r"\b(?:two|three|four|five|six|seven|eight|nine|ten)\s+(?:such\s+|identical\s+|similar\s+|more\s+)?(?:pairs?|teams?|crews?|groups?|sets?|copies)\b"
                   r"|\b(?:twice|double|triple|half)\b")
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
    # "two such pairs", "two teams like them", "twice as fast": the workers are multiplied or their rates changed
    if re.search(_SPELLED_REPEAT, t) or re.search(_BOTH_GROUPS, t) or re.search(r"\b(?:such|identical|like them|just like)\b", t):
        return None
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
    # "two coats cost $170": a number written as a word multiplies the thing asked about, so decline
    if re.search(_SPELLED, t) or re.search(_GROUPED, t):
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
    # a number written as a word ("two printers", "twice", "another") is a number with no role: decline
    if re.search(r"\b(?:two|three|four|five|six|seven|eight|nine|ten|twice|double|triple|half|another|second|both)\b", t):
        return None
    if re.search(r"\d\s+and\s+\d|\btogether\b|\bper (?:minute|hour|second|day|week)\b", t):
        return None
    if re.search(r"(?:/|=|\bfirst\b|after that|overtime|split|among|times as|more than|less than|plus|minus|\bis \d)", t):
        return None
    if not re.search(r"\b(cost|costs|price|pay|pays|paid|earn|earns|for|per|rate|varies directly|needs|need|uses|use|travels|travel|drives|weigh|weighs|buy|gets|makes|cover|covers|stamp|stamps|print|prints)\b", t):
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
# ---------------------------------------------------------------------------------------------------------
# 6. two solutions with different percents mixed to a target percent
#    p1*x + p2*(T - x) = target*T      (the generator's "mixture" and "x_alloy")
# ---------------------------------------------------------------------------------------------------------
_AMOUNT_UNIT = (r"(?:liters?|litres?|l|ml|milliliters?|millilitres?|kg|kilograms?|g|grams?|oz|ounces?|lbs?|pounds?|"
                r"gallons?|quarts?|cups?)")
# anything that is a different mixing shape (adding water or pure stuff, evaporating, draining, replacing, price per pound)
_MIX_OTHER = re.compile(r"\b(?:water|pure|evaporat\w*|boil\w*|drain\w*|replac\w*|remov\w*|dilut\w*|add|adds|added|adding|"
                        r"price|priced|cost|costs|per pound|per lb|worth|selling)\b|/lb|\$")
_MIX_EXTRA = re.compile(r"\b(?:times as|twice|double|triple|half|as much|ratio|more than|less than|each of the)\b")
_MIX_MAKE = re.compile(r"\b(?:make|makes|making|get|gets|need|needs|needed|obtain|produce|produces|want|wants|total|of the mixture)\b")


def two_solution_mix(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    # "How much of the 10% do you use?" repeats a source percent to say which amount is asked for: it is not a new number
    q = t.rfind("how ")
    if q != -1:
        for n in list(nums):
            if n[2] > q and t[n[3]:n[3] + 1] == "%" and re.search(r"\bthe\s*$", t[:n[2]]) and any(m is not n and m[0] == n[0] and m[2] < q for m in nums):
                nums.remove(n)
    if len(nums) != 4 or "$" in problem:
        return None
    # "two solutions" / "another alloy" are the shape of this problem; a bigger spelled count (three batches ...) is not
    if _MIX_OTHER.search(t) or _MIX_EXTRA.search(t) or re.search(r"\b(?:three|four|five|six|seven|eight|nine|ten)\b", t):
        return None
    if not re.search(r"\b(?:mix\w*|combin\w*|blend\w*|alloy\w*|solutions?|make|use)\b", t):
        return None
    if not re.search(r"\bhow (?:much|many)\b", t):
        return None
    pct = [n for n in nums if t[n[3]:n[3] + 2].strip().startswith("%")]
    amt = [n for n in nums if n not in pct]
    if len(pct) != 3 or len(amt) != 1:
        return None
    T, a_start, a_end = amt[0][0], amt[0][2], amt[0][3]
    # the amount must be followed by a unit, and introduced by "make / get / need ..." (the total wanted)
    um = re.match(r"\s*(" + _AMOUNT_UNIT + r")\b", t[a_end:])
    if not um or not _MIX_MAKE.search(" ".join(t[:a_start].split()[-3:])):
        return None
    # the target is the percent that comes right after the amount (within six words)
    after = [n for n in pct if n[2] >= a_end]
    if not after:
        return None
    target_n = min(after, key=lambda n: n[2])
    if len(t[a_end:target_n[2]].split()) > 6:
        return None
    sources = [n for n in pct if n is not target_n]
    p1, p2, tg = sources[0][0], sources[1][0], target_n[0]
    if p1 == p2 or not (min(p1, p2) < tg < max(p1, p2)) or T <= 0:
        return None
    x1 = T * (tg - p2) / (p1 - p2)
    x2 = T - x1
    if x1 <= 0 or x2 <= 0:
        return None
    unit = um.group(1)
    eq = "%sx + %s(%s - x) = %s(%s)" % (show(p1 / 100), show(p2 / 100), show(T), show(tg / 100), show(T))
    return Result("two_solution_mix", [x1, x2], eq,
                  "x = amount of the %s%% solution, %s - x of the %s%%: %s, so x = %s %s of the %s%% and %s %s of the %s%%" % (
                      show(p1), show(T), show(p2), eq, show_exact(x1), unit, show(p1), show_exact(x2), unit, show(p2)))


# ---------------------------------------------------------------------------------------------------------
# 7. money split between two interest rates:   r1*x + r2*(T - x) = I      (the generator's "interest")
# ---------------------------------------------------------------------------------------------------------
_INT_WORD = re.compile(r"\b(?:interest|earn|earns|earned|earning|earnings|yield|yields|yielded|return|returns)\b")
_INT_OTHER = re.compile(r"\b(?:compound\w*|monthly|quarterly|per month|each month|a month|semi|daily|months?|two years|how long|how many years|"
                        r"same interest|equal|equally|overall|such|of the year|for part of|of the time|how much more|extra|additional|rate of|what rate|loan|borrow\w*|owe\w*|"
                        r"times as|twice|double|triple|half|as much|more than|less than|three|four|five|six|seven|eight|nine|ten)\b")
_INVEST_WORD = re.compile(r"\b(?:invest\w*|account|accounts|deposit\w*|savings|bonds?|put|saved|fund|funds)\b")


def two_rate_interest(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    # "How much was invested at 6%?" repeats one of the two rates to say which amount is asked for: not a new number
    q = t.rfind("how ")
    if q != -1:
        for n in list(nums):
            if n[2] > q and t[n[3]:n[3] + 1] == "%" and any(m is not n and m[0] == n[0] and m[2] < q for m in nums):
                nums.remove(n)
    if len(nums) != 4:
        return None
    pct = [n for n in nums if t[n[3]:n[3] + 2].strip().startswith("%")]
    money = [n for n in nums if n not in pct]
    if len(pct) != 2 or len(money) != 2 or not all(n[1] for n in money):
        return None
    if _INT_OTHER.search(t) or not _INT_WORD.search(t) or not _INVEST_WORD.search(t):
        return None
    if not re.search(r"\bhow much\b", t):
        return None
    # the money invested must be SPLIT between the two rates ("part ... the rest", "some ... and some", "two accounts"):
    # otherwise the first amount may be the money at one rate only, and the equation is different
    if not re.search(r"\b(?:rest|remainder|remaining|part|some|split|divided|each|one at|two (?:accounts|funds|bonds|investments|loans))\b", t):
        return None
    # the interest is the amount nearest a word like "interest" / "earned"; the other amount is the money invested
    words = t.split()
    marks = [i for i, w in enumerate(words) if _INT_WORD.fullmatch(w.strip(".,;:?!"))]
    if not marks:
        return None

    def word_index(n):
        return len(t[:n[2]].split())

    dist = [min(abs(word_index(n) - m) for m in marks) for n in money]
    if abs(dist[0] - dist[1]) < 2:
        return None
    interest, total = (money[0], money[1]) if dist[0] < dist[1] else (money[1], money[0])
    I, T = interest[0], total[0]
    r1, r2 = pct[0][0], pct[1][0]
    if r1 == r2 or T <= 0 or I <= 0:
        return None
    x1 = (I - r2 * T / 100) / ((r1 - r2) / 100)          # invested at the first rate
    x2 = T - x1
    if x1 <= 0 or x2 <= 0:
        return None
    eq = "%sx + %s(%s - x) = %s" % (show(r1 / 100), show(r2 / 100), show(T), show(I))
    return Result("two_rate_interest", [x1, x2], eq,
                  "x = amount at %s%%, %s - x at %s%%: %s, so $%s at %s%% and $%s at %s%%" % (
                      show(r1), show(T), show(r2), eq, show_exact(x1), show(r1), show_exact(x2), show(r2)))


# ---------------------------------------------------------------------------------------------------------
# 8. two purchases of the same two items:   a*x + b*y = T1,   c*x + d*y = T2     (the generator's "two_items")
# ---------------------------------------------------------------------------------------------------------
_COUNT_WORDS = {"a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
_CNT = r"(?:\d+|" + "|".join(_COUNT_WORDS) + r")"
_ITEM = r"[a-z]+(?:\s[a-z]+)?"
_PURCHASE = re.compile(r"(?<![\w.])(" + _CNT + r")\s+(" + _ITEM + r")\s+and\s+(" + _CNT + r")\s+(" + _ITEM + r")\s+"
                       r"(?:cost|costs|come to|comes to|total|totals)\s+(\d+(?:\.\d+)?)")


def _count(word):
    return int(word) if word.isdigit() else _COUNT_WORDS[word]


def _singular_word(w):
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 4 and w.endswith(("sses", "xes", "zes", "ches", "shes")):
        return w[:-2]
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        return w[:-1]
    return w


def _singular(phrase):
    """Only used to tell that "passes" and "pass" (or "pears" and "pear") name the same item; the reading keeps the words as written."""
    return " ".join(_singular_word(w) for w in phrase.split())


def two_purchases(problem):
    t = clean(problem).replace("$", "")
    found = list(_PURCHASE.finditer(t))
    if len(found) != 2 or re.search(r"\bsuch\b", t):
        return None
    # a price followed by each / apiece / per ("$5 each", "$5 for each", "$5 a piece") is the price of ONE item, not a total
    if any(re.match(r"\s*(?:(?:for|a)\s+)?(?:each|apiece|per|piece)\b", t[m.end():]) for m in found):
        return None
    rows = []
    digit_counts = 0
    for m in found:
        c1, i1, c2, i2, price = m.groups()
        digit_counts += c1.isdigit() + c2.isdigit()
        rows.append((_count(c1), _singular(i1), _count(c2), _singular(i2), Fraction(price)))
    # every number written in digits must be a count or a price of these two statements
    if len(digit_numbers(problem)) != digit_counts + 2:
        return None
    (a, n1, b, n2, T1), (c, m1, d, m2, T2) = rows
    if n1 == n2:
        return None
    if (m1, m2) == (n2, n1):                    # the second purchase names the items the other way round
        c, d = d, c
        m1, m2 = m2, m1
    if (m1, m2) != (n1, n2):
        return None
    # what is left after the two statements may only ask for the prices ("Find the price of one of each.")
    rest = t
    for m in reversed(found):
        rest = rest[:m.start()] + " " + rest[m.end():]
    if re.search(r"\d", rest) or re.search(_SPELLED, rest) or re.search(_GROUPED, rest):
        return None
    if not re.search(r"\b(?:price|cost)\b", rest) or not re.search(r"\beach\b|\bone of\b|\bper\b", rest):
        return None
    det = a * d - b * c
    if det == 0 or min(a, b, c, d) <= 0:
        return None
    x = (T1 * d - b * T2) / det
    y = (a * T2 - c * T1) / det
    if x <= 0 or y <= 0:
        return None
    eq1 = "%sx + %sy = %s" % (a, b, show(T1))
    eq2 = "%sx + %sy = %s" % (c, d, show(T2))
    first = found[0].groups()
    return Result("two_purchases", [x, y], "%s;  %s" % (eq1, eq2),
                  "x = price of one '%s', y = price of one '%s': %s and %s, so x = %s and y = %s" % (
                      first[1], first[3], eq1, eq2, show_exact(x), show_exact(y)))


# ---------------------------------------------------------------------------------------------------------
# 9. price-per-pound blend:   p1*x + p2*(T - x) = blend*T      (the generator's "weighted_avg")
#    the percent mixture with prices instead of percents.  NOT "how much must be added to a known amount".
# ---------------------------------------------------------------------------------------------------------
_UNIT_NAMES = {"lb": "lb", "lbs": "lb", "pound": "lb", "pounds": "lb", "kg": "kg", "kilogram": "kg", "kilograms": "kg",
               "oz": "oz", "ounce": "oz", "ounces": "oz"}
_UNIT_RE = "(" + "|".join(sorted(_UNIT_NAMES, key=len, reverse=True)) + r")\b"
_PER_UNIT = re.compile(r"\s*(?:/\s*|(?:per|a)\s+)" + _UNIT_RE)
_BLEND_OTHER = re.compile(r"\b(?:add|adds|added|adding|already|water|evaporat\w*|remov\w*|replac\w*|profit|loss|discount\w*|tax|"
                          r"times as|twice|double|triple|half|as much|ratio|more than|less than|each of the|extra|another|"
                          r"three|four|five|six|seven|eight|nine|ten)\b|%")
_BLEND_MAKE = re.compile(r"\b(?:make|makes|making|get|gets|need|needs|needed|obtain|produce|produces|want|wants)\b")
_BLEND_TARGET_CUE = re.compile(r"\b(?:worth|selling for|sells for|sell for|sold for|selling at|sells at|sell at|sold at|priced at|valued at)\s*$")


def price_blend(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 4 or _BLEND_OTHER.search(t):
        return None
    prices = [n for n in nums if n[1]]
    amts = [n for n in nums if not n[1]]
    if len(prices) != 3 or len(amts) != 1:
        return None
    if not re.search(r"\b(?:how (?:much|many)|find|determine|what (?:amount|weight))\b", t):
        return None
    if not re.search(r"\b(?:mix\w*|blend\w*|combin\w*)\b", t):
        return None
    if re.search(r"\btwo\s+(?:lb|lbs|pounds?|kg|kilograms?|oz|ounces?)\b", t):
        return None
    # every price is "per unit" ("$6 a pound", "$6/lb", "$6 per kg"), all with the same unit
    units = set()
    for n in prices:
        m = _PER_UNIT.match(t[n[3]:])
        if not m:
            return None
        units.add(_UNIT_NAMES[m.group(1)])
    T, a_start, a_end = amts[0][0], amts[0][2], amts[0][3]
    um = re.match(r"\s*" + _UNIT_RE, t[a_end:])
    if not um or units != {_UNIT_NAMES[um.group(1)]}:
        return None
    # the amount is the weight of the blend wanted: "to make 40 lb ..." or "40 lb of a blend ..."
    unit_end = a_end + um.end()
    if not (_BLEND_MAKE.search(" ".join(t[:a_start].split()[-3:])) or re.match(r"\s*of (?:a |the |an )?(?:blend|mixture|mix)\b", t[unit_end:])):
        return None
    # the blend's price is the first price after the amount, introduced by "worth / selling for / priced at ..."
    after = [n for n in prices if n[2] >= unit_end]
    if not after:
        return None
    target_n = min(after, key=lambda n: n[2])
    if not _BLEND_TARGET_CUE.search(t[:target_n[2]].rstrip().rstrip("$").rstrip()) or len(t[unit_end:target_n[2]].split()) > 8:
        return None
    sources = [n for n in prices if n is not target_n]
    p1, p2, tg = sources[0][0], sources[1][0], target_n[0]
    if p1 == p2 or not (min(p1, p2) < tg < max(p1, p2)) or T <= 0:
        return None
    x1 = T * (tg - p2) / (p1 - p2)
    x2 = T - x1
    if x1 <= 0 or x2 <= 0:
        return None
    unit = _UNIT_NAMES[um.group(1)]
    eq = "%sx + %s(%s - x) = %s(%s)" % (show(p1), show(p2), show(T), show(tg), show(T))
    return Result("price_blend", [x1, x2], eq,
                  "x = %s at $%s, %s - x at $%s: %s, so %s %s at $%s and %s %s at $%s" % (
                      unit, show(p1), show(T), show(p2), eq, show_exact(x1), unit, show(p1), show_exact(x2), unit, show(p2)))


# ---------------------------------------------------------------------------------------------------------
# Words that change the equation of any of the three families below: they decline
# ---------------------------------------------------------------------------------------------------------
_SPELLED_ANY = r"\b(?:two|three|four|five|six|seven|eight|nine|ten|twice|double|doubles|triple|half|halves|thrice)\b"
_CHANGES_EQUATION = re.compile(r"\b(?:such|of the year|for part of|of the time|part of the time|some of the time)\b")
_EACH_AFTER = re.compile(r"\s*(?:(?:for|a)\s+)?(?:each|apiece|per|piece)\b")


# ---------------------------------------------------------------------------------------------------------
# 10. two savers, same total:   a + ra*w = b + rb*w      (the generator's "savings")
# ---------------------------------------------------------------------------------------------------------
_SAVE_STMT = re.compile(
    r"(?<![\w$])(?P<who>i|[a-z]+(?:\s[a-z]+)?)\s+(?:has|have|had|starts?|started)(?:\s+with)?\s+\$(?P<a>\d+(?:\.\d+)?)"
    r"(?:\s+(?:saved|in savings|in the bank|in (?:her|his|their|my) account))?\s*(?:,|and|but)?\s*(?:and\s+)?"
    r"(?:saves?|adds?|puts? away|deposits?)\s+\$(?P<r>\d+(?:\.\d+)?)\s+(?:a|each|per|every)\s+(?P<u>week|month|day)\b")


def savings_equal(problem):
    t = clean(problem)
    found = list(_SAVE_STMT.finditer(t))
    if len(found) != 2 or len(digit_numbers(problem)) != 4 or _CHANGES_EQUATION.search(t):
        return None
    # the starting amounts are totals: "$200 each" / "$200 apiece" would change the equation (the rates are followed by "a week" by design)
    if any(_EACH_AFTER.match(t[m.end("a"):]) for m in found):
        return None
    m1, m2 = found
    if m1.group("who") == m2.group("who") or m1.group("u") != m2.group("u"):
        return None
    rest = t[:m1.start()] + " " + t[m1.end():m2.start()] + " " + t[m2.end():]
    if re.search(r"\d", rest) or re.search(_SPELLED_ANY, rest) or re.search(r"\b(?:now|currently|today|at the moment|so far)\b", rest):
        return None
    # the question asks WHEN they are equal, not an amount of money
    if not re.search(r"\b(?:when|how (?:many|long)|after how)\b", rest) or not re.search(r"\b(?:same|equal|even|as much)\b", rest):
        return None
    if re.search(r"\bhow much\b|\bwhat amount\b|\bhow many dollars\b", rest):
        return None
    a, b = Fraction(m1.group("a")), Fraction(m2.group("a"))
    ra, rb = Fraction(m1.group("r")), Fraction(m2.group("r"))
    if ra == rb:
        return None
    w = (b - a) / (ra - rb)
    if w <= 0 or w.denominator != 1:
        return None
    unit = m1.group("u")
    each = a + ra * w
    eq = "%s + %sw = %s + %sw" % (show(a), show(ra), show(b), show(rb))
    return Result("savings_equal", [w], eq,
                  "w = number of %ss: %s, so w = %s %ss (each will have $%s)" % (unit, eq, show_exact(w), unit, show_exact(each)))


# ---------------------------------------------------------------------------------------------------------
# 11. the score needed on the next test for a target average:   (s1 + ... + sk + x) / (k + 1) = target   ("average_needed")
# ---------------------------------------------------------------------------------------------------------
_ORDINALS = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10}
_TEST_NOUN = r"(?:tests?|exams?|quizzes|quiz|games?|papers?|assignments?|rounds?|scores|marks|grades)"
_AVG_OTHER = re.compile(r"\b(?:weighted|weights?|worth|counts?|counted|drop\w*|lowest|highest|best|worst|discard\w*|ignor\w*|curve\w*|bonus|extra|credit|"
                        r"replac\w*|median|mode|total|sum|at least|at most|minimum|maximum|no less|no more|passing|pass|out of|each)\b|%|\$")
_AVG_WORD = re.compile(r"\baverag\w*|\bmean\b|\bavg\b")
_AVG_TARGET = re.compile(r"\b(?:to average|to be averaging|an average of|the average of|average of|average score of|mean of|to bring (?:my|the|our|her|his) average (?:up )?to|"
                         r"to raise (?:my|the|our|her|his) average to|average at)\s+(\d+(?:\.\d+)?)\b(?!\s*,|\s+and\s+\d)")


def average_needed(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if _AVG_OTHER.search(t) or len(_AVG_WORD.findall(t)) != 1:
        return None
    tm = list(_AVG_TARGET.finditer(t))
    if len(tm) != 1:
        return None
    tstart, tend = tm[0].start(1), tm[0].end(1)
    target_n = [n for n in nums if n[2] <= tstart < n[3] or n[2] == tstart]
    if len(target_n) != 1 or target_n[0][3] != tend:
        return None
    target = target_n[0]
    # a stated count of tests ("on 5 tests", "after four tests") is not a score; it must agree with the scores listed
    counts = []
    for n in nums:
        if n is target:
            continue
        if re.match(r"\s+" + _TEST_NOUN + r"\b", t[n[3]:]) and re.search(r"\b(?:on|in|after|over|across|from)\s+(?:the\s+|my\s+|her\s+|his\s+|these\s+|those\s+|all\s+)?(?:first\s+)?$", t[:n[2]].rstrip() + " "):
            counts.append(n)
    if len(counts) > 1:
        return None
    scores = [n for n in nums if n is not target and n not in counts]
    k = len(scores)
    if k < 2:
        return None
    if counts and counts[0][0] != k:
        return None
    work = t
    word_counts = list(re.finditer(r"\b(two|three|four|five|six|seven|eight|nine|ten)\s+" + _TEST_NOUN + r"\b", work))
    if len(word_counts) > 1 or (word_counts and counts):
        return None
    if word_counts:
        if _COUNT_WORDS[word_counts[0].group(1)] != k:
            return None
        work = work[:word_counts[0].start()] + " " + work[word_counts[0].end():]
    if re.search(_SPELLED_ANY, work) or _CHANGES_EQUATION.search(work):
        return None
    # ordinals: only "the fourth test" naming the unknown score, and it must be number k + 1
    ords = re.findall(r"\b(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth)\b", work)
    if ords:
        if len(ords) != 1 or not re.search(r"\b" + ords[0] + r"\s+" + _TEST_NOUN + r"\b", work) or _ORDINALS[ords[0]] != k + 1:
            return None
    # the question asks for the score on the next / last / final / (k+1)th test
    if not re.search(r"\b(?:what|which|how (?:many )?(?:points|marks|high|well))\b", work):
        return None
    if not re.search(r"\b(?:need|needed|must|should|have to|has to|require|required|get|score|make|earn|take)\b", work):
        return None
    if not (ords or re.search(r"\b(?:next|last|final|another|one more)\b", work)):
        return None
    total = sum((n[0] for n in scores), Fraction(0))
    x = target[0] * (k + 1) - total
    if x < 0:
        return None
    if all(n[0] <= 100 for n in nums) and x > 100:
        return None
    listed = " + ".join(show(n[0]) for n in scores)
    eq = "(%s + x) / %d = %s" % (listed, k + 1, show(target[0]))
    return Result("average_needed", [x], eq,
                  "x = the next score: %s, so %s + x = %s and x = %s" % (eq, show(total), show(target[0] * (k + 1)), show_exact(x)))


# ---------------------------------------------------------------------------------------------------------
# 12. heads and feet of a two-legged and a four-legged animal:   h + s = H,  2h + 4s = L      (the generator's "heads_legs")
# ---------------------------------------------------------------------------------------------------------
_TWO_LEGGED = {"hen", "chicken", "duck", "goose", "geese", "turkey", "rooster", "bird", "ostrich", "pigeon", "swan", "peacock", "parrot",
               "penguin", "flamingo", "chick", "duckling", "gosling", "emu"}
_FOUR_LEGGED = {"cow", "sheep", "pig", "goat", "horse", "dog", "cat", "rabbit", "donkey", "lamb", "calf", "calves", "bull", "ox", "oxen",
                "deer", "mule", "pony", "llama", "camel", "elephant", "tiger", "lion", "puppy", "kitten", "piglet", "foal", "hog"}
_OTHER_CREATURE = {"spider", "beetle", "insect", "bug", "ant", "fly", "flie", "snake", "fish", "octopus", "centipede", "millipede", "cricket",
                   "ladybug", "bee", "butterfly", "person", "people", "man", "men", "woman", "women", "human", "child", "children", "kid", "boy",
                   "girl", "farmer", "bicycle", "tricycle", "car", "truck", "wheel", "motorcycle", "table", "stool", "chair", "tripod", "alien",
                   "worm", "monkey", "ape", "frog", "turtle", "lizard", "crab", "scorpion", "mite", "tick", "ostriches"}


def _animal_stem(w):
    if w in _TWO_LEGGED or w in _FOUR_LEGGED or w in _OTHER_CREATURE or w in ("sheep", "geese", "oxen", "calves"):
        return w
    if w.endswith("ies"):
        return w[:-3] + "y"
    if w.endswith("es") and w[:-2] in (_TWO_LEGGED | _FOUR_LEGGED | _OTHER_CREATURE):
        return w[:-2]
    if w.endswith("s"):
        return w[:-1]
    return w


def heads_and_feet(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 2 or "$" in t or "%" in t or _CHANGES_EQUATION.search(t):
        return None
    if re.search(_SPELLED_ANY, t) or re.search(r"\blegged\b|\b(?:wings?|tails?|horns?|arms?|wheels?)\b", t):
        return None
    heads = [n for n in nums if re.match(r"\s+(?:heads|animals|creatures)\b", t[n[3]:])]
    legs = [n for n in nums if re.match(r"\s+(?:legs|feet)\b", t[n[3]:])]
    if len(heads) != 1 or len(legs) != 1 or heads[0] is legs[0]:
        return None
    # one two-legged animal and one four-legged animal, nothing else with legs
    words = re.findall(r"[a-z]+", t)
    stems = []
    shown = {}
    for w in words:
        s = _animal_stem(w)
        if s in _TWO_LEGGED or s in _FOUR_LEGGED or s in _OTHER_CREATURE:
            if s not in stems:
                stems.append(s)
                shown[s] = w
    if len(stems) != 2:
        return None
    two = [s for s in stems if s in _TWO_LEGGED]
    four = [s for s in stems if s in _FOUR_LEGGED]
    if len(two) != 1 or len(four) != 1:
        return None
    # the question asks how many of the animals, not for legs or heads
    q = t.rfind("how many")
    if q == -1:
        return None
    tail = t[q:]
    if re.search(r"\b(?:legs|feet|heads|total|altogether|more|fewer|less)\b", tail):
        return None
    tail_words = re.findall(r"[a-z]+", tail)
    if "each" not in tail_words and not ({_animal_stem(w) for w in tail_words} & {two[0], four[0]}):    # "how many animals" is the heads, not an answer
        return None
    H, L = heads[0][0], legs[0][0]
    s_count = (L - 2 * H) / 2
    h_count = H - s_count
    if s_count <= 0 or h_count <= 0 or s_count.denominator != 1 or h_count.denominator != 1:
        return None
    n2, n4 = shown[two[0]], shown[four[0]]
    eq = "h + s = %s;  2h + 4s = %s" % (show(H), show(L))
    return Result("heads_and_feet", [h_count, s_count], eq,
                  "h = number of %s (2 feet), s = number of %s (4 feet): h + s = %s and 2h + 4s = %s, so h = %s and s = %s" % (
                      n2, n4, show(H), show(L), show_exact(h_count), show_exact(s_count)))


# ---------------------------------------------------------------------------------------------------------
# 13-15. distance and geometry:  opposite directions, catch-up, interior angles of a polygon
# ---------------------------------------------------------------------------------------------------------
_SPEED_UNIT = r"mph|mi/h|miles per hour|miles an hour|miles/hour|km/h|kph|kmh|km/hr|kilometers per hour|kilometres per hour|km per hour"
_SPEED = re.compile(NUM + r"\s*(" + _SPEED_UNIT + r")(?![\w/])")
_DIST = re.compile(NUM + r"\s*(miles?|mi|kilometers?|kilometres?|km)\s+apart\b")


def _speed_group(unit):
    return "mi" if unit.startswith(("mph", "mi", "miles")) else "km"


def _dist_group(unit):
    return "mi" if unit.startswith("mi") else "km"


_TWO_VEHICLES = re.compile(r"\btwo (?:cars|trains|cyclists|runners|planes|boats|buses|trucks|bikes|bicycles|friends|people|hikers|walkers|vehicles|ships|joggers|riders|drivers|motorcycles)\b")
_ASKS_TIME = re.compile(r"\b(?:how (?:many hours|long|much time)|when|after how many hours)\b")
_ASKS_OTHER = re.compile(r"\b(?:how fast|what speed|what (?:is|are) (?:the|their) speeds?|how far|how many (?:miles|kilometers|kilometres|km))\b")


def opposite_directions(problem):
    t = clean(problem)
    if "$" in t or "%" in t or _CHANGES_EQUATION.search(t) or len(digit_numbers(problem)) != 3:
        return None
    if not re.search(r"\bopposite directions?\b", t):
        return None
    if re.search(r"\b(?:same direction|toward|towards|meet|meets|later|earlier|head start|ahead|behind|follow\w*|catch\w*|chase\w*|round trip|return\w*|back|then|"
                 r"current|stream|wind|stop\w*|rest\w*|break)\b", t):
        return None
    work = _TWO_VEHICLES.sub(" ", t)                  # "Two cars" is the count of the two speeds the equation uses
    if re.search(_SPELLED_ANY, work):
        return None
    speeds = list(_SPEED.finditer(t))
    dists = list(_DIST.finditer(t))
    if len(speeds) != 2 or len(dists) != 1:
        return None
    g1, g2 = _speed_group(speeds[0].group(2)), _speed_group(speeds[1].group(2))
    if not (g1 == g2 == _dist_group(dists[0].group(2))):
        return None
    if not _ASKS_TIME.search(t) or _ASKS_OTHER.search(t):
        return None
    s1, s2, D = Fraction(speeds[0].group(1)), Fraction(speeds[1].group(1)), Fraction(dists[0].group(1))
    if s1 <= 0 or s2 <= 0 or D <= 0:
        return None
    tt = D / (s1 + s2)
    eq = "(%s + %s)t = %s" % (show(s1), show(s2), show(D))
    return Result("opposite_directions", [tt], eq, "t = hours: %s, so t = %s hours" % (eq, show_exact(tt)))


_HEAD_WORDS = {"a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
_HEAD_START = re.compile(r"(\d+(?:\.\d+)?|" + "|".join(_HEAD_WORDS) + r")\s+(?:hours?|hrs?)\s+later\b[,]?")
_FOLLOW_VERB = re.compile(r"\b(?:follows?|following|chases?|chasing)\b")
_SUBJECT_VERBS = {"follows", "follow", "leaves", "leave", "starts", "start", "departs", "chases", "drives", "drive", "travels", "travel", "rides",
                  "ride", "runs", "run", "sets", "goes", "heads", "walks", "walk", "jogs", "is", "starts"}
_CATCH_CUE = re.compile(r"\b(?:catch|catches|catching|overtake|overtakes)\b")
_ARTICLES = {"a", "an", "the", "his", "her", "their", "its", "my", "our"}


def _subject_tokens(sentence):
    toks = re.findall(r"[a-z]+", sentence)
    out = []
    for w in toks:
        if w in _SUBJECT_VERBS:
            break
        out.append(w)
    return {w for w in out if w not in _ARTICLES}


def catch_up(problem):
    t = clean(problem)
    if "$" in t or "%" in t or _CHANGES_EQUATION.search(t):
        return None
    if re.search(r"\b(?:opposite|toward|towards|meet|meets|apart|return\w*|back|stops?|stopped|rests?|breaks?|detour|lunch|current|stream|wind|also|another)\b", t):
        return None
    hs = list(_HEAD_START.finditer(t))
    if len(hs) != 1 or not _FOLLOW_VERB.search(t) or not _CATCH_CUE.search(t):
        return None
    head = Fraction(_HEAD_WORDS[hs[0].group(1)]) if hs[0].group(1) in _HEAD_WORDS else Fraction(hs[0].group(1))
    work = t[:hs[0].start()] + " " + t[hs[0].end():]          # "Two hours later" is the head start the equation uses
    if re.search(_SPELLED_ANY, work):
        return None
    speeds = list(_SPEED.finditer(t))
    if len(speeds) != 2 or _speed_group(speeds[0].group(2)) != _speed_group(speeds[1].group(2)):
        return None
    # every number in digits is a speed or the head start
    if len(digit_numbers(problem)) != 2 + (1 if hs[0].group(1) not in _HEAD_WORDS else 0):
        return None
    s1, s2 = Fraction(speeds[0].group(1)), Fraction(speeds[1].group(1))
    if s1 <= 0 or head <= 0 or s2 <= s1:
        return None
    # the question: "how long ... catches" asks the FOLLOWER's time; "after <the leader> leaves" or a distance declines
    q = max(t.rfind("how "), t.rfind("when "))
    if q == -1:
        return None
    tail = t[q:]
    if not _CATCH_CUE.search(tail) or not re.match(r"(?:how (?:long|many hours)|when)\b", tail) or _ASKS_OTHER.search(tail):
        return None
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    lead_s = next((s for s in sents if speeds[0].group(0) in s), None)
    foll_s = next((s for s in sents if speeds[1].group(0) in s), None)
    if lead_s is None or foll_s is None or lead_s == foll_s:
        return None
    # the head start belongs to the sentence of the SECOND speed, and that sentence's subject is the follower: the vehicle that leaves later
    # must be the faster one.  "Two hours later it follows a 60 mph train that left earlier" has the slower vehicle leaving later: decline.
    if not _HEAD_START.search(foll_s) or _HEAD_START.search(lead_s) or _FOLLOW_VERB.search(lead_s):
        return None
    if re.search(r"\b(?:that|who|which)\s+(?:left|started|set off|departed|had)\b|\bearlier\b|\bahead\b|\bbefore\b|\balready\b|\bhad (?:left|started)\b", t):
        return None
    if re.search(r"(?:" + _SPEED_UNIT + r")\s+(?:train|car|bus|bike|bicycle|truck|plane|runner|cyclist|boat|ship|jogger|walker|hiker|vehicle|motorcycle|rider|driver)\b", t):
        return None
    foll_s = _HEAD_START.sub(" ", foll_s)
    F, Ld = _subject_tokens(foll_s), _subject_tokens(lead_s)
    if not F or F <= {"it", "he", "she", "they", "him", "her", "them", "i", "we", "you"}:
        return None
    for am in re.finditer(r"\bafter\s+(.*?)\s+(?:leaves|starts|departs|sets off|begins)\b", tail):
        C = set(re.findall(r"[a-z]+", am.group(1))) - _ARTICLES
        if not (C & (F - Ld)) or (C & (Ld - F)):
            return None
    if re.search(r"\b(?:since|from the start|in all|in total|altogether)\b", tail):
        return None
    tt = s1 * head / (s2 - s1)
    eq = "%s(t + %s) = %st" % (show(s1), show(head), show(s2))
    return Result("catch_up", [tt], eq,
                  "t = hours after the follower leaves: %s, so t = %s hours" % (eq, show_exact(tt)))


_POLY_SUM = re.compile(r"\b(?:interior|inside|inner) angles\b")


def polygon_angle_sum(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 1 or "$" in t or "%" in t or _CHANGES_EQUATION.search(t):
        return None
    if not _POLY_SUM.search(t) or not re.search(r"\bpolygon\b", t):
        return None
    if re.search(r"\b(?:regular|each|every|exterior|outside|outer|equal|measures?|diagonals?|one angle|same measure|triangle|quadrilateral|pentagon|hexagon|"
                 r"octagon|heptagon|decagon|square|rectangle)\b", t):
        return None
    if re.search(_SPELLED_ANY, t):
        return None
    S = nums[0]
    if not re.match(r"\s*(?:°|degrees?|deg)\b|\s*°", t[S[3]:]) or not re.search(r"\b(?:sum|add up|adds up|add to|total|totals|sum to|add)\b", t):
        return None
    if not re.search(r"\bhow many (?:sides|vertices|corners|edges)\b", t):
        return None
    n = S[0] / 180 + 2
    if n.denominator != 1 or n < 3:
        return None
    eq = "(n - 2) * 180 = %s" % show(S[0])
    return Result("polygon_angle_sum", [n], eq, "n = number of sides: %s, so n = %s sides" % (eq, show_exact(n)))


# ---------------------------------------------------------------------------------------------------------
# 16. walking / driving toward each other:   (s1 + s2) t = D      (the generator's "toward each other", without a head start)
# ---------------------------------------------------------------------------------------------------------
def toward_each_other(problem):
    t = clean(problem)
    if "$" in t or "%" in t or _CHANGES_EQUATION.search(t) or len(digit_numbers(problem)) != 3:
        return None
    if not re.search(r"\b(?:toward|towards|meet|meets)\b", t):
        return None
    if re.search(r"\b(?:opposite|away|same direction|later|earlier|before|head start|ahead|behind|follow\w*|catch\w*|chase\w*|round trip|return\w*|back|then|"
                 r"current|stream|wind|stop\w*|rest\w*|break)\b", t):
        return None
    if re.search(_SPELLED_ANY, _TWO_VEHICLES.sub(" ", t)):
        return None
    speeds = list(_SPEED.finditer(t))
    dists = list(_DIST.finditer(t))
    if len(speeds) != 2 or len(dists) != 1:
        return None
    g1, g2 = _speed_group(speeds[0].group(2)), _speed_group(speeds[1].group(2))
    if not (g1 == g2 == _dist_group(dists[0].group(2))):
        return None
    if not _ASKS_TIME.search(t) or _ASKS_OTHER.search(t):
        return None
    s1, s2, D = Fraction(speeds[0].group(1)), Fraction(speeds[1].group(1)), Fraction(dists[0].group(1))
    if s1 <= 0 or s2 <= 0 or D <= 0:
        return None
    tt = D / (s1 + s2)
    eq = "(%s + %s)t = %s" % (show(s1), show(s2), show(D))
    return Result("toward_each_other", [tt], eq, "t = hours until they meet: %s, so t = %s hours" % (eq, show_exact(tt)))


# ---------------------------------------------------------------------------------------------------------
# 17. product of two consecutive (even / odd) integers:   x (x + step) = P      (the generator's "consecutive_product")
# ---------------------------------------------------------------------------------------------------------
_PRODUCT_WORD = re.compile(r"\b(?:product|multiply|multiplies|multiplied|times each other)\b")
_NEXT_WORD = re.compile(r"\b(?:consecutive|one after another|one after the other|in a row|back to back|next to each other|following each other)\b")
_TWO_NUMBERS = re.compile(r"\btwo\b(?= (?:(?:consecutive|even|odd|whole|positive|natural) )*(?:numbers|integers))")


def _isqrt_exact(n):
    """The integer square root of the integer n, or None when n is not a perfect square."""
    if n < 0:
        return None
    r = int(n ** 0.5)
    for c in (r - 1, r, r + 1):
        if c >= 0 and c * c == n:
            return c
    return None


def consecutive_product(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 1 or nums[0][1] or "$" in t or "%" in t or _CHANGES_EQUATION.search(t):
        return None
    P = nums[0][0]
    if P.denominator != 1 or P <= 0 or "." in t[nums[0][2]:nums[0][3]]:
        return None
    if not _TWO_NUMBERS.search(t) and not re.search(r"\bpair of\b", t):
        return None
    if re.search(_SPELLED_ANY, _TWO_NUMBERS.sub(" ", t)):
        return None
    if not _PRODUCT_WORD.search(t) or not _NEXT_WORD.search(t):
        return None
    if re.search(r"\b(?:sum|add|adds|plus|difference|square|squares|squared|negative|larger|smaller|greater|less|average|mean|reciprocal|quotient|divide\w*)\b", t):
        return None
    if not re.search(r"\b(?:what are|find|which|what numbers|what integers|name|list)\b", t):
        return None
    kind = "even" if re.search(r"\beven\b", t) else "odd" if re.search(r"\bodd\b", t) else ""
    if "even" in t.split() and "odd" in t.split():
        return None
    step = 2 if kind else 1
    root = _isqrt_exact(int(step * step + 4 * P))
    if root is None:
        return None
    x2 = root - step
    if x2 % 2 != 0:
        return None
    x = Fraction(x2, 2)
    if x < 1 or (kind == "even" and x % 2 != 0) or (kind == "odd" and x % 2 != 1):
        return None
    eq = "x(x + %d) = %s" % (step, show(P))
    note = "" if re.search(r"\bpositive\b", t) else " (the pair %s and %s also multiplies to %s)" % (show_exact(-(x + step)), show_exact(-x), show(P))
    return Result("consecutive_product", [x, x + step], eq,
                  "x = the smaller number: %s, so x = %s and the numbers are %s and %s%s" % (
                      eq, show_exact(x), show_exact(x), show_exact(x + step), note))


# ---------------------------------------------------------------------------------------------------------
# 18. the most you can buy:   c n + f <= B, the greatest whole n      (the generator's budget inequality "to spend ... entry fee")
# ---------------------------------------------------------------------------------------------------------
_FEE_WORD = re.compile(r"\b(?:fee|admission|entry|membership|delivery|shipping|deposit|cover charge|fixed|setup|registration)\b")
_BUDGET_BEFORE = re.compile(r"\b(?:have|has|had|budget of|spend|spending|no more than|at most|up to|only|limit of|brought|bring|saved|allowance of|with)\s*(?:only\s+)?$")
_BUDGET_AFTER = re.compile(r"^\s*(?:to spend|available|to use|budget|in total|total)\b")
_UNIT_AFTER = re.compile(r"^\s*(?:(?:for|a)\s+)?(?:each|apiece|per\s+\w+)\b")
_UNIT_BEFORE = re.compile(r"\b(?:cost|costs|costing|priced at|sell for|sells for|sold for|are|is|at)\s*$")
_BUY_OTHER = re.compile(r"\b(?:discount\w*|coupon\w*|free|sale|bogo|off|tax|tip|bulk|every|additional|after the first|for the first|profit|least|fewest|minimum|"
                        r"must|how much|left|change|remain\w*|leftover|spare|altogether|total cost|loan|borrow\w*|interest|per month|a month|a week|per week)\b|%")


def most_you_can_buy(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) not in (2, 3) or not all(n[1] for n in nums) or _CHANGES_EQUATION.search(t):
        return None
    if re.search(_SPELLED_ANY, t) or _BUY_OTHER.search(t.replace("no more than", " ").replace("at most", " ").replace("the most", " ")):
        return None
    # the question: the greatest number you can buy (not money left over)
    q = max(t.rfind("what "), t.rfind("how "), t.rfind("which "))
    if q == -1:
        return None
    tail = t[q:]
    asks_most = re.search(r"\b(?:greatest|largest|most|maximum|max|biggest|highest)\b", tail) or re.search(r"\bhow many\b.*\b(?:can|could)\b.*\b(?:buy|afford|purchase|get)\b", tail) \
        or re.search(r"\bhow many\b.*\bcan be (?:bought|purchased)\b", tail)
    if not asks_most or not re.search(r"\b(?:buy|bought|afford|purchase\w*|get|number|many)\b", tail):
        return None
    # "tickets at $12 or snacks at $4": two money amounts joined by "or" are a CHOICE, not a fee that must be paid
    if any(re.search(r"\bor\b|\beither\b", t[a[3]:b[2]]) for a, b in zip(nums, nums[1:])):
        return None
    roles = {"fee": [], "unit": [], "budget": []}
    for n in nums:
        before, after = t[:n[2]].rstrip(), t[n[3]:]
        window = " ".join(before.split()[-3:]) + " " + " ".join(after.split()[:3])
        if _FEE_WORD.search(window) and not _UNIT_AFTER.match(after):
            roles["fee"].append(n)
        elif _UNIT_AFTER.match(after):
            roles["unit"].append(n)
        elif _BUDGET_BEFORE.search(before) or _BUDGET_AFTER.match(after):
            roles["budget"].append(n)
        elif _UNIT_BEFORE.search(before):
            roles["unit"].append(n)
        else:
            return None
    if len(roles["unit"]) != 1 or len(roles["budget"]) != 1 or len(roles["fee"]) > 1 or len(nums) != 2 + len(roles["fee"]):
        return None
    B, c = roles["budget"][0][0], roles["unit"][0][0]
    f = roles["fee"][0][0] if roles["fee"] else Fraction(0)
    # a budget or a fee followed by "each / apiece / per" would be a price of one, not the money available
    if c <= 0 or B <= 0 or f < 0:
        return None
    n = (B - f) // c
    if n < 1 or not (n * c + f <= B < (n + 1) * c + f):
        return None
    eq = "%sn + %s <= %s" % (show(c), show(f), show(B)) if f else "%sn <= %s" % (show(c), show(B))
    return Result("most_you_can_buy", [Fraction(n)], eq,
                  "n = the number bought: %s, so n <= %s and the most is %s (one more would cost $%s, over $%s)" % (
                      eq, show_exact((B - f) / c), show_exact(Fraction(n)), show_exact((n + 1) * c + f), show_exact(B)))


# ---------------------------------------------------------------------------------------------------------
# 19. still water and current:   b + c = D1/T1 (downstream),  b - c = D2/T2 (upstream)      (the generator's "boat")
# ---------------------------------------------------------------------------------------------------------
_LEG = re.compile(NUM + r"\s*(km|kilometers?|kilometres?|miles?|mi|meters?|metres?)\b(?:\s+(?:downstream|upstream))?\s+in\s+" + NUM + r"\s*(?:hours?\b|hrs?\b|h(?![a-z]))")      # "2 hours", "2 hr", "2 h" (a lone h, never inside another word)
_DOWNSTREAM = re.compile(r"\b(?:downstream|with the (?:current|stream|flow)|down the river|down river)\b")
_UPSTREAM = re.compile(r"\b(?:upstream|against the (?:current|stream|flow)|against it|up the river|up river)\b")


def still_water_current(problem):
    t = clean(problem)
    if "$" in t or "%" in t or _CHANGES_EQUATION.search(t) or len(digit_numbers(problem)) != 4:
        return None
    if re.search(_SPELLED_ANY, t) or re.search(r"\b(?:wind|air|plane|return\w*|back|round trip|stops?|rests?|drift\w*|minutes?|seconds?|lake|pond)\b", t):
        return None
    legs = list(_LEG.finditer(t))
    if len(legs) != 2 or legs[0].group(2)[:2] != legs[1].group(2)[:2]:
        return None
    segs = [t[:legs[0].end()], t[legs[0].end():legs[1].end()]]
    kinds = []
    for seg in segs:
        d, u = bool(_DOWNSTREAM.search(seg)), bool(_UPSTREAM.search(seg))
        if d == u:
            return None
        kinds.append("down" if d else "up")
    if kinds[0] == kinds[1]:
        return None
    speeds = {}
    for leg, kind in zip(legs, kinds):
        D, T = Fraction(leg.group(1)), Fraction(leg.group(3))
        if D <= 0 or T <= 0:
            return None
        speeds[kind] = D / T
    vd, vu = speeds["down"], speeds["up"]
    if vu <= 0 or vd <= vu:
        return None                                            # equal speeds (no current) or the "upstream" trip faster: decline
    b, c = (vd + vu) / 2, (vd - vu) / 2
    # what is asked: the speed in still water, the speed of the current, or both
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    q = sents[-1]
    if re.search(r"\b(?:against|with the|downstream|upstream|how long|how far|how many)\b", q):
        return None
    want_b = bool(re.search(r"still water|speed of the (?:boat|canoe|rower|swimmer|kayak)|\b(?:boat|rowing|paddling|swimming)\s+speed\b", q))
    want_c = bool(re.search(r"\b(?:current|stream|flow)\b", q)) and bool(re.search(r"\bspeed|\brate|how fast", q))
    if not (want_b or want_c):
        return None
    unit = legs[0].group(2)
    vals, parts = [], []
    if want_b:
        vals.append(b)
        parts.append("still water b = %s" % show_exact(b))
    if want_c:
        vals.append(c)
        parts.append("current c = %s" % show_exact(c))
    eq = "b + c = %s;  b - c = %s" % (show_exact(vd), show_exact(vu))
    return Result("still_water_current", vals, eq,
                  "downstream speed = %s, upstream speed = %s (%s per hour): %s, so %s" % (show_exact(vd), show_exact(vu), unit, eq, " and ".join(parts)))


# ---------------------------------------------------------------------------------------------------------
# 20. a ratio split between two named substances, one amount known:   a : b  with  x of the first   (the generator's "paint ratio")
# ---------------------------------------------------------------------------------------------------------
_RATIO = re.compile(r"(?<![\d.])(\d+)\s*:\s*(\d+)(?!\d|\.\d)")
_NAME = r"([a-z]+)"
_RATIO_NAMES = [
    # "Water is mixed into concentrate in the ratio 5:1."
    re.compile(r"\b" + _NAME + r" (?:is|are) (?:mixed|combined|blended|added|stirred|poured|diluted) (?:into|with|to|in) (?:the )?" + _NAME + r" in (?:the )?ratio"),
    # "A shade of green uses blue and yellow paint in the ratio 3:4."
    re.compile(r"\b" + _NAME + r" and " + _NAME + r"(?: [a-z]+)? (?:are )?(?:mixed |used |combined |blended )?in (?:the )?ratio"),
    # "The ratio of sand to cement is 3:1."
    re.compile(r"\bratio of " + _NAME + r" to " + _NAME + r"\b"),
]
_RATIO_OTHER = re.compile(r"\b(?:total|altogether|in all|whole|together|combined amount|times as|more|less|extra|remove\w*|dilut\w*|each|per|cost|price)\b|%|\$")


def ratio_split(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or "$" in t or "%" in t or _CHANGES_EQUATION.search(t) or re.search(_SPELLED_ANY, t) or _RATIO_OTHER.search(t):
        return None
    rm = list(_RATIO.finditer(t))
    if len(rm) != 1:
        return None
    ra, rb = Fraction(rm[0].group(1)), Fraction(rm[0].group(2))
    if ra <= 0 or rb <= 0:
        return None
    pair = None
    for pat in _RATIO_NAMES:
        m = pat.search(t)
        if m:
            if pair is not None and pair != (m.group(1), m.group(2)):
                return None
            pair = (m.group(1), m.group(2))
    if pair is None or pair[0] == pair[1]:
        return None
    x, y = pair
    # the known amount is attached to one of the two substances: "30 litres of water", "6 L of blue"
    amount_n = [n for n in nums if not (n[3] > rm[0].start() and n[2] < rm[0].end())]      # the numbers that are not part of the ratio
    if len(amount_n) != 1 or amount_n[0][1]:
        return None
    am = re.match(r"\s*([a-z]+)\s+of\s+(?:the\s+)?" + _NAME + r"\b", t[amount_n[0][3]:])
    if not am or am.group(2) not in (x, y):
        return None
    known, missing = am.group(2), (y if am.group(2) == x else x)
    # the question must name the missing substance
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    qs = [s for s in sents if re.search(r"\bhow (?:much|many)\b", s)]
    if len(qs) != 1:
        return None
    asked = re.sub(r"[\d.]+\s*[a-z]*\s+of\s+(?:the\s+)?" + known + r"\b", " ", qs[0])       # the known amount may be repeated in the question
    if not re.search(r"\b" + missing + r"\b", asked) or re.search(r"\b" + known + r"\b", asked):
        return None
    k_part, m_part = (ra, rb) if known == x else (rb, ra)
    amount = amount_n[0][0]
    result = amount * m_part / k_part
    unit = am.group(1)
    return Result("ratio_split", [result], "%s : %s = %s : %s" % (x, y, show(ra), show(rb)),
                  "%s : %s = %s : %s, so %s = %s x %s/%s = %s %s" % (
                      x, y, show(ra), show(rb), missing, show(amount), show(m_part), show(k_part), show_exact(result), unit))


# ---------------------------------------------------------------------------------------------------------
# 21. three numbers from their total and two pair sums:   x + y + z = S, plus two of x + y, y + z, x + z
# ---------------------------------------------------------------------------------------------------------
_TOTAL3 = re.compile(r"\b(?:the )?sum of (?:the )?three (?:numbers|integers) (?:is|equals|=) " + NUM + r"|\bthree (?:numbers|integers) (?:add|sum|total|add up|sum up)(?: up)?(?: to| of)? " + NUM
                     + r"|\bthree (?:numbers|integers) have a sum of " + NUM)
_PAIR_WORDS = r"(?:the first two|the last two|the first and (?:the )?second|the second and (?:the )?third|the first and (?:the )?(?:third|last)|the second and (?:the )?first)"
_PAIR3 = re.compile(r"(" + _PAIR_WORDS + r")(?: numbers)?\s+(?:add|adds|sum|total|totals|make|makes|equal|equals|have a sum of|is|are)(?: up)?(?: to| of)?\s+" + NUM)
_PAIR_INDEX = {"the first two": (0, 1), "the last two": (1, 2), "the first and second": (0, 1), "the first and the second": (0, 1),
               "the second and third": (1, 2), "the second and the third": (1, 2), "the first and third": (0, 2), "the first and the third": (0, 2),
               "the first and last": (0, 2), "the first and the last": (0, 2), "the second and first": (0, 1), "the second and the first": (0, 1)}


def three_numbers(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or "$" in t or "%" in t or _CHANGES_EQUATION.search(t):
        return None
    if re.search(r"\b(?:product|times|twice|double|triple|half|difference|more than|less than|greater|smaller|larger|average|mean|consecutive|ratio|square\w*|each other)\b", t):
        return None
    if re.search(_SPELLED_ANY, re.sub(r"\bthree (?:numbers|integers)\b|\bthe (?:first|last) two\b", " ", t)):
        return None
    tot = list(_TOTAL3.finditer(t))
    pairs = list(_PAIR3.finditer(t))
    if len(tot) != 1 or len(pairs) != 2:
        return None
    S = Fraction(next(g for g in tot[0].groups() if g))
    idx = [_PAIR_INDEX[p.group(1)] for p in pairs]
    if len({frozenset(i) for i in idx}) != 2:
        return None
    vals = [Fraction(p.group(2)) for p in pairs]
    # every number in digits is the total or one of the two pair sums
    if len(nums) != 3:
        return None
    known = {}
    for (i, j), v in zip(idx, vals):
        k = ({0, 1, 2} - {i, j}).pop()                    # the number left out of the pair
        known[k] = S - v
    if len(known) != 2:
        return None
    rest = ({0, 1, 2} - set(known)).pop()
    known[rest] = S - sum(known.values())
    out = [known[0], known[1], known[2]]
    # a question, if there is one, must ask for the numbers
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    for s in sents:
        if re.search(r"\b(?:what|which|how|find|determine|name|list)\b", s) and not re.search(r"\b(?:what are|find|which|determine|name|list)\b.*\b(?:numbers|integers|them)\b|\bwhat are (?:they|the numbers)\b", s):
            return None
    names = ["x", "y", "z"]
    facts = ["x + y + z = %s" % show(S)]
    for (i, j), v in zip(idx, vals):
        facts.append("%s + %s = %s" % (names[i], names[j], show(v)))
    return Result("three_numbers", out, ";  ".join(facts),
                  "%s, so x = %s, y = %s, z = %s" % (", ".join(facts), show_exact(out[0]), show_exact(out[1]), show_exact(out[2])))


# ---------------------------------------------------------------------------------------------------------
# 23. a clock head start:  "leaves at noon ... leaves at 2 pm ... when does the car catch the cyclist?"    s1 (t + h) = s2 t
# ---------------------------------------------------------------------------------------------------------
_TIME_EXPR = re.compile(r"\b(?:(noon)|(\d{1,2})\s*(?:pm|p\.m\.))(?![\w:])")
_CATCHER = re.compile(r"\b(?:when|how long|how many hours)\b(?:\s+(?:does|do|did|will|would|can|could|is|until|after))*\s+(.*?)\s+(?:catch|catches|overtake|overtakes)\b")
_QUESTION_STOP = {"it", "he", "she", "they", "him", "her", "them", "i", "we", "you", "up", "one"}


def _clock_hours(m):
    """Hours after noon for 'noon' (0) or 'H pm' (H, with 12 pm = noon); None for anything else."""
    if m.group(1):
        return Fraction(0)
    h = int(m.group(2))
    if h == 12:
        return Fraction(0)
    return Fraction(h) if 1 <= h <= 11 else None


def catch_up_clock(problem):
    t = clean(problem)
    if "$" in t or "%" in t or _CHANGES_EQUATION.search(t) or re.search(_SPELLED_ANY, t):
        return None
    if re.search(r"\b(?:later|earlier|head start|am|midnight|minutes?|half past|quarter|opposite|toward|towards|meet|meets|apart|return\w*|back|stops?|rests?|breaks?|"
                 r"detour|lunch|current|stream|wind|also|another)\b|\d:\d\d|a\.m\.|o'clock", t):
        return None
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    qs = [s for s in sents if _CATCH_CUE.search(s) and re.search(r"\b(?:when|how long|how many hours)\b", s)]
    if len(qs) != 1 or _ASKS_OTHER.search(qs[0]):
        return None
    facts = [s for s in sents if s is not qs[0]]
    facts = [s for s in facts if _SPEED.search(s)]
    if len(facts) != 2:
        return None
    infos = []
    clock_digits = 0
    for s in facts:
        sp, tm = list(_SPEED.finditer(s)), list(_TIME_EXPR.finditer(s))
        if len(sp) != 1 or len(tm) != 1:
            return None
        hrs = _clock_hours(tm[0])
        if hrs is None:
            return None
        clock_digits += 0 if tm[0].group(1) else 1
        infos.append((Fraction(sp[0].group(1)), hrs, _speed_group(sp[0].group(2)), _subject_tokens(s)))
    if infos[0][2] != infos[1][2] or len(digit_numbers(problem)) != 2 + clock_digits:
        return None
    (s1, h1, _, tok1), (s2, h2, _, tok2) = infos
    if h1 == h2:
        return None
    if h1 > h2:                                          # the vehicle named second left first
        (s1, h1, _, tok1), (s2, h2, _, tok2) = (s2, h2, _, tok2), (s1, h1, _, tok1)
    head = h2 - h1
    if s1 <= 0 or s2 <= s1:
        return None                                      # the one that leaves later must be the faster one
    cm = _CATCHER.search(qs[0])
    if not cm:
        return None
    C = set(re.findall(r"[a-z]+", cm.group(1))) - _ARTICLES - _QUESTION_STOP
    if not C or not (C & (tok2 - tok1)) or (C & (tok1 - tok2)):
        return None
    tt = s1 * head / (s2 - s1)
    eq = "%s(t + %s) = %st" % (show(s1), show(head), show(s2))
    return Result("catch_up_clock", [tt], eq,
                  "the later vehicle leaves %s hours after the earlier one; t = hours after it leaves: %s, so t = %s hour%s (%s after noon)" % (
                      show_exact(head), eq, show_exact(tt), "" if tt == 1 else "s", show_exact(h2 + tt) + (" hour" if h2 + tt == 1 else " hours")))


# ---------------------------------------------------------------------------------------------------------
# 24. doubling, tripling, halving every period, exact whole numbers of periods     (the generator's "Exponential": doubles / triples / half-life)
# ---------------------------------------------------------------------------------------------------------
_GROWTH_UNIT = r"(?:hours?|hrs?|days?|weeks?|months?|years?|minutes?|mins?|seconds?|secs?)"
_TIME_NAME = {"hour": "hour", "hr": "hour", "day": "day", "week": "week", "month": "month", "year": "year", "minute": "minute", "min": "minute", "second": "second", "sec": "second"}
_PERIOD_PATTERNS = [
    re.compile(r"\bevery\s+(\d+(?:\.\d+)?|two|three|four|five|six|seven|eight|nine|ten)\s+(" + _GROWTH_UNIT + r")\b"),
    re.compile(r"\bevery\s+()(" + _GROWTH_UNIT + r")\b"),
    re.compile(r"\bhalf-life of\s+(\d+(?:\.\d+)?)\s+(" + _GROWTH_UNIT + r")\b"),
]
_GROW_END_CUE = re.compile(r"(?:reach(?:es)?|to|becomes?|decays to|falls to|grows to|when will(?: there be)?|will there be|there be|there are|are there)\s*$")


def _unit_name(word):
    return _TIME_NAME[word.rstrip("s")] if word.rstrip("s") in _TIME_NAME else _TIME_NAME[word]


def periodic_growth(problem):
    t = clean(problem)
    if "$" in t or "%" in t or _CHANGES_EQUATION.search(t) or re.search(r"\b(?:per|twice|thrice|quadrupl\w*|quarter\w*|tenfold|fold|then|other|percent)\b", t):
        return None
    kinds = [k for k, pat in (("double", r"\b(?:doubles|double|doubling|doubled)\b"), ("triple", r"\b(?:triples|triple|tripling|tripled)\b"),
                              ("halve", r"\b(?:halves|halving|halved|half-life)\b")) if re.search(pat, t)]
    if len(kinds) != 1:
        return None
    found = [m for pat in _PERIOD_PATTERNS for m in pat.finditer(t)]
    if len(found) != 1:
        return None
    pm = found[0]
    period = fr(pm.group(1)) if pm.group(1) else Fraction(1)
    unit = _unit_name(pm.group(2))
    work = t[:pm.start()] + " " + t[pm.end():]
    work = work.replace("half-life", " ")
    if re.search(r"\b(?:two|three|four|five|six|seven|eight|nine|ten|half)\b", work):
        return None
    nums = digit_numbers(problem)
    period_digit = pm.start(1) if pm.group(1) and pm.group(1)[0].isdigit() else None
    others = [n for n in nums if period_digit is None or not (n[2] <= period_digit < n[3])]
    if len(others) != 2 or len(nums) != len(others) + (1 if period_digit is not None else 0) or any(n[1] for n in others):
        return None
    ends = [n for n in others if _GROW_END_CUE.search(t[:n[2]].rstrip())]
    if len(ends) != 1:
        return None
    end = ends[0]
    start = others[0] if others[1] is end else others[1]
    A, B = start[0], end[0]
    if A <= 0 or B <= 0 or period <= 0:
        return None
    # the question asks for the time, in the unit of the period
    qs = [s for s in re.split(r"[.?!]\s*", t) if re.search(r"\b(?:when|how long|how many " + _GROWTH_UNIT + r"|after how many)\b", s)]
    if len(qs) != 1:
        return None
    for w in re.findall(_GROWTH_UNIT, qs[0]):
        if _unit_name(w) != unit:
            return None
    f = Fraction(3) if kinds[0] == "triple" else Fraction(2)
    ratio = (A / B) if kinds[0] == "halve" else (B / A)
    if ratio <= 1 or ratio.denominator != 1:
        return None
    k, r = 0, int(ratio)
    while r % int(f) == 0:
        r //= int(f)
        k += 1
    if r != 1 or k < 1:
        return None
    total = period * k
    if kinds[0] == "halve":
        eq = "%s / 2^k = %s" % (show(A), show(B))
        step = "%s / %s = %s = 2^%d" % (show(A), show(B), show_exact(ratio), k)
    else:
        eq = "%s x %d^k = %s" % (show(A), int(f), show(B))
        step = "%s / %s = %s = %d^%d" % (show(B), show(A), show_exact(ratio), int(f), k)
    return Result("periodic_growth", [total], eq,
                  "%s, so %d periods of %s %ss: t = %s %ss" % (step, k, show_exact(period), unit, show_exact(total), unit))


# ---------------------------------------------------------------------------------------------------------
# 25. a fixed cost plus a rate:   F + r n = T      (the generator's "venue", "taxi", "gym", "plumber")
# ---------------------------------------------------------------------------------------------------------
_FIXED_RATE_AFTER = re.compile(r"\s*(?:per|a|an|each|every|/)\s*([a-z]+)")
_FIXED_TOTAL_BEFORE = re.compile(r"(?:\btotal(?: cost| bill)?(?: was| is| came to| comes to)?|\b(?:bill|fare|ride|trip|cost|costs|price|invoice|job)(?: was| is| came to| comes to| costs?| totaled| totalled)?|"
                                 r"\b(?:paid|spent|owes?|owed|charged|billed|came to|comes to))\s*(?:a total of\s+)?$")
_FIXED_OTHER = re.compile(r"\b(?:discount\w*|tax|tip|percent|coupon\w*|free|waived|first|additional|extra|minimum|maximum|at least|at most|between|rest|remaining|balance)\b|%")
_FIXED_CONTINUOUS = {"hour", "minute", "mile", "km", "kilometer", "kilometre", "meter", "metre", "foot", "feet", "pound", "lb", "kg", "gallon", "liter", "litre"}
_FIXED_TIME_UNITS = {"hour", "minute", "day", "week", "month", "year"}


def _stem_unit(w):
    w = w.lower()
    if w.endswith("ies"):
        return w[:-3] + "y"
    if w.endswith("s") and not w.endswith("ss") and w not in ("lbs",):
        return w[:-1]
    return "lb" if w == "lbs" else w


def fixed_plus_rate(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or not all(n[1] for n in nums) or _CHANGES_EQUATION.search(t) or _FIXED_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    rates = [(n, _FIXED_RATE_AFTER.match(t[n[3]:])) for n in nums]
    rates = [(n, m) for n, m in rates if m]
    if len(rates) != 1:
        return None
    rate_n, rate_m = rates[0]
    others = [n for n in nums if n is not rate_n]
    F, T = others[0], others[1]
    if not (F[2] < rate_n[2] < T[2]):
        return None                                           # the order is: fixed cost, then the rate, then the total
    # the fixed cost is followed by "plus" or a fee word; the total is introduced by a word like "total was / the ride cost / has paid"
    after_f = " ".join(t[F[3]:].split()[:3])
    if not re.search(r"\b(?:plus|fee|and)\b|\+", after_f):
        return None
    if not (_FIXED_TOTAL_BEFORE.search(t[:T[2]].rstrip()) or re.match(r"\s*(?:in total|altogether)\b", t[T[3]:])):
        return None
    if _EACH_AFTER.match(t[F[3]:]) or _EACH_AFTER.match(t[T[3]:]):
        return None
    unit = _stem_unit(rate_m.group(1))
    # the question asks how many of the unit (or how long, for a time unit), not the total
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    q = next((s for s in reversed(sents) if re.search(r"\bhow\b", s)), None)
    if q is None or re.search(r"\bhow much\b|\btotal\b", q):
        return None
    qm = re.search(r"\bhow many ([a-z]+)", q)
    ok = bool(qm and _stem_unit(qm.group(1)) == unit) or (bool(re.search(r"\bhow long\b", q)) and unit in _FIXED_TIME_UNITS)
    if not ok:
        return None
    f, r, total = F[0], rate_n[0], T[0]
    if r <= 0 or f < 0 or total <= f:
        return None
    n = (total - f) / r
    if n <= 0 or (n.denominator != 1 and unit not in _FIXED_CONTINUOUS):
        return None
    eq = "%s + %sn = %s" % (show(f), show(r), show(total))
    return Result("fixed_plus_rate", [n], eq, "n = number of %ss: %s, so n = %s %s%s" % (unit, eq, show_exact(n), unit, "" if n == 1 else "s"))


# ---------------------------------------------------------------------------------------------------------
# 26. two amounts changing at constant rates until equal:   a + ca t = b + cb t      (the generator's "Town A ... grows by ... Town B ... shrinks by")
# ---------------------------------------------------------------------------------------------------------
_GROW_STMT = re.compile(
    r"(?<![\w$])(?P<who>[a-z]+(?:\s[a-z]+)?)\s+(?:has|had|have|starts? with|started with|begins? with)\s+(?P<a>\$?\d+(?:\.\d+)?)(?:\s+[a-z]+)?(?:,|\s+and|\s+but)?\s+(?:and\s+)?"
    r"(?P<v>grows?|increases?|rises?|gains?|shrinks?|decreases?|falls?|drops?|loses?|declines?)(?:\s+by)?\s+(?P<c>\$?\d+(?:\.\d+)?)(?:\s+[a-z]+)?\s+(?:a|per|each|every)\s+"
    r"(?P<u>year|month|week|day|hour|decade)\b")
_GROW_FALL = re.compile(r"shrink|decreas|fall|drop|lose|declin")


def two_changing_equal(problem):
    t = clean(problem)
    found = list(_GROW_STMT.finditer(t))
    measured = False
    if not found:
        found = list(_GROW_STMT2.finditer(t))                   # "is 13 cm tall and grows 3 cm a week": a continuous quantity
        measured = True
    nums = digit_numbers(problem)
    if len(found) != 2 or len(nums) != 4 or _CHANGES_EQUATION.search(t) or "%" in t:
        return None
    m1, m2 = found
    if m1.group("who") == m2.group("who") or m1.group("u") != m2.group("u"):
        return None
    if measured and not (m1.group("au") == m1.group("cu") == m2.group("au") == m2.group("cu")):
        return None                                              # one unit of measure throughout
    if len({n[1] for n in nums}) != 1:
        return None                                              # all money or none
    rest = t[:m1.start()] + " " + t[m1.end():m2.start()] + " " + t[m2.end():]
    if re.search(r"\d", rest) or re.search(_SPELLED_ANY, rest):
        return None
    unit = m1.group("u")
    # the question asks for the TIME they are equal, not an amount
    if not re.search(r"\b(?:when|how long|how many (?:years|months|weeks|days|hours|decades)|after how many)\b", rest) or not re.search(r"\b(?:equal|same)\b", rest):
        return None
    if re.search(r"\bhow much\b|\bhow many (?:people|residents|dollars|items)\b|\bwhat (?:will|is|would)\b|\bhow (?:tall|heavy|high|big|deep|wide)\b|\bwhat (?:height|weight|size|length)\b", rest):
        return None                                              # a question for the HEIGHT / amount, not the time they are equal

    def val(s):
        return Fraction(s.lstrip("$"))
    a, b = val(m1.group("a")), val(m2.group("a"))
    ca = -val(m1.group("c")) if _GROW_FALL.match(m1.group("v")) else val(m1.group("c"))
    cb = -val(m2.group("c")) if _GROW_FALL.match(m2.group("v")) else val(m2.group("c"))
    if ca == cb:
        return None
    tt = (b - a) / (ca - cb)
    if tt <= 0 or (tt.denominator != 1 and not measured):
        return None
    sa = "+ %s" % show(ca) if ca >= 0 else "- %s" % show(-ca)
    sb = "+ %s" % show(cb) if cb >= 0 else "- %s" % show(-cb)
    eq = "%s %s t = %s %s t" % (show(a), sa, show(b), sb)
    return Result("two_changing_equal", [tt], eq, "t = number of %ss: %s, so t = %s %ss" % (unit, eq, show_exact(tt), unit))


# ---------------------------------------------------------------------------------------------------------
# 27. adding to an amount you already have, to reach a blend price:   p1 a + p2 x = t (a + x)      (the generator's "must be added to ... worth")
# ---------------------------------------------------------------------------------------------------------
_ADDMIX_UNIT = r"(?:lb|lbs|pounds?|kg|kilograms?|oz|ounces?)"
_ADDMIX_PRICE = r"\$(\d+(?:\.\d+)?)\s*(?:/\s*|per\s+|a\s+)(" + _ADDMIX_UNIT + r")\b"
_ADDMIX = re.compile(
    r"how (?:many|much)\s+(?:(?:" + _ADDMIX_UNIT + r")\s+of\s+)?(?:[a-z]+(?:\s[a-z]+)?\s+)?(?:worth|at|priced at|costing|that costs?|selling for)\s+" + _ADDMIX_PRICE
    + r"\s+must be added to\s+(\d+(?:\.\d+)?)\s*(" + _ADDMIX_UNIT + r")\s+of\s+(?:[a-z]+(?:\s[a-z]+)?\s+)?(?:worth|at|priced at|costing|that costs?|selling for)\s+" + _ADDMIX_PRICE
    + r"\s+to\s+(?:make|get|obtain|produce)\s+(?:an?\s+)?(?:mix|blend|mixture)?\s*(?:that is\s+)?(?:worth|priced at|selling for|at)\s+" + _ADDMIX_PRICE)
_ADDMIX_OTHER = re.compile(r"\b(?:water|pure|evaporat\w*|remov\w*|replac\w*|profit|loss|discount\w*|tax|times as|twice|double|triple|half|as much|ratio|more than|less than|"
                           r"three|four|five|six|seven|eight|nine|ten|another)\b|%")


def add_to_blend(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 4 or _CHANGES_EQUATION.search(t) or _ADDMIX_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None                                  # a spelled "two pounds spill" / "twice" changes the equation: found by fresh set 17
    m = _ADDMIX.search(t)
    if not m:
        return None
    p2, u1, a, u2, p1, u3, tg, u4 = m.groups()
    if len({_UNIT_NAMES[u] for u in (u1, u2, u3, u4)}) != 1:
        return None
    p2, a, p1, tg = Fraction(p2), Fraction(a), Fraction(p1), Fraction(tg)
    if a <= 0 or p1 == p2 or not (min(p1, p2) < tg < max(p1, p2)):
        return None                                                # the blend price must lie strictly between the two prices
    x = a * (tg - p1) / (p2 - tg)
    if x <= 0:
        return None
    unit = _UNIT_NAMES[u2]
    eq = "%s(%s) + %sx = %s(%s + x)" % (show(p1), show(a), show(p2), show(tg), show(a))
    return Result("add_to_blend", [x], eq, "x = %s added: %s, so x = %s %s" % (unit, eq, show_exact(x), unit))


# ---------------------------------------------------------------------------------------------------------
# 28. two kinds of score:   x + y = N,  a x + b y = P      (the generator's "basketball" and "football" scores)
# ---------------------------------------------------------------------------------------------------------
_SCORE_KIND = re.compile(r"\b(?:(\d+)|(two|three|four|five|six|seven))-(?:pointers?|points?)\b")
_SCORE_TOTAL = re.compile(r"(?<![\w-])(\d+)\s+points?\b")
_SCORE_COUNT = re.compile(r"\bfrom\s+(\d+)\s+[a-z]+(?:\s+[a-z]+)?")          # only "from" introduces the number of scores ("in 40 games" does not)
_SCORE_OTHER = re.compile(r"\b(?:free throws?|fouls?|safety|safeties|penalt\w*|conversions?|bonus\w*|overtime|other|rest|some)\b")


def two_scores(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if "$" in t or "%" in t or _CHANGES_EQUATION.search(t) or _SCORE_OTHER.search(t.replace("(with extra point)", " ")):
        return None
    if not re.search(r"\b(?:all|only|just|nothing but)\b", t):
        return None
    kinds = list(_SCORE_KIND.finditer(t))
    values = []
    for m in kinds:
        v = Fraction(m.group(1)) if m.group(1) else Fraction(_SMALL[m.group(2)])
        values.append(v)
    if len(values) != 2 or values[0] == values[1] or min(values) < 1:
        return None
    tot, cnt = list(_SCORE_TOTAL.finditer(t)), list(_SCORE_COUNT.finditer(t))
    if len(tot) != 1 or len(cnt) != 1:
        return None
    work = _SCORE_KIND.sub(" ", t.replace("(with extra point)", " "))
    if re.search(_SPELLED_ANY, work):
        return None
    digit_kinds = sum(1 for m in kinds if m.group(1))
    if len(nums) != 2 + digit_kinds:
        return None
    P, N = Fraction(tot[0].group(1)), Fraction(cnt[0].group(1))
    if P == N or tot[0].start(1) == cnt[0].start(1):
        return None
    # the question asks how many of each (or names a kind of score)
    q = t.rfind("how many")
    if q == -1 or not (re.search(r"\beach\b", t[q:]) or _SCORE_KIND.search(t[q:])):
        return None
    a, b = values
    y = (P - a * N) / (b - a)
    x = N - y
    if x <= 0 or y <= 0 or x.denominator != 1 or y.denominator != 1:
        return None
    e1, e2 = "x + y = %s" % show(N), "%sx + %sy = %s" % (show(a), show(b), show(P))
    return Result("two_scores", [x, y], "%s;  %s" % (e1, e2),
                  "x = number of %s-point scores, y = number of %s-point scores: %s and %s, so x = %s and y = %s" % (
                      show(a), show(b), e1, e2, show_exact(x), show_exact(y)))


# ---------------------------------------------------------------------------------------------------------
# 29. two discounts, one after the other:   (1 - a)(1 - b) p = F     (the generator's "coat ... an extra b% is taken off the sale price")
# ---------------------------------------------------------------------------------------------------------
_DISC2_FINAL = re.compile(r"\b(?:final (?:price|cost)|now (?:costs?|sells? for|is)|pays?|paid|ends? up|after both)\b")
_DISC2_ORIGINAL_Q = re.compile(r"\b(?:what|how much)\b[^.?!]*\b(?:original|regular|list|starting|before)\b")
_DISC2_OTHER = re.compile(r"\b(?:tax|tip|both|combined|together|add up|adds up|total discount|save|saved|savings)\b")


def two_discounts(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or t.count("%") != 2 or _CHANGES_EQUATION.search(t) or _DISC2_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    money = [n for n in nums if n[1]]
    pcts = [n for n in nums if t[n[3]:n[3] + 2].strip().startswith("%")]
    if len(money) != 1 or len(pcts) != 2:
        return None
    p1, p2 = pcts
    # the first cut: "40% off" / "marked down 40%"; the second: an extra / additional / further cut taken off the SALE (reduced) price, not the original
    if not (re.match(r"\s*%\s*(?:off|discount)\b", t[p1[3]:]) or re.search(r"\b(?:marked down|reduced|discounted)(?: by)?\s*$", t[:p1[2]].rstrip())):
        return None
    if not re.search(r"\b(?:extra|additional|further|another)\s*$", " ".join(t[:p2[2]].split()[-2:])) or not re.search(r"\b(?:then|after that|next|on top)\b", t):
        return None
    clause = re.split(r"[.?!]", t[p2[3]:])[0]
    if not re.search(r"\b(?:sale|discounted|reduced|new|marked-down|marked down|lower)\s+price\b", clause) or re.search(r"\b(?:original|regular|list|first)\b", clause):
        return None
    if not _DISC2_FINAL.search(t) or not _DISC2_ORIGINAL_Q.search(t):
        return None
    a, b, F = p1[0] / 100, p2[0] / 100, money[0][0]
    if not (0 < a < 1 and 0 < b < 1) or F <= 0:
        return None
    price = F / ((1 - a) * (1 - b))
    eq = "%s x %s x p = %s" % (show(1 - a), show(1 - b), show(F))
    return Result("two_discounts", [price], eq,
                  "p = original price; the second cut is taken off the sale price: %s, so p = %s" % (eq, show_answer(price, True)))


# ---------------------------------------------------------------------------------------------------------
# 30. angles of a triangle in a ratio of three whole numbers      (the generator's "angles of a triangle are in the ratio a:b:c")
# ---------------------------------------------------------------------------------------------------------
_TRI_RATIO = re.compile(r"(?<![\d.:])(\d+)\s*:\s*(\d+)\s*:\s*(\d+)(?!\d|\.\d|:)")
_TRI_OTHER = re.compile(r"\b(?:right|isosceles|equilateral|exterior|outside|largest|smallest|biggest|difference|sum of two|quadrilateral|polygon|pentagon|hexagon|"
                        r"one angle|another|degrees more|more than|less than|twice|double)\b")


def triangle_ratio(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or "$" in t or "%" in t or _CHANGES_EQUATION.search(t) or _TRI_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    if not re.search(r"\bangles of a triangle\b|\btriangle'?s? angles\b|\bthree angles of a triangle\b", t) or not re.search(r"\bratio\b", t):
        return None
    rm = list(_TRI_RATIO.finditer(t))
    if len(rm) != 1:
        return None
    parts = [Fraction(g) for g in rm[0].groups()]
    if min(parts) < 1:
        return None
    # the question asks for every angle
    if not re.search(r"\b(?:find|what (?:are|is)|determine|give|name)\b[^.?!]*\b(?:each angle|the angles|all (?:three )?angles|every angle|each of the angles)\b", t):
        return None
    total = sum(parts)
    angles = [Fraction(180) * p / total for p in parts]
    return Result("triangle_ratio", angles, "%sk + %sk + %sk = 180" % tuple(show(p) for p in parts),
                  "%s parts in all, so one part is 180/%s = %s: %s" % (
                      show(total), show(total), show_exact(Fraction(180) / total), ", ".join("%s degrees" % show_exact(a) for a in angles)))


# ---------------------------------------------------------------------------------------------------------
# 31. two prices and a known count:   x + y = N,  p1 x + p2 y = T      (the generator's "stamps" in cents and "two jobs" at an hourly wage)
#     a price in cents is 1/100 of a dollar before it meets a dollar total
# ---------------------------------------------------------------------------------------------------------
_TP_RATE_AFTER = re.compile(r"\s*(?:/\s*(?:h|hr|hrs|hour|lb|kg|ea|each)\b|(?:an?|per)\s+[a-z]+\b|each\b|apiece\b)")
_TP_TOTAL_BEFORE = re.compile(r"(?:\b(?:for|earning|earned|earns|totaling|totalling|totaled|costing|cost|costs|paying|paid|made|worth|in all)\s*(?:a total of\s*)?|\btotal of\s*)$")
_TP_OTHER = re.compile(r"\b(?:tax|discount|tip|bonus|overtime|percent|extra|also|third|another|rest|remaining)\b|%")
_TP_RATE_UNIT = re.compile(r"\s*(?:/\s*|per\s+|an?\s+)([a-z]+)\b")
_TP_MEASURE = {"kg": "kg", "kilogram": "kg", "kilograms": "kg", "lb": "lb", "lbs": "lb", "pound": "lb", "pounds": "lb", "oz": "oz", "ounce": "oz", "ounces": "oz",
               "g": "g", "gram": "g", "grams": "g", "h": "hour", "hr": "hour", "hrs": "hour", "hour": "hour", "hours": "hour", "l": "l", "liter": "l", "liters": "l",
               "litre": "l", "litres": "l", "gallon": "gal", "gallons": "gal", "gal": "gal", "mile": "mile", "miles": "mile", "km": "km", "min": "minute",
               "minute": "minute", "minutes": "minute", "day": "day", "days": "day"}
_TP_TWO_WORDS = re.compile(r"\btwo (?:jobs|kinds|types|rates|prices|wages|sizes|brands|teas|coffees|grades|flavors|varieties|blends|candies|nuts|oils|fruits)\b")


def two_prices_known_count(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if _CHANGES_EQUATION.search(t) or _TP_OTHER.search(t) or re.search(_SPELLED_ANY, _TP_TWO_WORDS.sub(" ", t)):
        return None
    # the question may repeat a price ("How many hours were worked at the $16 job?"): not a new number
    q = t.rfind("how ")
    main = [n for n in nums if q == -1 or n[2] < q]
    repeated = [n for n in nums if q != -1 and n[2] >= q]
    if any(not any(m[0] == n[0] for m in main) for n in repeated):
        return None
    cents = [n for n in main if re.match(r"\s*(?:¢|cents?\b)", t[n[3]:])]
    rated = [n for n in main if n[1] and _TP_RATE_AFTER.match(t[n[3]:]) and n not in cents]
    plain = [n for n in main if not n[1] and n not in cents]
    money = [n for n in main if n[1] and n not in rated and n not in cents]
    if len(plain) != 1 or len(money) != 1:
        return None
    if len(cents) == 2 and not rated:
        prices, in_cents = cents, True
    elif len(rated) == 2 and not cents:
        prices, in_cents = rated, False
    else:
        return None
    # the known amount's unit must match the unit of the price: 31 lb at $5/kg is not 31 kg; 61 hours at $16/h is
    rate_units = []
    for n in prices:
        um = _TP_RATE_UNIT.match(t[n[3]:])
        rate_units.append(_TP_MEASURE.get(um.group(1)) if um else None)
    if any(u is not None for u in rate_units):
        cw = re.match(r"\s*([a-z]+)", t[plain[0][3]:])
        if len(set(rate_units)) != 1 or not cw or _TP_MEASURE.get(cw.group(1)) != rate_units[0]:
            return None
    T = money[0]
    if not (_TP_TOTAL_BEFORE.search(t[:T[2]].rstrip()) or re.match(r"\s*(?:in total|altogether)\b", t[T[3]:])) or _EACH_AFTER.match(t[T[3]:]):
        return None
    N = plain[0][0]
    if N <= 0 or N.denominator != 1:
        return None
    # the question asks how many of each (or at a named price)
    if q == -1 or not (re.search(r"\bhow many\b", t[q:]) and (re.search(r"\beach\b", t[q:]) or repeated)):
        return None
    scale = Fraction(1, 100) if in_cents else Fraction(1)
    p1, p2, total = prices[0][0] * scale, prices[1][0] * scale, T[0]
    if p1 == p2 or p1 <= 0 or p2 <= 0:
        return None
    y = (total - p1 * N) / (p2 - p1)
    x = N - y
    if x <= 0 or y <= 0 or x.denominator != 1 or y.denominator != 1:
        return None
    unit = "cents" if in_cents else "dollars"
    e1, e2 = "x + y = %s" % show(N), "%sx + %sy = %s" % (show(p1), show(p2), show(total))
    return Result("two_prices_known_count", [x, y], "%s;  %s" % (e1, e2),
                  "x = number at %s, y = number at %s%s: %s and %s, so x = %s and y = %s" % (
                      show(prices[0][0]) + " " + unit, show(prices[1][0]) + " " + unit,
                      " (a price in cents is divided by 100 to meet the dollar total)" if in_cents else "", e1, e2, show_exact(x), show_exact(y)))


# ---------------------------------------------------------------------------------------------------------
# 32. draining or filling to a mark:   V - r t = L  (drains)   or   V + r t = L  (fills)      (the generator's "pool drains")
# ---------------------------------------------------------------------------------------------------------
_DRAIN_UNIT = r"(?:liters?|litres?|l|gallons?|gal|quarts?|kg|lbs?|pounds?|cups?)"
_DRAIN_UNIT_NAME = {"liter": "l", "litre": "l", "l": "l", "gallon": "gal", "gal": "gal", "quart": "quart", "kg": "kg", "lb": "lb", "pound": "lb", "cup": "cup"}
_DRAIN_TIME = r"(?:seconds?|secs?|minutes?|mins?|hours?|hrs?|days?|weeks?)"
_DRAIN_TIME_NAME = {"second": "second", "sec": "second", "minute": "minute", "min": "minute", "hour": "hour", "hr": "hour", "day": "day", "week": "week"}
_DRAIN_START = re.compile(r"\b(?:holds|contains|has|had|starts? with|started with|is filled with|is holding|is full with)\s+(\d+(?:\.\d+)?)\s*(" + _DRAIN_UNIT + r")\b")
_DRAIN_RATE = re.compile(r"\b(drains?|empties|leaks?|loses|lose|pumps? out|fills?|gains?|pumps? in|adds?)\s+(?:at|by|about)?\s*(\d+(?:\.\d+)?)\s*(" + _DRAIN_UNIT
                         + r")\s*(?:per|a|each|every|/)\s*(" + _DRAIN_TIME + r")\b")
_DRAIN_OTHER = re.compile(r"\b(?:while|but|and then|then|until|both|valve|second|another|also|stops?|resum\w*|after (?:that|which)|half|full)\b|%|\$")


def _drain_norm(table, word):
    w = word.lower()
    return table.get(w, table.get(w.rstrip("s"), w))


def drain_or_fill(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or _CHANGES_EQUATION.search(t) or _DRAIN_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    sm, rm = list(_DRAIN_START.finditer(t)), list(_DRAIN_RATE.finditer(t))
    if len(sm) != 1 or len(rm) != 1:
        return None
    verb = rm[0].group(1)
    down = bool(re.match(r"drain|empt|leak|lose|pumps? out", verb))
    V, r = Fraction(sm[0].group(1)), Fraction(rm[0].group(2))
    u1, u2 = _drain_norm(_DRAIN_UNIT_NAME, sm[0].group(2)), _drain_norm(_DRAIN_UNIT_NAME, rm[0].group(3))
    if u1 != u2:
        return None
    tunit = _drain_norm(_DRAIN_TIME_NAME, rm[0].group(4))
    # the third number is the mark to reach: "will 500 L remain", "will it hold 2,000 L"
    used = [sm[0].start(1), rm[0].start(2)]
    rest = [n for n in nums if not any(n[2] <= u < n[3] for u in used)]
    if len(rest) != 1 or rest[0][1]:
        return None
    target = rest[0]
    um = re.match(r"\s*(" + _DRAIN_UNIT + r")\b", t[target[3]:])
    if not um or _drain_norm(_DRAIN_UNIT_NAME, um.group(1)) != u1:
        return None
    # the question asks for the TIME, in the unit of the rate, and mentions the mark: remain / left / hold / contain / reach
    qm = re.search(r"\b(?:after how many|how many|how long)\s*(" + _DRAIN_TIME + r")?", t)
    if not qm or (qm.group(1) and _drain_norm(_DRAIN_TIME_NAME, qm.group(1)) != tunit):
        return None
    if not qm.group(1) and "how long" not in qm.group(0):
        return None
    after = t[qm.start():]
    if not re.search(r"\b(?:remain\w*|left|hold|holds|contain\w*|have|reach\w*|be in)\b", after) or re.search(r"\bhow many (?:" + _DRAIN_UNIT + r")\b", t):
        return None
    L = target[0]
    tt = (V - L) / r if down else (L - V) / r
    if tt <= 0 or r <= 0 or V < 0 or L < 0:
        return None
    sign = "-" if down else "+"
    eq = "%s %s %st = %s" % (show(V), sign, show(r), show(L))
    return Result("drain_or_fill", [tt], eq, "t = number of %ss: %s, so t = %s %s%s" % (tunit, eq, show_exact(tt), tunit, "" if tt == 1 else "s"))


# ---------------------------------------------------------------------------------------------------------
# 33. a percent of a count:   count x percent / 100      (the generator's "A test has N questions. X scored P%.")
# ---------------------------------------------------------------------------------------------------------
_PCTC_NOUN = r"(?:questions?|problems?|items?|shots?|attempts?|students?|people|marbles|cards|tickets|games|answers|points)"
_PCTC_OTHER = re.compile(r"\b(?:more|less|increase\w*|decrease\w*|off|discount\w*|tax|tip|of which|rest|remaining|incorrect\w*|wrong|missed|failed|fewer|than|each|per|doubl\w*)\b|\$")


def percent_of_count(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 2 or t.count("%") != 1 or _CHANGES_EQUATION.search(t) or _PCTC_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    pct = [n for n in nums if t[n[3]:n[3] + 2].strip().startswith("%")]
    cnt = [n for n in nums if n not in pct]
    if len(pct) != 1 or len(cnt) != 1 or cnt[0][1] or cnt[0][0].denominator != 1:
        return None
    cm = re.match(r"\s*" + _PCTC_NOUN + r"\b", t[cnt[0][3]:])
    if not cm:
        return None
    # "scored 65%" / "got 65%" / "made 65%": the percent is the score on the count; the question asks how many were correct
    # the percent must be a SCORE on the count ("scored 65%", "got 65%"); a bare "65% of the students passed" is a percent of something else
    if not re.search(r"\b(?:scored|score of|got|earned|made|scoring)\s+(?:an?\s+|only\s+|about\s+|a score of\s+)?$", t[:pct[0][2]].rstrip() + " "):
        return None
    q = t.rfind("how many")
    if q == -1 or not re.search(r"\b(?:correct\w*|right|passed|made|scored|earned|got)\b", t[q:]) or re.search(r"\bwhat percent\b|\bhow much\b", t):
        return None
    n, p = cnt[0][0], pct[0][0]
    if n <= 0 or not (0 <= p <= 100):
        return None
    result = n * p / 100
    if result.denominator != 1:
        return None
    eq = "%s x %s/100" % (show(n), show(p))
    return Result("percent_of_count", [result], eq, "%s, so %s answered correctly" % (eq, show_exact(result)))


# ---------------------------------------------------------------------------------------------------------
# 34. percent change from one amount to another:   (new - old) / old x 100      (the generator's "A town's population changed from ... to ...")
# ---------------------------------------------------------------------------------------------------------
_PCHG_FROM_TO = re.compile(r"\bfrom\s+\$?(\d+(?:\.\d+)?)(?:\s+[a-z]+)?\s+to\s+\$?(\d+(?:\.\d+)?)\b")
# clean() turns the word "percent" into "%", so the question is read as "the % change"
_PCHG_ASK = re.compile(r"\bby what %[^.?!]*\bchange|%\s*change\b|\bchange in %|\bwhat %[^.?!]*\bchange|\bpercentage change\b")
_PCHG_OTHER = re.compile(r"\b(?:increase\w*|decrease\w*|new|how many|how much|compound\w*|average|each year|per year|annual\w*|monthly|total|difference)\b")


def percent_change_between(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 2 or _CHANGES_EQUATION.search(t) or t.count("%") != 1 or re.search(_SPELLED_ANY, t) or len({n[1] for n in nums}) != 1:
        return None
    if any(t[n[3]:n[3] + 2].strip().startswith("%") for n in nums):
        return None                                              # "from 20% to 25%" is points, not an amount
    m = _PCHG_FROM_TO.search(t)
    if not m:
        return None
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    q = next((s for s in reversed(sents) if "%" in s), None)
    if q is None or not _PCHG_ASK.search(q) or _PCHG_OTHER.search(q):
        return None
    old, new = Fraction(m.group(1)), Fraction(m.group(2))
    if old <= 0 or new < 0 or old == new:
        return None
    pct = (new - old) / old * 100
    eq = "(%s - %s) / %s x 100" % (show(new), show(old), show(old))
    return Result("percent_change_between", [pct], eq, "%s = %s percent (a fall is negative)" % (eq, show_exact(pct)))


# ---------------------------------------------------------------------------------------------------------
# 35. ages with a later multiple:   j = k e,   j + y = m (e + y)      (the generator's "X is k times as old as Y. In y years, X will be m times as old as Y")
# ---------------------------------------------------------------------------------------------------------
_AGEM = re.compile(r"(?P<a>[a-z]+(?: [a-z]+)?) is (?P<k>\d+) times as old as (?P<b>[a-z]+(?: [a-z]+)?)\.\s*in (?P<y>\d+) years?,\s*(?P=a) will be (?P<m>\d+) times as old as (?P=b)\b")


def ages_later_multiple(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or "$" in t or "%" in t or _CHANGES_EQUATION.search(t) or re.search(_SPELLED_ANY, t) or re.search(r"\b(?:ago|sum|difference|together|older than|younger than)\b", t):
        return None
    m = _AGEM.search(t)
    if not m or m.group("a") == m.group("b"):
        return None
    rest = t[:m.start()] + " " + t[m.end():]
    if re.search(r"\d", rest) or not re.search(r"\bhow old (?:is each|are they|are (?:both|the two))\b|\bfind (?:each|their|both) (?:age|of their ages)", rest):
        return None
    k, y, mm = Fraction(m.group("k")), Fraction(m.group("y")), Fraction(m.group("m"))
    if k == mm or k <= 0 or mm <= 0 or y <= 0:
        return None
    e = y * (mm - 1) / (k - mm)
    j = k * e
    if e <= 0 or j <= 0 or e.denominator != 1 or j.denominator != 1:
        return None
    eq = "j = %se;  j + %s = %s(e + %s)" % (show(k), show(y), show(mm), show(y))
    return Result("ages_later_multiple", [j, e], eq,
                  "j = %s's age, e = %s's age: %s, so e = %s and j = %s" % (m.group("a"), m.group("b"), eq, show_exact(e), show_exact(j)))


# ---------------------------------------------------------------------------------------------------------
# 36. a shared fixed cost plus a fee each:   B / n + f = E      (the generator's "A field trip costs $B for the bus plus $f admission per student")
# ---------------------------------------------------------------------------------------------------------
_SHARED_RATE = re.compile(r"\s*(?:[a-z]+\s+){0,2}per\s+([a-z]+)")
_SHARED_OTHER = re.compile(r"\b(?:tax|discount\w*|tip|free|first|extra|additional|chaperone\w*|teachers?|unequally|only)\b|%")


def shared_fixed_cost(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or not all(n[1] for n in nums) or _CHANGES_EQUATION.search(t) or _SHARED_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    rated = [(n, _SHARED_RATE.match(t[n[3]:])) for n in nums]
    rated = [(n, m) for n, m in rated if m]
    if len(rated) != 1:
        return None
    rate_n, rate_m = rated[0]
    others = [n for n in nums if n is not rate_n]
    B, E = others[0], others[1]
    if not (B[2] < E[2]):
        return None
    # the shared cost is followed by "for / plus"; the amount each person pays is introduced by "pays / paid / costs" in a sentence that says each / every
    if not re.match(r"\s*(?:for|plus|\+|to)\b", t[B[3]:]) or _EACH_AFTER.match(t[B[3]:]):
        return None
    sent_start = max(t.rfind(".", 0, E[2]), t.rfind("?", 0, E[2]), t.rfind("!", 0, E[2])) + 1
    before = t[sent_start:E[2]].rstrip()
    if not re.search(r"\b(?:pays?|paid|costs?|owes?)(?: a total of)?$", before) or not re.search(r"\b(?:each|every)\b", before):
        return None
    unit = _stem_unit(rate_m.group(1))
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    q = next((s for s in reversed(sents) if re.search(r"\bhow\b", s)), None)
    if q is None or re.search(r"\bhow much\b|\bper\b|\bcost\b", q):
        return None
    qm = re.search(r"\bhow many ([a-z]+)", q)
    if not qm or _stem_unit(qm.group(1)) != unit:
        return None
    bus, fee, each = B[0], rate_n[0], E[0]
    if bus <= 0 or fee < 0 or each <= fee:
        return None
    n = bus / (each - fee)
    if n <= 0 or n.denominator != 1:
        return None
    eq = "%s/n + %s = %s" % (show(bus), show(fee), show(each))
    return Result("shared_fixed_cost", [n], eq,
                  "n = number of %ss: %s, so n = %s / %s = %s" % (unit, eq, show(bus), show_exact(each - fee), show_exact(n)))


# ---------------------------------------------------------------------------------------------------------
# 37. two rates working on one pile together:   (r1 + r2) t = W      (the generator's "Two typists type a and b words per minute ...")
# ---------------------------------------------------------------------------------------------------------
_PILE_RATES = [
    re.compile(r"(\d+(?:\.\d+)?)\s*(?:[a-z]+\s+)?and\s+(\d+(?:\.\d+)?)\s+([a-z]+)\s+(?:per|a|each)\s+([a-z]+)"),
    re.compile(r"(\d+(?:\.\d+)?)\s+([a-z]+)\s+(?:per|a|each)\s+([a-z]+)\s+and\s+(\d+(?:\.\d+)?)\s+(?:\2)\s+(?:per|a|each)\s+(?:\3)"),
]
_PILE_WORKERS = re.compile(r"\btwo (?:typists|workers|machines|printers|pumps|pipes|people|painters|bakers|copiers|computers|robots|trucks|scanners|clerks|writers|friends|students|assistants)\b")
_PILE_OTHER = re.compile(r"\b(?:alone|then|first|after|before|later|earlier|breaks?|stops?|rests?|each other|faster|slower|more than|less than|per hour of|how fast|how many (?:words|pages|items|pieces|units) per)\b|%|\$")
_PILE_TIME = {"minute": "minute", "min": "minute", "hour": "hour", "hr": "hour", "second": "second", "sec": "second", "day": "day", "week": "week"}


def two_rates_one_pile(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or _CHANGES_EQUATION.search(t) or _PILE_OTHER.search(t) or re.search(_SPELLED_ANY, _PILE_WORKERS.sub(" ", t)):
        return None
    if not re.search(r"\b(?:together|both|combined|at the same time|at once)\b", t):
        return None
    found = None
    m = _PILE_RATES[0].search(t)
    if m:
        found = (Fraction(m.group(1)), Fraction(m.group(2)), m.group(3), m.group(4), m.end())
    else:
        m = _PILE_RATES[1].search(t)
        if m:
            found = (Fraction(m.group(1)), Fraction(m.group(4)), m.group(2), m.group(3), m.end())
    if found is None:
        return None
    r1, r2, unit, per, end = found
    tname = _PILE_TIME.get(per.rstrip("s"), _PILE_TIME.get(per))
    if tname is None:
        return None
    rate_pos = {m.start(1), m.start(2) if m.re is _PILE_RATES[0] else m.start(4)}
    rest = [n for n in nums if not any(n[2] <= p < n[3] for p in rate_pos)]
    if len(rest) != 1 or rest[0][1]:
        return None
    W_n = rest[0]
    wm = re.match(r"\s*(?:of\s+)?" + re.escape(unit) + r"\b", t[W_n[3]:])
    if not wm:
        return None
    # the question asks for the TIME, in the unit of the rates
    qm = re.search(r"\bhow (?:long|many (" + "|".join(_PILE_TIME) + r")s?|much time)\b", t)
    if not qm or (qm.group(1) and _PILE_TIME[qm.group(1)] != tname):
        return None
    if r1 <= 0 or r2 <= 0 or W_n[0] <= 0:
        return None
    tt = W_n[0] / (r1 + r2)
    eq = "(%s + %s)t = %s" % (show(r1), show(r2), show(W_n[0]))
    return Result("two_rates_one_pile", [tt], eq, "t = %ss: %s, so t = %s %s%s" % (tname, eq, show_exact(tt), tname, "" if tt == 1 else "s"))


# ---------------------------------------------------------------------------------------------------------
# 38. the least number sold for a profit:   p n - F >= G, the least whole n      (the generator's "A school dance costs $F to run. Tickets are $p.")
# ---------------------------------------------------------------------------------------------------------
_LEAST_FIXED_AFTER = re.compile(r"\s*(?:to\s+(?:run|host|put on|hold|stage|organize|set up|produce|operate)|in (?:costs|expenses))\b")
_LEAST_GOAL_BEFORE = re.compile(r"\bat least\s*$")
_LEAST_PRICE_BEFORE = re.compile(r"(?:([a-z]+)\s+)?(?:are|is|cost|costs|sell for|sells for|go for|goes for|priced at|sold at|at)\s*$")
_LEAST_OTHER = re.compile(r"\b(?:at most|no more than|maximum|fewer|less than|tax|discount\w*|free|loss|break even|each month|per month|first)\b|%")


def least_for_profit(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or not all(n[1] for n in nums) or _CHANGES_EQUATION.search(t) or _LEAST_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    if not re.search(r"\bprofit\b", t) or not re.search(r"\bat least\b", t):
        return None
    G = [n for n in nums if _LEAST_GOAL_BEFORE.search(t[:n[2]].rstrip())]
    F = [n for n in nums if _LEAST_FIXED_AFTER.match(t[n[3]:])]
    if len(G) != 1 or len(F) != 1 or G[0] is F[0]:
        return None
    P = [n for n in nums if n is not G[0] and n is not F[0]]
    if len(P) != 1:
        return None
    price_n = P[0]
    pm = _LEAST_PRICE_BEFORE.search(t[:price_n[2]].rstrip())
    per_unit = re.match(r"\s*(?:each|apiece|per\s+[a-z]+)\b", t[price_n[3]:])
    if not pm and not per_unit:
        return None
    if _EACH_AFTER.match(t[F[0][3]:]) or _EACH_AFTER.match(t[G[0][3]:]):
        return None
    # the question asks how many (of the thing sold) must be sold
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    q = next((s for s in reversed(sents) if re.search(r"\bhow many\b", s)), None)
    if q is None or not re.search(r"\b(?:must|need to|have to|has to|should)\b[^.?!]*\b(?:sold|sell|sale)\b|\b(?:sold|sell)\b[^.?!]*\b(?:must|need)\b", q):
        return None
    qm = re.search(r"\bhow many ([a-z]+)", q)
    noun = pm.group(1) if pm else None
    if noun and qm and _stem_unit(noun) != _stem_unit(qm.group(1)):
        return None
    cost, price, goal = F[0][0], price_n[0], G[0][0]
    if price <= 0 or goal < 0 or cost < 0:
        return None
    need = (goal + cost) / price
    n = -((-need.numerator) // need.denominator)          # ceiling of an exact fraction
    if n < 1 or not (price * n - cost >= goal and price * (n - 1) - cost < goal):
        return None
    eq = "%sn - %s >= %s" % (show(price), show(cost), show(goal))
    return Result("least_for_profit", [Fraction(n)], eq,
                  "%s, so n >= %s and the least is %s (%s sold make $%s, one fewer makes $%s)" % (
                      eq, show_exact(need), n, n, show_exact(price * n - cost), show_exact(price * (n - 1) - cost)))


# ---------------------------------------------------------------------------------------------------------
# 39. two seat prices written "at $p" before the number, a known count and a total:   x + y = N,  p1 x + p2 y = T     (the generator's "concert")
# ---------------------------------------------------------------------------------------------------------
_SEAT_TOTAL_BEFORE = re.compile(r"(?:\b(?:totaled|totalled|total|sales|revenue|receipts|brought in|collected|raised|earned|made|grossed|came to|comes to)"
                                r"(?:\s+(?:was|were|is|of|came to|comes to|totaled|totalled))?)\s*$")
_SEAT_TWO_WORDS = re.compile(r"\btwo (?:kinds|types|sections|classes|levels|sizes|categories|prices)\b")
_SEAT_OTHER = re.compile(r"\b(?:tax|discount\w*|fee|fees|percent|free|extra|also|third|another|rest|remaining|bonus|refund\w*)\b|%")


def two_priced_items(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 4 or _CHANGES_EQUATION.search(t) or _SEAT_OTHER.search(t) or re.search(_SPELLED_ANY, _SEAT_TWO_WORDS.sub(" ", t)):
        return None
    money = [n for n in nums if n[1]]
    plain = [n for n in nums if not n[1]]
    if len(money) != 3 or len(plain) != 1:
        return None
    prices = [n for n in money if re.search(r"\bat\s*$", t[:n[2]].rstrip())]
    others = [n for n in money if n not in prices]
    if len(prices) != 2 or len(others) != 1:
        return None
    T = others[0]
    if not (_SEAT_TOTAL_BEFORE.search(t[:T[2]].rstrip()) or re.match(r"\s*(?:in total|altogether)\b", t[T[3]:])) or _EACH_AFTER.match(t[T[3]:]):
        return None
    if not (prices[0][2] < prices[1][2] < T[2]):
        return None                                           # the prices come first, then the total
    N = plain[0][0]
    if N <= 0 or N.denominator != 1 or not re.match(r"\s*[a-z]+", t[plain[0][3]:]):
        return None
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    q = next((s for s in reversed(sents) if re.search(r"\bhow many\b", s)), None)
    if q is None or not re.search(r"\beach\b", q):
        return None
    p1, p2, total = prices[0][0], prices[1][0], T[0]
    if p1 == p2 or p1 <= 0 or p2 <= 0:
        return None
    y = (total - p1 * N) / (p2 - p1)
    x = N - y
    if x <= 0 or y <= 0 or x.denominator != 1 or y.denominator != 1:
        return None
    e1, e2 = "x + y = %s" % show(N), "%sx + %sy = %s" % (show(p1), show(p2), show(total))
    return Result("two_priced_items", [x, y], "%s;  %s" % (e1, e2),
                  "x = number at $%s, y = number at $%s: %s and %s, so x = %s and y = %s" % (
                      show(p1), show(p2), e1, e2, show_exact(x), show_exact(y)))


# ---------------------------------------------------------------------------------------------------------
# 40. a plan that includes some, then charges extra:   B + r (d - I) = T      (the generator's "phone plan ... includes I GB ... Each extra GB costs $r")
# ---------------------------------------------------------------------------------------------------------
_PLAN_INCLUDES = re.compile(r"\bincludes?\s+(\d+(?:\.\d+)?)\s*([a-z]+)\b")
_PLAN_EXTRA = [
    re.compile(r"\b(?:each|every|per)\s+(?:extra|additional)\s+([a-z]+)\s+(?:costs?|is|are|charges?)\s+\$(\d+(?:\.\d+)?)"),
    re.compile(r"\$(\d+(?:\.\d+)?)\s+(?:per|for each|for every|a)\s+(?:extra|additional)\s+([a-z]+)"),
]
_PLAN_OTHER = re.compile(r"\b(?:unlimited|tax|discount\w*|fee|fees|percent|free|rest|remaining|how much extra|how many extra|extra data)\b|%")
_PLAN_BILL_BEFORE = re.compile(r"\b(?:bill|total|charge|charged|cost|owed|owes?|paid|pays?)(?:\s+(?:was|is|came to|comes to))?\s*$")


def plan_with_included(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 4 or _CHANGES_EQUATION.search(t) or _PLAN_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    im = list(_PLAN_INCLUDES.finditer(t))
    if len(im) != 1:
        return None
    inc, unit = Fraction(im[0].group(1)), im[0].group(2)
    em = _PLAN_EXTRA[0].search(t)
    if em:
        eunit, rate = em.group(1), Fraction(em.group(2))
    else:
        em = _PLAN_EXTRA[1].search(t)
        if not em:
            return None
        rate, eunit = Fraction(em.group(1)), em.group(2)
    if _stem_unit(eunit) != _stem_unit(unit):
        return None
    inc_pos, rate_pos = im[0].start(1), em.start(2) if em.re is _PLAN_EXTRA[0] else em.start(1)
    rest = [n for n in nums if not any(n[2] <= p < n[3] for p in (inc_pos, rate_pos))]
    if len(rest) != 2 or not all(n[1] for n in rest):
        return None
    base, bill = rest[0], rest[1]
    if not re.match(r"\s*(?:a|per|each|every)\s+(?:month|week|day|year)\b", t[base[3]:]):
        return None
    if not _PLAN_BILL_BEFORE.search(t[:bill[2]].rstrip()) or _EACH_AFTER.match(t[bill[3]:]):
        return None
    # the question asks for the TOTAL used, not only the extra
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    q = next((s for s in reversed(sents) if re.search(r"\bhow (?:much|many)\b", s)), None)
    if q is None or not re.search(r"\b(?:used|use|uses|consumed)\b", q):
        return None
    # "how many X" must count the included unit: "how many hours" on a plan in GB asks for something else
    hm = re.search(r"\bhow many ([a-z]+)", q)
    if hm and _stem_unit(hm.group(1)) != _stem_unit(unit):
        return None
    B, T = base[0], bill[0]
    if rate <= 0 or inc < 0 or T <= B:
        return None                                           # a bill that is not above the monthly price means no extra was used
    d = inc + (T - B) / rate
    eq = "%s + %s(d - %s) = %s" % (show(B), show(rate), show(inc), show(T))
    return Result("plan_with_included", [d], eq,
                  "d = total %s used: %s, so d = %s + (%s - %s) / %s = %s %s" % (
                      unit, eq, show(inc), show(T), show(B), show(rate), show_exact(d), unit))


# ---------------------------------------------------------------------------------------------------------
# 41. the most that still fits under a limit:   w + b n <= L, the greatest whole n      (the generator's "elevator holds at most")
# ---------------------------------------------------------------------------------------------------------
_FITS_UNIT = r"(?:lbs?|pounds?|kg|kilograms?)"
_FITS_LIMIT_BEFORE = re.compile(r"\b(?:at most|up to|maximum of|no more than|capacity of|limit of|holds|can hold)\s*$")
_FITS_OTHER = re.compile(r"\b(?:at least|more than|fewer|less than|trips|each way|round trip|twice|empty|already over|tax|discount\w*)\b|%|\$")


def most_that_fits(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or _CHANGES_EQUATION.search(t) or _FITS_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    if not re.search(r"\bat most\b|\bup to\b|\bno more than\b|\bmaximum\b|\bcapacity\b|\blimit\b", t):
        return None
    for n in nums:
        if n[1] or not re.match(r"\s*" + _FITS_UNIT + r"\b", t[n[3]:]):
            return None
    unit_words = [re.match(r"\s*(" + _FITS_UNIT + r")\b", t[n[3]:]).group(1) for n in nums]
    if len({_UNIT_NAMES[w] for w in unit_words}) != 1:
        return None                                           # all three weights in one unit
    lim = [n for n in nums if _FITS_LIMIT_BEFORE.search(t[:n[2]].rstrip())]
    if len(lim) != 1:
        return None
    L = lim[0]
    others = [n for n in nums if n is not L]
    # the question names the thing loaded ("how many boxes can go up ..."): its weight is the one followed by that noun
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    q = next((s for s in reversed(sents) if re.search(r"\bhow many\b", s)), None)
    if q is None or not re.search(r"\b(?:go|fit|fits|be loaded|be carried|be added|be put|can be|can go|can the)\b", q):
        return None
    qm = re.search(r"\bhow many ([a-z]+)", q)
    if not qm:
        return None
    noun = _stem_unit(qm.group(1))
    item = [n for n in others if (re.match(r"\s*" + _FITS_UNIT + r"\s+([a-z]+)", t[n[3]:]) and _stem_unit(re.match(r"\s*" + _FITS_UNIT + r"\s+([a-z]+)", t[n[3]:]).group(1)) == noun)]
    if len(item) != 1:
        return None
    body = item[0]
    base = [n for n in others if n is not body][0]
    if not re.match(r"\s*" + _FITS_UNIT + r"\s+(?:worker|person|man|woman|operator|driver|passenger|helper|employee|attendant|cart|trolley|pallet|loader|mover)\b", t[base[3]:]):
        return None
    limit, w, b = L[0], base[0], body[0]
    if b <= 0 or w < 0 or w >= limit:
        return None                                           # a load that is already at or over the limit leaves no room
    n = (limit - w) // b
    if n < 1 or not (w + b * n <= limit < w + b * (n + 1)):
        return None
    eq = "%s + %sn <= %s" % (show(w), show(b), show(limit))
    return Result("most_that_fits", [Fraction(n)], eq,
                  "%s, so n <= %s and the most is %s (one more would weigh %s, over %s)" % (
                      eq, show_exact((limit - w) / b), show_exact(Fraction(n)), show_exact(w + b * (n + 1)), show(limit)))


# ---------------------------------------------------------------------------------------------------------
# 42. a straight fare from two rides:   4m + b = y1,  11m + b = y2, then  m x + b = target      (the generator's "The cost is linear: C = m·x + b")
# ---------------------------------------------------------------------------------------------------------
_LINE2_RIDE = re.compile(r"(?<![\w$.])(\d+(?:\.\d+)?)\s+([a-z]+)\s+cost\s+\$(\d+(?:\.\d+)?)")
_LINE2_TARGET = re.compile(r"\bhow many ([a-z]+)\s+cost\s+\$(\d+(?:\.\d+)?)")
_LINE2_OTHER = re.compile(r"\b(?:quadratic|exponential|squared|per|each|tax|discount\w*|%)\b|%")


def line_from_two_points(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if _CHANGES_EQUATION.search(t) or _LINE2_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    rides = list(_LINE2_RIDE.finditer(t))
    tm = list(_LINE2_TARGET.finditer(t))
    if len(rides) < 2 or len(tm) != 1 or len(nums) != 2 * len(rides) + 1:
        return None
    unit = _stem_unit(rides[0].group(2))
    if any(_stem_unit(r.group(2)) != unit for r in rides) or _stem_unit(tm[0].group(1)) != unit:
        return None
    pts = [(Fraction(r.group(1)), Fraction(r.group(3))) for r in rides]
    (x1, y1), (x2, y2) = pts[0], pts[1]
    if x1 == x2:
        return None
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    # a further ride must sit on the same line
    if any(y != m * x + b for x, y in pts[2:]):
        return None
    if m <= 0 or b < 0:
        return None
    target = Fraction(tm[0].group(2))
    x = (target - b) / m
    if x <= 0 or (x.denominator != 1 and unit not in _FIXED_CONTINUOUS):
        return None
    asks_mb = bool(re.search(r"\bfind m and b\b|\bfind the rate and\b|\bfind m, b\b", t))
    vals = [m, b, x] if asks_mb else [x]
    eq = "%sm + b = %s;  %sm + b = %s;  %sx + %s = %s" % (show(x1), show(y1), show(x2), show(y2), show(m), show(b), show(target))
    return Result("line_from_two_points", vals, eq,
                  "m = (%s - %s) / (%s - %s) = %s and b = %s - %s x %s = %s: C = %sx + %s; %sx + %s = %s, so x = %s %s%s" % (
                      show(y2), show(y1), show(x2), show(x1), show_exact(m), show(y1), show_exact(m), show(x1), show_exact(b),
                      show_exact(m), show_exact(b), show_exact(m), show_exact(b), show(target), show_exact(x), unit, "" if x == 1 else "s"))


# ---------------------------------------------------------------------------------------------------------
# 43. an election margin:   (2p - 100)% of V = M      (the generator's "In a two-candidate election, the winner got p% of the votes and won by M votes")
# ---------------------------------------------------------------------------------------------------------
_VOTE_OTHER = re.compile(r"\b(?:three|third|runner-up|others?|independent|spoiled|abstain\w*|absent|turnout|each|per)\b|\$")


def election_margin(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 2 or t.count("%") != 1 or _CHANGES_EQUATION.search(t) or _VOTE_OTHER.search(t):
        return None
    if re.search(_SPELLED_ANY, re.sub(r"\btwo[- ](?:candidate|person|way|party|man|woman)s?\b", " ", t)):
        return None
    pct = [n for n in nums if t[n[3]:n[3] + 2].strip().startswith("%")]
    other = [n for n in nums if n not in pct]
    if len(pct) != 1 or len(other) != 1 or other[0][1]:
        return None
    if not re.match(r"\s*%\s*of\s+the\s+(?:votes|vote|ballots|total)\b", t[pct[0][3]:]):
        return None
    if not re.search(r"\b(?:winner|won|wins|winning)\b", t) or re.search(r"\b(?:loser|lost|lose|loses)\b", t):
        return None
    if not re.match(r"\s*(?:votes|ballots)\b", t[other[0][3]:]) or not re.search(r"\b(?:won|wins|win) by\s*$|\bmargin of\s*$", t[:other[0][2]].rstrip()):
        return None
    q = t.rfind("how many")
    if q == -1 or not re.search(r"\b(?:votes|ballots)\b[^.?!]*\b(?:cast|in all|total|altogether|counted)\b", t[q:]):
        return None
    p, M = pct[0][0], other[0][0]
    if not (50 < p < 100) or M <= 0:
        return None
    gap = (2 * p - 100) / 100                                  # the winner's share minus the other candidate's
    V = M / gap
    if V <= 0 or V.denominator != 1:
        return None
    eq = "%s%% of V - %s%% of V = %s" % (show(p), show(100 - p), show(M))
    return Result("election_margin", [V], eq,
                  "%s, so %sV = %s and V = %s" % (eq, show(gap), show(M), show_exact(V)))


# ---------------------------------------------------------------------------------------------------------
# 44. the same time with and against the wind:   a / (p + w) = b / (p - w)      (the generator's "plane ... tailwind ... headwind")
# ---------------------------------------------------------------------------------------------------------
_WIND_SPEED_UNIT = r"(?:mph|km/h|kph|miles per hour|kilometers per hour|kilometres per hour)"
_WIND_DIST_UNIT = r"(?:miles?|mi|km|kilometers?|kilometres?)"
_WIND_WITH = re.compile(r"(\d+(?:\.\d+)?)\s*(" + _WIND_DIST_UNIT + r")\s+with\s+an?\s+(\d+(?:\.\d+)?)\s*(" + _WIND_SPEED_UNIT + r")\s+(?:tailwind|wind)")
_WIND_AGAINST = re.compile(r"in the same time (?:it|the \w+) flies\s+(\d+(?:\.\d+)?)\s*(" + _WIND_DIST_UNIT + r")\s+(?:into|against)\s+(?:the same|that|this|the)\s+(?:wind|headwind)")
_WIND_OTHER = re.compile(r"\b(?:round trip|return\w*|back|stops?|rests?|twice|fuel|climb\w*|descend\w*)\b|%|\$")


def wind_same_time(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or _CHANGES_EQUATION.search(t) or _WIND_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    wm, am = _WIND_WITH.search(t), _WIND_AGAINST.search(t)
    if not wm or not am:
        return None
    a, w, b = Fraction(wm.group(1)), Fraction(wm.group(3)), Fraction(am.group(1))
    d1, d2 = _dist_group(wm.group(2)), _dist_group(am.group(2))
    if not (d1 == d2 == _speed_group(wm.group(4))):
        return None
    # the question asks for the speed in still air
    if not re.search(r"\bspeed\b[^.?!]*\b(?:still air|calm air|no wind|without (?:the )?wind)\b|\b(?:still air|calm air)\b[^.?!]*\bspeed\b", t):
        return None
    if a <= 0 or b <= 0 or w <= 0 or b >= a:
        return None                                            # the headwind trip must be the shorter one, or no speed can be found
    p = w * (a + b) / (a - b)
    if p <= w:
        return None
    eq = "%s/(p + %s) = %s/(p - %s)" % (show(a), show(w), show(b), show(w))
    return Result("wind_same_time", [p], eq,
                  "%s, so %s(p - %s) = %s(p + %s) and p = %s %s" % (eq, show(a), show(w), show(b), show(w), show_exact(p), "mph" if d1 == "mi" else "km/h"))


# ---------------------------------------------------------------------------------------------------------
# 45. an allowance plus extra chores over some weeks:   w a + c n = T      (the generator's "gets $a allowance a week plus $c for each extra chore. Over w weeks ...")
# ---------------------------------------------------------------------------------------------------------
_EXTRA_BASE = re.compile(r"\$(\d+(?:\.\d+)?)\s+(?:allowance|pay|salary|wage|stipend|base pay)\s+(?:a|per|each|every)\s+(week|month|day|year)\b")
_EXTRA_RATE = re.compile(r"\$(\d+(?:\.\d+)?)\s+(?:for|per)\s+(?:each|every)\s+(?:extra|additional)\s+([a-z]+)\b")
_EXTRA_PERIOD = re.compile(r"\b(?:over|for|in|during)\s+(\d+(?:\.\d+)?)\s+(weeks?|months?|days?|years?)\b")
_EXTRA_TOTAL_BEFORE = re.compile(r"\b(?:came to|comes to|totaled|totalled|total of|earned|received|got|made|paid|add(?:ed)? up to|adds up to)\s*$")
_EXTRA_OTHER = re.compile(r"\b(?:tax|bonus|deduct\w*|fine|fines|lost|missed|half|twice|each week they|average)\b|%")


def base_plus_extra_over_time(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 4 or _CHANGES_EQUATION.search(t) or _EXTRA_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    bm, rm, pm = _EXTRA_BASE.search(t), _EXTRA_RATE.search(t), _EXTRA_PERIOD.search(t)
    if not bm or not rm or not pm:
        return None
    a, c, w = Fraction(bm.group(1)), Fraction(rm.group(1)), Fraction(pm.group(1))
    if _stem_unit(pm.group(2)) != _stem_unit(bm.group(2)):
        return None
    used = [bm.start(1), rm.start(1), pm.start(1)]
    rest = [n for n in nums if not any(n[2] <= u < n[3] for u in used)]
    if len(rest) != 1 or not rest[0][1]:
        return None
    T = rest[0]
    if not _EXTRA_TOTAL_BEFORE.search(t[:T[2]].rstrip()) or _EACH_AFTER.match(t[T[3]:]):
        return None
    # the question asks how many extra <things> (the same noun as "each extra chore"), not an amount of money
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    q = next((s for s in reversed(sents) if re.search(r"\bhow\b", s)), None)
    if q is None or re.search(r"\bhow much\b|\btotal\b|\bper\b", q):
        return None
    qm = re.search(r"\bhow many (?:extra |additional )?([a-z]+)", q)
    if not qm or _stem_unit(qm.group(1)) != _stem_unit(rm.group(2)):
        return None
    if c <= 0 or a < 0 or w <= 0 or T[0] <= a * w:
        return None                                              # nothing above the base pay means no extra work
    n = (T[0] - a * w) / c
    if n <= 0 or n.denominator != 1:
        return None
    eq = "%s x %s + %sn = %s" % (show(w), show(a), show(c), show(T[0]))
    return Result("base_plus_extra_over_time", [n], eq, "n = number of extra %ss: %s, so n = (%s - %s) / %s = %s" % (
        _stem_unit(rm.group(2)), eq, show(T[0]), show(a * w), show(c), show_exact(n)))


# ---------------------------------------------------------------------------------------------------------
# 46. distance, speed and time:   D = S t, the one the question asks for      (the generator's "Using distance = speed x time, how long does it take to travel 160 km at 40 km/h?")
# ---------------------------------------------------------------------------------------------------------
_DST_DIST = re.compile(NUM + r"\s*(miles?|mi|kilometers?|kilometres?|km)\b(?![/\w])")
_DST_TIME = re.compile(NUM + r"\s*(hours?|hrs?|h)(?![\w/])")
_DST_OTHER = re.compile(r"\b(?:then|after that|back|return\w*|round trip|each way|stops?|rests?|breaks?|also|another|faster than|slower than|twice|acceleration|"
                        r"average speed|against|with the|current|wind|stream)\b|%|\$|²")


def distance_speed_time(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 2 or _CHANGES_EQUATION.search(t) or _DST_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    sp = list(_SPEED.finditer(t))
    spans = [(m.start(), m.end()) for m in sp]
    dist = [m for m in _DST_DIST.finditer(t) if not any(s <= m.start() < e for s, e in spans)]
    tim = [m for m in _DST_TIME.finditer(t) if not any(s <= m.start() < e for s, e in spans)]
    given = {"speed": sp, "distance": dist, "time": tim}
    present = [k for k, v in given.items() if len(v) == 1]
    if len(present) != 2 or any(len(v) > 1 for v in given.values()) or sum(len(v) for v in given.values()) != 2:
        return None
    # the question asks for the third quantity
    q = t.rfind("how ")
    if q == -1:
        q = t.rfind("what ")
    if q == -1:
        return None
    tail = t[q:]
    asks_time = bool(re.search(r"\bhow long\b|\bhow (?:many|much) (?:hours?|time)\b|\bwhat time\b", tail))
    asks_dist = bool(re.search(r"\bhow far\b|\bwhat distance\b|\bhow many (?:miles|kilometers|kilometres|km)\b", tail))
    asks_speed = bool(re.search(r"\bhow fast\b|\bwhat (?:speed|rate)\b|\bwhat is the speed\b|\bhow many (?:mph|km/h)\b", tail))
    if sum([asks_time, asks_dist, asks_speed]) != 1:
        return None
    missing = [k for k in ("speed", "distance", "time") if k not in present]
    if len(missing) != 1 or not {"time": asks_time, "distance": asks_dist, "speed": asks_speed}[missing[0]]:
        return None
    vals = {}
    if sp:
        vals["S"] = Fraction(sp[0].group(1))
        sgroup = _speed_group(sp[0].group(2))
    if dist:
        vals["D"] = Fraction(dist[0].group(1))
        dgroup = _dist_group(dist[0].group(2))
    if tim:
        vals["T"] = Fraction(tim[0].group(1))
    if sp and dist and sgroup != dgroup:
        return None                                              # the distance unit and the speed unit have to match
    unit_d = ("miles" if sgroup == "mi" else "km") if sp else ("miles" if dgroup == "mi" else "km")
    unit_s = "mph" if (sp and sgroup == "mi") or (not sp and dgroup == "mi") else "km/h"
    if any(v <= 0 for v in vals.values()):
        return None
    if missing[0] == "time":
        res = vals["D"] / vals["S"]
        eq = "%s = %st" % (show(vals["D"]), show(vals["S"]))
        text = "%s, so t = %s hour%s" % (eq, show_exact(res), "" if res == 1 else "s")
    elif missing[0] == "distance":
        res = vals["S"] * vals["T"]
        eq = "d = %s x %s" % (show(vals["S"]), show(vals["T"]))
        text = "%s, so d = %s %s" % (eq, show_exact(res), unit_d)
    else:
        res = vals["D"] / vals["T"]
        eq = "%s = s x %s" % (show(vals["D"]), show(vals["T"]))
        text = "%s, so s = %s %s" % (eq, show_exact(res), unit_s)
    return Result("distance_speed_time", [res], eq, text)


# a measured thing for family 26 (two_changing_equal): "Plant A is 13 cm tall and grows 3 cm a week" (a continuous quantity, so a fraction of a week is a fine answer)
_GROW_UNIT = r"(?:cm|mm|m|meters?|metres?|inch(?:es)?|in|ft|feet|foot|kg|lbs?|pounds?)"
_GROW_STMT2 = re.compile(
    r"(?<![\w$])(?P<who>[a-z]+(?:\s[a-z]+)?)\s+(?:is|are|measures)\s+(?P<a>\d+(?:\.\d+)?)\s*(?P<au>" + _GROW_UNIT + r")(?:\s+(?:tall|long|high|heavy|deep|wide))?(?:,|\s+and|\s+but)?\s+(?:and\s+)?"
    r"(?P<v>grows?|gains?|shrinks?|loses?|drops?|falls?|rises?|increases?|decreases?)(?:\s+by)?\s+(?P<c>\d+(?:\.\d+)?)\s*(?P<cu>" + _GROW_UNIT + r")\s+(?:a|per|each|every)\s+"
    r"(?P<u>year|month|week|day|hour|decade)\b")


# ---------------------------------------------------------------------------------------------------------
# 47. pages a day to finish a book:   (N - R) / D      (the generator's "A 331-page book has 13 pages already read. How many pages a day must be read to finish in 6 days?")
# ---------------------------------------------------------------------------------------------------------
_PAGES_TOTAL = re.compile(r"\b(\d+)-pages?\b|\b(book|novel|report|packet|manual)\s+(?:has|of|with)\s+(\d+)\s+pages\b")
_PAGES_BOOKISH = {"book", "novel", "story", "text", "volume", "paperback", "textbook"}
_PAGES_FUNCTION = {"the", "this", "that", "it", "my", "her", "his", "their", "its", "reading", "read", "rest", "remaining", "of", "pages", "page"}
_PAGES_READ = re.compile(r"\b(\d+)\s+pages?\s+(?:already\s+)?(?:read|finished|done|completed|written|typed)\b")
# "to finish [reading the book] in 6 days": the time allowed to finish THIS book (the present tense only; "already finished in 6 days" is how long the pages took)
_PAGES_DAYS = re.compile(r"\bfinish((?:\s+[a-z]+){0,5}?)\s+(?:in|within|over)\s+(\d+)\s+(days?|weeks?|nights?)\b")
_PAGES_OTHER = re.compile(r"\b(?:more than|less than|twice|double|half|each day she|already read twice|skip\w*|except|weekend\w*|at most|at least)\b|%|\$")


def pages_per_day(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or _CHANGES_EQUATION.search(t) or _PAGES_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    tm, rm, dm = _PAGES_TOTAL.search(t), _PAGES_READ.search(t), _PAGES_DAYS.search(t)
    if not tm or not rm or not dm:
        return None
    N = Fraction(tm.group(1) or tm.group(3))
    R, D = Fraction(rm.group(1)), Fraction(dm.group(2))
    if len({tm.start(), rm.start(), dm.start()}) != 3:
        return None
    # the words between "finish" and the day count have to be about the same book (not "the chapter", "the essay", "the race")
    nm = re.match(r"\s+([a-z]+)", t[tm.end():]) if tm.group(1) else None
    noun = tm.group(2) if tm.group(2) else (nm.group(1) if nm else None)
    if noun is None:
        return None
    allowed = _PAGES_FUNCTION | (_PAGES_BOOKISH if noun in _PAGES_BOOKISH else set()) | {noun}
    if any(w not in allowed for w in dm.group(1).split()):
        return None
    # every "finish ..." in the problem (the question too) has to name this book: "to finish the chapter?" asks about another job
    for fm in re.finditer(r"\bfinish(?:ing)?\b", t):
        after = re.split(r"[.?!]", t[fm.end():])[0]
        words = re.findall(r"[a-z]+", after)
        for stop in ("in", "within", "over"):                       # the day count itself ("in 6 days") ends the words about the book ...
            if stop in words:
                i = words.index(stop)
                tail = words[i + 1:]
                if tail and tail[0] in ("day", "days", "week", "weeks", "night", "nights"):
                    tail = tail[1:]
                words = words[:i] + tail                            # ... and whatever follows it must be about the book too ("by tomorrow" is another deadline)
        if any(w not in allowed for w in words):                    # "by tomorrow", "today", "before Friday" are a deadline of their own: decline
            return None
    unit = dm.group(3).rstrip("s")
    # the question asks for pages per (day / week / night), in the unit of the deadline
    sents = [s for s in re.split(r"[.?!]\s*", t) if s.strip()]
    q = next((s for s in reversed(sents) if re.search(r"\bhow many pages\b", s)), None)
    if q is None or not re.search(r"\b(?:a|per|each|every)\s+" + unit + r"\b", q) or not re.search(r"\b(?:must|need to|have to|should|has to|needs to)\b", q):
        return None
    if D <= 0 or R < 0 or R >= N:
        return None                                              # a deadline of zero, or the whole book already read (or more)
    p = (N - R) / D
    eq = "%s + %sp = %s" % (show(R), show(D), show(N))
    return Result("pages_per_day", [p], eq, "p = pages per %s: %s, so p = (%s - %s) / %s = %s" % (unit, eq, show(N), show(R), show(D), show_exact(p)))


# ---------------------------------------------------------------------------------------------------------
# 48. opposite (vertical) angles are equal:   a1 x + b1 = a2 x + b2      (the generator's "Where two lines cross, opposite angles are (2x + 4)° and (5x - 110)°")
# ---------------------------------------------------------------------------------------------------------
_OPPANG_EXPR = re.compile(r"\(\s*(\d*)\s*x\s*([+-])\s*(\d+(?:\.\d+)?)\s*\)\s*(?:°|degrees?)?")
_OPPANG_OTHER = re.compile(r"\b(?:adjacent|supplementary|complementary|complements?|supplements?|linear pair|straight line|add to|adds to|sum|total|together|triangle|parallel lines|"
                           r"difference|product|ratio|half|double|twice|bisect\w*|quadrilateral|cyclic|inscribed|circle|arc|chord|polygon)\b")


def opposite_angles_equal(problem):
    t = clean(problem)
    if _CHANGES_EQUATION.search(t) or _OPPANG_OTHER.search(t) or re.search(_SPELLED_ANY, re.sub(r"\btwo (?:straight )?lines\b", " ", t)):
        return None                                              # "two lines" is the two crossing lines, the shape of the problem
    if not re.search(r"\b(?:opposite|vertical) angles\b", t):
        return None
    ex = list(_OPPANG_EXPR.finditer(t))
    if len(ex) != 2:
        return None
    rest = t[:ex[0].start()] + " " + t[ex[0].end():ex[1].start()] + " " + t[ex[1].end():]
    if re.search(r"\d", rest):
        return None
    coefs = []
    for m in ex:
        a = Fraction(m.group(1)) if m.group(1) else Fraction(1)
        b = Fraction(m.group(3)) * (1 if m.group(2) == "+" else -1)
        coefs.append((a, b))
    (a1, b1), (a2, b2) = coefs
    if a1 == a2:
        return None
    x = (b2 - b1) / (a1 - a2)
    angle = a1 * x + b1
    if not (0 < angle <= 180):
        return None
    if re.search(r"\bforms?\s+(?:an?\s+)?(?:acute|obtuse|right|straight|reflex)\s+angle", t):
        return None                                              # "the opposite angles form a straight angle" means the two ADD UP to 180
    # a named kind ("the acute angle", "a straight angle") is answered only when the angle IS that kind
    kind_ok = {"acute": 0 < angle < 90, "obtuse": 90 < angle < 180, "right": angle == 90, "straight": angle == 180, "reflex": False}
    if any(not kind_ok[k] for k in re.findall(r"\b(acute|obtuse|right|straight|reflex)\s+angles?\b", t)):
        return None
    # what is asked: the angle, x, or both
    q = max(t.rfind("find"), t.rfind("what"), t.rfind("how"))
    if q == -1:
        return None
    tail = t[q:]
    asks_angle = bool(re.search(r"\bangles?\b", tail))
    asks_x = bool(re.search(r"\bx\b", tail))
    if not (asks_angle or asks_x):
        return None
    vals = ([x] if asks_x else []) + ([angle] if asks_angle else [])
    eq = "%sx %s %s = %sx %s %s" % (show(a1), "+" if b1 >= 0 else "-", show(abs(b1)), show(a2), "+" if b2 >= 0 else "-", show(abs(b2)))
    return Result("opposite_angles_equal", vals, eq,
                  "opposite angles are equal: %s, so x = %s and each angle is %s degrees" % (eq, show_exact(x), show_exact(angle)))


# ---------------------------------------------------------------------------------------------------------
# 49. a rectangle from its perimeter and its area:   l + w = P / 2,  l w = A      (the generator's "A rectangle has a perimeter of 40 ft and an area of 36 ft^2")
# ---------------------------------------------------------------------------------------------------------
_RECT_PERIM = re.compile(r"\bperimeter of\s+(\d+(?:\.\d+)?)\s*([a-z]+)\b")
_RECT_AREA = re.compile(r"\barea of\s+(\d+(?:\.\d+)?)\s*(?:(square|sq\.?)\s+)?([a-z]+)(²|\^2|2)?")      # the unit is marked squared: ft^2, ft2, sq ft, square ft
_RECT_UNIT = {"feet": "ft", "foot": "ft", "meters": "m", "metres": "m", "meter": "m", "metre": "m", "centimeters": "cm", "centimetres": "cm", "inches": "in", "inch": "in",
              "yards": "yd", "yard": "yd", "miles": "mi", "mile": "mi", "kilometers": "km", "kilometres": "km"}
_RECT_LONG = r"(?:longer|larger|greater|bigger|wider|broader|more|longest|largest|greatest|widest)"
_RECT_SHORT = r"(?:shorter|smaller|lesser|narrower|less|shortest|smallest|least|narrowest)"
_RECT_BOUNDARY = r"(?=\s*(?:$|[,;.:?!]|\b(?:and|but|while|so|then|if|when)\b))"
_RECT_REL = re.compile(r"\b(length|width|it|one)\s+(?:is|are|being)\s+(?:the\s+)?(" + _RECT_LONG + "|" + _RECT_SHORT + r")(?:\s+(?:side|one|dimension))?"
                       r"(?:\s+than\s+(?:the\s+|its\s+)?(length|width|other(?:\s+(?:side|one|dimension))?))?" + _RECT_BOUNDARY)
_RECT_SIDE = re.compile(r"\b(" + _RECT_LONG + "|" + _RECT_SHORT + r")\s+(?:side|dimension|one)\s+(?:is|being)\s+(?:the\s+)?(length|width)" + _RECT_BOUNDARY)


def _rect_length_is_longer(text, asked=None):
    """True / False when the problem says which of length and width is the longer side, None when it does not, "bad" when it contradicts itself or is unclear."""
    found = []
    for m in _RECT_REL.finditer(text):
        dim, rel, other = m.group(1), m.group(2), m.group(3)
        if not text[m.end(2):m.end()].strip():
            return "bad"                                             # "It is shorter." with nothing to compare
        if dim in ("it", "one"):                                     # "It is shorter than the width": "it" is the side the question asks for
            if asked is None:
                return "bad"
            dim = asked
        if other is not None and other == dim:
            return "bad"
        found.append((dim, bool(re.match(_RECT_LONG, rel))))
    for m in _RECT_SIDE.finditer(text):
        found.append((m.group(2), bool(re.match(_RECT_LONG, m.group(1)))))
    # a comparison word that is NOT part of a comparison of the two sides ("shorter than a foot", "more interesting than the length") is not about this rectangle: decline
    spans = [m.span() for m in _RECT_REL.finditer(text)] + [m.span() for m in _RECT_SIDE.finditer(text)]
    for w in re.finditer(r"\b(?:" + _RECT_LONG + "|" + _RECT_SHORT + r")\b", text):
        if not any(a <= w.start() < b for a, b in spans):
            return "bad"
    if not found:
        return None
    verdicts = {(longer if dim == "length" else not longer) for dim, longer in found}
    return verdicts.pop() if len(verdicts) == 1 else "bad"


_RECT_OTHER = re.compile(r"\b(?:same as|equal to|equals?|as long as|as wide as|square(?! (?:feet|foot|ft|meters?|metres?|m|cm|centimeters?|centimetres?|inch(?:es)?|in|yards?|yd|miles?|mi|km|kilometers?)\b)|diagonal|border|frame|path|cut|hole|cost|triangle|circle|twice|times as)\b|%|\$")


def rectangle_from_perimeter_area(problem):
    problem = re.sub(r"\^\s*2\b", "²", problem)              # "ft^2" is a squared mark, not a number
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 2 or _CHANGES_EQUATION.search(t) or _RECT_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    if not re.search(r"\brectangle\b", t):
        return None
    pm, am = _RECT_PERIM.search(t), _RECT_AREA.search(t)
    if not pm or not am or _RECT_UNIT.get(pm.group(2), pm.group(2)) != _RECT_UNIT.get(am.group(3), am.group(3)):
        return None                                              # the area's unit is the perimeter's unit squared
    if not (am.group(2) or am.group(4)):
        return None                                              # "an area of 36 ft" is not marked squared
    # the question: both sides, only the length (the longer side), or only the width (the shorter); a sum / difference / product of them is a different question
    sents = [x for x in re.split(r"[.?!]\s*", t) if x.strip()]
    q = next((x for x in reversed(sents) if re.search(r"\b(?:find|what|determine|give|name|calculate|compute|state|list|work out|how (?:long|wide|big|tall))\b", x)), None)
    if q is None:
        return None                                                  # no question the solver recognises ("The sides please."): decline, never raise
    q_orig = q
    # a condition inside the question ("... if the length is shorter than the width") is a STATEMENT, not part of what is asked
    cm = re.search(r"\b(?:if|when|given that|since|because|assuming|provided)\b", q) if q else None
    q_main, cond = (q[:cm.start()], q[cm.end():]) if cm else (q, "")
    q_parts = re.split(r"(?:,\s*)?\b(?:so|then|therefore)\b|;", q_main) if q_main else [q_main]
    if len(q_parts) > 1:
        cond = cond + " . " + " . ".join(q_parts[:-1])
        q_main = q_parts[-1]
    # a clause hanging on the side just named is a statement about THAT side, not a question about the other:
    #   "What is its length, which is shorter than the width?"   ->  asks the length;  statement "length is shorter than the width"
    #   "Find the length, the shorter side." / "What is its width, the longer one?"  ->  asks that side; statement "length is the shorter side"
    #   (the comma is optional: "What is its length which is shorter than the width?" is the same question)
    # "the length of the shorter side" / "the width of the longer side": the word after "of the" names the side, the word in front of "of" does not switch them
    named_kind = None
    om = re.search(r"\b(?:(?:length|width)\s+of|how\s+(?:long|wide|big|tall)\s+(?:is|are))\s+the\s+(" + _RECT_LONG + "|" + _RECT_SHORT + r")\s+(?:side|one|dimension)\b(?=\s*(?:,|$))", q_main)
    if om:
        named_kind = "long" if re.match(_RECT_LONG, om.group(1)) else "short"
        q_main = q_main[:om.start()] + " " + q_main[om.end():]
    # a clause hanging on the side just named is a statement about THAT side (it may sit in the middle: ", the shorter side, and its width"):
    #   "What is its length, which is shorter than the width?"   ->  asks the length;  statement "length is shorter than the width"
    #   "Find the length, the shorter side." / "What is its width, the longer one?"  ->  asks that side; statement "length is the shorter side"
    #   (the comma is optional: "What is its length which is shorter than the width?" is the same question)
    wm = re.search(r"\b(length|width)\s*,?\s*(?:which|that)\s+(?:is|are)\s+([^,]*?)(?=\s*(?:,|$))", q_main)
    clause_kind = "which"
    if not wm:
        wm = re.search(r"\b(length|width)\s*,?\s*(?:the\s+)?((?:" + _RECT_LONG + "|" + _RECT_SHORT + r")\s+(?:side|one|dimension))(?=\s*(?:,|$))", q_main)
        clause_kind = "apposition"
    if wm:
        before = q_main[:wm.end(1)]
        cond = cond + " . " + wm.group(1) + (" is " if clause_kind == "which" else " is the ") + wm.group(2)
        q_main = q_main[:wm.end(1)] + q_main[wm.end():]
        # when BOTH sides are named before the clause, it does not say which of the two it describes ("length and width, the longer side" vs
        # "width and length, the longer side" would give opposite answers for the same words): decline
        if re.search(r"\blength\b", before) and re.search(r"\bwidth\b", before):
            return None
    if q is None or re.search(r"\b(?:sum|difference|product|ratio|half|double|average|perimeter|area|per|more|less|larger than|longer than)\b", q_main):
        return None
    # a comparison word left in the question that is not part of a recognised clause ("the longer side of the rectangle") does not end on the comparison: decline
    if re.search(r"\b(?:" + _RECT_LONG + "|" + _RECT_SHORT + r")\b", q_main):
        return None
    q = q_main
    asks_len, asks_wid = bool(re.search(r"\blength\b", q)), bool(re.search(r"\bwidth\b", q))
    asks_both = bool(re.search(r"\b(?:sides|dimensions)\b", q)) or (asks_len and asks_wid)
    if named_kind and (asks_len or asks_wid or asks_both):
        return None                                                  # the named side AND a length / width: unclear
    if not (asks_len or asks_wid or asks_both or named_kind):
        return None
    others = " . ".join([x for x in sents if x is not q_orig] + [cond])           # the " . " keeps the end of each statement visible
    asked_side = "length" if (asks_len and not asks_wid and not asks_both) else ("width" if (asks_wid and not asks_len and not asks_both) else None)
    length_longer = _rect_length_is_longer(others, asked_side)
    if length_longer == "bad":
        return None
    P, A = Fraction(pm.group(1)), Fraction(am.group(1))
    if P <= 0 or A <= 0:
        return None
    s = P / 2
    disc = s * s - 4 * A
    if disc < 0:
        return None
    # the sides are the roots of z^2 - s z + A = 0; they must be positive and exact (a whole or fractional number, not an irrational one)
    num, den = disc.numerator, disc.denominator
    rn, rd = _isqrt_exact(num), _isqrt_exact(den)
    if rn is None or rd is None:
        return None
    root = Fraction(rn, rd)
    l, w = (s + root) / 2, (s - root) / 2
    if w <= 0:
        return None
    unit = pm.group(2)
    if length_longer is False:
        length, width = w, l                                         # the problem says the length is the shorter side
    else:
        length, width = l, w                                         # unless it says otherwise, the length is the longer side
    if named_kind:
        vals = [l] if named_kind == "long" else [w]                  # "the length of the shorter side" is the shorter side, 2
    else:
        vals = [length, width] if asks_both else ([length] if asks_len else [width])
    return Result("rectangle_from_perimeter_area", vals, "l + w = %s;  l w = %s" % (show(s), show(A)),
                  "l + w = %s and l w = %s, so the sides are the roots of z^2 - %sz + %s = 0: l = %s and w = %s %s" % (
                      show(s), show(A), show(s), show(A), show_exact(l), show_exact(w), unit))


# ---------------------------------------------------------------------------------------------------------
# 50. a falling temperature, in whole hours:   T0 - r h >= L  (or > L)      (the generator's "The temperature is 26°F and falling 3°F per hour. For how many whole hours will it stay at or above 1°F?")
# ---------------------------------------------------------------------------------------------------------
_TEMP_VAL = re.compile(r"(-?\d+(?:\.\d+)?)\s*°\s*([fc])\b")
_TEMP_FALL = re.compile(r"\b(?:falling|dropping|decreasing|cooling|falls|drops|decreases|cools|going down)\s*(?:by\s+)?$")
_TEMP_INCLUSIVE = re.compile(r"\b(?:at or above|at least|no lower than|not below|or above)\s*$")
_TEMP_STRICT = re.compile(r"\b(?:above|over|higher than|warmer than)\s*$")
_TEMP_OTHER = re.compile(r"\b(?:rising|climbing|warming|increasing|rises|climbs|warms|increases|going up|below|at or below|under|colder than|no higher than|at most)\b")


def temperature_whole_hours(problem):
    t = clean(problem)
    vals = list(_TEMP_VAL.finditer(t))
    if len(vals) != 3 or len(digit_numbers(problem)) != 3 or _CHANGES_EQUATION.search(t) or re.search(_SPELLED_ANY, t) or "$" in t or "%" in t:
        return None
    if len({v.group(2) for v in vals}) != 1:
        return None                                              # one temperature scale throughout
    # a rising temperature (or an "at or below" limit) is a different problem: decline.  "at or below" is checked on the limit phrase, "below" never appears in "at or above"
    if _TEMP_OTHER.search(re.sub(r"\bat or above\b", " ", t)):
        return None
    rate = [v for v in vals if _TEMP_FALL.search(t[:v.start()].rstrip())]
    limit = [v for v in vals if _TEMP_INCLUSIVE.search(t[:v.start()].rstrip()) or _TEMP_STRICT.search(t[:v.start()].rstrip())]
    if len(rate) != 1 or len(limit) != 1 or rate[0] is limit[0]:
        return None
    start = [v for v in vals if v is not rate[0] and v is not limit[0]]
    if len(start) != 1 or not re.search(r"\b(?:is|starts at|begins at|reads|now|currently)\s*$", t[:start[0].start()].rstrip()):
        return None
    if not re.match(r"\s*(?:per|an|each|every|a)\s+hour\b", t[rate[0].end():]):
        return None
    inclusive = bool(_TEMP_INCLUSIVE.search(t[:limit[0].start()].rstrip()))
    # the question asks for whole HOURS of staying at (or above) the limit
    if not re.search(r"\bhow many (?:whole|full) hours\b", t):
        return None
    T0, r, L = Fraction(start[0].group(1)), Fraction(rate[0].group(1)), Fraction(limit[0].group(1))
    if r <= 0:
        return None
    q = (T0 - L) / r
    floor_q = q.numerator // q.denominator
    h = floor_q if inclusive else -((-q.numerator) // q.denominator) - 1      # "above" does not include landing exactly on the limit
    if h < 1:
        return None
    unit = "°" + start[0].group(2).upper()
    cmp_ = ">=" if inclusive else ">"
    eq = "%s - %sh %s %s" % (show(T0), show(r), cmp_, show(L))
    return Result("temperature_whole_hours", [Fraction(h)], eq,
                  "%s, so h %s %s and the most whole hours is %d (after %d hours it is %s%s, after %d it is %s%s)" % (
                      eq, "<=" if inclusive else "<", show_exact(q), h, h, show_exact(T0 - r * h), unit, h + 1, show_exact(T0 - r * (h + 1)), unit))


# ---------------------------------------------------------------------------------------------------------
# 51. two candles burning down until they are the same height:   a - ra t = b - rb t      (the generator's "One candle is 13 cm tall and burns 2 cm per hour. Another ...")
# ---------------------------------------------------------------------------------------------------------
_CANDLE_UNIT = r"(?:cm|mm|m|inch(?:es)?|in)"
_CANDLE_STMT = re.compile(r"\bis\s+(\d+(?:\.\d+)?)\s*(" + _CANDLE_UNIT + r")\s+tall\s+and\s+burns\s+(\d+(?:\.\d+)?)\s*(" + _CANDLE_UNIT + r")\s+(?:per|an|each|every|a)\s+(hour|minute|day)\b")


def two_candles_equal(problem):
    t = clean(problem)
    found = list(_CANDLE_STMT.finditer(t))
    if len(found) != 2 or len(digit_numbers(problem)) != 4 or not re.search(r"\bcandles?\b", t) or _CHANGES_EQUATION.search(t) or re.search(_SPELLED_ANY, re.sub(r"\btwo candles\b", " ", t)):
        return None
    m1, m2 = found
    if not (m1.group(2) == m1.group(4) == m2.group(2) == m2.group(4)) or m1.group(5) != m2.group(5):
        return None                                              # one unit of length and one unit of time
    rest = t[:m1.start()] + " " + t[m1.end():m2.start()] + " " + t[m2.end():]
    if re.search(r"\d", rest):
        return None
    # the LAST sentence (with the two statements cut out of it) is the question, and it must ask the TIME they are the same height.  Any other sentence, with the
    # statements cut out, may not ask anything: "... burns 4 cm per hour when they are the same height. How old is the room?" and
    # "They were the same height yesterday. When will the power return?" are not questions about when the candles meet.
    sentences = [x for x in re.split(r"[.?!]", t) if x.strip()]
    remainders = [_CANDLE_STMT.sub(" ", x) for x in sentences]
    asks = [i for i, x in enumerate(remainders)
            if re.search(r"\b(?:when|how long|after how many (?:hours|minutes|days))\b", x) and re.search(r"\bsame height\b|\bequal height\b|\bsame size\b|\bequally tall\b", x)]
    if len(asks) != 1:
        return None
    question = remainders[asks[0]]
    others = [x for i, x in enumerate(remainders) if i != asks[0]]
    # (a statement sentence that carries "when they are the same height" is such a candidate too: then the real question, "How old is the room?", is another sentence that asks)
    # (a request without a question word is a question too: "Find the age of the room.")
    if any(re.search(r"\b(?:when|how|what|why|who|where|which|will|would|find|determine|calculate|compute|give|state|name|tell|list|solve|show)\b|\bsame height\b|\bequal height\b", x) for x in others):
        return None
    # "the same height as ..." has to compare the two candles with each other: "as the table" is another object, whose height is not given
    for cm in re.finditer(r"\b(?:same|equal) height\s+(?:as|to|with)\b(.*)$", question):
        if not re.match(r"\s*(?:each other|one another|the other(?:\s+(?:candle|one))?)\s*$", cm.group(1)):
            return None                                              # ... and nothing more after it ("each other and the table" names a third thing)
    if re.search(r"\bhow (?:tall|high|old)\b|\bwhat (?:height|size)\b|\bhow much\b", question):
        return None
    a, ra, b, rb = Fraction(m1.group(1)), Fraction(m1.group(3)), Fraction(m2.group(1)), Fraction(m2.group(3))
    if ra <= 0 or rb <= 0 or ra == rb:
        return None
    tt = (a - b) / (ra - rb)
    if tt <= 0:
        return None
    height = a - ra * tt
    if height <= 0:
        return None                                              # one would burn out before they meet
    unit = m1.group(5)
    eq = "%s - %st = %s - %st" % (show(a), show(ra), show(b), show(rb))
    return Result("two_candles_equal", [tt], eq, "t = %ss: %s, so t = %s %ss (both candles are still %s %s tall)" % (unit, eq, show_exact(tt), unit, show_exact(height), m1.group(2)))


# ---------------------------------------------------------------------------------------------------------
# 52. parallel lines and a transversal: corresponding / alternate interior / alternate exterior angles are equal      (the generator's "A pair of alternate exterior angles measure ...")
# ---------------------------------------------------------------------------------------------------------
_TRANS_KIND = re.compile(r"\b(corresponding|alternate interior|alternate exterior)\s+angles\b")
_TRANS_OTHER = re.compile(r"\b(?:same[- ]side|consecutive|co-?interior|supplementary|complementary|adjacent|linear pair|straight line|add to|adds to|sum|total|together|triangle|"
                          r"difference|product|ratio|half|double|twice|bisect\w*|quadrilateral|cyclic|inscribed|circle|arc|chord|polygon|exterior angle of)\b")


def transversal_equal_angles(problem):
    t = clean(problem)
    if _CHANGES_EQUATION.search(t) or _TRANS_OTHER.search(t) or re.search(_SPELLED_ANY, re.sub(r"\btwo parallel lines\b", " ", t)):
        return None
    if not re.search(r"\bparallel lines\b", t) or not re.search(r"\btransversal\b", t):
        return None
    kinds = _TRANS_KIND.findall(t)
    if len(kinds) != 1:
        return None                                              # the equal pairs only; same-side interior angles ADD to 180 and decline
    ex = list(_OPPANG_EXPR.finditer(t))
    if len(ex) != 2:
        return None
    rest = t[:ex[0].start()] + " " + t[ex[0].end():ex[1].start()] + " " + t[ex[1].end():]
    if re.search(r"\d", rest):
        return None
    coefs = []
    for m in ex:
        a = Fraction(m.group(1)) if m.group(1) else Fraction(1)
        b = Fraction(m.group(3)) * (1 if m.group(2) == "+" else -1)
        coefs.append((a, b))
    (a1, b1), (a2, b2) = coefs
    if a1 == a2:
        return None
    x = (b2 - b1) / (a1 - a2)
    angle = a1 * x + b1
    if not (0 < angle <= 180):
        return None
    q = max(t.rfind("find"), t.rfind("what"), t.rfind("how"))
    if q == -1:
        return None
    tail = t[q:]
    asks_angle = bool(re.search(r"\bangles?\b", tail)) and not re.search(r"\bboth angles\b", tail)
    asks_x = bool(re.search(r"\bx\b", tail))
    if not (asks_angle or asks_x):
        return None
    vals = ([x] if asks_x else []) + ([angle] if asks_angle else [])
    eq = "%sx %s %s = %sx %s %s" % (show(a1), "+" if b1 >= 0 else "-", show(abs(b1)), show(a2), "+" if b2 >= 0 else "-", show(abs(b2)))
    return Result("transversal_equal_angles", vals, eq,
                  "%s angles are equal: %s, so x = %s and each angle is %s degrees" % (kinds[0], eq, show_exact(x), show_exact(angle)))


# ---------------------------------------------------------------------------------------------------------
# 53. a class ratio after more students join:   b k / (g k + n) = p / q      (the generator's "The ratio of boys to girls in a class is 3:8. After 4 more girls join, the ratio becomes 1:3.")
# ---------------------------------------------------------------------------------------------------------
_JOIN_RATIO = re.compile(r"\bratio of ([a-z]+) to ([a-z]+)(?: [a-z ]*?)? is (\d+)\s*:\s*(\d+)")
_JOIN_AFTER = re.compile(r"\bafter (\d+) more ([a-z]+) (?:join|joins|joined|arrive|arrives|arrived|enrol|enroll|enrolls|enrolled)\b")
_JOIN_NEW = re.compile(r"\b(?:the )?ratio (?:becomes|changes to|is then|is now|will be|then is)\s+(\d+)\s*:\s*(\d+)")
_JOIN_OTHER = re.compile(r"\b(?:leave|leaves|left|drop out|dropped out|transfer\w*|absent|twice|half|double|total of|altogether|together|each)\b|%|\$")


def class_ratio_after_join(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 5 or _CHANGES_EQUATION.search(t) or _JOIN_OTHER.search(t) or re.search(_SPELLED_ANY, t):
        return None
    rm, am, nm = _JOIN_RATIO.search(t), _JOIN_AFTER.search(t), _JOIN_NEW.search(t)
    if not rm or not am or not nm or len(re.findall(r"\bratio of\b", t)) != 1:
        return None                                              # one "ratio of X to Y", read in that order both times
    X, Y = rm.group(1), rm.group(2)
    b, g = Fraction(rm.group(3)), Fraction(rm.group(4))
    n, joined = Fraction(am.group(1)), am.group(2)
    p, q = Fraction(nm.group(1)), Fraction(nm.group(2))
    if X == Y or min(b, g, n, p, q) <= 0:
        return None
    # the newcomers join the group the sentence names
    if joined == Y:
        # b k / (g k + n) = p / q
        denom = b * q - g * p
        if denom == 0:
            return None
        k = n * p / denom
        eq = "%sk / (%sk + %s) = %s/%s" % (show(b), show(g), show(n), show(p), show(q))
    elif joined == X:
        # (b k + n) / (g k) = p / q
        denom = p * g - q * b
        if denom == 0:
            return None
        k = q * n / denom
        eq = "(%sk + %s) / %sk = %s/%s" % (show(b), show(n), show(g), show(p), show(q))
    else:
        return None
    B, G = b * k, g * k
    if k <= 0 or B.denominator != 1 or G.denominator != 1 or B <= 0 or G <= 0:
        return None                                              # the counts have to be positive whole numbers
    # the question asks for the ORIGINAL total
    # exactly ONE sentence asks "how many", and THAT sentence says originally / at first: "Originally there were some ... How many students are there now?" asks the total now,
    # and a second question ("How many are there now?") makes the problem ask two things
    asking = [x for x in re.split(r"[.?!]", t) if re.search(r"\bhow many\b", x)]
    if len(asking) != 1 or len(re.findall(r"\bhow many\b", t)) != 1 or not re.search(r"\b(?:originally|at first|to begin with|in the beginning)\b", asking[0]) or re.search(r"\b(?:now|currently|today|afterwards|after that|finally|at the end)\b", asking[0]):
        return None
    qm = re.search(r"\bhow many (?:of the )?([a-z]+)", asking[0])
    if not qm or qm.group(1) not in ("students", "pupils", "children", "people", "members", "kids", "learners"):
        return None                                              # the TOTAL at the start, not the boys or the girls, and not the total afterwards
    total = B + G
    return Result("class_ratio_after_join", [total], eq,
                  "%s, so k = %s: %s %s and %s %s at first, %s in all" % (eq, show_exact(k), show_exact(B), X, show_exact(G), Y, show_exact(total)))


# ---------------------------------------------------------------------------------------------------------
# 54. v = u + a t:   how long to go from u to v at acceleration a      (the generator's "Using v = u + at, how long does it take an object to go from 0 m/s to 30 m/s with acceleration 5 m/s²?")
# ---------------------------------------------------------------------------------------------------------
_KIN_FROM = re.compile(r"\bfrom\s+(\d+(?:\.\d+)?)\s*([a-z]+)/([a-z]+)\s+to\s+(\d+(?:\.\d+)?)\s*([a-z]+)/([a-z]+)")
_KIN_ACC = re.compile(r"\bacceleration(?: of)?\s+(\d+(?:\.\d+)?)\s*([a-z]+)/([a-z]+)(?:²|\^2)")
_KIN_TIME_NAME = {"s": "second", "h": "hour", "min": "minute", "hr": "hour"}


def kinematics_time(problem):
    problem = re.sub(r"\^\s*2\b", "²", problem)
    t = clean(problem)
    nums = digit_numbers(problem)
    if len(nums) != 3 or _CHANGES_EQUATION.search(t) or re.search(_SPELLED_ANY, t) or re.search(r"\b(?:deceleration|decelerat\w*|slows?|brakes?|braking|stops?|then)\b|%|\$", t):
        return None
    fm, am = _KIN_FROM.search(t), _KIN_ACC.search(t)
    if not fm or not am:
        return None
    u, v, a = Fraction(fm.group(1)), Fraction(fm.group(4)), Fraction(am.group(1))
    # one system of units: the speeds and the acceleration are all (distance)/(time) with (distance)/(time)^2
    if not (fm.group(2) == fm.group(5) == am.group(2) and fm.group(3) == fm.group(6) == am.group(3)):
        return None
    tname = _KIN_TIME_NAME.get(fm.group(3))
    if tname is None:
        return None
    # the question asks how long, in the time unit of the speeds
    qm = re.search(r"\bhow (?:long|many (seconds|hours|minutes)|much time)\b", t)
    if not qm or (qm.group(1) and {"seconds": "second", "hours": "hour", "minutes": "minute"}[qm.group(1)] != tname):
        return None
    if a <= 0:
        return None                                              # an acceleration of 0 never reaches a different speed
    tt = (v - u) / a
    if tt <= 0:
        return None
    eq = "%s + %st = %s" % (show(u), show(a), show(v))
    return Result("kinematics_time", [tt], eq, "%s, so t = (%s - %s) / %s = %s %s%s" % (eq, show(v), show(u), show(a), show_exact(tt), tname, "" if tt == 1 else "s"))


# ---------------------------------------------------------------------------------------------------------
# 55. pipes that fill and a drain that empties:   1/a + 1/b - 1/c per hour      (the generator's "Pipe A fills a pool in 4 hours, pipe B in 5 hours, and a drain empties it in 20 hours")
# ---------------------------------------------------------------------------------------------------------
_PIPE_IN = re.compile(r"\bin\s+(\d+(?:\.\d+)?)\s+(hours?|minutes?|days?)\b")
_PIPE_FILL_WORD = re.compile(r"\b(?:pipe|fills?|inlet|tap|faucet|hose)\b")
# what may stay in the "everything is open" statement once the phrase is taken out, and the words that hang another clause on the question
_PIPE_FILLER = {"if", "when", "with", "then", "together", "now", "at", "the", "same", "time", "once", "all", "both", "are", "is", "be"}
_PIPE_HANG_ON = {"if", "when", "while", "as", "with", "and", "also", "too", "but", "since", "because", "once", "after", "before", "until", "plus", "besides", "even", "still", "in", "through", "from", "into", "by"}
_PIPE_VESSEL = {"tank", "pool", "tub", "bathtub", "cistern", "basin", "reservoir", "barrel", "drum", "bucket", "vat", "trough", "pond", "container", "bath", "sink", "pot"}
_PIPE_ENDING = {"up", "it", "them", "the", "a", "an", "this", "that", "empty", "whole", "entire", "completely", "fully", "entirely", "one", "all", "swimming", "water", "storage", "big", "large", "small"}
_PIPE_ASK = {"how", "long", "does", "do", "did", "will", "would", "should", "can", "could", "it", "they", "them", "take", "takes", "to", "for", "the", "a", "an", "this", "that", "all", "up", "empty", "whole", "entire", "tank", "pool", "tub", "bathtub", "cistern", "basin", "reservoir", "barrel", "drum", "bucket", "vat", "trough", "pond", "container", "bath", "sink", "pot"}
_PIPE_DRAIN_WORD = re.compile(r"\b(?:drain|drains|empties|empty|leak\w*|outlet)\b")


def pipes_and_drain(problem):
    t = clean(problem)
    nums = digit_numbers(problem)
    occ = list(_PIPE_IN.finditer(t))
    if len(occ) < 3 or len(nums) != len(occ) or _CHANGES_EQUATION.search(t) or re.search(_SPELLED_ANY, re.sub(r"\ball three\b", " ", t)) or re.search(r"\b(?:then|after|alone|only|closed|shut|half|twice|%)\b|\$", t):
        return None
    if len({m.group(2).rstrip("s") for m in occ}) != 1:
        return None                                              # one unit of time
    fills, drains = [], []
    prev = 0
    for m in occ:
        seg = t[prev:m.start()]
        prev = m.end()
        is_drain, is_fill = bool(_PIPE_DRAIN_WORD.search(seg)), bool(_PIPE_FILL_WORD.search(seg))
        if is_drain == is_fill:
            return None                                          # a clause that says both, or neither, is not safe to read
        (drains if is_drain else fills).append(Fraction(m.group(1)))
    if not fills or not drains or min(fills + drains) <= 0:
        return None
    # the question: with everything open, how long to FILL the pool
    # everything open, THE DRAIN INCLUDED: "all three open", "all open", "with everything open", "the pipes and the drain open".  A bare "The pipes work together" /
    # "both" / "at the same time" does not open the drain (the two pipes alone are a different problem).
    # the three devices must be said to be OPEN (or running / working / flowing): "all three" alone is only a count ("All three are stopped", "all three hours", "I like all of them")
    devices = r"(?:all three|all of them|everything|(?:both |all )?(?:the )?(?:pipes|taps) and (?:the )?(?:drain|leak|outlet))"
    state = r"(?:open|opened|running|working|flowing)"
    if not (re.search(devices + r"\s+(?:(?:are|is|being|stay|stays|remain|remains)\s+)?(?:all\s+)?" + state + r"\b", t)
            or re.search(r"(?:^|[.?!]\s*|\bwith\s+)all " + state + r"\b(?=\s*(?:[,.;?!]|$|\b(?:how|what|then|and)\b))", t)):
        return None                                              # a bare "all open" starts the sentence (or follows "with") and ENDS there: "The pool, all open to swimmers, ..." is not it
    # ... and nothing in the problem may turn something off or negate it
    cue_phrase = re.compile(devices + r"\s+(?:(?:are|is|being|stay|stays|remain|remains)\s+)?(?:all\s+)?" + state + r"\b")
    for sent in re.split(r"[.?!]", t):
        if not sent.strip():
            continue
        times = list(_PIPE_IN.finditer(sent))
        if times:
            # the time clause has to END the sentence: "A drain empties it in 12 hours and is pinched." / "... and is full of leaves." say more about the device
            if sent[times[-1].end():].strip(" ,;"):
                return None
        else:
            # a sentence that gives no time is the "everything is open" statement or the question, and nothing more: a sentence that is neither is something else going on
            # ("Water also leaves through a crack." is another way out), and so is anything added to the statement ("... and water also leaves through a crack") or to the question
            # ("... if rain also falls in").  What is left of the statement once the open phrase is taken out may only be small filler words; the question may not hang a clause on
            # (no "if / when / while / and / also / as well" after "how long").
            lead = r"(?:\b(?:with|if|when|once)\s+)?"
            opened = re.sub(lead + cue_phrase.pattern, " ", sent)                       # the open phrase may sit in the question too: "... fill the pool with all three open?"
            opened = re.sub(r"(?:^|" + lead + r")\s*all " + state + r"\b", " ", opened)
            q = re.search(r"\bhow long\b", opened)
            if opened == sent and not q:
                return None                                      # it does not open the devices and asks nothing
            if set(re.findall(r"[a-z']+", opened[:q.start()] if q else opened)) - _PIPE_FILLER:
                return None
            if q and set(re.findall(r"[a-z']+", opened[q.start():])) & _PIPE_HANG_ON:
                return None
            if q:
                # once the question has named the thing being filled it has to END ("... fill the tank during a storm / under a downpour / amid the rain" is something else going on)
                fm = re.search(r"\bfill\b(.*)$", opened[q.start():], flags=re.S)
                if fm:
                    # ... and so does the way in: between "how long" and "fill" only the plain question words may stand ("How long does it take to fill", "How long will it take for the tank to fill"),
                    # not a storm named on the way ("How long does it take during a storm to fill the pool?", "How long, during a storm, does it take to fill the pool?")
                    if set(re.findall(r"[a-z']+", opened[q.start():q.start() + fm.start()])) - _PIPE_ASK:
                        return None
                    tail = re.findall(r"[a-z']+", fm.group(1))
                    named = [k for k, w in enumerate(tail) if w in _PIPE_VESSEL]
                    if (set(tail[named[0] + 1:]) if named else set(tail)) - _PIPE_ENDING:
                        return None
        if _PIPE_DRAIN_WORD.search(sent) and not _PIPE_IN.search(sent):
            # a sentence about the drain that is not the clause giving its time: it may only be the "everything is open" phrase itself, and nothing else about the drain may
            # remain once that phrase is taken out ("The drain is covered.", "The drain is pinched.", "All three are open and the drain is full of leaves.")
            if not cue_phrase.search(sent) or _PIPE_DRAIN_WORD.search(cue_phrase.sub(" ", sent)):
                return None
    if re.search(r"\b(?:not|no|never|neither|nor|except|without|off|stopped|stops?|broken|blocked|clogged|jammed|out of order|sealed|capped|plugged|stoppered|corked|locked|bolted|disabled|inactive|covered|but|however|although|though|yet|unless)\b|n't\b", t):
        return None                                              # "The pipes are all together" / "The lights are all on" say nothing about the drain
    if not re.search(r"\bhow long\b[^.?!]*\bfill\b", t) or re.search(r"\bhow long\b[^.?!]*\bempty\b", t):
        return None
    rate = sum((Fraction(1) / f for f in fills), Fraction(0)) - sum((Fraction(1) / d for d in drains), Fraction(0))
    if rate <= 0:
        return None                                              # the drain keeps up with the pipes: the pool never fills
    tt = 1 / rate
    unit = occ[0].group(2).rstrip("s")
    eq = " + ".join("1/%s" % show(f) for f in fills) + "".join(" - 1/%s" % show(d) for d in drains)
    return Result("pipes_and_drain", [tt], eq + " = " + show_exact(rate),
                  "%s = %s of the pool per %s, so it takes 1 / %s = %s %ss" % (eq, show_exact(rate), unit, show_exact(rate), show_exact(tt), unit))


# ---------------------------------------------------------------------------------------------------------
# 56. a percent spent, with money or fuel left:   x - p% x = left      (the generator's "Yara spent 75% of a paycheck on rent and had $280 left")
# ---------------------------------------------------------------------------------------------------------
_SPENT_AT_FIRST = r"(?: at first| originally| to begin with)?"
_SPENT_MONEY = re.compile(r"^[a-z]+ spent " + NUM + r"% of (?:a|the|his|her|their|my|our) ([a-z]+)(?: on [a-z]+)? and (?:had|has|have) \$" + NUM + r" left\. how much was the \2" + _SPENT_AT_FIRST + r"\?$")
_SPENT_FUEL = re.compile(r"^after (?:using|burning) " + NUM + r"% of the ([a-z]+) in (?:a|the) ([a-z]+), " + NUM + r" (?:liters?|litres?|gallons?) (?:remain|remains|remained|are left|were left)\. how much \2 was there" + _SPENT_AT_FIRST + r"\?$")


def percent_spent_left(problem):
    t = clean(problem).strip()
    if n_numbers(problem) != 2 or t.count("%") != 1:
        return None
    m = _SPENT_MONEY.match(t)
    if m:
        pct, left, what = fr(m.group(1)), fr(m.group(3)), "money"
    else:
        m = _SPENT_FUEL.match(t)
        if not m:
            return None
        pct, left, what = fr(m.group(1)), fr(m.group(4)), m.group(2)
    if not (0 < pct < 100) or left <= 0:
        return None
    x = left * 100 / (100 - pct)
    eq = "x - %s%% of x = %s" % (show(pct), show(left))
    return Result("percent_spent_left", [x], eq,
                  "%s%% was not spent, so x = %s / %s%% = %s" % (show_exact(100 - pct), show(left), show_exact(100 - pct), show_exact(x)))


# ---------------------------------------------------------------------------------------------------------
# 57. a price times a count, minus a coupon:   p n - c = paid      (the generator's "Notebooks cost $3.50 each. With a $3 coupon, Hiro paid $46.00")
# ---------------------------------------------------------------------------------------------------------
_COUPON = re.compile(r"^([a-z]+(?: [a-z]+){0,3}) cost \$" + NUM + r" each\. with a \$" + NUM + r" coupon, [a-z]+ paid \$" + NUM + r"\. how many \1 were bought\?$")


def price_minus_coupon(problem):
    t = clean(problem).strip()
    m = _COUPON.match(t)
    if not m or n_numbers(problem) != 3:
        return None
    price, coupon, paid = fr(m.group(2)), fr(m.group(3)), fr(m.group(4))
    if price <= 0 or coupon <= 0 or paid <= 0 or coupon > paid:
        return None
    n = (paid + coupon) / price
    if n.denominator != 1 or n <= 0:
        return None
    eq = "%sn - %s = %s" % (show(price), show(coupon), show(paid))
    return Result("price_minus_coupon", [n], eq, "%s, so %sn = %s and n = %s" % (eq, show(price), show(paid + coupon), show_exact(n)))


# ---------------------------------------------------------------------------------------------------------
# 58. complementary and supplementary angles:   x + (k x +- c) = 90 or 180      (the generator's "Two angles are complementary. One angle is 12 less than 5 times the other.")
# ---------------------------------------------------------------------------------------------------------
_COMPSUPP = re.compile(r"^two angles are (complementary|supplementary)\. one angle is (?:" + NUM + r" (more|less) than )?" + NUM +
                       r" times the other(?: angle)?\. (?:find (?:both|the two) angles\.?|what are (?:both|the two) angles\?)$")


def complementary_supplementary(problem):
    t = clean(problem).strip()
    m = _COMPSUPP.match(t)
    if not m:
        return None
    if n_numbers(problem) != (2 if m.group(2) else 1):
        return None
    total = Fraction(90 if m.group(1) == "complementary" else 180)
    c = (fr(m.group(2)) * (1 if m.group(3) == "more" else -1)) if m.group(2) else Fraction(0)
    k = fr(m.group(4))
    if k <= 0:
        return None
    x = (total - c) / (k + 1)
    other = k * x + c
    if x <= 0 or other <= 0:
        return None
    eq = "x + (%sx %s %s) = %s" % (show(k), "-" if c < 0 else "+", show(abs(c)), show(total))
    return Result("complementary_supplementary", [x, other], eq,
                  "%s, so %sx = %s and x = %s; the other angle is %s degrees" % (eq, show_exact(k + 1), show(total - c), show_exact(x), show_exact(other)))


FAMILIES = [sum_difference, age_sum, consecutive, work_together, percent_change, proportion, two_solution_mix, two_rate_interest,
            two_purchases, price_blend, savings_equal, average_needed, heads_and_feet,
            opposite_directions, catch_up, polygon_angle_sum,
            toward_each_other, consecutive_product, most_you_can_buy,
            still_water_current, ratio_split, three_numbers, catch_up_clock, periodic_growth,
            fixed_plus_rate, two_changing_equal, add_to_blend,
            two_scores, two_discounts, triangle_ratio,
            two_prices_known_count, drain_or_fill, percent_of_count,
            percent_change_between, ages_later_multiple, shared_fixed_cost,
            two_rates_one_pile, least_for_profit,
            two_priced_items, plan_with_included, most_that_fits,
            line_from_two_points, election_margin, wind_same_time,
            base_plus_extra_over_time, distance_speed_time,
            pages_per_day, opposite_angles_equal, rectangle_from_perimeter_area,
            temperature_whole_hours, two_candles_equal, transversal_equal_angles,
            class_ratio_after_join, kinematics_time, pipes_and_drain,
            percent_spent_left, price_minus_coupon, complementary_supplementary]


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
