//! Typed math -> a row tree: the same readings and the same complaints as the Python `template_math`.

use rust_calculator::row::Document;
use rust_calculator::template_math::{describe, empty_boxes, parse_math};
use serde_json::Value;

#[test]
fn typed_math_reads_the_same_as_python() {
    let text = std::fs::read_to_string(concat!(env!("CARGO_MANIFEST_DIR"), "/tests/template_cases.json")).unwrap();
    let cases: Vec<Value> = serde_json::from_str(&text).unwrap();
    assert!(cases.len() > 30);
    for c in cases {
        let typed = c["text"].as_str().unwrap();
        match parse_math(typed) {
            Ok(row) => {
                assert!(c["ok"].as_bool().unwrap(), "Rust accepts {typed:?} but Python says {}", c["message"]);
                assert_eq!(describe(&row), c["describe"].as_str().unwrap(), "{typed:?}");
                assert_eq!(empty_boxes(&row) as i64, c["empty"].as_i64().unwrap(), "{typed:?}");
            }
            Err(e) => {
                assert!(!c["ok"].as_bool().unwrap(), "Rust refuses {typed:?} ({e}) but Python accepts it as {}", c["describe"]);
                assert_eq!(e.message, c["message"].as_str().unwrap(), "{typed:?}");
                assert_eq!(e.incomplete, c["incomplete"].as_bool().unwrap(), "{typed:?}");
            }
        }
    }
}

#[test]
fn a_template_can_be_filled_and_calculated() {
    let mut doc = Document::new();
    doc.place_row(parse_math("(x + 3) × 2").unwrap());
    let empty: Vec<Vec<usize>> = doc.rows[0].box_paths().into_iter().filter(|p| doc.rows[0].slot_text(p).map_or(false, |t| t.is_empty())).collect();
    assert_eq!(empty.len(), 1, "one empty box to fill in");
    *doc.rows[0].slot_mut(&empty[0]).unwrap() = "4".into();
    doc.equals_all().unwrap();
    assert_eq!(doc.rows[0].result, "14");
}

#[test]
fn saved_templates_survive_a_restart() {
    let dir = std::env::temp_dir().join(format!("tpl_test_{}", std::process::id()));
    std::fs::create_dir_all(&dir).unwrap();
    let path = dir.join("saved_templates.json");
    assert_eq!(rust_calculator::template_math::load_data(&path), (vec![], false));
    rust_calculator::template_math::save_data(&path, &["(□ + 3) × 2".to_string(), "sqrt(x)".to_string()], true).unwrap();
    assert_eq!(rust_calculator::template_math::load_data(&path), (vec!["(□ + 3) × 2".to_string(), "sqrt(x)".to_string()], true));
    std::fs::remove_dir_all(dir).ok();
}
