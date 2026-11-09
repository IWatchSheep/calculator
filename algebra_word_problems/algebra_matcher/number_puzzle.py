"""Reads "number puzzles" directly, without the matcher:   "Five less than twice a number is 31."

A bag-of-words matcher cannot tell "5 less than x" (x - 5) from "x less than 5" (5 - x).  This reader keeps the
order.  It understands one unknown number, whole-number / decimal / fraction constants, and a closed list of
phrases, builds the equation  a*x + b = c*x + d  and solves it exactly.

    solve("Five less than twice a number is 31. Find it.")
    -> Puzzle(answer=Fraction(18, 1), equation='2x - 5 = 31', reading='five less than twice a number  ->  2x - 5')

It returns None whenever it is not completely sure it understood every word of the equation sentence, so it can
safely run BEFORE the matcher: None means "not a plain number puzzle, use the matcher".
Only the standard library is used.
"""
import re
from collections import namedtuple
from fractions import Fraction

Puzzle = namedtuple("Puzzle", "answer equation reading")


class NotAPuzzle(Exception):
    """Raised inside the reader for anything it does not fully understand."""


# ---------------------------------------------------------------------------------------------------------
# A linear expression  a*x + b  with exact fractions
# ---------------------------------------------------------------------------------------------------------
class Lin:
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = Fraction(a), Fraction(b)

    def __add__(self, o):
        return Lin(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        return Lin(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        if self.a and o.a:
            raise NotAPuzzle("x times x")
        return Lin(self.a * o.b + self.b * o.a, self.b * o.b)

    def __truediv__(self, o):
        if o.a or o.b == 0:
            raise NotAPuzzle("division by x or by zero")
        return Lin(self.a / o.b, self.b / o.b)

    def is_const(self):
        return self.a == 0


X = Lin(1, 0)


def const(v):
    return Lin(0, v)


def show_fraction(f):
    return str(f.numerator) if f.denominator == 1 else "%d/%d" % (f.numerator, f.denominator)


def show(e):
    """2x - 5  /  x/4 + 3  /  7"""
    text = ""
    if e.a:
        c = abs(e.a)
        if c.denominator == 1:
            body = ("" if c == 1 else str(c.numerator)) + "x"
        else:
            body = ("" if c.numerator == 1 else str(c.numerator)) + "x/%d" % c.denominator
        text = ("-" if e.a < 0 else "") + body
    if e.b or not text:
        mag = show_fraction(abs(e.b))
        text = ("-" if e.b < 0 else "") + mag if not text else text + (" - " if e.b < 0 else " + ") + mag
    return text


# ---------------------------------------------------------------------------------------------------------
# Words -> numbers
# ---------------------------------------------------------------------------------------------------------
_ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
_WORD = {w: i for i, w in enumerate(_ONES)}
_WORD.update(_TENS)
_WORD["hundred"] = 100
_FRACTION_WORDS = {"half": 2, "halves": 2, "third": 3, "thirds": 3, "fourth": 4, "fourths": 4, "quarter": 4, "quarters": 4,
                   "fifth": 5, "fifths": 5, "sixth": 6, "sixths": 6, "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10}
_NUM = r"-?\d+(?:\.\d+)?(?:/\d+)?"


def words_to_digits(s):
    """'one-fourth' -> '1/4', 'twenty-one' -> '21', 'five' -> '5', 'half' -> '1/2'.  Lower-case text in and out."""
    s = s.replace("−", "-").replace("–", "-").replace("×", " times ").replace("÷", " divided by ")
    s = re.sub(r"\b(one|two|three|four|five|six|seven|eight|nine|ten)[- ](half|halves|third|thirds|fourth|fourths|quarter|quarters|fifth|fifths|sixth|sixths|seventh|eighth|ninth|tenth)\b",
               lambda m: "%d/%d" % (_WORD[m.group(1)], _FRACTION_WORDS[m.group(2)]), s)
    s = re.sub(r"\b(a|one)[- ](half|third|fourth|quarter|fifth|sixth|seventh|eighth|ninth|tenth)\b",
               lambda m: "1/%d" % _FRACTION_WORDS[m.group(2)], s)
    s = re.sub(r"\bhalf\b", "1/2", s)
    s = re.sub(r"\b(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)[- ](one|two|three|four|five|six|seven|eight|nine)\b",
               lambda m: str(_TENS[m.group(1)] + _WORD[m.group(2)]), s)
    s = re.sub(r"\b(" + "|".join(sorted(_WORD, key=len, reverse=True)) + r")\b", lambda m: str(_WORD[m.group(1)]), s)
    return s


def to_fraction(tok):
    if "/" in tok:
        a, b = tok.split("/")
        return Fraction(int(a), int(b))
    return Fraction(tok)


# ---------------------------------------------------------------------------------------------------------
# Phrase grammar (everything is matched on lower-case text with words already turned into digits)
# ---------------------------------------------------------------------------------------------------------
_UNKNOWN = r"(?:the same number|a certain number|a number|the number|my number|this number|that number|some number|x)"
_VERB = (r"(?:add|subtract|take away|multiply|divide|increase|decrease|reduce|double|triple|halve|minus|plus|"
         r"increased|decreased|reduced|multiplied|divided|subtracted|added|doubled|tripled|halved|then)")
_CHAIN_SPLIT = re.compile(r"\s*(?:,\s*(?:and\s+)?(?:then\s+)?|\s+and\s+(?:then\s+)?|\s+then\s+)(?=(?:the result is\s+)?" + _VERB + r"\b)")


def expr(s):
    """Parse a phrase into a Lin, or raise NotAPuzzle."""
    s = s.strip(" ,.;")
    s = re.sub(r"^(?:the result of|the value of|the answer to|the number that is|the number which is)\s+", "", s)
    s = re.sub(r"^(?:the same as|equal to|exactly)\s+", "", s)
    if not s:
        raise NotAPuzzle("empty")
    parts = _CHAIN_SPLIT.split(s)
    if len(parts) > 1:
        return chain(parts)
    return phrase(s)


def phrase(s):
    s = s.strip(" ,.;")
    # "A less than B" -> B - A   ,   "A more than B" -> B + A
    m = re.match(r"^(.+?)\s+(?:less|fewer|smaller)\s+than\s+(.+)$", s)
    if m:
        return expr(m.group(2)) - expr(m.group(1))
    m = re.match(r"^(.+?)\s+(?:more|greater|larger|bigger)\s+than\s+(.+)$", s)
    if m:
        return expr(m.group(2)) + expr(m.group(1))
    # "A subtracted from B" -> B - A,  "A added to B" -> B + A    (also passive: "4 is subtracted from a number")
    m = re.match(r"^(.+?)\s+(?:is\s+|are\s+)?subtracted\s+from\s+(.+)$", s)
    if m:
        return expr(m.group(2)) - expr(m.group(1))
    m = re.match(r"^(.+?)\s+(?:is\s+|are\s+)?added\s+to\s+(.+)$", s)
    if m:
        return expr(m.group(2)) + expr(m.group(1))
    # left-to-right additive operators: split at the LAST one
    best = None
    for rx, sign in ((r"\s+(?:plus|increased by|added with)\s+", 1), (r"\s+(?:minus|decreased by|reduced by|take away)\s+", -1)):
        for m in re.finditer(rx, s):
            if best is None or m.start() > best[0].start():
                best = (m, sign)
    if best:
        m, sign = best
        left, right = expr(s[:m.start()]), expr(s[m.end():])
        return left + right if sign > 0 else left - right
    # multiplicative operators: split at the LAST one
    best = None
    for rx, op in ((r"\s+(?:times|multiplied by)\s+", "*"), (r"\s+(?:divided by|over)\s+", "/")):
        for m in re.finditer(rx, s):
            if best is None or m.start() > best[0].start():
                best = (m, op)
    if best:
        m, op = best
        left, right = expr(s[:m.start()]), expr(s[m.end():])
        return left * right if op == "*" else left / right
    # fractions of something: "1/2 of a number", "4/5 of it"
    m = re.match(r"^(" + _NUM + r")\s+of\s+(.+)$", s)
    if m:
        return const(to_fraction(m.group(1))) * expr(m.group(2))
    # prefix forms
    m = re.match(r"^(?:twice|double)\s+(.+)$", s)
    if m:
        return const(2) * expr(m.group(1))
    m = re.match(r"^triple\s+(.+)$", s)
    if m:
        return const(3) * expr(m.group(1))
    m = re.match(r"^the\s+(sum|difference|product|quotient)\s+of\s+(.+?)\s+and\s+(.+)$", s)
    if m:
        a, b = expr(m.group(2)), expr(m.group(3))
        return {"sum": lambda: a + b, "difference": lambda: a - b, "product": lambda: a * b, "quotient": lambda: a / b}[m.group(1)]()
    m = re.match(r"^(?:multiply|divide)\s+(.+?)\s+by\s+(.+)$", s)
    if m:
        a, b = expr(m.group(1)), expr(m.group(2))
        return a * b if s.startswith("multiply") else a / b
    m = re.match(r"^subtract\s+(.+?)\s+from\s+(.+)$", s)
    if m:
        return expr(m.group(2)) - expr(m.group(1))
    m = re.match(r"^add\s+(.+?)\s+to\s+(.+)$", s)
    if m:
        return expr(m.group(2)) + expr(m.group(1))
    # atoms
    if re.fullmatch(_UNKNOWN, s) or s in ("it", "that", "the result"):
        return X
    if re.fullmatch(_NUM, s):
        return const(to_fraction(s))
    raise NotAPuzzle("cannot read: " + s)


def apply_step(prev, step):
    """One later step of a chain ('and add 5', 'then increased by 9', 'the result is multiplied by 5') on the running value."""
    s = step.strip(" ,.;")
    s = re.sub(r"^the result is\s+", "", s)
    s = re.sub(r"^then\s+", "", s)
    for rx, fn in (
        (r"^(?:add|plus|increased by|increase (?:it )?by|increase by|added)\s+(" + _NUM + r")(?:\s+to it)?$", lambda c: prev + const(c)),
        (r"^(?:subtract|take away|minus|decreased by|decrease (?:it )?by|reduced by|reduce (?:it )?by|subtracted)\s+(" + _NUM + r")(?:\s+from it)?$", lambda c: prev - const(c)),
        (r"^(?:multiply (?:it |the result )?by|multiplied by|times)\s+(" + _NUM + r")$", lambda c: prev * const(c)),
        (r"^(?:divide (?:it |the result )?by|divided by)\s+(" + _NUM + r")$", lambda c: prev / const(c)),
    ):
        m = re.match(rx, s)
        if m:
            return fn(to_fraction(m.group(1)))
    if re.fullmatch(r"(?:double it|doubled)", s):
        return prev * const(2)
    if re.fullmatch(r"(?:triple it|tripled)", s):
        return prev * const(3)
    if re.fullmatch(r"(?:halve it|halved)", s):
        return prev * const(Fraction(1, 2))
    raise NotAPuzzle("cannot read step: " + step)


def chain(parts):
    first = parts[0].strip(" ,.;")
    # an imperative start on the unknown: "triple it", "multiply it by 6", "divide it by 7"
    if re.fullmatch(r"(?:double|triple|halve) it", first):
        value = apply_step(X, first)
    else:
        m = re.match(r"^(multiply|divide)\s+it\s+by\s+(" + _NUM + r")$", first)
        if m:
            value = apply_step(X, first)
        else:
            value = phrase(first)
    for step in parts[1:]:
        value = apply_step(value, step)
    return value


# ---------------------------------------------------------------------------------------------------------
# Whole problems
# ---------------------------------------------------------------------------------------------------------
_RELATIONS = [r"\s+is the same as\s+", r"\s+is equal to\s+", r"\s+you(?:'ll| will)? get\s+", r"\s+gives\s+", r"\s+equals\s+",
              r"\s+is\s+", r"\s+are\s+", r"\s+makes\s+", r"\s+results in\s+", r"\s+comes to\s+", r"\s+the same as\s+"]
_SKIP_SENTENCE = re.compile(r"^(?:find|what|which|how|solve|give|list|determine|calculate|tell|i'?m thinking|i am thinking|think of)\b")


def clean_sentence(sent):
    s = sent.strip().lower().replace("’", "'")
    s = re.sub(r"^(?:if|when|suppose|given that|after)\s+", "", s)
    s = re.sub(r"^(?:you|i)\s+(?=(?:add|subtract|multiply|divide|double|triple|halve|take))", "", s)
    s = re.sub(r"^you\s+", "", s)
    return words_to_digits(s)


def split_equation(sentence):
    """Yield (left text, right text) for every place the sentence could be split into two sides."""
    s = sentence
    # "..., you get 29"  /  "..., the answer is 60"  /  "...,  is 106"
    for pre in (r",\s*(?:then\s+)?(?:you\s+(?:will\s+)?get|the (?:answer|result) is|it (?:is|equals|gives))\s+", r"\s+(?:you\s+(?:will\s+)?get|the (?:answer|result) is)\s+"):
        for m in re.finditer(pre, s):
            yield s[:m.start()], s[m.end():]
    for m in re.finditer(r"\s+you(?:'ll| will)? get (?:the same as|exactly the same as)\s+", s):
        yield s[:m.start()], s[m.end():]
    for rx in _RELATIONS:
        for m in re.finditer(rx, s):
            yield s[:m.start()], s[m.end():]
    m = re.search(r"\s*,\s*(?:is|gives)\s+", s)
    if m:
        yield s[:m.start()], s[m.end():]


def solve(problem):
    """Puzzle(answer, equation, reading) for a plain one-unknown number puzzle, otherwise None."""
    text = problem.strip()
    low = text.lower()
    if not re.search(r"\bnumber\b", low) and not re.search(r"\bthink of\b|\bit\b", low):
        return None
    if re.search(r"\b(numbers|digits?|consecutive|integers|squared|square|cubed|reciprocal|percent|%|\$)\b", low) or re.search(r"[a-z]\d|\d[a-z]", low.replace("1st", "")):
        return None
    sentences = [x for x in re.split(r"(?<=[.!?])\s+", text) if x.strip()]
    found = []
    for sent in sentences:
        if sent.strip().endswith("?"):
            continue
        s = clean_sentence(sent.rstrip(".!? "))
        if _SKIP_SENTENCE.match(s):
            continue
        for left, right in split_equation(s):
            left = re.sub(r"[\s,]*\band\s*$", "", left)
            try:
                lhs, rhs = expr(left), expr(right)
            except (NotAPuzzle, ZeroDivisionError, ValueError):
                continue
            denom = lhs.a - rhs.a
            if denom == 0 or (lhs.a == 0 and rhs.a == 0):
                continue
            answer = (rhs.b - lhs.b) / denom
            found.append(Puzzle(answer, "%s = %s" % (show(lhs), show(rhs)), "%s  ->  %s = %s" % (sent.strip().rstrip(".!? "), show(lhs), show(rhs))))
            break
    if len(found) != 1:
        return None
    return found[0]


def answer_text(p):
    return show_fraction(p.answer)


if __name__ == "__main__":
    import sys
    r = solve(" ".join(sys.argv[1:]))
    print("not a plain number puzzle" if r is None else "%s   ->   x = %s" % (r.equation, answer_text(r)))
