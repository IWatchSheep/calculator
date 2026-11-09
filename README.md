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

Besides the 507 operators the project is getting a second library: **1,000 algebra word problems**, each stored as its own file with a diagram, and each with a
row layout so it can sit in a calculator row like an operator does. This part is **not wired into the calculator window yet**: the folders, the solver and the
tests exist, and the next step (see *What is left*) is the operator that takes pasted text and uses them.

> ### NOTE TO GROK: please review this section
> Claude wrote this section and the two folders it describes. Please read it, check it against the folders and amend this README directly (fix errors, tighten the
> wording, change a decision you disagree with and say why in the commit message). The decisions I would most like a second opinion on are listed under
> **Questions for review** at the end of this section. After your review the user will restart Claude, and the new Claude will read this section to learn how
> a word problem travels from text to file, diagram and row (see *How a problem travels* below). So the steps must be exactly right.

### The four pieces

| Piece | Where | What it holds |
|---|---|---|
| **The problems** | `algebra_word_problems/algebra_word_problems.txt` | The 1,000 generated problems in 55 categories: Problem / Let / Equation / Solve / Answer. The ground truth. |
| **One problem per file** | `operators_one_algebra_word_problem_per_file/<category>/<id>/` | `<id>.py` (the problem, its steps and its answer, plus `compute(...)`) and `<id>.jpg` (a **diagram** of the problem). `INDEX.md` lists all 1,000. |
| **How a problem goes into a row** | `operator_row_math_for_algebra_word_problems/<category>/<id>/<id>.py` | The row of cards for the calculator, in the same style as `operator_row_math/`. |
| **The solver** | `algebra_word_problems/algebra_matcher/word_solver.py` | 55 families that solve problems straight from their wording. Standard library only. |

Keys look like `savings/0848` (category folder, then the four-digit problem number).

**The diagram** (`<id>.jpg`) shows the problem the way the operator pictures show a formula: the problem text, the "Let" line, and the equation with **every number
in a blue box**, then the answer in green. For example `savings/0848` shows `[150] + [25]w = [310] + [15]w` and "Answer: 16 weeks".

**The problem file** (`<id>.py`) defines `ID, KEY, NAME, CATEGORY, PROBLEM, LET, EQUATION, SOLVE, ANSWER`, and also

- `SOLVER` and `FAMILY`: who answers this problem today (`"word_solver"` with the family name, `"number_puzzle"`, or `None`);
- `TEMPLATE` and `NUMBERS`: the problem text with every number replaced by `{0}`, `{1}` ... and the numbers as written, in order;
- `compute(*numbers)`: puts your numbers into the template and asks the solver. With no arguments it uses the stored numbers.

A problem is **Ready** when a solver answers it (365 of the 1,000: 337 by `word_solver`, 28 by `number_puzzle`) and **Reference** when only the text and its steps
are stored (635). Calling `compute()` on a Reference problem raises `NotImplementedError`; calling it with numbers the solver cannot accept (an equation that would not
have a positive whole answer, for example) raises `ValueError`. It never guesses.

**The row file** lays the problem out as one row: `Savings 0848(□, □, □, □) = □`. There is one small box for every number in the problem (in the order they appear in its text)
and the **answer lands in the box right of `=`**, exactly like `Time dilation(□) = ...` for an operator. The file defines `PATTERN`, `CALC` (`ready` or `reference`),
`INPUTS` (labelled `number 1`, `number 2` ...), `DEFAULTS` (the stored numbers), `KINDS`, `LEFT`, `RIGHT` and `place(parent, stacked=False)`, which builds the row with the
same `build_row` the operator rows use. Try one: `python operator_row_math_for_algebra_word_problems/preview.py savings/0848`.

### Using them from Python

```python
from operators_one_algebra_word_problem_per_file import get, keys

keys()[:3]                                  # ['age/0001', 'age/0002', ...]  (1,000 keys)
p = get("savings/0848")
p.PROBLEM                                   # 'Ben has $150 saved and adds $25 each week. ...'
p.compute()                                 # 16        (the stored numbers)
p.compute(200, 15, 350, 5)                  # 15        (your own numbers, in the order of p.NUMBERS)
get("system_of_equations/0920").compute()   # [27, 21]  (chickens and pigs: a problem with two answers returns a list)

import operator_row_math_for_algebra_word_problems as rows
rows.get("savings/0848").PATTERN            # 'Savings 0848(□, □, □, □) = □'
```

A problem that has several answers (for example "How many of each?") returns a list. Whole answers come back as `int`, the rest as `float`.

### How a problem travels  (the steps the next Claude follows)

1. **The text** is a problem in `algebra_word_problems/algebra_word_problems.txt` (the generated ones), or a new problem a person pastes.
2. **A solver family answers it.** `algebra_word_problems/algebra_matcher/word_solver.py` has one function per kind of problem (`savings_equal`, `two_scores`, `pipes_and_drain` ...).
   A family only answers when its wording matches, **every number has a role** and the answer passes its sanity checks; otherwise it declines (returns `None`) and nothing wrong is
   ever shown. New families, and fixes to old ones, are done in batches; the status of that work is kept in `algebra_word_problems_status.txt` and the long write-up of every batch in
   `algebra_word_problems/algebra_matcher/word_solver_results.txt`.
3. **The problem file and the diagram are generated** from the text and the solver: run `.venv\Scripts\python.exe operator_keys\make_algebra_word_problem_files.py` (it needs
   Pillow, which the project's `.venv` has). It rewrites every `<id>.py`, `<id>.jpg`, every row file and `INDEX.md`, and it marks each problem Ready or Reference from what the solver
   answers at that moment. Run it **again after every batch that adds or fixes a family**, otherwise a newly solvable problem stays marked Reference.
4. **The row** is the generated file in `operator_row_math_for_algebra_word_problems/`. The calculator window will place it with `place(parent)`; its `LIBRARY_KEY` points at the
   problem file whose `compute(...)` fills the result box.
5. **Check it**: `python tests/test_algebra_word_problem_files.py` (1,000 folders, files, pictures, rows, and `compute()` for all 365 Ready problems), then
   `python -m unittest test_word_solver test_number_puzzle` from `algebra_word_problems/algebra_matcher/` for the solver itself.
6. **Update the status file** `algebra_word_problems_status.txt` (its UPDATE PROTOCOL says how) and commit the code, the regenerated folders, the README if it changed, and the status file together.

### The status files (how Claude keeps track of the algebra work)

Three files record where the algebra word problem work stands. **Read them at the start of every session, and update them every time a batch (a new family or a fix) is finished.**

| File | What it holds | How to read / update it |
|---|---|---|
| `algebra_word_problems_status.txt` (project root) | **The one to read first.** The update protocol, where everything is, the numbers (claimed / 1,000, wrong must stay 0, hand-written answered, test count, last commit), what is DONE per batch, what is TO DO, the working rules and technical lessons, and an appendix of unclaimed wording shapes. | Follow its UPDATE PROTOCOL after every batch: run the solver tests and the generated-problem check, change the numbers, add the batch to DONE, move finished items out of TO DO, then regenerate the appendix. Commit it together with the code. |
| `algebra_word_problems/algebra_matcher/word_solver_results.txt` | The long write-up of every batch (families added, wrong answers fixed, fresh-set results). | Append a short entry for the batch; never rewrite old entries. |
| `algebra_word_problems/algebra_matcher/todo_report.py` | Script that prints the unclaimed wording shapes (what the solver still cannot answer); `--counts` prints only the numbers. | Run `python algebra_word_problems/algebra_matcher/todo_report.py` to refresh the TO DO appendix of the status file. |

**Each time a problem or family is finished:**

1. Read `algebra_word_problems_status.txt` (UPDATE PROTOCOL first).
2. Do the batch (family or fix) in `word_solver.py` with tests and a fresh problem set, never tuning on the fresh set.
3. Run the tests: `python -m unittest test_word_solver test_number_puzzle` from `algebra_word_problems/algebra_matcher/`. The output must say 0 wrong.
4. Regenerate the two folders: `.venv\Scripts\python.exe operator_keys\make_algebra_word_problem_files.py`, then `python tests/test_algebra_word_problem_files.py`. Change the Ready count in that test and in this README when the claimed count changes.
5. Update the numbers, the DONE list and the TO DO appendix in `algebra_word_problems_status.txt`, and add the batch to `word_solver_results.txt`.
6. Commit the code, tests, regenerated folders and status files together, and push.

### What is left

- **The solver covers 337 of the 1,000 generated problems** (plus 28 by the number-puzzle reader); the other 635 are Reference. The list of what is missing, by wording, is the appendix of
  `algebra_word_problems_status.txt` (regenerate it with `python algebra_word_problems/algebra_matcher/todo_report.py`).
- **The operator is not built:** text pasted in the Templates box should be split into word boxes and number boxes, matched to a family and answered (with the reading the solver already
  produces), falling back to the trained matcher when no family is sure. The open decisions are in `algebra_word_problems/chess_test_results.txt` part 7.4.
- The row files are laid out but nothing in the window loads them yet (like `operators_one_operator_per_file/`, which also is not imported by the window directly).

### Questions for review  (Grok)

1. **The row shape.** A word problem is a row `Name(□, □, ...) = □` with one generic box per number (`number 1`, `number 2` ...). Would the row be more useful if the boxes were
   labelled by role (`first rate`, `total`) and the right side showed the equation instead of a single answer box? The solver knows the roles inside each family but does not export them yet.
2. **Several answers.** "How many of each?" returns a list, but the row has one result box. Should such a problem put the list into the box through Advanced Input, or get one result box per answer?
3. **Diagram.** Is "the equation with the numbers in blue boxes" the right picture of a word problem? It is generated from the stored `Equation:` line, so problems whose equation has
   several parts (`x + y = 30; 2x + 4y = 84`) draw one line per part. Anything else you would want drawn (a bar, a number line, a figure for the geometry problems)?
4. **Size.** The 1,000 pictures are about 24 MB and the row files 4 MB (mostly small files). Acceptable for the repository, or should the pictures be smaller or generated on demand?
5. **Naming.** Folders are `<category>/<id>` (for example `savings/0848`), not one folder per problem *type* (there are 216 types). Is the category the right grouping?
6. **`compute()` rebuilds the text.** It fills the template with the numbers and calls the solver, so numbers that change the wording's meaning (a negative count) decline. Is that the behaviour you want
   from a row, or should the row show a message when it declines?

## Project files

| Path | What it is |
|---|---|
| `main.py` | The calculator window |
| `gui_style.py` | Colours and button styles |
| `operator_links.py` | Connects each Operators pop-up button to its operator |
| `operators_one_operator_per_file/` | The 507 operators: one folder each with `<name>.py` (formula and `compute()`) and `<name>.jpg` (picture). `INDEX.md` lists them all |
| `operator_row_math/` | How each operator is laid out as cards in a row, the Advanced Input parser, and the multi-row operators |
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

The algebra word problem folders have their own tests:

```
python tests/test_algebra_word_problem_files.py
```

They check all 1,000 problem folders (file, picture, row), that each file holds the stored text, and that `compute()` works for the 365 problems a solver answers.
The solver itself is tested from `algebra_word_problems/algebra_matcher/` with `python -m unittest test_word_solver test_number_puzzle`.
