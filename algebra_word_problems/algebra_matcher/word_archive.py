"""Find algebra word-problem answers the way the chess program uses its four lists and its archive.

    python word_archive.py [passes]        play the stored problems (default: until nothing changes, at most 40 passes)

A stored problem is a board.  A game is one LINE: an equation shape, and one of the problem's numbers in each slot of it.
    shape   "R2/R0 + X/R0 + X/R1 = 1"      X is the unknown, R0 R1 R2 are slots, 1 is a fixed number of the shape
    line    the shape and, for each slot, the place of a number in the sentence (N0, N1, ...), never its value
A slot is a role.  The shape may write a role twice.  Every number of the sentence gets exactly one slot.

The shapes are the equation shapes of the stored problems (the book).  A book game is a stored problem whose stored EQUATION
solves to its stored ANSWER.  The stored equation of a problem, or of another problem of the same wording, is the answer key:
  - a problem is offered a shape only when a problem of a DIFFERENT wording is a source of it;
  - a book game is not a played game: it never makes a line "tried" and it is never a win;
  - a line that won in another wording (a book game there, or a played game) is "similar".  Similar orders List 3.  It proves nothing.
A game is compared only with the problem's own ANSWER, after the game has ended.

List 1  the shapes forming in this sentence.  30: the shape has as many slots as the sentence has numbers.
        60: a book sentence of another wording that used the shape also shares most of this sentence's words.
List 2  every legal line of the List 1 shapes, the furthest formed shape first, then the numbers in sentence order.
List 3  one row per legal line, from finished games: proven win, proven loss, tried, similar, never tried.
List 4  what the finished games actually got with each tried or similar line: won here, lost here, other wordings it won in.
        Empty until a game of this wording has finished or another wording has won with one of these lines.

A pass plays one game for every problem: a proven win, else a line that has only won in this wording, else a similar line,
else the first never-tried line.  A line that lost in this wording is never played there again.  The games are merged only after
the pass, so a problem never reads its own game.  A wrong number is stored as a loss.  A problem with no line left is stored as
a dead end.

A wording (the proof key) is the sentence without its numbers, people's names, the plural s after a number, and the name of
the work ("paint a fence", "mow a lawn").  Cue words stay: sentences that differ by "more" and "less" are two wordings.
A wording is proven only when the same line was PLAYED and won on every stored problem of the wording, and at least two of
those problems have different numbers.  One win is only a candidate.  A game wins only when it gives every number the answer
asks for: a line that gives one number loses a problem that asks for two.
answer() returns a number only from a proven line.  Anything else is None.  It is not wired to = or to word_solver.FAMILIES.

After the passes, every wording with two different sets of numbers is swept with GENERATED lines (word_generator.py): trees
over the sentence's numbers and the fixed numbers 1, 2 and 100, smallest first, built from no stored equation.  A generated
line that wins every stored problem is stored on its own.  A finished sweep that found none is stored as one loss record
(size reached, problem ids, fixed numbers, generator version).  The record never answers, and it is void when a stored
problem of the wording is added or the generator changes.

The "templates" part of word_archive.json is the older final check (the stored equation solves to the stored answer); it is
what make_archive_families.py reads.  The "games" part is the four lists' archive.  Standard library only.
"""
import itertools
import json
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import word_generator  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
PROBLEMS = os.path.join(ROOT, "operators_one_algebra_word_problem_per_file")
ARCHIVE = os.path.join(HERE, "word_archive.json")
GENERATED_MIN_TUPLES = 3      # a generated line is proven only on three independent sets of numbers (see _independent)
MAX_SLOTS = 6                 # 7 numbers are 5,040 orders for every shape: those problems are left as dead ends
STARTS = (0.0, 1.0, 2.0, 0.5, 10.0, 0.25, 5.0, -2.0, 20.0, 50.0, 8.0, 100.0, -10.0)
NUMBER = re.compile(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?")
# Words that change the equation.  Two sentences that differ by one of these are two wordings, never one with a work name out.
CUES = set("""more less fewer greater smaller larger older younger longer shorter faster slower higher lower heavier lighter
    increased decreased increase decrease raised reduced added removed gained lost even odd complementary supplementary
    exterior interior first second third fourth fifth half twice double triple quarter sum product difference quotient
    square squares squared cube cubes hour hours minute minutes day days week weeks month months year years mile miles
    penny pennies nickel nickels dime dimes quarters adult child before after ago together alone each per total with against
    upstream downstream north south east west same opposite toward apart not no every all both either only fills empties
    in out up down over under plus minus times
    bicycle bicycles tricycle tricycles motorcycle motorcycles car cars""".split())


# ---------------------------------------------------------------------------------------------------------------------------
# the final check: the stored equation of one problem (unchanged; make_archive_families.py and the tests use these names)
# ---------------------------------------------------------------------------------------------------------------------------
def _normalize(equation):
    equation = equation.replace("×", "*").replace("−", "-").replace("–", "-").replace("·", "*")
    previous = None
    while previous != equation:
        previous = equation
        equation = re.sub(r"(\d)\s*([A-Za-z])", r"\1*\2", equation)
        equation = re.sub(r"(\d)\s*\(", r"\1*(", equation)
        equation = re.sub(r"([A-Za-z])\s*\(", r"\1*(", equation)
        equation = re.sub(r"\)\s*(\d)", r")*\1", equation)
        equation = re.sub(r"\)\s*([A-Za-z])", r")*\1", equation)
        equation = re.sub(r"\)\s*\(", r")*(", equation)
    return equation


def _answer_number(text):
    match = re.search(r"-?\d+(?:\.\d+)?", text.replace(",", ""))
    return float(match.group(0)) if match else None


def _literals(equation):
    """Numbers written in the equation, left to right, and the one letter that is the unknown."""
    letters = set(re.findall(r"[A-Za-z]", equation))
    if len(letters) != 1:
        return None, []
    return letters.pop(), [float(n) for n in re.findall(r"\d+(?:\.\d+)?", equation)]


def solve_equation(equation):
    """The unknown in a school equation with one letter, or None when this reader cannot take it."""
    if any(mark in equation for mark in ";≥≤<>%√π^"):
        return None
    equation = _normalize(equation)
    sides = equation.split("=")
    if len(sides) != 2:
        return None
    variable, _ = _literals(equation)
    if variable is None:
        return None
    expression = "(%s)-(%s)" % (sides[0], sides[1])

    def f(x):
        return eval(expression, {"__builtins__": {}}, {variable: float(x)})

    for start in STARTS:
        x = float(start)
        good = True
        for _ in range(50):
            try:
                y = f(x)
                y2 = f(x + 1e-6)
            except Exception:
                good = False
                break
            slope = (y2 - y) / 1e-6
            if abs(slope) < 1e-14:
                good = False
                break
            nxt = x - y / slope
            if abs(nxt - x) < 1e-9:
                x = nxt
                break
            x = nxt
        if not good:
            continue
        try:
            if abs(f(x)) < 1e-5:
                return round(x, 8)
        except Exception:
            continue
    return None


def _bind(literals, numbers):
    """Each equation number is the index of a problem number, or None when it is a fixed number."""
    pool = [float(n) for n in numbers]
    binding = []
    for literal in literals:
        found = None
        for i, number in enumerate(pool):
            if abs(number - literal) <= 1e-9 * max(1.0, abs(literal)):
                found = i
                break
        binding.append(found)
    return binding


def load_problems():
    """Every generated problem: reference ones and ready ones."""
    import importlib.util
    found = []
    for folder, _dirs, files in os.walk(PROBLEMS):
        name = os.path.basename(folder)
        if name + ".py" not in files:
            continue
        path = os.path.join(folder, name + ".py")
        spec = importlib.util.spec_from_file_location("prob_" + name + "_" + str(len(found)), path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        found.append(module)
    return found


def final_check(problem):
    """The stored equation of one problem: how its numbers sit in it, what it solves to, and whether that is the stored answer."""
    equation = problem.EQUATION
    variable, literals = _literals(_normalize(equation))
    solved = solve_equation(equation)
    answer = _answer_number(problem.ANSWER)
    matched = solved is not None and answer is not None and abs(solved - answer) <= 1e-4 * max(1.0, abs(answer))
    return {"variable": variable, "binding": _bind(literals, list(problem.NUMBERS)) if variable else [],
            "solved": solved, "stored_answer": answer, "matched": matched}


def _in_reference_set(problem):
    """No hand-written family answers it.  A problem that only an archive family answers stays in: that family was made
    from this archive, and leaving its problems out would un-prove the wording the family came from."""
    return problem.SOLVER is None or str(getattr(problem, "FAMILY", "") or "").startswith("archive_")


def _templates(problems, reference_only):
    groups = {}
    for problem in problems:
        if reference_only and not _in_reference_set(problem):
            continue
        groups.setdefault(problem.TEMPLATE, []).append(final_check(problem))
    templates = {}
    proven = candidates = skipped = 0
    for wording, games in groups.items():
        matched = [g for g in games if g["matched"]]
        record = {"tried": len(games), "matched": len(matched), "pattern": wording,
                  "proven": len(games) >= 2 and len(matched) == len(games)}
        templates[wording] = record
        if record["proven"]:
            proven += 1
        elif matched:
            candidates += 1
        else:
            skipped += 1
    return {"templates": templates, "proven_wordings": proven, "candidate_wordings": candidates, "unmatched_wordings": skipped}


# ---------------------------------------------------------------------------------------------------------------------------
# wordings, shapes and lines
# ---------------------------------------------------------------------------------------------------------------------------
def template_of(text):
    """The sentence with every number replaced by {0}, {1}, ..., and the numbers as written (the problem files' rule)."""
    numbers, parts, last = [], [], 0
    for m in NUMBER.finditer(text):
        parts.append(text[last:m.start()].replace("{", "{{").replace("}", "}}"))
        parts.append("{%d}" % len(numbers))
        numbers.append(m.group(0).replace(",", ""))
        last = m.end()
    parts.append(text[last:].replace("{", "{{").replace("}", "}}"))
    return "".join(parts), numbers


def asked_numbers(text):
    """The numbers written in a stored answer, as exact fractions: outside brackets, a clock time (1:00) left out, and a
    rounded copy of another number ("60/11 ≈ 5.45") left out."""
    text = re.sub(r"\([^)]*\)", "", text)
    text = re.sub(r"\d+:\d+", " ", text)
    text = re.sub(r"(?<=\d),(?=\d{3})", "", text)
    found = []
    for whole, dec, bottom in re.findall(r"(-?\d+(\.\d+)?)(?:/(\d+))?", text.replace("−", "-")):
        if bottom and int(bottom) == 0:
            continue
        found.append((Fraction(whole) / int(bottom) if bottom else Fraction(whole), len(dec) - 1 if dec and not bottom else None))
    out = []
    for n, (value, places) in enumerate(found):
        copy = places is not None and any(m != n and other != value and round(other, places) == value for m, (other, _p) in enumerate(found))
        if not copy:
            out.append(value)
    return out


def answer_numbers(text, given=()):
    """The asked numbers of one answer as floats.  A number the sentence itself gave ("12 lb at $3") is left out when the
    answer has other numbers.  (Inside a Book, the numbers a whole wording echoes are found from all its problems.)"""
    out = asked_numbers(text)
    pool = [Fraction(g) for g in given]
    asked = [a for a in out if a not in pool]
    return [float(a) for a in (asked or out)]


def _same(a, b):
    return abs(a - b) <= 1e-6 * max(1.0, abs(b))


class Book:
    """The stored problems, their wordings, and the shapes and book games read from their stored equations."""

    def __init__(self, problems=None):
        self.problems = list(problems) if problems is not None else load_problems()
        self.problems.sort(key=lambda p: p.ID)
        self.by_id = {p.ID: p for p in self.problems}
        self.lower = set(re.findall(r"\b[a-z]+\b", " ".join(p.TEMPLATE for p in self.problems)))
        self.exact = {p.ID: self.exact_of(p.TEMPLATE) for p in self.problems}       # numbers, names and plurals out
        self.key, self.work_names = self._proof_keys(sorted(set(self.exact.values())))
        self.wording = {p.ID: self.key[self.exact[p.ID]] for p in self.problems}    # the proof key: the work name out too
        self.words = {p.ID: set(re.findall(r"[a-z]+", self.exact[p.ID].lower())) for p in self.problems}
        self.mates = {}                                   # wording -> ids of its stored problems
        for p in self.problems:
            self.mates.setdefault(self.wording[p.ID], []).append(p.ID)
        self.asked = {}                                   # id -> the numbers its answer asks for, or None
        for ids in self.mates.values():
            rows = [asked_numbers(self.by_id[i].ANSWER) for i in ids]
            if len({len(r) for r in rows}) != 1 or not rows[0]:
                for i in ids:
                    self.asked[i] = None                  # the answers of the wording are not written the same way
                continue
            echo = [j for j in range(len(rows[0]))        # a place that repeats the same number of the sentence in every problem
                    if any(all(len(self.by_id[i].NUMBERS) > n and Fraction(self.by_id[i].NUMBERS[n]) == r[j] for i, r in zip(ids, rows))
                           for n in range(len(self.by_id[ids[0]].NUMBERS)))]
            keep = [j for j in range(len(rows[0])) if j not in echo] or list(range(len(rows[0])))
            for i, r in zip(ids, rows):
                self.asked[i] = [r[j] for j in keep]
        self.shapes = {}                                  # shape -> {"slots": k, "sources": {id: order}}
        self.book_line = {}                               # id -> line of its own book game
        for p in self.problems:
            found = self._book_game(p)
            if found:
                shape, order = found
                self.shapes.setdefault(shape, {"slots": len(order), "sources": {}})["sources"][p.ID] = order
                self.book_line[p.ID] = line_key(shape, order)
        self._code = {}

    def exact_of(self, template):
        """Names out (a capitalised word the book never writes in lower case), and the plural s after a number out."""
        text = re.sub(r"\b[A-Z][a-z]+\b", lambda m: m.group(0) if m.group(0).lower() in self.lower else "{name}", template)
        return re.sub(r"(\{\d+\} [A-Za-z]{2,}?[a-rt-z])s\b", r"\1", text)

    def wording_of(self, template):
        """The proof key of a sentence.  A sentence the book does not hold keeps its own text: it has no stored problems."""
        exact = self.exact_of(template)
        return self.key.get(exact, exact)

    @staticmethod
    def _proof_keys(exacts):
        """exact wording -> proof key, and the work names taken out of each key.

        Two exact wordings are one proof key when they have the same number slots and differ only in one short run of
        words (at most four on each side) that holds no cue word, no slot and no sign: the name of the work."""
        tokens = {w: re.findall(r"\{\d+\}|\{name\}|[A-Za-z]+|\S", w) for w in exacts}
        slots = {w: [t for t in tokens[w] if re.match(r"\{\d", t)] for w in exacts}

        def middle(a, b):
            i = 0
            while i < min(len(a), len(b)) and a[i] == b[i]:
                i += 1
            j = 0
            while j < min(len(a), len(b)) - i and a[-1 - j] == b[-1 - j]:
                j += 1
            return a[i:len(a) - j], b[i:len(b) - j], i, j

        def work(run):
            return (0 < len(run) <= 4 and any(len(t) >= 3 for t in run)
                    and all(re.match(r"[A-Za-z]+$|-$", t) and t.lower() not in CUES for t in run))

        parent = {w: w for w in exacts}

        def find(w):
            while parent[w] != w:
                parent[w] = parent[parent[w]]
                w = parent[w]
            return w

        for x, a in enumerate(exacts):
            for b in exacts[x + 1:]:
                if slots[a] != slots[b]:
                    continue
                da, db, i, j = middle(tokens[a], tokens[b])
                if work(da) and work(db) and i + j >= 0.7 * max(len(tokens[a]), len(tokens[b])):
                    parent[find(a)] = find(b)
        groups = {}
        for w in exacts:
            groups.setdefault(find(w), []).append(w)
        key, names = {}, {}
        for members in groups.values():
            if len(members) == 1:
                key[members[0]] = members[0]
                continue
            first = tokens[members[0]]
            i = min(middle(first, tokens[m])[2] for m in members[1:])
            j = min(middle(first, tokens[m])[3] for m in members[1:])
            j = min(j, len(first) - i)
            proof = " ".join(first[:i] + ["{work}"] + first[len(first) - j:])
            for m in members:
                key[m] = proof
            names[proof] = sorted(" ".join(tokens[m][i:len(tokens[m]) - j]) for m in members)
        return key, names

    def _book_game(self, problem):
        """The shape and the order of a stored problem whose equation passes the final check and uses every number once or more."""
        check = final_check(problem)
        if not check["matched"] or any(mark in problem.EQUATION for mark in ";≥≤<>%√π^"):
            return None
        equation = _normalize(problem.EQUATION)
        pool = [float(n) for n in problem.NUMBERS]
        order, pieces = [], []
        for token in re.findall(r"\d+(?:\.\d+)?|[A-Za-z]|[^\dA-Za-z]+", equation):
            if re.match(r"\d", token):
                index = next((i for i, n in enumerate(pool) if abs(n - float(token)) <= 1e-9 * max(1.0, abs(n))), None)
                if index is None:
                    pieces.append(token)                  # a fixed number of the shape
                else:
                    if index not in order:
                        order.append(index)
                    pieces.append("R%d" % order.index(index))
            elif re.match(r"[A-Za-z]", token):
                pieces.append("X")
            else:
                pieces.append(token)
        if len(order) != len(pool) or not order:          # a number of the sentence has no role: not a legal game
            return None
        return re.sub(r"\s+", " ", "".join(pieces)).strip(), tuple(order)

    def code(self, shape):
        if shape not in self._code:
            left, right = shape.split("=")
            self._code[shape] = compile("(%s)-(%s)" % (left, right), "<shape>", "eval")
        return self._code[shape]

    def play(self, shape, order, numbers):
        """Place the numbers and solve.  The number is the one root, or the one positive root; anything else is None."""
        code = self.code(shape)
        env = {"R%d" % k: float(numbers[i]) for k, i in enumerate(order)}

        def f(x):
            env["X"] = x
            return eval(code, {"__builtins__": {}}, env)

        roots = []
        for start in STARTS:
            x, good = float(start), False
            for _ in range(50):
                try:
                    y = f(x)
                    slope = (f(x + 1e-6) - y) / 1e-6
                except Exception:
                    break
                if abs(slope) < 1e-14:
                    break
                nxt = x - y / slope
                if abs(nxt - x) < 1e-9:
                    x, good = nxt, True
                    break
                x = nxt
            try:
                if good and abs(x) < 1e12 and abs(f(x)) < 1e-5 and not any(_same(x, r) for r in roots):
                    roots.append(round(x, 8))
            except Exception:
                pass
        if len(roots) == 1:
            return roots[0]
        positive = [r for r in roots if r > 0]
        return positive[0] if len(positive) == 1 else None


def line_key(shape, order):
    return "%s | %s" % (shape, ",".join(str(i) for i in order))


def split_line(key):
    shape, _, order = key.rpartition(" | ")
    return shape, tuple(int(i) for i in order.split(","))


# ---------------------------------------------------------------------------------------------------------------------------
# the four lists
# ---------------------------------------------------------------------------------------------------------------------------
def list1(book, words, n_numbers, wording=None):
    """Shapes forming in a sentence: (score, shape).  30: the shape has as many slots as the sentence has numbers.
    60: a book sentence of another wording that used the shape shares most of this sentence's words (6 of every 10,
    counted over both).  A shape whose only sources are problems of this wording is absent: that is the answer key."""
    rows = []
    for shape, info in book.shapes.items():
        if info["slots"] != n_numbers or n_numbers > MAX_SLOTS:
            continue
        sources = [i for i in info["sources"] if book.wording[i] != wording]
        if not sources:
            continue
        near = max(len(words & book.words[i]) / float(len(words | book.words[i]) or 1) for i in sources)
        rows.append((60 if near >= 0.6 else 30, round(near, 4), shape))
    rows.sort(key=lambda r: (-r[0], -r[1], r[2]))
    return [(score, shape) for score, _near, shape in rows]


def list2(book, words, n_numbers, wording=None):
    """Every legal line of the List 1 shapes, in List 1's order, the numbers in sentence order first: (score, line)."""
    lines = []
    for score, shape in list1(book, words, n_numbers, wording):
        for order in itertools.permutations(range(n_numbers)):
            lines.append((score, line_key(shape, order)))
    return lines


def _games(archive, wording):
    return archive.setdefault("games", {}).setdefault(wording, {"lines": {}, "dead_end": []})


def winners(book, archive):
    """line -> the wordings it won in: a book game there, or a played line there that never lost."""
    won = {}
    for pid, key in book.book_line.items():
        won.setdefault(key, set()).add(book.wording[pid])
    for wording, games in archive.get("games", {}).items():
        for key, record in games["lines"].items():
            if record["won"] and not record["lost"]:
                won.setdefault(key, set()).add(wording)
    return won


def _varied(book, wording):
    """True when at least two stored problems of the wording have different numbers."""
    return len({tuple(float(n) for n in book.by_id[i].NUMBERS) for i in book.mates.get(wording, [])}) >= 2


def _status(book, archive, wording, key, won):
    """(status, won, lost) of one line in one wording.  Only played games of this wording make it tried, won or lost."""
    record = archive.get("games", {}).get(wording, {"lines": {}})["lines"].get(key)
    if record and record["lost"]:
        return "proven loss", len(record["won"]), len(record["lost"])
    if record and _varied(book, wording) and set(record["won"]) >= set(book.mates.get(wording, [])):
        return "proven win", len(record["won"]), 0
    if record:
        return "tried", len(record["won"]), 0
    if won.get(key, set()) - {wording}:
        return "similar", 0, 0
    return "never tried", 0, 0


def list3(book, archive, wording, lines, won=None):
    """One row per legal line: (line, status, won, lost).  Played games of this wording, then other wordings (similar)."""
    won = winners(book, archive) if won is None else won
    return [(key,) + _status(book, archive, wording, key, won) for _score, key in lines]


def list4(book, archive, wording, rows, won=None):
    """For every List 3 row that a finished game played: (line, won here, lost here, other wordings it won in), best first."""
    won = winners(book, archive) if won is None else won
    out = []
    for key, status, wins, losses in rows:
        if status != "never tried":
            out.append((key, wins, losses, len(won.get(key, set()) - {wording})))
    out.sort(key=lambda r: (-(r[1] - r[2]), -r[3], r[0]))
    return out


def lists_for(problem, book=None, archive=None):
    """The four lists for one stored problem.  Its own equation, its siblings' equations and its own answer are not read."""
    book = book or Book()
    archive = _read_archive() if archive is None else archive
    wording = book.wording[problem.ID]
    lines = list2(book, book.words[problem.ID], len(problem.NUMBERS), wording)
    rows = list3(book, archive, wording, lines)
    return {"wording": wording,
            "list1": list1(book, book.words[problem.ID], len(problem.NUMBERS), wording),
            "list2": lines, "list3": rows, "list4": list4(book, archive, wording, rows)}


def choose(rows):
    """Step 5: a proven win, else a line that has only won here, else a similar line, else the first never-tried line."""
    for wanted in ("proven win", "tried", "similar", "never tried"):
        for key, status, _won, _lost in rows:
            if status == wanted:
                return key
    return None


def _choose_quick(book, archive, problem, won, state):
    """The same choice as choose(list3(...)), without building every row on every pass."""
    wording = book.wording[problem.ID]
    if problem.ID not in state["lines"]:
        lines = [key for _score, key in list2(book, book.words[problem.ID], len(problem.NUMBERS), wording)]
        state["lines"][problem.ID] = (lines, {key: n for n, key in enumerate(lines)})
        state["next"][problem.ID] = 0
        state["similar"][problem.ID] = [key for key in lines if state["book"].get(key, set()) - {wording}]   # book games elsewhere
    lines, place = state["lines"][problem.ID]
    record = archive.get("games", {}).get(wording, {"lines": {}})["lines"]
    best = None
    for key in record:
        if key in place:
            rank = {"proven win": 0, "tried": 1}.get(_status(book, archive, wording, key, won)[0])
            if rank is not None and (best is None or (rank, place[key]) < best):
                best = (rank, place[key])
    if best:
        return lines[best[1]]
    for key in state["similar"][problem.ID]:
        if key not in record:
            best = place[key]
            break
    for key in state["played_wins"]:                      # lines that played games of other wordings won since
        if key in place and key not in record and won[key] - {wording}:
            if best is None or place[key] < best:
                best = place[key]
    if best is not None:
        return lines[best]
    n = state["next"][problem.ID]
    while n < len(lines) and lines[n] in record:
        n += 1
    state["next"][problem.ID] = n
    return lines[n] if n < len(lines) else None


def one_pass(book, archive, problems=None, state=None):
    """One game for every problem, merged after the pass.  Returns how many games added something new."""
    state = state if state is not None else {"lines": {}, "next": {}, "similar": {}}
    if "book" not in state:
        state["book"] = winners(book, {})
    won = winners(book, archive)
    state["played_wins"] = {key for games in archive.get("games", {}).values() for key, r in games["lines"].items() if r["won"] and not r["lost"]}
    finished = []
    for problem in (problems or book.problems):
        key = _choose_quick(book, archive, problem, won, state)
        number = book.play(*split_line(key), numbers=problem.NUMBERS) if key else None
        finished.append((problem, key, number))
    new = 0
    for problem, key, number in finished:
        games = _games(archive, book.wording[problem.ID])
        if key is None:
            if problem.ID not in games["dead_end"]:
                games["dead_end"].append(problem.ID)
            continue
        record = games["lines"].setdefault(key, {"won": [], "lost": []})
        asked = book.asked[problem.ID]                    # a line gives one number: it loses when the answer asks for two
        won_game = number is not None and asked is not None and len(asked) == 1 and _same(number, float(asked[0]))
        side = record["won"] if won_game else record["lost"]
        if problem.ID not in side:
            side.append(problem.ID)
            new += 1
    return new


def proven_line(book, archive, wording):
    """The line that was played and won on every stored problem of the wording, two of them with different numbers, or None."""
    mates = book.mates.get(wording, [])
    if not _varied(book, wording):
        return None
    for key, record in sorted(archive.get("games", {}).get(wording, {"lines": {}})["lines"].items()):
        if not record["lost"] and set(record["won"]) >= set(mates):
            return key
    return None


# ---------------------------------------------------------------------------------------------------------------------------
# generated lines (word_generator.py): one sweep for every wording, after the passes
# ---------------------------------------------------------------------------------------------------------------------------
def _sweepable(book, wording):
    """The stored problems of a wording can be swept: two different sets of numbers, answers written the same way."""
    ids = book.mates.get(wording, [])
    first = book.by_id[ids[0]]
    return (_varied(book, wording) and book.asked[ids[0]] is not None
            and 1 <= len(first.NUMBERS) <= MAX_SLOTS and all(len(book.by_id[i].NUMBERS) == len(first.NUMBERS) for i in ids))


def _cue_words(book, wording):
    return set.union(*(book.words[i] for i in book.mates[wording]))


def generated_record(book, archive, wording):
    """The stored sweep of a wording when it is still valid: same problems, same fixed numbers, same generator."""
    record = archive.get("generated", {}).get(wording)
    if not record or record.get("version") != word_generator.VERSION:
        return None
    if record.get("ids") != sorted(book.mates.get(wording, [])):
        return None                                       # a stored problem was added or removed: the sweep is void
    if record.get("fixed") != word_generator.fixed_numbers(_cue_words(book, wording)):
        return None
    return record


def sweep_wordings(book, archive, max_size=None, wordings=None):
    """Sweep every wording that has no valid finished sweep up to max_size.  Returns how many wordings were swept."""
    max_size = word_generator.MAX_SIZE if max_size is None else max_size
    store = archive.setdefault("generated", {})
    swept = 0
    for wording in sorted(wordings if wordings is not None else book.mates):
        if not _sweepable(book, wording):
            store.pop(wording, None)
            continue
        old = generated_record(book, archive, wording)
        if old and (old["line"] or old["size"] >= max_size or old.get("number_without_role")):
            continue
        ids = sorted(book.mates[wording])
        rows = [list(book.by_id[i].NUMBERS) for i in ids]
        targets = [[book.asked[i][j] for i in ids] for j in range(len(book.asked[ids[0]]))]
        result = word_generator.sweep(rows, targets, _cue_words(book, wording), max_size)
        # written only now, after every size up to result["size"] was finished on every one of these problems
        store[wording] = {"version": word_generator.VERSION, "ids": ids, "fixed": result["fixed"], "size": result["size"],
                          "line": result["line"], "open": result["open"], "tuples": _independent(book, wording)}
        if result["number_without_role"]:                 # every asked number has a tree, but a number of the sentence has no role
            store[wording]["number_without_role"] = True
        swept += 1
    for wording in [w for w in store if w not in book.mates]:
        del store[wording]
    return swept


def _independent(book, wording):
    """How many sets of numbers the wording has that are not one another scaled: (4, 5), (8, 10) and (12, 15) are one."""
    seen = set()
    for i in book.mates.get(wording, []):
        row = [Fraction(n) for n in book.by_id[i].NUMBERS]
        unit = next((n for n in row if n != 0), Fraction(1))
        seen.add(tuple(n / unit for n in row))
    return len(seen)


def generated_candidate(book, archive, wording):
    """The generated line that won every stored problem of the wording (one tree for each asked number), or None.
    It is a candidate, not proof, until the wording has GENERATED_MIN_TUPLES independent sets of numbers."""
    record = generated_record(book, archive, wording)
    return record["line"] if record and record["line"] else None


def generated_line(book, archive, wording):
    """The proven generated line of a wording, or None."""
    if _independent(book, wording) < GENERATED_MIN_TUPLES:
        return None
    return generated_candidate(book, archive, wording)


def answer(text, book=None, archive=None):
    """The answer for a sentence, only from a proven line of its wording: a number, or a list when several are asked.
    Anything else is None (a decline).

    A number that is the same in every stored problem of the wording was never tested with another value, so a sentence
    that changes it is declined.  When a played book line and a generated line are both proven and give different
    numbers for this sentence, it is declined."""
    book = book or Book()
    archive = _read_archive() if archive is None else archive
    template, numbers = template_of(text)
    wording = book.wording_of(template)
    if wording not in book.mates:
        return None                                       # not a stored sentence shape, even with the work name out
    stored = [book.by_id[i].NUMBERS for i in book.mates[wording]]
    if any(len(s) != len(numbers) for s in stored):
        return None
    for place in range(len(numbers)):
        seen = {float(s[place]) for s in stored}
        if len(seen) == 1 and float(numbers[place]) not in seen:
            return None
    values = None
    trees = generated_line(book, archive, wording)
    if trees:
        try:
            values = [float(word_generator.evaluate(tree, numbers)) for tree in trees]
        except ZeroDivisionError:
            return None
    key = proven_line(book, archive, wording)
    if key is not None:
        shape, order = split_line(key)
        number = book.play(shape, order, numbers)
        if number is None or (values is not None and (len(values) != 1 or not _same(number, values[0]))):
            return None
        values = [number]
    if values is None:
        return None
    return values[0] if len(values) == 1 else values


# ---------------------------------------------------------------------------------------------------------------------------
# the archive file and the run
# ---------------------------------------------------------------------------------------------------------------------------
def _read_archive():
    """The archive file.  In the file a lost line is short: shape -> "order:times order:times"; here every line is a record."""
    if not os.path.isfile(ARCHIVE):
        return {"templates": {}, "games": {}, "generated": {}}
    with open(ARCHIVE, encoding="utf-8") as handle:
        archive = json.load(handle)
    games = {}
    for wording, stored in archive.get("games", {}).items():
        lines = {key: {"won": list(ids), "lost": []} for key, ids in stored.get("won", {}).items()}
        for shape, packed in stored.get("lost", {}).items():
            for item in packed.split():
                order, _, times = item.partition(":")
                lines.setdefault("%s | %s" % (shape, order), {"won": [], "lost": []})["lost"] += ["-"] * int(times or 1)
        games[wording] = {"lines": lines, "dead_end": list(stored.get("dead_end", []))}
    archive["games"] = games
    archive.setdefault("generated", {})
    return archive


def _write_archive(archive):
    out = dict(archive)
    out["games"] = {}
    for wording, games in archive.get("games", {}).items():
        won, lost = {}, {}
        for key, record in sorted(games["lines"].items()):
            if record["won"]:
                won[key] = sorted(record["won"])
            if record["lost"]:
                shape, _, order = key.rpartition(" | ")
                lost.setdefault(shape, []).append("%s:%d" % (order, len(record["lost"])))
        out["games"][wording] = {"won": won, "lost": {shape: " ".join(items) for shape, items in lost.items()},
                                 "dead_end": sorted(games["dead_end"])}
    with open(ARCHIVE, "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=1, sort_keys=True)


def summary(book, archive):
    played = {w for w in book.mates if proven_line(book, archive, w)}
    made = {w for w in book.mates if generated_line(book, archive, w)}
    swept = [w for w in book.mates if generated_record(book, archive, w)]
    maybe = {w for w in swept if generated_candidate(book, archive, w)} - made
    either = played | made
    count = lambda wordings: sum(len(book.mates[w]) for w in wordings)       # noqa: E731
    return {"wordings": len(book.mates),
            "proven_by_book_line": len(played), "problems_by_book_line": count(played),
            "proven_by_generated_line": len(made), "problems_by_generated_line": count(made),
            "proven": len(either), "problems_in_proven": count(either),
            "reference_problems_in_proven": sum(1 for w in either for i in book.mates[w] if book.by_id[i].SOLVER is None),
            "generated_candidates_too_few_tuples": len(maybe),
            "swept": len(swept), "loss_records": len(swept) - len(made) - len(maybe),
            "not_swept_one_set_of_numbers": sum(1 for w in book.mates if not _varied(book, w)),
            "games_played": sum(len(r["won"]) + len(r["lost"]) for g in archive.get("games", {}).values() for r in g["lines"].values())}


def run(reference_only=True, passes=40, book=None, write=True, max_size=None):
    """Play passes until one adds nothing (or the limit), sweep the wordings with generated lines, then write the archive.
    The games and the finished sweeps already in the file are kept, so the next run goes on where this one stopped.

    Returns the archive.  Its "templates" part is the final check of the stored equations, as before."""
    book = book or Book()
    archive = _read_archive()
    archive.update(_templates(book.problems, reference_only))
    played, state = 0, {"lines": {}, "next": {}, "similar": {}}
    while played < passes and one_pass(book, archive, state=state):
        played += 1
    swept = sweep_wordings(book, archive, max_size)
    archive["four_lists"] = dict(summary(book, archive), shapes=len(book.shapes), book_games=len(book.book_line),
                                 passes_this_run=played, wordings_swept_this_run=swept)
    archive["work_names"] = book.work_names               # what the proof key took out, for review
    if write:
        _write_archive(archive)
    return archive


if __name__ == "__main__":
    result = run(passes=int(sys.argv[1]) if len(sys.argv) > 1 else 40, max_size=int(sys.argv[2]) if len(sys.argv) > 2 else None)
    print("final check of the stored equations")
    print("  proven wordings: %d" % result["proven_wordings"])
    print("  candidate wordings (one matching problem): %d" % result["candidate_wordings"])
    print("  unmatched wordings: %d" % result["unmatched_wordings"])
    info = result["four_lists"]
    print("four lists")
    print("  shapes in the book: %d, from %d book games" % (info["shapes"], info["book_games"]))
    print("  passes this run: %d, games in the archive: %d" % (info["passes_this_run"], info["games_played"]))
    print("  wordings: %d" % info["wordings"])
    print("  proven by a played book line:  %d wordings (%d problems)" % (info["proven_by_book_line"], info["problems_by_book_line"]))
    print("  proven by a generated line:    %d wordings (%d problems)" % (info["proven_by_generated_line"], info["problems_by_generated_line"]))
    print("  proven by either:              %d wordings (%d problems, %d of them reference-only)" % (
        info["proven"], info["problems_in_proven"], info["reference_problems_in_proven"]))
    print("  generated lines that won but have under %d independent sets of numbers (not proof): %d" % (
        GENERATED_MIN_TUPLES, info["generated_candidates_too_few_tuples"]))
    print("  swept this run: %d; loss records: %d; not swept (one set of numbers): %d" % (
        info["wordings_swept_this_run"], info["loss_records"], info["not_swept_one_set_of_numbers"]))
