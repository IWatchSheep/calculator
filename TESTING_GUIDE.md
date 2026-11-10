# Testing guide — how to verify this calculator

This file tells a human or another AI exactly what to run and what to check, so the calculator can be
verified independently. The automated suite is `tests/test_operators.py` (standard library only).

## 1. Setup and run

```
python -m pip install -r requirements.txt     # Pillow (only needed for the diagram check and the GUI)
python tests/test_operators.py                # full run, ~2 seconds
python tests/test_operators.py -v             # one line per test
python tests/test_operators.py NumericTests.test_000_math.arithmetic.addition   # a single test
```

Use the project's `.venv` Python if Pillow is not installed globally. Without Pillow one test is
skipped (`test_diagrams_are_valid_jpegs`). With no display, the GUI smoke test is skipped.

**Last full run (author's machine, Python 3.15, Windows): 682 tests, all passed (the full run now takes about a minute because it drives the real window).**

## 2. What the project contains

| Thing | Count | Where |
|---|---|---|
| Operators | 595 | `operators_one_operator_per_file/<category>/<subcategory>/<operator>/<operator>.py` |
| "Ready" operators (`compute()` calculates) | 523 | marked `Ready` in `operators_one_operator_per_file/INDEX.md` |
| "Reference" operators (formula only) | 66 | marked `Reference`; `compute()` raises `NotImplementedError` |
| Row modules (GUI placement of each operator) | 595 | `operator_row_math/` |
| Button-to-operator links | — | `operator_links.py` |
| Input parser (typed text → Python values) | — | `operator_row_math/advanced_input.py` |

Load any operator with `operators_one_operator_per_file.get("math/algebra/power").compute(2, 10)`.
Keys look like `math/<subcategory>/<name>`, `geometry/geometry/<name>`, `physics/physics/<name>`.

## 3. What the automated suite checks

| Group | Tests | What it proves |
|---|---|---|
| `StructureTests` | 9 | All 595 operators load; each has NAME/SYMBOL/CATEGORY/SUBCATEGORY/FORMULA/`compute`; each has a valid `.jpg` diagram; INDEX.md lists every operator; "Reference" operators really raise `NotImplementedError`; every `operator_links.py` target exists; every operator has a row module; every `.py` file compiles |
| `NumericTests` | 604 | `compute()` returns a hand-calculated answer for known inputs. All 523 Ready operators are covered, most with 2+ cases |
| `ErrorTests` | 9 | Bad input raises a clear exception (`ZeroDivisionError`, `ValueError`, …) instead of returning a wrong number |
| `IdentityTests` | 18 | Operators agree with each other: sin²+cos²=1, exp/ln inverse, M·M⁻¹=I, Pascal's rule, gcd·lcm=ab, A·v=λ·v, RK4 ≈ e, … |
| `InputParserTests` | 4 | Typed text becomes the right Python value; unsafe function text (`__import__`, `x.__class__`, `open(...)`, `exec`) is rejected |
| `GuiSmokeTest` | 1 | `main.CalculatorGUI()` builds, updates and closes |
| `NewPhysicsRowTests` | 3 | The 49 magnetism / fluid / quantum / optics / relativity operators: row module boxes match `compute()` arguments, every operator has a calculator button, row evaluation equals `compute()` |
| `NewPhysicsCalculatorTests` | 6 | Drives the real window for all 49 new operators: pick the operator, type the numbers on the keypad (including the `±` and `EE` keys for negative and tiny values), press `=`, compare with the hand-calculated answer; checks the `±`/`EE` key rules, the `C` / Clear button and that every keypad key is a working one; errors are shown as readable messages |
| `TemplateMathTests` | 10 | The typed-math parser behind the Templates panel: precedence and brackets, operators by name and short name, every alias, empty boxes, readable error messages, unsafe text rejected, the saved-templates file |
| `TemplatePanelTests` | 18 | The Templates panel in the real window: Preview Posted puts the math in the row and a new preview replaces the old one, Save Template (list + file), Apply Template, the whole journey to a calculated answer, duplicates, nothing picked, nesting; the step-by-step guide pop-up (opens once when you start typing, follows your progress with ticks, "keep typing" vs red errors, Got it / ? / Don't show this again remembered, fully on screen and clear of the text box and buttons); the three removed toolbar buttons are gone |

## 4. How another AI should verify (do not just trust the suite)

The suite was written by the same author as the code, so check it rather than believing it.

1. **Run it** (section 1) and confirm it passes on your machine.
2. **Spot-check the expected values.** Open `CASES` in `tests/test_operators.py` and recompute at least
   30 rows yourself, from the maths, not by running the operator. Pick across categories. Any row where
   the expected value is wrong is a bug in the test, and any row where you get a different answer from
   the operator is a bug in the operator.
3. **Mutation check.** Break one operator on purpose (e.g. change `+` to `-` in `addition.py`), re-run, and
   confirm the suite goes red, then `git checkout` the file. Do this for 3 or 4 operators in different
   categories. A suite that stays green after a deliberate break is not testing that operator.
4. **Test what the suite does not.** Try inputs of your own, especially:
   - zero, negative, very large (`1e308`), very small, `float('nan')`, `float('inf')`
   - empty lists, one-element lists, mismatched list lengths, non-square matrices
   - integers vs floats (`factorial(20)`, `fibonacci(90)` must stay exact integers)
   - strings or `None` where a number is expected (should raise, not return garbage)
   Record every case where an operator returns a plausible-looking wrong number or crashes with an
   unhelpful message.
5. **Check against an independent source** for the numerically hard ones: use `numpy`, `scipy`,
   `sympy` or a handheld calculator for eigenvalues, SVD, QR, LU, ODE solvers, integrals, Fourier
   series and special distributions.
6. **Do the manual GUI checklist** (section 6).

## 5. Conventions the tests rely on (so you can tell a bug from a convention)

| Operator | Behaviour |
|---|---|
| trig, `arc_length`, `sector_area`, `law_of_*`, `snell_s_law`, `torque` | angles are **radians** |
| `modulo(-7, 3)` | `2` (result takes the sign of the divisor, floor-style) |
| `quadratic_formula` | always returns two roots as complex numbers, e.g. `(2+0j, 1-0j)` |
| `eigenvalues` | tuple of complex numbers, largest first |
| `eigenvectors` | list of `(eigenvalue, [vectors])` |
| `minimize`, `maximize` | return `(x, f(x))` |
| `cartesian_product`, `power_set` | return lists |
| `prime_factorization(360)` | `[2, 2, 2, 3, 3, 5]` (with repeats) |
| `quartiles`, `percentile`, `interquartile_range` | linear-interpolation method (`quartiles([1..8]) = [2.25, 4.5, 6.75]`) |
| `variance`, `standard_deviation` | **population** (divide by n); `sample_*` divide by n−1 |
| `linear_regression`, `least_squares` | named tuple `(slope, intercept)` |
| `mean_value_theorem` | returns the secant slope (f(b)−f(a))/(b−a), not the point c |
| `integral_test(f, N)` | returns `(Σ f(n) for n=1..N, ∫₁ᴺ f)` |
| `alternating_series_test` | returns `(terms decreasing?, last term)` |
| `epsilon_delta_continuity` | returns *a* valid δ (not necessarily the largest) |
| `spanning_tree` | takes a **weighted** graph `{v: [(neighbour, weight)]}` and returns `(edges, total)` |
| numerical calculus (`derivative`, integrals, limits…) | accurate to about 1e-6, not exact |
| Reference-only operators (66) | `compute()` raises `NotImplementedError` by design |

## 6. Manual GUI checklist (cannot be automated here)

Run `python main.py`, then for each item note pass/fail:

- [ ] Window opens; layout matches `picture_of_gui/gui_template.png`
- [ ] Number pad: type `12 + 7 =` → `19`; `7 ÷ 0` shows an error and does not crash
- [ ] Templates: start typing `(? + 3) × 2` in the text box: the guide pop-up opens (four cards, step 1 turns green with `✓ Understood`); press **Preview Posted** (the math appears in Row 1, step 2 turns green), **Save Template** (step 3), pick it in the list and press **Apply Template** (step 4), fill the box, keypad `=`
- [ ] The guide pop-up is fully on screen, does not cover the text box, list or buttons, and **Got it**, the **?** button and *Don't show this again* work
- [ ] Templates: close and reopen the calculator; the saved template is still in the list. Bad math (`sqrt(`) shows a message and is not saved
- [ ] `C` key and the toolbar `Clear (C)` button: every row goes back to one empty box, join symbols disappear, the results area says "Cleared"
- [ ] `±` key: flips a box between `5` and `-5`; after `EE` it flips the exponent's sign
- [ ] `EE` key: `1.5 EE ± 3` gives `1.5e-3`; a second `EE`, an `EE` on an empty box, and a `.` after `EE` are ignored
- [ ] Open the Operators pop-up; every section lists its buttons
- [ ] Click at least one operator per section (Math, Geometry, Physics): its diagram (`.jpg`) shows and its row appears
- [ ] Fill in the row inputs and compute: result equals `compute()` called directly
- [ ] Advanced Input: enter a list, matrix, function (`x**2 + 3*x`), set, graph; each is accepted
- [ ] Enter invalid text in each input kind: a readable error, no traceback, no freeze
- [ ] Reference-only operator: shows a "reference only" message, not a crash
- [ ] Resize / close / reopen the window

## 7. Where the suite is thin (known gaps)

- The 72 Reference operators are only checked for structure and `NotImplementedError`, because they have
  no calculation to test.
- Several results are numerical approximations; the suite uses a relative tolerance of 1e-6, so errors
  smaller than that are invisible.
- Only a few edge cases per operator (see `ErrorTests`). Section 4 step 4 asks you to probe further.
- The GUI is only smoke-tested automatically; real clicking and display behaviour is the manual list above.

## 8. Reporting results

Reply with: Python version and OS, `Ran N tests … OK/FAILED`, how many CASES rows you re-derived and any
that disagreed, which operators you mutated and whether the suite caught them, every input where an
operator misbehaved (operator key, exact call, expected, actual), and the manual-GUI checklist.
