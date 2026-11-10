"""Redraws the pictures of the operators whose row is stacked (a fraction, an exponent, a subscript) so the picture is stacked the same way.

The picture (operators_one_operator_per_file/<group>/<name>/<name>.jpg) used to write every `/` on one line and every exponent beside its base.  The rows follow rule 1
(math that can be written on several lines is always written on several lines), so the picture is redrawn on the SAME grid as the row (operator_row_math.row_builder._plan):
the numerator on the line above a bar, the denominator on the line below, an exponent one line up, a subscript one line down.

What is kept from the old picture: the title and its rule, the description line under the formula, and every blue box (cut out of the old picture, so its label --
the F, m1, theta ... -- is the one already drawn).  What is redrawn: the operators, letters, numbers, bars and the places of everything.
The old picture is the source: the first run copies it to operator_pictures_one_line/<key>.jpg, and every later run starts from that copy, so the script can be run again.

    python operator_keys/make_operator_pictures.py            # redraw every operator whose row has a fraction / exponent / subscript
    python operator_keys/make_operator_pictures.py --check    # only count the boxes: the old picture and the row must agree
    python operator_keys/make_operator_pictures.py key ...    # only these operators
"""
import os
import shutil
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import operator_row_math as R  # noqa: E402
from operator_row_math.layout import shown  # noqa: E402
from operator_row_math.row_builder import _plan  # noqa: E402

LIB = os.path.join(ROOT, "operators_one_operator_per_file")
FONT_DIR = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts")
KEEP = os.path.join(ROOT, "operator_pictures_one_line")      # the old one-line pictures, kept as the source of the title, the description and the boxes


def font(size):
    """The formula font: Cambria, like every other operator picture (the others are only fallbacks for a computer without Windows fonts)."""
    for path, index in ((os.path.join(FONT_DIR, "cambria.ttc"), 0), (os.path.join(FONT_DIR, "georgia.ttf"), 0), (os.path.join(FONT_DIR, "times.ttf"), 0),
                        ("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 0), ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 0)):
        try:
            return ImageFont.truetype(path, size, index=index)
        except OSError:
            continue
    return ImageFont.load_default()


def small_font(size):
    """The font of the word list under a formula (Segoe UI, like the description line)."""
    for path in (os.path.join(FONT_DIR, "segoeui.ttf"), "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def is_blue(p):
    """A pixel of a blue box (its fill or its outline); text is grey/black, so r is close to b there."""
    d = p[2] - p[0]
    return (d >= 45 and p[2] >= 120 and p[0] <= 120) or (d >= 18 and 200 <= p[0] <= 238 and p[2] >= 236)


def split_runs(flags, gap=2):
    runs, start, last = [], None, None
    for i, f in enumerate(flags):
        if f:
            if start is None:
                start = i
            elif i - last > gap + 1:
                runs.append((start, last))
                start = i
            last = i
    if start is not None:
        runs.append((start, last))
    return runs


def old_parts(img):
    """(style, rule row, formula band (y0, y1), [box crops left to right], description crop or None, title right edge) of an old one-line picture."""
    img = img.convert("RGB")
    W, H = img.size
    px = img.load()
    style = "A" if (W, H) == (1040, 236) else "B"
    rule = 67 if style == "A" else 40
    top, bottom = (rule + 6, 180) if style == "A" else (rule + 6, H)
    cols = [sum(1 for y in range(top, bottom) if is_blue(px[x, y])) >= 14 for x in range(W)]
    boxes = []
    for x0, x1 in split_runs(cols):
        ys = [y for y in range(top, bottom) if any(is_blue(px[x, y]) for x in range(x0, x1 + 1))]
        box = (x0, min(ys), x1 + 1, max(ys) + 1)
        boxes.append(img.crop(box))
    desc = None
    if style == "A":
        rows = [y for y in range(180, H) if any(sum(px[x, y]) < 600 for x in range(W))]
        if rows:
            xs = [x for y in range(rows[0], rows[-1] + 1) for x in range(W) if sum(px[x, y]) < 600]
            desc = img.crop((max(0, min(xs) - 2), rows[0] - 3, min(W, max(xs) + 3), min(H, rows[-1] + 4)))
    title_rows = range(0, rule - 4)
    txs = [x for y in title_rows for x in range(W) if sum(px[x, y]) < 600]
    return style, rule, (top, bottom), boxes, desc, (max(txs) if txs else 0), px


def dark_colour(img, y0, y1):
    px = img.convert("RGB").load()
    best = (255, 255, 255)
    for y in range(y0, y1):
        for x in range(img.width):
            p = px[x, y]
            if not is_blue(p) and sum(p) < sum(best):
                best = p
    return best


def picture_cards(m):
    """(LEFT, RIGHT) as the picture shows them: the row adds `with [ ] ...` after the picture for inputs the picture does not draw; those are not in the picture."""
    left, right = list(m.LEFT), list(m.RIGHT)
    for i, c in enumerate(left):
        if c == ("op", "with"):
            return left[:i], []
    return left, right


def redraw(key, source, dest):
    m = R.get(key)
    old = Image.open(source)
    style, rule, band, boxes, desc, title_right, px = old_parts(old)
    left, right = picture_cards(m)
    n = len(left)
    levels = list(getattr(m, "LEVELS", None) or [0] * n) + [0] * n
    fracs = [list(f) for f in (getattr(m, "FRAC", None) or [])] + [[] for _ in range(n)]
    levels, fracs = levels[:n], fracs[:n]
    box_cards = [i for i, c in enumerate(left) if c[0] != "op"]
    need = len(box_cards) + sum(1 for c in right if c[0] != "op")
    if need != len(boxes):
        raise ValueError("%s: the row has %d boxes, the old picture shows %d" % (key, need, len(boxes)))
    box_of = {i: boxes[k] for k, i in enumerate(box_cards)}
    right_boxes = boxes[len(box_cards):]

    big = 46 if style == "A" else 44
    f_big, f_small = font(big), font(int(big * 0.62))
    colour = dark_colour(old, 0 if style == "B" else rule + 6, band[1])
    box_h = max([b.height for b in boxes] + [42 if style == "B" else 58])
    small_h = int(big * 0.6)
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))

    placed, bars, _end = _plan(n, levels, fracs, bool(getattr(m, "STACK_EXPONENTS", False)))

    def width_of(i):
        if i in box_of:
            return box_of[i].width + 4
        return int(probe.textlength(shown(left[i][1]), font=f_small if levels[i] else f_big)) + (4 if levels[i] else 10)

    columns = max([c for r, c in placed.values()] + [0]) + 1
    colw = [10] * columns
    for i, (r, c) in placed.items():
        colw[c] = max(colw[c], width_of(i))
    for r, c, w in bars:
        for cc in range(c, c + w):
            colw[cc] = max(colw[cc], 16)
    # "= [ ]" right of the formula: the answer box after the "="
    tail = []
    if right:
        tail.append(("text", "="))
        for b in right_boxes:
            tail.append(("box", b))
        tail += [("text", t) for k, t in right if k == "op"]
    tail_w = [int(probe.textlength("=", font=f_big)) + 14 if k == "text" else v.width + 4 for k, v in tail]

    rows_all = [r for r, c in placed.values()] + [r for r, c, w in bars] + [0]
    r_top, r_bot = min(rows_all), max(rows_all)
    big_rows = {0} | {r for i, (r, c) in placed.items() if levels[i] == 0} | {r for r, c, w in bars}
    heights = {r: (box_h if r in big_rows else small_h) for r in range(r_top, r_bot + 1)}
    gap = 2
    ys, y = {}, 0
    for r in range(r_top, r_bot + 1):
        ys[r] = y + heights[r] / 2
        y += heights[r]
    band_h = int(y)
    formula_w = sum(colw) + gap * (columns - 1) + (sum(tail_w) + gap * len(tail_w) if tail else 0)

    words = getattr(m, "WORDS", {})
    # one line for every card that has words: the card's symbol (a boxed number or answer: the box exactly as drawn above), its label, its context
    word_rows = [(box_of[i] if i in box_of else shown(left[i][1]), words[i][0], words[i][1]) for i in sorted(words) if i < n and i in placed]
    W = 1040 if style == "A" else max(int(formula_w) + 68, title_right + 34, 120)
    W = max(W, int(formula_w) + 68)
    single = box_h if style == "B" else 58
    height = old.height + (band_h - single) + 24 * len(word_rows)
    out = Image.new("RGB", (W, height), "white")
    d = ImageDraw.Draw(out)
    head = 72 if style == "A" else 44
    out.paste(old.convert("RGB").crop((0, 0, min(old.width, W), head)), (0, 0))
    d.rectangle((0, rule - 2, W, rule + 2), fill="white")
    rule_col = old.convert("RGB").getpixel((60, rule)) if style == "B" else old.convert("RGB").getpixel((80, rule + 1))
    d.line((33 if style == "B" else 36, rule, W - (34 if style == "B" else 36), rule), fill=rule_col, width=1 if style == "B" else 3)
    top_y = rule + (26 if style == "B" else 32)
    x0 = (W - formula_w) / 2 if style == "A" else 34
    xs, x = [], x0
    for w in colw:
        xs.append(x)
        x += w + gap

    def text(cx, cy, s, level, row, left_x=0):
        """Ordinary text is centred on its line; an exponent sits on the bottom edge of its row (just above its base), a subscript hangs from the top edge of its row."""
        if level == 0:
            d.text((cx, cy + 0.30 * big), s, font=f_big, fill=colour, anchor="ms")
        elif level < 0:
            d.text((left_x, top_y + ys[row] + heights[row] / 2 - 4), s, font=f_small, fill=colour, anchor="ls")
        else:
            d.text((left_x, top_y + ys[row] - heights[row] / 2 + 0.75 * big * 0.62 + 2), s, font=f_small, fill=colour, anchor="ls")

    for i, (r, c) in placed.items():
        cx, cy = xs[c] + colw[c] / 2, top_y + ys[r]
        if i in box_of:
            b = box_of[i]
            out.paste(b, (int(cx - b.width / 2), int(cy - b.height / 2)))
        else:
            text(cx, cy, shown(left[i][1]), levels[i], r, xs[c] + 1)
    for r, c0, w in bars:
        by = top_y + ys[r]
        d.line((xs[c0] - 2, by, xs[c0 + w - 1] + colw[c0 + w - 1] + 2, by), fill=colour, width=3)
    x = xs[-1] + colw[-1] + gap if columns else x0
    cy = top_y + ys[0]
    for (k, v), w in zip(tail, tail_w):
        if k == "box":
            out.paste(v, (int(x + 3), int(cy - v.height / 2)))
        else:
            text(x + w / 2, cy, v, 0, 0)
        x += w + gap
    f_word = small_font(15)
    for n_line, (symbol, label, context) in enumerate(word_rows):
        y_line = top_y + band_h + 8 + 24 * n_line
        if isinstance(symbol, str):
            d.text((40, y_line + 10), symbol, font=font(19), fill="#1c2b3a", anchor="lm")
        else:
            small = symbol.copy()
            small.thumbnail((74, 24), Image.LANCZOS)
            out.paste(small, (40, y_line + 10 - small.height // 2))
        d.text((128, y_line + 10), "%s  -  %s" % (label, context), font=f_word, fill="#4a5a78", anchor="lm")
    if desc is not None:
        out.paste(desc, (36 + 2, top_y + band_h + 39 + 24 * len(word_rows)))
    out.save(dest, "JPEG", quality=92)


def targets(argv):
    keys = [a for a in argv if not a.startswith("--")]
    out = []
    for k in keys or R.keys():
        m = R.get(k)
        lv, fr = getattr(m, "LEVELS", None), getattr(m, "FRAC", None)
        if keys or (lv and any(lv)) or (fr and any(fr)):
            out.append(k)
    return out


def main():
    check = "--check" in sys.argv
    bad = 0
    for k in targets(sys.argv[1:]):
        name = k.split("/")[-1]
        folder = os.path.join(LIB, *k.split("/"))
        path, keep = os.path.join(folder, name + ".jpg"), os.path.join(KEEP, *k.split("/")) + ".jpg"
        source = keep if os.path.isfile(keep) else path
        try:
            if check:
                m = R.get(k)
                s = old_parts(Image.open(source))
                need = sum(1 for c in sum(picture_cards(m), []) if c[0] != "op")
                if need != len(s[3]):
                    raise ValueError("%s: row has %d boxes, picture %d" % (k, need, len(s[3])))
                continue
            if not os.path.isfile(keep):
                os.makedirs(os.path.dirname(keep), exist_ok=True)
                shutil.copyfile(path, keep)
            redraw(k, source, path)
        except ValueError as e:
            bad += 1
            print("SKIPPED", e)
    print("done, %d problem(s)" % bad)


if __name__ == "__main__":
    main()
