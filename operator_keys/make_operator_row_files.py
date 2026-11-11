"""Rewrites the row files of the operators (operator_row_math/<area>/<group>/<operator>/<operator>.py) so each row looks like the operator's PICTURE.

The picture (operators_one_operator_per_file/.../<operator>.jpg) is the reference.  operator_row_specs.txt holds one line per operator, written from the picture:

    math/algebra/power | [a] ^ [b] => {}
    geometry/geometry/cone_surface_area | {} = π × [r] × ( [r] + [l] )

    []       a box the picture draws that is not an input: an ordinary card showing a square (never typed into, not blue)
    [_x]     the same, when the picture shows the letter or constant x in that box (g, h, Δx ...)
    [name]   a box for the operator's input `name` (the names are the INPUTS of the row file).  Writing the same name again draws another box that shares the same value
             (the picture writes the variable twice), so the row's SLOTS list repeats that input.
    {}       an answer box inside the formula (the A of A = π r²).  It is never typed into; = fills it with the answer.
    =>       everything after it is the result box right of the row (the picture ends with "= [ ]").  Only {} may follow.
    anything else   one card per token (a symbol, a letter, a number, a word such as sin or det).

Run from the project root:   python operator_keys/make_operator_row_files.py          (rewrites the rows named in the specs, checks them)
                             python operator_keys/make_operator_row_files.py --todo   (lists the operators that have no spec yet)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import operator_row_math as R  # noqa: E402
from operator_row_math.layout import group_fractions, level_of, shown  # noqa: E402

EXTRAS = {}
WORDS_OF = {}      # key -> {card index: (label, context)}: the words a card carries (written  ρ{density|mass per volume}  in a spec line)
STACK = set()      # keys whose spec starts with @stack: exponents share the column of the symbol they power (STACK_EXPONENTS = True in the row file)
SPECS = os.path.join(ROOT, "operator_keys", "operator_row_specs.txt")
BOX = "□"


def read_specs():
    out = {}
    for n, line in enumerate(open(SPECS, encoding="utf-8").read().splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, dsl = line.partition("|")
        if not sep:
            raise SystemExit("%s line %d: no '|'" % (SPECS, n))
        key = key.strip()
        if key in out:
            raise SystemExit("%s line %d: %s is written twice" % (SPECS, n, key))
        out[key] = dsl.strip()
    return out


def build(key, dsl, inputs, calc="ready"):
    """(left cards, right cards, slots, pattern) from one spec line."""
    if dsl.split()[:1] == ["@stack"]:
        dsl = dsl.split(None, 1)[1]
        STACK.add(key)
        stack = True
    else:
        STACK.discard(key)
        stack = False
    left_text, arrow, right_text = dsl.partition("=>")
    left, slots, pattern, levels = [], [], [], []
    first_seen = set()
    card_words = {}
    extra_words = {}          # with:NAME{label|context}  = the words of the "with" box the row adds for the input NAME (a picture does not draw it)
    WORDS_OF[key] = card_words
    for raw in re.findall(r"\S*?\{[^{}|]*\|[^{}]*\}|\S+", left_text):          # a token, or a token with {label|context}; a plain { } card has no |
        mw = re.fullmatch(r"with:(\S+?)\{([^{}|]*)\|([^{}]*)\}", raw)
        if mw:
            extra_words[mw.group(1)] = (mw.group(2).strip(), mw.group(3).strip())
            continue
        tok, words = raw, None
        m = re.fullmatch(r"\{sub:([^|}]+)(?:\|([^|}]*)\|([^}]*))?\}", raw)          # {sub:y|label|context}
        if m:
            tok, words = "{sub:%s}" % m.group(1), ((m.group(2), m.group(3)) if m.group(2) is not None else None)
        elif raw != "{}":
            m = re.fullmatch(r"(\S+?)\{([^{}|]*)\|([^{}]*)\}", raw)                          # symbol{label|context}
            if m:
                tok, words = m.group(1), (m.group(2), m.group(3))
        m = None if tok.startswith("[_") else re.fullmatch(r"\[([^\]]+)\]", tok)
        if m:
            name = m.group(1)
            if name not in inputs:
                raise SystemExit("%s: [%s] is not an input (%s)" % (key, name, inputs))
            left.append(("box", ""))
            levels.append(0)
            slots.append(inputs.index(name))
            first_seen.add(name)
            pattern.append(BOX)
        elif tok == "{}":
            left.append(("out", ""))
            levels.append(0)
            pattern.append(BOX)
        elif tok == "[]":
            left.append(("dec", ""))
            levels.append(0)
            pattern.append(BOX)
        elif re.fullmatch(r"\[_([^\]]+)\]", tok):          # [_x] = a variable letter or constant the picture draws in a box: an ordinary card, not an input
            letter = tok[2:-1]
            left.append(("dec", letter))
            levels.append(0)
            pattern.append(letter)
        elif re.fullmatch(r"\{sub:(.+)\}", tok):          # {sub:y} = the letter y one grid row down (Unicode has no subscript y or z)
            left.append(("op", tok[5:-1]))
            levels.append(1)
            pattern.append(tok[5:-1])
        else:
            left.append(("op", shown(tok)))          # an exponent / subscript has its own cell (one row up / down) and shows ordinary characters
            levels.append(level_of(tok))
            pattern.append(tok)
        if words:
            card_words[len(left) - 1] = (words[0].strip(), words[1].strip())
    fracs = group_fractions(left, levels)           # the picture's own cards only: the "with" boxes added below are never part of a fraction
    if stack:
        # group_fractions takes everything back to the "+" as the numerator, so  u ∂u / ∂x  would be (u ∂u) / ∂x.  The equation is u TIMES ∂u/∂x: the velocity that multiplies
        # a derivative stays on the line in its own column and the bar goes only under the derivative.
        for i in range(len(left) - 1):
            if (left[i][0] == "op" and left[i][1] in ("u", "v", "w") and left[i + 1] == ("op", "∂") and fracs[i] and fracs[i + 1]
                    and fracs[i][-1] == fracs[i + 1][-1] and fracs[i][-1][1] == "n"):
                fracs[i] = fracs[i][:-1]
    missing = [n for n in inputs if n not in first_seen]
    if calc == "reference":                      # a reference operator cannot calculate: nothing to add
        missing = []
    for i, name in enumerate(missing):          # an input the picture does not draw still gets a box, after the picture: "with [ ] , [ ]"
        left.append(("op", "with" if i == 0 else ","))
        left.append(("box", ""))
        levels.extend([0, 0])
        fracs.extend([[], []])
        slots.append(inputs.index(name))
        pattern.append("with" if i == 0 else ",")
        pattern.append(BOX)
        if name in extra_words:
            card_words[len(left) - 1] = extra_words[name]
    EXTRAS[key] = missing
    right = []
    if arrow:
        if right_text.split() != ["{}"]:
            raise SystemExit("%s: after => only {} may follow" % key)
        right = [("box", "")]
        pattern.append("= " + BOX)
    if not left:
        raise SystemExit("%s: empty formula" % key)
    return left, right, slots, " ".join(pattern), levels, fracs


def rewrite(key, dsl):
    base = os.path.join(ROOT, "operator_row_math", *key.split("/"))
    path = os.path.join(base, os.path.basename(base) + ".py")
    src = open(path, encoding="utf-8", newline="").read()
    nl = "\r\n" if "\r\n" in src else "\n"
    src = src.replace("\r\n", "\n")
    mod = R.get(key)
    left, right, slots, pattern, levels, fracs = build(key, dsl, list(mod.INPUTS), mod.CALC)
    ident = list(range(len(mod.INPUTS)))

    def put(name, value, comment=None):
        nonlocal src
        rx = re.compile(r"^%s = .*$" % name, re.M)
        m = rx.search(src)
        if not m:
            raise SystemExit("%s: no %s line in %s" % (key, name, path))
        old = m.group(0)
        tail = re.search(r"\s+# .*$", old)
        src = src.replace(old, "%s = %s%s" % (name, value, tail.group(0) if tail else ""), 1)

    put("PATTERN", repr(pattern))
    put("LEFT", repr(left))
    put("RIGHT", repr(right))
    src = re.sub(r"^SLOTS = .*\n", "", src, flags=re.M)
    src = re.sub(r"^LEVELS = .*\n", "", src, flags=re.M)
    src = re.sub(r"^FRAC = .*\n", "", src, flags=re.M)
    src = re.sub(r"^STACK_EXPONENTS = .*\n", "", src, flags=re.M)
    src = re.sub(r"^WORDS = .*\n", "", src, flags=re.M)
    extra = ""
    if slots != ident:
        extra += "SLOTS = %r    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)\n" % slots
    if any(levels):
        extra += "LEVELS = %r    # the grid row of each card of LEFT: -1 = an exponent (one row up), +1 = a subscript or lower limit (one row down), 0 = on the line\n" % levels
    if WORDS_OF.get(key):
        extra += "WORDS = %r    # the words each card of LEFT carries, {card index: (label, context)}: shown in the card's Label and Context boxes when the operator is used\n" % WORDS_OF[key]
    if key in STACK:
        extra += "STACK_EXPONENTS = True    # an exponent card shares the column of the symbol it powers (one grid row up) instead of having a column of its own\n"
    if any(fracs):
        extra += "FRAC = %r    # for each card of LEFT the fractions it is inside: (group, n = numerator on the row above | d = denominator on the row below | bar | hide = not drawn)\n" % [[list(e) for e in f] for f in fracs]
    if extra:
        src = re.sub(r"^(KINDS = .*\n)", lambda m: m.group(1) + extra, src, count=1, flags=re.M)
    call = "return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get(\"LEVELS\"), fracs=globals().get(\"FRAC\"))"
    if key in STACK:
        call = call[:-1] + ", stack_exponents=True)"
    src = re.sub(r"return build_row\(parent, LEFT, RIGHT, stacked[^\n]*\)", lambda m: call, src)     # also fixes files that only pass levels=
    src = re.sub(r"^Picture:      .*$", "Picture:      " + pattern.replace("\\", "\\\\"), src, count=1, flags=re.M)
    open(path, "w", encoding="utf-8", newline="").write(src.replace("\n", nl))


def read_notes():
    """{key: note} from operator_keys/formula_only_notes.txt (lines  <key> — <note>)."""
    notes = {}
    with open(os.path.join(ROOT, "operator_keys", "formula_only_notes.txt"), encoding="utf-8") as f:
        for line in f:
            key, sep, note = line.rstrip().partition(" — ")
            if sep and key.count("/") >= 2 and " " not in key:
                notes[key] = note.strip()
    return notes


def write_note(key, note):
    """Put  NOTE = '...'  (one sentence on the row of a formula-only operator, shown under the row and added to the answer of =) after the KINDS line."""
    base = os.path.join(ROOT, "operator_row_math", *key.split("/"))
    path = os.path.join(base, os.path.basename(base) + ".py")
    src = open(path, encoding="utf-8", newline="").read()
    crlf = chr(13) + chr(10)
    lf = chr(10)
    nl = crlf if crlf in src else lf
    src = src.replace(crlf, lf)
    src = re.sub(r"^NOTE = .*" + lf, "", src, flags=re.M)
    line = "NOTE = %r    # formula only: what the row says (no box is added and compute() is unchanged)" % note + lf
    src = re.sub(r"^(KINDS = .*" + lf + ")", lambda m: m.group(1) + line, src, count=1, flags=re.M)
    open(path, "w", encoding="utf-8", newline="").write(src.replace(lf, nl))


def main():
    specs = read_specs()
    if "--todo" in sys.argv:
        todo = [k for k in R.keys() if k not in specs]
        print("%d of %d operators have a spec, %d to do" % (len(specs), len(R.keys()), len(todo)))
        for k in todo:
            print(k)
        return
    unknown = [k for k in specs if k not in set(R.keys())]
    if unknown:
        raise SystemExit("not operators: %s" % unknown)
    for key, dsl in specs.items():
        rewrite(key, dsl)
    notes = read_notes()
    for key, note in notes.items():
        write_note(key, note)
    extra = {k: v for k, v in EXTRAS.items() if v}
    report = os.path.join(ROOT, "operator_keys", "operator_rows_with_extra_boxes.txt")
    with open(report, "w", encoding="utf-8") as f:
        f.write("Operators whose picture does not draw every input.  The row follows the picture, then adds  with [ ] , [ ]  for the inputs listed here (so the operator still calculates).\n")
        f.write("Written by make_operator_row_files.py.  %d operators.\n\n" % len(extra))
        for k in sorted(extra):
            f.write("%s   extra boxes for: %s\n" % (k, ", ".join(extra[k])))
    print("%d formula-only notes written" % len(notes))
    print("rewrote %d row files; %d have extra boxes (see operator_rows_with_extra_boxes.txt)" % (len(specs), len(extra)))


if __name__ == "__main__":
    main()
