//! Parity for operators whose boxes are lists, matrices, sets, graphs or functions.
//!
//! `parity_values.tsv` is written by `operator_keys/make_value_grid.py`: typed inputs (the text a person types in
//! the Advanced Input window) and what the REAL Python `compute()` returned for them, or `ERR`.  Every line whose
//! operator exists in Rust must give the same answer, or an error on exactly the same inputs.

use rust_calculator::kinds::parse_kind;
use rust_calculator::ops;
use rust_calculator::value::Value;
use rust_calculator::valuejson::{parse_json_value, values_match};

const VALUES: &str = include_str!("parity_values.tsv");

/// Number of cases that must pass today.  Raise it whenever more operators are ported.
const MIN_PASSING: usize = 4600;

/// Where Python returns a complex number from real input (a negative number to a fractional power, the square
/// root of a negative) the Rust operators are real-valued and report an error: allowed only in that situation.
fn has_complex(v: &Value) -> bool {
    match v {
        Value::Complex(..) => true,
        Value::List(a) | Value::Tuple(a) | Value::Set(a) => a.iter().any(has_complex),
        Value::Dict(d) => d.iter().any(|(k, x)| has_complex(k) || has_complex(x)),
        _ => false,
    }
}

/// Python builds these answers by walking a set, so the order of the items depends on the hash of each item
/// (and for text it changes from run to run).  Only the items are compared, not their order.
const ORDER_FREE: &[&str] = &[
    "math/abstract_algebra/direct_product",
    "math/category_theory_and_foundations/cartesian_product",
    "math/category_theory_and_foundations/power_set",
    "math/graph_theory_and_combinatorics/hamiltonian_path", // which valid path comes first depends on set order
];

fn as_set(v: &Value) -> Value {
    match v {
        Value::List(a) => Value::Set(a.clone()),
        other => other.clone(),
    }
}

struct Outcome {
    passed: usize,
    skipped: usize,
    failures: Vec<String>,
    /// seconds spent per operator (printed with --nocapture, slowest first)
    seconds: Vec<(String, f64)>,
}

fn run() -> Outcome {
    let mut o = Outcome { passed: 0, skipped: 0, failures: vec![], seconds: vec![] };
    for line in VALUES.lines().filter(|l| !l.starts_with('#') && !l.trim().is_empty()) {
        let mut parts = line.split('\t');
        let (key, texts, want) = (parts.next().unwrap(), parts.next().unwrap(), parts.next().unwrap());
        let Some(op) = ops::get(key) else {
            o.skipped += 1;
            continue;
        };
        if op.compute_v.is_none() && op.kinds.is_empty() && !op.inputs.is_empty() {
            o.skipped += 1;
            continue;
        }
        let texts: Vec<String> = match parse_json_value(texts) {
            Ok(Value::List(items)) => items
                .into_iter()
                .map(|v| match v {
                    Value::Text(t) => t,
                    other => panic!("input text expected, got {other:?}"),
                })
                .collect(),
            other => panic!("bad input list {other:?}"),
        };
        let kinds: Vec<&str> = if op.kinds.is_empty() { vec!["number"; texts.len()] } else { op.kinds.to_vec() };
        let mut args = vec![];
        let mut parse_error = None;
        for (k, t) in kinds.iter().zip(&texts) {
            match parse_kind(k, t) {
                Ok(v) => args.push(v),
                Err(e) => parse_error = Some(format!("{k} {t:?}: {e}")),
            }
        }
        let started = std::time::Instant::now();
        let got = match parse_error {
            Some(e) => Err(format!("could not read the input: {e}")),
            None => op.run_values(&args),
        };
        let spent = started.elapsed().as_secs_f64();
        match o.seconds.iter_mut().find(|(k, _)| k == key) {
            Some(slot) => slot.1 += spent,
            None => o.seconds.push((key.to_string(), spent)),
        }
        let ok = if want == "ERR" {
            got.is_err()
        } else {
            let expected = parse_json_value(want).unwrap_or_else(|e| panic!("bad answer {want:?}: {e}"));
            match &got {
                Ok(v) if ORDER_FREE.contains(&key) => values_match(&as_set(v), &as_set(&expected)),
                Ok(v) => values_match(v, &expected),
                Err(_) => has_complex(&expected),
            }
        };
        if ok {
            o.passed += 1;
        } else {
            o.failures.push(format!("{key} {texts:?}\n      Python: {want}\n      Rust:   {got:?}"));
        }
    }
    o
}

#[test]
fn typed_inputs_match_python() {
    let o = run();
    println!("values: {} passed, {} wrong, {} for operators not ported yet", o.passed, o.failures.len(), o.skipped);
    let mut slow = o.seconds.clone();
    slow.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
    for (k, t) in slow.iter().take(8) {
        println!("  slowest: {k} {t:.2}s");
    }
    let shown: Vec<_> = o.failures.iter().take(60).cloned().collect();
    assert!(
        o.failures.is_empty(),
        "{} case(s) differ from Python (first {}):\n{}",
        o.failures.len(),
        shown.len(),
        shown.join("\n")
    );
}

#[test]
fn value_coverage_does_not_shrink() {
    let o = run();
    assert!(o.passed >= MIN_PASSING, "only {} cases pass, expected at least {}", o.passed, MIN_PASSING);
}
