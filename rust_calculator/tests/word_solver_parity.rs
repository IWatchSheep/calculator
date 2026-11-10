//! The Rust word solver against Python, problem by problem.
//!
//! `tests/word_corpus.jsonl` (written by `scripts/export_word_corpus.py`) holds every problem text the Python tests use, with what each Python family returned,
//! what `solve()` returned and what the number-puzzle reader returned.  Every family that has been ported must give EXACTLY the same answer, equation and
//! reading as Python on every one of them, and decline exactly where Python declines.

use rust_calculator::word_solver::{self, q::Q};
use serde_json::Value;
use std::collections::HashMap;

fn corpus() -> Vec<Value> {
    let text = std::fs::read_to_string(concat!(env!("CARGO_MANIFEST_DIR"), "/tests/word_corpus.jsonl")).expect("word_corpus.jsonl (run scripts/export_word_corpus.py)");
    text.lines().filter(|l| !l.trim().is_empty()).map(|l| serde_json::from_str(l).unwrap()).collect()
}

fn values_text(v: &[Q]) -> Vec<String> {
    v.iter().map(|x| x.to_string()).collect()
}

fn json_strings(v: &Value) -> Vec<String> {
    v.as_array().unwrap().iter().map(|x| x.as_str().unwrap().to_string()).collect()
}

#[test]
fn every_ported_family_matches_python_on_every_problem() {
    let families = word_solver::families();
    let mut bad: Vec<String> = Vec::new();
    for entry in corpus() {
        let problem = entry["p"].as_str().unwrap();
        // what Python's families returned for this problem: name -> (values, equation, reading)
        let mut expected: HashMap<String, (String, Vec<String>, String, String)> = HashMap::new();
        for f in entry["fam"].as_array().unwrap() {
            let name = f[0].as_str().unwrap().to_string();
            expected.insert(name, (f[1].as_str().unwrap().to_string(), json_strings(&f[2]), f[3].as_str().unwrap().to_string(), f[4].as_str().unwrap().to_string()));
        }
        for (name, fam) in &families {
            let got = word_solver::run_family(*fam, problem);
            // the corpus is keyed by the Python function name; the result also carries a family label (age_sum reports "sum_difference")
            let want = expected.get(*name);
            match (&got, want) {
                (None, None) => {}
                (Some(g), Some(w)) => {
                    let gt = (g.family.to_string(), values_text(&g.values), g.equation.clone(), g.reading.clone());
                    if gt != *w {
                        bad.push(format!("{name} differs on {problem:?}\n   rust: {gt:?}\n   py  : {w:?}"));
                    }
                }
                (Some(g), None) => bad.push(format!("{name} answers {:?} where Python declines: {problem:?}", values_text(&g.values))),
                (None, Some(w)) => bad.push(format!("{name} declines where Python answers {:?}: {problem:?}", w.1)),
            }
        }
    }
    assert!(bad.is_empty(), "{} mismatches, first ones:\n{}", bad.len(), bad.iter().take(12).cloned().collect::<Vec<_>>().join("\n"));
}

#[test]
fn the_number_puzzle_reader_matches_python() {
    let mut bad: Vec<String> = Vec::new();
    for entry in corpus() {
        let problem = entry["p"].as_str().unwrap();
        let got = word_solver::solve_number_puzzle(problem);
        match (got, entry["np"].as_array()) {
            (None, None) => {}
            (Some(g), Some(w)) => {
                let gt = (g.answer.to_string(), g.equation.clone(), g.reading.clone());
                let wt = (w[0].as_str().unwrap().to_string(), w[1].as_str().unwrap().to_string(), w[2].as_str().unwrap().to_string());
                if gt != wt {
                    bad.push(format!("differs on {problem:?}\n   rust: {gt:?}\n   py  : {wt:?}"));
                }
            }
            (Some(g), None) => bad.push(format!("answers {} where Python declines: {problem:?}", g.answer)),
            (None, Some(w)) => bad.push(format!("declines where Python answers {:?}: {problem:?}", w[0])),
        }
    }
    assert!(bad.is_empty(), "{} mismatches, first ones:\n{}", bad.len(), bad.iter().take(12).cloned().collect::<Vec<_>>().join("\n"));
}

#[test]
fn solve_matches_python_on_every_problem() {
    let mut bad: Vec<String> = Vec::new();
    for entry in corpus() {
        let problem = entry["p"].as_str().unwrap();
        let got = word_solver::solve(problem);
        match (got, entry["solve"].as_array()) {
            (None, None) => {}
            (Some(g), Some(w)) => {
                let gt = (g.family.to_string(), values_text(&g.values));
                let wt = (w[0].as_str().unwrap().to_string(), json_strings(&w[1]));
                if gt != wt {
                    bad.push(format!("differs on {problem:?}\n   rust: {gt:?}\n   py  : {wt:?}"));
                }
            }
            (Some(g), None) => bad.push(format!("answers {:?} where Python declines: {problem:?}", values_text(&g.values))),
            (None, Some(w)) => bad.push(format!("declines where Python answers {:?}: {problem:?}", w[1])),
        }
    }
    assert!(bad.is_empty(), "{} mismatches, first ones:\n{}", bad.len(), bad.iter().take(12).cloned().collect::<Vec<_>>().join("\n"));
}
