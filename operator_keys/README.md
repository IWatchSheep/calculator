# Operator key catalog (for the Rust port)

Generated from the real files by `make_operator_keys.py` (run it from the project root: `python operator_keys/make_operator_keys.py`). Nothing is typed by hand, so the keys are character-identical to the Python folder names.

| File | What it holds |
|---|---|
| `operator_keys.json` | all 526 operators, one object each (see fields below) |
| `operator_keys.tsv` | the same, flat (key, name, symbol, category, subcategory, formula, status, arity, max_args, inputs, compute_signature) |
| `rust_key_mismatch_map.json` | the Rust port's current keys that do not exist in Python -> the Python key to rename them to |

## Fields in `operator_keys.json`

- `key` – exact folder key, e.g. `physics/physics/time_dilation` (always `group/subgroup/name`; physics is flat under `physics/physics/`, geometry under `geometry/geometry/`)
- `name`, `symbol`, `category`, `subcategory`, `formula`
- `status` – `Ready` (454) or `Reference` (72, formula only, no `compute`)
- `inputs` / `input_kinds` – what each box in the row is, left to right, and what to type in it (`number`, `list`, `matrix` ...)
- `arity` – number of boxes in the row (what `row_tree.evaluate` passes positionally to `compute`)
- `compute_signature`, `compute_params` – the real positional signature, with defaults. `required_args` / `max_args` / `varargs` summarise it (`max_args` is `null` when it takes any number)
- `examples` – hand-checked `{args, expected}` pairs from `tests/test_operators.py` (452 examples over 309 operators; cases that use functions, sets or tuples are left out because JSON cannot hold them)

## Things the Rust port must know

- **Optional trailing arguments.** The row passes only the box values; optional arguments keep their defaults. Relativity and similar operators take constants after the boxes, e.g. `time_dilation` is `compute(dt0, v, c=299792458)` and the row has 2 boxes. `gravitational_time_dilation` has 3 boxes, `compute(dt, M, r, G=6.674e-11, c=299792458)`. The `examples` often pass the constants explicitly (e.g. `[100, 1, 4, 1, 1]`) to keep the numbers simple.
- **Varargs.** `math/arithmetic/minimum` and `maximum` take `*values`; the row shows 3 boxes (`x1`, `x2`, `x3`). Several abstract operators take `*args` and are list/structure based (use the Advanced Input window in Python).
- **Possessives** are spelled with an underscore: `ohm_s_law`, `newton_s_second_law`, `zorn_s_lemma`, `laplace_s_equation`.
- **Rust keys that were wrong** (25 of the first 75 the port used; they have since been renamed) were in `rust_key_mismatch_map.json`. The `how` field says how each was matched: same name in a different folder (20), possessive spelling (2), and the three matched by symbol: `math/constants/e` -> `math/constants_and_relations/euler_s_number`, `math/discrete/gcd` -> `.../discrete_and_number_theory/greatest_common_divisor`, `math/discrete/lcm` -> `.../least_common_multiple`.

## Rust parity (how the Rust port is checked against Python)

Run from the project root, in this order, whenever Python operators or Rust functions change:

```
python operator_keys/make_operator_keys.py   # catalog + parity_examples.tsv + parity_differential.tsv
python operator_keys/make_value_grid.py      # parity_values.tsv (about a minute: it runs the real Python operators)
python operator_keys/make_rust_ops.py        # rust_calculator/src/ops/generated.rs
python operator_keys/make_rust_layouts.py    # rust_calculator/src/layouts.rs: how each operator's row is drawn (from the Python row files)
cd rust_calculator && cargo test --release
```

All 454 Ready operators and all 72 Reference operators exist in Rust (`rust_todo.json` is empty).

| File (in `rust_calculator/tests/`) | What it holds |
|---|---|
| `parity_examples.tsv` | 367 hand-checked examples from the Python test suite whose boxes are numbers (or true/false, written 1/0) and whose answer is a number, a pair, true/false or a complex number (`re+imj`) |
| `parity_differential.tsv` | the real Python `compute()` on a fixed grid of numbers (about 7,000 cases): the answer or `ERR` |
| `parity_values.tsv` | the real Python `compute()` on **typed** inputs for the 206 operators whose boxes are lists, matrices, sets, graphs, functions, text ... (about 5,400 cases). The inputs are the text a person types in the Advanced Input window (`1, 2, 3`   `1 2; 3 4`   `x**2 + 3*x`   `A: B, C; B: C`), turned into Python values by the program's own `advanced_input.parse`; answers are JSON with tags for tuples, sets, dicts and complex numbers |
| `parity.rs`, `parity_values.rs` | read those files. Rust must give the same answer, or an error on exactly the same inputs. `MIN_PASSING` stops the count going down |

Rust side: `src/kinds.rs` parses typed text exactly like `advanced_input.parse`; `src/expr.rs` is the safe evaluator for typed functions (`x**2 + 3*x`, `[2*x, 2*y]`, `x > 2`) with Python's error behaviour; `src/ops/{lists,matrices,sets,graphs,calculus,misc}.rs` hold the compute functions (one per operator, named after its folder); `make_rust_ops.py` writes the `Operator { ... }` entries.

Known, deliberate differences (each is an allow-list in the test files):
- Python integers are unbounded and Rust numbers are not (huge factorial-style results are an error or rounded; the grids skip integer results above 10^15).
- For some whole-number operators Rust rejects fractional or negative input where Python returns nonsense (`STRICTER` in `parity.rs`); the prime / field tests say a fractional number is not prime (`FRACTION_NONSENSE`).
- A negative number to a fractional power is a complex number in Python; real-valued Rust operators report an error instead (`COMPLEX_POWER`, and "Python's answer is complex" in `parity_values.rs`).
- Python builds some answers by walking a set, so the order of the items depends on hashing and on text changes from run to run (`direct_product`, `cartesian_product`, `power_set`, and which valid route `hamiltonian_path` finds first): only the items are compared (`ORDER_FREE`).
- `statistics.quantiles` with one data point follows Python 3.13+ (the grid was generated with Python 3.15).
