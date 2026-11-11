"""Builds the two algebra word problem folders from algebra_word_problems/algebra_word_problems.txt.

    operators_one_algebra_word_problem_per_file/<category>/<id>/<id>.py   the problem, its steps, its answer and compute(...)
    operators_one_algebra_word_problem_per_file/<category>/<id>/<id>.jpg  a diagram of the problem (the equation drawn with number boxes)
    operators_one_algebra_word_problem_per_file/INDEX.md                  one line per problem
    operator_row_math_for_algebra_word_problems/<category>/<id>/<id>.py   how the problem is laid out as a row of cards in the calculator

Run it from the project folder with the project's own virtual environment (it needs Pillow for the pictures):

    .venv\\Scripts\\python.exe operator_keys\\make_algebra_word_problem_files.py

It is safe to run again: it rewrites every generated file.  Run it again whenever the word solver gains or loses a family, because each problem file records which
solver answers it (SOLVER) and the rows are marked ready or reference from that.  The two folders' __init__.py, _solve.py and preview.py are written by hand and not touched.
"""
import os
import re
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(ROOT, "algebra_word_problems", "algebra_word_problems.txt")
MATCHER = os.path.join(ROOT, "algebra_word_problems", "algebra_matcher")
LIB = os.path.join(ROOT, "operators_one_algebra_word_problem_per_file")
ROWS = os.path.join(ROOT, "operator_row_math_for_algebra_word_problems")
sys.path.insert(0, MATCHER)

import number_puzzle as NP  # noqa: E402
import word_solver as WS  # noqa: E402

NUMBER = re.compile(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?")
BOX = "\u25a1"


def slug(text):
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def read_problems():
    text = open(SOURCE, encoding="utf-8").read()
    out = []
    for block in re.split(r"\n-{20,}\n", text):
        m = re.search(r"^#(\d{4}) \[([^\]]+)\]\n(.*)", block, flags=re.S | re.M)       # (the first block also holds the file's header)
        if not m:
            continue
        fields = {}
        for line in m.group(3).splitlines():
            k, _, v = line.partition(": ")
            if k in ("Problem", "Let", "Equation", "Solve", "Answer"):
                fields[k] = v.strip()
        if len(fields) == 5:
            out.append({"id": m.group(1), "category": m.group(2), **fields})
    return out


def template_of(problem):
    """The problem text with every number replaced by {0}, {1}, ...; also the numbers as written."""
    numbers, parts, last = [], [], 0
    for m in NUMBER.finditer(problem):
        parts.append(problem[last:m.start()].replace("{", "{{").replace("}", "}}"))
        parts.append("{%d}" % len(numbers))
        numbers.append(m.group(0).replace(",", ""))
        last = m.end()
    parts.append(problem[last:].replace("{", "{{").replace("}", "}}"))
    return "".join(parts), numbers


def equation_plan(equation, numbers):
    """The equation as tokens: ('txt', text) or ('num', text, i).  A number of the equation is a BOX only when it is one of the numbers written in the problem text
    (same value, matched left to right, each text number used once); i is that number's place in the text.  Any other number (the 1 and 2 of x + (x + 1) + (x + 2),
    a 0.75 that stands for 75%) stays plain text: it is not blue in the picture and not a box in the row.  Text numbers that no equation number matches (the 3 in
    "the sum of 3 consecutive integers") are not boxes either: compute() keeps them as written."""
    used, out, last = set(), [], 0

    def add(kind, text, index=None):
        if kind == "txt" and out and out[-1][0] == "txt":
            out[-1] = ("txt", out[-1][1] + text)
        elif kind == "txt":
            out.append(("txt", text))
        else:
            out.append(("num", text, index))

    for m in NUMBER.finditer(equation):
        if equation[last:m.start()]:
            add("txt", equation[last:m.start()])
        value = Fraction(m.group(0).replace(",", ""))
        i = next((j for j, n in enumerate(numbers) if j not in used and Fraction(n) == value), None)
        if i is None:
            add("txt", m.group(0))
        else:
            used.add(i)
            add("num", m.group(0), i)
        last = m.end()
    if equation[last:]:
        add("txt", equation[last:])
    return out


def equation_parts(plan):
    """The plan cut at each ';' (an equation with several parts is drawn one part per line)."""
    parts = [[]]
    for tok in plan:
        if tok[0] == "txt" and ";" in tok[1]:
            pieces = tok[1].split(";")
            parts[-1].append(("txt", pieces[0]))
            for piece in pieces[1:]:
                parts.append([("txt", piece)])
        else:
            parts[-1].append(tok)
    out = []
    for part in parts:
        part = [t for t in part]
        if part and part[0][0] == "txt":
            part[0] = ("txt", part[0][1].lstrip())
        if part and part[-1][0] == "txt":
            part[-1] = ("txt", part[-1][1].rstrip())
        part = [t for t in part if t[0] == "num" or t[1]]
        if part:
            out.append(part)
    return out


def solver_of(problem):
    """('word_solver', family) / ('number_puzzle', 'number_puzzle') / (None, None): who answers this problem today."""
    r = WS.solve(problem)
    if r is not None:
        return "word_solver", r.family
    if NP.solve(problem) is not None:
        return "number_puzzle", "number_puzzle"
    return None, None


# ------------------------------------------------------------------------------------------------------------
# the picture
# ------------------------------------------------------------------------------------------------------------
def make_picture(path, p, numbers):
    from PIL import Image, ImageDraw, ImageFont
    font_dir = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")

    def font(name, size):
        for candidate in (os.path.join(font_dir, name), os.path.join(font_dir, "arial.ttf")):
            try:
                return ImageFont.truetype(candidate, size)
            except OSError:
                continue
        return ImageFont.load_default()

    f_title, f_text, f_small, f_num, f_bold = font("segoeui.ttf", 16), font("segoeui.ttf", 21), font("segoeui.ttf", 17), font("segoeuib.ttf", 21), font("segoeuib.ttf", 21)
    width, pad = 900, 28
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))

    def wrap(text, fnt, limit):
        lines, cur = [], ""
        for word in text.split(" "):
            trial = (cur + " " + word).strip()
            if probe.textlength(trial, font=fnt) <= limit or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
        return lines

    problem_lines = wrap(p["Problem"], f_text, width - 2 * pad)
    let_lines = wrap("Let: " + p["Let"], f_small, width - 2 * pad)
    answer_lines = wrap("Answer: " + p["Answer"], f_bold, width - 2 * pad)
    equations = equation_parts(equation_plan(p["Equation"], numbers))

    sys.path.insert(0, ROOT)
    from operator_row_math.row_builder import _plan

    def stacked_part(tokens):
        """One part of the equation on a grid exactly like the row's: a fraction has its numerator above the bar and its denominator below, an exponent is one row up.
        Returns (grid rows, [(grid row, column, kind, text, pixel width)], [(grid row, first column, last column)] of the bars, column widths)."""
        cards, _, _, levels, fracs = row_cards(tokens)
        texts = [t[1] for t in tokens if t[0] == "num"]
        shown_texts, k = [], 0
        for kind, text in cards:
            if kind == "box":
                shown_texts.append(texts[k])
                k += 1
            else:
                shown_texts.append(text)
        placed, bars, _end = _plan(len(cards), levels, fracs)
        ncols = max([c for r, c in placed.values()] + [0]) + 1
        colw = [0] * (ncols + 1)
        for i, (r, c) in placed.items():
            w = probe.textlength(shown_texts[i], font=f_num if cards[i][0] == "box" else f_text) + (22 if cards[i][0] == "box" else 6)
            colw[c] = max(colw[c], w)
        for r, c, w in bars:
            for cc in range(c, c + w):
                colw[cc] = max(colw[cc], 14)
        top = min([r for r, c in placed.values()] + [r for r, c, w in bars])
        bottom = max([r for r, c in placed.values()] + [r for r, c, w in bars])
        items = [(r - top, c, cards[i][0], shown_texts[i]) for i, (r, c) in placed.items()]
        return bottom - top + 1, items, [(r - top, c, c + w - 1) for r, c, w in bars], colw

    eq_blocks = [stacked_part(e) for e in equations]
    need = max([sum(blk[3]) + 10 * len(blk[3]) for blk in eq_blocks] + [width - 2 * pad]) + 2 * pad
    width = max(width, int(need))
    cell = 46
    height = pad + 24 + 14 + 30 * len(problem_lines) + 10 + 24 * len(let_lines) + 18
    height += sum(cell * blk[0] + 16 for blk in eq_blocks) + 14 + 32 * len(answer_lines) + pad - 6

    img = Image.new("RGB", (width, height), "white")
    d = ImageDraw.Draw(img)
    y = pad - 8
    d.text((pad, y), "Algebra word problem %s   \u00b7   %s" % (p["id"], p["category"]), font=f_title, fill="#777777")
    y += 30
    d.line((pad, y, width - pad, y), fill="#dddddd")
    y += 14
    for line in problem_lines:
        d.text((pad, y), line, font=f_text, fill="#222222")
        y += 30
    y += 10
    for line in let_lines:
        d.text((pad, y), line, font=f_small, fill="#4a5a78")
        y += 24
    y += 18
    for nrows, items, bars, colw in eq_blocks:
        xs, x = [], pad
        for w in colw:
            xs.append(x)
            x += w + 10
        for r, c, kind, text in items:
            w, cy = colw[c], y + r * cell + 20
            if kind == "box":
                bw = probe.textlength(text, font=f_num) + 22
                x0 = xs[c] + (w - bw) / 2
                d.rounded_rectangle((x0 + 2, cy - 20, x0 + bw - 2, cy + 20), radius=5, fill="#d6e6fb", outline="#2a6ec9", width=2)
                d.text((x0 + bw / 2, cy), text, font=f_num, fill="#1b3f7a", anchor="mm")
            else:
                d.text((xs[c] + w / 2, cy), text, font=f_text, fill="#222222", anchor="mm")
        for r, c0, c1 in bars:
            by = y + r * cell + 20
            d.line((xs[c0], by, xs[c1] + colw[c1], by), fill="#222222", width=2)
        y += cell * nrows + 16
    y += 14
    for line in answer_lines:
        d.text((pad, y), line, font=f_bold, fill="#2a6a20")
        y += 32
    img.save(path, "JPEG", quality=82, optimize=True)


# ------------------------------------------------------------------------------------------------------------
# the files
# ------------------------------------------------------------------------------------------------------------
def py_str(text):
    return repr(text)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def problem_file(p, key, template, numbers, solver, family):
    status = ("ready: %s answers it (compute(...) solves it with any numbers the solver accepts)" % family) if solver else "reference only: no solver answers it yet (compute(...) raises)"
    return '''"""Algebra word problem %(id)s   [%(category)s]

Problem : %(problem)s
Let     : %(let)s
Equation: %(equation)s
Solve   : %(solve)s
Answer  : %(answer)s

Status  : %(status)s
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operators_one_algebra_word_problem_per_file._solve import solve_numbers  # noqa: E402

ID = %(id_r)s
KEY = %(key_r)s
NAME = %(name_r)s
CATEGORY = %(category_r)s
PROBLEM = %(problem_r)s
LET = %(let_r)s
EQUATION = %(equation_r)s
SOLVE = %(solve_r)s
ANSWER = %(answer_r)s
# who answers it today:  "word_solver" (a family in algebra_word_problems/algebra_matcher/word_solver.py), "number_puzzle", or None (reference only)
SOLVER = %(solver_r)s
FAMILY = %(family_r)s
# the problem text with every number replaced by {0}, {1}, ...; NUMBERS are the numbers as written, in order (these fill the boxes of the row)
TEMPLATE = %(template_r)s
NUMBERS = %(numbers_r)s


def compute(*numbers):
    """Solve the problem with these numbers (one per box, in the order of NUMBERS).  Returns the answer (a number, or a list when the problem has several answers)."""
    return solve_numbers(TEMPLATE, SOLVER, numbers or NUMBERS)
''' % {
        "id": p["id"], "category": p["category"], "problem": p["Problem"], "let": p["Let"], "equation": p["Equation"], "solve": p["Solve"], "answer": p["Answer"],
        "status": status, "id_r": py_str(p["id"]), "key_r": py_str(key), "name_r": py_str("%s %s" % (p["category"], p["id"])), "category_r": py_str(p["category"]),
        "problem_r": py_str(p["Problem"]), "let_r": py_str(p["Let"]), "equation_r": py_str(p["Equation"]), "solve_r": py_str(p["Solve"]), "answer_r": py_str(p["Answer"]),
        "solver_r": py_str(solver), "family_r": py_str(family), "template_r": py_str(template), "numbers_r": py_str(numbers)}


TOKEN = re.compile(NUMBER.pattern + r"|[A-Za-z]{2,}|\S")      # a word of 2+ letters (pay) is ONE card, never p a y


def row_cards(plan):
    """The row's cards from the plan, ONE TOKEN PER CARD (a card's centre shows one symbol): a blue box is a box card; a number that is not a box, a letter, + - x / = ( ) ;
    each is an operator card of its own; an exponent or subscript is its own card one grid row up or down.  Returns (cards, box_index, pattern, levels)."""
    sys.path.insert(0, ROOT)
    from operator_row_math.layout import level_of, shown
    cards, box_index, pattern, levels = [], [], [], []
    for tok in plan:
        if tok[0] == "txt":
            for m in TOKEN.finditer(tok[1]):
                cards.append(("op", shown(m.group(0))))
                levels.append(level_of(m.group(0)))
                pattern.append(m.group(0))
        else:
            cards.append(("box", ""))
            levels.append(0)
            box_index.append(tok[2])
            pattern.append(BOX)
    from operator_row_math.layout import group_fractions
    return cards, box_index, " ".join(pattern), levels, group_fractions(cards, levels)


def row_file(p, key, numbers, solver):
    cards, box_index, pattern, levels, fracs = row_cards(equation_plan(p["Equation"], numbers))
    boxes = pattern
    left = repr(cards)
    return '''"""Row for the algebra word problem: %(category)s %(id)s

Picture:      %(boxes)s   (the equation of the problem; each box is a number of the problem text; the answer is right of =)
Calculation:  %(calc_text)s
Try it:       python operator_row_math_for_algebra_word_problems/preview.py %(key)s
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = %(name_r)s
KEY = %(key_r)s
LIBRARY_KEY = %(key_r)s    # the problem in operators_one_algebra_word_problem_per_file (its compute(...) feeds the result box)
PATTERN = %(pattern_r)s
# "ready"     = the boxes on the left feed compute() and the answer shows right of "="
# "reference" = the problem and its steps are stored, but no solver answers it yet
CALC = %(calc_r)s
INPUTS = %(inputs_r)s    # what each box (left to right, as in the equation) is: which number of the problem text it holds
BOX_INDEX = %(box_index_r)s    # the place of each box's number in the problem text (NUMBERS of the problem file); the other text numbers stay as written
DEFAULTS = %(defaults_r)s    # the boxes' numbers as written in the stored problem
KINDS = %(kinds_r)s    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
FRAC = %(frac_r)s    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)
LEVELS = %(levels_r)s    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript (one row down), 0 = on the line
LEFT = %(left)s      # cards left of "="
RIGHT = [('box', '')]    # cards right of "="  (the result box = Row 1's number card: the answer)


def place(parent, stacked=False):
    """Create this problem's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=LEVELS, fracs=FRAC)
''' % {
        "category": p["category"], "id": p["id"], "name": "%s %s" % (p["category"], p["id"]), "boxes": boxes, "box": BOX, "key": key,
        "calc_text": "ready - fill the boxes, press = and the answer appears right of =" if solver else "reference - the problem is stored; no solver answers it yet",
        "name_r": py_str("%s %s" % (p["category"], p["id"])), "key_r": py_str(key),
        "pattern_r": py_str("%s  ->  answer %s" % (pattern, BOX)), "calc_r": py_str("ready" if solver else "reference"),
        "inputs_r": py_str(["number %d" % (i + 1) for i in box_index]), "box_index_r": py_str(box_index), "defaults_r": py_str([numbers[i] for i in box_index]),
        "kinds_r": py_str(["number"] * len(box_index)), "left": left, "levels_r": py_str(levels), "frac_r": py_str([[list(e) for e in f] for f in fracs])}


def main():
    problems = read_problems()
    if len(problems) != 479:
        raise SystemExit("expected 479 problems, one per wording, found %d" % len(problems))
    index = {}
    counts = {"word_solver": 0, "number_puzzle": 0, None: 0}
    for n, p in enumerate(problems, 1):
        cat = slug(p["category"])
        key = "%s/%s" % (cat, p["id"])
        template, numbers = template_of(p["Problem"])
        solver, family = solver_of(p["Problem"])
        counts[solver] += 1
        folder = os.path.join(LIB, cat, p["id"])
        write(os.path.join(folder, p["id"] + ".py"), problem_file(p, key, template, numbers, solver, family))
        make_picture(os.path.join(folder, p["id"] + ".jpg"), p, numbers)
        write(os.path.join(ROWS, cat, p["id"], p["id"] + ".py"), row_file(p, key, numbers, solver))
        index.setdefault(p["category"], []).append((p, key, solver, family))
        if n % 100 == 0:
            print("%d / 1000" % n)
    lines = ["# Algebra word problem index", "",
             "One folder per problem, holding `<id>.py` (the problem, its steps, its answer and `compute(...)`) and `<id>.jpg` (a diagram of the problem).",
             "**Ready** = a solver answers it today (`compute(...)` works); **Reference** = the problem and its steps are stored, no solver answers it yet.",
             "Written by `operator_keys/make_algebra_word_problem_files.py`; the solver column comes from `algebra_word_problems/algebra_matcher/word_solver.py`.", "",
             "%d problems: %d ready (%d word_solver, %d number_puzzle), %d reference." % (
                 len(problems), counts["word_solver"] + counts["number_puzzle"], counts["word_solver"], counts["number_puzzle"], counts[None]), ""]
    for category in sorted(index):
        lines += ["## %s" % category, "", "| Id | Problem | Answer | Status | Solver | Folder |", "|---|---|---|---|---|---|"]
        for p, key, solver, family in index[category]:
            prob = p["Problem"].replace("|", "\\|")
            lines.append("| %s | %s | %s | %s | %s | `%s/` |" % (p["id"], prob, p["Answer"].replace("|", "\\|"), "Ready" if solver else "Reference", family or "", key))
        lines.append("")
    write(os.path.join(LIB, "INDEX.md"), "\n".join(lines))
    print("done:", counts)


if __name__ == "__main__":
    main()
