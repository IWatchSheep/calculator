# Rust calculator - status

**Full Ready parity reached.** All 446 Ready operators and all 61 Reference operators exist in Rust
(`operator_keys/rust_todo.json` is empty). Verify from the repo root (details in `operator_keys/README.md`):

```
python operator_keys/make_operator_keys.py
python operator_keys/make_value_grid.py
python operator_keys/make_rust_ops.py
cd rust_calculator && cargo test --release
```

Success = 0 parity failures; `MIN_PASSING` (in `tests/parity.rs` and `tests/parity_values.rs`) only goes up.

## Done

- Canonical keys, parity harness, numeric / bool / complex operators (see `operator_keys/README.md`)
- `Value` now has List, Tuple, Set, Dict and Func (a function typed as text) as well as Number, Pair, Bool, Complex, Text
- `src/kinds.rs`: typed text -> `Value`, the same rules as the Python Advanced Input window
- `src/expr.rs`: safe evaluator for typed functions with Python's error behaviour
- `src/ops/{lists,matrices,sets,graphs,calculus,misc}.rs`: 206 operators on typed values (statistics, linear algebra, sets and topology, graphs, calculus and numerical methods, ODEs, contour integrals, group tests, polynomial text)
- A row box takes typed text (`1, 2, 3`   `1 2; 3 4`   `x**2 + 3*x`   `A: B, C; B: C`): `Row::compute` uses `Operator::kinds` and `run_values`
- `tests/parity_values.tsv`: about 4,700 cases from the real Python operators on typed inputs; all agree

## Still open (product work, not operator maths)

- GUI: show each box's expected kind as a hint (lists, matrices, functions ...) and offer an Advanced Input window
- Larger boxes for matrices, graphs and long functions
- Formula JPGs, templates, nested operators, multi-row layouts
- Commit `rust_calculator/` (keep `target/` out; `.gitignore` already excludes it)
