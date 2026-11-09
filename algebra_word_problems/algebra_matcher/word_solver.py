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


def _singular(phrase):
    return " ".join(re.sub(r"(?<=[a-z])s$", "", w) if len(w) > 3 else w for w in phrase.split())


def two_purchases(problem):
    t = clean(problem).replace("$", "")
    found = list(_PURCHASE.finditer(t))
    if len(found) != 2 or re.search(r"\bsuch\b", t):
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
    return Result("two_purchases", [x, y], "%s;  %s" % (eq1, eq2),
                  "x = price of one %s, y = price of one %s: %s and %s, so x = %s and y = %s" % (
                      n1, n2, eq1, eq2, show_exact(x), show_exact(y)))


FAMILIES = [sum_difference, age_sum, consecutive, work_together, percent_change, proportion, two_solution_mix, two_rate_interest,
            two_purchases]


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
