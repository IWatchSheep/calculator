# Rust Calculator

Rust **1.83** port of the Python Tkinter calculator in this repo (`main.py`).

**Goal:** the same program — operators in rows, fill boxes, press `=`, browse the
operator library — built toward full parity in phases.

## Rows follow the pictures (the design rules)

The Rust rows are drawn by the same rules as the Python program (see the README in the repo root, section *Design rules for the rows*):

1. Math that can be written on several lines is always written on several lines: a fraction has its numerator on the row above its bar and its denominator on the row below, an exponent is one line up, a subscript one line down.
2. Those lines are ONE row. They are not Row 2, Row 3 ...; the Next Row button goes from Row 1 to Row 2.
3. The answer is shown to the right of the `=`, on the same row (and in the formula's own answer box, e.g. the `F` of `F = G m1 m2 / r²`; a formula with two answers, like the quadratic formula's `x1`, `x2`, shows each in its own box).
4. Row 2 is joined to Row 1 by a math sign (`+ − × ÷ = ≠ < > ≤ ≥`); `=` shows each row's own answer and the answer for both on Row 3.
5. Every operator's row follows its picture: a variable the picture writes twice is one input with two boxes.

How: `src/layouts.rs` holds every operator's picture as cards. It is GENERATED from the Python row files and must not be edited by hand:

```
python operator_keys/make_rust_layouts.py      # from the repo root; run it whenever the Python row files change
```

`src/layout.rs` places the cards on a grid (numerator / bar / denominator, exponents) and has the unit tests of that; `src/row.rs` has the row rules (`Document::equals_all`: each row's own answer, joins, the answer row); `src/app.rs` draws it. `tests/rows.rs` checks the row rules. A Python test (`tests/test_operator_pictures.py`) fails if `layouts.rs` is out of date.

To look at one row: `cargo run --release -- --demo physics/physics/gravitation 5 2 3`.

Answers are shown like the Python program (`7.415555556e-11`, `24`), through `Value::show`; `Value::display` stays the exact form the parity tests use.

Sets and neighbour lists keep the order they were typed in, on both sides: `Direct product` of `a, b, c` and `1, 2, 3` lists (a,1) (a,2) (a,3) (b,1) ... (the diagram reads g in G, h in H). Python used to list letters in a different order every run (a plain `set`); `OrderedSet` in `operator_row_math/advanced_input.py` and `_NeighbourSet` in `operators_one_operator_per_file/_helpers.py` fixed that, and `make_value_grid.py` now writes the same file under every `PYTHONHASHSEED`.

## What is in the Rust program

Everything in the Python program is ported:

- all 512 operators (446 Ready, 66 Reference), each drawn from its picture (`layouts.rs`), with typed values for lists, matrices, sets, graphs and functions (`kinds.rs`, `expr.rs`)
- the Advanced Input window, the kind hint in every box, the formula pictures (the JPGs) and the word-problem diagrams (`pictures.rs`)
- operators nested inside operators and the multi-row operators (`multirow.rs`)
- Mathematical Templates (`template_math.rs`)
- the algebra word problems: the solver (`word_solver/`, number puzzle + 58 families) and the 377 Ready problems in an "Algebra word problems" tab

`WORKLIST.md` is the status; `operator_keys/README.md` says how the parity files are made. Still open: larger boxes for matrices, graphs and long functions.

## Build and run

```
cd rust_calculator
cargo run --release --locked
```

Tests:

```
cargo test --release --locked
```

`rust-version = "1.83"` in `Cargo.toml`. Built with a newer rustc is fine.

**Always use `--locked` with Rust 1.83.** `Cargo.lock` pins older crate versions (for example `idna_adapter`, `webbrowser`, and `mime_guess2` 2.0.5) that 1.83 can compile. Newer ones need a newer Cargo (`edition2024`). Without `--locked`, or after `cargo update`, Cargo may pull those newer versions and the build fails on 1.83. Keep `Cargo.lock` committed. To refresh it safely, run `CARGO_RESOLVER_INCOMPATIBLE_RUST_VERSIONS=fallback cargo update`, then `cargo update mime_guess2 --precise 2.0.5`, then check with `cargo +1.83.0 build --locked`.

## Layout

| Path | Role |
|---|---|
| `src/main.rs` | Window entry |
| `src/app.rs` | egui UI (toolbar, rows, keypad, Operators) |
| `src/row.rs` | Document / row / join / compute wiring |
| `src/operator.rs` | Operator metadata (Python NAME/SYMBOL/FORMULA/CALC) |
| `src/ops/` | the operators (`generated.rs` registry, `lists`, `matrices`, `sets`, `graphs`, `calculus`, `misc`, `words`) + `compute` |
| `src/value.rs` | Number / pair / bool / complex / text / list / tuple / set / dict / function values |
| `src/kinds.rs`, `src/expr.rs` | typed text -> `Value` (Advanced Input rules), typed functions |
| `src/layout.rs`, `src/layouts.rs`, `src/multirow.rs`, `src/pictures.rs` | row placement, generated pictures, multi-row operators, formula / word-problem images |
| `src/template_math.rs` | Mathematical Templates |
| `src/word_solver/`, `src/word_layouts.rs` | algebra word-problem solver and equation rows |
| `tests/` | parity with Python (`parity*.rs`, `words.rs`, `word_solver_parity.rs`), rows, nesting, templates |
