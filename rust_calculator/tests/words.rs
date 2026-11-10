//! The 377 Ready algebra word problems as rows: each one, filled with its own numbers and computed by the Rust solver, gives what Python's `compute()` gives.

use rust_calculator::layout::{self, CardKind};
use rust_calculator::ops::{self, words};
use rust_calculator::row::Row;
use rust_calculator::value::Value;

fn numbers(v: &Value) -> Vec<f64> {
    match v {
        Value::Number(n) => vec![*n],
        Value::List(items) => items.iter().flat_map(numbers).collect(),
        other => panic!("not a number: {other:?}"),
    }
}

#[test]
fn every_ready_word_problem_gives_the_python_answer() {
    let text = std::fs::read_to_string(concat!(env!("CARGO_MANIFEST_DIR"), "/tests/words_expected.tsv")).unwrap();
    let mut count = 0;
    for line in text.lines().filter(|l| !l.is_empty()) {
        let (key, want) = line.split_once('\t').unwrap();
        let op = ops::get(key).unwrap_or_else(|| panic!("no operator {key}"));
        let mut row = Row::blank();
        row.set_operator(op);
        assert!(row.inputs.iter().all(|s| !s.is_empty()), "{key}: the boxes start with the problem's own numbers");
        row.compute();
        assert!(row.error.is_none(), "{key}: {:?}", row.error);
        let got = numbers(row.value.as_ref().unwrap());
        let want: Vec<f64> = want.split(' ').map(|x| x.parse().unwrap()).collect();
        assert_eq!(got.len(), want.len(), "{key}");
        for (g, w) in got.iter().zip(&want) {
            assert!((g - w).abs() <= 1e-9 * w.abs().max(1.0), "{key}: rust {g} python {w}");
        }
        count += 1;
    }
    assert_eq!(count, 377);
}

#[test]
fn every_ready_word_problem_has_a_row_whose_boxes_are_its_numbers() {
    assert_eq!(rust_calculator::word_layouts::WORD_LAYOUTS.len(), 377);
    assert_eq!(words::items().len(), 1000);
    assert_eq!(words::items().iter().filter(|i| i.ready).count(), 377);
    for l in rust_calculator::word_layouts::WORD_LAYOUTS {
        let op = ops::get(l.key).unwrap_or_else(|| panic!("no operator for {}", l.key));
        for s in 0..op.arity() {
            assert!(l.cards.iter().any(|c| c.kind == CardKind::Box && c.slot == s as i32), "{}: input {} has no box", l.key, s);
        }
        assert!(layout::get(l.key).is_some());
    }
}

#[test]
fn changing_a_box_changes_the_answer() {
    let op = ops::get("word:age/0002").unwrap();
    let mut row = Row::blank();
    row.set_operator(op);
    assert_eq!(row.inputs, vec!["13".to_string(), "85".to_string()]);
    row.compute();
    assert_eq!(numbers(row.value.as_ref().unwrap()), vec![36.0, 49.0]);
    row.inputs = vec!["10".into(), "50".into()];
    row.compute();
    assert_eq!(numbers(row.value.as_ref().unwrap()), vec![20.0, 30.0]);
    row.inputs = vec!["10".into(), "51".into()];
    row.compute();
    assert!(row.error.is_some(), "a count that is not whole is declined, not guessed");
}
