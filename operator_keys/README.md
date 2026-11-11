# Operator key catalog

Generated from the real files by `make_operator_keys.py` (run it from the project root: `python operator_keys/make_operator_keys.py`). Nothing is typed by hand, so the keys are character-identical to the Python folder names.

| File | What it holds |
|---|---|
| `operator_keys.json` | all 631 operators, one object each (see fields below) |
| `operator_keys.tsv` | the same, flat (key, name, symbol, category, subcategory, formula, status, arity, max_args, inputs, compute_signature) |

## Fields in `operator_keys.json`

- `key` – exact folder key, e.g. `physics/physics/time_dilation` (always `group/subgroup/name`; physics is flat under `physics/physics/`, geometry under `geometry/geometry/`)
- `name`, `symbol`, `category`, `subcategory`, `formula`
- `status` – `Ready` (559) or `Reference` (72, formula only, no `compute`)
- `inputs` / `input_kinds` – what each box in the row is, left to right, and what to type in it (`number`, `list`, `matrix` ...)
- `arity` – number of boxes in the row (what `row_tree.evaluate` passes positionally to `compute`)
- `compute_signature`, `compute_params` – the real positional signature, with defaults. `required_args` / `max_args` / `varargs` summarise it (`max_args` is `null` when it takes any number)
- `examples` – hand-checked `{args, expected}` pairs from `tests/test_operators.py` (452 examples over 309 operators; cases that use functions, sets or tuples are left out because JSON cannot hold them)

## Notes on operators

- **Optional trailing arguments.** The row passes only the box values; optional arguments keep their defaults. Relativity and similar operators take constants after the boxes, e.g. `time_dilation` is `compute(dt0, v, c=299792458)` and the row has 2 boxes. `gravitational_time_dilation` has 3 boxes, `compute(dt, M, r, G=6.674e-11, c=299792458)`. The `examples` often pass the constants explicitly (e.g. `[100, 1, 4, 1, 1]`) to keep the numbers simple.
- **Varargs.** `math/arithmetic/minimum` and `maximum` take `*values`; the row shows 3 boxes (`x1`, `x2`, `x3`). Several abstract operators take `*args` and are list/structure based (use the Advanced Input window in Python).
- **Possessives** are spelled with an underscore: `ohm_s_law`, `newton_s_second_law`, `zorn_s_lemma`, `laplace_s_equation`.
