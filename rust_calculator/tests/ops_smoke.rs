use rust_calculator::ops;
use rust_calculator::value::Value;

#[test]
fn addition() {
    let op = ops::get("math/arithmetic/addition").unwrap();
    assert_eq!(op.run(&[2.0, 3.0]).unwrap(), Value::Number(5.0));
}

#[test]
fn division_by_zero() {
    let op = ops::get("math/arithmetic/division").unwrap();
    assert!(op.run(&[1.0, 0.0]).is_err());
}

#[test]
fn quadratic() {
    let op = ops::get("math/algebra/quadratic_formula").unwrap();
    match op.run(&[1.0, -3.0, 2.0]).unwrap() {
        Value::Pair(a, b) => {
            assert!((a - 2.0).abs() < 1e-9 || (a - 1.0).abs() < 1e-9);
            assert!((b - 2.0).abs() < 1e-9 || (b - 1.0).abs() < 1e-9);
        }
        other => panic!("expected pair, got {other:?}"),
    }
}

#[test]
fn time_dilation_sixty_percent_c() {
    let op = ops::get("physics/physics/time_dilation").unwrap();
    let v = 0.6 * 299_792_458.0;
    let out = op.run(&[1.0, v]).unwrap();
    let n = out.as_number().unwrap();
    assert!((n - 1.25).abs() < 1e-9, "got {n}");
}

#[test]
fn library_has_core_coverage() {
    let n = ops::all_operators().len();
    assert!(n >= 60, "expected a solid phase-1 set, got {n}");
    assert!(ops::get("math/arithmetic/addition").is_some());
    assert!(ops::get("math/trigonometry/sine").is_some());
    assert!(ops::get("geometry/geometry/pythagorean_theorem").is_some());
    assert!(ops::get("physics/physics/ohm_s_law").is_some());
    assert!(ops::get("math/constants_and_relations/euler_s_number").is_some());
    assert!(ops::get("math/discrete_and_number_theory/greatest_common_divisor").is_some());
}

#[test]
fn minimum_three_boxes() {
    let op = ops::get("math/arithmetic/minimum").unwrap();
    assert_eq!(op.arity(), 3);
    assert_eq!(op.run(&[3.0, 1.0, 2.0]).unwrap(), Value::Number(1.0));
}

/// Boxes take typed text like the Python Advanced Input window: lists, matrices, functions, sets, graphs.
#[test]
fn row_accepts_typed_values() {
    use rust_calculator::row::Row;
    let try_row = |key: &str, boxes: &[&str]| {
        let mut row = Row::blank();
        row.set_operator(ops::get(key).unwrap());
        row.inputs = boxes.iter().map(|s| s.to_string()).collect();
        row.compute();
        assert!(row.error.is_none(), "{key}: {:?}", row.error);
        row.result
    };
    assert_eq!(try_row("math/statistics_and_probability/mean", &["1, 2, 3, 4"]), "2.5");
    assert_eq!(try_row("math/linear_algebra/determinant", &["1 2; 3 4"]), "-2");
    assert_eq!(try_row("math/linear_algebra/matrix_multiply", &["1 2; 3 4", "0 1; 1 0"]), "[[2, 1], [4, 3]]");
    assert_eq!(try_row("math/logic_and_sets/union", &["1, 2", "2, 3"]), "{1, 2, 3}");
    assert_eq!(try_row("math/algebra/expand", &["(x+1)(x-1)"]), "x² - 1");
    assert_eq!(try_row("math/graph_theory_and_combinatorics/vertex_degree", &["A: B, C; B: C; C: A", "A"]), "2");
    let d = try_row("math/calculus/definite_integral", &["x**2", "0", "3"]);
    assert!((d.parse::<f64>().unwrap() - 9.0).abs() < 1e-9, "{d}");
}

#[test]
fn every_ready_operator_has_a_calculation() {
    use rust_calculator::operator::CalcKind;
    let ready = ops::all_operators().iter().filter(|o| o.calc == CalcKind::Ready).count();
    assert_eq!(ready, 473, "the Python library has 473 Ready operators");
    assert_eq!(ops::all_operators().len(), 545);
}
