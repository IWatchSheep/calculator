"""
ALGEBRA WORD PROBLEM MATCHER
============================
Matches a word problem to one of the generator's 216 problem types, offline, in plain Python
(standard library only, nothing to install).

Needs algebra_problem_generator.py (or .txt) in the same folder.

Commands
  python3 algebra_matcher.py build    [--per-type 400]   make labelled training data -> training_data.jsonl
  python3 algebra_matcher.py train                       train the matcher            -> matcher_model.json
  python3 algebra_matcher.py evaluate                    accuracy on held-out generated problems
                                                         AND on hand-written new wordings
  python3 algebra_matcher.py predict "problem text"      top 5 types with confidence
  python3 algebra_matcher.py all                         build + train + evaluate

How it works
  1. Text is normalised: numbers become tokens (NUM, MONEY, PCT, FRAC, DEG), names become NAME,
     algebra expressions like (3x + 5) become EXPR. So "Ava has $4.50" and "Ben has $9" look the same.
  2. Features: single words + pairs of words (bigrams).
  3. Model: naive Bayes on word presence (Bernoulli-style counts) with log probabilities -> fast, tiny (one JSON file),
     and gives a ranked list, which is what the "try the top few types" step needs.
  4. predict() returns the top-k types with a confidence (0-1).
     Suggested use in the calculator:
       - confidence >= 0.8  -> use the top type (right about 94% of the time on new wordings)
       - otherwise          -> try the top 3-5 types, fit the numbers into each type's equation,
                               keep the first one giving a sensible answer (positive, whole number
                               for counts, uses all the numbers), and show the equation it used.

Measured accuracy on 40 hand-written problems in new wording (never used for tuning):
  correct type ranked 1st 72.5%, in top 3 90%, in top 5 92.5%.
  On the generator's own wording it is 100%, which only shows it learned the templates.
To improve it: add wordings to the templates, or add entries to SYNONYMS, then rerun "all".
"""
import json, math, os, random, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
GEN_FILES = ["algebra_problem_generator.py", "algebra_problem_generator.txt"]
DATA = os.path.join(HERE, "training_data.jsonl")
MODEL = os.path.join(HERE, "matcher_model.json")

# ---------------------------------------------------------------------------
# 1. Load the generator's templates (without running its "write the file" part)
# ---------------------------------------------------------------------------
def load_generator(seed=None):
    for name in GEN_FILES:
        p = os.path.join(HERE, name)
        if os.path.exists(p):
            src = open(p, encoding="utf-8").read()
            break
    else:
        sys.exit("Put algebra_problem_generator.py (or .txt) next to this script.")
    lib = src.split("# GENERATE AND WRITE THE FILE")[0]
    g = {"__name__": "algebra_generator"}
    exec(compile(lib, "algebra_problem_generator", "exec"), g)
    if seed is not None:
        g["R"].seed(seed)
    return g

# ---------------------------------------------------------------------------
# 2. Text normalisation and features
# ---------------------------------------------------------------------------
STOP = set("a an the of to and is are was were be it its in on at for by with as that this there".split())
SENTENCE_START = re.compile(r'(^|[.!?]\s+)([A-Z][a-z]+)')
COMMON_CAPS = set("""A An The If In On At After Before When Two Three Four Five Six Seven Eight Nine Ten One
Each Every Some How What Which Who Find Using Use Solve Plan Pipe Town Class Job Service Plant Angles
Adult Child Pay Sound Bowling Bags Notebooks Sandwiches Magazines Plants Apples Oranges Burgers Hot""".split())

# Everyday phrasing -> the words the generator's templates use. Phrases are matched first
# (longest first), whole words only. Add to this table to teach the matcher new wordings;
# it is the cheapest accuracy gain available.
SYNONYMS = {
    # arithmetic words
    "triple": "three times", "tripled": "three times", "thrice": "three times", "treble": "three times",
    "double": "twice", "doubled": "twice", "quadruple": "four times", "halve": "half", "halved": "half",
    "take away": "minus", "takes away": "minus", "subtract": "minus", "subtracted": "minus", "less": "minus",
    "decreased by": "minus", "reduced by": "minus", "fewer": "minus", "minus": "decreased",
    "plus": "increased", "added to": "increased", "increased by": "increased", "add on": "increased",
    "bigger than": "more than", "larger than": "more than", "greater than": "more than", "exceeds": "more than",
    "exceed": "more than", "smaller than": "less than",
    "add up to": "sum", "adds up to": "sum", "add to": "sum", "adds to": "sum", "total": "sum",
    "totals": "sum", "altogether": "sum", "combined": "sum", "together": "together",
    "multiply to": "product", "multiplied together": "product", "times each other": "product",
    "in a row": "consecutive", "one after another": "consecutive", "back to back": "consecutive",
    "next to each other": "consecutive", "successive": "consecutive",
    "i am thinking of a number": "a number", "think of a number": "a number", "my number": "the number",
    "mystery number": "a number", "what number": "the number",
    # geometry
    "all the way round": "perimeter", "all the way around": "perimeter", "around the outside": "perimeter",
    "distance around": "perimeter", "border length": "perimeter", "inside angles": "interior angles",
    "proportion": "ratio", "in proportion": "ratio", "is to": "ratio", " to ": " to ",
    "square metres": "m²", "square meters": "m²", "square feet": "ft²", "sq ft": "ft²", "covers": "area",
    "as long as it is wide": "length times its width", "as long as it's wide": "length times its width",
    "it is wide": "width", "wide": "width", "slanted": "hypotenuse", "diagonal": "diagonal", "right angle": "right triangle",
    # motion
    "km/h": "kmh", "kph": "kmh", "mph": "mph", "miles per hour": "mph", "kilometres per hour": "kmh",
    "heading": "driving", "set off": "leaves", "sets off": "leaves", "head off": "leaves", "depart": "leave",
    "departs": "leaves", "go opposite ways": "opposite directions", "opposite ways": "opposite directions",
    "in opposite directions": "opposite directions", "toward each other": "toward each other",
    "towards each other": "toward each other", "head toward": "toward", "catch up with": "catch up",
    "catches": "catch up", "overtake": "catch up", "with the current": "downstream",
    "against the current": "upstream", "against it": "upstream", "rowing": "boat", "still water": "still water",
    # work
    "team up": "together", "teamed up": "together", "work together": "together", "both work": "together",
    "if they both": "together", "at the same time": "together", "tap": "pipe", "faucet": "pipe",
    "hose": "pipe", "plug leaks": "drain", "leaks": "drain", "leak": "drain", "empties": "empties",
    "bath": "tank", "bathtub": "tank", "pool": "tank",
    # money / percent
    "percent": "%", "per cent": "%", "off": "discount", "on sale": "discount", "sale": "discount",
    "reduced": "discount", "markdown": "discount", "marked down": "discount", "pay went up": "raise",
    "pay rise": "raise", "got a raise": "raise", "salary increase": "raise", "my pay": "salary",
    "receipt": "total cost", "gratuity": "tip", "cab": "taxi", "uber": "taxi", "fare": "charges",
    "membership": "per month", "a month": "per month", "monthly": "per month", "each month": "per month",
    "joining fee": "joining fee", "sign up": "sign-up", "signup": "sign-up",
    "put some money": "invests", "put money": "invests", "deposited": "invests", "account": "interest",
    "per hour": "per hour", "an hour": "per hour", "hourly": "per hour", "every mile": "per mile",
    "a mile": "per mile", "each mile": "per mile",
    # people / things
    "mum": "parent", "mom": "parent", "dad": "parent", "father": "parent", "mother": "parent",
    "brother": "sibling", "sister": "sibling", "kid": "child", "kids": "children",
    "hens": "chickens", "hen": "chicken", "sheep": "cows", "feet": "legs", "heads": "heads",
    "5-cent": "nickels", "10-cent": "dimes", "25-cent": "quarters", "1-cent": "pennies",
    "litres": "liters", "litre": "liter", "metres": "m", "metre": "m", "hrs": "hours", "hr": "hours",
    "mins": "minutes", "min": "minutes", "secs": "seconds", "years old": "old",
    "marks": "scores", "mark": "score", "grade": "score", "grades": "scores", "exam": "test",
    "exams": "tests", "quiz": "test",
}
NUMBER_WORDS = set("""zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen
fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred
thousand half quarter third""".split())
KEEP_NUMBER_WORDS = {"half", "quarter", "third", "two", "three", "four"}   # these carry meaning ("three times")
_SYN = sorted(SYNONYMS.items(), key=lambda kv: -len(kv[0]))
_SYN_RE = [(re.compile(r'(?<![A-Za-z])' + re.escape(k.strip()) + r'(?![A-Za-z])', re.I), v)
           for k, v in _SYN if k.strip()]

def apply_synonyms(text):
    for rx, v in _SYN_RE:
        text = rx.sub(v, text)
    return text

def stem(w):
    if len(w) > 4 and w.endswith("ies"): return w[:-3] + "y"
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss"): return w[:-1]
    return w

def normalise(text):
    t = apply_synonyms(text)
    t = re.sub(r'\([^()]*[a-z]\s*[+−-][^()]*\)', ' EXPR ', t)          # (3x + 5)
    t = re.sub(r'\b\d+(\.\d+)?[a-z]\b', ' EXPR ', t)                   # 3x
    t = re.sub(r'\$\s?\d[\d,]*(\.\d+)?', ' MONEY ', t)
    t = re.sub(r'\d[\d,]*(\.\d+)?\s?%', ' PCT ', t)
    t = re.sub(r'\d+(\.\d+)?\s?°', ' DEG ', t)
    t = re.sub(r'\b\d+\s?/\s?\d+\b', ' FRAC ', t)
    t = re.sub(r'\d+:\d+(:\d+)?', ' RATIO ', t)
    t = re.sub(r'\b\d+ to \d+( to \d+)?\b', ' RATIO ', t)               # "2 to 3 to 4"
    t = re.sub(r'\d[\d,]*(\.\d+)?', ' NUM ', t)
    t = t.replace('¢', ' CENTS ').replace('²', ' SQ ').replace('³', ' CUBE ')
    # capitalised words that are not sentence starts -> NAME
    words = re.findall(r"[A-Za-z']+|[A-Z]{2,}", t)
    out = []
    prev_end = True
    for w in re.finditer(r"[A-Za-z']+|[.!?]", t):
        tok = w.group(0)
        if tok in ".!?":
            prev_end = True
            continue
        if tok.isupper() and len(tok) > 1:            # our placeholder tokens
            out.append(tok)
        elif tok[0].isupper() and not prev_end and tok not in COMMON_CAPS:
            out.append("NAME")
        else:
            low = tok.lower().strip("'")
            if low.endswith("'s"):
                low = low[:-2]
            if low in NUMBER_WORDS and low not in KEEP_NUMBER_WORDS:
                low = "NUM"
            out.append(stem(low) if low != "NUM" else low)
        prev_end = False
    return out

def features(text):
    toks = [w for w in normalise(text) if w not in STOP]
    feats = list(toks)
    feats += [a + "_" + b for a, b in zip(toks, toks[1:])]
    return list(dict.fromkeys(feats))      # each feature counted once per problem (works better)

# ---------------------------------------------------------------------------
# 3. Build labelled training data from the generator
# ---------------------------------------------------------------------------
def build(per_type=400, seed=12345):
    g = load_generator(seed)
    T, P = g["T"], g["P"]
    rows, seen = [], set()
    for f in T:
        got, tries = 0, 0
        while got < per_type and tries < per_type * 40:
            tries += 1
            before = len(P)
            try:
                f()
            except Exception:
                continue
            if len(P) > before:
                cat, prob = P[-1][0], P[-1][1]
                if prob in seen:
                    continue
                seen.add(prob)
                rows.append({"type": f.__name__, "category": cat, "text": prob})
                got += 1
    with open(DATA, "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")
    counts = collections.Counter(r["type"] for r in rows)
    print(f"Wrote {len(rows)} problems for {len(counts)} types -> {DATA}")
    few = [k for k, v in counts.items() if v < 20]
    if few:
        print("Types with few distinct wordings/numbers (fine, just fewer examples):", ", ".join(few))
    return rows

def load_rows():
    return [json.loads(l) for l in open(DATA, encoding="utf-8")]

# ---------------------------------------------------------------------------
# 4. Naive Bayes matcher
# ---------------------------------------------------------------------------
class Matcher:
    def __init__(self, alpha=0.1):
        self.alpha = alpha
        self.prior, self.logp, self.default, self.category = {}, {}, {}, {}

    def fit(self, rows):
        counts = collections.defaultdict(collections.Counter)
        ndocs = collections.Counter()
        vocab = set()
        for r in rows:
            fs = features(r["text"])
            counts[r["type"]].update(fs)
            ndocs[r["type"]] += 1
            vocab.update(fs)
            self.category[r["type"]] = r["category"]
        V, N = len(vocab), sum(ndocs.values())
        for c, cnt in counts.items():
            total = sum(cnt.values()) + self.alpha * V
            self.prior[c] = math.log(ndocs[c] / N)
            self.logp[c] = {w: math.log((n + self.alpha) / total) for w, n in cnt.items()}
            self.default[c] = math.log(self.alpha / total)
        return self

    def scores(self, text):
        fs = features(text)
        known = [f for f in fs if any(f in lp for lp in self.logp.values())]
        out = {}
        for c in self.logp:
            lp, d = self.logp[c], self.default[c]
            out[c] = self.prior[c] + sum(lp.get(f, d) for f in known)
        return out, len(known), len(fs)

    # Raw naive-Bayes scores are wildly over-confident (top pick is always ~100%).
    # Dividing by the number of recognised features and multiplying by TEMPERATURE makes
    # the confidence usable. Measured on unseen wordings: confidence >= 0.8 -> top pick right ~94%.
    TEMPERATURE = 2.0
    CONFIDENT = 0.8

    # Types whose equation only differs by a sign from a commoner type. They are only allowed
    # when the text contains one of these words; otherwise they are pushed to the bottom.
    REQUIRES = {
        "pool":     ["drain", "empt", "leak", "out"],
        "w_pipes3": ["drain", "empt", "leak", "out"],
    }

    def predict(self, text, k=5):
        s, known, total = self.scores(text)
        low = text.lower()
        for c, words in self.REQUIRES.items():
            if c in s and not any(w in low for w in words):
                s[c] -= 1e6
        n = max(known, 1)
        best = sorted(s.items(), key=lambda kv: -kv[1])
        m = best[0][1]
        z = sum(math.exp((v - m) * self.TEMPERATURE / n) for v in s.values())
        res = [{"type": c, "category": self.category[c],
                "confidence": round(math.exp((v - m) * self.TEMPERATURE / n) / z, 3)} for c, v in best[:k]]
        return res, (known / total if total else 0.0)

    def save(self, path=MODEL):
        json.dump({"alpha": self.alpha, "prior": self.prior, "logp": self.logp,
                   "default": self.default, "category": self.category}, open(path, "w"))

    @classmethod
    def load(cls, path=MODEL):
        d = json.load(open(path))
        m = cls(d["alpha"])
        m.prior, m.logp, m.default, m.category = d["prior"], d["logp"], d["default"], d["category"]
        return m

def train(rows=None, holdout=0.2, seed=7):
    rows = rows or load_rows()
    rnd = random.Random(seed)
    rnd.shuffle(rows)
    cut = int(len(rows) * (1 - holdout))
    m = Matcher().fit(rows[:cut])
    acc_heldout = top_k_accuracy(m, rows[cut:], [1, 3, 5])
    final = Matcher().fit(rows)          # final model uses everything
    final.save()
    print(f"Trained on {len(rows)} problems -> {MODEL} ({os.path.getsize(MODEL)//1024} KB)")
    return final, acc_heldout

def top_k_accuracy(m, rows, ks):
    hits = collections.Counter()
    for r in rows:
        preds = [p["type"] for p in m.predict(r["text"], max(ks))[0]]
        for k in ks:
            hits[k] += r["type"] in preds[:k]
    return {k: hits[k] / len(rows) for k in ks}

# ---------------------------------------------------------------------------
# 5. Hand-written test set: NEW wordings the generator never produces.
#    Each item lists every type whose equation would solve it correctly.
# ---------------------------------------------------------------------------
COUNT_VALUE = {"coins", "tickets", "heads_legs", "s_tables", "s_boats", "s_bills", "s_egg_boxes",
               "s_concert", "s_stamps", "s_mix_two_rates", "s_points", "two_items", "s_test_scoring", "m_wages_two"}
HAND_TEST = [
 ("I've got a pile of 5-cent and 10-cent coins, 40 in all, adding up to $3.10. How many dimes are in there?", COUNT_VALUE),
 ("Our class sold cookies at $2 and brownies at $3. We sold 85 treats and made $205. How many brownies did we sell?", COUNT_VALUE),
 ("On a farm there are some hens and some sheep. Altogether I count 30 heads and 84 feet. How many sheep?", COUNT_VALUE),
 ("Jo is three years older than her brother. Together their ages total 27. How old is Jo?", {"age_diff"}),
 ("Mum is 4 times as old as Lily. In 6 years their ages will add up to 62. What are their ages today?", {"age_ratio", "s_age_ratio_two"}),
 ("Find two numbers that add to 50 if one is 8 bigger than the other.", {"sum_diff", "wire_longer", "age_diff"}),
 ("I'm thinking of a number. Triple it and take away 7 and you get 29. What's my number?", {"number_linear"}),
 ("Add up three integers in a row and you get 138. Which integers?", {"consecutive"}),
 ("Two even numbers that come one after another multiply to 168. What are they?", {"consecutive_product"}),
 ("A rectangle is twice as long as it is wide and goes 72 cm all the way round. How wide is it?", {"rect_perim", "s_rect_two"}),
 ("A garden's length exceeds its width by 5 m. It covers 84 square metres. Give the width.", {"rect_area"}),
 ("The three angles of a triangle are in proportion 2 to 3 to 4. What is the biggest?", {"triangle_angles"}),
 ("Two angles add up to 90 degrees and one is 30 more than the other. Find them.", {"compsupp"}),
 ("A 13 m ladder rests against a wall with its base 5 m out. How high does it reach?", {"g_pythag_ladder", "g_rect_diag"}),
 ("How many sides does a polygon have if its inside angles total 1440 degrees?", {"g_polygon_sum"}),
 ("Two cars leave the same spot heading in opposite directions, one at 50 km/h and one at 70 km/h. When are they 360 km apart?", {"opposite"}),
 ("A slow train leaves at 40 mph. Two hours later a fast train sets off after it on the same track at 60 mph. How long until the fast one catches it?", {"catchup"}),
 ("Rowing with the current I cover 24 km in 2 h, but against it only 12 km in 2 h. What's my rowing speed in still water?", {"boat"}),
 ("Tom paints a fence alone in 6 hours, Sue in 3. If they team up, how long does it take?", {"work"}),
 ("A tap fills a bath in 10 minutes but the plug leaks and empties it in 30 minutes. With both going, how long to fill it?", {"pool"}),
 ("You need 20 litres of 30% acid. You have 10% and 50% acid. How much of the 10% do you use?", {"mixture", "x_alloy"}),
 ("How much pure water should I pour into 8 litres of 40% bleach solution to make it 25%?", {"x_dilute"}),
 ("I put some money in an account at 3% and the rest at 5%, $10,000 total. I earned $420 in interest in a year. How much was at 5%?", {"interest"}),
 ("Shoes are 30% off and now cost $56. What did they cost before the sale?", {"discount"}),
 ("My pay went up 4% and I now make $52,000. What was I making before?", {"raise_"}),
 ("With 8% sales tax my receipt says $54. What was the price before tax?", {"tax"}),
 ("15 is 20 percent of which number?", {"percent_of", "m_what_percent"}),
 ("After a 15% tip the lunch came to $46. How much was lunch before tip?", {"m_tip"}),
 ("A cab costs $3 to get in and $2 every mile after. I paid $19. How far did I go?", {"taxi"}),
 ("Gym A: $50 to join plus $20 a month. Gym B: no joining fee but $30 a month. After how many months do they cost the same?", {"m_streaming", "plans", "m_buy_vs_rent"}),
 ("A recipe for 4 people needs 300 g of pasta. How much pasta for 10 people?", {"proportion_recipe", "r_scale_recipe2", "direct_var"}),
 ("If 6 workers take 10 days to dig a ditch, how long would 4 workers take?", {"inverse_var"}),
 ("A ball is thrown up at 48 ft/s from the ground, h = -16t² + 48t. When does it land?", {"projectile"}),
 ("My test marks are 70, 85 and 90. What do I need on the fourth test to average 85?", {"average_needed"}),
 ("The digits of a two-digit number sum to 9. Swap them and the number goes up by 27. What is the number?", {"digits"}),
 ("I have $200 and save $15 a week. My sister has $350 and saves $5 a week. When will we have the same?", {"savings"}),
 ("A 60 cm ribbon is cut so the pieces are in the ratio 1 to 4. How long is the short piece?", {"wire"}),
 ("Water is mixed into concentrate in the ratio 5:1. How much concentrate for 30 litres of water?", {"r_paint", "proportion_recipe", "direct_var"}),
 ("A bacteria colony doubles every 3 hours. Starting at 500 cells, when will there be 8000?", {"e_double"}),
 ("A radioactive sample halves every 5 years. When does 160 g become 20 g?", {"e_half"}),
 ("You can spend no more than $60. Each ride ticket costs $4 and entry is $12. What's the most ride tickets you can buy?", {"i_budget"}),
 ("What is the lowest score I can get on my last exam and still average at least 80, if I have 75 and 78 so far?", {"i_avg_atleast"}),
 ("A candle 30 cm tall burns 2 cm an hour; another 24 cm tall burns 1 cm an hour. When are they equally tall?", {"l_candles"}),
 ("Town X has 50,000 people and gains 1,000 a year; Town Y has 80,000 and loses 500 a year. When are they equal?", {"l_towns"}),
 ("Convert: what Celsius temperature equals 98.6 Fahrenheit using F = 9/5 C + 32?", {"l_temp_conv"}),
 ("Two trains are 300 miles apart and head toward each other at 70 and 80 mph. When do they meet?", {"d_toward"}),
 ("I drove to the beach at 60 mph and back at 40 mph. The whole drive took 5 hours. How far is the beach?", {"d_round_trip_dist"}),
 ("A salesperson gets $500 a week plus 5% of sales. Last week they got $1,100. What were their sales?", {"m_commission"}),
 ("A store buys a lamp and adds 40% to sell it for $70. What did the store pay?", {"m_markup"}),
 ("Every team played every other team once and there were 28 games. How many teams?", {"n_handshakes"}),
 ("The angles inside a regular polygon are each 140 degrees. How many sides?", {"g_regular_angle"}),
 ("A sloped roof has a 5 m rise and 12 m run. Use the Pythagorean theorem... actually: one leg is 7 longer than the other and the hypotenuse is 13. Find the legs.", {"g_pythag_legs"}),
 ("A seesaw balances when a 30 kg child sits 2 m from the middle. Where must a 20 kg child sit on the other side?", {"l_lever"}),
 ("When do the hands of a clock line up between 4 and 5 o'clock?", {"c_clock"}),
 ("The sum of three numbers is 30. The first two add to 18 and the last two add to 20. What are the numbers?", {"s_three_var"}),
 ("40% of a club are boys and there are 24 girls. How many members?", {"m_class_percent"}),
 ("A shop has fixed costs of $500 a day. Each mug costs $3 to make and sells for $8. How many mugs to break even?", {"m_breakeven", "m_profit_items"}),
 ("A car worth $24,000 loses $2,000 of value per year. When is it worth $10,000?", {"m_depreciation"}),
 ("A tank is a quarter full. Add 30 litres and it's three quarters full. How big is it?", {"m_tank_fraction"}),
 ("A 2 m tall pole casts a 3 m shadow, and a tree casts a 15 m shadow. How tall is the tree?", {"g_shadow"}),
]

# Second hand-written set, written AFTER the synonym table and settings were tuned on HAND_TEST.
# Nothing was adjusted to fit these, so this is the unbiased estimate for unseen wording.
FRESH_TEST = [
 ("Pens cost 50 cents and pencils 20 cents. I bought 18 items for $5.70. How many pens?", COUNT_VALUE),
 ("A parking lot has motorbikes and cars, 25 vehicles with 80 wheels. How many cars?", COUNT_VALUE),
 ("Grandpa is 50 years older than his grandson. Their combined age is 74. How old is the grandson?", {"age_diff"}),
 ("Five less than twice a number is 31. Find it.", {"number_linear"}),
 ("When you multiply a number by 6 and subtract 4 you get the same as 4 times the number plus 10. What is it?", {"number_both_sides"}),
 ("Four odd numbers in a row sum to 96. List them.", {"consecutive"}),
 ("The perimeter of a rectangular yard is 100 ft and the length is 10 ft more than the width. What are the dimensions?", {"rect_perim", "s_rect_two"}),
 ("A square patio's side is increased by 3 m and its area goes up by 51 m². How long was each side?", {"g_square_grow"}),
 ("An isosceles triangle's equal sides are each 4 cm longer than its base, and the perimeter is 35 cm. Find the base.", {"isosceles"}),
 ("Two angles on a straight line are (3x + 10)° and (2x + 20)°. Find x.", {"g_linear_pair", "g_parallel"}),
 ("How many diagonals... no: a polygon has 35 diagonals. How many sides does it have?", {"g_diagonals"}),
 ("A kite string is 25 m long and the kite is directly above a point 7 m away from the person. How high is the kite?", {"g_pythag_ladder", "g_rect_diag"}),
 ("A cyclist leaves at noon going 12 mph. A car leaves the same place at 2 pm going 36 mph along the same road. When does the car catch the cyclist?", {"catchup"}),
 ("Two hikers start 18 km apart and walk toward each other at 4 km/h and 5 km/h. When do they meet?", {"d_toward"}),
 ("A plane flies 1200 km with the wind in 3 hours and returns against the wind in 4 hours. Find the wind speed.", {"plane_wind", "boat"}),
 ("One printer finishes a job in 4 hours and another in 12 hours. Running both, how long does the job take?", {"work"}),
 ("Working together, two gardeners weed a park in 6 hours. One alone would need 10 hours. How long would the other need alone?", {"work_find"}),
 ("How many ounces of a 20% sugar syrup must be combined with 50% syrup to get 30 oz of 40% syrup?", {"mixture", "x_alloy"}),
 ("A 12-litre bucket of 60% paint thinner is diluted with water down to 40%. How much water is added?", {"x_dilute"}),
 ("Coffee worth $6 a pound is mixed with coffee worth $10 a pound to make 40 lb worth $7 a pound. How much of each?", {"weighted_avg", "s_mix_two_rates", "mixture"}),
 ("$8,000 was invested, some at 6% and some at 4%. The total yearly interest was $400. How much was invested at 6%?", {"interest"}),
 ("A TV is marked down 25% to $450. What was the original price?", {"discount"}),
 ("Rent went up 5% to $1,260 a month. What was the old rent?", {"raise_", "m_markup"}),
 ("What percent of 80 is 20?", {"m_what_percent", "percent_of"}),
 ("A plumber charges $60 to come out plus $45 an hour. The bill was $195. How many hours did they work?", {"m_plumber", "taxi", "gym"}),
 ("Phone plan A is $30 plus 10 cents a minute; plan B is $20 plus 15 cents a minute. At how many minutes are they equal?", {"plans"}),
 ("If 3 kg of apples cost $7.50, how much do 8 kg cost?", {"direct_var", "proportion_recipe", "fuel"}),
 ("At 60 km/h a trip takes 3 hours. How long at 90 km/h?", {"w_speed_time_inverse", "inverse_var"}),
 ("A stone is dropped... thrown upward at 80 ft/s from ground level with h = -16t² + 80t. When does it come back down?", {"projectile"}),
 ("A number squared plus 3 times the number equals 40. What is the positive number?", {"number_square", "n_square_more"}),
 ("The product of two consecutive odd numbers is 143. Find them.", {"consecutive_product"}),
 ("Sam has $40 and saves $12 a week to buy a $160 bike. How many weeks?", {"goal"}),
 ("A 90 cm stick is broken into pieces in the ratio 4:5. How long is each piece?", {"wire"}),
 ("An investment of bacteria... a yeast culture triples every 2 hours, starting at 10 cells. When does it reach 810?", {"e_triple"}),
 ("You have $45. A movie costs $9 per ticket. What is the greatest number of tickets you can buy?", {"i_budget"}),
 ("Two plants are 5 cm and 15 cm tall. The first grows 3 cm per week and the second 1 cm per week. When will they be the same height?", {"l_plants"}),
 ("Using d = rt, how long does a 210 km trip take at 70 km/h?", {"l_speed_formula", "d_sound"}),
 ("Red, white and blue beads are in the ratio 2:3:5, with 150 beads total. How many blue beads?", {"r_three_part"}),
 ("The mean of five numbers is 12. Four of them are 10, 14, 9 and 15. What is the fifth?", {"a_missing"}),
 ("An apple and a pear cost $1.30. Two apples and three pears cost $3.40. Find the price of each.", {"two_items"}),
]

def evaluate(m=None, heldout=None):
    m = m or Matcher.load()
    if heldout:
        print("\nHeld-out GENERATED problems (same wordings the generator uses):")
        for k, v in heldout.items():
            print(f"  top-{k} accuracy: {v:.1%}")
    results = {}
    for label, testset in [("Hand-written set A (used for tuning)", HAND_TEST),
                           ("Hand-written set B (never tuned on: the honest number)", FRESH_TEST)]:
        hits = collections.Counter()
        misses = []
        for text, ok in testset:
            preds = [p["type"] for p in m.predict(text, 5)[0]]
            for k in (1, 3, 5):
                hits[k] += any(p in ok for p in preds[:k])
            if not any(p in ok for p in preds[:3]):
                misses.append((text, sorted(ok), preds[:3]))
        n = len(testset)
        print(f"\n{label}, {n} problems:")
        for k in (1, 3, 5):
            print(f"  top-{k} accuracy: {hits[k]/n:.1%}")
        conf = [(m.predict(t, 1)[0][0]["confidence"], m.predict(t, 1)[0][0]["type"] in ok) for t, ok in testset]
        sure = [ok for c, ok in conf if c >= Matcher.CONFIDENT]
        print(f"  confidence >= {Matcher.CONFIDENT}: {len(sure)}/{n} problems, top pick right in {sum(sure)/max(len(sure),1):.0%} of those")
        if misses:
            print(f"  Not in top 3 ({len(misses)}):")
            for text, ok, preds in misses:
                print(f"   - {text[:85]}\n       wanted {ok}, got {preds}")
        results[label] = hits
    return results

def main():
    args = sys.argv[1:]
    cmd = args[0] if args else "all"
    if cmd == "build":
        per = int(args[args.index("--per-type") + 1]) if "--per-type" in args else 400
        build(per)
    elif cmd == "train":
        train()
    elif cmd == "evaluate":
        _, held = train()
        evaluate(heldout=held)
    elif cmd == "predict":
        m = Matcher.load()
        res, coverage = m.predict(" ".join(args[1:]))
        verdict = "confident" if res[0]["confidence"] >= Matcher.CONFIDENT else "unsure: try the top few types and check answers"
        print(f"(words recognised: {coverage:.0%}; {verdict})")
        for r in res:
            print(f"  {r['confidence']:.3f}  {r['type']:<22} [{r['category']}]")
    elif cmd == "all":
        build()
        m, held = train()
        evaluate(m, held)
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
