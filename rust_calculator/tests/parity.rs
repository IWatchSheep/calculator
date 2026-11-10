//! Parity with the Python calculator.
//!
//! `parity_examples.tsv` is generated from the hand-checked cases in the Python test suite
//! (`python operator_keys/make_operator_keys.py`).  Every example whose operator exists in Rust must give the
//! same answer.  Examples for operators that are not ported yet are counted, not failed, and
//! `coverage_does_not_shrink` stops the count from going backwards.
//!
//! Expected tokens (after layer 1): plain numbers, `true`/`false`, and `re±imj` complexes.
//! Claude regenerates the TSVs with those forms once layer 1 is in; until then number-only rows still work.

use rust_calculator::ops;
use rust_calculator::value::{self, Value};

const EXAMPLES: &str = include_str!("parity_examples.tsv");
const DIFFERENTIAL: &str = include_str!("parity_differential.tsv");

/// Number of examples that must pass today.  Raise it whenever more operators are ported.
const MIN_PASSING: usize = 366;

fn close(actual: f64, expected: f64) -> bool {
    if expected == 0.0 {
        return actual.abs() <= 1e-9;
    }
    (actual - expected).abs() <= 1e-9 * expected.abs()
}

fn close_abs(actual: f64, expected: f64) -> bool {
    (actual - expected).abs() <= 1e-9 * expected.abs() + 1e-12
}

fn numbers(s: &str) -> Vec<f64> {
    s.split_whitespace()
        .map(|t| t.parse::<f64>().unwrap_or_else(|_| panic!("bad number {t:?}")))
        .collect()
}

fn expected_tokens(s: &str) -> Vec<Value> {
    s.split_whitespace()
        .map(|t| value::parse_token(t).unwrap_or_else(|e| panic!("{e}")))
        .collect()
}

fn value_matches(got: &Value, expected: &[Value], abs: bool) -> bool {
    let c = if abs { close_abs } else { close };
    match (got, expected) {
        (Value::Number(n), [Value::Number(e)]) => c(*n, *e),
        (Value::Pair(a, b), [Value::Number(e1), Value::Number(e2)]) => {
            (c(*a, *e1) && c(*b, *e2)) || (c(*a, *e2) && c(*b, *e1))
        }
        (Value::Bool(b), [Value::Bool(e)]) => b == e,
        (Value::Complex(re, im), [Value::Complex(ere, eim)]) => c(*re, *ere) && c(*im, *eim),
        // Allow a real result written as a complex with imag 0, and vice versa.
        (Value::Number(n), [Value::Complex(ere, eim)]) if *eim == 0.0 => c(*n, *ere),
        (Value::Complex(re, im), [Value::Number(e)]) if *im == 0.0 => c(*re, *e),
        _ => false,
    }
}

struct Tally {
    passed: usize,
    not_ported: usize,
    failures: Vec<String>,
}

fn run_all() -> Tally {
    let mut t = Tally {
        passed: 0,
        not_ported: 0,
        failures: vec![],
    };
    for line in EXAMPLES.lines().filter(|l| !l.starts_with('#') && !l.trim().is_empty()) {
        let mut parts = line.split('\t');
        let key = parts.next().unwrap();
        let args = numbers(parts.next().unwrap());
        let expected = expected_tokens(parts.next().unwrap());
        let Some(op) = ops::get(key) else {
            t.not_ported += 1;
            continue;
        };
        let got = op.run(&args);
        let ok = match &got {
            Ok(v) => value_matches(v, &expected, false),
            Err(_) => false,
        };
        if ok {
            t.passed += 1;
        } else {
            t.failures
                .push(format!("{key}({args:?}): expected {expected:?}, got {got:?}"));
        }
    }
    t
}

#[test]
fn ported_operators_match_python() {
    let t = run_all();
    println!(
        "parity: {} passed, {} wrong, {} for operators not ported yet",
        t.passed,
        t.failures.len(),
        t.not_ported
    );
    assert!(
        t.failures.is_empty(),
        "{} example(s) differ from Python:\n{}",
        t.failures.len(),
        t.failures.join("\n")
    );
}

#[test]
fn coverage_does_not_shrink() {
    let t = run_all();
    assert!(
        t.passed >= MIN_PASSING,
        "only {} examples pass, expected at least {}",
        t.passed,
        MIN_PASSING
    );
}

/// Whole-number operators where Rust rejects fractional or negative input that Python computes something for.
const STRICTER: &[&str] = &[
    "math/discrete_and_number_theory/euler_s_totient",
    "math/graph_theory_and_combinatorics/partition_number",
    "math/graph_theory_and_combinatorics/stirling_number_second_kind",
    "math/algebra/binomial_theorem",
    "math/graph_theory_and_combinatorics/bell_number",
    "math/discrete_and_number_theory/fibonacci",
];

/// Python answers `true` for a fractional number such as 7.5 (it truncates it, or its loop never finds a divisor);
/// Rust says a fractional number is not prime.  Only fractional input may differ.
const FRACTION_NONSENSE: &[&str] = &[
    "math/discrete_and_number_theory/prime_check",
    "math/abstract_algebra/field",
    "math/abstract_algebra/integral_domain",
];

/// A negative number raised to a fractional power: Python's `**` returns a complex number, the Rust operators
/// are real-valued and report an error instead.  Allowed only when Python's answer is complex.
const COMPLEX_POWER: &[&str] = &[
    "math/algebra/nth_root",
    "math/algebra/power",
    "math/algebra/geometric_sequence",
    "math/algebra/geometric_series_sum",
];

/// The real Python `compute()` run on a grid of inputs: same value, or an error on exactly the same inputs.
#[test]
fn differential_grid_matches_python() {
    let (mut checked, mut skipped) = (0usize, 0usize);
    let mut failures: Vec<String> = vec![];
    for line in DIFFERENTIAL.lines().filter(|l| !l.starts_with('#') && !l.trim().is_empty()) {
        let mut parts = line.split('\t');
        let (key, args, want) = (
            parts.next().unwrap(),
            numbers(parts.next().unwrap()),
            parts.next().unwrap(),
        );
        let Some(op) = ops::get(key) else {
            skipped += 1;
            continue;
        };
        checked += 1;
        let got = op.run(&args);
        let ok = if want == "ERR" {
            got.is_err()
        } else {
            match &got {
                Ok(v) => {
                    value_matches(v, &expected_tokens(want), true)
                        || (FRACTION_NONSENSE.contains(&key) && args.iter().any(|v| v.fract() != 0.0))
                }
                // Python happily returns a number for nonsense input (a fractional n in n!, a negative count);
                // Rust refuses.  That is allowed only for these whole-number operators and only for such input.
                Err(_) => {
                    (STRICTER.contains(&key) && args.iter().any(|v| v.fract() != 0.0 || *v < 0.0))
                        || (COMPLEX_POWER.contains(&key) && want.ends_with('j'))
                }
            }
        };
        if !ok {
            failures.push(format!(
                "{key}({args:?}): Python gave {want}, Rust gave {got:?}"
            ));
        }
    }
    println!(
        "differential: {checked} cases checked, {skipped} for operators not ported yet, {} differ",
        failures.len()
    );
    let shown: Vec<_> = failures.iter().take(1000).cloned().collect();
    assert!(
        failures.is_empty(),
        "{} case(s) differ from Python (first {}):\n{}",
        failures.len(),
        shown.len(),
        shown.join("\n")
    );
}
