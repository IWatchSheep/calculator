//! The row rules of the design (same as the Python program's README):
//!   - the answer of a row stays on that row, to the right of its `=`;
//!   - Next Row goes from Row 1 to Row 2 (the lines of one operator's math are not rows);
//!   - Row 2 is joined to Row 1 by a math sign, each row keeps its own answer, and the answer for both is on Row 3.

use rust_calculator::layout::{self, CardKind};
use rust_calculator::ops;
use rust_calculator::row::{Document, Join, Row};
use rust_calculator::value::Value;

fn fill(row: &mut Row, key: &str, inputs: &[&str]) {
    let op = ops::get(key).unwrap();
    row.set_operator(op);
    for (i, t) in inputs.iter().enumerate() {
        row.inputs[i] = t.to_string();
    }
}

#[test]
fn a_single_row_keeps_its_answer_on_its_own_row() {
    let mut doc = Document::new();
    fill(&mut doc.rows[0], "physics/physics/gravitation", &["5", "2", "3"]);
    let msg = doc.equals_all().unwrap();
    assert!(msg.starts_with("Row 1 ="), "{msg}");
    assert_eq!(doc.rows[0].result, "7.415555556e-11"); // shown like the Python program
    assert!(!doc.rows.iter().any(|r| r.is_result), "nothing is printed into another row");
    assert_eq!(doc.rows.len(), 2);
    // the answer box inside the formula (the F of F = G m1 m2 / r^2) shows the same answer
    assert_eq!(doc.rows[0].outs.len(), 1);
    assert_eq!(doc.rows[0].outs[0], doc.rows[0].result);
}

#[test]
fn next_row_goes_from_row_1_to_row_2() {
    let mut doc = Document::new();
    fill(&mut doc.rows[0], "physics/physics/gravitation", &["5", "2", "3"]); // a formula drawn on several lines is still only Row 1
    assert_eq!(doc.target_row, 0);
    doc.next_row();
    assert_eq!(doc.target_row, 1);
    assert_eq!(doc.rows.len(), 2);
}

#[test]
fn row_2_joins_to_row_1_and_the_answer_for_both_is_on_row_3() {
    let mut doc = Document::new();
    fill(&mut doc.rows[0], "math/arithmetic/addition", &["1", "2"]);
    fill(&mut doc.rows[1], "math/arithmetic/multiplication", &["3", "4"]);
    doc.rows[1].join = Join::Add;
    let msg = doc.equals_all().unwrap();
    assert!(msg.contains("Row 3"), "{msg}");
    assert_eq!(doc.rows[0].result, "3"); // each row keeps its own answer
    assert_eq!(doc.rows[1].result, "12");
    assert_eq!(doc.rows.len(), 3);
    assert!(doc.rows[2].is_result);
    assert_eq!(doc.rows[2].result, "15"); // 3 + 12
    assert_eq!(doc.rows[2].value, Some(Value::Number(15.0)));
}

#[test]
fn rows_need_a_join_sign_and_lists_cannot_be_joined() {
    let mut doc = Document::new();
    fill(&mut doc.rows[0], "math/arithmetic/addition", &["1", "2"]);
    fill(&mut doc.rows[1], "math/arithmetic/addition", &["3", "4"]);
    assert!(doc.equals_all().unwrap_err().contains("needs a join symbol"));
    doc.rows[1].join = Join::Lt;
    doc.equals_all().unwrap();
    assert_eq!(doc.rows[2].value, Some(Value::Bool(true))); // 3 < 7
    // a list answer is not a number
    assert!(Join::Mul.apply(&Value::List(vec![Value::Number(1.0)]), &Value::Number(2.0)).is_err());
}

#[test]
fn a_formula_with_two_answer_boxes_shows_each_answer() {
    let mut doc = Document::new();
    fill(&mut doc.rows[0], "math/algebra/quadratic_formula", &["1", "-3", "2"]);
    doc.equals_all().unwrap();
    let mut outs = doc.rows[0].outs.clone();
    outs.sort();
    assert_eq!(outs, vec!["1".to_string(), "2".to_string()]);
}

#[test]
fn an_answer_is_forgotten_when_a_number_changes() {
    let mut doc = Document::new();
    fill(&mut doc.rows[0], "math/arithmetic/addition", &["1", "2"]);
    doc.equals_all().unwrap();
    doc.target_row = 0;
    doc.target_path = vec![1];
    doc.append_digit('5');
    assert!(doc.rows[0].result.is_empty());
    assert!(doc.rows[0].outs.is_empty());
}

#[test]
fn the_cone_has_one_input_for_the_two_r_boxes() {
    let l = layout::get("geometry/geometry/cone_surface_area").unwrap();
    let boxes: Vec<i32> = l.cards.iter().filter(|c| c.kind == CardKind::Box).map(|c| c.slot).collect();
    assert_eq!(boxes, vec![0, 0, 1]); // r, r, l
    assert_eq!(l.cards[0].kind, CardKind::Out); // A is the answer box
}
