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

**Last full run (author's machine, Python 3.15, Windows): 535 tests, all passed.**

## 2. What the project contains

| Thing | Count | Where |
|---|---|---|
| Operators | 458 | `operators_one_operator_per_file/<category>/<subcategory>/<operator>/<operator>.py` |
| "Ready" operators (`compute()` calculates) | 397 | marked `Ready` in `operators_one_operator_per_file/INDEX.md` |
| "Reference" operators (formula only) | 61 | marked `Reference`; `compute()` raises `NotImplementedError` |
| Row modules (GUI placement of each operator) | 458 | `operator_row_math/` |
| Button-to-operator links | — | `operator_links.py` |
| Input parser (typed text → Python values) | — | `operator_row_math/advanced_input.py` |

Load any operator with `operators_one_operator_per_file.get("math/algebra/power").compute(2, 10)`.
Keys look like `math/<subcategory>/<name>`, `geometry/geometry/<name>`, `physics/physics/<name>`.

## 3. What the automated suite checks

| Group | Tests | What it proves |
|---|---|---|
| `StructureTests` | 9 | All 458 operators load; each has NAME/SYMBOL/CATEGORY/SUBCATEGORY/FORMULA/`compute`; each has a valid `.jpg` diagram; INDEX.md lists every operator; "Reference" operators really raise `NotImplementedError`; every `operator_links.py` target exists; every operator has a row module; every `.py` file compiles |
| `NumericTests` | 494 | `compute()` returns a hand-calculated answer for known inputs. All 397 Ready operators are covered, most with 2+ cases |
| `ErrorTests` | 9 | Bad input raises a clear exception (`ZeroDivisionError`, `ValueError`, …) instead of returning a wrong number |
| `IdentityTests` | 18 | Operators agree with each other: sin²+cos²=1, exp/ln inverse, M·M⁻¹=I, Pascal's rule, gcd·lcm=ab, A·v=λ·v, RK4 ≈ e, … |
| `InputParserTests` | 4 | Typed text becomes the right Python value; unsafe function text (`__import__`, `x.__class__`, `open(...)`, `exec`) is rejected |
| `GuiSmokeTest` | 1 | `main.CalculatorGUI()` builds, updates and closes |

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
| Reference-only operators (61) | `compute()` raises `NotImplementedError` by design |

## 6. Manual GUI checklist (cannot be automated here)

Run `python main.py`, then for each item note pass/fail:

- [ ] Window opens; layout matches `picture_of_gui/gui_template.png`
- [ ] Number pad: type `12 + 7 =` → `19`; `7 ÷ 0` shows an error and does not crash
- [ ] Open the Operators pop-up; every section lists its buttons
- [ ] Click at least one operator per section (Math, Geometry, Physics): its diagram (`.jpg`) shows and its row appears
- [ ] Fill in the row inputs and compute: result equals `compute()` called directly
- [ ] Advanced Input: enter a list, matrix, function (`x**2 + 3*x`), set, graph; each is accepted
- [ ] Enter invalid text in each input kind: a readable error, no traceback, no freeze
- [ ] Reference-only operator: shows a "reference only" message, not a crash
- [ ] Resize / close / reopen the window

## 7. Where the suite is thin (known gaps)

- The 61 Reference operators are only checked for structure and `NotImplementedError`, because they have
  no calculation to test.
- Several results are numerical approximations; the suite uses a relative tolerance of 1e-6, so errors
  smaller than that are invisible.
- Only a few edge cases per operator (see `ErrorTests`). Section 4 step 4 asks you to probe further.
- The GUI is only smoke-tested automatically; real clicking and display behaviour is the manual list above.

## 8. Reporting results

Reply with: Python version and OS, `Ran N tests … OK/FAILED`, how many CASES rows you re-derived and any
that disagreed, which operators you mutated and whether the suite caught them, every input where an
operator misbehaved (operator key, exact call, expected, actual), and the manual-GUI checklist.
