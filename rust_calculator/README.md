# Rust Calculator

Rust **1.83** port of the Python Tkinter calculator in this repo (`main.py`).

**Goal:** the same program — operators in rows, fill boxes, press `=`, browse the
operator library — built toward full parity in phases.

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
