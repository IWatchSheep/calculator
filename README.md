# Calculator

A desktop calculator written in Python (Tkinter) that works with **operators instead of a single
expression line**. You pick an operator from a library of 507 (arithmetic, algebra, calculus, linear
algebra, statistics, geometry, physics and more), fill in its square boxes, press `=`, and the answer
appears. Every operator comes with a picture of its formula.

![The calculator with the Operators pop-up open, Time dilation calculated as 1.25](picture_of_gui/calculator_screenshot.png)

*Time dilation(1, 179 875 474.8) = 1.25: one second on a clock moving at 60% of the speed of light is
1.25 seconds for a stationary observer.*

## What it can do

- **507 operators**, 446 of which calculate (the other 61 show their formula only, see below).
- **A picture of each formula** drawn with small square boxes for the inputs.
- **Rows and joins:** results from several rows can be combined with `+ − × ÷ = ≠ < > ≤ ≥`.
- **Operators inside operators:** put an operator into the box of another one.
- **Advanced Input** for things a number pad cannot type: lists, matrices, functions, sets and graphs.
- **Templates:** type your own math once, save it, and put it into a row whenever you want it.
- **Multi-row operators** (for example Stokes' theorem) that add the rows they need for you.
- **Safe function input:** typed functions such as `x**2 + 3*x` are checked against a small whitelist
  (no `eval` on raw text), so `__import__('os')` and similar are rejected.

### The operator library

| Area | Operators | Examples |
|---|---|---|
| Physics | 81 | motion, forces, energy, gravitation, electricity, **magnetism, fluid dynamics, quantum mechanics, optics, relativity** |
| Geometry | 33 | areas, volumes, distance, Heron's formula, law of sines and cosines |
| Algebra | 29 | quadratic formula, logs, roots, sequences and series, complex numbers, factor / expand / simplify |
| Real analysis | 29 | supremum, series tests, Riemann sums, norms, convergence |
| Statistics and probability | 29 | mean, variance, regression, distributions, z-score, confidence interval |
| Abstract algebra | 28 | groups, subgroups, cosets, kernels, rings and fields |
| Linear algebra | 26 | determinant, inverse, eigenvalues, LU / QR / SVD, dot and cross product |
| Topology | 26 | open and closed sets, closure, interior, boundary |
| Calculus | 24 | derivatives, integrals (single to triple), limits, gradient, curl, Taylor series |
| Optimization and numerical methods | 24 | Newton's method, bisection, Simpson's rule, linear programming, RK4 |
| Category theory and foundations | 23 | functions, injective / surjective, power sets, number systems |
| Trigonometry | 22 | sin, cos, tan and inverses, hyperbolic functions, identities |
| Graph theory and combinatorics | 21 | shortest path, max flow, chromatic number, Bell and Catalan numbers |
| Transforms and differential equations | 21 | Laplace, Fourier, DFT, first and second order ODEs |
| Logic and sets | 18 | and, or, implies, union, intersection, power set |
| Constants and relations | 16 | π, e, golden ratio, `=`, `≠`, `<`, `≥` |
| Differential geometry and tensors | 16 | metric tensor, Lie bracket, Gaussian curvature |
| Complex analysis | 15 | argument, Euler's formula, contour integrals, residues |
| Arithmetic | 14 | `+ − × ÷`, modulo, rounding, min, max |
| Discrete and number theory | 12 | factorial, combinations, gcd, lcm, primes, Fibonacci |

The full list, with each formula and whether it calculates, is in
[`operators_one_operator_per_file/INDEX.md`](operators_one_operator_per_file/INDEX.md).

**The rows look like the pictures.** Each operator's row (`operator_row_math/`) is laid out from its picture, one card per symbol: `Cone surface area` is `[A] = π × [r] × ( [r] + [ℓ] )`. The answer box (`A`) cannot be typed into and fills in when you press `=`. A variable the picture writes twice (the two `r`) has two boxes that share one value. A formula with two answers (the quadratic formula's `x₁`, `x₂`) shows each answer in its own box. Only a box you can type into is blue. A box the picture draws that is not an input (the second box of `A ⊕ B`) is an ordinary card showing a square, and a constant or letter the picture puts in a box (the `g` of `W = m g`) is an ordinary card with that letter. If a picture does not draw every input of the operator (`ker [ ]` needs three), the row follows the picture and then adds `with [ ] , [ ]` for the missing inputs so it still calculates; those 115 operators are listed in `operator_keys/operator_rows_with_extra_boxes.txt`. The rows are written by `operator_keys/make_operator_row_files.py` from `operator_keys/operator_row_specs.txt` (one line per operator, written by reading the picture).

## Requirements

- **Python 3** with **Tkinter**. It was developed and tested with Python 3.15 on Windows 11.
  Tkinter comes with the python.org installers for Windows and macOS. On Linux install it first, for
  example `sudo apt install python3-tk`.
- **Pillow** (shows the operator pictures). It is listed in `requirements.txt`.

## Download and run

1. Download the project from GitHub using **Code > Download ZIP** and extract it
   (or `git clone https://github.com/IWatchSheep/calculator.git`).
2. Open the folder in PyCharm (or any terminal) and open a terminal in it.
3. Install the one required package:

   ```
   python -m pip install -r requirements.txt
   ```

4. Start the calculator:

   ```
   python main.py
   ```

   On Windows you can also use `py main.py`.

## How to use it

**Example: time dilation.**

1. Click **Operators** on the keypad. A pop-up opens with the operator library, grouped by area.
2. Type `time dilation` in the **Search** box and click **Time dilation**. The pop-up shows its
   picture and the keys it needs, and Row 1 now reads `Time dilation( □ , □ )`.
3. Click the first square box and type `1` on the keypad. Click the second box and type `179875474.8`.
4. Press **`=`**. The result `1.25` appears in the results area and in Row 2.

**The pieces of the window**

| Part | What it does |
|---|---|
| Rows area (top) | Each row is a line of cards. Square boxes are the inputs. Click a box to select it. |
| Keypad (bottom left) | `0–9` and `.` type into the selected box. `±` flips the sign. `EE` starts a power of ten, so `1.5 EE ± 3` is `1.5e-3`. `Backspace` deletes. `Next Row (↓)` moves to the next row, adding one if needed. `=` calculates. `C` (or the toolbar's Clear (C)) clears everything and starts again. |
| Join keys | `+ − × ÷ = ≠ < > ≤ ≥` combine the result of a row with the rows above it. |
| Operators pop-up | Search and pick an operator. It shows the formula picture and the keys it uses. Drag it by its title bar. |
| Mathematical Templates | Type math, preview it, save it, and apply it to a row (see below). |
| Advanced Input | A pop-up for values that need more than a number (see below). |
| Results area | Shows what was calculated, for example `Row 1: Time dilation( 1 , 179875474.8 )` and `= 1.25`. |

**Nesting.** If Row 1 already holds an operator, picking another operator puts it into the
selected box, so the result of one feeds the next.

**Templates.** The *Mathematical Templates* panel keeps math you use often. There are four steps, and a
guide pop-up walks you through them the first time you start typing in the text box:

1. **Type your math** in the text box, for example `(? + 3) × 2` or `Time dilation(1, x)`.
2. Press **Preview Posted**. Your math is put into the target row, just like an operator from the Operators
   pop-up, so you can see it. Change the text and press it again to replace the preview.
3. Like it? Press **Save Template**. It is added to the list and saved in `saved_templates.json` next to
   `main.py`, so it is still there next time. The file is yours alone and is not part of the repository.
4. Whenever you want it: pick it in the list next to **Apply Template** and press **Apply Template**. It goes
   into the target row (inside the selected box if the row already has math). Fill the empty boxes and press `=`
   on the keypad.

**The guide pop-up** shows the four steps side by side. The step you are on is yellow, finished steps are green
with a tick, and under step 1 it tells you live whether your math is understood (`✓ Understood: (□ + 3) × 2
(1 empty box)`), still unfinished (`… keep typing`) or wrong (`✗ There is no operator called 'foo'`). Tick
*Don't show this again* to stop it opening; the **?** button beside Apply Template opens it any time. The small
`=` between the text box and Preview Posted is only a sign that the math in the box is what gets previewed.

What you can type:

| You type | Meaning |
|---|---|
| `3`, `2.5`, `.5`, `1.5e-3` | numbers |
| `□`, `?`, or a bare letter such as `x` | an empty box to fill in later (each one is its own box) |
| `+ − × ÷ ^ %` (or `* / -`) | the arithmetic operators; `^` binds tightest, then `× ÷ %`, then `+ −` |
| `( ... )` | grouping |
| `sqrt(16)`, `Square root(16)`, `sin(pi / 2)` | any operator in the library, by name or short name (`sqrt`, `sin`, `ln`, `abs`, `gcd`, ...), with its inputs in brackets |
| `Time dilation(1, □)` | operators with several inputs: separate them with commas |
| `pi`, `e` | the constants |

A mistake gives a plain message in the results area, for example `Time dilation needs 2 input(s) but was
given 1.` and nothing is saved.

**Advanced Input** lets a box take a list (`1, 2, 3`), a matrix (`1 2; 3 4`), a function of x
(`x**2 + 3*x`), a yes/no test (`x > 2`), a set, a list of edges, a graph (`A: B, C; B: C; C: A`), a
weighted graph, or a polynomial to factor. Pick the type, type the value, and it goes into the
selected box.

**Operators marked "reference"** (61 of them, such as `ring`, `manifold` or `open bracket`) show their
formula and picture but cannot calculate. Pressing `=` tells you so instead of failing.

**Angles are in radians**, and physics operators use standard constants by default (g = 9.81 m/s²,
c = 299 792 458 m/s, and so on). The constant is named in each operator's formula in `INDEX.md`.

## Using the operators from Python

Every operator is a plain Python file you can use without the window:

```python
from operators_one_operator_per_file import get

get("math/algebra/power").compute(2, 10)                      # 1024
get("physics/physics/lorentz_factor").compute(179875474.8)    # 1.25
get("math/linear_algebra/determinant").compute([[1, 2], [3, 4]])   # -2
```

Keys look like `math/<area>/<operator>`, `geometry/geometry/<operator>` and
`physics/physics/<operator>`. Each operator file defines `NAME`, `SYMBOL`, `FORMULA` and `compute(...)`.

## Algebra word problems (work in progress)

Besides the 507 operators the project is getting a second library: **1,000 algebra word problems**, each stored as its own file with a diagram, and each with a row layout so it can sit in a calculator row like an operator does. The diagrams are in the window. Click Operators, then Algebra word problems, and the list shows all 1,000 problems. Clicking one opens its diagram, and if the problem is Ready (377 of them) it is also put into the target row as `Name(□, □ ...) = □`: fill one box for every number in the text, in the order they appear, and press `=` to get the answer. A Reference problem shows its diagram and says so, and is not placed. The operator that takes pasted text is not built. It is under *What is left*.

> Reviewed. The steps under *How a problem travels* and the decisions under *Decisions* are the ones to follow. A family answers only when its wording matches, every number has a role, and the answer passes its checks. Otherwise it declines. A decline is safe. A wrong number is a failure.

### The four pieces

| Piece | Where | What it holds |
|---|---|---|
| **The problems** | `algebra_word_problems/algebra_word_problems.txt` | The 1,000 generated problems in 55 categories: Problem / Let / Equation / Solve / Answer. The ground truth. |
| **One problem per file** | `operators_one_algebra_word_problem_per_file/<category>/<id>/` | `<id>.py` (the problem, its steps and its answer, plus `compute(...)`) and `<id>.jpg` (a diagram of the problem). `INDEX.md` lists all 1,000. |
| **How a problem goes into a row** | `operator_row_math_for_algebra_word_problems/<category>/<id>/<id>.py` | The row of cards for the calculator, in the same style as `operator_row_math/`. |
| **The solver** | `algebra_word_problems/algebra_matcher/word_solver.py` | 58 families that solve problems straight from their wording. Standard library only. `number_puzzle.py` answers a smaller set of number puzzles. |

Keys look like `savings/0848` (category folder, then the four-digit problem number).

**The diagram** (`<id>.jpg`) shows the problem text, the "Let" line, and the equation with every number in a blue box, then the answer in green. For example `savings/0848` shows `[150] + [25]w = [310] + [15]w` and "Answer: 16 weeks". An equation with several parts is drawn one line per part.

**The problem file** (`<id>.py`) defines `ID, KEY, NAME, CATEGORY, PROBLEM, LET, EQUATION, SOLVE, ANSWER`, and also

- `SOLVER` and `FAMILY`: who answers this problem today (`"word_solver"` with the family name, `"number_puzzle"`, or `None`);
- `TEMPLATE` and `NUMBERS`: the problem text with every number replaced by `{0}`, `{1}` ... and the numbers as written, in order;
- `compute(*numbers)`: puts your numbers into the template and asks the solver. With no arguments it uses the stored numbers.

A problem is **Ready** when a solver answers it (377 of the 1,000: 349 by `word_solver`, 28 by `number_puzzle`) and **Reference** when only the text and its steps are stored (623). Calling `compute()` on a Reference problem raises `NotImplementedError`. Calling it with numbers the solver will not accept raises `ValueError`. It never guesses.

**The row file** lays the problem out as one row that is its equation, for example `x + (x + 1) + (x + 2) = □` for `consecutive_integers/0070` (the 120 is the box) or `□ + □w = □ + □w` for `savings/0848`. A number of the equation is a box only when it is also written in the problem text (same value, matched left to right); the 1 and 2 above are plain text, and so is a 0.75 that stands for 75%. A text number that no equation number matches (the 3 in "the sum of 3 consecutive integers") is not a box: `compute()` keeps it as written. Every symbol of the equation is its own card, as in the other rows (`x` `+` `(` `x` `+` `1` `)` `+` `(` `x` `+` `2` `)` `=` then the box), so a card's centre is one token: a box, a number that is not a box, or one character. Each box starts with its stored number, labelled `number 1`, `number 2`, ... by its place in the text. The answer lands in the result box, printed in the next row. The file defines `PATTERN`, `CALC` (`ready` or `reference`), `INPUTS`, `BOX_INDEX` (the place of each box's number in the text), `DEFAULTS`, `KINDS`, `LEFT`, `RIGHT` and `place(parent, stacked=False)`, which builds the row with the same `build_row` the operator rows use. Try one: `python operator_row_math_for_algebra_word_problems/preview.py savings/0848`.

### Using them from Python

```python
from operators_one_algebra_word_problem_per_file import get, keys

keys()[:3]                                  # ['age/0001', 'age/0002', ...]  (1,000 keys)
p = get("savings/0848")
p.PROBLEM                                   # 'Ben has $150 saved and adds $25 each week. ...'
p.compute()                                 # 16        (the stored numbers)
p.compute(200, 15, 350, 5)                  # 15        (your own numbers, in the order of p.NUMBERS)
get("system_of_equations/0920").compute()   # [27, 21]  (chickens and pigs: several answers come back as a list)

import operator_row_math_for_algebra_word_problems as rows
rows.get("savings/0848").PATTERN            # '□ + □ w = □ + □ w  ->  answer □'
```

A problem that has several answers returns a list. Whole answers come back as `int`, the rest as `float`.

### How a problem travels

1. **The text** is a problem in `algebra_word_problems/algebra_word_problems.txt`, or a new problem a person pastes.
2. **A solver family answers it.** `algebra_word_problems/algebra_matcher/word_solver.py` has one function per kind of problem. A family only answers when its wording matches, every number has a role, and the answer passes its checks. Otherwise it returns `None`. New families and fixes are done in batches. The short record is `algebra_word_problems_status.txt`. The long write-up of every batch is `algebra_word_problems/algebra_matcher/word_solver_results.txt`.
3. **The problem file and the diagram are generated** by `operator_keys/make_algebra_word_problem_files.py`. On Windows, from the project folder: `.venv\Scripts\python.exe operator_keys\make_algebra_word_problem_files.py`. On Linux: `.venv/bin/python operator_keys/make_algebra_word_problem_files.py`. It needs Pillow. It rewrites every `<id>.py`, `<id>.jpg`, every row file and `INDEX.md`, and it marks each problem Ready or Reference from what the solver answers at that moment. Run it again after every batch that adds or fixes a family.
4. **The row** is the generated file in `operator_row_math_for_algebra_word_problems/`. Its `LIBRARY_KEY` points at the problem file whose `compute(...)` fills the one result box.
5. **Check it.** From `algebra_word_problems/algebra_matcher/`: `python -m unittest test_word_solver test_number_puzzle`. The generated-problem line must say `wrong 0`. Then, from the project folder: `python tests/test_algebra_word_problem_files.py`.
6. **Update the records.** Follow the UPDATE PROTOCOL at the top of `algebra_word_problems_status.txt`: change the numbers, add the batch to DONE, refresh the TO DO appendix with `python algebra_word_problems/algebra_matcher/todo_report.py`, and append the batch to `word_solver_results.txt`. When the Ready count changes, change it in `tests/test_algebra_word_problem_files.py` and in this README. Commit and push only when the user asks. That commit includes the code, the tests, the regenerated folders, the status file and the results file.

### The status files

Read these at the start of every session. Update them every time a batch is finished.

| File | What it holds |
|---|---|
| `algebra_word_problems_status.txt` | The update protocol, the current numbers, what is done, what is left, and the unclaimed wording shapes. Read this one first. |
| `algebra_word_problems/algebra_matcher/word_solver_results.txt` | The long write-up of every batch. Append a new entry. Do not rewrite old entries. |
| `algebra_word_problems/algebra_matcher/todo_report.py` | Prints the unclaimed wording shapes. `--counts` prints only the numbers. |

### What is left

- **The solver covers 349 of the 1,000 generated problems**, and the number-puzzle reader covers 28 more. The other 623 are Reference. The missing wordings are the appendix of `algebra_word_problems_status.txt`.
- **The operator is not built.** Text pasted in the Templates box should be split into word boxes and number boxes, matched to a family, and answered with the reading the solver already produces. When no family is sure, it falls back to the trained matcher. The open window decisions are in `algebra_word_problems/chess_test_results.txt`, section 7.4.
- **The rows are in the window.** A Ready problem clicked in Operators > Algebra word problems goes into the target row (or into a box of a row that already has math), and `=` calls its `compute()`. Several answers show as a list in the result. Reference problems are not placed. The boxes start with the problem's own numbers, so the first `=` works at once; change them and press `=` again. They are labelled `number 1`, `number 2`, ... rather than by role. A list of answers cannot be joined to another row with any join symbol, and inside an operator that wants one number it says so.

### Decisions

1. **The row is the equation, and a box is a blue number of the diagram.** A box is a number of the equation that is also written in the text; it keeps its place in the equation and its value, and starts filled. The labels stay `number 1`, `number 2`, and so on, by place in the text, and `compute()` fills `{0}`, `{1}`, ... from the boxes with the other text numbers as written. Known limits: three Ready problems (`current_wind` 0086, 0090, 0094) have no box, and 102 Ready problems have text numbers that are not boxes, so they cannot be changed in the row. A role label (`first rate`, `total`) is not shown until a family exports those roles, because a label on the wrong box would put a number in the wrong place.
2. **Several answers share the one result box.** `compute()` returns a list, and that list is what the box shows. The row does not grow a box per answer. Advanced Input is for what the person types, not for splitting the result.
3. **The diagram is the equation with each box number in blue and the answer in green; any other number in the equation is plain.** Several equation parts are several lines. Bars, number lines and geometry figures are not added in this pass. The picture is drawn from the stored `Equation:` line, so it stays tied to the ground truth.
4. **The pictures stay in the repository.** The 1,000 diagrams are about 24 MB. The tests check that each jpg is there. They are not generated on demand.
5. **The folder key stays `<category>/<id>`**, for example `savings/0848`. That is the same 55 categories as the ground-truth file. The problems are not split into the 216 wording types, and they are not regrouped by solver family. A Reference problem has no family.
6. **`compute()` rebuilds the sentence and asks the solver.** Numbers that the solver will not accept raise `ValueError`. A Reference problem raises `NotImplementedError`. The row shows that message. It does not show a number when the solver declines.

## Project files

| Path | What it is |
|---|---|
| `main.py` | The calculator window |
| `gui_style.py` | Colours and button styles |
| `operator_links.py` | Connects each Operators pop-up button to its operator |
| `operators_one_operator_per_file/` | The 507 operators: one folder each with `<name>.py` (formula and `compute()`) and `<name>.jpg` (picture). `INDEX.md` lists them all |
| `operator_row_math/` | How each operator is laid out as cards in a row (following its picture), the Advanced Input parser, and the multi-row operators |
| `operator_keys/operator_row_specs.txt` | One line per operator: its picture written as cards. `make_operator_row_files.py` turns it into the row files |
| `operators_one_algebra_word_problem_per_file/` | The 1,000 algebra word problems: one folder each with `<id>.py` (problem, steps, answer, `compute()`) and `<id>.jpg` (diagram). `INDEX.md` lists them all |
| `operator_row_math_for_algebra_word_problems/` | How each algebra word problem is laid out as a row of cards in the calculator |
| `algebra_word_problems/` | The problem list, the generator, and the word solver (`algebra_matcher/`) that answers the problems from their wording |
| `algebra_word_problems_status.txt` | What algebra work is done and to do, and how to keep that list current |
| `operator_keys/make_algebra_word_problem_files.py` | Rebuilds the two algebra word problem folders (run again after the solver changes) |
| `tests/` | The automated test suite |
| `TESTING_GUIDE.md` | How to verify the calculator independently |
| `picture_of_gui/` | Screenshot and the original GUI mock-up |

## Testing

Run the automated test suite (standard library only; Pillow adds the picture check):

```
python tests/test_operators.py
```

It checks all 507 operators: 446 working operators against hand-calculated answers, plus structure,
error handling, input parsing, and the real calculator window for the newer physics operators
(magnetism, fluid dynamics, quantum mechanics, optics, relativity). The full run takes about a
minute because it drives the real window. See [`TESTING_GUIDE.md`](TESTING_GUIDE.md) for how to verify
the calculator independently, including a manual GUI checklist.

Numerical results are checked to about 1e-6, and only the newer physics operators are tested through
the window, so independent verification is still welcome.

The operator rows are checked against their pictures by `python tests/test_operator_pictures.py`.

The algebra word problem folders have their own tests:

```
python tests/test_algebra_word_problem_files.py
```

They check all 1,000 problem folders (file, picture, row), that each file holds the stored text, and that `compute()` works for the 377 problems a solver answers.
The solver itself is tested from `algebra_word_problems/algebra_matcher/` with `python -m unittest test_word_solver test_number_puzzle`.
