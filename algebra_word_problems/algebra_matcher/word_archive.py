"""Find algebra word-problem answers the way the chess program uses its four lists and its archive.

    python word_archive.py [passes]        play the stored problems (default: until nothing changes, at most 40 passes)

A stored problem is a board.  A game is one LINE: an equation shape, and one of the problem's numbers in each slot of it.
    shape   "R2/R0 + X/R0 + X/R1 = 1"      X is the unknown, R0 R1 R2 are slots, 1 is a fixed number of the shape
    line    the shape and, for each slot, the place of a number in the sentence (N0, N1, ...), never its value
A slot is a role.  The shape may write a role twice.  Every number of the sentence gets exactly one slot.

The shapes are the equation shapes of the stored problems (the book).  A book game is a stored problem whose stored EQUATION
solves to its stored ANSWER.  A problem never reads its own book game: its EQUATION is never a hint for its own line.  The lines
it tries come from OTHER problems, and its game is compared only with its own ANSWER, after the game has ended.

List 1  the shapes forming in this sentence.  30: the shape has as many slots as the sentence has numbers.
        60: a book sentence that used the shape also shares most of this sentence's words.  It does not read the played games.
List 2  every legal line of the List 1 shapes, the furthest formed shape first, then the numbers in sentence order.
List 3  one row per legal line, from finished games: proven win, proven loss, tried, similar, never tried.
        "similar" is a line that won in another wording.  A similar row is never proof.
List 4  what the finished games actually got with each tried line: how many won, how many lost, and in which wordings.
        Empty until a game of this wording, or a book game with one of these lines, has finished.

A pass plays one game for every problem: a proven win, else a line that has only won in this wording, else a similar line,
else the first never-tried line.  A line that lost in this wording is never played there again.  The games are merged only after
the pass, so a problem never reads its own game.  A wrong number is stored as a loss.  A problem with no line left is stored as
a dead end.

A wording is the sentence without its numbers, its names and the plural s after a number.  A wording is proven only when the
same line was PLAYED and won on every stored problem of the wording, and there are at least two.  One win is only a candidate.
answer() returns a number only from a proven line.  Anything else is None.

The "templates" part of word_archive.json is the older final check (the stored equation solves to the stored answer); it is
what make_archive_families.py reads.  The "games" part is the four lists' archive.  Standard library only.
"""
import itertools
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROBLEMS = os.path.join(ROOT, "operators_one_algebra_word_problem_per_file")
ARCHIVE = os.path.join(HERE, "word_archive.json")
MAX_SLOTS = 6                 # 7 numbers are 5,040 orders for every shape: those problems are left as dead ends
STARTS = (0.0, 1.0, 2.0, 0.5, 10.0, 0.25, 5.0, -2.0, 20.0, 50.0, 8.0, 100.0, -10.0)
NUMBER = re.compile(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?")


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


def answer_numbers(text, given=()):
    """The numbers of a stored answer that a game may equal: outside brackets, a fraction read as a fraction, a clock time
    (1:00) left out.  A number the sentence itself gave ("12 lb at $3") is left out when the answer has other numbers."""
    text = re.sub(r"\([^)]*\)", "", text)
    text = re.sub(r"\d+:\d+", " ", text)
    text = re.sub(r"(?<=\d),(?=\d{3})", "", text)
    out = []
    for whole, _dec, bottom in re.findall(r"(-?\d+(\.\d+)?)(?:/(\d+))?", text.replace("−", "-")):
        out.append(float(whole) / float(bottom) if bottom else float(whole))
    pool = [float(g) for g in given]
    asked = [a for a in out if not any(_same(a, g) for g in pool)]
    return asked or out


def _same(a, b):
    return abs(a - b) <= 1e-4 * max(1.0, abs(b))


class Book:
    """The stored problems, their wordings, and the shapes and book games read from their stored equations."""

    def __init__(self, problems=None):
        self.problems = list(problems) if problems is not None else load_problems()
        self.problems.sort(key=lambda p: p.ID)
        self.by_id = {p.ID: p for p in self.problems}
        self.lower = set(re.findall(r"\b[a-z]+\b", " ".join(p.TEMPLATE for p in self.problems)))
        self.wording = {p.ID: self.wording_of(p.TEMPLATE) for p in self.problems}
        self.words = {p.ID: set(re.findall(r"[a-z]+", self.wording[p.ID].lower())) for p in self.problems}
        self.mates = {}                                   # wording -> ids of its stored problems
        for p in self.problems:
            self.mates.setdefault(self.wording[p.ID], []).append(p.ID)
        self.shapes = {}                                  # shape -> {"slots": k, "sources": {id: order}}
        self.book_line = {}                               # id -> line of its own book game
        for p in self.problems:
            found = self._book_game(p)
            if found:
                shape, order = found
                self.shapes.setdefault(shape, {"slots": len(order), "sources": {}})["sources"][p.ID] = order
                self.book_line[p.ID] = line_key(shape, order)
        self._code = {}

    def wording_of(self, template):
        """Names out (a capitalised word the book never writes in lower case), and the plural s after a number out."""
        text = re.sub(r"\b[A-Z][a-z]+\b", lambda m: m.group(0) if m.group(0).lower() in self.lower else "{name}", template)
        return re.sub(r"(\{\d+\} [A-Za-z]{3,}?)s\b", r"\1", text)

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
def list1(book, words, n_numbers, own_id=None):
    """Shapes forming in a sentence: (score, shape).  30: the shape has as many slots as the sentence has numbers.
    60: a book sentence that used the shape also shares most of this sentence's words (6 of every 10, counted over both)."""
    rows = []
    for shape, info in book.shapes.items():
        if info["slots"] != n_numbers or n_numbers > MAX_SLOTS:
            continue
        sources = [i for i in info["sources"] if i != own_id]
        if not sources:
            continue                                      # only this problem's own equation has the shape: not a hint for it
        near = max(len(words & book.words[i]) / float(len(words | book.words[i]) or 1) for i in sources)
        rows.append((60 if near >= 0.6 else 30, round(near, 4), shape))
    rows.sort(key=lambda r: (-r[0], -r[1], r[2]))
    return [(score, shape) for score, _near, shape in rows]


def list2(book, words, n_numbers, own_id=None):
    """Every legal line of the List 1 shapes, in List 1's order, the numbers in sentence order first: (score, line)."""
    lines = []
    for score, shape in list1(book, words, n_numbers, own_id):
        for order in itertools.permutations(range(n_numbers)):
            lines.append((score, line_key(shape, order)))
    return lines


def _games(archive, wording):
    return archive.setdefault("games", {}).setdefault(wording, {"lines": {}, "dead_end": []})


def winners(book, archive):
    """line -> {wording: who won with it there}: the ids of book games, and "played" for a played line that never lost."""
    won = {}
    for pid, key in book.book_line.items():
        won.setdefault(key, {}).setdefault(book.wording[pid], set()).add(pid)
    for wording, games in archive.get("games", {}).items():
        for key, record in games["lines"].items():
            if record["won"] and not record["lost"]:
                won.setdefault(key, {}).setdefault(wording, set()).add("played")
    return won


def _status(book, archive, wording, key, own_id, won):
    """(status, won, lost) of one line for one problem.  The problem's own book game is never counted."""
    record = archive.get("games", {}).get(wording, {"lines": {}})["lines"].get(key)
    mates = book.mates.get(wording, [])
    if record and record["lost"]:
        return "proven loss", len(record["won"]), len(record["lost"])
    if record and len(mates) >= 2 and set(record["won"]) >= set(mates):
        return "proven win", len(record["won"]), 0
    where = won.get(key, {})
    book_wins = where.get(wording, set()) - {own_id, "played"}       # book games of the other problems of this wording
    if record or book_wins:
        return "tried", len(book_wins | set(record["won"] if record else ())), 0
    if any(w != wording and who - {own_id} for w, who in where.items()):
        return "similar", 0, 0
    return "never tried", 0, 0


def list3(book, archive, wording, lines, own_id=None, won=None):
    """One row per legal line: (line, status, won, lost).  Finished games of this wording, then other wordings (similar)."""
    won = winners(book, archive) if won is None else won
    return [(key,) + _status(book, archive, wording, key, own_id, won) for _score, key in lines]


def list4(book, archive, wording, rows, own_id=None, won=None):
    """For every List 3 row that a finished game played: (line, won here, lost here, other wordings it won in), best first."""
    won = winners(book, archive) if won is None else won
    out = []
    for key, status, wins, losses in rows:
        if status != "never tried":
            others = sum(1 for w, who in won.get(key, {}).items() if w != wording and who - {own_id})
            out.append((key, wins, losses, others))
    out.sort(key=lambda r: (-(r[1] - r[2]), -r[3], r[0]))
    return out


def lists_for(problem, book=None, archive=None):
    """The four lists for one stored problem.  Its own equation and its own answer are not read."""
    book = book or Book()
    archive = _read_archive() if archive is None else archive
    wording = book.wording[problem.ID]
    lines = list2(book, book.words[problem.ID], len(problem.NUMBERS), problem.ID)
    rows = list3(book, archive, wording, lines, problem.ID)
    return {"wording": wording,
            "list1": list1(book, book.words[problem.ID], len(problem.NUMBERS), problem.ID),
            "list2": lines, "list3": rows, "list4": list4(book, archive, wording, rows, problem.ID)}


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
        lines = [key for _score, key in list2(book, book.words[problem.ID], len(problem.NUMBERS), problem.ID)]
        state["lines"][problem.ID] = (lines, {key: n for n, key in enumerate(lines)})
        state["next"][problem.ID] = 0
    lines, place = state["lines"][problem.ID]
    record = archive.get("games", {}).get(wording, {"lines": {}})["lines"]
    known = [key for key in record if key in place]
    known += [book.book_line[i] for i in book.mates[wording] if i != problem.ID and book.book_line.get(i) in place]
    best = None
    for key in known:
        status = _status(book, archive, wording, key, problem.ID, won)[0]
        rank = {"proven win": 0, "tried": 1}.get(status)
        if rank is not None and (best is None or (rank, place[key]) < best):
            best = (rank, place[key])
    if best:
        return lines[best[1]]
    similar = state["similar"].get(problem.ID)
    if similar is None:                                   # lines of this problem that some other wording's book game won
        similar = [key for key in lines if any(w != wording and who - {problem.ID, "played"} for w, who in won.get(key, {}).items())]
        state["similar"][problem.ID] = similar
    for key in similar:
        if key not in record:
            best = place[key]
            break
    for key, where in state["played_wins"].items():       # lines that played games of other wordings won
        if key in place and key not in record and any(w != wording and "played" in who for w, who in where.items()):
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
    won = winners(book, archive)
    state["played_wins"] = {key: where for key, where in won.items() if any("played" in who for who in where.values())}
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
        won_game = number is not None and any(_same(number, a) for a in answer_numbers(problem.ANSWER, problem.NUMBERS))
        side = record["won"] if won_game else record["lost"]
        if problem.ID not in side:
            side.append(problem.ID)
            new += 1
    return new


def proven_line(book, archive, wording):
    """The line that was played and won on every stored problem of the wording (two or more), or None."""
    mates = book.mates.get(wording, [])
    if len(mates) < 2:
        return None
    for key, record in sorted(archive.get("games", {}).get(wording, {"lines": {}})["lines"].items()):
        if not record["lost"] and set(record["won"]) >= set(mates):
            return key
    return None


def answer(text, book=None, archive=None):
    """The number for a sentence, only from the proven line of its wording.  Anything else is None (a decline).

    A number that is the same in every stored problem of the wording was never tested with another value, so a sentence
    that changes it is declined."""
    book = book or Book()
    archive = _read_archive() if archive is None else archive
    template, numbers = template_of(text)
    wording = book.wording_of(template)
    key = proven_line(book, archive, wording)
    if key is None:
        return None
    shape, order = split_line(key)
    if len(order) != len(numbers):
        return None
    stored = [book.by_id[i].NUMBERS for i in book.mates[wording]]
    for place in range(len(numbers)):
        seen = {float(s[place]) for s in stored}
        if len(seen) == 1 and float(numbers[place]) not in seen:
            return None
    return book.play(shape, order, numbers)


# ---------------------------------------------------------------------------------------------------------------------------
# the archive file and the run
# ---------------------------------------------------------------------------------------------------------------------------
def _read_archive():
    """The archive file.  In the file a lost line is short: shape -> "order:times order:times"; here every line is a record."""
    if not os.path.isfile(ARCHIVE):
        return {"templates": {}, "games": {}}
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
    proven = [w for w in book.mates if proven_line(book, archive, w)]
    won_once = dead = 0
    for wording in book.mates:
        games = archive.get("games", {}).get(wording, {"lines": {}, "dead_end": []})
        if wording in proven:
            continue
        if any(r["won"] and not r["lost"] for r in games["lines"].values()):
            won_once += 1
        elif games["dead_end"]:
            dead += 1
    return {"wordings": len(book.mates), "proven": len(proven), "problems_in_proven": sum(len(book.mates[w]) for w in proven),
            "candidates": won_once, "dead_ends": dead,
            "games_played": sum(len(r["won"]) + len(r["lost"]) for g in archive.get("games", {}).values() for r in g["lines"].values())}


def run(reference_only=True, passes=40, book=None, write=True):
    """Play passes until one adds nothing (or the limit), then write the archive.  The games already in the file are kept,
    so the next run goes on where this one stopped.

    Returns the archive.  Its "templates" part is the final check of the stored equations, as before."""
    book = book or Book()
    archive = _read_archive()
    archive.update(_templates(book.problems, reference_only))
    played, state = 0, {"lines": {}, "next": {}, "similar": {}}
    while played < passes and one_pass(book, archive, state=state):
        played += 1
    archive["four_lists"] = dict(summary(book, archive), shapes=len(book.shapes), book_games=len(book.book_line), passes_this_run=played)
    if write:
        _write_archive(archive)
    return archive


if __name__ == "__main__":
    result = run(passes=int(sys.argv[1]) if len(sys.argv) > 1 else 40)
    print("final check of the stored equations")
    print("  proven wordings: %d" % result["proven_wordings"])
    print("  candidate wordings (one matching problem): %d" % result["candidate_wordings"])
    print("  unmatched wordings: %d" % result["unmatched_wordings"])
    info = result["four_lists"]
    print("four lists")
    print("  shapes in the book: %d, from %d book games" % (info["shapes"], info["book_games"]))
    print("  passes this run: %d, games in the archive: %d" % (info["passes_this_run"], info["games_played"]))
    print("  wordings: %d, proven by play: %d (%d problems)" % (info["wordings"], info["proven"], info["problems_in_proven"]))
    print("  wordings with a win that is not proof: %d, dead ends: %d" % (info["candidates"], info["dead_ends"]))
