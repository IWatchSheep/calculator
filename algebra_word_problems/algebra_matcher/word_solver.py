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
    foll_s = _HEAD_START.sub(" ", foll_s)
    F, Ld = _subject_tokens(foll_s), _subject_tokens(lead_s)
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


FAMILIES = [sum_difference, age_sum, consecutive, work_together, percent_change, proportion, two_solution_mix, two_rate_interest,
            two_purchases, price_blend, savings_equal, average_needed, heads_and_feet,
            opposite_directions, catch_up, polygon_angle_sum]


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
