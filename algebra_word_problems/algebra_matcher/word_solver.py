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

import archive_families as AF
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


# Find the second person's time alone from the together time and the first person's time alone.
# x = t * a / (a - t). The first name is the known alone time. The second name is the one asked.
_PARTNER_ALONE_FROM_TOGETHER = re.compile(
    r"working together, "
    r"(?P<first>[a-z]+) and (?P<second>[a-z]+) "
    r"can finish a job in "
    r"(?P<t>\d+(?:\.\d+)?) hours?\. "
    r"(?P<known_name>[a-z]+) alone takes "
    r"(?P<a>\d+(?:\.\d+)?) hours?\. "
    r"how long would (?P<asked_name>[a-z]+) "
    r"take alone\?")


def partner_alone_from_together(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PARTNER_ALONE_FROM_TOGETHER.fullmatch(text)
    if match is None:
        return None
    if match.group("known_name") != match.group("first") or match.group("asked_name") != match.group("second"):
        return None
    if match.group("first") == match.group("second"):
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(n[1] for n in numbers):
        return None
    t = Fraction(match.group("t"))
    a = Fraction(match.group("a"))
    if [n[0] for n in numbers] != [t, a]:
        return None
    if t <= 0 or a <= t:
        return None
    x = t * a / (a - t)
    if x <= 0:
        return None
    if t / a + t / x != 1:
        return None
    eq = "%s/%s + %s/x = 1" % (show(t), show(a), show(t))
    return Result("partner_alone_from_together", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


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
# two-leg average speed: drove h1 hours at v1, then t hours at v2, average A.   t = h1 (A - v1) / (v2 - A)
# "Kofi drove 1 hour at 30 mph and then some hours at 55 mph. The average speed for the whole trip was 50 mph. How long was the second part?"
# ---------------------------------------------------------------------------------------------------------
_AVERAGE_SPEED_TWO_LEG = re.compile(
    r"(?P<name>[a-z]+) drove "
    r"(?P<h1>\d+(?:\.\d+)?) hours? at "
    r"(?P<v1>\d+(?:\.\d+)?) mph "
    r"and then some hours at "
    r"(?P<v2>\d+(?:\.\d+)?) mph\. "
    r"the average speed for the whole trip was "
    r"(?P<avg>\d+(?:\.\d+)?) mph\. "
    r"how long was the second part\?")


def average_speed_two_leg_unknown_time(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _AVERAGE_SPEED_TWO_LEG.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4:
        return None
    # sentence order: first hours, first speed, second speed, whole-trip average
    h1 = Fraction(match.group("h1"))
    v1 = Fraction(match.group("v1"))
    v2 = Fraction(match.group("v2"))
    avg = Fraction(match.group("avg"))
    if [n[0] for n in numbers] != [h1, v1, v2, avg]:
        return None
    if h1 <= 0 or v1 <= 0 or v2 <= 0 or avg <= 0:
        return None
    if v2 == avg:
        return None
    t = h1 * (avg - v1) / (v2 - avg)
    if t <= 0:
        return None
    if (v1 * h1 + v2 * t) / (h1 + t) != avg:
        return None
    eq = "(%s×%s + %st)/(%s + t) = %s" % (show(v1), show(h1), show(v2), show(h1), show(avg))
    return Result("average_speed_two_leg_unknown_time", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


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
                  "%s, so %sx = %s and x = %s; the angle described is %s degrees" % (eq, show_exact(k + 1), show(total - c), show_exact(x), show_exact(other)))


# Course grade: (c/100)*w + (e/100)*f = g. The two percents add to 100. f is the final exam score.
_COURSE_GRADE_FINAL_EXAM = re.compile(
    r"a course grade is "
    r"(?P<c>\d+(?:\.\d+)?)% coursework and "
    r"(?P<e>\d+(?:\.\d+)?)% final exam\. "
    r"(?P<name>[a-z]+) has a coursework average of "
    r"(?P<w>\d+(?:\.\d+)?)\. "
    r"what final exam score gives an overall grade of "
    r"(?P<g>\d+(?:\.\d+)?)\?")


def course_grade_final_exam(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _COURSE_GRADE_FINAL_EXAM.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(n[1] for n in numbers):
        return None
    c = Fraction(match.group("c"))
    e = Fraction(match.group("e"))
    w = Fraction(match.group("w"))
    g = Fraction(match.group("g"))
    if [n[0] for n in numbers] != [c, e, w, g]:
        return None
    if c <= 0 or e <= 0 or w <= 0 or g <= 0 or c + e != 100:
        return None
    f = (g - (c / 100) * w) / (e / 100)
    if f <= 0:
        return None
    if (c / 100) * w + (e / 100) * f != g:
        return None
    eq = "(%s/100)(%s) + (%s/100)f = %s" % (show(c), show(w), show(e), show(g))
    return Result("course_grade_final_exam", [f], eq, "%s, so f = %s" % (eq, show_exact(f)))


# Round trip to a lake: d/v1 + d/v2 = t, so d = t * v1 * v2 / (v1 + v2).
_ROUND_TRIP_LAKE_DISTANCE = re.compile(
    r"(?P<name>[a-z]+) drove to a lake at "
    r"(?P<v1>\d+(?:\.\d+)?) mph and returned on the same road at "
    r"(?P<v2>\d+(?:\.\d+)?) mph\. "
    r"the round trip took "
    r"(?P<t>\d+(?:\.\d+)?) hours?\. "
    r"how far is the lake\?")


def round_trip_lake_distance(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _ROUND_TRIP_LAKE_DISTANCE.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(n[1] for n in numbers):
        return None
    v1 = Fraction(match.group("v1"))
    v2 = Fraction(match.group("v2"))
    t = Fraction(match.group("t"))
    if [n[0] for n in numbers] != [v1, v2, t]:
        return None
    if v1 <= 0 or v2 <= 0 or t <= 0:
        return None
    d = t * v1 * v2 / (v1 + v2)
    if d <= 0:
        return None
    if d / v1 + d / v2 != t:
        return None
    eq = "d/%s + d/%s = %s" % (show(v1), show(v2), show(t))
    return Result("round_trip_lake_distance", [d], eq,
                  "%s drove to a lake at %s mph and returned at %s mph. The round trip took %s hours, so the lake is %s miles away."
                  % (match.group("name"), show(v1), show(v2), show(t), show_exact(d)))


# Three painters: 1/t = 1/a + 1/b + 1/c. The three alone times are in the order the names are written.
_THREE_PAINTERS_TOGETHER = re.compile(
    r"(?P<name1>[a-z]+), "
    r"(?P<name2>[a-z]+), and "
    r"(?P<name3>[a-z]+) "
    r"can each paint a room alone in "
    r"(?P<a>\d+(?:\.\d+)?), "
    r"(?P<b>\d+(?:\.\d+)?), and "
    r"(?P<c>\d+(?:\.\d+)?) hours\. "
    r"how long will it take all three together\?")


def three_painters_together(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _THREE_PAINTERS_TOGETHER.fullmatch(text)
    if match is None:
        return None
    names = [match.group("name1"), match.group("name2"), match.group("name3")]
    if len(set(names)) != 3:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(n[1] for n in numbers):
        return None
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    c = Fraction(match.group("c"))
    if [n[0] for n in numbers] != [a, b, c]:
        return None
    if a <= 0 or b <= 0 or c <= 0:
        return None
    t = 1 / (1 / a + 1 / b + 1 / c)
    if t <= 0:
        return None
    if 1 / t != 1 / a + 1 / b + 1 / c:
        return None
    eq = "t/%s + t/%s + t/%s = 1" % (show(a), show(b), show(c))
    return Result("three_painters_together", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


# Seesaw: w1 * d1 = w2 * d. The numbers are first weight, first distance, second weight.
_SEESAW_BALANCE_DISTANCE = re.compile(
    "on a seesaw, weight \u00d7 distance from the pivot "
    r"must be equal on both sides\. "
    r"(?P<first>[a-z]+) "
    r"\((?P<w1>\d+(?:\.\d+)?) kg\) "
    r"sits (?P<d1>\d+(?:\.\d+)?) m from the pivot\. "
    r"how far from the pivot must "
    r"(?P<second>[a-z]+) "
    r"\((?P<w2>\d+(?:\.\d+)?) kg\) "
    r"sit to balance\?")


def seesaw_balance_distance(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SEESAW_BALANCE_DISTANCE.fullmatch(text)
    if match is None:
        return None
    if match.group("first") == match.group("second"):
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(n[1] for n in numbers):
        return None
    w1 = Fraction(match.group("w1"))
    d1 = Fraction(match.group("d1"))
    w2 = Fraction(match.group("w2"))
    if [n[0] for n in numbers] != [w1, d1, w2]:
        return None
    if w1 <= 0 or d1 <= 0 or w2 <= 0:
        return None
    d = w1 * d1 / w2
    if d <= 0:
        return None
    if w1 * d1 != w2 * d:
        return None
    eq = "%s \u00d7 %s = %sd" % (show(w1), show(d1), show(w2))
    return Result("seesaw_balance_distance", [d], eq, "%s, so d = %s" % (eq, show_exact(d)))


# More invested at a second rate so the combined money earns an overall rate.
# x = P * (r3 - r1) / (r2 - r3). Rates are the percent numbers, not decimals.
_MORE_INVESTED_FOR_OVERALL_RATE = re.compile(
    r"(?P<name>[a-z]+) has "
    r"\$(?P<P>\d+(?:\.\d+)?) invested at "
    r"(?P<r1>\d+(?:\.\d+)?)%\. "
    r"how much more must be invested at "
    r"(?P<r2>\d+(?:\.\d+)?)% "
    r"so that the total earns "
    r"(?P<r3>\d+(?:\.\d+)?)% overall\?")


def more_invested_for_overall_rate(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _MORE_INVESTED_FOR_OVERALL_RATE.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or not numbers[0][1] or any(n[1] for n in numbers[1:]):
        return None
    P = Fraction(match.group("P"))
    r1 = Fraction(match.group("r1"))
    r2 = Fraction(match.group("r2"))
    r3 = Fraction(match.group("r3"))
    if [n[0] for n in numbers] != [P, r1, r2, r3]:
        return None
    if P <= 0 or r1 <= 0 or r2 <= 0 or r3 <= 0 or r2 == r3:
        return None
    x = P * (r3 - r1) / (r2 - r3)
    if x <= 0:
        return None
    if (r1 / 100) * P + (r2 / 100) * x != (r3 / 100) * (P + x):
        return None
    eq = "(%s/100)(%s) + (%s/100)x = (%s/100)(%s + x)" % (show(r1), show(P), show(r2), show(r3), show(P))
    return Result("more_invested_for_overall_rate", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


# Overtime at time-and-a-half. The only answer is the overtime hours.
# regular * wage + h * (3/2) * wage = pay.
_OVERTIME_HOURS_TIME_AND_A_HALF = re.compile(
    r"(?P<name>[a-z]+) earns "
    r"\$(?P<wage>\d+(?:\.\d+)?)/hour "
    r"for the first (?P<regular>\d+(?:\.\d+)?) hours "
    r"and time-and-a-half after that\. "
    r"last week's pay was "
    r"\$(?P<pay>\d+(?:\.\d+)?)\. "
    r"how many overtime hours were worked\?")


def overtime_hours_time_and_a_half(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _OVERTIME_HOURS_TIME_AND_A_HALF.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [True, False, True]:
        return None
    wage = Fraction(match.group("wage"))
    regular = Fraction(match.group("regular"))
    pay = Fraction(match.group("pay"))
    if [n[0] for n in numbers] != [wage, regular, pay]:
        return None
    if wage <= 0 or regular <= 0 or pay <= regular * wage:
        return None
    half = Fraction(3, 2)
    overtime = (pay - regular * wage) / (wage * half)
    if overtime <= 0 or overtime.denominator != 1:
        return None
    if regular * wage + overtime * half * wage != pay:
        return None
    eq = "%s(%s) + %sh = %s" % (show(regular), show(wage), show(wage * half), show(pay))
    return Result("overtime_hours_time_and_a_half", [overtime], eq, "%s, so h = %s" % (eq, show_exact(overtime)))


# Walk then bus. The only answer is the walking time.
# walk * t + bus * (T - t) = D.
_WALK_THEN_BUS_UNKNOWN_TIME = re.compile(
    r"(?P<name>[a-z]+) walked at "
    r"(?P<walk>\d+(?:\.\d+)?) km/h "
    r"and then rode a bus at "
    r"(?P<bus>\d+(?:\.\d+)?) km/h\. "
    r"the whole trip was "
    r"(?P<distance>\d+(?:\.\d+)?) km "
    r"and took (?P<total>\d+(?:\.\d+)?) hours\. "
    r"how long was the walk\?")


def walk_then_bus_unknown_time(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WALK_THEN_BUS_UNKNOWN_TIME.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [n[1] for n in numbers] != [False, False, False, False]:
        return None
    walk = Fraction(match.group("walk"))
    bus = Fraction(match.group("bus"))
    distance = Fraction(match.group("distance"))
    total = Fraction(match.group("total"))
    if [n[0] for n in numbers] != [walk, bus, distance, total]:
        return None
    if walk <= 0 or bus <= walk or total <= 0 or distance <= 0:
        return None
    walking_time = (bus * total - distance) / (bus - walk)
    if walking_time <= 0 or walking_time >= total:
        return None
    bus_time = total - walking_time
    if bus_time <= 0:
        return None
    if walk * walking_time + bus * bus_time != distance:
        return None
    eq = "%st + %s(%s - t) = %s" % (show(walk), show(bus), show(total), show(distance))
    return Result("walk_then_bus_unknown_time", [walking_time], eq, "%s, so t = %s" % (eq, show_exact(walking_time)))


# Two successive fraction spends. The only answer is the starting amount.
# x * (1 - a/b) * (1 - c/d) = leftover.
_LEFTOVER_AFTER_TWO_FRACTION_SPENDS = re.compile(
    r"(?P<name>[a-z]+) spent "
    r"(?P<a>\d+)/(?P<b>\d+) "
    r"of their money on a game "
    r"and then "
    r"(?P<c>\d+)/(?P<d>\d+) "
    r"of what was left on lunch, "
    r"leaving \$(?P<leftover>\d+(?:\.\d+)?)\. "
    r"how much did they start with\?")


def leftover_after_two_fraction_spends(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LEFTOVER_AFTER_TWO_FRACTION_SPENDS.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 5 or [n[1] for n in numbers] != [False, False, False, False, True]:
        return None
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    c = Fraction(match.group("c"))
    d = Fraction(match.group("d"))
    leftover = Fraction(match.group("leftover"))
    if [n[0] for n in numbers] != [a, b, c, d, leftover]:
        return None
    if b <= 0 or d <= 0 or leftover <= 0:
        return None
    first_fraction = a / b
    second_fraction = c / d
    if not (0 < first_fraction < 1) or not (0 < second_fraction < 1):
        return None
    remaining_fraction = (1 - first_fraction) * (1 - second_fraction)
    if remaining_fraction <= 0:
        return None
    starting_money = leftover / remaining_fraction
    if starting_money <= 0:
        return None
    if starting_money * (1 - first_fraction) * (1 - second_fraction) != leftover:
        return None
    eq = "x(1 - %s/%s)(1 - %s/%s) = %s" % (show(a), show(b), show(c), show(d), show(leftover))
    return Result("leftover_after_two_fraction_spends", [starting_money], eq, "%s, so x = %s" % (eq, show_exact(starting_money)))


# One person has m more than k times as many stamps as the other.
# x + (k*x + m) = total. Answers are x, then k*x + m.
_MORE_THAN_TIMES_STAMPS = re.compile(
    r"(?P<more_person>[a-z]+) has "
    r"(?P<m>\d+) more than "
    r"(?P<k>\d+) times as many stamps as "
    r"(?P<less_person>[a-z]+)\. "
    r"together they have "
    r"(?P<total>\d+) stamps\. "
    r"how many does each have\?")


def more_than_times_stamps(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _MORE_THAN_TIMES_STAMPS.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [False, False, False]:
        return None
    m = Fraction(match.group("m"))
    k = Fraction(match.group("k"))
    total = Fraction(match.group("total"))
    if [n[0] for n in numbers] != [m, k, total]:
        return None
    if m < 0 or k < 2 or total <= m:
        return None
    smaller = (total - m) / (k + 1)
    larger = k * smaller + m
    if smaller <= 0 or larger <= 0 or smaller.denominator != 1 or larger.denominator != 1:
        return None
    if smaller + larger != total or larger != k * smaller + m:
        return None
    eq = "x + (%s*x + %s) = %s" % (show(k), show(m), show(total))
    return Result(
        "more_than_times_stamps",
        [smaller, larger],
        eq,
        "%s, so x = %s and %s*x + %s = %s" % (eq, show_exact(smaller), show(k), show(m), show_exact(larger))
    )


# Giver has k times the receiver. After a gift they are equal.
# k*x - g = x + g. Answers are x, then k*x.
_GIVE_UNTIL_EQUAL_MONEY = re.compile(
    r"(?P<giver>[a-z]+) has "
    r"(?P<k>\d+) times as much money as "
    r"(?P<receiver>[a-z]+)\. "
    r"after (?P=giver) gives (?P=receiver) "
    r"\$(?P<gift>\d+(?:\.\d+)?), "
    r"they have the same amount\. "
    r"how much did each have at first\?")


def give_until_equal_money(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _GIVE_UNTIL_EQUAL_MONEY.fullmatch(text)
    if match is None:
        return None
    if match.group("giver") == match.group("receiver"):
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [n[1] for n in numbers] != [False, True]:
        return None
    k = Fraction(match.group("k"))
    gift = Fraction(match.group("gift"))
    if [n[0] for n in numbers] != [k, gift]:
        return None
    if k.denominator != 1 or k < 2 or gift <= 0:
        return None
    smaller = (2 * gift) / (k - 1)
    larger = k * smaller
    if smaller <= 0 or larger <= 0:
        return None
    giver_after = larger - gift
    receiver_after = smaller + gift
    if giver_after <= 0 or receiver_after <= 0 or giver_after != receiver_after:
        return None
    if larger != k * smaller:
        return None
    eq = "%s*x - %s = x + %s" % (show(k), show(gift), show(gift))
    return Result(
        "give_until_equal_money",
        [smaller, larger],
        eq,
        "%s, so x = %s and %s*x = %s" % (eq, show_exact(smaller), show(k), show_exact(larger))
    )


# Three heirs: k times the base, and m more than the base.
# k*x + x + (x + m) = total. Answers are k*x, x, x + m.
_ESTATE_THREE_HEIRS_TIMES_AND_MORE = re.compile(
    r"an estate of "
    r"\$(?P<total>\d+(?:\.\d+)?) "
    r"is split among three heirs\. "
    r"(?P<times_person>[a-z]+) gets "
    r"(?P<k>\d+) times as much as "
    r"(?P<base_person>[a-z]+), "
    r"and (?P<extra_person>[a-z]+) gets "
    r"\$(?P<m>\d+(?:\.\d+)?) "
    r"more than (?P=base_person)\. "
    r"how much does each receive\?")


def estate_three_heirs_times_and_more(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _ESTATE_THREE_HEIRS_TIMES_AND_MORE.fullmatch(text)
    if match is None:
        return None
    times_person = match.group("times_person")
    base_person = match.group("base_person")
    extra_person = match.group("extra_person")
    if len({times_person, base_person, extra_person}) != 3:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [True, False, True]:
        return None
    total = Fraction(match.group("total"))
    k = Fraction(match.group("k"))
    m = Fraction(match.group("m"))
    if [n[0] for n in numbers] != [total, k, m]:
        return None
    if k.denominator != 1 or k < 2 or m <= 0 or total <= m:
        return None
    base_share = (total - m) / (k + 2)
    times_share = k * base_share
    extra_share = base_share + m
    if base_share <= 0 or times_share <= 0 or extra_share <= 0:
        return None
    if times_share != k * base_share or extra_share != base_share + m:
        return None
    if times_share + base_share + extra_share != total:
        return None
    eq = "%s*x + x + (x + %s) = %s" % (show(k), show(m), show(total))
    return Result(
        "estate_three_heirs_times_and_more",
        [times_share, base_share, extra_share],
        eq,
        "%s, so x = %s, %s*x = %s, and x + %s = %s" % (
            eq, show_exact(base_share), show(k), show_exact(times_share), show(m), show_exact(extra_share)
        )
    )


# After a gift the marble ratio changes.
# (a*k - g)/(b*k + g) = c/d. Answers are a*k, b*k.
_MARBLES_GIVEN_RATIO_CHANGES = re.compile(
    r"the ratio of "
    r"(?P<giver>[a-z]+)'s marbles to "
    r"(?P<receiver>[a-z]+)'s is "
    r"(?P<a>\d+):(?P<b>\d+)\. "
    r"after (?P=giver) gives (?P=receiver) "
    r"(?P<gift>\d+) marbles, "
    r"the ratio is "
    r"(?P<c>\d+):(?P<d>\d+)\. "
    r"how many did each have at first\?")


def marbles_given_ratio_changes(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _MARBLES_GIVEN_RATIO_CHANGES.fullmatch(text)
    if match is None:
        return None
    if match.group("giver") == match.group("receiver"):
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 5 or [n[1] for n in numbers] != [False, False, False, False, False]:
        return None
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    gift = Fraction(match.group("gift"))
    c = Fraction(match.group("c"))
    d = Fraction(match.group("d"))
    if [n[0] for n in numbers] != [a, b, gift, c, d]:
        return None
    if a <= 0 or b <= 0 or c <= 0 or d <= 0 or gift <= 0:
        return None
    denominator = d * a - c * b
    if denominator <= 0:
        return None
    scale = gift * (c + d) / denominator
    if scale <= 0:
        return None
    first = a * scale
    second = b * scale
    if first <= 0 or second <= 0 or first.denominator != 1 or second.denominator != 1:
        return None
    first_after = first - gift
    second_after = second + gift
    if first_after <= 0 or second_after <= 0:
        return None
    if d * first_after != c * second_after or b * first != a * second:
        return None
    if first_after + second_after != first + second:
        return None
    eq = "(%s*k - %s)/(%s*k + %s) = %s/%s" % (show(a), show(gift), show(b), show(gift), show(c), show(d))
    return Result(
        "marbles_given_ratio_changes",
        [first, second],
        eq,
        "%s, so k = %s, %s*k = %s, and %s*k = %s" % (
            eq, show_exact(scale), show(a), show_exact(first), show(b), show_exact(second)
        )
    )


# Profit shared in the same ratio as the investment.
# a*k + b*k = profit. Answers are a*k, b*k.
_PROFIT_SHARED_IN_INVESTMENT_RATIO = re.compile(
    r"(?P<first_person>[a-z]+) and "
    r"(?P<second_person>[a-z]+) "
    r"invested in a business in the ratio "
    r"(?P<a>\d+):(?P<b>\d+)\. "
    r"they share a profit of "
    r"\$(?P<profit>\d+(?:\.\d+)?) "
    r"in the same ratio\. "
    r"how much does each get\?")


def profit_shared_in_investment_ratio(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PROFIT_SHARED_IN_INVESTMENT_RATIO.fullmatch(text)
    if match is None:
        return None
    if match.group("first_person") == match.group("second_person"):
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [False, False, True]:
        return None
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    profit = Fraction(match.group("profit"))
    if [n[0] for n in numbers] != [a, b, profit]:
        return None
    if a <= 0 or b <= 0 or profit <= 0:
        return None
    share_unit = profit / (a + b)
    first_share = a * share_unit
    second_share = b * share_unit
    if first_share <= 0 or second_share <= 0:
        return None
    if first_share + second_share != profit or b * first_share != a * second_share:
        return None
    eq = "%s*k + %s*k = %s" % (show(a), show(b), show(profit))
    return Result(
        "profit_shared_in_investment_ratio",
        [first_share, second_share],
        eq,
        "%s, so k = %s, %s*k = %s, and %s*k = %s" % (
            eq, show_exact(share_unit), show(a), show_exact(first_share), show(b), show_exact(second_share)
        )
    )


# A is k times as old as B. In y years their ages sum to S.
# x = (S - 2y)/(k + 1). Answers are x, k*x (younger, then older).
_TIMES_AS_OLD_FUTURE_SUM = re.compile(
    r"(?P<older_person>[a-z]+) is "
    r"(?P<k>\d+) times as old as "
    r"(?P<younger_person>[a-z]+)\. "
    r"in (?P<years>\d+) years, "
    r"the sum of their ages will be "
    r"(?P<total>\d+)\. "
    r"how old is each now\?")


def times_as_old_future_sum(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TIMES_AS_OLD_FUTURE_SUM.fullmatch(text)
    if match is None:
        return None
    if match.group("older_person") == match.group("younger_person"):
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [False, False, False]:
        return None
    k = Fraction(match.group("k"))
    years = Fraction(match.group("years"))
    total = Fraction(match.group("total"))
    if [n[0] for n in numbers] != [k, years, total]:
        return None
    if k <= 1 or years < 0 or total <= 0:
        return None
    younger_now = (total - 2 * years) / (k + 1)
    older_now = k * younger_now
    if younger_now <= 0 or older_now <= 0:
        return None
    if older_now != k * younger_now:
        return None
    if younger_now + years + older_now + years != total:
        return None
    eq = "(x + %s) + (%s*x + %s) = %s" % (show(years), show(k), show(years), show(total))
    return Result(
        "times_as_old_future_sum",
        [younger_now, older_now],
        eq,
        "%s, so x = %s and %s*x = %s" % (eq, show_exact(younger_now), show(k), show_exact(older_now))
    )


# Read a/b of a book, then c/d of the remainder. L pages left.
# x * (1 - a/b) * (1 - c/d) = L.
_LEFTOVER_PAGES_AFTER_TWO_READS = re.compile(
    r"(?P<name>[a-z]+) read "
    r"(?P<a>\d+)/(?P<b>\d+) "
    r"of a book on monday and "
    r"(?P<c>\d+)/(?P<d>\d+) "
    r"of the remaining pages on tuesday\. "
    r"(?P<leftover>\d+) pages are left\. "
    r"how many pages does the book have\?")


def leftover_pages_after_two_reads(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LEFTOVER_PAGES_AFTER_TWO_READS.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 5 or [n[1] for n in numbers] != [False, False, False, False, False]:
        return None
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    c = Fraction(match.group("c"))
    d = Fraction(match.group("d"))
    leftover = Fraction(match.group("leftover"))
    if [n[0] for n in numbers] != [a, b, c, d, leftover]:
        return None
    if b <= 0 or d <= 0:
        return None
    first_fraction = a / b
    second_fraction = c / d
    if not (0 < first_fraction < 1) or not (0 < second_fraction < 1) or leftover <= 0:
        return None
    remaining_fraction = (1 - first_fraction) * (1 - second_fraction)
    if remaining_fraction <= 0:
        return None
    total_pages = leftover / remaining_fraction
    if total_pages <= 0:
        return None
    if total_pages * remaining_fraction != leftover:
        return None
    eq = "x(1 - %s/%s)(1 - %s/%s) = %s" % (show(a), show(b), show(c), show(d), show(leftover))
    return Result(
        "leftover_pages_after_two_reads",
        [total_pages],
        eq,
        "%s, so x = %s" % (eq, show_exact(total_pages))
    )


# Start with A, save R a week, fewest whole weeks so A + R*w >= T.
_FEWEST_WEEKS_TO_HAVE_AT_LEAST = re.compile(
    r"(?P<name>[a-z]+) has "
    r"\$(?P<start>\d+(?:\.\d+)?) "
    r"and saves "
    r"\$(?P<rate>\d+(?:\.\d+)?) a week\. "
    r"what is the fewest weeks needed "
    r"to have at least "
    r"\$(?P<target>\d+(?:\.\d+)?)\?")


def fewest_weeks_to_have_at_least(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _FEWEST_WEEKS_TO_HAVE_AT_LEAST.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [True, True, True]:
        return None
    start = Fraction(match.group("start"))
    rate = Fraction(match.group("rate"))
    target = Fraction(match.group("target"))
    if [n[0] for n in numbers] != [start, rate, target]:
        return None
    if rate <= 0 or start >= target:
        return None
    remaining = target - start
    if remaining <= 0:
        return None
    exact_weeks = remaining / rate
    if exact_weeks <= 0:
        return None
    weeks = (exact_weeks.numerator + exact_weeks.denominator - 1) // exact_weeks.denominator
    if weeks <= 0:
        return None
    if start + rate * weeks < target:
        return None
    if start + rate * (weeks - 1) >= target:
        return None
    eq = "%s + %s*w >= %s" % (show(start), show(rate), show(target))
    return Result(
        "fewest_weeks_to_have_at_least",
        [Fraction(weeks)],
        eq,
        "%s, so the fewest whole weeks is %s" % (eq, show_exact(Fraction(weeks)))
    )


# Bowling: per-game rate, then shoe rental, then amount spent.
# F + R*n = S. Answer is n.
_BOWLING_GAMES_PLUS_SHOE_RENTAL = re.compile(
    r"bowling costs "
    r"\$(?P<rate>\d+(?:\.\d+)?) "
    r"per game plus "
    r"\$(?P<rental>\d+(?:\.\d+)?) "
    r"for shoe rental\. "
    r"(?P<name>[a-z]+) spent "
    r"\$(?P<spent>\d+(?:\.\d+)?)\. "
    r"how many games were bowled\?")


def bowling_games_plus_shoe_rental(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BOWLING_GAMES_PLUS_SHOE_RENTAL.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [True, True, True]:
        return None
    rate = Fraction(match.group("rate"))
    rental = Fraction(match.group("rental"))
    spent = Fraction(match.group("spent"))
    if [n[0] for n in numbers] != [rate, rental, spent]:
        return None
    if rate <= 0 or rental < 0 or spent <= rental:
        return None
    games = (spent - rental) / rate
    if games <= 0 or games.denominator != 1:
        return None
    if rental + rate * games != spent:
        return None
    eq = "%s + %s*n = %s" % (show(rental), show(rate), show(spent))
    return Result(
        "bowling_games_plus_shoe_rental",
        [games],
        eq,
        "%s, so n = %s" % (eq, show_exact(games))
    )


# Every question answered: c + w = N, p*c - q*w = S.
# Answers are c, w.
_TEST_CORRECT_AND_WRONG_PENALTY = re.compile(
    r"a test has "
    r"(?P<total>\d+) questions\. "
    r"each correct answer earns "
    r"(?P<correct_points>\d+) points "
    r"and each wrong answer loses "
    r"(?P<wrong_penalty>\d+)\. "
    r"(?P<name>[a-z]+) answered every question "
    r"and scored (?P<score>\d+)\. "
    r"how many were correct\?")


def test_correct_and_wrong_penalty(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TEST_CORRECT_AND_WRONG_PENALTY.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [n[1] for n in numbers] != [False, False, False, False]:
        return None
    total = Fraction(match.group("total"))
    correct_points = Fraction(match.group("correct_points"))
    wrong_penalty = Fraction(match.group("wrong_penalty"))
    score = Fraction(match.group("score"))
    if [n[0] for n in numbers] != [total, correct_points, wrong_penalty, score]:
        return None
    if total <= 0 or correct_points <= 0 or wrong_penalty <= 0:
        return None
    denominator = correct_points + wrong_penalty
    if denominator <= 0:
        return None
    correct = (score + wrong_penalty * total) / denominator
    wrong = total - correct
    if correct <= 0 or wrong <= 0 or correct.denominator != 1 or wrong.denominator != 1:
        return None
    if correct + wrong != total:
        return None
    if correct_points * correct - wrong_penalty * wrong != score:
        return None
    eq = "c + w = %s; %s*c - %s*w = %s" % (
        show(total), show(correct_points), show(wrong_penalty), show(score)
    )
    return Result(
        "test_correct_and_wrong_penalty",
        [correct, wrong],
        eq,
        "%s, so c = %s and w = %s" % (eq, show_exact(correct), show_exact(wrong))
    )


_NICKELS_AND_QUARTERS_COUNT = re.compile(
    r"(?P<name>[a-z]+) has "
    r"(?P<total>\d+) coins, "
    r"all nickels and quarters, "
    r"worth \$(?P<worth>\d+(?:\.\d+)?) "
    r"in total\. "
    r"how many of each coin are there\?")


def nickels_and_quarters_count(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _NICKELS_AND_QUARTERS_COUNT.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [n[1] for n in numbers] != [False, True]:
        return None
    total = Fraction(match.group("total"))
    worth = Fraction(match.group("worth"))
    if [n[0] for n in numbers] != [total, worth]:
        return None
    if total <= 0 or worth <= 0:
        return None
    cents = 100 * worth
    nickels = (25 * total - cents) / 20
    quarters = total - nickels
    if nickels <= 0 or quarters <= 0 or nickels.denominator != 1 or quarters.denominator != 1:
        return None
    if nickels + quarters != total:
        return None
    if 5 * nickels + 25 * quarters != cents:
        return None
    eq = "5*x + 25(%s - x) = %s" % (show(total), show(cents))
    return Result(
        "nickels_and_quarters_count",
        [nickels, quarters],
        eq,
        "%s, so x = %s nickels and %s quarters" % (eq, show_exact(nickels), show_exact(quarters))
    )


_HOUR_LATER_TOWARD_MEET = re.compile(
    r"(?P<first_person>[a-z]+) and "
    r"(?P<second_person>[a-z]+) live "
    r"(?P<distance>\d+(?:\.\d+)?) miles apart\. "
    r"(?P=first_person) drives toward "
    r"(?P=second_person) at "
    r"(?P<speed1>\d+(?:\.\d+)?) mph\. "
    r"(?P<delay>1) hour later, "
    r"(?P=second_person) starts driving toward "
    r"(?P=first_person) at "
    r"(?P<speed2>\d+(?:\.\d+)?) mph\. "
    r"how long after (?P=second_person) "
    r"leaves do they meet\?")


def hour_later_toward_meet(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _HOUR_LATER_TOWARD_MEET.fullmatch(text)
    if match is None:
        return None
    if match.group("first_person") == match.group("second_person"):
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [n[1] for n in numbers] != [False, False, False, False]:
        return None
    distance = Fraction(match.group("distance"))
    speed1 = Fraction(match.group("speed1"))
    delay = Fraction(match.group("delay"))
    speed2 = Fraction(match.group("speed2"))
    if [n[0] for n in numbers] != [distance, speed1, delay, speed2]:
        return None
    if delay != 1 or distance <= 0 or speed1 <= 0 or speed2 <= 0:
        return None
    distance_before_second_leaves = speed1 * delay
    if distance <= distance_before_second_leaves:
        return None
    combined_speed = speed1 + speed2
    if combined_speed <= 0:
        return None
    time = (distance - distance_before_second_leaves) / combined_speed
    if time <= 0:
        return None
    first_distance = speed1 * (time + delay)
    second_distance = speed2 * time
    if first_distance + second_distance != distance:
        return None
    if first_distance <= 0 or second_distance <= 0:
        return None
    eq = "%s*(t + 1) + %s*t = %s" % (show(speed1), show(speed2), show(distance))
    return Result(
        "hour_later_toward_meet",
        [time],
        eq,
        "%s, so t = %s" % (eq, show_exact(time))
    )


_WORKS_ALONE_THEN_PARTNER_JOINS = re.compile(
    r"(?P<first_person>[a-z]+) can do a job in "
    r"(?P<a>\d+) hours and "
    r"(?P<second_person>[a-z]+) can do it in "
    r"(?P<b>\d+) hours\. "
    r"(?P=first_person) works alone for "
    r"(?P<alone>2) hours, "
    r"then (?P=second_person) joins\. "
    r"how much longer will it take to finish\?")


def works_alone_then_partner_joins(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WORKS_ALONE_THEN_PARTNER_JOINS.fullmatch(text)
    if match is None:
        return None
    if match.group("first_person") == match.group("second_person"):
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [False, False, False]:
        return None
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    alone = Fraction(match.group("alone"))
    if [n[0] for n in numbers] != [a, b, alone]:
        return None
    if a <= 0 or b <= 0 or alone != 2 or alone >= a:
        return None
    remaining_work = 1 - alone / a
    if remaining_work <= 0:
        return None
    combined_rate = 1 / a + 1 / b
    if combined_rate <= 0:
        return None
    time = remaining_work / combined_rate
    if time <= 0:
        return None
    if alone / a + time / a + time / b != 1:
        return None
    if time != (a - alone) * b / (a + b):
        return None
    eq = "%s/%s + t/%s + t/%s = 1" % (show(alone), show(a), show(a), show(b))
    return Result(
        "works_alone_then_partner_joins",
        [time],
        eq,
        "%s, so t = %s" % (eq, show_exact(time))
    )


_DIMES_AND_QUARTERS_COUNT = re.compile(
    r"(?P<name>[a-z]+) has "
    r"(?P<total>\d+) coins, "
    r"all dimes and quarters, "
    r"worth \$(?P<worth>\d+(?:\.\d+)?) "
    r"in total\. "
    r"how many of each coin are there\?")


def dimes_and_quarters_count(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _DIMES_AND_QUARTERS_COUNT.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [n[1] for n in numbers] != [False, True]:
        return None
    total = Fraction(match.group("total"))
    worth = Fraction(match.group("worth"))
    if [n[0] for n in numbers] != [total, worth]:
        return None
    if total <= 0 or worth <= 0:
        return None
    cents = 100 * worth
    dimes = (25 * total - cents) / 15
    quarters = total - dimes
    if dimes <= 0 or quarters <= 0 or dimes.denominator != 1 or quarters.denominator != 1:
        return None
    if dimes + quarters != total:
        return None
    if 10 * dimes + 25 * quarters != cents:
        return None
    eq = "10*x + 25(%s - x) = %s" % (show(total), show(cents))
    return Result(
        "dimes_and_quarters_count",
        [dimes, quarters],
        eq,
        "%s, so x = %s dimes and %s quarters" % (eq, show_exact(dimes), show_exact(quarters))
    )


_TWO_HOURS_LATER_TOWARD_MEET = re.compile(
    r"(?P<first_person>[a-z]+) and "
    r"(?P<second_person>[a-z]+) live "
    r"(?P<distance>\d+(?:\.\d+)?) miles apart\. "
    r"(?P=first_person) drives toward "
    r"(?P=second_person) at "
    r"(?P<speed1>\d+(?:\.\d+)?) mph\. "
    r"(?P<delay>2) hours later, "
    r"(?P=second_person) starts driving toward "
    r"(?P=first_person) at "
    r"(?P<speed2>\d+(?:\.\d+)?) mph\. "
    r"how long after (?P=second_person) "
    r"leaves do they meet\?")


def two_hours_later_toward_meet(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_HOURS_LATER_TOWARD_MEET.fullmatch(text)
    if match is None:
        return None
    if match.group("first_person") == match.group("second_person"):
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [n[1] for n in numbers] != [False, False, False, False]:
        return None
    distance = Fraction(match.group("distance"))
    speed1 = Fraction(match.group("speed1"))
    delay = Fraction(match.group("delay"))
    speed2 = Fraction(match.group("speed2"))
    if [n[0] for n in numbers] != [distance, speed1, delay, speed2]:
        return None
    if delay != 2 or distance <= 0 or speed1 <= 0 or speed2 <= 0:
        return None
    distance_before_second_leaves = speed1 * delay
    if distance <= distance_before_second_leaves:
        return None
    combined_speed = speed1 + speed2
    if combined_speed <= 0:
        return None
    time = (distance - distance_before_second_leaves) / combined_speed
    if time <= 0:
        return None
    first_distance = speed1 * (time + delay)
    second_distance = speed2 * time
    if first_distance + second_distance != distance or first_distance <= 0 or second_distance <= 0:
        return None
    eq = "%s*(t + 2) + %s*t = %s" % (show(speed1), show(speed2), show(distance))
    return Result(
        "two_hours_later_toward_meet",
        [time],
        eq,
        "%s, so t = %s" % (eq, show_exact(time))
    )


_LOWEST_NEXT_SCORE_FOR_AVERAGE = re.compile(
    r"(?P<name>[a-z]+)'s test scores are "
    r"(?P<s1>\d+), (?P<s2>\d+), (?P<s3>\d+), (?P<s4>\d+), (?P<s5>\d+)\. "
    r"what is the lowest score on the next test "
    r"that gives an average of at least (?P<target>\d+)\?")


def lowest_next_score_for_average(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LOWEST_NEXT_SCORE_FOR_AVERAGE.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 6 or any(n[1] for n in numbers):
        return None
    scores = [Fraction(match.group(g)) for g in ("s1", "s2", "s3", "s4", "s5")]
    target = Fraction(match.group("target"))
    if [n[0] for n in numbers] != scores + [target]:
        return None
    needed = target * 6 - sum(scores)
    if needed < 0:
        return None
    if needed.denominator == 1:
        lowest = needed
    else:
        lowest = Fraction((needed.numerator + needed.denominator - 1) // needed.denominator)
    if lowest < 0:
        return None
    if all(s <= 100 for s in scores) and target <= 100 and lowest > 100:
        return None
    if (sum(scores) + lowest) / 6 < target:
        return None
    if lowest > 0 and (sum(scores) + (lowest - 1)) / 6 >= target:
        return None
    listed = " + ".join(show(s) for s in scores)
    eq = "(%s + x)/6 >= %s" % (listed, show(target))
    return Result(
        "lowest_next_score_for_average",
        [lowest],
        eq,
        "%s, so the lowest whole score is %s" % (eq, show_exact(lowest))
    )


_WEEKLY_BASE_PLUS_COMMISSION_SALES = re.compile(
    r"(?P<name>[a-z]+) earns a weekly base pay of "
    r"\$(?P<base>\d+(?:\.\d+)?) "
    r"plus (?P<percent>\d+(?:\.\d+)?)% commission on sales\. "
    r"one week the total pay was "
    r"\$(?P<pay>\d+(?:\.\d+)?)\. "
    r"what were the sales\?")


def weekly_base_plus_commission_sales(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WEEKLY_BASE_PLUS_COMMISSION_SALES.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [True, False, True]:
        return None
    base = Fraction(match.group("base"))
    percent = Fraction(match.group("percent"))
    pay = Fraction(match.group("pay"))
    if [n[0] for n in numbers] != [base, percent, pay]:
        return None
    if base < 0 or percent <= 0 or pay <= base:
        return None
    rate = percent / 100
    sales = (pay - base) / rate
    if sales <= 0:
        return None
    if base + rate * sales != pay:
        return None
    eq = "%s + %s*s = %s" % (show(base), show(rate), show(pay))
    return Result(
        "weekly_base_plus_commission_sales",
        [sales],
        eq,
        "%s, so s = %s" % (eq, show_exact(sales))
    )


_WEEKS_UNTIL_GUITAR = re.compile(
    r"(?P<name>[a-z]+) has "
    r"\$(?P<start>\d+(?:\.\d+)?) "
    r"and saves "
    r"\$(?P<rate>\d+(?:\.\d+)?) per week "
    r"to buy a guitar that costs "
    r"\$(?P<target>\d+(?:\.\d+)?)\. "
    r"how many weeks until there is enough\?")


def weeks_until_guitar(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WEEKS_UNTIL_GUITAR.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [True, True, True]:
        return None
    start = Fraction(match.group("start"))
    rate = Fraction(match.group("rate"))
    target = Fraction(match.group("target"))
    if [n[0] for n in numbers] != [start, rate, target]:
        return None
    if start < 0 or rate <= 0 or start >= target:
        return None
    weeks = (target - start) / rate
    if weeks <= 0 or weeks.denominator != 1:
        return None
    if start + rate * weeks != target:
        return None
    eq = "%s + %s*w = %s" % (show(start), show(rate), show(target))
    return Result(
        "weeks_until_guitar",
        [weeks],
        eq,
        "%s, so w = %s" % (eq, show_exact(weeks))
    )


_WORKS_ALONE_ONE_HOUR_THEN_JOINS = re.compile(
    r"(?P<first_person>[a-z]+) can do a job in "
    r"(?P<a>\d+) hours and "
    r"(?P<second_person>[a-z]+) can do it in "
    r"(?P<b>\d+) hours\. "
    r"(?P=first_person) works alone for "
    r"(?P<alone>1) hour, "
    r"then (?P=second_person) joins\. "
    r"how much longer will it take to finish\?")


def works_alone_one_hour_then_joins(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WORKS_ALONE_ONE_HOUR_THEN_JOINS.fullmatch(text)
    if match is None:
        return None
    if match.group("first_person") == match.group("second_person"):
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [False, False, False]:
        return None
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    alone = Fraction(match.group("alone"))
    if [n[0] for n in numbers] != [a, b, alone]:
        return None
    if a <= 0 or b <= 0 or alone != 1 or alone >= a:
        return None
    remaining_work = 1 - alone / a
    if remaining_work <= 0:
        return None
    combined_rate = 1 / a + 1 / b
    if combined_rate <= 0:
        return None
    time = remaining_work / combined_rate
    if time <= 0:
        return None
    if alone / a + time / a + time / b != 1:
        return None
    if time != (a - alone) * b / (a + b):
        return None
    eq = "%s/%s + t/%s + t/%s = 1" % (show(alone), show(a), show(a), show(b))
    return Result(
        "works_alone_one_hour_then_joins",
        [time],
        eq,
        "%s, so t = %s" % (eq, show_exact(time))
    )


def _ax_plus_c(a, op, c):
    a, c = Fraction(a), Fraction(c)
    return a, (c if op == "+" else -c)


_MEAN_OF_LISTED_MISSING = re.compile(
    r"the mean of (?P<n>\d+) numbers is (?P<mean>\d+(?:\.\d+)?)\. "
    r"(?P<k>\d+) of them are (?P<listed>\d+(?:\.\d+)?(?:, \d+(?:\.\d+)?)*)\. "
    r"what is the missing number\?")


def mean_of_listed_missing(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _MEAN_OF_LISTED_MISSING.fullmatch(text)
    if match is None:
        return None
    n = Fraction(match.group("n"))
    mean = Fraction(match.group("mean"))
    k = Fraction(match.group("k"))
    listed = [Fraction(x) for x in match.group("listed").split(", ")]
    numbers = digit_numbers(problem)
    values = [n, mean, k] + listed
    if len(numbers) != len(values) or any(flag for _v, flag, _s, _e in numbers):
        return None
    if [num[0] for num in numbers] != values:
        return None
    if n.denominator != 1 or k.denominator != 1 or n < 2 or k != n - 1 or k != len(listed):
        return None
    missing = n * mean - sum(listed, Fraction(0))
    if n * mean != sum(listed, Fraction(0)) + missing:
        return None
    listed_text = " + ".join(show(x) for x in listed)
    eq = "(%s + x)/%s = %s" % (listed_text, show(n), show(mean))
    return Result(
        "mean_of_listed_missing",
        [missing],
        eq,
        "%s, so x = %s" % (eq, show_exact(missing))
    )


_RENT_FEE_PLUS_USE_EQUALS_BUY = re.compile(
    r"buying a (?P<item>[a-z]+(?: [a-z]+)*) costs "
    r"\$(?P<buy>\d+(?:\.\d+)?)\. "
    r"renting one costs "
    r"\$(?P<fee>\d+(?:\.\d+)?) once plus "
    r"\$(?P<per>\d+(?:\.\d+)?) per use\. "
    r"after how many uses does renting cost the same as buying\?")


def rent_fee_plus_use_equals_buy(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RENT_FEE_PLUS_USE_EQUALS_BUY.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [True, True, True]:
        return None
    buy = Fraction(match.group("buy"))
    fee = Fraction(match.group("fee"))
    per = Fraction(match.group("per"))
    if [n[0] for n in numbers] != [buy, fee, per]:
        return None
    if buy <= 0 or fee < 0 or per <= 0 or fee >= buy:
        return None
    uses = (buy - fee) / per
    if uses <= 0 or uses.denominator != 1:
        return None
    if fee + per * uses != buy:
        return None
    eq = "%s + %s*n = %s" % (show(fee), show(per), show(buy))
    return Result(
        "rent_fee_plus_use_equals_buy",
        [uses],
        eq,
        "%s, so n = %s" % (eq, show_exact(uses))
    )


_RENT_PER_USE_EQUALS_BUY = re.compile(
    r"buying a (?P<item>[a-z]+(?: [a-z]+)*) costs "
    r"\$(?P<buy>\d+(?:\.\d+)?)\. "
    r"renting costs "
    r"\$(?P<per>\d+(?:\.\d+)?) per use\. "
    r"after how many uses would renting cost the same as buying\?")


def rent_per_use_equals_buy(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RENT_PER_USE_EQUALS_BUY.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [n[1] for n in numbers] != [True, True]:
        return None
    buy = Fraction(match.group("buy"))
    per = Fraction(match.group("per"))
    if [n[0] for n in numbers] != [buy, per]:
        return None
    if buy <= 0 or per <= 0:
        return None
    uses = buy / per
    if uses <= 0 or uses.denominator != 1:
        return None
    if per * uses != buy:
        return None
    eq = "%s*n = %s" % (show(per), show(buy))
    return Result(
        "rent_per_use_equals_buy",
        [uses],
        eq,
        "%s, so n = %s" % (eq, show_exact(uses))
    )


_REVERSE_DIGITS_SUM_AND_DIFF = re.compile(
    r"the digits of a two-digit number add up to (?P<s>\d+)\. "
    r"when the digits are reversed, the new number is (?P<d>\d+) "
    r"(?P<dir>more|less) than the original\. find the original number[.?]")


def reverse_digits_sum_and_diff(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _REVERSE_DIGITS_SUM_AND_DIFF.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [n[1] for n in numbers] != [False, False]:
        return None
    s = Fraction(match.group("s"))
    d = Fraction(match.group("d"))
    if [n[0] for n in numbers] != [s, d]:
        return None
    if s.denominator != 1 or d.denominator != 1 or d % 9 != 0 or s < 1 or s > 18 or d <= 0:
        return None
    step = d / 9
    if match.group("dir") == "more":
        # (10u + t) - (10t + u) = d  =>  u - t = d/9
        tens = (s - step) / 2
        units = s - tens
    else:
        # (10t + u) - (10u + t) = d  =>  t - u = d/9
        tens = (s + step) / 2
        units = s - tens
    if tens.denominator != 1 or units.denominator != 1:
        return None
    tens, units = int(tens), int(units)
    if tens < 1 or tens > 9 or units < 1 or units > 9:
        return None
    original = 10 * tens + units
    reversed_n = 10 * units + tens
    if tens + units != s:
        return None
    if match.group("dir") == "more" and reversed_n - original != d:
        return None
    if match.group("dir") == "less" and original - reversed_n != d:
        return None
    eq = "t + u = %s; 9(u - t) = %s" % (show(s), show(d if match.group("dir") == "more" else -d))
    return Result(
        "reverse_digits_sum_and_diff",
        [Fraction(original)],
        eq,
        "%s, so the original number is %s" % (eq, show_exact(original))
    )


_LINEAR_PAIR_TWO_ANGLES = re.compile(
    r"two angles form a linear pair\. one measures "
    r"\((?P<a1>\d+)x (?P<op1>[+\-]) (?P<c1>\d+)\)° and the other "
    r"\((?P<a2>\d+)x (?P<op2>[+\-]) (?P<c2>\d+)\)°\. find both angles[.?]")


def linear_pair_two_angles(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LINEAR_PAIR_TWO_ANGLES.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(n[1] for n in numbers):
        return None
    a1, c1 = _ax_plus_c(match.group("a1"), match.group("op1"), match.group("c1"))
    a2, c2 = _ax_plus_c(match.group("a2"), match.group("op2"), match.group("c2"))
    raw = [Fraction(match.group(g)) for g in ("a1", "c1", "a2", "c2")]
    if [n[0] for n in numbers] != raw:
        return None
    if a1 + a2 == 0:
        return None
    x = (180 - c1 - c2) / (a1 + a2)
    ang1 = a1 * x + c1
    ang2 = a2 * x + c2
    if ang1 <= 0 or ang2 <= 0 or ang1 >= 180 or ang2 >= 180:
        return None
    if ang1 + ang2 != 180:
        return None
    eq = "(%sx %s %s) + (%sx %s %s) = 180" % (
        show(a1), "+" if c1 >= 0 else "−", show(abs(c1)),
        show(a2), "+" if c2 >= 0 else "−", show(abs(c2)),
    )
    return Result(
        "linear_pair_two_angles",
        [x, ang1, ang2],
        eq,
        "%s, so x = %s and the angles are %s° and %s°" % (eq, show_exact(x), show_exact(ang1), show_exact(ang2))
    )


_STRAIGHT_LINE_ANGLES_A_B = re.compile(
    r"angles a and b lie on a straight line\. "
    r"a = \((?P<a1>\d+)x (?P<op1>[+\-]) (?P<c1>\d+)\)° and "
    r"b = \((?P<a2>\d+)x (?P<op2>[+\-]) (?P<c2>\d+)\)°\. what are a and b\?")


def straight_line_angles_a_b(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _STRAIGHT_LINE_ANGLES_A_B.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(n[1] for n in numbers):
        return None
    a1, c1 = _ax_plus_c(match.group("a1"), match.group("op1"), match.group("c1"))
    a2, c2 = _ax_plus_c(match.group("a2"), match.group("op2"), match.group("c2"))
    raw = [Fraction(match.group(g)) for g in ("a1", "c1", "a2", "c2")]
    if [n[0] for n in numbers] != raw:
        return None
    if a1 + a2 == 0:
        return None
    x = (180 - c1 - c2) / (a1 + a2)
    ang1 = a1 * x + c1
    ang2 = a2 * x + c2
    if ang1 <= 0 or ang2 <= 0 or ang1 >= 180 or ang2 >= 180:
        return None
    if ang1 + ang2 != 180:
        return None
    eq = "(%sx %s %s) + (%sx %s %s) = 180" % (
        show(a1), "+" if c1 >= 0 else "−", show(abs(c1)),
        show(a2), "+" if c2 >= 0 else "−", show(abs(c2)),
    )
    return Result(
        "straight_line_angles_a_b",
        [x, ang1, ang2],
        eq,
        "%s, so x = %s and the angles are %s° and %s°" % (eq, show_exact(x), show_exact(ang1), show_exact(ang2))
    )


_SQUARE_SIDE_LINEAR_PERIMETER = re.compile(
    r"each side of a square is "
    r"\((?P<a>\d+)x (?P<op>[+\-]) (?P<c>\d+)\) cm\. "
    r"the perimeter is (?P<p>\d+(?:\.\d+)?) cm\. find x and the side length[.?]")


def square_side_linear_perimeter(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SQUARE_SIDE_LINEAR_PERIMETER.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(n[1] for n in numbers):
        return None
    a, c = _ax_plus_c(match.group("a"), match.group("op"), match.group("c"))
    p = Fraction(match.group("p"))
    raw = [Fraction(match.group("a")), Fraction(match.group("c")), p]
    if [n[0] for n in numbers] != raw:
        return None
    if a == 0:
        return None
    side = p / 4
    x = (side - c) / a
    if side <= 0:
        return None
    if 4 * (a * x + c) != p:
        return None
    eq = "4(%sx %s %s) = %s" % (show(a), "+" if c >= 0 else "−", show(abs(c)), show(p))
    return Result(
        "square_side_linear_perimeter",
        [x, side],
        eq,
        "%s, so x = %s and the side is %s" % (eq, show_exact(x), show_exact(side))
    )


_TWO_NUMBERS_SUM_AND_PRODUCT = re.compile(
    r"(?:two numbers add up to (?P<s1>\d+(?:\.\d+)?) and multiply to (?P<p1>\d+(?:\.\d+)?)\. what are they\?"
    r"|the sum of two numbers is (?P<s2>\d+(?:\.\d+)?) and their product is (?P<p2>\d+(?:\.\d+)?)\. find the numbers[.?])")


def two_numbers_sum_and_product(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_NUMBERS_SUM_AND_PRODUCT.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(n[1] for n in numbers):
        return None
    s = Fraction(match.group("s1") or match.group("s2"))
    p = Fraction(match.group("p1") or match.group("p2"))
    if [n[0] for n in numbers] != [s, p]:
        return None
    disc = s * s - 4 * p
    root = _isqrt_exact(int(disc)) if disc.denominator == 1 else None
    if root is None:
        return None
    x1 = (s - root) / 2
    x2 = (s + root) / 2
    if x1 + x2 != s or x1 * x2 != p:
        return None
    eq = "x + y = %s; xy = %s" % (show(s), show(p))
    return Result(
        "two_numbers_sum_and_product",
        [x1, x2],
        eq,
        "%s, so the numbers are %s and %s" % (eq, show_exact(x1), show_exact(x2))
    )


_THREE_PART_MIX_RATIO = re.compile(
    r"a mix uses (?P<parts>.+?) in the ratio "
    r"(?P<a>\d+):(?P<b>\d+):(?P<c>\d+)\. "
    r"the total is (?P<total>\d+(?:\.\d+)?) (?P<unit>[a-z]+)\. "
    r"how much of each is used\?")


def three_part_mix_ratio(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _THREE_PART_MIX_RATIO.fullmatch(text)
    if match is None:
        return None
    if re.search(r"\d", match.group("parts")):
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(n[1] for n in numbers):
        return None
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    c = Fraction(match.group("c"))
    total = Fraction(match.group("total"))
    if [n[0] for n in numbers] != [a, b, c, total]:
        return None
    parts = a + b + c
    if a <= 0 or b <= 0 or c <= 0 or total <= 0 or parts <= 0:
        return None
    one = total / parts
    amounts = [a * one, b * one, c * one]
    if sum(amounts) != total:
        return None
    eq = "%sk + %sk + %sk = %s" % (show(a), show(b), show(c), show(total))
    return Result(
        "three_part_mix_ratio",
        amounts,
        eq,
        "%s, so the amounts are %s, %s, %s" % (eq, show_exact(amounts[0]), show_exact(amounts[1]), show_exact(amounts[2]))
    )


_WEEKS_UNTIL_ITEM = re.compile(
    r"(?P<name>[a-z]+) has "
    r"\$(?P<start>\d+(?:\.\d+)?) "
    r"and saves "
    r"\$(?P<rate>\d+(?:\.\d+)?) per week "
    r"to buy (?:a )?(?P<item>[a-z]+(?: [a-z]+)*) that costs "
    r"\$(?P<target>\d+(?:\.\d+)?)\. "
    r"how many weeks until there is enough\?")


def weeks_until_item(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WEEKS_UNTIL_ITEM.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [True, True, True]:
        return None
    start = Fraction(match.group("start"))
    rate = Fraction(match.group("rate"))
    target = Fraction(match.group("target"))
    if [n[0] for n in numbers] != [start, rate, target]:
        return None
    if start < 0 or rate <= 0 or start >= target:
        return None
    weeks = (target - start) / rate
    if weeks <= 0 or weeks.denominator != 1:
        return None
    if start + rate * weeks != target:
        return None
    eq = "%s + %s*w = %s" % (show(start), show(rate), show(target))
    return Result(
        "weeks_until_item",
        [weeks],
        eq,
        "%s, so w = %s" % (eq, show_exact(weeks))
    )


_ADULT_AND_CHILD_TICKETS = re.compile(
    r"adult tickets to a (?P<venue>museum|concert) cost "
    r"\$(?P<adult>\d+(?:\.\d+)?) "
    r"and child tickets cost "
    r"\$(?P<child>\d+(?:\.\d+)?)\. "
    r"(?P<count>\d+) tickets were sold for a total of "
    r"\$(?P<total>\d+(?:\.\d+)?)\. "
    r"how many of each were sold\?")


def adult_and_child_tickets(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _ADULT_AND_CHILD_TICKETS.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [n[1] for n in numbers] != [True, True, False, True]:
        return None
    adult = Fraction(match.group("adult"))
    child = Fraction(match.group("child"))
    count = Fraction(match.group("count"))
    total = Fraction(match.group("total"))
    if [n[0] for n in numbers] != [adult, child, count, total]:
        return None
    if adult <= child or child < 0 or count <= 0 or count.denominator != 1:
        return None
    adults = (total - child * count) / (adult - child)
    children = count - adults
    if adults.denominator != 1 or children.denominator != 1 or adults <= 0 or children <= 0:
        return None
    if adult * adults + child * children != total:
        return None
    eq = "%s*a + %s*(%s - a) = %s" % (show(adult), show(child), show(count), show(total))
    return Result(
        "adult_and_child_tickets",
        [adults, children],
        eq,
        "%s, so a = %s adult and %s child tickets" % (eq, show_exact(adults), show_exact(children))
    )


_TWO_PLANS_SAME_COST = re.compile(
    r"(?P<kind>electric utility|phone) plan a costs "
    r"\$(?P<a>\d+(?:\.\d+)?) plus "
    r"\$(?P<ra>\d+(?:\.\d+)?) per (?P<u1>kwh|minute)\. "
    r"plan b costs "
    r"\$(?P<b>\d+(?:\.\d+)?) plus "
    r"\$(?P<rb>\d+(?:\.\d+)?) per (?P<u2>kwh|minute)\. "
    r"for how many (?P<q>kwhs|minutes) do they cost the same\?")


def two_plans_same_cost(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_PLANS_SAME_COST.fullmatch(text)
    if match is None:
        return None
    if match.group("u1") != match.group("u2"):
        return None
    if match.group("u1") == "kwh" and match.group("q") != "kwhs":
        return None
    if match.group("u1") == "minute" and match.group("q") != "minutes":
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [n[1] for n in numbers] != [True, True, True, True]:
        return None
    a = Fraction(match.group("a"))
    ra = Fraction(match.group("ra"))
    b = Fraction(match.group("b"))
    rb = Fraction(match.group("rb"))
    if [n[0] for n in numbers] != [a, ra, b, rb]:
        return None
    if ra == rb:
        return None
    x = (a - b) / (rb - ra)
    if x <= 0:
        return None
    if a + ra * x != b + rb * x:
        return None
    eq = "%s + %s*x = %s + %s*x" % (show(a), show(ra), show(b), show(rb))
    return Result(
        "two_plans_same_cost",
        [x],
        eq,
        "%s, so x = %s" % (eq, show_exact(x))
    )


_FOOD_TRUCK_MEALS_COVER_COSTS = re.compile(
    r"a food truck pays \$(?P<fixed>\d+(?:\.\d+)?) in daily costs, "
    r"and each meal costs \$(?P<cost>\d+(?:\.\d+)?) in ingredients\. "
    r"meals sell for \$(?P<price>\d+(?:\.\d+)?)\. "
    r"how many meals a day cover the costs\?")


def food_truck_meals_cover_costs(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _FOOD_TRUCK_MEALS_COVER_COSTS.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [True, True, True]:
        return None
    fixed = Fraction(match.group("fixed"))
    cost = Fraction(match.group("cost"))
    price = Fraction(match.group("price"))
    if [n[0] for n in numbers] != [fixed, cost, price]:
        return None
    if price <= cost or fixed <= 0:
        return None
    n = fixed / (price - cost)
    if n <= 0 or n.denominator != 1:
        return None
    if price * n != fixed + cost * n:
        return None
    eq = "%s*n = %s + %s*n" % (show(price), show(fixed), show(cost))
    return Result(
        "food_truck_meals_cover_costs",
        [n],
        eq,
        "%s, so n = %s" % (eq, show_exact(n))
    )


_PRINT_RUN_POSTERS_BREAK_EVEN = re.compile(
    r"it costs \$(?P<setup>\d+(?:\.\d+)?) to set up a print run plus "
    r"\$(?P<each>\d+(?:\.\d+)?) per poster\. "
    r"posters sell for \$(?P<price>\d+(?:\.\d+)?) each\. "
    r"how many must be sold to break even\?")


def print_run_posters_break_even(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PRINT_RUN_POSTERS_BREAK_EVEN.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [n[1] for n in numbers] != [True, True, True]:
        return None
    setup = Fraction(match.group("setup"))
    each = Fraction(match.group("each"))
    price = Fraction(match.group("price"))
    if [n[0] for n in numbers] != [setup, each, price]:
        return None
    if price <= each or setup <= 0:
        return None
    n = setup / (price - each)
    if n <= 0 or n.denominator != 1:
        return None
    if price * n != setup + each * n:
        return None
    eq = "%s*n = %s + %s*n" % (show(price), show(setup), show(each))
    return Result(
        "print_run_posters_break_even",
        [n],
        eq,
        "%s, so n = %s" % (eq, show_exact(n))
    )


_TANK_FILL_FROM_FRACTION = re.compile(
    r"(?:a gas tank is (?P<a1>\d+)/(?P<b1>\d+) full\. adding (?P<add1>\d+(?:\.\d+)?) gallons fills it to (?P<c1>\d+)/(?P<d1>\d+)\. how much does the tank hold\?"
    r"|a tank is (?P<a2>\d+)/(?P<b2>\d+) full\. after (?P<add2>\d+(?:\.\d+)?) liters are added, it is (?P<c2>\d+)/(?P<d2>\d+) full\. what is the tank's capacity\?)")


def tank_fill_from_fraction(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TANK_FILL_FROM_FRACTION.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if match.group("a1") is not None:
        parts = [match.group(g) for g in ("a1", "b1", "add1", "c1", "d1")]
    else:
        parts = [match.group(g) for g in ("a2", "b2", "add2", "c2", "d2")]
    vals = [Fraction(x) for x in parts]
    if len(numbers) != 5 or any(n[1] for n in numbers) or [n[0] for n in numbers] != vals:
        return None
    start = vals[0] / vals[1]
    added = vals[2]
    end = vals[3] / vals[4]
    if end <= start or added <= 0:
        return None
    cap = added / (end - start)
    if cap <= 0:
        return None
    if start * cap + added != end * cap:
        return None
    eq = "(%s/%s)c + %s = (%s/%s)c" % (show(vals[0]), show(vals[1]), show(added), show(vals[3]), show(vals[4]))
    return Result(
        "tank_fill_from_fraction",
        [cap],
        eq,
        "%s, so c = %s" % (eq, show_exact(cap))
    )


_RECTANGLE_LENGTH_FROM_WIDTH_PERIMETER = re.compile(
    r"the length of a rectangle is "
    r"(?:(?P<k_less>\d+) less than (?P<m_less>\d+) times its width"
    r"|(?P<k_more>\d+) more than its width"
    r"|(?P<k_more_times>\d+) more than (?P<m_more>\d+) times its width)"
    r"\. the perimeter is (?P<p>\d+(?:\.\d+)?) cm\. find the dimensions\.")


def rectangle_length_from_width_perimeter(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RECTANGLE_LENGTH_FROM_WIDTH_PERIMETER.fullmatch(text)
    if match is None:
        return None
    p = Fraction(match.group("p"))
    if match.group("k_less") is not None:
        k = Fraction(match.group("k_less"))
        m = Fraction(match.group("m_less"))
        expected = [k, m, p]
        length_from = lambda w: m * w - k
    elif match.group("k_more_times") is not None:
        k = Fraction(match.group("k_more_times"))
        m = Fraction(match.group("m_more"))
        expected = [k, m, p]
        length_from = lambda w: m * w + k
    else:
        k = Fraction(match.group("k_more"))
        m = Fraction(1)
        expected = [k, p]
        length_from = lambda w: w + k
    numbers = digit_numbers(problem)
    if len(numbers) != len(expected) or any(n[1] for n in numbers) or [n[0] for n in numbers] != expected:
        return None
    # 2w + 2 L(w) = P
    # For L = m w + c with c = ±k: 2w + 2m w + 2c = P, w = (P - 2c) / (2 + 2m)
    sample_c = length_from(0)
    denom = 2 + 2 * m
    if denom == 0:
        return None
    w = (p - 2 * sample_c) / denom
    length = length_from(w)
    if w <= 0 or length <= 0:
        return None
    if 2 * w + 2 * length != p:
        return None
    eq = "2w + 2(%s) = %s" % (
        "%sw %s %s" % (show(m), "+" if sample_c >= 0 else "−", show(abs(sample_c))) if m != 1 or sample_c != 0 else "w + %s" % show(k),
        show(p),
    )
    return Result(
        "rectangle_length_from_width_perimeter",
        [w, length],
        eq,
        "%s, so w = %s and L = %s" % (eq, show_exact(w), show_exact(length))
    )


_LOWEST_NEXT_SCORE_FEW_TESTS = re.compile(
    r"(?P<name>[a-z]+)'s test scores are "
    r"(?P<listed>\d+(?:, \d+){1,3})\. "
    r"what is the lowest score on the next test "
    r"that gives an average of at least (?P<target>\d+)\?")


def lowest_next_score_few_tests(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LOWEST_NEXT_SCORE_FEW_TESTS.fullmatch(text)
    if match is None:
        return None
    scores = [Fraction(x) for x in match.group("listed").split(", ")]
    if not (2 <= len(scores) <= 4):
        return None
    target = Fraction(match.group("target"))
    numbers = digit_numbers(problem)
    expected = scores + [target]
    if len(numbers) != len(expected) or any(n[1] for n in numbers) or [n[0] for n in numbers] != expected:
        return None
    k = len(scores) + 1
    needed = target * k - sum(scores)
    if needed < 0:
        return None
    if needed.denominator == 1:
        lowest = needed
    else:
        lowest = Fraction((needed.numerator + needed.denominator - 1) // needed.denominator)
    if lowest < 0:
        return None
    if all(s <= 100 for s in scores) and target <= 100 and lowest > 100:
        return None
    if (sum(scores) + lowest) / k < target:
        return None
    if lowest > 0 and (sum(scores) + (lowest - 1)) / k >= target:
        return None
    listed = " + ".join(show(s) for s in scores)
    eq = "(%s + x)/%s >= %s" % (listed, show(k), show(target))
    return Result(
        "lowest_next_score_few_tests",
        [lowest],
        eq,
        "%s, so the lowest whole score is %s" % (eq, show_exact(lowest))
    )


_ITEMS_SOLD_FOR_GIVEN_PROFIT = re.compile(
    r"a (?P<who>t-shirt business|bakery stall) has fixed costs of "
    r"\$(?P<fixed>\d+(?:\.\d+)?)\. "
    r"each item costs \$(?P<cost>\d+(?:\.\d+)?) to make and sells for "
    r"\$(?P<price>\d+(?:\.\d+)?)\. "
    r"how many items must be sold to make a profit of "
    r"\$(?P<profit>\d+(?:\.\d+)?)\?")


def items_sold_for_given_profit(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _ITEMS_SOLD_FOR_GIVEN_PROFIT.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [n[1] for n in numbers] != [True, True, True, True]:
        return None
    fixed = Fraction(match.group("fixed"))
    cost = Fraction(match.group("cost"))
    price = Fraction(match.group("price"))
    profit = Fraction(match.group("profit"))
    if [n[0] for n in numbers] != [fixed, cost, price, profit]:
        return None
    if price <= cost or fixed < 0 or profit < 0:
        return None
    n = (profit + fixed) / (price - cost)
    if n <= 0 or n.denominator != 1:
        return None
    if price * n - (fixed + cost * n) != profit:
        return None
    eq = "%s*n - (%s + %s*n) = %s" % (show(price), show(fixed), show(cost), show(profit))
    return Result(
        "items_sold_for_given_profit",
        [n],
        eq,
        "%s, so n = %s" % (eq, show_exact(n))
    )


_PROJECTILE_HIT_GROUND = re.compile(
    r"a (?P<object>rocket|rock|stone) is launched upward from a height of "
    r"(?P<h>\d+(?:\.\d+)?) ft at (?P<v>\d+(?:\.\d+)?) ft/s\. "
    r"its height is h = -(?P<g>\d+(?:\.\d+)?)t² \+ (?P<v2>\d+(?:\.\d+)?)t \+ (?P<h2>\d+(?:\.\d+)?)\. "
    r"after how many seconds does it hit the ground\?")


def projectile_hit_ground(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PROJECTILE_HIT_GROUND.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    h = Fraction(match.group("h"))
    v = Fraction(match.group("v"))
    g = Fraction(match.group("g"))
    v2 = Fraction(match.group("v2"))
    h2 = Fraction(match.group("h2"))
    if len(numbers) != 5 or any(n[1] for n in numbers):
        return None
    if [n[0] for n in numbers] != [h, v, g, v2, h2]:
        return None
    if v != v2 or h != h2 or g <= 0 or h <= 0 or v < 0:
        return None
    disc = v * v + 4 * g * h
    root = _isqrt_exact(int(disc)) if disc.denominator == 1 else None
    if root is None:
        return None
    t = (v + root) / (2 * g)
    if t <= 0:
        return None
    if -g * t * t + v * t + h != 0:
        return None
    eq = "-%s*t² + %s*t + %s = 0" % (show(g), show(v), show(h))
    return Result(
        "projectile_hit_ground",
        [t],
        eq,
        "%s, so t = %s" % (eq, show_exact(t))
    )


_STACK_OF_CANS_ROWS = re.compile(
    r"a stack of cans has (?P<a>\d+) cans? in the top row, "
    r"and each row below has (?P<d>\d+) more than the row above\. "
    r"the stack has (?P<s>\d+) cans in total\. how many rows are there\?")


def stack_of_cans_rows(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _STACK_OF_CANS_ROWS.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(n[1] for n in numbers):
        return None
    a = Fraction(match.group("a"))
    d = Fraction(match.group("d"))
    total = Fraction(match.group("s"))
    if [n[0] for n in numbers] != [a, d, total]:
        return None
    if a <= 0 or d <= 0 or total <= 0:
        return None
    # d n^2 + (2a - d) n - 2 total = 0
    aa = d
    bb = 2 * a - d
    cc = -2 * total
    disc = bb * bb - 4 * aa * cc
    root = _isqrt_exact(int(disc)) if disc.denominator == 1 else None
    if root is None or aa == 0:
        return None
    n = (-bb + root) / (2 * aa)
    if n <= 0 or n.denominator != 1:
        return None
    if n / 2 * (2 * a + (n - 1) * d) != total:
        return None
    eq = "(n/2)(2*%s + (n - 1)*%s) = %s" % (show(a), show(d), show(total))
    return Result(
        "stack_of_cans_rows",
        [n],
        eq,
        "%s, so n = %s" % (eq, show_exact(n))
    )


_NUMBER_PLUS_RECIPROCAL = re.compile(
    r"a number plus its reciprocal equals "
    r"(?:(?P<k>\d+(?:\.\d+)?)|(?P<num>\d+)/(?P<den>\d+))"
    r"\. find the number\.")


def number_plus_reciprocal(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _NUMBER_PLUS_RECIPROCAL.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if match.group("k") is not None:
        k = Fraction(match.group("k"))
        expected = [k]
    else:
        k = Fraction(match.group("num")) / Fraction(match.group("den"))
        expected = [Fraction(match.group("num")), Fraction(match.group("den"))]
    if len(numbers) != len(expected) or any(n[1] for n in numbers) or [n[0] for n in numbers] != expected:
        return None
    disc = k * k - 4
    if disc < 0:
        return None
    if disc.denominator == 1:
        root = _isqrt_exact(int(disc))
        if root is None:
            return None
        root = Fraction(root)
    else:
        # (p/q)^2 = disc
        if disc.numerator < 0:
            return None
        rn = _isqrt_exact(disc.numerator)
        rd = _isqrt_exact(disc.denominator)
        if rn is None or rd is None:
            return None
        root = Fraction(rn, rd)
    x1 = (k - root) / 2
    x2 = (k + root) / 2
    if x1 == 0 or x2 == 0:
        return None
    if x1 + 1 / x1 != k or x2 + 1 / x2 != k:
        return None
    pair = [x1, x2] if x1 <= x2 else [x2, x1]
    eq = "x + 1/x = %s" % show(k)
    return Result(
        "number_plus_reciprocal",
        pair,
        eq,
        "%s, so x = %s or %s" % (eq, show_exact(pair[0]), show_exact(pair[1]))
    )


_XY_EQ = re.compile(
    r"(?P<sx>-)?(?P<ax>\d+)?x (?P<sy>[+-]) (?P<ay>\d+)?y = (?P<sc>-)?(?P<c>\d+)")
_TWO_LINEAR_EQUATIONS_XY = re.compile(
    r"two numbers x and y satisfy (?P<e1>.+?) and (?P<e2>.+?)\. find x and y\.")


def _xy_line(eq):
    match = _XY_EQ.fullmatch(eq.strip())
    if match is None:
        return None
    ax = Fraction(match.group("ax") or 1)
    if match.group("sx") == "-":
        ax = -ax
    ay = Fraction(match.group("ay") or 1)
    if match.group("sy") == "-":
        ay = -ay
    c = Fraction(match.group("c"))
    if match.group("sc") == "-":
        c = -c
    digits = []
    if match.group("ax"):
        digits.append(Fraction(match.group("ax")))
    if match.group("ay"):
        digits.append(Fraction(match.group("ay")))
    digits.append(Fraction(match.group("c")))
    return ax, ay, c, digits


def two_linear_equations_xy(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_LINEAR_EQUATIONS_XY.fullmatch(text)
    if match is None:
        return None
    line1 = _xy_line(match.group("e1"))
    line2 = _xy_line(match.group("e2"))
    if line1 is None or line2 is None:
        return None
    a1, b1, c1, d1 = line1
    a2, b2, c2, d2 = line2
    numbers = digit_numbers(problem)
    expected = d1 + d2
    if len(numbers) != len(expected) or any(n[1] for n in numbers) or [n[0] for n in numbers] != expected:
        return None
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    if a1 * x + b1 * y != c1 or a2 * x + b2 * y != c2:
        return None
    eq = "%sx + %sy = %s; %sx + %sy = %s" % (show(a1), show(b1), show(c1), show(a2), show(b2), show(c2))
    return Result(
        "two_linear_equations_xy",
        [x, y],
        eq,
        "%s, so x = %s and y = %s" % (eq, show_exact(x), show_exact(y))
    )


def _two_counts(n, a, b, total):
    if a == b or n <= 0:
        return None
    x = (b * n - total) / (b - a)
    y = n - x
    if x <= 0 or y <= 0 or x.denominator != 1 or y.denominator != 1:
        return None
    if a * x + b * y != total:
        return None
    return x, y


def _pyth_leg(hyp, other):
    d = hyp * hyp - other * other
    if d <= 0 or d.denominator != 1:
        return None
    root = _isqrt_exact(int(d))
    return None if root is None else Fraction(root)


_CAMP_TWO_SEAT_SIZES = re.compile(
    r"a camp rents (?P<n>\d+) (?P<craft>canoes|paddle boats) for (?P<people>\d+) campers, filling every seat\. "
    r"some (?P=craft) hold (?P<a>\d+) people and the rest hold (?P<b>\d+)\. "
    r"how many of each were rented\?")


def camp_two_seat_sizes(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CAMP_TWO_SEAT_SIZES.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    n = Fraction(match.group("n"))
    people = Fraction(match.group("people"))
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [n, people, a, b]:
        return None
    pair = _two_counts(n, a, b, people)
    if pair is None:
        return None
    x, y = pair
    eq = "x + y = %s; %s*x + %s*y = %s" % (show(n), show(a), show(b), show(people))
    return Result("camp_two_seat_sizes", [x, y], eq, "%s, so x = %s and y = %s" % (eq, show_exact(x), show_exact(y)))


_PACKED_TWO_CARTON_SIZES = re.compile(
    r"a farm packed (?P<eggs>\d+) eggs into (?P<n>\d+) cartons, using cartons of (?P<a>\d+) and cartons of (?P<b>\d+)\. "
    r"all cartons were full\. how many of each\?")


def packed_two_carton_sizes(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PACKED_TWO_CARTON_SIZES.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    eggs = Fraction(match.group("eggs"))
    n = Fraction(match.group("n"))
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [eggs, n, a, b]:
        return None
    pair = _two_counts(n, a, b, eggs)
    if pair is None:
        return None
    x, y = pair
    eq = "x + y = %s; %s*x + %s*y = %s" % (show(n), show(a), show(b), show(eggs))
    return Result("packed_two_carton_sizes", [x, y], eq, "%s, so x = %s and y = %s" % (eq, show_exact(x), show_exact(y)))


_BANQUET_TWO_TABLE_SIZES = re.compile(
    r"a banquet hall seats (?P<guests>\d+) guests at (?P<n>\d+) tables\. "
    r"some tables seat (?P<a>\d+) and the others seat (?P<b>\d+)\. how many of each kind are there\?")


def banquet_two_table_sizes(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BANQUET_TWO_TABLE_SIZES.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    guests = Fraction(match.group("guests"))
    n = Fraction(match.group("n"))
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [guests, n, a, b]:
        return None
    pair = _two_counts(n, a, b, guests)
    if pair is None:
        return None
    x, y = pair
    eq = "x + y = %s; %s*x + %s*y = %s" % (show(n), show(a), show(b), show(guests))
    return Result("banquet_two_table_sizes", [x, y], eq, "%s, so x = %s and y = %s" % (eq, show_exact(x), show_exact(y)))


_CASH_DRAWER_TWO_BILL_VALUES = re.compile(
    r"a cash drawer has (?P<n>\d+) bills, all \$(?P<a>\d+) and \$(?P<b>\d+) bills, totaling \$(?P<total>\d+(?:\.\d+)?)\. how many of each\?")


def cash_drawer_two_bill_values(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CASH_DRAWER_TWO_BILL_VALUES.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    n = Fraction(match.group("n"))
    a = Fraction(match.group("a"))
    b = Fraction(match.group("b"))
    total = Fraction(match.group("total"))
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [False, True, True, True]:
        return None
    if [num[0] for num in numbers] != [n, a, b, total]:
        return None
    pair = _two_counts(n, a, b, total)
    if pair is None:
        return None
    x, y = pair
    eq = "x + y = %s; %s*x + %s*y = %s" % (show(n), show(a), show(b), show(total))
    return Result("cash_drawer_two_bill_values", [x, y], eq, "%s, so x = %s and y = %s" % (eq, show_exact(x), show_exact(y)))


_LOT_TWO_WHEEL_VEHICLES = re.compile(
    r"a lot has (?P<pair>motorcycles and cars|bicycles and tricycles)\. "
    r"there are (?P<n>\d+) vehicles and (?P<w>\d+) wheels\. how many of each are there\?")


def lot_two_wheel_vehicles(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LOT_TWO_WHEEL_VEHICLES.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    n = Fraction(match.group("n"))
    w = Fraction(match.group("w"))
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [n, w]:
        return None
    a, b = (2, 4) if match.group("pair") == "motorcycles and cars" else (2, 3)
    pair = _two_counts(n, Fraction(a), Fraction(b), w)
    if pair is None:
        return None
    x, y = pair
    eq = "x + y = %s; %s*x + %s*y = %s" % (show(n), show(a), show(b), show(w))
    return Result("lot_two_wheel_vehicles", [x, y], eq, "%s, so x = %s and y = %s" % (eq, show_exact(x), show_exact(y)))


_FARM_SPIDERS_AND_BEETLES = re.compile(
    r"a farm has spiders and beetles\. there are (?P<n>\d+) bugs and (?P<legs>\d+) legs\. how many of each are there\?")


def farm_spiders_and_beetles(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _FARM_SPIDERS_AND_BEETLES.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    n = Fraction(match.group("n"))
    legs = Fraction(match.group("legs"))
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [n, legs]:
        return None
    pair = _two_counts(n, Fraction(8), Fraction(6), legs)
    if pair is None:
        return None
    x, y = pair
    eq = "x + y = %s; 8*x + 6*y = %s" % (show(n), show(legs))
    return Result("farm_spiders_and_beetles", [x, y], eq, "%s, so x = %s spiders and y = %s beetles" % (eq, show_exact(x), show_exact(y)))


_RECTANGLE_SIDE_AND_DIAGONAL = re.compile(
    r"(?:a rectangular field is (?P<long>\d+(?:\.\d+)?) m long\. a diagonal path across it is (?P<diag1>\d+(?:\.\d+)?) m long\. how wide is the field\?"
    r"|a rectangular tv screen is (?P<tall>\d+(?:\.\d+)?) in tall with a diagonal of (?P<diag2>\d+(?:\.\d+)?) in\. how wide is it\?)")


def rectangle_side_and_diagonal(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RECTANGLE_SIDE_AND_DIAGONAL.fullmatch(text)
    if match is None:
        return None
    if match.group("long") is not None:
        known, hyp = Fraction(match.group("long")), Fraction(match.group("diag1"))
    else:
        known, hyp = Fraction(match.group("tall")), Fraction(match.group("diag2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [known, hyp]:
        return None
    width = _pyth_leg(hyp, known)
    if width is None or width <= 0:
        return None
    eq = "%s² + x² = %s²" % (show(known), show(hyp))
    return Result("rectangle_side_and_diagonal", [width], eq, "%s, so x = %s" % (eq, show_exact(width)))


_LADDER_WIRE_RAMP_HEIGHT = re.compile(
    r"(?:a (?P<ladder>\d+(?:\.\d+)?) ft ladder leans against a wall with its foot (?P<foot>\d+(?:\.\d+)?) ft from the wall\. how high up the wall does it reach\?"
    r"|a (?P<wire>\d+(?:\.\d+)?) m support wire runs from the top of a pole to a stake (?P<stake>\d+(?:\.\d+)?) m from the pole's base\. how tall is the pole\?"
    r"|a ramp is (?P<ramp>\d+(?:\.\d+)?) ft long and covers a horizontal distance of (?P<horiz>\d+(?:\.\d+)?) ft; how high does it rise\?)")


def ladder_wire_ramp_height(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LADDER_WIRE_RAMP_HEIGHT.fullmatch(text)
    if match is None:
        return None
    if match.group("ladder") is not None:
        hyp, other = Fraction(match.group("ladder")), Fraction(match.group("foot"))
    elif match.group("wire") is not None:
        hyp, other = Fraction(match.group("wire")), Fraction(match.group("stake"))
    else:
        hyp, other = Fraction(match.group("ramp")), Fraction(match.group("horiz"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [hyp, other]:
        return None
    height = _pyth_leg(hyp, other)
    if height is None or height <= 0:
        return None
    eq = "%s² + h² = %s²" % (show(other), show(hyp))
    return Result("ladder_wire_ramp_height", [height], eq, "%s, so h = %s" % (eq, show_exact(height)))


_RIGHT_TRIANGLE_LEGS_DIFFER = re.compile(
    r"(?:one leg of a right triangle is (?P<d1>\d+(?:\.\d+)?) cm longer than the other\. the hypotenuse is (?P<h1>\d+(?:\.\d+)?) cm\. find the legs\."
    r"|the hypotenuse of a right triangle is (?P<h2>\d+(?:\.\d+)?) in, and one leg is (?P<d2>\d+(?:\.\d+)?) in longer than the other leg\. how long are the legs\?)")


def right_triangle_legs_differ(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RIGHT_TRIANGLE_LEGS_DIFFER.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if match.group("d1") is not None:
        d, hyp = Fraction(match.group("d1")), Fraction(match.group("h1"))
        expected = [d, hyp]
    else:
        hyp, d = Fraction(match.group("h2")), Fraction(match.group("d2"))
        expected = [hyp, d]
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != expected:
        return None
    # x^2 + (x+d)^2 = hyp^2  =>  2x^2 + 2 d x + d^2 - hyp^2 = 0
    aa = Fraction(2)
    bb = 2 * d
    cc = d * d - hyp * hyp
    disc = bb * bb - 4 * aa * cc
    root = _isqrt_exact(int(disc)) if disc.denominator == 1 else None
    if root is None:
        return None
    x = (-bb + root) / (2 * aa)
    if x <= 0:
        return None
    other = x + d
    if x * x + other * other != hyp * hyp:
        return None
    eq = "x² + (x + %s)² = %s²" % (show(d), show(hyp))
    return Result("right_triangle_legs_differ", [x, other], eq, "%s, so the legs are %s and %s" % (eq, show_exact(x), show_exact(other)))


_WATER_ADDED_TO_DILUTE = re.compile(
    r"(?:how much water must be added to (?P<amt1>\d+(?:\.\d+)?) l of a (?P<p1>\d+(?:\.\d+)?)% salt solution to make it (?P<q1>\d+(?:\.\d+)?)% salt\?"
    r"|a (?P<amt2>\d+(?:\.\d+)?) l batch of (?P<p2>\d+(?:\.\d+)?)% juice concentrate is diluted with water to (?P<q2>\d+(?:\.\d+)?)% juice\. how much water is added\?)")


def water_added_to_dilute(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WATER_ADDED_TO_DILUTE.fullmatch(text)
    if match is None:
        return None
    if match.group("amt1") is not None:
        amt, p, q = Fraction(match.group("amt1")), Fraction(match.group("p1")), Fraction(match.group("q1"))
    else:
        amt, p, q = Fraction(match.group("amt2")), Fraction(match.group("p2")), Fraction(match.group("q2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [amt, p, q]:
        return None
    if amt <= 0 or p <= q or q < 0:
        return None
    old, new = p / 100, q / 100
    w = (old * amt - new * amt) / new
    if w <= 0:
        return None
    if old * amt != new * (amt + w):
        return None
    eq = "%s*%s = %s*(%s + w)" % (show(old), show(amt), show(new), show(amt))
    return Result("water_added_to_dilute", [w], eq, "%s, so w = %s" % (eq, show_exact(w)))


_PURE_ANTIFREEZE_ADDED = re.compile(
    r"how many liters of pure antifreeze must be added to (?P<amt>\d+(?:\.\d+)?) l of a (?P<p>\d+(?:\.\d+)?)% antifreeze mix to get a (?P<q>\d+(?:\.\d+)?)% mix\?")


def pure_antifreeze_added(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PURE_ANTIFREEZE_ADDED.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    amt = Fraction(match.group("amt"))
    p = Fraction(match.group("p"))
    q = Fraction(match.group("q"))
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [amt, p, q]:
        return None
    if amt <= 0 or p >= q or q >= 100:
        return None
    old, new = p / 100, q / 100
    x = (new * amt - old * amt) / (1 - new)
    if x <= 0:
        return None
    if old * amt + x != new * (amt + x):
        return None
    eq = "%s*%s + x = %s*(%s + x)" % (show(old), show(amt), show(new), show(amt))
    return Result("pure_antifreeze_added", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_SALT_WATER_EVAPORATES = re.compile(
    r"a (?P<amt>\d+(?:\.\d+)?) l tank of (?P<p>\d+(?:\.\d+)?)% salt water is left to evaporate until it is (?P<q>\d+(?:\.\d+)?)% salt\. how much water evaporates\?")


def salt_water_evaporates(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SALT_WATER_EVAPORATES.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    amt = Fraction(match.group("amt"))
    p = Fraction(match.group("p"))
    q = Fraction(match.group("q"))
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [amt, p, q]:
        return None
    if amt <= 0 or p >= q or q <= 0:
        return None
    old, new = p / 100, q / 100
    e = amt - (old * amt) / new
    if e <= 0 or e >= amt:
        return None
    if old * amt != new * (amt - e):
        return None
    eq = "%s*%s = %s*(%s - e)" % (show(old), show(amt), show(new), show(amt))
    return Result("salt_water_evaporates", [e], eq, "%s, so e = %s" % (eq, show_exact(e)))


_HANDSHAKE_OR_ROUND_ROBIN_COUNT = re.compile(
    r"(?:at a party everyone shook hands with everyone else exactly once, for (?P<h>\d+) handshakes\. how many people were there\?"
    r"|in a round-robin tournament each team plays every other team once, for (?P<g>\d+) games\. how many teams are there\?)")


def handshake_or_round_robin_count(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _HANDSHAKE_OR_ROUND_ROBIN_COUNT.fullmatch(text)
    if match is None:
        return None
    k = Fraction(match.group("h") or match.group("g"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != k:
        return None
    disc = 1 + 8 * k
    root = _isqrt_exact(int(disc)) if disc.denominator == 1 else None
    if root is None:
        return None
    n = (Fraction(1) + root) / 2
    if n <= 1 or n.denominator != 1:
        return None
    if n * (n - 1) / 2 != k:
        return None
    eq = "n(n - 1)/2 = %s" % show(k)
    return Result("handshake_or_round_robin_count", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_TRIANGLE_THREE_SIDES_PERIMETER = re.compile(
    r"(?:a triangle's second side is (?P<a>\d+(?:\.\d+)?) in longer than the first, and its third side is (?P<b>\d+(?:\.\d+)?) in less than twice the first\. if the perimeter is (?P<p1>\d+(?:\.\d+)?) in, how long is each side\?"
    r"|the sides of a triangle are x, x \+ (?P<c>\d+(?:\.\d+)?), and (?P<m>\d+)x [−\-] (?P<d>\d+(?:\.\d+)?) inches long\. the perimeter is (?P<p2>\d+(?:\.\d+)?) inches\. find each side\.)")


def triangle_three_sides_perimeter(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TRIANGLE_THREE_SIDES_PERIMETER.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    if match.group("a") is not None:
        a, b, p = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("p1"))
        if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [a, b, p]:
            return None
        # x + (x+a) + (2x - b) = p  => 4x + a - b = p
        x = (p - a + b) / 4
        sides = [x, x + a, 2 * x - b]
        eq = "x + (x + %s) + (2x − %s) = %s" % (show(a), show(b), show(p))
    else:
        c, m, d, p = Fraction(match.group("c")), Fraction(match.group("m")), Fraction(match.group("d")), Fraction(match.group("p2"))
        if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [c, m, d, p]:
            return None
        # x + (x+c) + (m x - d) = p
        x = (p - c + d) / (2 + m)
        sides = [x, x + c, m * x - d]
        eq = "x + (x + %s) + (%sx − %s) = %s" % (show(c), show(m), show(d), show(p))
    if any(s <= 0 for s in sides):
        return None
    if sum(sides) != (p if match.group("a") is not None else Fraction(match.group("p2"))):
        return None
    return Result("triangle_three_sides_perimeter", sides, eq, "%s, so the sides are %s, %s, %s" % (eq, show_exact(sides[0]), show_exact(sides[1]), show_exact(sides[2])))


_RECTANGLE_PERIMETER_LENGTH_MORE_WIDTH = re.compile(
    r"the perimeter of a rectangle is (?P<p>\d+(?:\.\d+)?) m and its length is (?P<d>\d+(?:\.\d+)?) m more than its width\. find the length and width\.")


def rectangle_perimeter_length_more_width(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RECTANGLE_PERIMETER_LENGTH_MORE_WIDTH.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    p = Fraction(match.group("p"))
    d = Fraction(match.group("d"))
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [p, d]:
        return None
    # 2(w+d) + 2w = p => 4w + 2d = p
    w = (p - 2 * d) / 4
    length = w + d
    if w <= 0 or length <= 0:
        return None
    if 2 * length + 2 * w != p:
        return None
    eq = "2(w + %s) + 2w = %s" % (show(d), show(p))
    return Result("rectangle_perimeter_length_more_width", [length, w], eq, "%s, so L = %s and w = %s" % (eq, show_exact(length), show_exact(w)))


_TWO_JOBS_SAME_COMMISSION_PAY = re.compile(
    r"job a pays \$(?P<a>\d+(?:\.\d+)?) a month plus (?P<pa>\d+(?:\.\d+)?)% commission\. "
    r"job b pays \$(?P<b>\d+(?:\.\d+)?) a month plus (?P<pb>\d+(?:\.\d+)?)% commission\. "
    r"at what monthly sales total do both pay the same\?")


def two_jobs_same_commission_pay(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_JOBS_SAME_COMMISSION_PAY.fullmatch(text)
    if match is None:
        return None
    numbers = digit_numbers(problem)
    a = Fraction(match.group("a"))
    pa = Fraction(match.group("pa"))
    b = Fraction(match.group("b"))
    pb = Fraction(match.group("pb"))
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, False, True, False]:
        return None
    if [num[0] for num in numbers] != [a, pa, b, pb]:
        return None
    ra, rb = pa / 100, pb / 100
    if ra == rb:
        return None
    s = (a - b) / (rb - ra)
    if s <= 0:
        return None
    if a + ra * s != b + rb * s:
        return None
    eq = "%s + %s*s = %s + %s*s" % (show(a), show(ra), show(b), show(rb))
    return Result("two_jobs_same_commission_pay", [s], eq, "%s, so s = %s" % (eq, show_exact(s)))


def _sqrt_frac(d):
    if d < 0:
        return None
    rn, rd = _isqrt_exact(d.numerator), _isqrt_exact(d.denominator)
    if rn is None or rd is None:
        return None
    return Fraction(rn, rd)


def _positive_quadratic(a, b, c):
    if a == 0:
        return None
    root = _sqrt_frac(b * b - 4 * a * c)
    if root is None:
        return None
    for sign in (1, -1):
        x = (-b + sign * root) / (2 * a)
        if x > 0 and a * x * x + b * x + c == 0:
            return x
    return None


_FORMULA_PERIMETER_SOLVE_WIDTH = re.compile(
    r"solve p = (?P<a>\d+)l \+ (?P<b>\d+)w for w when p = (?P<p>\d+(?:\.\d+)?) and l = (?P<l>\d+(?:\.\d+)?)\.")


def formula_perimeter_solve_width(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _FORMULA_PERIMETER_SOLVE_WIDTH.fullmatch(text)
    if match is None:
        return None
    a, b, p, length = (Fraction(match.group(k)) for k in ("a", "b", "p", "l"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, p, length]:
        return None
    if a <= 0 or b <= 0:
        return None
    w = (p - a * length) / b
    if w <= 0:
        return None
    if a * length + b * w != p:
        return None
    eq = "%s*%s + %s*w = %s" % (show(a), show(length), show(b), show(p))
    return Result("formula_perimeter_solve_width", [w], eq, "%s, so w = %s" % (eq, show_exact(w)))


_FAHRENHEIT_TWICE_CELSIUS = re.compile(
    r"at what celsius temperature is the fahrenheit reading exactly (?P<k>\d+(?:\.\d+)?) times the celsius reading\? "
    r"\(f = \((?P<n>\d+)/(?P<d>\d+)\)c \+ (?P<b>\d+)\)$")


def fahrenheit_twice_celsius(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _FAHRENHEIT_TWICE_CELSIUS.fullmatch(text)
    if match is None:
        return None
    k, n, d, b = (Fraction(match.group(g)) for g in ("k", "n", "d", "b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [k, n, d, b]:
        return None
    if d == 0:
        return None
    slope = n / d
    if k == slope:
        return None
    c = b / (k - slope)
    if (slope * c + b) != k * c:
        return None
    eq = "(%s/%s)c + %s = %s*c" % (show(n), show(d), show(b), show(k))
    return Result("fahrenheit_twice_celsius", [c], eq, "%s, so c = %s" % (eq, show_exact(c)))


_FAHRENHEIT_TO_CELSIUS = re.compile(
    r"using f = \((?P<n>\d+)/(?P<d>\d+)\)c \+ (?P<b>\d+), what celsius temperature equals (?P<f>\d+(?:\.\d+)?)°f\?")


def fahrenheit_to_celsius(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _FAHRENHEIT_TO_CELSIUS.fullmatch(text)
    if match is None:
        return None
    n, d, b, f = (Fraction(match.group(g)) for g in ("n", "d", "b", "f"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [n, d, b, f]:
        return None
    if n == 0 or d == 0:
        return None
    c = (f - b) * d / n
    if n / d * c + b != f:
        return None
    eq = "(%s/%s)c + %s = %s" % (show(n), show(d), show(b), show(f))
    return Result("fahrenheit_to_celsius", [c], eq, "%s, so c = %s" % (eq, show_exact(c)))


_RENTAL_CAR_DAYS_PLUS_MILES = re.compile(
    r"a rental car costs \$(?P<day>\d+(?:\.\d+)?) per day plus \$(?P<mile>\d+(?:\.\d+)?) per mile. "
    r"a (?P<days>\d+)-day rental cost \$(?P<total>\d+(?:\.\d+)?). how many miles were driven\?")


def rental_car_days_plus_miles(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RENTAL_CAR_DAYS_PLUS_MILES.fullmatch(text)
    if match is None:
        return None
    day, mile, days, total = (Fraction(match.group(g)) for g in ("day", "mile", "days", "total"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, True, False, True]:
        return None
    if [n[0] for n in numbers] != [day, mile, days, total]:
        return None
    if day <= 0 or mile <= 0 or days <= 0 or total <= day * days:
        return None
    miles = (total - day * days) / mile
    if miles <= 0 or miles.denominator != 1:
        return None
    if day * days + mile * miles != total:
        return None
    eq = "%s*%s + %s*m = %s" % (show(day), show(days), show(mile), show(total))
    return Result("rental_car_days_plus_miles", [miles], eq, "%s, so m = %s" % (eq, show_exact(miles)))


_ITEM_COUPON_WHEN_COUPON_EXCEEDS_PAID = re.compile(
    r"(?P<item>[a-z]+(?: [a-z]+){0,3}) cost \$(?P<price>\d+(?:\.\d+)?) each. "
    r"with a \$(?P<coupon>\d+(?:\.\d+)?) coupon, [a-z]+ paid \$(?P<paid>\d+(?:\.\d+)?). "
    r"how many (?P=item) were bought\?")


def item_coupon_when_coupon_exceeds_paid(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _ITEM_COUPON_WHEN_COUPON_EXCEEDS_PAID.fullmatch(text)
    if match is None:
        return None
    price, coupon, paid = Fraction(match.group("price")), Fraction(match.group("coupon")), Fraction(match.group("paid"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or not all(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [price, coupon, paid]:
        return None
    if price <= 0 or coupon <= 0 or paid < 0 or coupon <= paid:
        return None
    n = (paid + coupon) / price
    if n.denominator != 1 or n <= 0:
        return None
    if price * n - coupon != paid:
        return None
    eq = "%s*n - %s = %s" % (show(price), show(coupon), show(paid))
    return Result("item_coupon_when_coupon_exceeds_paid", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_SOUND_TRAVEL_TIME = re.compile(
    r"sound travels about (?P<v>\d+(?:\.\d+)?) m/s, so d = (?P<v2>\d+(?:\.\d+)?)t. "
    r"a storm is (?P<dist>\d+(?:\.\d+)?) m away. how many seconds after the lightning flash will the thunder be heard\?")


def sound_travel_time(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SOUND_TRAVEL_TIME.fullmatch(text)
    if match is None:
        return None
    v, v2, dist = Fraction(match.group("v")), Fraction(match.group("v2")), Fraction(match.group("dist"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [v, v2, dist]:
        return None
    if v <= 0 or v != v2 or dist <= 0:
        return None
    t = dist / v
    if t <= 0:
        return None
    if v * t != dist:
        return None
    eq = "%s*t = %s" % (show(v), show(dist))
    return Result("sound_travel_time", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_RAISED_PLUS_PER_ITEM_TO_GOAL = re.compile(
    r"a club has raised \$(?P<have>\d+(?:\.\d+)?) so far. at its car wash it charges \$(?P<rate>\d+(?:\.\d+)?) per car. "
    r"how many more cars must it sell to reach its \$(?P<goal>\d+(?:\.\d+)?) goal\?")


def raised_plus_per_item_to_goal(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RAISED_PLUS_PER_ITEM_TO_GOAL.fullmatch(text)
    if match is None:
        return None
    have, rate, goal = Fraction(match.group("have")), Fraction(match.group("rate")), Fraction(match.group("goal"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or not all(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [have, rate, goal]:
        return None
    if rate <= 0 or goal <= have:
        return None
    n = (goal - have) / rate
    if n <= 0 or n.denominator != 1:
        return None
    if have + rate * n != goal:
        return None
    eq = "%s + %s*n = %s" % (show(have), show(rate), show(goal))
    return Result("raised_plus_per_item_to_goal", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_LOSES_VALUE_EACH_YEAR = re.compile(
    r"a delivery van bought for \$(?P<start>\d+(?:\.\d+)?) loses \$(?P<loss>\d+(?:\.\d+)?) in value each year. "
    r"after how many years will it be worth \$(?P<end>\d+(?:\.\d+)?)\?")


def loses_value_each_year(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LOSES_VALUE_EACH_YEAR.fullmatch(text)
    if match is None:
        return None
    start, loss, end = Fraction(match.group("start")), Fraction(match.group("loss")), Fraction(match.group("end"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or not all(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [start, loss, end]:
        return None
    if loss <= 0 or start <= end:
        return None
    y = (start - end) / loss
    if y <= 0 or y.denominator != 1:
        return None
    if start - loss * y != end:
        return None
    eq = "%s - %s*y = %s" % (show(start), show(loss), show(end))
    return Result("loses_value_each_year", [y], eq, "%s, so y = %s" % (eq, show_exact(y)))


_PART_IS_PERCENT_OF_WHOLE = re.compile(
    r"(?P<part>\d+(?:\.\d+)?) is (?P<pct>\d+(?:\.\d+)?)% of what number\?")


def part_is_percent_of_whole(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PART_IS_PERCENT_OF_WHOLE.fullmatch(text)
    if match is None:
        return None
    part, pct = Fraction(match.group("part")), Fraction(match.group("pct"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [part, pct]:
        return None
    if pct <= 0:
        return None
    whole = part / (pct / 100)
    if whole <= 0:
        return None
    if (pct / 100) * whole != part:
        return None
    eq = "(%s/100)*x = %s" % (show(pct), show(part))
    return Result("part_is_percent_of_whole", [whole], eq, "%s, so x = %s" % (eq, show_exact(whole)))


_SPLIT_BILL_INCLUDING_TIP = re.compile(
    r"(?P<n>\d+) friends split a restaurant bill equally, including a (?P<tip>\d+(?:\.\d+)?)% tip. "
    r"each paid \$(?P<each>\d+(?:\.\d+)?). what was the bill before the tip\?")


def split_bill_including_tip(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SPLIT_BILL_INCLUDING_TIP.fullmatch(text)
    if match is None:
        return None
    n, tip, each = Fraction(match.group("n")), Fraction(match.group("tip")), Fraction(match.group("each"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [False, False, True] or [num[0] for num in numbers] != [n, tip, each]:
        return None
    if n <= 0 or n.denominator != 1 or tip < 0 or each <= 0:
        return None
    factor = 1 + tip / 100
    bill = n * each / factor
    if bill <= 0:
        return None
    if factor * bill / n != each:
        return None
    eq = "%s*(1 + %s/100)*b / %s = %s" % (show(n), show(tip), show(n), show(each))
    return Result("split_bill_including_tip", [bill], eq, "%s, so b = %s" % (eq, show_exact(bill)))


_PERCENT_BOYS_GIVEN_GIRLS = re.compile(
    r"(?P<p>\d+(?:\.\d+)?)% of the students in a club are boys. there are (?P<g>\d+) girls. how many students are in the club\?")


def percent_boys_given_girls(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PERCENT_BOYS_GIVEN_GIRLS.fullmatch(text)
    if match is None:
        return None
    p, g = Fraction(match.group("p")), Fraction(match.group("g"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [p, g]:
        return None
    if p < 0 or p >= 100 or g <= 0:
        return None
    club = g / ((100 - p) / 100)
    if club <= 0 or club.denominator != 1:
        return None
    if (100 - p) / 100 * club != g:
        return None
    eq = "((100 - %s)/100)*n = %s" % (show(p), show(g))
    return Result("percent_boys_given_girls", [club], eq, "%s, so n = %s" % (eq, show_exact(club)))


_PERCENT_UP_THEN_DOWN_ENDING = re.compile(
    r"a stock's price rose (?P<up>\d+(?:\.\d+)?)% one month and then fell (?P<down>\d+(?:\.\d+)?)% the next, "
    r"ending at \$(?P<end>\d+(?:\.\d+)?). what was the starting price\?")


def percent_up_then_down_ending(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PERCENT_UP_THEN_DOWN_ENDING.fullmatch(text)
    if match is None:
        return None
    up, down, end = Fraction(match.group("up")), Fraction(match.group("down")), Fraction(match.group("end"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [False, False, True] or [n[0] for n in numbers] != [up, down, end]:
        return None
    rise, fall = 1 + up / 100, 1 - down / 100
    if rise <= 0 or fall <= 0 or end <= 0:
        return None
    start = end / (rise * fall)
    if start <= 0:
        return None
    if rise * fall * start != end:
        return None
    eq = "s*(1 + %s/100)*(1 - %s/100) = %s" % (show(up), show(down), show(end))
    return Result("percent_up_then_down_ending", [start], eq, "%s, so s = %s" % (eq, show_exact(start)))


_WEEKLY_PAY_PLUS_PERCENT_OF_SALES = re.compile(
    r"a salesperson gets \$(?P<base>\d+(?:\.\d+)?) per week plus (?P<pct>\d+(?:\.\d+)?)% of everything they sell. "
    r"to earn \$(?P<pay>\d+(?:\.\d+)?) in a week, how much must they sell\?")


def weekly_pay_plus_percent_of_sales(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WEEKLY_PAY_PLUS_PERCENT_OF_SALES.fullmatch(text)
    if match is None:
        return None
    base, pct, pay = Fraction(match.group("base")), Fraction(match.group("pct")), Fraction(match.group("pay"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, False, True] or [n[0] for n in numbers] != [base, pct, pay]:
        return None
    if base < 0 or pct <= 0 or pay <= base:
        return None
    sales = (pay - base) / (pct / 100)
    if sales <= 0:
        return None
    if base + (pct / 100) * sales != pay:
        return None
    eq = "%s + %s*s = %s" % (show(base), show(pct / 100), show(pay))
    return Result("weekly_pay_plus_percent_of_sales", [sales], eq, "%s, so s = %s" % (eq, show_exact(sales)))


_SCALE_MODEL_FROM_REAL = re.compile(
    r"a model car is built at a (?P<a>\d+):(?P<b>\d+) scale. the real car is (?P<real>\d+(?:\.\d+)?) cm long. how long is the model\?")


def scale_model_from_real(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SCALE_MODEL_FROM_REAL.fullmatch(text)
    if match is None:
        return None
    a, b, real = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("real"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, real]:
        return None
    if a <= 0 or b <= 0 or real <= 0:
        return None
    model = real * a / b
    if model <= 0:
        return None
    if model / real != a / b:
        return None
    eq = "x/%s = %s/%s" % (show(real), show(a), show(b))
    return Result("scale_model_from_real", [model], eq, "%s, so x = %s" % (eq, show_exact(model)))


_MAP_SCALE_DISTANCE = re.compile(
    r"on a map, (?P<a>\d+(?:\.\d+)?) cm represents (?P<b>\d+(?:\.\d+)?) km. "
    r"two cities are (?P<d>\d+(?:\.\d+)?) km apart. how far apart are they on the map\?")


def map_scale_distance(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _MAP_SCALE_DISTANCE.fullmatch(text)
    if match is None:
        return None
    a, b, d = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("d"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, d]:
        return None
    if a <= 0 or b <= 0 or d <= 0:
        return None
    x = d * a / b
    if x <= 0:
        return None
    if x / a != d / b:
        return None
    eq = "x/%s = %s/%s" % (show(a), show(d), show(b))
    return Result("map_scale_distance", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_SIMILAR_SHADOWS_HEIGHT = re.compile(
    r"at noon a (?P<p>\d+(?:\.\d+)?) m post casts a (?P<ps>\d+(?:\.\d+)?) m shadow, "
    r"and a building nearby casts a (?P<bs>\d+(?:\.\d+)?) m shadow. how tall is the building\?")


def similar_shadows_height(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SIMILAR_SHADOWS_HEIGHT.fullmatch(text)
    if match is None:
        return None
    p, ps, bs = Fraction(match.group("p")), Fraction(match.group("ps")), Fraction(match.group("bs"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [p, ps, bs]:
        return None
    if p <= 0 or ps <= 0 or bs <= 0:
        return None
    h = p * bs / ps
    if h <= 0:
        return None
    if h / bs != p / ps:
        return None
    eq = "h/%s = %s/%s" % (show(bs), show(p), show(ps))
    return Result("similar_shadows_height", [h], eq, "%s, so h = %s" % (eq, show_exact(h)))


_SQUARE_MORE_THAN_TIMES_NUMBER = re.compile(
    r"the square of a positive number is (?P<c>\d+(?:\.\d+)?) more than (?P<k>\d+(?:\.\d+)?) times the number. find the number.")


def square_more_than_times_number(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SQUARE_MORE_THAN_TIMES_NUMBER.fullmatch(text)
    if match is None:
        return None
    c, k = Fraction(match.group("c")), Fraction(match.group("k"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [c, k]:
        return None
    x = _positive_quadratic(1, -k, -c)
    if x is None:
        return None
    if x * x != k * x + c:
        return None
    eq = "x² = %s*x + %s" % (show(k), show(c))
    return Result("square_more_than_times_number", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_CONSECUTIVE_SQUARES_SUM = re.compile(
    r"the sum of the squares of two consecutive positive integers is (?P<s>\d+(?:\.\d+)?). find the integers.")


def consecutive_squares_sum(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CONSECUTIVE_SQUARES_SUM.fullmatch(text)
    if match is None:
        return None
    s = Fraction(match.group("s"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != s:
        return None
    n = _positive_quadratic(2, 2, 1 - s)
    if n is None or n.denominator != 1:
        return None
    if n * n + (n + 1) * (n + 1) != s:
        return None
    eq = "n² + (n + 1)² = %s" % show(s)
    return Result("consecutive_squares_sum", [n, n + 1], eq, "%s, so n = %s and n + 1 = %s" % (eq, show_exact(n), show_exact(n + 1)))


_SQUARE_PLUS_TIMES_EQUALS = re.compile(
    r"the square of a positive number plus (?P<k>\d+(?:\.\d+)?) times the number equals (?P<c>\d+(?:\.\d+)?). find the number.")


def square_plus_times_equals(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SQUARE_PLUS_TIMES_EQUALS.fullmatch(text)
    if match is None:
        return None
    k, c = Fraction(match.group("k")), Fraction(match.group("c"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [k, c]:
        return None
    x = _positive_quadratic(1, k, -c)
    if x is None:
        return None
    if x * x + k * x != c:
        return None
    eq = "x² + %s*x = %s" % (show(k), show(c))
    return Result("square_plus_times_equals", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_POLYGON_DIAGONALS_TO_SIDES = re.compile(
    r"a polygon has (?P<diag>\d+) diagonals. using d = n\(n [−\-] (?P<k>\d+)\)/(?P<den>\d+), how many sides does it have\?")


def polygon_diagonals_to_sides(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _POLYGON_DIAGONALS_TO_SIDES.fullmatch(text)
    if match is None:
        return None
    diag, k, den = Fraction(match.group("diag")), Fraction(match.group("k")), Fraction(match.group("den"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [diag, k, den]:
        return None
    if den == 0:
        return None
    n = _positive_quadratic(1, -k, -den * diag)
    if n is None or n.denominator != 1 or n <= 2:
        return None
    if n * (n - k) / den != diag:
        return None
    eq = "n(n - %s)/%s = %s" % (show(k), show(den), show(diag))
    return Result("polygon_diagonals_to_sides", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_TRIANGULAR_SUM_FROM_ONE = re.compile(
    r"how many consecutive whole numbers, starting from (?P<start>\d+), must be added to get a sum of (?P<s>\d+)\? "
    r"\(use (?P<a>\d+) \+ (?P<b>\d+) \+ [.…]+ \+ n = n\(n \+ (?P<one>\d+)\)/(?P<two>\d+).\)")


def triangular_sum_from_one(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TRIANGULAR_SUM_FROM_ONE.fullmatch(text)
    if match is None:
        return None
    start, s, a, b, one, two = (Fraction(match.group(g)) for g in ("start", "s", "a", "b", "one", "two"))
    numbers = digit_numbers(problem)
    expected = [start, s, a, b, one, two]
    if len(numbers) != 6 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != expected:
        return None
    if start != 1 or a != 1 or b != 2 or one != 1 or two != 2 or s <= 0:
        return None
    n = _positive_quadratic(1, 1, -2 * s)
    if n is None or n.denominator != 1:
        return None
    if n * (n + 1) / 2 != s:
        return None
    eq = "n(n + 1)/2 = %s" % show(s)
    return Result("triangular_sum_from_one", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_ROPE_CUT_IN_RATIO = re.compile(
    r"a (?P<length>\d+(?:\.\d+)?) m rope is cut into two pieces in the ratio (?P<a>\d+):(?P<b>\d+). how long is each piece\?")


def rope_cut_in_ratio(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _ROPE_CUT_IN_RATIO.fullmatch(text)
    if match is None:
        return None
    length, a, b = Fraction(match.group("length")), Fraction(match.group("a")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [length, a, b]:
        return None
    if length <= 0 or a <= 0 or b <= 0:
        return None
    x, y = length * a / (a + b), length * b / (a + b)
    if x + y != length:
        return None
    eq = "x + y = %s; x/y = %s/%s" % (show(length), show(a), show(b))
    return Result("rope_cut_in_ratio", [x, y], eq, "%s, so the pieces are %s and %s" % (eq, show_exact(x), show_exact(y)))


_SAVINGS_JAR_WEEK_N = re.compile(
    r"a savings jar holds \$(?P<a>\d+(?:\.\d+)?) in week (?P<w0>\d+) and grows by \$(?P<d>\d+(?:\.\d+)?) each week. "
    r"in which week does it hold \$(?P<target>\d+(?:\.\d+)?)\?")


def savings_jar_week_n(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SAVINGS_JAR_WEEK_N.fullmatch(text)
    if match is None:
        return None
    a, w0, d, target = Fraction(match.group("a")), Fraction(match.group("w0")), Fraction(match.group("d")), Fraction(match.group("target"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, False, True, True] or [n[0] for n in numbers] != [a, w0, d, target]:
        return None
    if d == 0 or w0.denominator != 1:
        return None
    n = w0 + (target - a) / d
    if n.denominator != 1 or n < w0:
        return None
    if a + d * (n - w0) != target:
        return None
    eq = "%s + %s*(n - %s) = %s" % (show(a), show(d), show(w0), show(target))
    return Result("savings_jar_week_n", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_SPLIT_EQUAL_SIMPLE_INTEREST = re.compile(
    r"\$(?P<t>\d+(?:\.\d+)?) is split between two accounts paying (?P<r1>\d+(?:\.\d+)?)% and (?P<r2>\d+(?:\.\d+)?)% simple interest. "
    r"both accounts earn the same interest in a year. how much is in each\?")


def split_equal_simple_interest(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SPLIT_EQUAL_SIMPLE_INTEREST.fullmatch(text)
    if match is None:
        return None
    t, r1, r2 = Fraction(match.group("t")), Fraction(match.group("r1")), Fraction(match.group("r2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, False, False] or [n[0] for n in numbers] != [t, r1, r2]:
        return None
    if t <= 0 or r1 <= 0 or r2 <= 0 or r1 == r2:
        return None
    x = r2 * t / (r1 + r2)
    y = t - x
    if x <= 0 or y <= 0:
        return None
    if (r1 / 100) * x != (r2 / 100) * y:
        return None
    eq = "%s*x = %s*(%s - x)" % (show(r1 / 100), show(r2 / 100), show(t))
    return Result("split_equal_simple_interest", [x, y], eq, "%s, so x = %s and y = %s" % (eq, show_exact(x), show_exact(y)))


_SIMPLE_INTEREST_YEARS = re.compile(
    r"how many years will it take \$(?P<p>\d+(?:\.\d+)?) to earn \$(?P<i>\d+(?:\.\d+)?) in simple interest at (?P<r>\d+(?:\.\d+)?)% per year\?")


def simple_interest_years(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SIMPLE_INTEREST_YEARS.fullmatch(text)
    if match is None:
        return None
    p, i, r = Fraction(match.group("p")), Fraction(match.group("i")), Fraction(match.group("r"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, True, False] or [n[0] for n in numbers] != [p, i, r]:
        return None
    if p <= 0 or i <= 0 or r <= 0:
        return None
    years = i / (p * r / 100)
    if years <= 0:
        return None
    if p * (r / 100) * years != i:
        return None
    eq = "%s*(%s/100)*t = %s" % (show(p), show(r), show(i))
    return Result("simple_interest_years", [years], eq, "%s, so t = %s" % (eq, show_exact(years)))


def _least_int_greater(x):
    x = Fraction(x)
    if x.denominator == 1:
        return int(x) + 1
    if x > 0:
        return x.numerator // x.denominator + 1
    return int(x)


def _ceil_int(x):
    x = Fraction(x)
    if x.denominator == 1:
        return int(x)
    if x > 0:
        return x.numerator // x.denominator + 1
    return int(x)


_AGO_OLDER_WAS_TWICE = re.compile(
    r"(?P<a>[a-z]+) is (?P<d>\d+) years older than (?P<b>[a-z]+). "
    r"(?P<y>\d+) years ago, (?P=a) was twice as old as (?P=b). how old is each now\?")


def ago_older_was_twice(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _AGO_OLDER_WAS_TWICE.fullmatch(text)
    if match is None:
        return None
    d, y = Fraction(match.group("d")), Fraction(match.group("y"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, y]:
        return None
    younger = d + y
    older = younger + d
    if younger <= y or older <= y:
        return None
    if older - y != 2 * (younger - y):
        return None
    eq = "(x + %s) - %s = 2(x - %s)" % (show(d), show(y), show(y))
    return Result("ago_older_was_twice", [younger, older], eq, "%s, so %s is %s and %s is %s" % (eq, match.group("b"), show_exact(younger), match.group("a"), show_exact(older)))


_CLOCK_HANDS_TOGETHER = re.compile(
    r"at what time between (?P<h>\d+):00 and (?P<h2>\d+):00 are the hour and minute hands of a clock exactly together\?")


def clock_hands_together(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CLOCK_HANDS_TOGETHER.fullmatch(text)
    if match is None:
        return None
    h, h2 = Fraction(match.group("h")), Fraction(match.group("h2"))
    numbers = digit_numbers(problem)
    expected = [h, Fraction(0), h2, Fraction(0)]
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != expected:
        return None
    if h2 != h + 1 or h < 0 or h >= 12:
        return None
    minutes = 60 * h / 11
    if minutes < 0 or minutes >= 60:
        return None
    eq = "m = 60*%s/11" % show(h)
    return Result("clock_hands_together", [minutes], eq, "%s, so m = %s" % (eq, show_exact(minutes)))


_JAR_THREE_COINS = re.compile(
    r"a jar has quarters, dimes, and nickels worth \$(?P<worth>\d+(?:\.\d+)?). "
    r"there are (?P<more>\d+) more dimes than quarters and twice as many nickels as quarters. how many of each coin\?")


def jar_three_coins(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _JAR_THREE_COINS.fullmatch(text)
    if match is None:
        return None
    worth, more = Fraction(match.group("worth")), Fraction(match.group("more"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [True, False] or [n[0] for n in numbers] != [worth, more]:
        return None
    cents = worth * 100
    # 25q + 10(q+more) + 5(2q) = cents
    q = (cents - 10 * more) / 45
    if q <= 0 or q.denominator != 1:
        return None
    d, n = q + more, 2 * q
    if 25 * q + 10 * d + 5 * n != cents:
        return None
    eq = "25q + 10(q + %s) + 5(2q) = %s" % (show(more), show(cents))
    return Result("jar_three_coins", [q, d, n], eq, "%s, so q = %s, d = %s, n = %s" % (eq, show_exact(q), show_exact(d), show_exact(n)))


_AVERAGE_OF_CONSECUTIVE = re.compile(
    r"the average of (?P<k>\d+) consecutive integers is (?P<m>\d+(?:\.\d+)?). what is the smallest\?")


def average_of_consecutive(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _AVERAGE_OF_CONSECUTIVE.fullmatch(text)
    if match is None:
        return None
    k, m = Fraction(match.group("k")), Fraction(match.group("m"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [k, m]:
        return None
    if k < 2 or k.denominator != 1:
        return None
    smallest = m - (k - 1) / 2
    if smallest.denominator != 1:
        return None
    eq = "x + (x + 1) + ... + (x + %s) = %s*%s" % (show(k - 1), show(k), show(m))
    return Result("average_of_consecutive", [smallest], eq, "%s, so x = %s" % (eq, show_exact(smallest)))


_CONSECUTIVE_TIMES_SMALLEST_VS_LARGEST = re.compile(
    r"three consecutive integers are such that (?P<k>\d+) times the smallest is (?P<c>\d+) less than the largest. find the integers.")


def consecutive_times_smallest_vs_largest(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CONSECUTIVE_TIMES_SMALLEST_VS_LARGEST.fullmatch(text)
    if match is None:
        return None
    k, c = Fraction(match.group("k")), Fraction(match.group("c"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [k, c]:
        return None
    # k x = (x+2) - c
    if k == 1:
        return None
    x = (2 - c) / (k - 1)
    if x.denominator != 1:
        return None
    vals = [x, x + 1, x + 2]
    if k * x != vals[2] - c:
        return None
    eq = "%s*x = (x + 2) - %s" % (show(k), show(c))
    return Result("consecutive_times_smallest_vs_largest", vals, eq, "%s, so the integers are %s, %s, %s" % (eq, show_exact(vals[0]), show_exact(vals[1]), show_exact(vals[2])))


_PLANE_WITH_AND_AGAINST_WIND = re.compile(
    r"a plane flies (?P<d>\d+(?:\.\d+)?) miles with the wind in (?P<t1>\d+(?:\.\d+)?) hours. "
    r"flying back against the same wind takes (?P<t2>\d+(?:\.\d+)?) hours. "
    r"find the plane's speed in still air and the wind speed.")


def plane_with_and_against_wind(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PLANE_WITH_AND_AGAINST_WIND.fullmatch(text)
    if match is None:
        return None
    d, t1, t2 = Fraction(match.group("d")), Fraction(match.group("t1")), Fraction(match.group("t2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, t1, t2]:
        return None
    if t1 <= 0 or t2 <= 0 or t2 <= t1:
        return None
    down, up = d / t1, d / t2
    p, w = (down + up) / 2, (down - up) / 2
    if p <= 0 or w <= 0:
        return None
    eq = "(p + w)*%s = %s; (p - w)*%s = %s" % (show(t1), show(d), show(t2), show(d))
    return Result("plane_with_and_against_wind", [p, w], eq, "%s, so p = %s and w = %s" % (eq, show_exact(p), show_exact(w)))


_TWO_DIGIT_UNITS_TIMES_TENS = re.compile(
    r"in a two-digit number, the units digit is (?P<k>\d+) times the tens digit. "
    r"the number is (?P<more>\d+) more than the sum of its digits. find the number.")


def two_digit_units_times_tens(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_DIGIT_UNITS_TIMES_TENS.fullmatch(text)
    if match is None:
        return None
    k, more = Fraction(match.group("k")), Fraction(match.group("more"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [k, more]:
        return None
    # 10t + k t = t + k t + more  => 9t = more, t = more/9
    t = more / 9
    u = k * t
    if t.denominator != 1 or u.denominator != 1:
        return None
    t, u = int(t), int(u)
    if t < 1 or t > 9 or u < 0 or u > 9:
        return None
    n = 10 * t + u
    if n != t + u + more:
        return None
    eq = "10t + %s*t = t + %s*t + %s" % (show(k), show(k), show(more))
    return Result("two_digit_units_times_tens", [Fraction(n)], eq, "%s, so the number is %s" % (eq, show_exact(Fraction(n))))


_ROUND_TRIP_FASTER_RETURN = re.compile(
    r"a cyclist rides (?P<d>\d+(?:\.\d+)?) km to a town and returns (?P<faster>\d+(?:\.\d+)?) km/h faster. "
    r"the whole trip takes (?P<n>\d+)/(?P<den>\d+) hours. how fast was the outbound ride\?")


def round_trip_faster_return(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _ROUND_TRIP_FASTER_RETURN.fullmatch(text)
    if match is None:
        return None
    d, faster, n, den = (Fraction(match.group(g)) for g in ("d", "faster", "n", "den"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [d, faster, n, den]:
        return None
    t = n / den
    # d/v + d/(v+f) = t  => t v^2 + t f v - 2 d v - d f = 0 => t v^2 + (t f - 2d) v - d f = 0
    v = _positive_quadratic(t, t * faster - 2 * d, -d * faster)
    if v is None or v <= 0:
        return None
    if d / v + d / (v + faster) != t:
        return None
    eq = "%s/v + %s/(v + %s) = %s" % (show(d), show(d), show(faster), show(t))
    return Result("round_trip_faster_return", [v], eq, "%s, so v = %s" % (eq, show_exact(v)))


_DIOPHANTUS_LIFE_AGES = re.compile(
    r"a puzzle: a man spent 1/6 of his life as a boy, 1/12 more as a youth, and 1/7 more before marrying. "
    r"(?P<later>\d+) years later a son was born, who lived 1/2 as long as his father. "
    r"the father died (?P<after>\d+) years after the son. how long did the father live\?")


def diophantus_life_ages(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _DIOPHANTUS_LIFE_AGES.fullmatch(text)
    if match is None:
        return None
    later, after = Fraction(match.group("later")), Fraction(match.group("after"))
    numbers = digit_numbers(problem)
    expected = [Fraction(1), Fraction(6), Fraction(1), Fraction(12), Fraction(1), Fraction(7), later, Fraction(1), Fraction(2), after]
    if len(numbers) != 10 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != expected:
        return None
    # x/6 + x/12 + x/7 + later + x/2 + after = x
    used = Fraction(1, 6) + Fraction(1, 12) + Fraction(1, 7) + Fraction(1, 2)
    if used >= 1:
        return None
    x = (later + after) / (1 - used)
    if x <= 0:
        return None
    if used * x + later + after != x:
        return None
    eq = "x/6 + x/12 + x/7 + %s + x/2 + %s = x" % (show(later), show(after))
    return Result("diophantus_life_ages", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_EXTERIOR_EQUALS_REMOTE_INTERIORS = re.compile(
    r"an exterior angle of a triangle measures \((?P<a>\d+)x (?P<op1>[+\-]) (?P<c1>\d+)\)°. "
    r"the two remote interior angles measure \((?P<b>\d+)x (?P<op2>[+\-]) (?P<c2>\d+)\)° and \((?P<c>\d+)x (?P<op3>[+\-]) (?P<c3>\d+)\)°. "
    r"find x and the exterior angle.")


def _signed(op, c):
    return Fraction(c) if op == "+" else -Fraction(c)


def exterior_equals_remote_interiors(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _EXTERIOR_EQUALS_REMOTE_INTERIORS.fullmatch(text)
    if match is None:
        return None
    a, b, c = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("c"))
    k1, k2, k3 = _signed(match.group("op1"), match.group("c1")), _signed(match.group("op2"), match.group("c2")), _signed(match.group("op3"), match.group("c3"))
    numbers = digit_numbers(problem)
    expected = [a, abs(k1), b, abs(k2), c, abs(k3)]
    if len(numbers) != 6 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != expected:
        return None
    # a x + k1 = (b x + k2) + (c x + k3)
    left_a, right_a = a, b + c
    if left_a == right_a:
        return None
    x = (k2 + k3 - k1) / (left_a - right_a)
    ext = a * x + k1
    if ext <= 0:
        return None
    if ext != (b * x + k2) + (c * x + k3):
        return None
    eq = "%sx %s %s = (%sx %s %s) + (%sx %s %s)" % (
        show(a), "+" if k1 >= 0 else "−", show(abs(k1)),
        show(b), "+" if k2 >= 0 else "−", show(abs(k2)),
        show(c), "+" if k3 >= 0 else "−", show(abs(k3)))
    return Result("exterior_equals_remote_interiors", [x, ext], eq, "%s, so x = %s and the exterior is %s" % (eq, show_exact(x), show_exact(ext)))


_VERTICAL_ANGLES_LINEAR_PAIR_MEASURES = re.compile(
    r"two vertical angles measure \((?P<a>\d+)x (?P<op1>[+\-]) (?P<c1>\d+)\)° and \((?P<b>\d+)x (?P<op2>[+\-]) (?P<c2>\d+)\)°. "
    r"find x and the angle measure.")


def vertical_angles_linear_pair_measures(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _VERTICAL_ANGLES_LINEAR_PAIR_MEASURES.fullmatch(text)
    if match is None:
        return None
    a, b = Fraction(match.group("a")), Fraction(match.group("b"))
    k1, k2 = _signed(match.group("op1"), match.group("c1")), _signed(match.group("op2"), match.group("c2"))
    numbers = digit_numbers(problem)
    expected = [a, abs(k1), b, abs(k2)]
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != expected:
        return None
    if a == b:
        return None
    x = (k2 - k1) / (a - b)
    ang = a * x + k1
    if not (0 < ang <= 180) or ang != b * x + k2:
        return None
    eq = "%sx %s %s = %sx %s %s" % (show(a), "+" if k1 >= 0 else "−", show(abs(k1)), show(b), "+" if k2 >= 0 else "−", show(abs(k2)))
    return Result("vertical_angles_linear_pair_measures", [x, ang], eq, "%s, so x = %s and the angle is %s" % (eq, show_exact(x), show_exact(ang)))


_ISOSCELES_VERTEX_LESS_THAN_BASE = re.compile(
    r"in an isosceles triangle, the vertex angle is (?P<d>\d+)° less than each base angle. find all three angles.")


def isosceles_vertex_less_than_base(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _ISOSCELES_VERTEX_LESS_THAN_BASE.fullmatch(text)
    if match is None:
        return None
    d = Fraction(match.group("d"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != d:
        return None
    # 2b + (b - d) = 180
    b = (180 + d) / 3
    v = b - d
    if b <= 0 or v <= 0:
        return None
    if 2 * b + v != 180:
        return None
    eq = "2b + (b - %s) = 180" % show(d)
    return Result("isosceles_vertex_less_than_base", [b, b, v], eq, "%s, so the angles are %s, %s, %s" % (eq, show_exact(b), show_exact(b), show_exact(v)))


_SQUARE_SIDE_INCREASE_AREA = re.compile(
    r"if each side of a square is increased by (?P<d>\d+(?:\.\d+)?) cm, its area increases by (?P<a>\d+(?:\.\d+)?) cm². find the original side length.")


def square_side_increase_area(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SQUARE_SIDE_INCREASE_AREA.fullmatch(text)
    if match is None:
        return None
    d, a = Fraction(match.group("d")), Fraction(match.group("a"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, a]:
        return None
    # (s+d)^2 - s^2 = a => 2 s d + d^2 = a
    if d == 0:
        return None
    s = (a - d * d) / (2 * d)
    if s <= 0:
        return None
    if (s + d) * (s + d) - s * s != a:
        return None
    eq = "(s + %s)² - s² = %s" % (show(d), show(a))
    return Result("square_side_increase_area", [s], eq, "%s, so s = %s" % (eq, show_exact(s)))


_RECTANGLE_TWICE_WIDTH_AREA_SAME = re.compile(
    r"a rectangle's length is twice its width. if the length is decreased by (?P<dl>\d+(?:\.\d+)?) m and the width increased by (?P<dw>\d+(?:\.\d+)?) m, the area stays the same. find the original dimensions.")


def rectangle_twice_width_area_same(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RECTANGLE_TWICE_WIDTH_AREA_SAME.fullmatch(text)
    if match is None:
        return None
    dl, dw = Fraction(match.group("dl")), Fraction(match.group("dw"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [dl, dw]:
        return None
    # L=2W, (2W-dl)(W+dw)=2W^2 => 2W^2 + 2W dw - dl W - dl dw = 2W^2 => W(2 dw - dl) = dl dw
    coef = 2 * dw - dl
    if coef == 0:
        return None
    w = (dl * dw) / coef
    length = 2 * w
    if w <= 0 or length <= dl:
        return None
    if (length - dl) * (w + dw) != length * w:
        return None
    eq = "(2w - %s)(w + %s) = 2w²" % (show(dl), show(dw))
    return Result("rectangle_twice_width_area_same", [w, length], eq, "%s, so w = %s and L = %s" % (eq, show_exact(w), show_exact(length)))


_PEN_AGAINST_BARN_TWO_DIMENSIONS = re.compile(
    r"a farmer has (?P<p>\d+(?:\.\d+)?) m of fencing to build a rectangular pen against a barn wall \(no fence on the wall side\). "
    r"the pen must have an area of (?P<area>\d+(?:\.\d+)?) m². what dimensions work\?")


def pen_against_barn_two_dimensions(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PEN_AGAINST_BARN_TWO_DIMENSIONS.fullmatch(text)
    if match is None:
        return None
    p, area = Fraction(match.group("p")), Fraction(match.group("area"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [p, area]:
        return None
    # 2x + y = p, x y = area, y = p - 2x, x(p-2x)=area => 2x^2 - p x + area = 0
    x1 = _positive_quadratic(2, -p, area)
    if x1 is None:
        return None
    y1 = p - 2 * x1
    x2 = p / 2 - x1  # the other root of 2x^2 - p x + area: sum of roots = p/2
    y2 = p - 2 * x2
    pair1, pair2 = sorted([x1, y1]), sorted([x2, y2])
    if min(pair1) <= 0 or min(pair2) <= 0:
        return None
    vals = pair1 + pair2 if pair1 <= pair2 else pair2 + pair1
    eq = "2x + y = %s; x*y = %s" % (show(p), show(area))
    return Result("pen_against_barn_two_dimensions", vals, eq, "%s, so the dimensions are %s by %s or %s by %s" % (eq, show_exact(vals[0]), show_exact(vals[1]), show_exact(vals[2]), show_exact(vals[3])))


_OPEN_BOX_CUT_SQUARES = re.compile(
    r"squares of side x are cut from each corner of a (?P<l>\d+(?:\.\d+)?) cm by (?P<w>\d+(?:\.\d+)?) cm sheet, "
    r"and the sides are folded up to make an open box. the base of the box has area (?P<a>\d+(?:\.\d+)?) cm². find x.")


def open_box_cut_squares(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _OPEN_BOX_CUT_SQUARES.fullmatch(text)
    if match is None:
        return None
    l, w, a = Fraction(match.group("l")), Fraction(match.group("w")), Fraction(match.group("a"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [l, w, a]:
        return None
    # (l-2x)(w-2x)=a => 4x^2 - 2(l+w)x + l w - a = 0
    x = _positive_quadratic(4, -2 * (l + w), l * w - a)
    if x is None or 2 * x >= min(l, w):
        x2 = _positive_quadratic(4, -2 * (l + w), l * w - a)
        # pick the root that fits
        root = _sqrt_frac((2 * (l + w)) ** 2 - 16 * (l * w - a))
        if root is None:
            return None
        cands = [(-(-2 * (l + w)) + s * root) / 8 for s in (1, -1)]
        cands = [c for c in cands if c > 0 and 2 * c < min(l, w) and (l - 2 * c) * (w - 2 * c) == a]
        if len(cands) != 1:
            return None
        x = cands[0]
    if (l - 2 * x) * (w - 2 * x) != a:
        return None
    eq = "(%s - 2x)(%s - 2x) = %s" % (show(l), show(w), show(a))
    return Result("open_box_cut_squares", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_PATH_AROUND_SQUARE_GARDEN = re.compile(
    r"a (?P<s>\d+(?:\.\d+)?) ft by (?P<s2>\d+(?:\.\d+)?) ft garden has a path of uniform width around it. "
    r"the path's area is (?P<a>\d+(?:\.\d+)?) ft². how wide is the path\?")


def path_around_square_garden(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PATH_AROUND_SQUARE_GARDEN.fullmatch(text)
    if match is None:
        return None
    s, s2, a = Fraction(match.group("s")), Fraction(match.group("s2")), Fraction(match.group("a"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [s, s2, a]:
        return None
    if s != s2 or s <= 0 or a <= 0:
        return None
    # (s+2w)^2 - s^2 = a => 4w^2 + 4 s w - a = 0
    w = _positive_quadratic(4, 4 * s, -a)
    if w is None:
        return None
    if (s + 2 * w) * (s + 2 * w) - s * s != a:
        return None
    eq = "(%s + 2w)² - %s² = %s" % (show(s), show(s), show(a))
    return Result("path_around_square_garden", [w], eq, "%s, so w = %s" % (eq, show_exact(w)))


_AQUARIUM_VOLUME_DEPTH = re.compile(
    r"an aquarium (?P<l>\d+(?:\.\d+)?) dm long and (?P<w>\d+(?:\.\d+)?) dm wide holds (?P<v>\d+(?:\.\d+)?) dm³ of water when full. how deep is it\?")


def aquarium_volume_depth(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _AQUARIUM_VOLUME_DEPTH.fullmatch(text)
    if match is None:
        return None
    l, w, v = Fraction(match.group("l")), Fraction(match.group("w")), Fraction(match.group("v"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [l, w, v]:
        return None
    if l <= 0 or w <= 0:
        return None
    d = v / (l * w)
    if d <= 0:
        return None
    eq = "%s*%s*d = %s" % (show(l), show(w), show(v))
    return Result("aquarium_volume_depth", [d], eq, "%s, so d = %s" % (eq, show_exact(d)))


_FEWEST_MINUTES_PLAN_B_CHEAPER = re.compile(
    r"plan a costs \$(?P<a>\d+(?:\.\d+)?) plus \$(?P<ra>\d+(?:\.\d+)?) per minute. "
    r"plan b costs \$(?P<b>\d+(?:\.\d+)?) plus \$(?P<rb>\d+(?:\.\d+)?) per minute. "
    r"what is the fewest whole minutes for which plan b is cheaper\?")


def fewest_minutes_plan_b_cheaper(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _FEWEST_MINUTES_PLAN_B_CHEAPER.fullmatch(text)
    if match is None:
        return None
    a, ra, b, rb = (Fraction(match.group(g)) for g in ("a", "ra", "b", "rb"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or not all(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, ra, b, rb]:
        return None
    if ra <= rb or b <= a:
        return None
    # b + rb m < a + ra m => b - a < (ra - rb) m => m > (b-a)/(ra-rb)
    bound = (b - a) / (ra - rb)
    m = Fraction(_least_int_greater(bound))
    if b + rb * m >= a + ra * m:
        return None
    if m > 1 and b + rb * (m - 1) < a + ra * (m - 1):
        return None
    eq = "%s + %s*m < %s + %s*m" % (show(b), show(rb), show(a), show(ra))
    return Result("fewest_minutes_plan_b_cheaper", [m], eq, "%s, so the fewest whole minutes is %s" % (eq, show_exact(m)))


_GREATEST_WHOLE_GARDEN_WIDTH = re.compile(
    r"a rectangular garden is (?P<l>\d+(?:\.\d+)?) ft long, and there is at most (?P<p>\d+(?:\.\d+)?) ft of fencing. "
    r"what is the greatest whole-number width possible\?")


def greatest_whole_garden_width(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _GREATEST_WHOLE_GARDEN_WIDTH.fullmatch(text)
    if match is None:
        return None
    l, p = Fraction(match.group("l")), Fraction(match.group("p"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [l, p]:
        return None
    # 2(l + w) <= p => w <= p/2 - l
    bound = p / 2 - l
    if bound <= 0:
        return None
    w = Fraction(int(bound)) if bound.denominator == 1 else Fraction(bound.numerator // bound.denominator)
    if w <= 0 or 2 * (l + w) > p:
        return None
    if 2 * (l + w + 1) <= p:
        return None
    eq = "2(%s + w) <= %s" % (show(l), show(p))
    return Result("greatest_whole_garden_width", [w], eq, "%s, so the greatest whole width is %s" % (eq, show_exact(w)))


_LEAST_SALES_FOR_PAY_FLOOR = re.compile(
    r"a salesperson earns \$(?P<base>\d+(?:\.\d+)?) a week plus (?P<pct>\d+(?:\.\d+)?)% of sales. "
    r"what is the least \(whole-dollar\) amount of sales needed to earn at least \$(?P<need>\d+(?:\.\d+)?)\?")


def least_sales_for_pay_floor(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LEAST_SALES_FOR_PAY_FLOOR.fullmatch(text)
    if match is None:
        return None
    base, pct, need = Fraction(match.group("base")), Fraction(match.group("pct")), Fraction(match.group("need"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, False, True] or [n[0] for n in numbers] != [base, pct, need]:
        return None
    if pct <= 0 or need <= base:
        return None
    raw = (need - base) / (pct / 100)
    s = Fraction(_ceil_int(raw))
    if base + (pct / 100) * s < need:
        return None
    if s > 0 and base + (pct / 100) * (s - 1) >= need:
        return None
    eq = "%s + %s*s >= %s" % (show(base), show(pct / 100), show(need))
    return Result("least_sales_for_pay_floor", [s], eq, "%s, so the least whole-dollar sales is %s" % (eq, show_exact(s)))


_DRAIN_REPLACE_PURE_ANTIFREEZE = re.compile(
    r"a (?P<amt>\d+(?:\.\d+)?)-liter radiator holds a (?P<p>\d+(?:\.\d+)?)% antifreeze mix. "
    r"how much must be drained and replaced with pure antifreeze to raise it to (?P<q>\d+(?:\.\d+)?)%\?")


def drain_replace_pure_antifreeze(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _DRAIN_REPLACE_PURE_ANTIFREEZE.fullmatch(text)
    if match is None:
        return None
    amt, p, q = Fraction(match.group("amt")), Fraction(match.group("p")), Fraction(match.group("q"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [amt, p, q]:
        return None
    if amt <= 0 or not (0 <= p < q < 100):
        return None
    old, new = p / 100, q / 100
    # (amt - x)*old + x = new*amt
    x = (new * amt - old * amt) / (1 - old)
    if x <= 0 or x >= amt:
        return None
    if (amt - x) * old + x != new * amt:
        return None
    eq = "(%s - x)*%s + x = %s*%s" % (show(amt), show(old), show(new), show(amt))
    return Result("drain_replace_pure_antifreeze", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_THREE_NUMBERS_TIMES_AND_MORE = re.compile(
    r"the second of three numbers is (?P<k>\d+) times the first. the third is (?P<more>\d+) more than the second. their sum is (?P<s>\d+(?:\.\d+)?). find the numbers.")


def three_numbers_times_and_more(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _THREE_NUMBERS_TIMES_AND_MORE.fullmatch(text)
    if match is None:
        return None
    k, more, s = Fraction(match.group("k")), Fraction(match.group("more")), Fraction(match.group("s"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [k, more, s]:
        return None
    # x + k x + (k x + more) = s
    x = (s - more) / (1 + 2 * k)
    vals = [x, k * x, k * x + more]
    if sum(vals) != s:
        return None
    eq = "x + %s*x + (%s*x + %s) = %s" % (show(k), show(k), show(more), show(s))
    return Result("three_numbers_times_and_more", vals, eq, "%s, so the numbers are %s, %s, %s" % (eq, show_exact(vals[0]), show_exact(vals[1]), show_exact(vals[2])))


_FRACTION_ADD_TO_BOTH = re.compile(
    r"the denominator of a fraction is (?P<d>\d+) more than the numerator. "
    r"if (?P<add>\d+) is added to both, the fraction becomes (?P<n>\d+)/(?P<m>\d+). find the original fraction.")


def fraction_add_to_both(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _FRACTION_ADD_TO_BOTH.fullmatch(text)
    if match is None:
        return None
    d, add, n, m = (Fraction(match.group(g)) for g in ("d", "add", "n", "m"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [d, add, n, m]:
        return None
    if m == 0:
        return None
    # (x+add)/(x+d+add) = n/m
    # m(x+add) = n(x+d+add)
    if m == n:
        return None
    x = (n * (d + add) - m * add) / (m - n)
    den = x + d
    if (x + add) / (den + add) != n / m:
        return None
    eq = "(x + %s)/(x + %s + %s) = %s/%s" % (show(add), show(d), show(add), show(n), show(m))
    return Result("fraction_add_to_both", [x / den], eq, "%s, so the fraction is %s/%s" % (eq, show_exact(x), show_exact(den)))


_JOG_MINUS_CYCLE_TIME = re.compile(
    r"jogging a route at (?P<j>\d+(?:\.\d+)?) km/h takes (?P<n>\d+)/(?P<den>\d+) hours longer than cycling it at (?P<c>\d+(?:\.\d+)?) km/h. how long is the route\?")


def jog_minus_cycle_time(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _JOG_MINUS_CYCLE_TIME.fullmatch(text)
    if match is None:
        return None
    j, n, den, c = (Fraction(match.group(g)) for g in ("j", "n", "den", "c"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [j, n, den, c]:
        return None
    extra = n / den
    if j <= 0 or c <= 0 or j >= c:
        return None
    # d/j - d/c = extra
    d = extra / (1 / j - 1 / c)
    if d <= 0:
        return None
    if d / j - d / c != extra:
        return None
    eq = "d/%s - d/%s = %s" % (show(j), show(c), show(extra))
    return Result("jog_minus_cycle_time", [d], eq, "%s, so d = %s" % (eq, show_exact(d)))


_THREE_NUMBERS_PAIR_SUMS = re.compile(
    r"three numbers add up to (?P<s>\d+(?:\.\d+)?). the first plus the second is (?P<ab>\d+(?:\.\d+)?), and the second plus the third is (?P<bc>\d+(?:\.\d+)?). find all three.")


def three_numbers_pair_sums(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _THREE_NUMBERS_PAIR_SUMS.fullmatch(text)
    if match is None:
        return None
    s, ab, bc = Fraction(match.group("s")), Fraction(match.group("ab")), Fraction(match.group("bc"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [s, ab, bc]:
        return None
    z, x = s - ab, s - bc
    y = s - x - z
    if x + y != ab or y + z != bc:
        return None
    eq = "x + y + z = %s; x + y = %s; y + z = %s" % (show(s), show(ab), show(bc))
    return Result("three_numbers_pair_sums", [x, y, z], eq, "%s, so x = %s, y = %s, z = %s" % (eq, show_exact(x), show_exact(y), show_exact(z)))


_SPELLED_OLDER_AGE_SUM = re.compile(
    r"(?P<a>[a-z]+) is (?P<d>two|three|four|five|six|seven|eight|nine|ten) years older than her brother\. "
    r"together their ages total (?P<s>\d+)\. how old is (?P=a)\?")


def spelled_older_age_sum(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SPELLED_OLDER_AGE_SUM.fullmatch(text)
    if match is None:
        return None
    d, s = fr(match.group("d")), Fraction(match.group("s"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != s:
        return None
    older = (s + d) / 2
    younger = s - older
    if older <= 0 or younger <= 0 or older - younger != d:
        return None
    eq = "x + (x - %s) = %s" % (show(d), show(s))
    return Result("spelled_older_age_sum", [older], eq, "%s, so %s is %s" % (eq, match.group("a"), show_exact(older)))


_TIMES_AS_OLD_ADD_UP_TODAY = re.compile(
    r"(?P<a>[a-z]+) is (?P<k>\d+) times as old as (?P<b>[a-z]+)\. "
    r"in (?P<y>\d+) years their ages will add up to (?P<s>\d+)\. what are their ages today\?")


def times_as_old_add_up_today(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TIMES_AS_OLD_ADD_UP_TODAY.fullmatch(text)
    if match is None:
        return None
    if match.group("a") == match.group("b"):
        return None
    k, y, s = Fraction(match.group("k")), Fraction(match.group("y")), Fraction(match.group("s"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [k, y, s]:
        return None
    if k <= 1:
        return None
    younger = (s - 2 * y) / (k + 1)
    older = k * younger
    if younger <= 0 or older <= 0 or younger + y + older + y != s:
        return None
    eq = "(x + %s) + (%s*x + %s) = %s" % (show(y), show(k), show(y), show(s))
    return Result("times_as_old_add_up_today", [younger, older], eq, "%s, so x = %s and %s*x = %s" % (eq, show_exact(younger), show(k), show_exact(older)))


_RECTANGLE_TWICE_LONG_AROUND = re.compile(
    r"a rectangle is twice as long as it is wide and goes (?P<p>\d+(?:\.\d+)?) cm all the way round\. how wide is it\?")


def rectangle_twice_long_around(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RECTANGLE_TWICE_LONG_AROUND.fullmatch(text)
    if match is None:
        return None
    p = Fraction(match.group("p"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != p:
        return None
    w = p / 6
    if w <= 0:
        return None
    if 2 * (2 * w) + 2 * w != p:
        return None
    eq = "2*(2w) + 2w = %s" % show(p)
    return Result("rectangle_twice_long_around", [w], eq, "%s, so w = %s" % (eq, show_exact(w)))


_GARDEN_LENGTH_EXCEEDS_AREA = re.compile(
    r"a garden's length exceeds its width by (?P<d>\d+(?:\.\d+)?) m\. it covers (?P<a>\d+(?:\.\d+)?) square metres\. give the width\.")


def garden_length_exceeds_area(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _GARDEN_LENGTH_EXCEEDS_AREA.fullmatch(text)
    if match is None:
        return None
    d, a = Fraction(match.group("d")), Fraction(match.group("a"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, a]:
        return None
    w = _positive_quadratic(1, d, -a)
    if w is None:
        return None
    if w * (w + d) != a:
        return None
    eq = "w(w + %s) = %s" % (show(d), show(a))
    return Result("garden_length_exceeds_area", [w], eq, "%s, so w = %s" % (eq, show_exact(w)))


_TRIANGLE_ANGLES_IN_PROPORTION = re.compile(
    r"the three angles of a triangle are in proportion (?P<a>\d+) to (?P<b>\d+) to (?P<c>\d+)\. what is the biggest\?")


def triangle_angles_in_proportion(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TRIANGLE_ANGLES_IN_PROPORTION.fullmatch(text)
    if match is None:
        return None
    a, b, c = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("c"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, c]:
        return None
    parts = a + b + c
    if parts <= 0:
        return None
    biggest = 180 * max(a, b, c) / parts
    if biggest <= 0 or biggest >= 180:
        return None
    eq = "(%s/%s)*180" % (show(max(a, b, c)), show(parts))
    return Result("triangle_angles_in_proportion", [biggest], eq, "%s, so the biggest is %s" % (eq, show_exact(biggest)))


_TWO_ANGLES_SUM_ONE_MORE = re.compile(
    r"two angles add up to (?P<s>\d+) degrees and one is (?P<d>\d+) more than the other\. find them\.")


def two_angles_sum_one_more(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_ANGLES_SUM_ONE_MORE.fullmatch(text)
    if match is None:
        return None
    s, d = Fraction(match.group("s")), Fraction(match.group("d"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [s, d]:
        return None
    small = (s - d) / 2
    large = small + d
    if small <= 0 or large <= 0 or small + large != s:
        return None
    eq = "x + (x + %s) = %s" % (show(d), show(s))
    return Result("two_angles_sum_one_more", [small, large], eq, "%s, so the angles are %s and %s" % (eq, show_exact(small), show_exact(large)))


_LADDER_WALL_BASE_HEIGHT = re.compile(
    r"a (?P<h>\d+(?:\.\d+)?) m ladder rests against a wall with its base (?P<b>\d+(?:\.\d+)?) m out\. how high does it reach\?")


def ladder_wall_base_height(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LADDER_WALL_BASE_HEIGHT.fullmatch(text)
    if match is None:
        return None
    h, b = Fraction(match.group("h")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [h, b]:
        return None
    reach = _pyth_leg(h, b)
    if reach is None or reach <= 0:
        return None
    eq = "x² + %s² = %s²" % (show(b), show(h))
    return Result("ladder_wall_base_height", [reach], eq, "%s, so x = %s" % (eq, show_exact(reach)))


_LATER_SAME_TRACK_CATCH = re.compile(
    r"a slow train leaves at (?P<s>\d+(?:\.\d+)?) mph\. "
    r"(?P<h>two|three|four|five|six|seven|eight|nine|ten|\d+(?:\.\d+)?) hours later a fast train sets off after it on the same track at (?P<f>\d+(?:\.\d+)?) mph\. "
    r"how long until the fast one catches it\?")


def later_same_track_catch(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LATER_SAME_TRACK_CATCH.fullmatch(text)
    if match is None:
        return None
    s, h, f = Fraction(match.group("s")), fr(match.group("h")), Fraction(match.group("f"))
    numbers = digit_numbers(problem)
    expected = [s, f] if match.group("h") in _SMALL else [s, h, f]
    if [n[0] for n in numbers] != expected or any(flag for _v, flag, _s, _e in numbers):
        return None
    if f <= s or h <= 0:
        return None
    t = s * h / (f - s)
    if t <= 0:
        return None
    if s * (t + h) != f * t:
        return None
    eq = "%s*(t + %s) = %s*t" % (show(s), show(h), show(f))
    return Result("later_same_track_catch", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_TAP_AND_LEAK_FILL = re.compile(
    r"a tap fills a bath in (?P<f>\d+(?:\.\d+)?) minutes but the plug leaks and empties it in (?P<e>\d+(?:\.\d+)?) minutes\. "
    r"with both going, how long to fill it\?")


def tap_and_leak_fill(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TAP_AND_LEAK_FILL.fullmatch(text)
    if match is None:
        return None
    f, e = Fraction(match.group("f")), Fraction(match.group("e"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [f, e]:
        return None
    if e <= f or f <= 0:
        return None
    t = 1 / (1 / f - 1 / e)
    if t <= 0:
        return None
    eq = "1/%s - 1/%s = 1/t" % (show(f), show(e))
    return Result("tap_and_leak_fill", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_POUR_WATER_TO_DILUTE = re.compile(
    r"how much pure water should i pour into (?P<v>\d+(?:\.\d+)?) litres of (?P<p>\d+(?:\.\d+)?)% bleach solution to make it (?P<q>\d+(?:\.\d+)?)%\?")


def pour_water_to_dilute(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _POUR_WATER_TO_DILUTE.fullmatch(text)
    if match is None:
        return None
    v, p, q = Fraction(match.group("v")), Fraction(match.group("p")), Fraction(match.group("q"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [v, p, q]:
        return None
    if not (0 < q < p <= 100) or v <= 0:
        return None
    water = v * (p / q - 1)
    if water <= 0:
        return None
    if p * v != q * (v + water):
        return None
    eq = "%s*%s = %s*(%s + w)" % (show(p), show(v), show(q), show(v))
    return Result("pour_water_to_dilute", [water], eq, "%s, so w = %s" % (eq, show_exact(water)))


_N_IS_P_PERCENT_OF_WHICH = re.compile(
    r"(?P<n>\d+(?:\.\d+)?) is (?P<p>\d+(?:\.\d+)?) % of which number\?")


def n_is_p_percent_of_which(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _N_IS_P_PERCENT_OF_WHICH.fullmatch(text)
    if match is None:
        return None
    n, p = Fraction(match.group("n")), Fraction(match.group("p"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [n, p]:
        return None
    if p <= 0 or p >= 100:
        return None
    whole = n * 100 / p
    if whole <= 0:
        return None
    eq = "%s = (%s/100)*x" % (show(n), show(p))
    return Result("n_is_p_percent_of_which", [whole], eq, "%s, so x = %s" % (eq, show_exact(whole)))


_CAB_FLAG_PLUS_PER_MILE = re.compile(
    r"a cab costs \$(?P<f>\d+(?:\.\d+)?) to get in and \$(?P<r>\d+(?:\.\d+)?) every mile after\. i paid \$(?P<t>\d+(?:\.\d+)?)\. how far did i go\?")


def cab_flag_plus_per_mile(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CAB_FLAG_PLUS_PER_MILE.fullmatch(text)
    if match is None:
        return None
    f, r, t = Fraction(match.group("f")), Fraction(match.group("r")), Fraction(match.group("t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, True, True] or [n[0] for n in numbers] != [f, r, t]:
        return None
    if r <= 0 or t <= f:
        return None
    miles = (t - f) / r
    if miles <= 0:
        return None
    eq = "%s + %s*m = %s" % (show(f), show(r), show(t))
    return Result("cab_flag_plus_per_mile", [miles], eq, "%s, so m = %s" % (eq, show_exact(miles)))


_GYM_JOIN_VS_MONTHLY_EQUAL = re.compile(
    r"gym a: \$(?P<j>\d+(?:\.\d+)?) to join plus \$(?P<a>\d+(?:\.\d+)?) a month\. "
    r"gym b: no joining fee but \$(?P<b>\d+(?:\.\d+)?) a month\. after how many months do they cost the same\?")


def gym_join_vs_monthly_equal(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _GYM_JOIN_VS_MONTHLY_EQUAL.fullmatch(text)
    if match is None:
        return None
    j, a, b = Fraction(match.group("j")), Fraction(match.group("a")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, True, True] or [n[0] for n in numbers] != [j, a, b]:
        return None
    if b <= a or j <= 0:
        return None
    m = j / (b - a)
    if m <= 0:
        return None
    if j + a * m != b * m:
        return None
    eq = "%s + %s*m = %s*m" % (show(j), show(a), show(b))
    return Result("gym_join_vs_monthly_equal", [m], eq, "%s, so m = %s" % (eq, show_exact(m)))


_WORKERS_DAYS_INVERSE = re.compile(
    r"if (?P<a>\d+) workers take (?P<d>\d+(?:\.\d+)?) days to dig a ditch, how long would (?P<b>\d+) workers take\?")


def workers_days_inverse(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WORKERS_DAYS_INVERSE.fullmatch(text)
    if match is None:
        return None
    a, d, b = Fraction(match.group("a")), Fraction(match.group("d")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, d, b]:
        return None
    if a <= 0 or b <= 0 or d <= 0:
        return None
    t = a * d / b
    if t <= 0:
        return None
    eq = "%s*%s = %s*t" % (show(a), show(d), show(b))
    return Result("workers_days_inverse", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_THROWN_UP_FROM_GROUND = re.compile(
    r"a ball is thrown up at (?P<v>\d+(?:\.\d+)?) ft/s from the ground, h = -(?P<g>\d+(?:\.\d+)?)t² \+ (?P<v2>\d+(?:\.\d+)?)t\. when does it land\?")


def thrown_up_from_ground(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _THROWN_UP_FROM_GROUND.fullmatch(text)
    if match is None:
        return None
    v, g, v2 = Fraction(match.group("v")), Fraction(match.group("g")), Fraction(match.group("v2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [v, g, v2]:
        return None
    if v != v2 or g <= 0 or v <= 0:
        return None
    t = v / g
    if t <= 0:
        return None
    if -g * t * t + v * t != 0:
        return None
    eq = "-%s*t² + %s*t = 0" % (show(g), show(v))
    return Result("thrown_up_from_ground", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_TWO_DIGIT_SUM_SWAP_UP = re.compile(
    r"the digits of a two-digit number sum to (?P<s>\d+)\. swap them and the number goes up by (?P<d>\d+)\. what is the number\?")


def two_digit_sum_swap_up(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_DIGIT_SUM_SWAP_UP.fullmatch(text)
    if match is None:
        return None
    s, d = Fraction(match.group("s")), Fraction(match.group("d"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [s, d]:
        return None
    if d / 9 != d / 9 or (d / 9).denominator != 1:
        return None
    diff = d / 9
    tens = (s - diff) / 2
    units = s - tens
    if tens.denominator != 1 or units.denominator != 1:
        return None
    tens, units = int(tens), int(units)
    if tens < 1 or tens > 9 or units < 0 or units > 9 or tens + units != s:
        return None
    n = 10 * tens + units
    if 10 * units + tens != n + d:
        return None
    eq = "t + u = %s; 9(u - t) = %s" % (show(s), show(d))
    return Result("two_digit_sum_swap_up", [Fraction(n)], eq, "%s, so the number is %s" % (eq, show_exact(Fraction(n))))


_RIBBON_CUT_RATIO_SHORT = re.compile(
    r"a (?P<l>\d+(?:\.\d+)?) cm ribbon is cut so the pieces are in the ratio (?P<a>\d+) to (?P<b>\d+)\. how long is the short piece\?")


def ribbon_cut_ratio_short(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RIBBON_CUT_RATIO_SHORT.fullmatch(text)
    if match is None:
        return None
    length, a, b = Fraction(match.group("l")), Fraction(match.group("a")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [length, a, b]:
        return None
    if a <= 0 or b <= 0:
        return None
    short = length * min(a, b) / (a + b)
    if short <= 0 or short >= length:
        return None
    eq = "x = %s*%s/(%s + %s)" % (show(length), show(min(a, b)), show(a), show(b))
    return Result("ribbon_cut_ratio_short", [short], eq, "%s, so x = %s" % (eq, show_exact(short)))


_BUDGET_ENTRY_PLUS_RIDE_TICKETS = re.compile(
    r"you can spend no more than \$(?P<b>\d+(?:\.\d+)?)\. each ride ticket costs \$(?P<t>\d+(?:\.\d+)?) and entry is \$(?P<e>\d+(?:\.\d+)?)\. "
    r"what's the most ride tickets you can buy\?")


def budget_entry_plus_ride_tickets(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BUDGET_ENTRY_PLUS_RIDE_TICKETS.fullmatch(text)
    if match is None:
        return None
    b, t, e = Fraction(match.group("b")), Fraction(match.group("t")), Fraction(match.group("e"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, True, True] or [n[0] for n in numbers] != [b, t, e]:
        return None
    if t <= 0 or e < 0 or b <= e:
        return None
    n = (b - e) / t
    if n < 0 or n.denominator != 1:
        return None
    eq = "%s + %s*n ≤ %s" % (show(e), show(t), show(b))
    return Result("budget_entry_plus_ride_tickets", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_LOWEST_LAST_EXAM_TWO_KNOWN = re.compile(
    r"what is the lowest score i can get on my last exam and still average at least (?P<m>\d+(?:\.\d+)?), "
    r"if i have (?P<a>\d+(?:\.\d+)?) and (?P<b>\d+(?:\.\d+)?) so far\?")


def lowest_last_exam_two_known(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _LOWEST_LAST_EXAM_TWO_KNOWN.fullmatch(text)
    if match is None:
        return None
    m, a, b = Fraction(match.group("m")), Fraction(match.group("a")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [m, a, b]:
        return None
    x = 3 * m - a - b
    if x < 0:
        return None
    eq = "( %s + %s + x )/3 ≥ %s" % (show(a), show(b), show(m))
    return Result("lowest_last_exam_two_known", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_TWO_CANDLES_BURN_EQUAL = re.compile(
    r"a candle (?P<h1>\d+(?:\.\d+)?) cm tall burns (?P<r1>\d+(?:\.\d+)?) cm an hour; "
    r"another (?P<h2>\d+(?:\.\d+)?) cm tall burns (?P<r2>\d+(?:\.\d+)?) cm an hour\. when are they equally tall\?")


def two_candles_burn_equal(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_CANDLES_BURN_EQUAL.fullmatch(text)
    if match is None:
        return None
    h1, r1, h2, r2 = (Fraction(match.group(g)) for g in ("h1", "r1", "h2", "r2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [h1, r1, h2, r2]:
        return None
    if r1 == r2:
        return None
    t = (h1 - h2) / (r1 - r2)
    if t <= 0:
        return None
    if h1 - r1 * t != h2 - r2 * t:
        return None
    eq = "%s - %s*t = %s - %s*t" % (show(h1), show(r1), show(h2), show(r2))
    return Result("two_candles_burn_equal", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_FAHRENHEIT_GIVEN_FORMULA = re.compile(
    r"convert: what celsius temperature equals (?P<f>\d+(?:\.\d+)?) fahrenheit using f = (?P<n>\d+)/(?P<d>\d+) c \+ (?P<b>\d+)\?")


def fahrenheit_given_formula(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _FAHRENHEIT_GIVEN_FORMULA.fullmatch(text)
    if match is None:
        return None
    f, n, d, b = (Fraction(match.group(g)) for g in ("f", "n", "d", "b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [f, n, d, b]:
        return None
    if n / d != Fraction(9, 5) or b != 32:
        return None
    c = (f - b) * d / n
    eq = "%s = (%s/%s)*c + %s" % (show(f), show(n), show(d), show(b))
    return Result("fahrenheit_given_formula", [c], eq, "%s, so c = %s" % (eq, show_exact(c)))


_TRAINS_APART_TOWARD_MEET = re.compile(
    r"two trains are (?P<dist>\d+(?:\.\d+)?) miles apart and head toward each other at (?P<a>\d+(?:\.\d+)?) and (?P<b>\d+(?:\.\d+)?) mph\. when do they meet\?")


def trains_apart_toward_meet(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TRAINS_APART_TOWARD_MEET.fullmatch(text)
    if match is None:
        return None
    dist, a, b = Fraction(match.group("dist")), Fraction(match.group("a")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [dist, a, b]:
        return None
    if a <= 0 or b <= 0:
        return None
    t = dist / (a + b)
    if t <= 0:
        return None
    eq = "(%s + %s)*t = %s" % (show(a), show(b), show(dist))
    return Result("trains_apart_toward_meet", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_BEACH_ROUND_TRIP_TWO_SPEEDS = re.compile(
    r"i drove to the beach at (?P<a>\d+(?:\.\d+)?) mph and back at (?P<b>\d+(?:\.\d+)?) mph\. "
    r"the whole drive took (?P<t>\d+(?:\.\d+)?) hours\. how far is the beach\?")


def beach_round_trip_two_speeds(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BEACH_ROUND_TRIP_TWO_SPEEDS.fullmatch(text)
    if match is None:
        return None
    a, b, t = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, t]:
        return None
    if a <= 0 or b <= 0 or t <= 0:
        return None
    d = t / (1 / a + 1 / b)
    if d <= 0:
        return None
    if d / a + d / b != t:
        return None
    eq = "d/%s + d/%s = %s" % (show(a), show(b), show(t))
    return Result("beach_round_trip_two_speeds", [d], eq, "%s, so d = %s" % (eq, show_exact(d)))


_SALESPERSON_WEEK_PLUS_PERCENT = re.compile(
    r"a salesperson gets \$(?P<base>\d+(?:\.\d+)?) a week plus (?P<p>\d+(?:\.\d+)?)% of sales\. "
    r"last week they got \$(?P<pay>\d+(?:\.\d+)?)\. what were their sales\?")


def salesperson_week_plus_percent(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SALESPERSON_WEEK_PLUS_PERCENT.fullmatch(text)
    if match is None:
        return None
    base, p, pay = Fraction(match.group("base")), Fraction(match.group("p")), Fraction(match.group("pay"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, False, True] or [n[0] for n in numbers] != [base, p, pay]:
        return None
    if p <= 0 or pay <= base:
        return None
    sales = (pay - base) * 100 / p
    if sales <= 0:
        return None
    eq = "%s + (%s/100)*s = %s" % (show(base), show(p), show(pay))
    return Result("salesperson_week_plus_percent", [sales], eq, "%s, so s = %s" % (eq, show_exact(sales)))


_EVERY_TEAM_PLAYED_ONCE = re.compile(
    r"every team played every other team once and there were (?P<g>\d+) games\. how many teams\?")


def every_team_played_once(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _EVERY_TEAM_PLAYED_ONCE.fullmatch(text)
    if match is None:
        return None
    g = Fraction(match.group("g"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != g:
        return None
    n = _positive_quadratic(1, -1, -2 * g)
    if n is None or n.denominator != 1:
        return None
    if n * (n - 1) / 2 != g:
        return None
    eq = "n(n - 1)/2 = %s" % show(g)
    return Result("every_team_played_once", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_REGULAR_POLYGON_EACH_INTERIOR = re.compile(
    r"the angles inside a regular polygon are each (?P<a>\d+(?:\.\d+)?) degrees\. how many sides\?")


def regular_polygon_each_interior(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _REGULAR_POLYGON_EACH_INTERIOR.fullmatch(text)
    if match is None:
        return None
    a = Fraction(match.group("a"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != a:
        return None
    if a <= 0 or a >= 180:
        return None
    n = 360 / (180 - a)
    if n.denominator != 1 or n < 3:
        return None
    if (n - 2) * 180 / n != a:
        return None
    eq = "((n - 2)*180)/n = %s" % show(a)
    return Result("regular_polygon_each_interior", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_SEESAW_CHILD_OTHER_SIDE = re.compile(
    r"a seesaw balances when a (?P<w1>\d+(?:\.\d+)?) kg child sits (?P<d>\d+(?:\.\d+)?) m from the middle\. "
    r"where must a (?P<w2>\d+(?:\.\d+)?) kg child sit on the other side\?")


def seesaw_child_other_side(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SEESAW_CHILD_OTHER_SIDE.fullmatch(text)
    if match is None:
        return None
    w1, d, w2 = Fraction(match.group("w1")), Fraction(match.group("d")), Fraction(match.group("w2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [w1, d, w2]:
        return None
    if w1 <= 0 or w2 <= 0 or d <= 0:
        return None
    x = w1 * d / w2
    if x <= 0:
        return None
    if w1 * d != w2 * x:
        return None
    eq = "%s*%s = %s*x" % (show(w1), show(d), show(w2))
    return Result("seesaw_child_other_side", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_CLOCK_HANDS_LINE_UP_HOURS = re.compile(
    r"when do the hands of a clock line up between (?P<a>\d+) and (?P<b>\d+) o'clock\?")


def clock_hands_line_up_hours(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CLOCK_HANDS_LINE_UP_HOURS.fullmatch(text)
    if match is None:
        return None
    a, b = Fraction(match.group("a")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b]:
        return None
    if b != a + 1 or a < 1 or a > 10:
        return None
    minutes = 60 * a / 11
    if minutes < 0 or minutes >= 60:
        return None
    eq = "m = 60*%s/11" % show(a)
    return Result("clock_hands_line_up_hours", [minutes], eq, "%s, so m = %s" % (eq, show_exact(minutes)))


_PERCENT_BOYS_GIVEN_GIRLS_CLUB = re.compile(
    r"(?P<p>\d+(?:\.\d+)?)% of a club are boys and there are (?P<g>\d+) girls\. how many members\?")


def percent_boys_given_girls_club(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PERCENT_BOYS_GIVEN_GIRLS_CLUB.fullmatch(text)
    if match is None:
        return None
    p, g = Fraction(match.group("p")), Fraction(match.group("g"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [p, g]:
        return None
    if not (0 < p < 100) or g <= 0:
        return None
    n = g * 100 / (100 - p)
    if n <= 0:
        return None
    if (100 - p) * n / 100 != g:
        return None
    eq = "(100 - %s)/100 * n = %s" % (show(p), show(g))
    return Result("percent_boys_given_girls_club", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_SHOP_FIXED_MAKE_SELL_BREAK_EVEN = re.compile(
    r"a shop has fixed costs of \$(?P<f>\d+(?:\.\d+)?) a day\. each mug costs \$(?P<c>\d+(?:\.\d+)?) to make and sells for \$(?P<s>\d+(?:\.\d+)?)\. "
    r"how many mugs to break even\?")


def shop_fixed_make_sell_break_even(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SHOP_FIXED_MAKE_SELL_BREAK_EVEN.fullmatch(text)
    if match is None:
        return None
    f, c, s = Fraction(match.group("f")), Fraction(match.group("c")), Fraction(match.group("s"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, True, True] or [n[0] for n in numbers] != [f, c, s]:
        return None
    if s <= c or f <= 0:
        return None
    n = f / (s - c)
    if n <= 0:
        return None
    if (s - c) * n != f:
        return None
    eq = "(%s - %s)*n = %s" % (show(s), show(c), show(f))
    return Result("shop_fixed_make_sell_break_even", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_CAR_LOSES_VALUE_UNTIL = re.compile(
    r"a car worth \$(?P<v>\d+(?:\.\d+)?) loses \$(?P<r>\d+(?:\.\d+)?) of value per year\. when is it worth \$(?P<w>\d+(?:\.\d+)?)\?")


def car_loses_value_until(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CAR_LOSES_VALUE_UNTIL.fullmatch(text)
    if match is None:
        return None
    v, r, w = Fraction(match.group("v")), Fraction(match.group("r")), Fraction(match.group("w"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, True, True] or [n[0] for n in numbers] != [v, r, w]:
        return None
    if r <= 0 or w >= v:
        return None
    t = (v - w) / r
    if t <= 0:
        return None
    if v - r * t != w:
        return None
    eq = "%s - %s*t = %s" % (show(v), show(r), show(w))
    return Result("car_loses_value_until", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_TANK_QUARTER_ADD_THREE_QUARTERS = re.compile(
    r"a tank is a quarter full\. add (?P<v>\d+(?:\.\d+)?) litres and it's three quarters full\. how big is it\?")


def tank_quarter_add_three_quarters(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TANK_QUARTER_ADD_THREE_QUARTERS.fullmatch(text)
    if match is None:
        return None
    v = Fraction(match.group("v"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != v:
        return None
    n = 2 * v
    if n <= 0:
        return None
    if Fraction(1, 4) * n + v != Fraction(3, 4) * n:
        return None
    eq = "n/4 + %s = 3n/4" % show(v)
    return Result("tank_quarter_add_three_quarters", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_POLE_AND_TREE_SHADOWS = re.compile(
    r"a (?P<p>\d+(?:\.\d+)?) m tall pole casts a (?P<ps>\d+(?:\.\d+)?) m shadow, and a tree casts a (?P<ts>\d+(?:\.\d+)?) m shadow\. how tall is the tree\?")


def pole_and_tree_shadows(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _POLE_AND_TREE_SHADOWS.fullmatch(text)
    if match is None:
        return None
    p, ps, ts = Fraction(match.group("p")), Fraction(match.group("ps")), Fraction(match.group("ts"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [p, ps, ts]:
        return None
    if p <= 0 or ps <= 0 or ts <= 0:
        return None
    h = p * ts / ps
    if h <= 0:
        return None
    if p / ps != h / ts:
        return None
    eq = "%s/%s = h/%s" % (show(p), show(ps), show(ts))
    return Result("pole_and_tree_shadows", [h], eq, "%s, so h = %s" % (eq, show_exact(h)))


_MEAN_OF_FIVE_LISTED_FIFTH = re.compile(
    r"the mean of five numbers is (?P<m>\d+(?:\.\d+)?)\. four of them are (?P<a>\d+(?:\.\d+)?), (?P<b>\d+(?:\.\d+)?), (?P<c>\d+(?:\.\d+)?) and (?P<d>\d+(?:\.\d+)?)\. what is the fifth\?")


def mean_of_five_listed_fifth(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _MEAN_OF_FIVE_LISTED_FIFTH.fullmatch(text)
    if match is None:
        return None
    m, a, b, c, d = (Fraction(match.group(g)) for g in ("m", "a", "b", "c", "d"))
    numbers = digit_numbers(problem)
    if len(numbers) != 5 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [m, a, b, c, d]:
        return None
    x = 5 * m - (a + b + c + d)
    eq = "( %s + %s + %s + %s + x )/5 = %s" % (show(a), show(b), show(c), show(d), show(m))
    return Result("mean_of_five_listed_fifth", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_SQUARE_SIDE_GROW_AREA = re.compile(
    r"a square patio's side is increased by (?P<d>\d+(?:\.\d+)?) m and its area goes up by (?P<a>\d+(?:\.\d+)?) m²\. how long was each side\?")


def square_side_grow_area(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SQUARE_SIDE_GROW_AREA.fullmatch(text)
    if match is None:
        return None
    d, a = Fraction(match.group("d")), Fraction(match.group("a"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, a]:
        return None
    # (s+d)^2 - s^2 = a => 2 s d + d^2 = a
    if d <= 0:
        return None
    s = (a - d * d) / (2 * d)
    if s <= 0:
        return None
    if (s + d) * (s + d) - s * s != a:
        return None
    eq = "(s + %s)² - s² = %s" % (show(d), show(a))
    return Result("square_side_grow_area", [s], eq, "%s, so s = %s" % (eq, show_exact(s)))


_WEEKS_UNTIL_BIKE = re.compile(
    r"(?P<name>[a-z]+) has \$(?P<have>\d+(?:\.\d+)?) and saves \$(?P<save>\d+(?:\.\d+)?) a week to buy a \$(?P<cost>\d+(?:\.\d+)?) bike\. how many weeks\?")


def weeks_until_bike(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WEEKS_UNTIL_BIKE.fullmatch(text)
    if match is None:
        return None
    have, save, cost = Fraction(match.group("have")), Fraction(match.group("save")), Fraction(match.group("cost"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, True, True] or [n[0] for n in numbers] != [have, save, cost]:
        return None
    if save <= 0 or cost <= have:
        return None
    w = (cost - have) / save
    if w <= 0:
        return None
    if have + save * w != cost:
        return None
    eq = "%s + %s*w = %s" % (show(have), show(save), show(cost))
    return Result("weeks_until_bike", [w], eq, "%s, so w = %s" % (eq, show_exact(w)))


_STICK_BROKEN_TWO_RATIO = re.compile(
    r"a (?P<l>\d+(?:\.\d+)?) cm stick is broken into pieces in the ratio (?P<a>\d+):(?P<b>\d+)\. how long is each piece\?")


def stick_broken_two_ratio(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _STICK_BROKEN_TWO_RATIO.fullmatch(text)
    if match is None:
        return None
    length, a, b = Fraction(match.group("l")), Fraction(match.group("a")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [length, a, b]:
        return None
    if a <= 0 or b <= 0:
        return None
    x, y = length * a / (a + b), length * b / (a + b)
    if x + y != length:
        return None
    eq = "x/%s = y/%s = %s/(%s + %s)" % (show(a), show(b), show(length), show(a), show(b))
    return Result("stick_broken_two_ratio", [x, y], eq, "%s, so the pieces are %s and %s" % (eq, show_exact(x), show_exact(y)))


_PLUMBER_COME_OUT_PLUS_HOUR = re.compile(
    r"a plumber charges \$(?P<f>\d+(?:\.\d+)?) to come out plus \$(?P<r>\d+(?:\.\d+)?) an hour\. the bill was \$(?P<t>\d+(?:\.\d+)?)\. how many hours did they work\?")


def plumber_come_out_plus_hour(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PLUMBER_COME_OUT_PLUS_HOUR.fullmatch(text)
    if match is None:
        return None
    f, r, t = Fraction(match.group("f")), Fraction(match.group("r")), Fraction(match.group("t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, True, True] or [n[0] for n in numbers] != [f, r, t]:
        return None
    if r <= 0 or t <= f:
        return None
    h = (t - f) / r
    if h <= 0:
        return None
    eq = "%s + %s*h = %s" % (show(f), show(r), show(t))
    return Result("plumber_come_out_plus_hour", [h], eq, "%s, so h = %s" % (eq, show_exact(h)))


_TRIP_FASTER_SAME_DISTANCE = re.compile(
    r"at (?P<a>\d+(?:\.\d+)?) km/h a trip takes (?P<t>\d+(?:\.\d+)?) hours\. how long at (?P<b>\d+(?:\.\d+)?) km/h\?")


def trip_faster_same_distance(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TRIP_FASTER_SAME_DISTANCE.fullmatch(text)
    if match is None:
        return None
    a, t, b = Fraction(match.group("a")), Fraction(match.group("t")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, t, b]:
        return None
    if a <= 0 or b <= 0 or t <= 0:
        return None
    t2 = a * t / b
    if t2 <= 0:
        return None
    eq = "%s*%s = %s*t" % (show(a), show(t), show(b))
    return Result("trip_faster_same_distance", [t2], eq, "%s, so t = %s" % (eq, show_exact(t2)))


_NUMBER_SQUARE_PLUS_TIMES = re.compile(
    r"a number squared plus (?P<k>\d+) times the number equals (?P<n>\d+)\. what is the positive number\?")


def number_square_plus_times(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _NUMBER_SQUARE_PLUS_TIMES.fullmatch(text)
    if match is None:
        return None
    k, n = Fraction(match.group("k")), Fraction(match.group("n"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [k, n]:
        return None
    x = _positive_quadratic(1, k, -n)
    if x is None:
        return None
    if x * x + k * x != n:
        return None
    eq = "x² + %s*x = %s" % (show(k), show(n))
    return Result("number_square_plus_times", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_GRANDPA_OLDER_COMBINED = re.compile(
    r"(?P<a>[a-z]+) is (?P<d>\d+) years older than his grandson\. their combined age is (?P<s>\d+)\. how old is the grandson\?")


def grandpa_older_combined(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _GRANDPA_OLDER_COMBINED.fullmatch(text)
    if match is None:
        return None
    d, s = Fraction(match.group("d")), Fraction(match.group("s"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, s]:
        return None
    young = (s - d) / 2
    if young <= 0 or young + d + young != s:
        return None
    eq = "x + (x + %s) = %s" % (show(d), show(s))
    return Result("grandpa_older_combined", [young], eq, "%s, so x = %s" % (eq, show_exact(young)))


_CENTS_TWO_COINS_DIMES = re.compile(
    r"i've got a pile of (?P<a>\d+)-cent and (?P<b>\d+)-cent coins, (?P<n>\d+) in all, adding up to \$(?P<t>\d+(?:\.\d+)?)\. how many dimes are in there\?")


def cents_two_coins_dimes(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CENTS_TWO_COINS_DIMES.fullmatch(text)
    if match is None:
        return None
    a, b, n, t = (Fraction(match.group(g)) for g in ("a", "b", "n", "t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [False, False, False, True] or [num[0] for num in numbers] != [a, b, n, t]:
        return None
    if {a, b} != {5, 10}:
        return None
    counts = _two_counts(n, a, b, t * 100)
    if counts is None:
        return None
    dimes = counts[0] if a == 10 else counts[1]
    eq = "%s*x + %s*(%s - x) = %s" % (show(a), show(b), show(n), show(t * 100))
    return Result("cents_two_coins_dimes", [dimes], eq, "%s, so dimes = %s" % (eq, show_exact(dimes)))


_COOKIES_BROWNIES_COUNT = re.compile(
    r"our class sold cookies at \$(?P<a>\d+(?:\.\d+)?) and brownies at \$(?P<b>\d+(?:\.\d+)?)\. "
    r"we sold (?P<n>\d+) treats and made \$(?P<t>\d+(?:\.\d+)?)\. how many brownies did we sell\?")


def cookies_brownies_count(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _COOKIES_BROWNIES_COUNT.fullmatch(text)
    if match is None:
        return None
    a, b, n, t = (Fraction(match.group(g)) for g in ("a", "b", "n", "t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, True, False, True] or [num[0] for num in numbers] != [a, b, n, t]:
        return None
    counts = _two_counts(n, a, b, t)
    if counts is None:
        return None
    eq = "%s*c + %s*b = %s; c + b = %s" % (show(a), show(b), show(t), show(n))
    return Result("cookies_brownies_count", [counts[1]], eq, "%s, so brownies = %s" % (eq, show_exact(counts[1])))


_PENS_PENCILS_CENTS = re.compile(
    r"pens cost (?P<a>\d+) cents and pencils (?P<b>\d+) cents\. i bought (?P<n>\d+) items for \$(?P<t>\d+(?:\.\d+)?)\. how many pens\?")


def pens_pencils_cents(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PENS_PENCILS_CENTS.fullmatch(text)
    if match is None:
        return None
    a, b, n, t = (Fraction(match.group(g)) for g in ("a", "b", "n", "t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [False, False, False, True] or [num[0] for num in numbers] != [a, b, n, t]:
        return None
    counts = _two_counts(n, a, b, t * 100)
    if counts is None:
        return None
    eq = "%s*p + %s*(%s - p) = %s" % (show(a), show(b), show(n), show(t * 100))
    return Result("pens_pencils_cents", [counts[0]], eq, "%s, so pens = %s" % (eq, show_exact(counts[0])))


_MOTORBIKES_CARS_WHEELS = re.compile(
    r"a parking lot has motorbikes and cars, (?P<n>\d+) vehicles with (?P<w>\d+) wheels\. how many cars\?")


def motorbikes_cars_wheels(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _MOTORBIKES_CARS_WHEELS.fullmatch(text)
    if match is None:
        return None
    n, w = Fraction(match.group("n")), Fraction(match.group("w"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [n, w]:
        return None
    counts = _two_counts(n, 2, 4, w)
    if counts is None:
        return None
    eq = "2*m + 4*c = %s; m + c = %s" % (show(w), show(n))
    return Result("motorbikes_cars_wheels", [counts[1]], eq, "%s, so cars = %s" % (eq, show_exact(counts[1])))

_YARD_PERIMETER_LENGTH_MORE = re.compile(
    r"the perimeter of a rectangular yard is (?P<p>\d+(?:\.\d+)?) ft and the length is (?P<d>\d+(?:\.\d+)?) ft more than the width\. what are the dimensions\?")


def yard_perimeter_length_more(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _YARD_PERIMETER_LENGTH_MORE.fullmatch(text)
    if match is None:
        return None
    p, d = Fraction(match.group("p")), Fraction(match.group("d"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [p, d]:
        return None
    w = (p / 2 - d) / 2
    length = w + d
    if w <= 0 or length <= 0 or 2 * (w + length) != p:
        return None
    eq = "2(w + (w + %s)) = %s" % (show(d), show(p))
    return Result("yard_perimeter_length_more", [w, length], eq, "%s, so w = %s and l = %s" % (eq, show_exact(w), show_exact(length)))


_ISOSCELES_SIDES_LONGER_BASE = re.compile(
    r"an isosceles triangle's equal sides are each (?P<d>\d+(?:\.\d+)?) cm longer than its base, and the perimeter is (?P<p>\d+(?:\.\d+)?) cm\. find the base\.")


def isosceles_sides_longer_base(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _ISOSCELES_SIDES_LONGER_BASE.fullmatch(text)
    if match is None:
        return None
    d, p = Fraction(match.group("d")), Fraction(match.group("p"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, p]:
        return None
    b = (p - 2 * d) / 3
    if b <= 0 or 2 * (b + d) + b != p:
        return None
    eq = "2(b + %s) + b = %s" % (show(d), show(p))
    return Result("isosceles_sides_longer_base", [b], eq, "%s, so b = %s" % (eq, show_exact(b)))


_STRAIGHT_LINE_TWO_AX_C = re.compile(
    r"two angles on a straight line are \((?P<a1>\d+)x (?P<op1>[+\-]) (?P<c1>\d+)\)° and \((?P<a2>\d+)x (?P<op2>[+\-]) (?P<c2>\d+)\)°\. find x\.")


def straight_line_two_ax_c(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _STRAIGHT_LINE_TWO_AX_C.fullmatch(text)
    if match is None:
        return None
    a1, c1 = _ax_plus_c(match.group("a1"), match.group("op1"), match.group("c1"))
    a2, c2 = _ax_plus_c(match.group("a2"), match.group("op2"), match.group("c2"))
    numbers = digit_numbers(problem)
    raw = [Fraction(match.group(g)) for g in ("a1", "c1", "a2", "c2")]
    if len(numbers) != 4 or any(n[1] for n in numbers) or [n[0] for n in numbers] != raw:
        return None
    if a1 + a2 == 0:
        return None
    x = (180 - c1 - c2) / (a1 + a2)
    if a1 * x + c1 + a2 * x + c2 != 180:
        return None
    if not (0 < a1 * x + c1 < 180 and 0 < a2 * x + c2 < 180):
        return None
    eq = "(%sx %s %s) + (%sx %s %s) = 180" % (
        show(a1), "+" if c1 >= 0 else "−", show(abs(c1)),
        show(a2), "+" if c2 >= 0 else "−", show(abs(c2)))
    return Result("straight_line_two_ax_c", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_POLYGON_HAS_DIAGONALS = re.compile(
    r"how many diagonals\.\.\. no: a polygon has (?P<d>\d+) diagonals\. how many sides does it have\?")


def polygon_has_diagonals(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _POLYGON_HAS_DIAGONALS.fullmatch(text)
    if match is None:
        return None
    d = Fraction(match.group("d"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != d:
        return None
    n = _positive_quadratic(1, -3, -2 * d)
    if n is None or n.denominator != 1 or n < 3:
        return None
    if n * (n - 3) / 2 != d:
        return None
    eq = "n(n - 3)/2 = %s" % show(d)
    return Result("polygon_has_diagonals", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_KITE_STRING_HEIGHT = re.compile(
    r"a kite string is (?P<h>\d+(?:\.\d+)?) m long and the kite is directly above a point (?P<b>\d+(?:\.\d+)?) m away from the person\. how high is the kite\?")


def kite_string_height(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _KITE_STRING_HEIGHT.fullmatch(text)
    if match is None:
        return None
    h, b = Fraction(match.group("h")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [h, b]:
        return None
    reach = _pyth_leg(h, b)
    if reach is None:
        return None
    eq = "x² + %s² = %s²" % (show(b), show(h))
    return Result("kite_string_height", [reach], eq, "%s, so x = %s" % (eq, show_exact(reach)))


_PLANE_WIND_SPEED_ONLY = re.compile(
    r"a plane flies (?P<d>\d+(?:\.\d+)?) km with the wind in (?P<t1>\d+(?:\.\d+)?) hours and returns against the wind in (?P<t2>\d+(?:\.\d+)?) hours\. find the wind speed\.")


def plane_wind_speed_only(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PLANE_WIND_SPEED_ONLY.fullmatch(text)
    if match is None:
        return None
    d, t1, t2 = Fraction(match.group("d")), Fraction(match.group("t1")), Fraction(match.group("t2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, t1, t2]:
        return None
    if t1 <= 0 or t2 <= 0 or t1 == t2:
        return None
    w = (d / t1 - d / t2) / 2
    if w <= 0:
        return None
    eq = "(p + w)*%s = %s; (p - w)*%s = %s" % (show(t1), show(d), show(t2), show(d))
    return Result("plane_wind_speed_only", [w], eq, "%s, so w = %s" % (eq, show_exact(w)))


_TWO_GARDENERS_OTHER_ALONE = re.compile(
    r"working together, two gardeners weed a park in (?P<t>\d+(?:\.\d+)?) hours\. one alone would need (?P<a>\d+(?:\.\d+)?) hours\. how long would the other need alone\?")


def two_gardeners_other_alone(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_GARDENERS_OTHER_ALONE.fullmatch(text)
    if match is None:
        return None
    t, a = Fraction(match.group("t")), Fraction(match.group("a"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [t, a]:
        return None
    if t <= 0 or a <= t:
        return None
    x = t * a / (a - t)
    if x <= 0 or t / a + t / x != 1:
        return None
    eq = "%s/%s + %s/x = 1" % (show(t), show(a), show(t))
    return Result("two_gardeners_other_alone", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_BUCKET_DILUTED_WITH_WATER = re.compile(
    r"a (?P<v>\d+(?:\.\d+)?)-litre bucket of (?P<p>\d+(?:\.\d+)?)% paint thinner is diluted with water down to (?P<q>\d+(?:\.\d+)?)%\. how much water is added\?")


def bucket_diluted_with_water(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BUCKET_DILUTED_WITH_WATER.fullmatch(text)
    if match is None:
        return None
    v, p, q = Fraction(match.group("v")), Fraction(match.group("p")), Fraction(match.group("q"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [v, p, q]:
        return None
    if not (0 < q < p <= 100) or v <= 0:
        return None
    w = v * (p / q - 1)
    if w <= 0 or p * v != q * (v + w):
        return None
    eq = "%s*%s = %s*(%s + w)" % (show(p), show(v), show(q), show(v))
    return Result("bucket_diluted_with_water", [w], eq, "%s, so w = %s" % (eq, show_exact(w)))


_PHONE_PLANS_CENTS_EQUAL = re.compile(
    r"phone plan a is \$(?P<a>\d+(?:\.\d+)?) plus (?P<ca>\d+) cents a minute; plan b is \$(?P<b>\d+(?:\.\d+)?) plus (?P<cb>\d+) cents a minute\. at how many minutes are they equal\?")


def phone_plans_cents_equal(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PHONE_PLANS_CENTS_EQUAL.fullmatch(text)
    if match is None:
        return None
    a, ca, b, cb = (Fraction(match.group(g)) for g in ("a", "ca", "b", "cb"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, False, True, False] or [n[0] for n in numbers] != [a, ca, b, cb]:
        return None
    ra, rb = ca / 100, cb / 100
    if ra == rb:
        return None
    m = (b - a) / (ra - rb)
    if m <= 0 or a + ra * m != b + rb * m:
        return None
    eq = "%s + (%s/100)*m = %s + (%s/100)*m" % (show(a), show(ca), show(b), show(cb))
    return Result("phone_plans_cents_equal", [m], eq, "%s, so m = %s" % (eq, show_exact(m)))


_STONE_THROWN_UP_LAND = re.compile(
    r"a stone is dropped\.\.\. thrown upward at (?P<v>\d+(?:\.\d+)?) ft/s from ground level with h = -(?P<g>\d+(?:\.\d+)?)t² \+ (?P<v2>\d+(?:\.\d+)?)t\. when does it come back down\?")


def stone_thrown_up_land(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _STONE_THROWN_UP_LAND.fullmatch(text)
    if match is None:
        return None
    v, g, v2 = Fraction(match.group("v")), Fraction(match.group("g")), Fraction(match.group("v2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [v, g, v2]:
        return None
    if v != v2 or g <= 0 or v <= 0:
        return None
    t = v / g
    if t <= 0 or -g * t * t + v * t != 0:
        return None
    eq = "-%s*t² + %s*t = 0" % (show(g), show(v))
    return Result("stone_thrown_up_land", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_TWO_PLANTS_GROW_EQUAL = re.compile(
    r"two plants are (?P<h1>\d+(?:\.\d+)?) cm and (?P<h2>\d+(?:\.\d+)?) cm tall\. the first grows (?P<r1>\d+(?:\.\d+)?) cm per week and the second (?P<r2>\d+(?:\.\d+)?) cm per week\. when will they be the same height\?")


def two_plants_grow_equal(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_PLANTS_GROW_EQUAL.fullmatch(text)
    if match is None:
        return None
    h1, h2, r1, r2 = (Fraction(match.group(g)) for g in ("h1", "h2", "r1", "r2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [h1, h2, r1, r2]:
        return None
    if r1 == r2:
        return None
    t = (h2 - h1) / (r1 - r2)
    if t <= 0 or h1 + r1 * t != h2 + r2 * t:
        return None
    eq = "%s + %s*t = %s + %s*t" % (show(h1), show(r1), show(h2), show(r2))
    return Result("two_plants_grow_equal", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_BEADS_THREE_RATIO_BLUE = re.compile(
    r"red, white and blue beads are in the ratio (?P<a>\d+):(?P<b>\d+):(?P<c>\d+), with (?P<n>\d+) beads total\. how many blue beads\?")


def beads_three_ratio_blue(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BEADS_THREE_RATIO_BLUE.fullmatch(text)
    if match is None:
        return None
    a, b, c, n = (Fraction(match.group(g)) for g in ("a", "b", "c", "n"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [a, b, c, n]:
        return None
    parts = a + b + c
    if parts <= 0:
        return None
    blue = n * c / parts
    if blue <= 0 or blue > n:
        return None
    eq = "blue = %s*%s/(%s + %s + %s)" % (show(n), show(c), show(a), show(b), show(c))
    return Result("beads_three_ratio_blue", [blue], eq, "%s, so blue = %s" % (eq, show_exact(blue)))


_BLEND_FROM_TWO_POUND_PRICES = re.compile(
    r"a (?P<n>\d+(?:\.\d+)?) lb blend worth \$(?P<m>\d+(?:\.\d+)?) a pound is made from \$(?P<a>\d+(?:\.\d+)?) a pound coffee and \$(?P<b>\d+(?:\.\d+)?) a pound coffee\. how many pounds of each\?")


def blend_from_two_pound_prices(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BLEND_FROM_TWO_POUND_PRICES.fullmatch(text)
    if match is None:
        return None
    n, m, a, b = (Fraction(match.group(g)) for g in ("n", "m", "a", "b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [False, True, True, True] or [num[0] for num in numbers] != [n, m, a, b]:
        return None
    counts = _two_counts(n, a, b, m * n)
    if counts is None:
        return None
    eq = "%s*x + %s*(%s - x) = %s" % (show(a), show(b), show(n), show(m * n))
    return Result("blend_from_two_pound_prices", [counts[0], counts[1]], eq, "%s, so %s lb and %s lb" % (eq, show_exact(counts[0]), show_exact(counts[1])))


_MATH_SCORES_NEXT_AVERAGE = re.compile(
    r"my scores in math are (?P<a>\d+(?:\.\d+)?), (?P<b>\d+(?:\.\d+)?) and (?P<c>\d+(?:\.\d+)?)\. what score on the next exam brings my average up to (?P<m>\d+(?:\.\d+)?)\?")


def math_scores_next_average(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _MATH_SCORES_NEXT_AVERAGE.fullmatch(text)
    if match is None:
        return None
    a, b, c, m = (Fraction(match.group(g)) for g in ("a", "b", "c", "m"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, c, m]:
        return None
    x = 4 * m - (a + b + c)
    eq = "(%s + %s + %s + x)/4 = %s" % (show(a), show(b), show(c), show(m))
    return Result("math_scores_next_average", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_BARN_DUCKS_GOATS_HEADS_FEET = re.compile(
    r"a barn holds ducks and goats\. counting heads gives (?P<h>\d+) and counting feet gives (?P<f>\d+)\. how many ducks are there\?")


def barn_ducks_goats_heads_feet(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BARN_DUCKS_GOATS_HEADS_FEET.fullmatch(text)
    if match is None:
        return None
    h, f = Fraction(match.group("h")), Fraction(match.group("f"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [h, f]:
        return None
    counts = _two_counts(h, 2, 4, f)
    if counts is None:
        return None
    eq = "2*d + 4*g = %s; d + g = %s" % (show(f), show(h))
    return Result("barn_ducks_goats_heads_feet", [counts[0], counts[1]], eq, "%s, so ducks = %s and goats = %s" % (eq, show_exact(counts[0]), show_exact(counts[1])))


_CYCLIST_SPELLED_HOURS_CATCH = re.compile(
    r"a cyclist leaves home at (?P<s>\d+(?:\.\d+)?) mph\. (?P<h>two|three|four|five|six|seven|eight|nine|ten) hours later her friend follows on the same road at (?P<f>\d+(?:\.\d+)?) mph\. how long after her friend leaves until she is caught\?")


def cyclist_spelled_hours_catch(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CYCLIST_SPELLED_HOURS_CATCH.fullmatch(text)
    if match is None:
        return None
    s, h, f = Fraction(match.group("s")), fr(match.group("h")), Fraction(match.group("f"))
    numbers = digit_numbers(problem)
    if [n[0] for n in numbers] != [s, f] or any(flag for _v, flag, _s, _e in numbers):
        return None
    if f <= s or h <= 0:
        return None
    t = s * h / (f - s)
    if t <= 0 or s * (t + h) != f * t:
        return None
    eq = "%s*(t + %s) = %s*t" % (show(s), show(h), show(f))
    return Result("cyclist_spelled_hours_catch", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_WHOLE_NUMBERS_FOLLOW_PRODUCT = re.compile(
    r"two whole numbers that follow each other multiply to (?P<p>\d+)\. which numbers are they\?")


def whole_numbers_follow_product(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WHOLE_NUMBERS_FOLLOW_PRODUCT.fullmatch(text)
    if match is None:
        return None
    p = Fraction(match.group("p"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != p:
        return None
    x = _positive_quadratic(1, 1, -p)
    if x is None or x.denominator != 1:
        return None
    if x * (x + 1) != p:
        return None
    eq = "x(x + 1) = %s" % show(p)
    return Result("whole_numbers_follow_product", [x, x + 1], eq, "%s, so the numbers are %s and %s" % (eq, show_exact(x), show_exact(x + 1)))


_MOTORBOAT_STILL_WATER = re.compile(
    r"a motorboat goes (?P<d1>\d+(?:\.\d+)?) miles with the current in (?P<t1>\d+(?:\.\d+)?) hours and (?P<d2>\d+(?:\.\d+)?) miles against the current in (?P<t2>\d+(?:\.\d+)?) hours\. what is the speed of the boat in still water\?")


def motorboat_still_water(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _MOTORBOAT_STILL_WATER.fullmatch(text)
    if match is None:
        return None
    d1, t1, d2, t2 = (Fraction(match.group(g)) for g in ("d1", "t1", "d2", "t2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d1, t1, d2, t2]:
        return None
    if t1 <= 0 or t2 <= 0:
        return None
    still = (d1 / t1 + d2 / t2) / 2
    if still <= 0:
        return None
    eq = "(d/%s + u/%s)/2" % (show(t1), show(t2))
    return Result("motorboat_still_water", [still], eq, "%s, so still water is %s" % (eq, show_exact(still)))


_TWO_JARS_GROW_EQUAL = re.compile(
    r"savings jar a holds \$(?P<a>\d+(?:\.\d+)?) and grows by \$(?P<ra>\d+(?:\.\d+)?) a week\. jar b holds \$(?P<b>\d+(?:\.\d+)?) and grows by \$(?P<rb>\d+(?:\.\d+)?) a week\. after how many weeks are they equal\?")


def two_jars_grow_equal(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_JARS_GROW_EQUAL.fullmatch(text)
    if match is None:
        return None
    a, ra, b, rb = (Fraction(match.group(g)) for g in ("a", "ra", "b", "rb"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, True, True, True] or [n[0] for n in numbers] != [a, ra, b, rb]:
        return None
    if ra == rb:
        return None
    w = (b - a) / (ra - rb)
    if w <= 0 or a + ra * w != b + rb * w:
        return None
    eq = "%s + %s*w = %s + %s*w" % (show(a), show(ra), show(b), show(rb))
    return Result("two_jars_grow_equal", [w], eq, "%s, so w = %s" % (eq, show_exact(w)))


_CATERER_PLUS_PER_PERSON = re.compile(
    r"a caterer charges \$(?P<f>\d+(?:\.\d+)?) plus \$(?P<r>\d+(?:\.\d+)?) per person\. the invoice came to \$(?P<t>\d+(?:\.\d+)?)\. how many people ate\?")


def caterer_plus_per_person(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CATERER_PLUS_PER_PERSON.fullmatch(text)
    if match is None:
        return None
    f, r, t = Fraction(match.group("f")), Fraction(match.group("r")), Fraction(match.group("t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, True, True] or [n[0] for n in numbers] != [f, r, t]:
        return None
    if r <= 0 or t <= f:
        return None
    n = (t - f) / r
    if n <= 0:
        return None
    eq = "%s + %s*n = %s" % (show(f), show(r), show(t))
    return Result("caterer_plus_per_person", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_JUICE_ADDED_TO_CHEAPER = re.compile(
    r"how many liters of juice worth \$(?P<a>\d+(?:\.\d+)?) per liter must be added to (?P<v>\d+(?:\.\d+)?) liters of juice worth \$(?P<b>\d+(?:\.\d+)?) per liter to make a mix worth \$(?P<m>\d+(?:\.\d+)?) per liter\?")


def juice_added_to_cheaper(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _JUICE_ADDED_TO_CHEAPER.fullmatch(text)
    if match is None:
        return None
    a, v, b, m = (Fraction(match.group(g)) for g in ("a", "v", "b", "m"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, False, True, True] or [n[0] for n in numbers] != [a, v, b, m]:
        return None
    if a == m:
        return None
    x = v * (m - b) / (a - m)
    if x <= 0 or a * x + b * v != m * (x + v):
        return None
    eq = "%s*x + %s*%s = %s*(x + %s)" % (show(a), show(b), show(v), show(m), show(v))
    return Result("juice_added_to_cheaper", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_TRIANGLE_RATIO_EACH_ANGLE = re.compile(
    r"in a triangle the three angles are in the ratio (?P<a>\d+):(?P<b>\d+):(?P<c>\d+)\. find each angle\.")


def triangle_ratio_each_angle(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TRIANGLE_RATIO_EACH_ANGLE.fullmatch(text)
    if match is None:
        return None
    a, b, c = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("c"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, c]:
        return None
    parts = a + b + c
    if parts <= 0:
        return None
    vals = [180 * a / parts, 180 * b / parts, 180 * c / parts]
    if sum(vals) != 180:
        return None
    eq = "180*(%s:%s:%s)/%s" % (show(a), show(b), show(c), show(parts))
    return Result("triangle_ratio_each_angle", vals, eq, "%s, so the angles are %s, %s, %s" % (eq, show_exact(vals[0]), show_exact(vals[1]), show_exact(vals[2])))


_TIMES_AS_OLD_LATER_TWICE = re.compile(
    r"(?P<a>[a-z]+) is (?P<k>\d+) times as old as (?P<b>[a-z]+)\. in (?P<y>\d+) years, (?P=a) will be twice as old as (?P=b)\. how old is each now\?")


def times_as_old_later_twice(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TIMES_AS_OLD_LATER_TWICE.fullmatch(text)
    if match is None:
        return None
    if match.group("a") == match.group("b"):
        return None
    k, y = Fraction(match.group("k")), Fraction(match.group("y"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [k, y]:
        return None
    if k <= 2:
        return None
    young = y / (k - 2)
    older = k * young
    if young <= 0 or older <= 0 or older + y != 2 * (young + y):
        return None
    eq = "%s*x + %s = 2(x + %s)" % (show(k), show(y), show(y))
    return Result("times_as_old_later_twice", [young, older], eq, "%s, so x = %s and %s*x = %s" % (eq, show_exact(young), show(k), show_exact(older)))


_BUS_SPLIT_EQUAL_PER_PERSON = re.compile(
    r"a concert bus costs \$(?P<f>\d+(?:\.\d+)?) plus \$(?P<r>\d+(?:\.\d+)?) per ticket\. the bus is split equally and each person pays \$(?P<p>\d+(?:\.\d+)?) in total\. how many people\?")


def bus_split_equal_per_person(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BUS_SPLIT_EQUAL_PER_PERSON.fullmatch(text)
    if match is None:
        return None
    f, r, p = Fraction(match.group("f")), Fraction(match.group("r")), Fraction(match.group("p"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, True, True] or [n[0] for n in numbers] != [f, r, p]:
        return None
    if p <= r:
        return None
    n = f / (p - r)
    if n <= 0 or (f + r * n) / n != p:
        return None
    eq = "(%s + %s*n)/n = %s" % (show(f), show(r), show(p))
    return Result("bus_split_equal_per_person", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_TWO_FLOURS_POUNDS = re.compile(
    r"a bakery sold (?P<n>\d+(?:\.\d+)?) lb of two flours, one at \$(?P<a>\d+(?:\.\d+)?)/lb and one at \$(?P<b>\d+(?:\.\d+)?)/lb, for \$(?P<t>\d+(?:\.\d+)?)\. how many lb of each\?")


def two_flours_pounds(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_FLOURS_POUNDS.fullmatch(text)
    if match is None:
        return None
    n, a, b, t = (Fraction(match.group(g)) for g in ("n", "a", "b", "t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [False, True, True, True] or [num[0] for num in numbers] != [n, a, b, t]:
        return None
    counts = _two_counts(n, a, b, t)
    if counts is None:
        return None
    eq = "%s*x + %s*(%s - x) = %s" % (show(a), show(b), show(n), show(t))
    return Result("two_flours_pounds", [counts[0], counts[1]], eq, "%s, so %s lb and %s lb" % (eq, show_exact(counts[0]), show_exact(counts[1])))


_CLOUD_INCLUDED_GB_EXTRA = re.compile(
    r"a cloud plan costs \$(?P<base>\d+(?:\.\d+)?) a month and includes (?P<inc>\d+) gb\. every additional gb costs \$(?P<r>\d+(?:\.\d+)?)\. the total came to \$(?P<t>\d+(?:\.\d+)?)\. how many gb were stored\?")


def cloud_included_gb_extra(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CLOUD_INCLUDED_GB_EXTRA.fullmatch(text)
    if match is None:
        return None
    base, inc, r, t = (Fraction(match.group(g)) for g in ("base", "inc", "r", "t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, False, True, True] or [n[0] for n in numbers] != [base, inc, r, t]:
        return None
    if r <= 0 or t < base:
        return None
    extra = (t - base) / r
    total = inc + extra
    if extra < 0 or total <= 0:
        return None
    eq = "%s + %s*(g - %s) = %s" % (show(base), show(r), show(inc), show(t))
    return Result("cloud_included_gb_extra", [total], eq, "%s, so g = %s" % (eq, show_exact(total)))


_WINNER_PERCENT_MARGIN_VOTES = re.compile(
    r"in a race between two people, the winner received (?P<p>\d+(?:\.\d+)?)% of the votes and won by (?P<m>\d+) votes\. how many votes were cast\?")


def winner_percent_margin_votes(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WINNER_PERCENT_MARGIN_VOTES.fullmatch(text)
    if match is None:
        return None
    p, m = Fraction(match.group("p")), Fraction(match.group("m"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [p, m]:
        return None
    if p <= 50 or p >= 100:
        return None
    n = m * 100 / (2 * p - 100)
    if n <= 0:
        return None
    eq = "(2*%s/100 - 1)*n = %s" % (show(p), show(m))
    return Result("winner_percent_margin_votes", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_ALLOWANCE_PLUS_TASKS_MONTHS = re.compile(
    r"(?P<name>[a-z]+) gets \$(?P<base>\d+(?:\.\d+)?) allowance a month plus \$(?P<r>\d+(?:\.\d+)?) for each extra task\. for (?P<m>\d+) months the total was \$(?P<t>\d+(?:\.\d+)?)\. how many extra tasks were done\?")


def allowance_plus_tasks_months(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _ALLOWANCE_PLUS_TASKS_MONTHS.fullmatch(text)
    if match is None:
        return None
    base, r, m, t = (Fraction(match.group(g)) for g in ("base", "r", "m", "t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, True, False, True] or [n[0] for n in numbers] != [base, r, m, t]:
        return None
    if r <= 0 or m <= 0:
        return None
    tasks = (t - base * m) / r
    if tasks < 0:
        return None
    eq = "%s*%s + %s*k = %s" % (show(base), show(m), show(r), show(t))
    return Result("allowance_plus_tasks_months", [tasks], eq, "%s, so k = %s" % (eq, show_exact(tasks)))


_BOAT_COVERS_THEN_FARTHER = re.compile(
    r"a boat covers (?P<d>\d+(?:\.\d+)?) km in (?P<t>\d+(?:\.\d+)?) hours\. at this speed, how far does it go in (?P<t2>\d+(?:\.\d+)?) hours\?")


def boat_covers_then_farther(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BOAT_COVERS_THEN_FARTHER.fullmatch(text)
    if match is None:
        return None
    d, t, t2 = Fraction(match.group("d")), Fraction(match.group("t")), Fraction(match.group("t2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, t, t2]:
        return None
    if t <= 0 or t2 <= 0:
        return None
    d2 = d / t * t2
    eq = "d/%s = x/%s" % (show(t), show(t2))
    return Result("boat_covers_then_farther", [d2], eq, "%s, so x = %s" % (eq, show_exact(d2)))


_CATS_DOGS_RATIO_THEN_EQUAL = re.compile(
    r"the ratio of cats to dogs at a shelter is (?P<a>\d+):(?P<b>\d+)\. after (?P<more>\d+) more cats arrive, the ratio becomes 1:1\. how many animals were there originally\?")


def cats_dogs_ratio_then_equal(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CATS_DOGS_RATIO_THEN_EQUAL.fullmatch(text)
    if match is None:
        return None
    a, b, more = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("more"))
    numbers = digit_numbers(problem)
    if len(numbers) != 5 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, more, Fraction(1), Fraction(1)]:
        return None
    if a == b:
        return None
    k = more / (b - a)
    if k <= 0:
        return None
    orig = k * (a + b)
    if a * k + more != b * k:
        return None
    eq = "%s*k + %s = %s*k" % (show(a), show(more), show(b))
    return Result("cats_dogs_ratio_then_equal", [orig], eq, "%s, so original total = %s" % (eq, show_exact(orig)))


_PUMP_LITRES_IN_MINUTES = re.compile(
    r"a pump moves (?P<d>\d+(?:\.\d+)?) litres in (?P<t>\d+(?:\.\d+)?) minutes\. how many litres does it move in (?P<t2>\d+(?:\.\d+)?) minutes\?")


def pump_litres_in_minutes(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PUMP_LITRES_IN_MINUTES.fullmatch(text)
    if match is None:
        return None
    d, t, t2 = Fraction(match.group("d")), Fraction(match.group("t")), Fraction(match.group("t2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, t, t2]:
        return None
    if t <= 0 or t2 <= 0:
        return None
    d2 = d / t * t2
    eq = "%s/%s = x/%s" % (show(d), show(t), show(t2))
    return Result("pump_litres_in_minutes", [d2], eq, "%s, so x = %s" % (eq, show_exact(d2)))


_TWO_PIPES_AND_DRAIN_FILL = re.compile(
    r"pipe a fills a pool in (?P<a>\d+(?:\.\d+)?) hours, pipe b in (?P<b>\d+(?:\.\d+)?) hours, and a drain empties it in (?P<d>\d+(?:\.\d+)?) hours\. with everything open, how long does it take to fill the empty pool\?")


def two_pipes_and_drain_fill(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_PIPES_AND_DRAIN_FILL.fullmatch(text)
    if match is None:
        return None
    a, b, d = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("d"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, d]:
        return None
    rate = 1 / a + 1 / b - 1 / d
    if rate <= 0:
        return None
    t = 1 / rate
    if t <= 0:
        return None
    eq = "1/%s + 1/%s - 1/%s = 1/t" % (show(a), show(b), show(d))
    return Result("two_pipes_and_drain_fill", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_SPENT_PERCENT_HAD_LEFT = re.compile(
    r"(?P<name>[a-z]+) spent (?P<p>\d+(?:\.\d+)?)% of an allowance on games and had \$(?P<left>\d+(?:\.\d+)?) left\. how much was the allowance\?")


def spent_percent_had_left(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SPENT_PERCENT_HAD_LEFT.fullmatch(text)
    if match is None:
        return None
    p, left = Fraction(match.group("p")), Fraction(match.group("left"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [False, True] or [n[0] for n in numbers] != [p, left]:
        return None
    if not (0 < p < 100):
        return None
    n = left * 100 / (100 - p)
    if n <= 0:
        return None
    eq = "(100 - %s)/100 * n = %s" % (show(p), show(left))
    return Result("spent_percent_had_left", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_SPLIT_TWO_RATES_CD = re.compile(
    r"(?P<name>[a-z]+) splits \$(?P<p>\d+(?:\.\d+)?) between a savings account at (?P<r1>\d+(?:\.\d+)?)% and a cd at (?P<r2>\d+(?:\.\d+)?)%\. she earned \$(?P<i>\d+(?:\.\d+)?) in interest this year\. how much is in the cd\?")


def split_two_rates_cd(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SPLIT_TWO_RATES_CD.fullmatch(text)
    if match is None:
        return None
    p, r1, r2, i = (Fraction(match.group(g)) for g in ("p", "r1", "r2", "i"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, False, False, True] or [n[0] for n in numbers] != [p, r1, r2, i]:
        return None
    if r1 == r2:
        return None
    cd = (i * 100 - r1 * p) / (r2 - r1)
    sav = p - cd
    if cd <= 0 or sav <= 0:
        return None
    if r1 * sav / 100 + r2 * cd / 100 != i:
        return None
    eq = "(%s/100)*(%s - x) + (%s/100)*x = %s" % (show(r1), show(p), show(r2), show(i))
    return Result("split_two_rates_cd", [sav, cd], eq, "%s, so the CD holds %s" % (eq, show_exact(cd)))

_SUM_ONE_TWICE_OTHER = re.compile(
    r"the sum of two numbers is (?P<s>\d+(?:\.\d+)?) and one is twice the other\. find the numbers\.")


def sum_one_twice_other(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SUM_ONE_TWICE_OTHER.fullmatch(text)
    if match is None:
        return None
    s = Fraction(match.group("s"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != s:
        return None
    small = s / 3
    if small <= 0 or small + 2 * small != s:
        return None
    eq = "x + 2x = %s" % show(s)
    return Result("sum_one_twice_other", [small, 2 * small], eq, "%s, so the numbers are %s and %s" % (eq, show_exact(small), show_exact(2 * small)))


_NAMED_TOGETHER_ONE_ALONE = re.compile(
    r"(?P<a>[a-z]+) and (?P<b>[a-z]+) together mow a lawn in (?P<t>\d+(?:\.\d+)?) hours\. "
    r"(?P=a) alone takes (?P<k>\d+(?:\.\d+)?) hours\. how long would (?P=b) take alone\?")


def named_together_one_alone(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _NAMED_TOGETHER_ONE_ALONE.fullmatch(text)
    if match is None:
        return None
    if match.group("a") == match.group("b"):
        return None
    t, k = Fraction(match.group("t")), Fraction(match.group("k"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [t, k]:
        return None
    if t <= 0 or k <= t:
        return None
    x = t * k / (k - t)
    if x <= 0 or t / k + t / x != 1:
        return None
    eq = "%s/%s + %s/x = 1" % (show(t), show(k), show(t))
    return Result("named_together_one_alone", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_TAP_LEAK_TANK_FILL = re.compile(
    r"a tap fills a tank in (?P<f>\d+(?:\.\d+)?) hours but a leak empties it in (?P<e>\d+(?:\.\d+)?) hours\. how long to fill it with both going\?")


def tap_leak_tank_fill(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TAP_LEAK_TANK_FILL.fullmatch(text)
    if match is None:
        return None
    f, e = Fraction(match.group("f")), Fraction(match.group("e"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [f, e]:
        return None
    if e <= f or f <= 0:
        return None
    t = 1 / (1 / f - 1 / e)
    if t <= 0:
        return None
    eq = "1/%s - 1/%s = 1/t" % (show(f), show(e))
    return Result("tap_leak_tank_fill", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_WORKERS_DAYS_INVERSE_WALL = re.compile(
    r"if (?P<a>\d+) workers build a wall in (?P<d>\d+(?:\.\d+)?) days, how long would (?P<b>\d+) workers take\?")


def workers_days_inverse_wall(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WORKERS_DAYS_INVERSE_WALL.fullmatch(text)
    if match is None:
        return None
    a, d, b = Fraction(match.group("a")), Fraction(match.group("d")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, d, b]:
        return None
    if a <= 0 or b <= 0 or d <= 0:
        return None
    t = a * d / b
    eq = "%s*%s = %s*t" % (show(a), show(d), show(b))
    return Result("workers_days_inverse_wall", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_TWO_LEGS_HOW_FAR = re.compile(
    r"a car goes (?P<s1>\d+(?:\.\d+)?) mph for (?P<t1>\d+(?:\.\d+)?) hours then (?P<s2>\d+(?:\.\d+)?) mph for (?P<t2>\d+(?:\.\d+)?) hours\. how far does it go in all\?")


def two_legs_how_far(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_LEGS_HOW_FAR.fullmatch(text)
    if match is None:
        return None
    s1, t1, s2, t2 = (Fraction(match.group(g)) for g in ("s1", "t1", "s2", "t2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [s1, t1, s2, t2]:
        return None
    if min(s1, t1, s2, t2) <= 0:
        return None
    d = s1 * t1 + s2 * t2
    eq = "%s*%s + %s*%s" % (show(s1), show(t1), show(s2), show(t2))
    return Result("two_legs_how_far", [d], eq, "%s, so d = %s" % (eq, show_exact(d)))


_TICKETS_EACH_TOTAL = re.compile(
    r"tickets cost \$(?P<p>\d+(?:\.\d+)?) each\. how much do (?P<n>\d+) tickets cost\?")


def tickets_each_total(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TICKETS_EACH_TOTAL.fullmatch(text)
    if match is None:
        return None
    p, n = Fraction(match.group("p")), Fraction(match.group("n"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [True, False] or [num[0] for num in numbers] != [p, n]:
        return None
    if p <= 0 or n <= 0:
        return None
    eq = "%s*%s" % (show(p), show(n))
    return Result("tickets_each_total", [p * n], eq, "%s, so the cost is %s" % (eq, show_exact(p * n)))


_COFFEE_ADDED_TO_MAKE_BLEND = re.compile(
    r"how many pounds of \$(?P<a>\d+(?:\.\d+)?) a pound coffee must be added to (?P<v>\d+(?:\.\d+)?) lb of \$(?P<b>\d+(?:\.\d+)?) a pound coffee to make a blend worth \$(?P<m>\d+(?:\.\d+)?) a pound\?")


def coffee_added_to_make_blend(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _COFFEE_ADDED_TO_MAKE_BLEND.fullmatch(text)
    if match is None:
        return None
    a, v, b, m = (Fraction(match.group(g)) for g in ("a", "v", "b", "m"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, False, True, True] or [n[0] for n in numbers] != [a, v, b, m]:
        return None
    if a == m:
        return None
    x = v * (m - b) / (a - m)
    if x <= 0 or a * x + b * v != m * (x + v):
        return None
    eq = "%s*x + %s*%s = %s*(x + %s)" % (show(a), show(b), show(v), show(m), show(v))
    return Result("coffee_added_to_make_blend", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_WORKERS_PAINT_INVERSE_DAYS = re.compile(
    r"if (?P<a>\d+) workers paint a house in (?P<d>\d+(?:\.\d+)?) days, how many days for (?P<b>\d+) workers\?")


def workers_paint_inverse_days(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WORKERS_PAINT_INVERSE_DAYS.fullmatch(text)
    if match is None:
        return None
    a, d, b = Fraction(match.group("a")), Fraction(match.group("d")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, d, b]:
        return None
    if a <= 0 or b <= 0 or d <= 0:
        return None
    t = a * d / b
    eq = "%s*%s = %s*t" % (show(a), show(d), show(b))
    return Result("workers_paint_inverse_days", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_STICK_CUT_TIMES_OTHER = re.compile(
    r"a (?P<l>\d+(?:\.\d+)?) cm stick is cut into two pieces\. one piece is (?P<k>\d+) times the other\. how long is each piece\?")


def stick_cut_times_other(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _STICK_CUT_TIMES_OTHER.fullmatch(text)
    if match is None:
        return None
    length, k = Fraction(match.group("l")), Fraction(match.group("k"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [length, k]:
        return None
    if k <= 1:
        return None
    small = length / (k + 1)
    if small <= 0 or small + k * small != length:
        return None
    eq = "x + %s*x = %s" % (show(k), show(length))
    return Result("stick_cut_times_other", [small, k * small], eq, "%s, so the pieces are %s and %s" % (eq, show_exact(small), show_exact(k * small)))


_EACH_INTERIOR_REGULAR_POLYGON = re.compile(
    r"each interior angle of a regular polygon is (?P<a>\d+(?:\.\d+)?)°\. how many sides does it have\?")


def each_interior_regular_polygon(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _EACH_INTERIOR_REGULAR_POLYGON.fullmatch(text)
    if match is None:
        return None
    a = Fraction(match.group("a"))
    numbers = digit_numbers(problem)
    if len(numbers) != 1 or numbers[0][1] or numbers[0][0] != a:
        return None
    if a <= 0 or a >= 180:
        return None
    n = 360 / (180 - a)
    if n.denominator != 1 or n < 3 or (n - 2) * 180 / n != a:
        return None
    eq = "((n - 2)*180)/n = %s" % show(a)
    return Result("each_interior_regular_polygon", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_PEOPLE_DOGS_HEADS_LEGS = re.compile(
    r"there are (?P<h>\d+) heads and (?P<f>\d+) legs in a room with people and dogs\. how many dogs are there\?")


def people_dogs_heads_legs(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PEOPLE_DOGS_HEADS_LEGS.fullmatch(text)
    if match is None:
        return None
    h, f = Fraction(match.group("h")), Fraction(match.group("f"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [h, f]:
        return None
    counts = _two_counts(h, 2, 4, f)
    if counts is None:
        return None
    eq = "2*p + 4*d = %s; p + d = %s" % (show(f), show(h))
    return Result("people_dogs_heads_legs", [counts[1]], eq, "%s, so dogs = %s" % (eq, show_exact(counts[1])))


_OPPOSITE_HOW_FAR_AFTER = re.compile(
    r"two cars leave a town in opposite directions at (?P<a>\d+(?:\.\d+)?) km/h and (?P<b>\d+(?:\.\d+)?) km/h\. how far apart are they after (?P<t>\d+(?:\.\d+)?) hours\?")


def opposite_how_far_after(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _OPPOSITE_HOW_FAR_AFTER.fullmatch(text)
    if match is None:
        return None
    a, b, t = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, t]:
        return None
    if min(a, b, t) <= 0:
        return None
    d = (a + b) * t
    eq = "(%s + %s)*%s" % (show(a), show(b), show(t))
    return Result("opposite_how_far_after", [d], eq, "%s, so d = %s" % (eq, show_exact(d)))


_SIMPLE_INTEREST_YEARS_EARNED = re.compile(
    r"(?P<name>[a-z]+) invested \$(?P<p>\d+(?:\.\d+)?) at (?P<r>\d+(?:\.\d+)?)% and earned \$(?P<i>\d+(?:\.\d+)?) in interest\. for how many years\?")


def simple_interest_years_earned(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SIMPLE_INTEREST_YEARS_EARNED.fullmatch(text)
    if match is None:
        return None
    p, r, i = Fraction(match.group("p")), Fraction(match.group("r")), Fraction(match.group("i"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, False, True] or [n[0] for n in numbers] != [p, r, i]:
        return None
    if p <= 0 or r <= 0 or i <= 0:
        return None
    t = i * 100 / (p * r)
    if t <= 0:
        return None
    eq = "%s = %s*(%s/100)*t" % (show(i), show(p), show(r))
    return Result("simple_interest_years_earned", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_BANK_ONE_KNOWN_OTHER_AMOUNT = re.compile(
    r"a bank pays (?P<r1>\d+(?:\.\d+)?)% on \$(?P<p>\d+(?:\.\d+)?) and (?P<r2>\d+(?:\.\d+)?)% on another amount\. the total interest is \$(?P<i>\d+(?:\.\d+)?)\. how much is the other amount\?")


def bank_one_known_other_amount(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BANK_ONE_KNOWN_OTHER_AMOUNT.fullmatch(text)
    if match is None:
        return None
    r1, p, r2, i = (Fraction(match.group(g)) for g in ("r1", "p", "r2", "i"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [False, True, False, True] or [n[0] for n in numbers] != [r1, p, r2, i]:
        return None
    if r2 <= 0:
        return None
    x = (i * 100 - r1 * p) / r2
    if x <= 0:
        return None
    if r1 * p / 100 + r2 * x / 100 != i:
        return None
    eq = "(%s/100)*%s + (%s/100)*x = %s" % (show(r1), show(p), show(r2), show(i))
    return Result("bank_one_known_other_amount", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_SPLIT_EQUAL_INTEREST_TWO_RATES = re.compile(
    r"\$(?P<p>\d+(?:\.\d+)?) is split between two accounts paying (?P<r1>\d+(?:\.\d+)?)% and (?P<r2>\d+(?:\.\d+)?)%\. both accounts earn the same interest in a year\. how much is in each\?")


def split_equal_interest_two_rates(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SPLIT_EQUAL_INTEREST_TWO_RATES.fullmatch(text)
    if match is None:
        return None
    p, r1, r2 = Fraction(match.group("p")), Fraction(match.group("r1")), Fraction(match.group("r2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [True, False, False] or [n[0] for n in numbers] != [p, r1, r2]:
        return None
    if r1 <= 0 or r2 <= 0:
        return None
    x = r2 * p / (r1 + r2)
    y = p - x
    if x <= 0 or y <= 0 or r1 * x != r2 * y:
        return None
    eq = "(%s/100)*x = (%s/100)*(%s - x)" % (show(r1), show(r2), show(p))
    return Result("split_equal_interest_two_rates", [x, y], eq, "%s, so the amounts are %s and %s" % (eq, show_exact(x), show_exact(y)))


_PERCENT_USED_REMAIN_WHOLE = re.compile(
    r"after using (?P<p>\d+(?:\.\d+)?)% of the fuel in a tank, (?P<left>\d+(?:\.\d+)?) liters remain\. how much did the tank hold\?")


def percent_used_remain_whole(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PERCENT_USED_REMAIN_WHOLE.fullmatch(text)
    if match is None:
        return None
    p, left = Fraction(match.group("p")), Fraction(match.group("left"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [p, left]:
        return None
    if not (0 < p < 100) or left <= 0:
        return None
    n = left * 100 / (100 - p)
    if n <= 0:
        return None
    eq = "(100 - %s)/100 * n = %s" % (show(p), show(left))
    return Result("percent_used_remain_whole", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_WATER_ADDED_TO_SOLUTION = re.compile(
    r"how many liters of water must be added to (?P<v>\d+(?:\.\d+)?) liters of a (?P<p>\d+(?:\.\d+)?)% solution to make it (?P<q>\d+(?:\.\d+)?)%\?")


def water_added_to_solution(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _WATER_ADDED_TO_SOLUTION.fullmatch(text)
    if match is None:
        return None
    v, p, q = Fraction(match.group("v")), Fraction(match.group("p")), Fraction(match.group("q"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [v, p, q]:
        return None
    if not (0 < q < p <= 100) or v <= 0:
        return None
    w = v * (p / q - 1)
    if w <= 0 or p * v != q * (v + w):
        return None
    eq = "%s*%s = %s*(%s + w)" % (show(p), show(v), show(q), show(v))
    return Result("water_added_to_solution", [w], eq, "%s, so w = %s" % (eq, show_exact(w)))


_COMPLEMENTARY_LESS_THAN_TIMES = re.compile(
    r"two angles are complementary\. one angle is (?P<d>\d+) less than (?P<k>\d+) times the other\. find the larger angle\.")


def complementary_less_than_times(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _COMPLEMENTARY_LESS_THAN_TIMES.fullmatch(text)
    if match is None:
        return None
    d, k = Fraction(match.group("d")), Fraction(match.group("k"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, k]:
        return None
    if k <= 1:
        return None
    small = (90 + d) / (k + 1)
    large = k * small - d
    if small <= 0 or large <= 0 or small + large != 90:
        return None
    eq = "x + (%s*x - %s) = 90" % (show(k), show(d))
    return Result("complementary_less_than_times", [large], eq, "%s, so the larger is %s" % (eq, show_exact(large)))


_PHARMACIST_KNOWN_ML_TO_TOTAL = re.compile(
    r"a pharmacist mixes (?P<v>\d+(?:\.\d+)?) ml of a (?P<p>\d+(?:\.\d+)?)% solution with a (?P<q>\d+(?:\.\d+)?)% solution to get (?P<t>\d+(?:\.\d+)?) ml of a (?P<m>\d+(?:\.\d+)?)% solution\. how much of the (?P=q)% is used\?")


def pharmacist_known_ml_to_total(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PHARMACIST_KNOWN_ML_TO_TOTAL.fullmatch(text)
    if match is None:
        return None
    v, p, q, t, m = (Fraction(match.group(g)) for g in ("v", "p", "q", "t", "m"))
    numbers = digit_numbers(problem)
    expected = [v, p, q, t, m, q]
    if [n[0] for n in numbers] != expected or any(flag for _v, flag, _s, _e in numbers):
        return None
    x = t - v
    if x <= 0:
        return None
    if p * v + q * x != m * t:
        return None
    eq = "%s*%s + %s*x = %s*%s" % (show(p), show(v), show(q), show(m), show(t))
    return Result("pharmacist_known_ml_to_total", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_EQUAL_AMOUNTS_BLEND_PRICE = re.compile(
    r"tea at \$(?P<a>\d+(?:\.\d+)?) a pound and tea at \$(?P<b>\d+(?:\.\d+)?) a pound are mixed in equal amounts\. what is the price of the blend per pound\?")


def equal_amounts_blend_price(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _EQUAL_AMOUNTS_BLEND_PRICE.fullmatch(text)
    if match is None:
        return None
    a, b = Fraction(match.group("a")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [True, True] or [n[0] for n in numbers] != [a, b]:
        return None
    m = (a + b) / 2
    eq = "(%s + %s)/2" % (show(a), show(b))
    return Result("equal_amounts_blend_price", [m], eq, "%s, so the blend is %s" % (eq, show_exact(m)))


_TWO_INVESTMENTS_TOTAL_INTEREST = re.compile(
    r"two investments of \$(?P<a>\d+(?:\.\d+)?) and \$(?P<b>\d+(?:\.\d+)?) earn (?P<r1>\d+(?:\.\d+)?)% and (?P<r2>\d+(?:\.\d+)?)%\. what is the total interest\?")


def two_investments_total_interest(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_INVESTMENTS_TOTAL_INTEREST.fullmatch(text)
    if match is None:
        return None
    a, b, r1, r2 = (Fraction(match.group(g)) for g in ("a", "b", "r1", "r2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, True, False, False] or [n[0] for n in numbers] != [a, b, r1, r2]:
        return None
    i = a * r1 / 100 + b * r2 / 100
    eq = "%s*(%s/100) + %s*(%s/100)" % (show(a), show(r1), show(b), show(r2))
    return Result("two_investments_total_interest", [i], eq, "%s, so the interest is %s" % (eq, show_exact(i)))


_BILL_INCLUDES_FLAT_CHARGE = re.compile(
    r"a bill of \$(?P<t>\d+(?:\.\d+)?) includes a \$(?P<c>\d+(?:\.\d+)?) service charge\. what was it before the service charge\?")


def bill_includes_flat_charge(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BILL_INCLUDES_FLAT_CHARGE.fullmatch(text)
    if match is None:
        return None
    t, c = Fraction(match.group("t")), Fraction(match.group("c"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [True, True] or [n[0] for n in numbers] != [t, c]:
        return None
    if t <= c:
        return None
    eq = "x + %s = %s" % (show(c), show(t))
    return Result("bill_includes_flat_charge", [t - c], eq, "%s, so x = %s" % (eq, show_exact(t - c)))


_DISCOUNT_IN_DOLLARS_AFTER = re.compile(
    r"a shirt costs \$(?P<p>\d+(?:\.\d+)?) after a (?P<r>\d+(?:\.\d+)?)% discount\. what is the discount in dollars\?")


def discount_in_dollars_after(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _DISCOUNT_IN_DOLLARS_AFTER.fullmatch(text)
    if match is None:
        return None
    p, r = Fraction(match.group("p")), Fraction(match.group("r"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [True, False] or [n[0] for n in numbers] != [p, r]:
        return None
    if not (0 < r < 100):
        return None
    orig = p * 100 / (100 - r)
    disc = orig - p
    if disc <= 0:
        return None
    eq = "x*(1 - %s/100) = %s" % (show(r), show(p))
    return Result("discount_in_dollars_after", [disc], eq, "%s, so the discount is %s" % (eq, show_exact(disc)))


_SPELLED_COUNT_AFTER_PERCENT_ONE = re.compile(
    r"after a (?P<r>\d+(?:\.\d+)?)% discount, (?P<k>two|three|four|five|six|seven|eight|nine|ten) jackets cost \$(?P<t>\d+(?:\.\d+)?)\. what was the original price of one\?")


def spelled_count_after_percent_one(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SPELLED_COUNT_AFTER_PERCENT_ONE.fullmatch(text)
    if match is None:
        return None
    r, k, t = Fraction(match.group("r")), fr(match.group("k")), Fraction(match.group("t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [False, True] or [n[0] for n in numbers] != [r, t]:
        return None
    if not (0 < r < 100) or k <= 0:
        return None
    sale = t / k
    orig = sale * 100 / (100 - r)
    eq = "%s*x*(1 - %s/100) = %s" % (show(k), show(r), show(t))
    return Result("spelled_count_after_percent_one", [orig], eq, "%s, so one cost %s" % (eq, show_exact(orig)))


_SPELLED_COUNT_AFTER_RISE_ONE = re.compile(
    r"prices rose (?P<r>\d+(?:\.\d+)?)% and (?P<k>two|three|four|five|six|seven|eight|nine|ten) phones now cost \$(?P<t>\d+(?:\.\d+)?)\. what did one cost before\?")


def spelled_count_after_rise_one(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SPELLED_COUNT_AFTER_RISE_ONE.fullmatch(text)
    if match is None:
        return None
    r, k, t = Fraction(match.group("r")), fr(match.group("k")), Fraction(match.group("t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [False, True] or [n[0] for n in numbers] != [r, t]:
        return None
    if r <= 0 or k <= 0:
        return None
    now = t / k
    orig = now * 100 / (100 + r)
    eq = "%s*x*(1 + %s/100) = %s" % (show(k), show(r), show(t))
    return Result("spelled_count_after_rise_one", [orig], eq, "%s, so one cost %s" % (eq, show_exact(orig)))


_TOWARD_MEET_DISTANCE_FROM_FIRST = re.compile(
    r"two friends are (?P<d>\d+(?:\.\d+)?) miles apart and bike toward each other at (?P<a>\d+(?:\.\d+)?) mph and (?P<b>\d+(?:\.\d+)?) mph\. how far from the first friend's start do they meet\?")


def toward_meet_distance_from_first(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TOWARD_MEET_DISTANCE_FROM_FIRST.fullmatch(text)
    if match is None:
        return None
    d, a, b = Fraction(match.group("d")), Fraction(match.group("a")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, a, b]:
        return None
    if min(d, a, b) <= 0:
        return None
    x = d * a / (a + b)
    if x <= 0 or x >= d:
        return None
    eq = "x/%s = (%s - x)/%s" % (show(a), show(d), show(b))
    return Result("toward_meet_distance_from_first", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_BUDGET_TICKETS_LEFT = re.compile(
    r"you have \$(?P<b>\d+(?:\.\d+)?)\. a movie costs \$(?P<p>\d+(?:\.\d+)?) per ticket\. how much money is left after buying as many tickets as you can\?")


def budget_tickets_left(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _BUDGET_TICKETS_LEFT.fullmatch(text)
    if match is None:
        return None
    b, p = Fraction(match.group("b")), Fraction(match.group("p"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [True, True] or [n[0] for n in numbers] != [b, p]:
        return None
    if p <= 0 or b < 0:
        return None
    n = b // p if p.denominator == 1 and b.denominator == 1 else None
    if n is None:
        n = int(b / p)
    left = b - p * n
    if left < 0 or left >= p:
        return None
    eq = "%s = %s*n + r" % (show(b), show(p))
    return Result("budget_tickets_left", [left], eq, "%s, so leftover is %s" % (eq, show_exact(left)))

_SHIRT_SALE_AFTER_PERCENT = re.compile(
    r"a shirt costs \$(?P<p>\d+(?:\.\d+)?) and is (?P<r>\d+(?:\.\d+)?)% off\. what is the sale price\?")


def shirt_sale_after_percent(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SHIRT_SALE_AFTER_PERCENT.fullmatch(text)
    if match is None:
        return None
    p, r = Fraction(match.group("p")), Fraction(match.group("r"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [True, False] or [n[0] for n in numbers] != [p, r]:
        return None
    if not (0 < r < 100) or p <= 0:
        return None
    sale = p * (100 - r) / 100
    if sale <= 0:
        return None
    eq = "%s*(1 - %s/100)" % (show(p), show(r))
    return Result("shirt_sale_after_percent", [sale], eq, "%s, so the sale price is %s" % (eq, show_exact(sale)))


_PERCENT_OFF_SAVING_ORIGINAL = re.compile(
    r"a shirt is (?P<r>\d+(?:\.\d+)?)% off, saving \$(?P<s>\d+(?:\.\d+)?)\. what was the original price\?")


def percent_off_saving_original(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PERCENT_OFF_SAVING_ORIGINAL.fullmatch(text)
    if match is None:
        return None
    r, s = Fraction(match.group("r")), Fraction(match.group("s"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [False, True] or [n[0] for n in numbers] != [r, s]:
        return None
    if not (0 < r < 100) or s <= 0:
        return None
    orig = s * 100 / r
    if orig <= 0:
        return None
    eq = "(%s/100)*x = %s" % (show(r), show(s))
    return Result("percent_off_saving_original", [orig], eq, "%s, so x = %s" % (eq, show_exact(orig)))


_SECOND_PERCENT_OFF_NOW = re.compile(
    r"a jacket is (?P<r1>\d+(?:\.\d+)?)% off\. it costs \$(?P<p>\d+(?:\.\d+)?) now\. what does it cost after another (?P<r2>\d+(?:\.\d+)?)% off\?")


def second_percent_off_now(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SECOND_PERCENT_OFF_NOW.fullmatch(text)
    if match is None:
        return None
    r1, p, r2 = Fraction(match.group("r1")), Fraction(match.group("p")), Fraction(match.group("r2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or [flag for _v, flag, _s, _e in numbers] != [False, True, False] or [n[0] for n in numbers] != [r1, p, r2]:
        return None
    if not (0 < r1 < 100 and 0 < r2 < 100) or p <= 0:
        return None
    sale = p * (100 - r2) / 100
    if sale <= 0:
        return None
    eq = "%s*(1 - %s/100)" % (show(p), show(r2))
    return Result("second_percent_off_now", [sale], eq, "%s, so it costs %s" % (eq, show_exact(sale)))


_THREE_SUCH_CREWS_TOGETHER = re.compile(
    r"a crew can pave a road in (?P<a>\d+(?:\.\d+)?) days and another crew can pave it in (?P<b>\d+(?:\.\d+)?) days\. "
    r"how long will three such crews take working together\?")


def three_such_crews_together(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _THREE_SUCH_CREWS_TOGETHER.fullmatch(text)
    if match is None:
        return None
    a, b = Fraction(match.group("a")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b]:
        return None
    if a <= 0 or b <= 0:
        return None
    t = 1 / (3 * (1 / a + 1 / b))
    if t <= 0:
        return None
    eq = "3*(1/%s + 1/%s) = 1/t" % (show(a), show(b))
    return Result("three_such_crews_together", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_PARTNER_HALF_SPEED_TOGETHER = re.compile(
    r"(?P<a>[a-z]+) can sort the mail in (?P<x>\d+(?:\.\d+)?) hours and (?P<b>[a-z]+) in (?P<y>\d+(?:\.\d+)?) hours\. "
    r"how long will they take together if (?P=b) works at half speed\?")


def partner_half_speed_together(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PARTNER_HALF_SPEED_TOGETHER.fullmatch(text)
    if match is None:
        return None
    if match.group("a") == match.group("b"):
        return None
    x, y = Fraction(match.group("x")), Fraction(match.group("y"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [x, y]:
        return None
    if x <= 0 or y <= 0:
        return None
    t = 1 / (1 / x + 1 / (2 * y))
    if t <= 0:
        return None
    eq = "1/%s + 1/(%s*2) = 1/t" % (show(x), show(y))
    return Result("partner_half_speed_together", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_ADD_PERCENT_TO_KNOWN_SOLUTION = re.compile(
    r"how many liters of a (?P<p>\d+(?:\.\d+)?)% solution must be added to (?P<v>\d+(?:\.\d+)?) liters of a (?P<q>\d+(?:\.\d+)?)% solution to make a (?P<m>\d+(?:\.\d+)?)% solution\?")


def add_percent_to_known_solution(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _ADD_PERCENT_TO_KNOWN_SOLUTION.fullmatch(text)
    if match is None:
        return None
    p, v, q, m = (Fraction(match.group(g)) for g in ("p", "v", "q", "m"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [p, v, q, m]:
        return None
    if p == m or v <= 0:
        return None
    x = v * (m - q) / (p - m)
    if x <= 0 or p * x + q * v != m * (x + v):
        return None
    eq = "%s*x + %s*%s = %s*(x + %s)" % (show(p), show(q), show(v), show(m), show(v))
    return Result("add_percent_to_known_solution", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_MIX_EQUAL_VOLUMES_PERCENT = re.compile(
    r"mixing (?P<a>\d+(?:\.\d+)?) liters of a (?P<p>\d+(?:\.\d+)?)% solution with (?P<b>\d+(?:\.\d+)?) liters of a (?P<q>\d+(?:\.\d+)?)% solution gives what %\?")


def mix_equal_volumes_percent(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _MIX_EQUAL_VOLUMES_PERCENT.fullmatch(text)
    if match is None:
        return None
    a, p, b, q = (Fraction(match.group(g)) for g in ("a", "p", "b", "q"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, p, b, q]:
        return None
    if a <= 0 or b <= 0:
        return None
    m = (p * a + q * b) / (a + b)
    eq = "(%s*%s + %s*%s)/(%s + %s)" % (show(p), show(a), show(q), show(b), show(a), show(b))
    return Result("mix_equal_volumes_percent", [m], eq, "%s, so the mix is %s%%" % (eq, show_exact(m)))


_DRAIN_REPLACE_TO_PERCENT = re.compile(
    r"how many liters of (?P<p>\d+(?:\.\d+)?)% solution should i drain and replace with (?P<q>\d+(?:\.\d+)?)% solution to make (?P<v>\d+(?:\.\d+)?) liters of (?P<m>\d+(?:\.\d+)?)% solution\?")


def drain_replace_to_percent(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _DRAIN_REPLACE_TO_PERCENT.fullmatch(text)
    if match is None:
        return None
    p, q, v, m = (Fraction(match.group(g)) for g in ("p", "q", "v", "m"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [p, q, v, m]:
        return None
    if q == p or v <= 0:
        return None
    x = v * (m - p) / (q - p)
    if x <= 0 or x >= v:
        return None
    if p * (v - x) + q * x != m * v:
        return None
    eq = "%s*(%s - x) + %s*x = %s*%s" % (show(p), show(v), show(q), show(m), show(v))
    return Result("drain_replace_to_percent", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_SAVINGS_EQUAL_HOW_MUCH = re.compile(
    r"(?P<a>[a-z]+) has \$(?P<a0>\d+(?:\.\d+)?) and saves \$(?P<ar>\d+(?:\.\d+)?) a week\. "
    r"(?P<b>[a-z]+) has \$(?P<b0>\d+(?:\.\d+)?) and saves \$(?P<br>\d+(?:\.\d+)?) a week\. "
    r"how much will each have when they have the same amount\?")


def savings_equal_how_much(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SAVINGS_EQUAL_HOW_MUCH.fullmatch(text)
    if match is None:
        return None
    if match.group("a") == match.group("b"):
        return None
    a0, ar, b0, br = (Fraction(match.group(g)) for g in ("a0", "ar", "b0", "br"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or not all(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a0, ar, b0, br]:
        return None
    if ar == br:
        return None
    w = (b0 - a0) / (ar - br)
    if w <= 0:
        return None
    amt = a0 + ar * w
    if amt != b0 + br * w or amt <= 0:
        return None
    eq = "%s + %s*w = %s + %s*w" % (show(a0), show(ar), show(b0), show(br))
    return Result("savings_equal_how_much", [amt], eq, "%s, so each has %s" % (eq, show_exact(amt)))


_QUIZZES_FINAL_COUNTS_DOUBLE = re.compile(
    r"(?P<name>[a-z]+) got (?P<s1>\d+(?:\.\d+)?), (?P<s2>\d+(?:\.\d+)?) and (?P<s3>\d+(?:\.\d+)?) on three quizzes\. "
    r"the final counts double\. what must (?P=name) score on the final to average (?P<avg>\d+(?:\.\d+)?)\?")


def quizzes_final_counts_double(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _QUIZZES_FINAL_COUNTS_DOUBLE.fullmatch(text)
    if match is None:
        return None
    s1, s2, s3, avg = (Fraction(match.group(g)) for g in ("s1", "s2", "s3", "avg"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [s1, s2, s3, avg]:
        return None
    x = (5 * avg - (s1 + s2 + s3)) / 2
    eq = "(%s + %s + %s + 2x)/5 = %s" % (show(s1), show(s2), show(s3), show(avg))
    return Result("quizzes_final_counts_double", [x], eq, "%s, so x = %s" % (eq, show_exact(x)))


_SAME_DIRECTION_GAP_TIME = re.compile(
    r"two cars leave the same spot in the same direction at (?P<a>\d+(?:\.\d+)?) km/h and (?P<b>\d+(?:\.\d+)?) km/h\. when are they (?P<d>\d+(?:\.\d+)?) km apart\?")


def same_direction_gap_time(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _SAME_DIRECTION_GAP_TIME.fullmatch(text)
    if match is None:
        return None
    a, b, d = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("d"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, d]:
        return None
    if a == b or min(a, b, d) <= 0:
        return None
    t = d / abs(a - b)
    eq = "|%s - %s|*t = %s" % (show(a), show(b), show(d))
    return Result("same_direction_gap_time", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_CATCH_AFTER_FIRST_LEAVES = re.compile(
    r"a jogger leaves at (?P<s>\d+(?:\.\d+)?) mph\. (?P<h>one|two|three|four|five|six|seven|eight|nine|ten) hour later a cyclist follows at (?P<f>\d+(?:\.\d+)?) mph\. "
    r"how many hours after the jogger leaves does the cyclist catch up\?")


def catch_after_first_leaves(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CATCH_AFTER_FIRST_LEAVES.fullmatch(text)
    if match is None:
        return None
    hword = match.group("h")
    s, h, f = Fraction(match.group("s")), (Fraction(1) if hword == "one" else fr(hword)), Fraction(match.group("f"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [s, f]:
        return None
    if f <= s or s <= 0 or h <= 0:
        return None
    t = s * h / (f - s) + h
    if t <= 0:
        return None
    eq = "%s*t = %s*(t - %s)" % (show(s), show(f), show(h))
    return Result("catch_after_first_leaves", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_HENS_PIGS_HOW_MANY_ANIMALS = re.compile(
    r"a (?P<place>[a-z]+) has hens and pigs\. there are (?P<h>\d+) heads and (?P<f>\d+) feet\. how many animals are there\?")


def hens_pigs_how_many_animals(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _HENS_PIGS_HOW_MANY_ANIMALS.fullmatch(text)
    if match is None:
        return None
    h, f = Fraction(match.group("h")), Fraction(match.group("f"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [h, f]:
        return None
    counts = _two_counts(h, 2, 4, f)
    if counts is None:
        return None
    eq = "p + g = %s; 2*p + 4*g = %s" % (show(h), show(f))
    return Result("hens_pigs_how_many_animals", [h], eq, "%s, so animals = %s" % (eq, show_exact(h)))


_CONSECUTIVE_EVEN_SUM_AND_PRODUCT = re.compile(
    r"the sum of two consecutive even integers is (?P<s>\d+) and their product is (?P<p>\d+)\. find the integers\.")


def consecutive_even_sum_and_product(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CONSECUTIVE_EVEN_SUM_AND_PRODUCT.fullmatch(text)
    if match is None:
        return None
    s, p = Fraction(match.group("s")), Fraction(match.group("p"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [s, p]:
        return None
    a = (s - 2) / 2
    b = a + 2
    if a.denominator != 1 or b.denominator != 1 or int(a) % 2 != 0 or a * b != p:
        return None
    eq = "x + (x + 2) = %s; x(x + 2) = %s" % (show(s), show(p))
    return Result("consecutive_even_sum_and_product", [a, b], eq, "%s, so the integers are %s and %s" % (eq, show_exact(a), show_exact(b)))


_RATIO_FOR_KNOWN_WATER = re.compile(
    r"water is mixed into concentrate in the ratio (?P<a>\d+):(?P<b>\d+)\. how much of each is needed for (?P<w>\d+(?:\.\d+)?) litres of water\?")


def ratio_for_known_water(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _RATIO_FOR_KNOWN_WATER.fullmatch(text)
    if match is None:
        return None
    a, b, w = Fraction(match.group("a")), Fraction(match.group("b")), Fraction(match.group("w"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a, b, w]:
        return None
    if a <= 0 or b <= 0 or w <= 0:
        return None
    conc = w * b / a
    eq = "%s/%s = %s/x" % (show(a), show(b), show(w))
    return Result("ratio_for_known_water", [conc, w], eq, "%s, so concentrate = %s and water = %s" % (eq, show_exact(conc), show_exact(w)))


_THREE_NUMBERS_PAIR_SUMS_LARGEST = re.compile(
    r"the sum of three numbers is (?P<t>\d+(?:\.\d+)?)\. the first two add to (?P<ab>\d+(?:\.\d+)?) and the last two add to (?P<bc>\d+(?:\.\d+)?)\. what is the largest\?")


def three_numbers_pair_sums_largest(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _THREE_NUMBERS_PAIR_SUMS_LARGEST.fullmatch(text)
    if match is None:
        return None
    t, ab, bc = Fraction(match.group("t")), Fraction(match.group("ab")), Fraction(match.group("bc"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [t, ab, bc]:
        return None
    c = t - ab
    a = t - bc
    b = t - a - c
    if min(a, b, c) <= 0:
        return None
    large = max(a, b, c)
    eq = "a + b + c = %s; a + b = %s; b + c = %s" % (show(t), show(ab), show(bc))
    return Result("three_numbers_pair_sums_largest", [large], eq, "%s, so the largest is %s" % (eq, show_exact(large)))


_TICKETS_OR_SNACKS_AFFORD = re.compile(
    r"you have \$(?P<b>\d+(?:\.\d+)?)\. you can buy tickets at \$(?P<t>\d+(?:\.\d+)?) or snacks at \$(?P<s>\d+(?:\.\d+)?) each\. how many snacks can you afford\?")


def tickets_or_snacks_afford(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TICKETS_OR_SNACKS_AFFORD.fullmatch(text)
    if match is None:
        return None
    b, t, s = Fraction(match.group("b")), Fraction(match.group("t")), Fraction(match.group("s"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or not all(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [b, t, s]:
        return None
    if s <= 0 or b < 0 or t <= 0:
        return None
    n = b / s
    if n.denominator != 1 or n < 0:
        return None
    eq = "%s = %s*n" % (show(b), show(s))
    return Result("tickets_or_snacks_afford", [n], eq, "%s, so n = %s" % (eq, show_exact(n)))


_HALL_FIRST_FREE_GUESTS = re.compile(
    r"a hall costs \$(?P<f>\d+(?:\.\d+)?) plus \$(?P<p>\d+(?:\.\d+)?) per guest, and the first (?P<k>\d+) guests are free\. the final bill was \$(?P<tot>\d+(?:\.\d+)?)\. how many guests attended\?")


def hall_first_free_guests(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _HALL_FIRST_FREE_GUESTS.fullmatch(text)
    if match is None:
        return None
    f, p, k, tot = (Fraction(match.group(g)) for g in ("f", "p", "k", "tot"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or [flag for _v, flag, _s, _e in numbers] != [True, True, False, True] or [n[0] for n in numbers] != [f, p, k, tot]:
        return None
    if p <= 0 or tot < f or k < 0:
        return None
    extra = (tot - f) / p
    if extra.denominator != 1 or extra < 0:
        return None
    g = extra + k
    if f + p * (g - k) != tot:
        return None
    eq = "%s + %s*(n - %s) = %s" % (show(f), show(p), show(k), show(tot))
    return Result("hall_first_free_guests", [g], eq, "%s, so n = %s" % (eq, show_exact(g)))


_TWO_TANKS_MEET = re.compile(
    r"tank a has (?P<a0>\d+(?:\.\d+)?) litres and drains (?P<ar>\d+(?:\.\d+)?) a day\. "
    r"tank b has (?P<b0>\d+(?:\.\d+)?) litres and fills (?P<br>\d+(?:\.\d+)?) a day\. when are they equal\?")


def two_tanks_meet(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TWO_TANKS_MEET.fullmatch(text)
    if match is None:
        return None
    a0, ar, b0, br = (Fraction(match.group(g)) for g in ("a0", "ar", "b0", "br"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a0, ar, b0, br]:
        return None
    t = (a0 - b0) / (ar + br)
    if t <= 0:
        return None
    if a0 - ar * t != b0 + br * t:
        return None
    eq = "%s - %s*t = %s + %s*t" % (show(a0), show(ar), show(b0), show(br))
    return Result("two_tanks_meet", [t], eq, "%s, so t = %s" % (eq, show_exact(t)))


_TOWNS_EQUAL_POPULATION = re.compile(
    r"town a has (?P<a0>\d+(?:\.\d+)?) people and grows by (?P<ar>\d+(?:\.\d+)?) a year\. "
    r"town b has (?P<b0>\d+(?:\.\d+)?) and shrinks by (?P<br>\d+(?:\.\d+)?) a year\. what will each population be when they are equal\?")


def towns_equal_population(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TOWNS_EQUAL_POPULATION.fullmatch(text)
    if match is None:
        return None
    a0, ar, b0, br = (Fraction(match.group(g)) for g in ("a0", "ar", "b0", "br"))
    numbers = digit_numbers(problem)
    if len(numbers) != 4 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [a0, ar, b0, br]:
        return None
    y = (b0 - a0) / (ar + br)
    if y <= 0:
        return None
    pop = a0 + ar * y
    if pop != b0 - br * y or pop <= 0:
        return None
    eq = "%s + %s*y = %s - %s*y" % (show(a0), show(ar), show(b0), show(br))
    return Result("towns_equal_population", [pop], eq, "%s, so each has %s" % (eq, show_exact(pop)))


_CULTURE_AFTER_HOURS = re.compile(
    r"a culture doubles every (?P<d>\d+(?:\.\d+)?) hours\. if it starts at (?P<n>\d+(?:\.\d+)?) cells, how many cells are there after (?P<t>\d+(?:\.\d+)?) hours\?")


def culture_after_hours(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _CULTURE_AFTER_HOURS.fullmatch(text)
    if match is None:
        return None
    d, n, t = Fraction(match.group("d")), Fraction(match.group("n")), Fraction(match.group("t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [d, n, t]:
        return None
    if d <= 0 or n <= 0 or t <= 0 or (t / d).denominator != 1:
        return None
    steps = int(t / d)
    end = n * (2 ** steps)
    eq = "%s * 2^(%s/%s)" % (show(n), show(t), show(d))
    return Result("culture_after_hours", [Fraction(end)], eq, "%s, so there are %s cells" % (eq, show_exact(end)))


_TANK_REMAIN_AFTER = re.compile(
    r"a tank holds (?P<c>\d+(?:\.\d+)?) l and drains at (?P<r>\d+(?:\.\d+)?) l per minute\. how many liters remain after (?P<t>\d+(?:\.\d+)?) minutes\?")


def tank_remain_after(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TANK_REMAIN_AFTER.fullmatch(text)
    if match is None:
        return None
    c, r, t = Fraction(match.group("c")), Fraction(match.group("r")), Fraction(match.group("t"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [c, r, t]:
        return None
    if min(c, r, t) <= 0:
        return None
    left = c - r * t
    if left < 0:
        return None
    eq = "%s - %s*%s" % (show(c), show(r), show(t))
    return Result("tank_remain_after", [left], eq, "%s, so %s remain" % (eq, show_exact(left)))


_QUIZ_PERCENT_WRONG = re.compile(
    r"a quiz has (?P<n>\d+) questions\. (?P<who>[a-z]+) scored (?P<p>\d+(?:\.\d+)?)%\. what percent were answered wrong\?")


def quiz_percent_wrong(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _QUIZ_PERCENT_WRONG.fullmatch(text)
    if match is None:
        return None
    qn, p = Fraction(match.group("n")), Fraction(match.group("p"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or any(flag for _v, flag, _s, _e in numbers) or [num[0] for num in numbers] != [qn, p]:
        return None
    if not (0 <= p <= 100) or qn <= 0:
        return None
    w = 100 - p
    eq = "100 - %s" % show(p)
    return Result("quiz_percent_wrong", [w], eq, "%s, so %s%% were wrong" % (eq, show_exact(w)))


_PERCENT_DECREASE_TWO_PRICES = re.compile(
    r"a bike's price went from \$(?P<a>\d+(?:\.\d+)?) to \$(?P<b>\d+(?:\.\d+)?)\. what is the % decrease\?")


def percent_decrease_two_prices(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _PERCENT_DECREASE_TWO_PRICES.fullmatch(text)
    if match is None:
        return None
    a, b = Fraction(match.group("a")), Fraction(match.group("b"))
    numbers = digit_numbers(problem)
    if len(numbers) != 2 or [flag for _v, flag, _s, _e in numbers] != [True, True] or [n[0] for n in numbers] != [a, b]:
        return None
    if a <= 0 or b >= a:
        return None
    p = (a - b) * 100 / a
    eq = "(%s - %s)/%s * 100" % (show(a), show(b), show(a))
    return Result("percent_decrease_two_prices", [p], eq, "%s, so the decrease is %s%%" % (eq, show_exact(p)))


_TIMES_AS_OLD_AGO_TIMES = re.compile(
    r"(?P<a>[a-z]+) is (?P<k1>\d+) times as old as (?P<b>[a-z]+)\. (?P<y>\d+) years ago, (?P=a) was (?P<k2>\d+) times as old as (?P=b)\. how old is each now\?")


def times_as_old_ago_times(problem):
    text = re.sub(r"\s+", " ", clean(problem)).strip()
    match = _TIMES_AS_OLD_AGO_TIMES.fullmatch(text)
    if match is None:
        return None
    if match.group("a") == match.group("b"):
        return None
    k1, y, k2 = Fraction(match.group("k1")), Fraction(match.group("y")), Fraction(match.group("k2"))
    numbers = digit_numbers(problem)
    if len(numbers) != 3 or any(flag for _v, flag, _s, _e in numbers) or [n[0] for n in numbers] != [k1, y, k2]:
        return None
    if k1 <= 1 or k2 <= k1 or y <= 0:
        return None
    young = y * (k2 - 1) / (k2 - k1)
    old = k1 * young
    if young <= 0 or old <= y or young <= y:
        return None
    if old - y != k2 * (young - y):
        return None
    eq = "%s*x - %s = %s*(x - %s)" % (show(k1), show(y), show(k2), show(y))
    return Result("times_as_old_ago_times", [young, old], eq, "%s, so they are %s and %s" % (eq, show_exact(young), show_exact(old)))

FAMILIES = [sum_difference, age_sum, consecutive, work_together, partner_alone_from_together, three_painters_together, percent_change, course_grade_final_exam, proportion, two_solution_mix, two_rate_interest, seesaw_balance_distance, more_invested_for_overall_rate, overtime_hours_time_and_a_half, walk_then_bus_unknown_time, leftover_after_two_fraction_spends, more_than_times_stamps, give_until_equal_money, estate_three_heirs_times_and_more, marbles_given_ratio_changes, profit_shared_in_investment_ratio, times_as_old_future_sum, leftover_pages_after_two_reads, fewest_weeks_to_have_at_least, bowling_games_plus_shoe_rental, test_correct_and_wrong_penalty, nickels_and_quarters_count, hour_later_toward_meet, works_alone_then_partner_joins, dimes_and_quarters_count, two_hours_later_toward_meet, lowest_next_score_for_average, weekly_base_plus_commission_sales, weeks_until_guitar, works_alone_one_hour_then_joins, mean_of_listed_missing, rent_fee_plus_use_equals_buy, rent_per_use_equals_buy, reverse_digits_sum_and_diff, linear_pair_two_angles, straight_line_angles_a_b, square_side_linear_perimeter, two_numbers_sum_and_product, three_part_mix_ratio, weeks_until_item, adult_and_child_tickets, two_plans_same_cost, food_truck_meals_cover_costs, print_run_posters_break_even, tank_fill_from_fraction, rectangle_length_from_width_perimeter, lowest_next_score_few_tests, items_sold_for_given_profit, projectile_hit_ground, stack_of_cans_rows, number_plus_reciprocal, two_linear_equations_xy, camp_two_seat_sizes, packed_two_carton_sizes, banquet_two_table_sizes, cash_drawer_two_bill_values, lot_two_wheel_vehicles, farm_spiders_and_beetles, rectangle_side_and_diagonal, ladder_wire_ramp_height, right_triangle_legs_differ, water_added_to_dilute, pure_antifreeze_added, salt_water_evaporates, handshake_or_round_robin_count, triangle_three_sides_perimeter, rectangle_perimeter_length_more_width, two_jobs_same_commission_pay, formula_perimeter_solve_width, fahrenheit_twice_celsius, fahrenheit_to_celsius, rental_car_days_plus_miles, item_coupon_when_coupon_exceeds_paid, sound_travel_time, raised_plus_per_item_to_goal, loses_value_each_year, part_is_percent_of_whole, split_bill_including_tip, percent_boys_given_girls, percent_up_then_down_ending, weekly_pay_plus_percent_of_sales, scale_model_from_real, map_scale_distance, similar_shadows_height, square_more_than_times_number, consecutive_squares_sum, square_plus_times_equals, polygon_diagonals_to_sides, triangular_sum_from_one, rope_cut_in_ratio, savings_jar_week_n, split_equal_simple_interest, simple_interest_years, ago_older_was_twice, clock_hands_together, jar_three_coins, average_of_consecutive, consecutive_times_smallest_vs_largest, plane_with_and_against_wind, two_digit_units_times_tens, round_trip_faster_return, diophantus_life_ages, exterior_equals_remote_interiors, vertical_angles_linear_pair_measures, isosceles_vertex_less_than_base, square_side_increase_area, rectangle_twice_width_area_same, pen_against_barn_two_dimensions, open_box_cut_squares, path_around_square_garden, aquarium_volume_depth, fewest_minutes_plan_b_cheaper, greatest_whole_garden_width, least_sales_for_pay_floor, drain_replace_pure_antifreeze, three_numbers_times_and_more, fraction_add_to_both, jog_minus_cycle_time, three_numbers_pair_sums, spelled_older_age_sum, times_as_old_add_up_today, rectangle_twice_long_around, garden_length_exceeds_area, triangle_angles_in_proportion, two_angles_sum_one_more, ladder_wall_base_height, later_same_track_catch, tap_and_leak_fill, pour_water_to_dilute, n_is_p_percent_of_which, cab_flag_plus_per_mile, gym_join_vs_monthly_equal, workers_days_inverse, thrown_up_from_ground, two_digit_sum_swap_up, ribbon_cut_ratio_short, budget_entry_plus_ride_tickets, lowest_last_exam_two_known, two_candles_burn_equal, fahrenheit_given_formula, trains_apart_toward_meet, beach_round_trip_two_speeds, salesperson_week_plus_percent, every_team_played_once, regular_polygon_each_interior, seesaw_child_other_side, clock_hands_line_up_hours, percent_boys_given_girls_club, shop_fixed_make_sell_break_even, car_loses_value_until, tank_quarter_add_three_quarters, pole_and_tree_shadows, mean_of_five_listed_fifth, square_side_grow_area, weeks_until_bike, stick_broken_two_ratio, plumber_come_out_plus_hour, trip_faster_same_distance, number_square_plus_times, grandpa_older_combined, cents_two_coins_dimes, cookies_brownies_count, pens_pencils_cents, motorbikes_cars_wheels, yard_perimeter_length_more, isosceles_sides_longer_base, straight_line_two_ax_c, polygon_has_diagonals, kite_string_height, plane_wind_speed_only, two_gardeners_other_alone, bucket_diluted_with_water, phone_plans_cents_equal, stone_thrown_up_land, two_plants_grow_equal, beads_three_ratio_blue, blend_from_two_pound_prices, math_scores_next_average, barn_ducks_goats_heads_feet, cyclist_spelled_hours_catch, whole_numbers_follow_product, motorboat_still_water, two_jars_grow_equal, caterer_plus_per_person, juice_added_to_cheaper, triangle_ratio_each_angle, times_as_old_later_twice, bus_split_equal_per_person, two_flours_pounds, cloud_included_gb_extra, winner_percent_margin_votes, allowance_plus_tasks_months, boat_covers_then_farther, cats_dogs_ratio_then_equal, pump_litres_in_minutes, two_pipes_and_drain_fill, spent_percent_had_left, split_two_rates_cd, sum_one_twice_other, named_together_one_alone, tap_leak_tank_fill, workers_days_inverse_wall, two_legs_how_far, tickets_each_total, coffee_added_to_make_blend, workers_paint_inverse_days, stick_cut_times_other, each_interior_regular_polygon, people_dogs_heads_legs, opposite_how_far_after, simple_interest_years_earned, bank_one_known_other_amount, split_equal_interest_two_rates, percent_used_remain_whole, water_added_to_solution, complementary_less_than_times, pharmacist_known_ml_to_total, equal_amounts_blend_price, two_investments_total_interest, bill_includes_flat_charge, discount_in_dollars_after, spelled_count_after_percent_one, spelled_count_after_rise_one, toward_meet_distance_from_first, budget_tickets_left, shirt_sale_after_percent, percent_off_saving_original, second_percent_off_now, three_such_crews_together, partner_half_speed_together, add_percent_to_known_solution, mix_equal_volumes_percent, drain_replace_to_percent, savings_equal_how_much, quizzes_final_counts_double, same_direction_gap_time, catch_after_first_leaves, hens_pigs_how_many_animals, consecutive_even_sum_and_product, ratio_for_known_water, three_numbers_pair_sums_largest, tickets_or_snacks_afford, hall_first_free_guests, two_tanks_meet, towns_equal_population, culture_after_hours, tank_remain_after, percent_decrease_two_prices, times_as_old_ago_times, 
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
            base_plus_extra_over_time, distance_speed_time, average_speed_two_leg_unknown_time, round_trip_lake_distance,
            pages_per_day, opposite_angles_equal, rectangle_from_perimeter_area,
            temperature_whole_hours, two_candles_equal, transversal_equal_angles,
            class_ratio_after_join, kinematics_time, pipes_and_drain,
            percent_spent_left, price_minus_coupon, complementary_supplementary]
FAMILIES += AF.families()          # one family for every wording the word archive proved (archive_families.json, written by make_archive_families.py)


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
