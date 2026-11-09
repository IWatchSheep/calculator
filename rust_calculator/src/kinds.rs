//! Typed text -> `Value`, the Rust twin of `parse(kind, text)` in `operator_row_math/advanced_input.py`.
//!
//! The kinds are the ones an operator's boxes can have (`number`, `list`, `matrix`, `function`, `multi`,
//! `predicate`, `set`, `pairs`, `graph`, `wgraph`, `text`, `setfamily`, `item`); the same text a person types in
//! the Python Advanced Input window gives the same value here.

use crate::expr::Callable;
use crate::value::Value;

fn num(tok: &str) -> Result<f64, String> {
    let t = tok.trim();
    t.parse::<f64>().map_err(|_| format!("'{t}' is not a number"))
}

/// A number if it reads as one, otherwise a name (quotes stripped).
fn item(tok: &str) -> Value {
    let t = tok.trim();
    match t.parse::<f64>() {
        Ok(v) if !t.is_empty() => Value::Number(v),
        _ => Value::Text(t.trim_matches(|c| c == '\'' || c == '"').to_string()),
    }
}

fn split_list(text: &str) -> Vec<String> {
    text.replace([',', '[', ']'], " ").split_whitespace().map(|s| s.to_string()).collect()
}

pub fn parse_kind(kind: &str, text: &str) -> Result<Value, String> {
    let text = text.trim();
    if text.is_empty() {
        return Err("Type something first (see the example).".into());
    }
    let cant = |what: &str| format!("I can't read that as a {what}.");
    match kind {
        "number" => Ok(Value::Number(num(text).map_err(|_| cant("number"))?)),
        "list" => {
            let v: Result<Vec<Value>, String> = split_list(text).iter().map(|t| num(t).map(Value::Number)).collect();
            Ok(Value::List(v.map_err(|_| cant("list / vector of numbers"))?))
        }
        "matrix" => {
            let cleaned = text.replace(['[', ']'], " ").replace('\n', ";");
            let mut rows: Vec<Vec<Value>> = vec![];
            for r in cleaned.split(';').filter(|r| !r.trim().is_empty()) {
                let row: Result<Vec<Value>, String> =
                    r.replace(',', " ").split_whitespace().map(|t| num(t).map(Value::Number)).collect();
                rows.push(row.map_err(|_| cant("matrix"))?);
            }
            if rows.iter().map(|r| r.len()).collect::<std::collections::BTreeSet<_>>().len() != 1 {
                return Err("Every row of the matrix needs the same number of entries.".into());
            }
            Ok(Value::List(rows.into_iter().map(Value::List).collect()))
        }
        "function" | "multi" | "predicate" => {
            Callable::parse(text)?;
            Ok(Value::Func(text.to_string()))
        }
        "set" => Ok(Value::set_of(
            text.trim_matches(|c| c == '{' || c == '}').split(',').filter(|t| !t.trim().is_empty()).map(item).collect(),
        )),
        "pairs" => {
            let body = text.trim().trim_start_matches('[').trim_end_matches(']');
            let mut out = vec![];
            let mut rest = body;
            while let Some(a) = rest.find('(') {
                let b = rest[a..].find(')').ok_or_else(|| cant("list of pairs (edges)"))? + a;
                out.push(Value::Tuple(rest[a + 1..b].split(',').filter(|t| !t.trim().is_empty()).map(item).collect()));
                rest = &rest[b + 1..];
            }
            if out.is_empty() {
                return Err(cant("list of pairs (edges)"));
            }
            Ok(Value::List(out))
        }
        "graph" | "wgraph" => {
            let mut g: Vec<(Value, Value)> = vec![];
            for part in text.split(';').filter(|p| !p.trim().is_empty()) {
                let (head, rest) = part.split_once(':').unwrap_or((part, ""));
                let mut nbrs = vec![];
                for tok in rest.split(',').filter(|t| !t.trim().is_empty()) {
                    if kind == "wgraph" {
                        let (name, w) = tok.split_once('=').unwrap_or((tok, ""));
                        nbrs.push(Value::Tuple(vec![item(name), Value::Number(num(w).map_err(|_| cant("weighted graph"))?)]));
                    } else {
                        nbrs.push(item(tok));
                    }
                }
                let key = item(head);
                if let Some(slot) = g.iter_mut().find(|(k, _)| k.same_item(&key)) {
                    slot.1 = Value::List(nbrs); // a repeated vertex replaces the earlier one, like a dict
                } else {
                    g.push((key, Value::List(nbrs)));
                }
            }
            Ok(Value::Dict(g))
        }
        "item" => Ok(item(text)),
        "text" => Ok(Value::Text(text.to_string())),
        "setfamily" => {
            let mut groups = vec![];
            let mut rest = text;
            while let Some(a) = rest.find('{') {
                let Some(b) = rest[a + 1..].find('}') else { break };
                let inner = &rest[a + 1..a + 1 + b];
                if inner.contains('{') {
                    rest = &rest[a + 1..];
                    continue;
                }
                groups.push(Value::set_of(inner.split(',').filter(|t| !t.trim().is_empty()).map(item).collect()));
                rest = &rest[a + 1 + b + 1..];
            }
            if groups.is_empty() {
                return Err("Put each set in braces, e.g. {1,2}, {2,3}".into());
            }
            Ok(Value::List(groups))
        }
        other => Err(format!("Unknown input type '{other}'.")),
    }
}
