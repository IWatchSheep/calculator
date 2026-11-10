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

Not ported yet: the algebra word problems (the solver is about 3,000 lines of Python), templates, the Advanced Input window, operators nested inside operators, the multi-row operators, the formula pictures (the JPGs).

## Phase 1 (this folder)

- Desktop GUI (`eframe` / `egui`)
- Rows with input boxes, join symbols, Clear / Next Row
- Number pad and Operators browser (filter + category)
- **60+ ready operators**: arithmetic, algebra, trigonometry, discrete, geometry, common physics (including time dilation)

Not yet (later phases, same architecture): all 507 operators, formula JPG diagrams, Advanced Input, templates, nested operators-inside-operators, multi-row auto layouts.

## Build and run

```
cd rust_calculator
cargo run --release
```

Tests:

```
cargo test --release
```

`rust-version = "1.83"` in `Cargo.toml`. Built with a newer rustc is fine.

## Layout

| Path | Role |
|---|---|
| `src/main.rs` | Window entry |
| `src/app.rs` | egui UI (toolbar, rows, keypad, Operators) |
| `src/row.rs` | Document / row / join / compute wiring |
| `src/operator.rs` | Operator metadata (Python NAME/SYMBOL/FORMULA/CALC) |
| `src/ops/mod.rs` | Phase-1 registry + `compute` |
| `src/value.rs` | Number / pair / text results |
