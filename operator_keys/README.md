# Operator key catalog (for the Rust port)

Generated from the real files by `make_operator_keys.py` (run it from the project root: `python operator_keys/make_operator_keys.py`). Nothing is typed by hand, so the keys are character-identical to the Python folder names.

| File | What it holds |
|---|---|
| `operator_keys.json` | all 507 operators, one object each (see fields below) |
| `operator_keys.tsv` | the same, flat (key, name, symbol, category, subcategory, formula, status, arity, max_args, inputs, compute_signature) |
| `rust_key_mismatch_map.json` | the Rust port's current keys that do not exist in Python -> the Python key to rename them to |

## Fields in `operator_keys.json`

- `key` – exact folder key, e.g. `physics/physics/time_dilation` (always `group/subgroup/name`; physics is flat under `physics/physics/`, geometry under `geometry/geometry/`)
- `name`, `symbol`, `category`, `subcategory`, `formula`
- `status` – `Ready` (446) or `Reference` (61, formula only, no `compute`)
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
python operator_keys/make_operator_keys.py   # catalog + the two test data files below
python operator_keys/make_rust_ops.py        # rust_calculator/src/ops/generated.rs
cd rust_calculator && cargo test --release
```

- `rust_calculator/tests/parity_examples.tsv` - the 367 hand-checked examples from the Python test suite whose boxes are numbers (or true/false, written 1/0) and whose answer is a number, a pair, true/false or a complex number (`re+imj`).
- `rust_calculator/tests/parity_differential.tsv` - the real Python `compute()` run on a fixed grid (about 7,000 cases; numbers, pairs, true/false and complex answers), recording the answer or `ERR`. Rust must agree on every answer **and on which inputs are errors**.
- `rust_calculator/tests/parity.rs` - reads both files. `MIN_PASSING` stops the count of passing examples from going down.
- `make_rust_ops.py` writes an `Operator { ... }` entry (key, name, symbol, formula, pattern, boxes, constants with defaults) for every operator that has a Rust function named after its folder in `src/ops/physics.rs`, `geometry.rs` or `math.rs`, and for all 61 Reference operators. Only the compute bodies are written by hand. `rust_todo.json` lists the Ready operators with no Rust function yet.

Known, deliberate differences: Python integers are unbounded and Rust numbers are not (factorial-style results beyond what fits are an error or rounded; the grid skips integer results above 10^15); and for a few whole-number operators Rust rejects fractional or negative input where Python returns nonsense (listed in `STRICTER` in `parity.rs`); fractional input to the prime / field tests, where Python returns `true` (`FRACTION_NONSENSE`); and a negative number to a fractional power, where Python returns a complex number and Rust reports an error (`COMPLEX_POWER`).
