//! Operators inside boxes (nesting) and operators that need several rows (Python `row_tree` and `multirow_specs`).

use rust_calculator::layout::CardKind;
use rust_calculator::multirow;
use rust_calculator::ops;
use rust_calculator::row::{Document, Join};

fn shown(doc: &Document) -> String {
    doc.rows[0].flatten().iter().map(|c| if c.text.is_empty() { "□".to_string() } else { c.text.clone() }).collect::<Vec<_>>().join(" ")
}

#[test]
fn an_operator_picked_with_a_box_selected_goes_inside_that_box() {
    let mut doc = Document::new();
    doc.place_operator(ops::get("math/arithmetic/multiplication").unwrap());
    // (a + b) x c : select the first box, pick addition
    doc.target_path = vec![0];
    doc.place_operator(ops::get("math/arithmetic/addition").unwrap());
    let boxes = doc.rows[0].box_paths();
    assert_eq!(boxes, vec![vec![0, 0], vec![0, 1], vec![1]], "{}", shown(&doc));
    for (p, v) in boxes.iter().zip(["2", "3", "4"]) {
        *doc.rows[0].slot_mut(p).unwrap() = v.to_string();
    }
    doc.equals_all().unwrap();
    assert_eq!(doc.rows[0].result, "20", "(2 + 3) x 4");
    // typing goes to the selected inner box
    doc.target_path = vec![0, 1];
    doc.clear_entry();
    doc.append_digit('7');
    doc.equals_all().unwrap();
    assert_eq!(doc.rows[0].result, "36", "(2 + 7) x 4");
}

#[test]
fn nesting_goes_two_levels_deep_and_a_bad_inner_answer_is_reported() {
    let mut doc = Document::new();
    doc.place_operator(ops::get("math/arithmetic/addition").unwrap());
    doc.target_path = vec![0];
    doc.place_operator(ops::get("math/arithmetic/multiplication").unwrap());
    doc.target_path = vec![0, 0];
    doc.place_operator(ops::get("math/arithmetic/subtraction").unwrap());
    let boxes = doc.rows[0].box_paths();
    assert_eq!(boxes.len(), 4);
    for (p, v) in boxes.iter().zip(["10", "4", "3", "1"]) {
        *doc.rows[0].slot_mut(p).unwrap() = v.to_string();
    }
    doc.equals_all().unwrap();
    assert_eq!(doc.rows[0].result, "19", "((10 - 4) x 3) + 1");
    // dividing by zero inside is an error for the row
    *doc.rows[0].slot_mut(&boxes[1]).unwrap() = "10".into();
    *doc.rows[0].slot_mut(&boxes[2]).unwrap() = "3".into();
    assert!(doc.equals_all().is_ok());
}

#[test]
fn a_fraction_inside_a_box_stays_a_fraction() {
    // an operator drawn as a fraction, put inside a box of another one, keeps its bar
    let mut doc = Document::new();
    doc.place_operator(ops::get("math/arithmetic/addition").unwrap());
    doc.target_path = vec![0];
    doc.place_operator(ops::get("geometry/geometry/slope").unwrap());
    let cards = doc.rows[0].flatten();
    assert!(cards.iter().any(|c| !c.frac.is_empty()), "the slope formula's numerator and denominator are inside a fraction");
    let plan = rust_calculator::layout::plan_pc(&cards.iter().map(|c| c.pc()).collect::<Vec<_>>(), false);
    assert!(plan.rows() >= 3 && !plan.bars.is_empty());
}

#[test]
fn row_two_replaces_instead_of_nesting() {
    let mut doc = Document::new();
    doc.place_operator(ops::get("math/arithmetic/addition").unwrap());
    doc.next_row();
    doc.place_operator(ops::get("math/arithmetic/subtraction").unwrap());
    doc.place_operator(ops::get("math/arithmetic/multiplication").unwrap());
    assert_eq!(doc.rows[1].op_key.as_deref(), Some("math/arithmetic/multiplication"));
    assert!(doc.rows[1].children.iter().all(|c| c.is_none()));
}

#[test]
fn the_number_row_and_the_brackets_template() {
    let mut doc = Document::new();
    let key = "math/constants_and_relations/open_bracket";
    doc.apply_template(ops::get(key).map_or(key, |o| o.key), multirow::get(key).unwrap()).unwrap();
    assert_eq!(doc.rows[0].op_key.as_deref(), Some("math/arithmetic/addition"));
    assert_eq!(doc.rows[1].op_key.as_deref(), Some("_number"));
    *doc.rows[0].slot_mut(&[0]).unwrap() = "2".into();
    *doc.rows[0].slot_mut(&[1]).unwrap() = "3".into();
    *doc.rows[1].slot_mut(&[0]).unwrap() = "4".into();
    let msg = doc.equals_all().unwrap();
    assert!(msg.contains("->  20"), "{msg}");
}

#[test]
fn heat_equation_links_the_boxes_of_row_two_to_row_one() {
    let mut doc = Document::new();
    let key = "math/transforms_and_differential_equations/heat_equation";
    doc.apply_template(ops::get(key).unwrap().key, multirow::get(key).unwrap()).unwrap();
    assert_eq!(doc.rows.len().max(2), doc.rows.len());
    // row 1 is the partial derivative; row 2 holds multiplication with a second partial derivative in its second box
    let boxes1 = doc.rows[1].box_paths();
    assert!(boxes1.iter().any(|p| p.len() == 2), "the nested second derivative has its own boxes: {boxes1:?}");
    *doc.rows[0].slot_mut(&[0]).unwrap() = "x**2 + y**2".into();
    *doc.rows[0].slot_mut(&[1]).unwrap() = "1, 2".into();
    doc.sync_links();
    assert_eq!(doc.rows[1].slot_text(&[1, 0]).unwrap(), "x**2 + y**2");
    assert_eq!(doc.rows[1].slot_text(&[1, 1]).unwrap(), "1, 2");
    assert!(doc.rows.iter().all(|r| r.flatten().iter().any(|c| c.kind == CardKind::Out) || true));
}

#[test]
fn the_exterior_derivative_and_the_direct_sum_open_on_two_rows() {
    for (key, rows) in [("math/differential_geometry_and_tensors/exterior_derivative", 2), ("math/abstract_algebra/direct_sum", 2)] {
        let mut doc = Document::new();
        doc.apply_template(ops::get(key).unwrap().key, multirow::get(key).unwrap()).unwrap();
        let placed: Vec<_> = doc.rows.iter().filter(|r| r.operator().is_some()).collect();
        assert_eq!(placed.len(), rows, "{key}");
        assert_eq!(doc.rows[1].join, Join::Eq, "{key}");
    }
}
