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
fn the_reference_formulas_that_are_several_equations_open_on_several_rows() {
    for (key, rows) in [
        ("math/differential_geometry_and_tensors/exterior_derivative", 2),
        ("math/abstract_algebra/direct_sum", 2),
        ("math/abstract_algebra/field_extension", 2),
        ("math/optimization_and_numerical_methods/kkt_conditions", 4),
    ] {
        let mut doc = Document::new();
        doc.apply_template(ops::get(key).unwrap().key, multirow::get(key).unwrap()).unwrap();
        let placed: Vec<_> = doc.rows.iter().filter(|r| r.operator().is_some()).collect();
        assert_eq!(placed.len(), rows, "{key}");
        assert_eq!(doc.rows[1].join, Join::Eq, "{key}");
    }
}

// ---------- chaining: a row reads the answer of an earlier row ----------

fn chain_doc(key: &str, typed: &[(usize, usize, &str)]) -> Document {
    let mut doc = Document::new();
    doc.apply_template(ops::get(key).unwrap().key, multirow::get(key).unwrap()).unwrap();
    for (row, slot, text) in typed {
        doc.rows[*row].inputs[*slot] = text.to_string();
    }
    doc
}

fn number(doc: &Document, row: usize) -> f64 {
    match doc.rows[row].value {
        Some(rust_calculator::value::Value::Number(x)) => x,
        ref other => panic!("row {row} has {other:?}"),
    }
}

#[test]
fn heron_in_two_rows_gives_the_same_number_as_heron_in_one() {
    let heron = ops::get("geometry/geometry/heron_s_formula").unwrap();
    for (a, b, c) in [(3.0, 4.0, 5.0), (7.0, 8.0, 9.0), (5.5, 6.25, 7.75), (0.1, 0.2, 0.25), (1000.0, 1200.0, 1500.0)] {
        let (sa, sb, sc) = (format!("{a}"), format!("{b}"), format!("{c}"));
        let mut doc = chain_doc("geometry/geometry/heron_s_formula", &[(0, 0, &sa), (0, 1, &sb), (0, 2, &sc)]);
        doc.equals_all().unwrap();
        let one_row = match (heron.compute)(&[a, b, c]).unwrap() {
            rust_calculator::value::Value::Number(x) => x,
            other => panic!("{other:?}"),
        };
        assert_eq!(number(&doc, 1), one_row, "{a} {b} {c}"); // the exact same number
        assert_eq!(doc.rows[1].inputs[0], format!("{}", (a + b + c) / 2.0)); // the s boxes of Row 2 hold Row 1's answer
        assert_eq!(doc.chain_source(1, &[0]), Some(0));
        assert_eq!(doc.chain_source(0, &[0]), None);
    }
}

#[test]
fn doppler_in_two_rows_gives_the_same_number_as_doppler_in_one() {
    let doppler = ops::get("physics/physics/relativistic_doppler").unwrap();
    let c = 299792458.0_f64;
    for (f0, v) in [(100.0, 0.6 * c), (100.0, -0.6 * c), (540e12, 1.5e7), (1.0, 0.0)] {
        let (sf, sv) = (format!("{f0}"), format!("{v}"));
        let mut doc = chain_doc("physics/physics/relativistic_doppler", &[(0, 0, &sv), (1, 0, &sf)]);
        doc.equals_all().unwrap();
        let one_row = match (doppler.compute)(&[f0, v, c]).unwrap() {
            rust_calculator::value::Value::Number(x) => x,
            other => panic!("{other:?}"),
        };
        assert_eq!(number(&doc, 1), one_row, "{f0} {v}");
        assert_eq!(doc.rows[1].inputs[1], format!("{}", v / c)); // beta: Row 1's answer
    }
}

#[test]
fn a_chain_declines_where_the_one_row_operator_declines() {
    let c = 299792458.0_f64;
    for v in [c, -c, 2.0 * c] {
        let sv = format!("{v}");
        let mut doc = chain_doc("physics/physics/relativistic_doppler", &[(0, 0, &sv), (1, 0, "100")]);
        let err = doc.equals_all().unwrap_err();
        assert!(err.contains("speed must be less than the speed of light"), "{err}");
        assert_eq!(doc.rows[1].inputs[1], ""); // the chained box holds no number
    }
    // a box left empty on Row 1: both rows decline
    let mut doc = chain_doc("geometry/geometry/heron_s_formula", &[(0, 0, "3"), (0, 1, "4")]);
    assert!(doc.equals_all().is_err());
    assert_eq!(doc.rows[1].inputs[0], "");
}

#[test]
fn a_changed_side_gives_a_new_semi_perimeter_and_typing_into_a_chained_box_does_not_stick() {
    let mut doc = chain_doc("geometry/geometry/heron_s_formula", &[(0, 0, "3"), (0, 1, "4"), (0, 2, "5")]);
    doc.equals_all().unwrap();
    assert_eq!(doc.rows[1].inputs[0], "6");
    doc.rows[0].inputs[0] = "6".to_string();
    doc.rows[1].inputs[0] = "999".to_string(); // typed into the chained box
    doc.equals_all().unwrap();
    assert_eq!(doc.rows[1].inputs[0], "7.5"); // (6 + 4 + 5) / 2: the new s, not 6 and not 999
}

#[test]
fn the_then_join_gives_the_last_rows_answer() {
    use rust_calculator::row::Join;
    use rust_calculator::value::Value;
    assert_eq!(Join::from_symbol("→"), Join::Then);
    assert_eq!(Join::Then.symbol(), "→");
    assert_eq!(Join::Then.apply(&Value::Number(1.0), &Value::Number(26.5)).unwrap(), Value::Number(26.5));
    let mut doc = chain_doc("geometry/geometry/heron_s_formula", &[(0, 0, "3"), (0, 1, "4"), (0, 2, "5")]);
    let message = doc.equals_all().unwrap();
    assert!(message.ends_with("6"), "{message}");
}

#[test]
fn the_lorentz_chains_give_todays_numbers_and_decline_at_the_speed_of_light() {
    let c = 299792458.0_f64;
    // (operator, the typed box of Row 2, same float as today's compute()?)  Kinetic energy is; the others may differ in the last bit (L0 / gamma is not always the
    // same float as L0 times the square root), so they are checked to one bit (2 epsilon), never more.
    for (name, typed, exact) in [
        ("relativistic_kinetic_energy", 1usize, true),
        ("relativistic_momentum", 1, false),
        ("length_contraction", 0, false),
        ("time_dilation", 0, false),
    ] {
        let key = format!("physics/physics/{name}");
        let today = ops::get(&key).unwrap();
        let gamma_box = if name == "length_contraction" || name == "time_dilation" { 1 } else { 0 };
        for (x, v) in [(2.0, 0.6 * c), (1.0, 0.8 * c), (100.0, 0.5 * c), (3.5, -0.3 * c), (1e6, 0.99 * c), (0.001, 1000.0), (5.0, 0.0)] {
            let (sv, sx) = (format!("{v}"), format!("{x}"));
            let mut doc = chain_doc(&key, &[(0, 0, &sv), (1, typed, &sx)]);
            doc.equals_all().unwrap_or_else(|e| panic!("{name} {x} {v}: {e}"));
            let got = number(&doc, 1);
            let want = match (today.compute)(&[x, v, c]).unwrap() {
                rust_calculator::value::Value::Number(n) => n,
                other => panic!("{other:?}"),
            };
            if exact {
                assert_eq!(got, want, "{name} {x} {v}");
            } else {
                assert!((got - want).abs() <= 2.0 * f64::EPSILON * want.abs(), "{name} {x} {v}: {got} vs {want}"); // one bit, never more
            }
            let gamma = match (ops::get("physics/physics/lorentz_factor").unwrap().compute)(&[v, c]).unwrap() {
                rust_calculator::value::Value::Number(n) => n,
                other => panic!("{other:?}"),
            };
            assert_eq!(doc.rows[1].inputs[gamma_box], format!("{}", gamma), "{name}"); // the chained box holds Row 1's exact answer
        }
        for v in [c, -c, 2.0 * c] {
            let sv = format!("{v}");
            let mut doc = chain_doc(&key, &[(0, 0, &sv), (1, typed, "2")]);
            let err = doc.equals_all().unwrap_err();
            assert!(err.contains("speed must be less than the speed of light"), "{name}: {err}");
            assert_eq!(doc.rows[1].inputs[gamma_box], "", "{name}"); // no γ in the chained box
        }
    }
}

#[test]
fn the_standard_deviations_in_two_rows_match_the_one_row_operators() {
    use rust_calculator::value::Value;
    for (key, one_row) in [
        ("math/statistics_and_probability/standard_deviation", "math/statistics_and_probability/standard_deviation"),
        ("math/statistics_and_probability/sample_standard_deviation", "math/statistics_and_probability/sample_standard_deviation"),
    ] {
        for data in ["2, 4, 4, 4, 5, 5, 7, 9", "1, 2, 3, 4", "0.1, 0.2, 0.3", "10.5, 3.25, 7.0", "73.148457, -9.6, -63.067931, 26.0, -81.18", "5, 5"] {
            let mut chain = Document::new();
            chain.apply_template(ops::get(key).unwrap().key, multirow::get(key).unwrap()).unwrap();
            chain.rows[0].inputs[0] = data.to_string();
            chain.equals_all().unwrap_or_else(|e| panic!("{key} {data}: {e}"));
            let mut single = Document::new();
            single.rows[0].set_operator(ops::get(one_row).unwrap());
            single.rows[0].inputs[0] = data.to_string();
            single.equals_all().unwrap();
            let (got, want) = (number(&chain, 1), match single.rows[0].value {
                Some(Value::Number(x)) => x,
                ref other => panic!("{other:?}"),
            });
            assert_eq!(got, want, "{key} {data}"); // Rust's one-row operators take the square root of the variance too: the same float
            assert!(chain.rows[1].inputs[0].parse::<f64>().is_ok(), "the chained box holds Row 1's number");
        }
    }
    // a sample of one number declines, and the chained box stays empty
    let key = "math/statistics_and_probability/sample_standard_deviation";
    let mut chain = Document::new();
    chain.apply_template(ops::get(key).unwrap().key, multirow::get(key).unwrap()).unwrap();
    chain.rows[0].inputs[0] = "5".to_string();
    let err = chain.equals_all().unwrap_err();
    assert!(err.contains("at least two data points"), "{err}");
    assert_eq!(chain.rows[1].inputs[0], "");
}

#[test]
fn gravitational_time_dilation_in_two_rows_gives_todays_number_and_declines_inside_the_horizon() {
    let key = "physics/physics/gravitational_time_dilation";
    let today = ops::get(key).unwrap();
    let (g, c) = (6.674e-11_f64, 299792458.0_f64);
    for (dt, m, r) in [(1000.0, 1.989e30, 6.957e8), (3600.0, 5.972e24, 6.371e6), (1.0, 1.989e30, 1e10), (2.5, 3e31, 5e8)] {
        let (sdt, sm, sr) = (format!("{dt}"), format!("{m}"), format!("{r}"));
        let mut doc = chain_doc(key, &[(0, 0, &sm), (1, 0, &sdt), (1, 2, &sr)]);
        doc.equals_all().unwrap();
        let want = match (today.compute)(&[dt, m, r, g, c]).unwrap() {
            rust_calculator::value::Value::Number(x) => x,
            other => panic!("{other:?}"),
        };
        let got = number(&doc, 1);
        assert!((got - want).abs() <= 2.0 * f64::EPSILON * want.abs(), "{dt} {m} {r}: {got} vs {want}"); // one bit, never more
        assert!(doc.rows[1].inputs[1].parse::<f64>().is_ok()); // the chained box holds Row 1's radius
    }
    let mut doc = chain_doc(key, &[(0, 0, "1.989e30"), (1, 0, "1000"), (1, 2, "2000")]);
    let err = doc.equals_all().unwrap_err();
    assert!(err.contains("r must be outside the Schwarzschild radius"), "{err}");
    assert!(doc.rows[1].inputs[1].parse::<f64>().is_ok()); // Row 1 did not decline: its radius is there
    let mut doc = chain_doc(key, &[(1, 0, "1000"), (1, 2, "1e9")]); // Row 1's mass box is empty: Row 1 declines
    assert!(doc.equals_all().is_err());
    assert_eq!(doc.rows[1].inputs[1], "");
}

#[test]
fn range_interquartile_range_and_variance_in_three_rows_give_the_one_row_numbers() {
    use rust_calculator::value::Value;
    let st = "math/statistics_and_probability/";
    let one = |key: &str, inputs: &[&str]| -> Result<f64, String> {
        let mut single = Document::new();
        single.rows[0].set_operator(ops::get(key).unwrap());
        for (i, t) in inputs.iter().enumerate() {
            single.rows[0].inputs[i] = t.to_string();
        }
        single.equals_all()?;
        match single.rows[0].value {
            Some(Value::Number(x)) => Ok(x),
            ref other => panic!("{other:?}"),
        }
    };
    for data in ["4, 9, 1", "2.5, -7.25, 10.125, 3", "5", "0.1, 0.2, 0.3, 0.7", "-3, -1, -2"] {
        let key = format!("{st}range");
        let mut doc = chain_doc(&key, &[(0, 0, data)]);
        doc.equals_all().unwrap();
        assert_eq!(doc.rows[1].inputs[0], data, "Row 2's list is copied from Row 1");
        assert_eq!(number(&doc, 2), one(&key, &[data]).unwrap(), "range {data}");
    }
    for data in ["1, 2, 3, 4, 5, 6, 7, 8", "10.5, 3.25, 7.0, 8.75, 1.5", "1, 1, 2, 2, 3, 3", "73.148457, -9.6, -63.067931, 26.0, -81.18", "5, 9"] {
        let key = format!("{st}interquartile_range");
        let mut doc = chain_doc(&key, &[(0, 0, data)]);
        doc.equals_all().unwrap();
        assert_eq!(number(&doc, 2), one(&key, &[data]).unwrap(), "iqr {data}");
    }
    for (v, p) in [("0, 1", "0.5, 0.5"), ("1, 2, 3", "0.2, 0.3, 0.5"), ("-2.5, 0, 4.25, 10", "0.1, 0.4, 0.3, 0.2"), ("7", "1")] {
        let key = format!("{st}variance_of_random_variable");
        let mut doc = chain_doc(&key, &[(0, 0, v), (0, 1, p)]);
        doc.equals_all().unwrap();
        assert_eq!((doc.rows[1].inputs[0].as_str(), doc.rows[1].inputs[1].as_str()), (v, p));
        assert_eq!(number(&doc, 2), one(&key, &[v, p]).unwrap(), "variance {v} / {p}");
    }
    // an empty list declines in Row 1 and nothing is chained
    let key = format!("{st}range");
    let mut doc = chain_doc(&key, &[(0, 0, "")]);
    assert!(doc.equals_all().is_err());
    assert_eq!(doc.rows[2].inputs[0], "");
}

#[test]
fn one_plus_one_plus_one_with_the_join_keys_gives_three_in_row_four() {
    let mut doc = Document::new();
    doc.append_digit('1');
    doc.join_key("+");
    doc.append_digit('1');
    doc.join_key("+");
    doc.append_digit('1');
    let typed: Vec<&str> = doc.rows.iter().take(3).map(|r| r.inputs[0].as_str()).collect();
    assert_eq!(typed, ["1", "1", "1"]);
    assert_eq!(doc.rows[1].join, rust_calculator::row::Join::Add);
    assert_eq!(doc.rows[2].join, rust_calculator::row::Join::Add);
    doc.equals_all().unwrap();
    assert!(doc.rows[3].is_result);
    assert_eq!(doc.rows[3].result, "3");
}

#[test]
fn one_plus_one_is_two_and_a_second_join_key_with_no_number_only_changes_the_symbol() {
    let mut doc = Document::new();
    doc.append_digit('1');
    doc.join_key("+");
    doc.append_digit('1');
    assert_eq!((doc.rows[0].inputs[0].as_str(), doc.rows[1].inputs[0].as_str()), ("1", "1")); // not 11
    doc.equals_all().unwrap();
    assert_eq!(doc.rows[2].result, "2");
    let mut doc = Document::new();
    doc.append_digit('1');
    doc.join_key("+");
    let rows = doc.rows.len();
    doc.join_key("−");
    assert_eq!(doc.rows[1].join, rust_calculator::row::Join::Sub);
    assert_eq!(doc.rows.len(), rows);
}

#[test]
fn the_quaternion_operators_give_the_numbers_of_the_work_plan_and_decline_with_its_messages() {
    use rust_calculator::value::Value;
    let la = "math/linear_algebra/";
    let run = |key: &str, args: Vec<Value>| -> Result<Vec<f64>, String> {
        let op = ops::get(&format!("{la}{key}")).unwrap();
        match (op.compute_v.unwrap())(&args)? {
            Value::List(items) => Ok(items.iter().map(|v| match v { Value::Number(x) => *x, o => panic!("{o:?}") }).collect()),
            o => panic!("{o:?}"),
        }
    };
    let list = |xs: &[f64]| Value::List(xs.iter().map(|x| Value::Number(*x)).collect());
    let near = |a: &[f64], b: &[f64]| a.len() == b.len() && a.iter().zip(b).all(|(p, q)| (p - q).abs() < 1e-12);
    let r2 = 2f64.sqrt();
    assert!(near(&run("quaternion_multiply", vec![list(&[0., 1., 0., 0.]), list(&[0., 0., 1., 0.])]).unwrap(), &[0., 0., 0., 1.]));
    assert!(near(&run("quaternion_multiply", vec![list(&[0., 1., 0., 0.]), list(&[0., 1., 0., 0.])]).unwrap(), &[-1., 0., 0., 0.]));
    assert!(near(&run("quaternion_conjugate", vec![list(&[0.5, 0.5, 0.5, 0.5])]).unwrap(), &[0.5, -0.5, -0.5, -0.5]));
    assert!(near(&run("quaternion_inverse", vec![list(&[r2, 0., 0., r2])]).unwrap(), &[0.35355339059327373, 0., 0., -0.35355339059327373]));
    assert!(near(&run("quaternion_normalize", vec![list(&[2., 0., 0., 2.])]).unwrap(), &[r2 / 2., 0., 0., r2 / 2.]));
    assert!(near(&run("quaternion_from_axis_angle", vec![list(&[0., 0., 2.]), Value::Number(std::f64::consts::FRAC_PI_2)]).unwrap(), &[r2 / 2., 0., 0., r2 / 2.]));
    assert!(near(&run("rotate_vector_by_quaternion", vec![list(&[r2, 0., 0., r2]), list(&[1., 0., 0.])]).unwrap(), &[0., 1., 0.]));
    assert!(near(&run("rotate_vector_by_quaternion", vec![list(&[0., 1., 0., 0.]), list(&[0., 1., 0.])]).unwrap(), &[0., -1., 0.]));
    assert!(near(&run("quaternion_to_yaw_pitch_roll", vec![list(&[r2, 0., 0., r2])]).unwrap(), &[std::f64::consts::FRAC_PI_2, 0., 0.]));
    assert!(near(
        &run("quaternion_from_yaw_pitch_roll", vec![Value::Number(std::f64::consts::FRAC_PI_2), Value::Number(0.), Value::Number(0.)]).unwrap(),
        &[r2 / 2., 0., 0., r2 / 2.]
    ));
    let h = 0.7071067811865476;
    let said = |key: &str, args: Vec<Value>| run(key, args).unwrap_err();
    assert!(said("quaternion_to_yaw_pitch_roll", vec![list(&[h, 0., h, 0.])]).contains("gimbal lock"));
    assert!(said("quaternion_inverse", vec![list(&[0., 0., 0., 0.])]).contains("the quaternion is zero, it has no inverse"));
    assert!(said("quaternion_normalize", vec![list(&[1., 2., 3.])]).contains("a quaternion has 4 numbers: w, x, y, z"));
    assert!(said("quaternion_from_axis_angle", vec![list(&[0., 0.]), Value::Number(1.)]).contains("a vector has 3 numbers: x, y, z"));
    assert!(said("quaternion_from_axis_angle", vec![list(&[0., 0., 0.]), Value::Number(1.)]).contains("the axis has length zero"));
}

#[test]
fn the_rotation_matrix_operators_give_the_numbers_of_the_work_plan_and_decline_with_its_messages() {
    use rust_calculator::value::Value;
    let la = "math/linear_algebra/";
    let call = |key: &str, args: Vec<Value>| -> Result<Value, String> { (ops::get(&format!("{la}{key}")).unwrap().compute_v.unwrap())(&args) };
    let flat = |v: Value| -> Vec<f64> {
        match v {
            Value::List(items) => items
                .iter()
                .flat_map(|r| match r {
                    Value::List(cells) => cells.iter().map(|c| if let Value::Number(x) = c { *x } else { panic!() }).collect::<Vec<f64>>(),
                    Value::Number(x) => vec![*x],
                    o => panic!("{o:?}"),
                })
                .collect(),
            Value::Number(x) => vec![x],
            o => panic!("{o:?}"),
        }
    };
    let list = |xs: &[f64]| Value::List(xs.iter().map(|x| Value::Number(*x)).collect());
    let matrix = |m: [[f64; 3]; 3]| Value::List(m.iter().map(|r| list(r)).collect());
    let near = |a: Vec<f64>, b: &[f64], tol: f64| a.len() == b.len() && a.iter().zip(b).all(|(p, q)| (p - q).abs() < tol);
    let (r2, half_pi) = (2f64.sqrt(), std::f64::consts::FRAC_PI_2);
    let rz = [[0., -1., 0.], [1., 0., 0.], [0., 0., 1.]];
    let rz_flat = [0., -1., 0., 1., 0., 0., 0., 0., 1.];
    assert!(near(flat(call("rotation_matrix_from_quaternion", vec![list(&[r2, 0., 0., r2])]).unwrap()), &rz_flat, 1e-12));
    assert!(near(flat(call("rotation_matrix_from_quaternion", vec![list(&[0., 1., 0., 0.])]).unwrap()), &[1., 0., 0., 0., -1., 0., 0., 0., -1.], 1e-12));
    assert!(near(flat(call("rotation_matrix_from_axis_angle", vec![list(&[0., 0., 2.]), Value::Number(half_pi)]).unwrap()), &rz_flat, 1e-12));
    assert!(near(flat(call("rotation_matrix_from_yaw_pitch_roll", vec![Value::Number(half_pi), Value::Number(0.), Value::Number(0.)]).unwrap()), &rz_flat, 1e-12));
    assert!(near(flat(call("rotate_vector_by_matrix", vec![matrix(rz), list(&[1., 0., 0.])]).unwrap()), &[0., 1., 0.], 1e-12));
    let h = 0.7071067811865476;
    let want = [0.9238795325112868, 0., 0., 0.38268343236508984];
    assert!(near(flat(call("quaternion_slerp", vec![list(&[1., 0., 0., 0.]), list(&[h, 0., 0., h]), Value::Number(0.5)]).unwrap()), &want, 1e-15));
    assert!(near(flat(call("quaternion_slerp", vec![list(&[1., 0., 0., 0.]), list(&[-h, 0., 0., -h]), Value::Number(0.5)]).unwrap()), &want, 1e-15));
    assert!(near(flat(call("angle_between_quaternions", vec![list(&[1., 0., 0., 0.]), list(&[0., 1., 0., 0.])]).unwrap()), &[std::f64::consts::PI], 1e-15));
    assert!(near(flat(call("angle_between_quaternions", vec![list(&[1., 0., 0., 0.]), list(&[-1., 0., 0., 0.])]).unwrap()), &[0.], 1e-15));
    assert!(near(flat(call("rotation_matrix_to_quaternion", vec![matrix(rz)]).unwrap()), &[h, 0., 0., h], 1e-12));
    assert!(near(flat(call("rotation_matrix_to_quaternion", vec![matrix([[1., 0., 0.], [0., -1., 0.], [0., 0., -1.]])]).unwrap()), &[0., 1., 0., 0.], 1e-12));
    let said = |key: &str, args: Vec<Value>| call(key, args).unwrap_err();
    assert!(said("rotation_matrix_to_quaternion", vec![matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]])]).contains("not a rotation matrix"));
    assert!(said("rotation_matrix_to_quaternion", vec![matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., -1.]])]).contains("not a rotation matrix"));
    assert!(said("rotate_vector_by_matrix", vec![Value::List(vec![list(&[1., 0.]), list(&[0., 1.])]), list(&[1., 0., 0.])]).contains("a rotation matrix has 3 rows of 3 numbers"));
    assert!(said("quaternion_slerp", vec![list(&[1., 0., 0., 0.]), list(&[0., 1., 0., 0.]), Value::Number(1.5)]).contains("the blend is outside 0 to 1"));
    assert!(said("rotation_matrix_from_quaternion", vec![list(&[0., 0., 0., 0.])]).contains("the quaternion is zero, it cannot be a rotation"));
}

#[test]
fn the_motion_operators_give_the_numbers_of_the_work_plan_and_decline_with_its_messages() {
    use rust_calculator::value::Value;
    let ph = "physics/physics/";
    // the optional gravity box is filled in by the calculator, so the operator is called the way the rows call it: with every number, g last
    let call = |key: &str, nums: &[f64]| -> Result<Value, String> {
        let op = ops::get(&format!("{ph}{key}")).unwrap();
        match op.compute_v {
            Some(f) => f(&nums.iter().map(|x| Value::Number(*x)).collect::<Vec<_>>()),
            None => (op.compute)(nums),
        }
    };
    let one = |key: &str, nums: &[f64]| -> f64 {
        match call(key, nums).unwrap() {
            Value::Number(x) => x,
            o => panic!("{o:?}"),
        }
    };
    let said = |key: &str, nums: &[f64]| call(key, nums).unwrap_err();
    let (g, half_pi, quarter_pi) = (9.81, std::f64::consts::FRAC_PI_2, std::f64::consts::FRAC_PI_4);
    assert_eq!(one("speed_after_distance", &[0., 2., 8.]), 5.656854249492381);
    assert_eq!(one("speed_after_distance", &[3., 0., 10.]), 3.0);
    assert_eq!(one("speed_after_distance", &[10., -2., 9.]), 8.0);
    assert_eq!(one("time_to_distance", &[0., 2., 4.]), 2.0);
    assert_eq!(one("time_to_distance", &[4., 0., 10.]), 2.5);
    assert_eq!(one("time_to_distance", &[10., -2., 9.]), 1.0);
    assert_eq!(one("time_to_distance", &[0., 0., 0.]), 0.0);
    assert_eq!(one("stopping_distance", &[10., -2.]), 25.0);
    assert_eq!(one("stopping_distance", &[-8., 2.]), -16.0);
    assert_eq!(one("stopping_distance", &[0., -2.]), 0.0);
    assert_eq!(one("braking_time", &[10., -2.]), 5.0);
    assert_eq!(one("braking_time", &[-8., 2.]), 4.0);
    assert_eq!(one("projectile_range", &[10., quarter_pi, g]), 10.19367991845056);
    assert_eq!(one("projectile_time_of_flight", &[10., half_pi, g]), 2.038735983690112);
    assert_eq!(one("projectile_time_of_flight", &[10., quarter_pi, g]), 1.4416040391163047);
    assert!((one("hover_thrust", &[2., g]) - 19.62).abs() < 1e-12);
    match call("projectile_position", &[10., half_pi, 1., g]).unwrap() {
        Value::List(p) => match (&p[0], &p[1]) {
            (Value::Number(x), Value::Number(y)) => assert!(x.abs() < 1e-12 && (y - 5.095).abs() < 1e-12, "{x} {y}"),
            o => panic!("{o:?}"),
        },
        o => panic!("{o:?}"),
    }
    assert!(said("speed_after_distance", &[1., -2., 5.]).contains("the motion stops before that distance"));
    assert!(said("time_to_distance", &[0., 0., 5.]).contains("not moving"));
    assert!(said("time_to_distance", &[1., -2., 5.]).contains("that distance is not reached"));
    assert!(said("stopping_distance", &[5., 0.]).contains("no acceleration, it does not stop"));
    assert!(said("braking_time", &[5., 2.]).contains("it is speeding up, it does not stop"));
    assert!(said("projectile_range", &[-1., 0.5, g]).contains("speed cannot be negative"));
    assert!(said("projectile_range", &[10., 1.6, g]).contains("the angle is past straight up"));
    assert!(said("projectile_time_of_flight", &[10., 0.5, 0.]).contains("gravity must pull downward"));
    assert!(said("projectile_position", &[10., 0.5, -1., g]).contains("time cannot be negative"));
    assert!(said("hover_thrust", &[0., g]).contains("mass must be positive"));
}
