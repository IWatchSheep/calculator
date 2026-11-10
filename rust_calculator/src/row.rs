//! One calculator row: operator, input boxes, join symbol, result.

use crate::operator::Operator;
use crate::ops;
use crate::value::Value;

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Join {
    None,
    Add,
    Sub,
    Mul,
    Div,
    Eq,
    Ne,
    Lt,
    Gt,
    Le,
    Ge,
}

impl Join {
    pub fn symbol(self) -> &'static str {
        match self {
            Join::None => "",
            Join::Add => "+",
            Join::Sub => "−",
            Join::Mul => "×",
            Join::Div => "÷",
            Join::Eq => "=",
            Join::Ne => "≠",
            Join::Lt => "<",
            Join::Gt => ">",
            Join::Le => "≤",
            Join::Ge => "≥",
        }
    }

    /// Combine the answer so far with the next row's answer.  Lists and the like cannot be joined (the same rule as the Python program).
    pub fn apply(self, a: &Value, b: &Value) -> Result<Value, String> {
        let (x, y) = match (a, b) {
            (Value::Number(x), Value::Number(y)) => (*x, *y),
            _ => return Err(format!("Can't join those two results with {}.", self.symbol())),
        };
        let close = |p: f64, q: f64| (p - q).abs() <= 1e-3 * 1.0_f64.max(p.abs()).max(q.abs());
        Ok(match self {
            Join::None => return Err("pick a join symbol".into()),
            Join::Add => Value::Number(x + y),
            Join::Sub => Value::Number(x - y),
            Join::Mul => Value::Number(x * y),
            Join::Div => {
                if y == 0.0 {
                    return Err("Division by zero.".into());
                }
                Value::Number(x / y)
            }
            Join::Eq => Value::Bool(close(x, y)),
            Join::Ne => Value::Bool(!close(x, y)),
            Join::Lt => Value::Bool(x < y),
            Join::Gt => Value::Bool(x > y),
            Join::Le => Value::Bool(x <= y),
            Join::Ge => Value::Bool(x >= y),
        })
    }
}

#[derive(Clone, Debug)]
pub struct Row {
    pub op_key: Option<String>,
    /// Text in each input box (one per input of the operator; a variable the picture writes twice is one input with two boxes).
    pub inputs: Vec<String>,
    /// The row's own answer, shown in its answer card to the right of the `=`.
    pub result: String,
    /// The answer as a value (used when rows are joined).
    pub value: Option<Value>,
    /// What each of the formula's answer boxes shows (one for a single answer, one each for `x1, x2`).
    pub outs: Vec<String>,
    /// How this row is joined to the rows above it (Row 1 has none).
    pub join: Join,
    /// A row that only shows the answer for the rows above it (Row 3 when Rows 1 and 2 are joined).
    pub is_result: bool,
    pub error: Option<String>,
}

impl Row {
    pub fn blank() -> Self {
        Self {
            op_key: None,
            inputs: Vec::new(),
            result: String::new(),
            value: None,
            outs: Vec::new(),
            join: Join::None,
            is_result: false,
            error: None,
        }
    }

    /// Forget the answer (something was changed).
    pub fn clear_result(&mut self) {
        self.result.clear();
        self.value = None;
        self.outs.clear();
    }

    /// How many answer boxes the formula has.
    pub fn out_count(&self) -> usize {
        self.operator()
            .and_then(|op| crate::layout::get(op.key))
            .map(|l| l.cards.iter().filter(|c| c.kind == crate::layout::CardKind::Out).count())
            .unwrap_or(0)
    }

    pub fn is_blank(&self) -> bool {
        self.op_key.is_none() && !self.is_result
    }

    pub fn set_operator(&mut self, op: &Operator) {
        self.op_key = Some(op.key.to_string());
        self.inputs = vec![String::new(); op.arity()];
        self.clear_result();
        self.is_result = false;
        self.error = None;
    }

    pub fn operator(&self) -> Option<&'static Operator> {
        self.op_key.as_deref().and_then(ops::get)
    }

    pub fn compute(&mut self) {
        self.error = None;
        self.clear_result();
        let Some(op) = self.operator() else {
            self.error = Some("pick an operator first".into());
            return;
        };
        // Each box is typed the way the Python Advanced Input window takes it: a number, `1, 2, 3` for a list,
        // `1 2; 3 4` for a matrix, `x**2 + 3*x` for a function, `A: B, C; B: C` for a graph ...
        let mut args = Vec::with_capacity(op.arity());
        for (i, raw) in self.inputs.iter().enumerate() {
            let t = raw.trim();
            if t.is_empty() {
                self.error = Some(format!("fill box {} ({})", i + 1, op.inputs.get(i).unwrap_or(&"?")));
                return;
            }
            let kind = op.kinds.get(i).copied().unwrap_or("number");
            match crate::kinds::parse_kind(kind, t) {
                Ok(Value::Number(n)) if !n.is_finite() => {
                    self.error = Some(format!("box {} is not finite", i + 1));
                    return;
                }
                Ok(v) => args.push(v),
                Err(_) if kind == "number" => {
                    self.error = Some(format!("box {} is not a number", i + 1));
                    return;
                }
                Err(e) => {
                    self.error = Some(format!("box {} ({}): {}", i + 1, op.inputs.get(i).unwrap_or(&"?"), e));
                    return;
                }
            }
        }
        match op.run_values(&args) {
            Ok(v) => {
                self.result = v.show();
                self.outs = out_texts(&v, self.out_count());
                self.value = Some(v);
            }
            Err(e) => self.error = Some(e),
        }
    }
}

/// What each answer box of the formula shows: a single answer in the one box, or each of `(x1, x2)` in its own box.
pub fn out_texts(v: &Value, outs: usize) -> Vec<String> {
    if outs == 0 {
        return Vec::new();
    }
    let parts: Option<Vec<String>> = match v {
        Value::Pair(a, b) => Some(vec![Value::Number(*a).show(), Value::Number(*b).show()]),
        Value::Tuple(items) | Value::List(items) => Some(items.iter().map(|x| x.show()).collect()),
        _ => None,
    };
    match parts {
        Some(p) if outs > 1 && p.len() == outs => p,
        _ => vec![v.show(); outs],
    }
}

#[derive(Clone, Debug)]
pub struct Document {
    pub rows: Vec<Row>,
    /// Which row receives the next operator / keypad digits.
    pub target_row: usize,
    /// Which input box in that row is focused.
    pub target_box: usize,
}

impl Document {
    pub fn new() -> Self {
        Self {
            rows: vec![Row::blank(), Row::blank()],
            target_row: 0,
            target_box: 0,
        }
    }

    pub fn clear(&mut self) {
        *self = Self::new();
    }

    pub fn ensure_target(&mut self) {
        if self.rows.is_empty() {
            self.rows.push(Row::blank());
        }
        if self.target_row >= self.rows.len() {
            self.target_row = self.rows.len() - 1;
        }
        let n = self.rows[self.target_row].inputs.len().max(1);
        if self.target_box >= n {
            self.target_box = 0;
        }
    }

    /// Next Row: from Row 1 to Row 2, and so on.  (The lines of one operator's math are not rows: only this button and the join signs make rows.)
    pub fn next_row(&mut self) {
        if self.target_row + 1 >= self.rows.len() {
            self.rows.push(Row::blank());
        }
        self.target_row += 1;
        self.target_box = 0;
        if self.rows[self.target_row].is_result {
            self.rows[self.target_row] = Row::blank(); // carry on from the answer row
        }
    }

    /// `=`: calculate every row that has math, join them with the join signs (Row 2 joins to Row 1, and so on), show each row's own answer in its own answer card
    /// and, when rows were joined, the answer for all of them in the row after the last one used (Row 3 for Rows 1 and 2).  Returns the message to show.
    pub fn equals_all(&mut self) -> Result<String, String> {
        // a previous answer row is dropped; the rows go back to being ready for more math
        while self.rows.len() > 2 && self.rows.last().map_or(false, |r| r.is_result) {
            self.rows.pop();
        }
        for r in self.rows.iter_mut() {
            if r.is_result {
                *r = Row::blank();
            }
        }
        if self.rows[0].is_blank() {
            return Err("Pick an operator for Row 1 (open Operators), type its numbers, then press =.".into());
        }
        let mut total: Option<Value> = None;
        let (mut used, mut last) = (0usize, 0usize);
        for k in 0..self.rows.len() {
            if self.rows[k].is_blank() {
                continue;
            }
            self.rows[k].compute();
            if let Some(e) = self.rows[k].error.clone() {
                return Err(if k == 0 { e } else { format!("Row {}: {}", k + 1, e) });
            }
            let v = self.rows[k].value.clone().ok_or_else(|| format!("Row {} has no answer", k + 1))?;
            total = Some(match total {
                None => v,
                Some(t) => {
                    if self.rows[k].join == Join::None {
                        return Err(format!("Row {} needs a join symbol: pick + − × ÷ = above its boxes.", k + 1));
                    }
                    self.rows[k].join.apply(&t, &v)?
                }
            });
            used += 1;
            last = k;
        }
        let total = total.ok_or_else(|| "nothing to calculate".to_string())?;
        if used > 1 {
            if last + 1 >= self.rows.len() {
                self.rows.push(Row::blank());
            }
            let r = &mut self.rows[last + 1];
            *r = Row::blank();
            r.is_result = true;
            r.result = total.show();
            r.value = Some(total.clone());
            return Ok(format!("All {} rows joined = {}  (shown in Row {})", used, total.show(), last + 2));
        }
        Ok(format!("Row 1 = {}", total.show()))
    }

    pub fn append_digit(&mut self, ch: char) {
        self.ensure_target();
        let row = &mut self.rows[self.target_row];
        if row.inputs.is_empty() {
            return;
        }
        if self.target_box >= row.inputs.len() {
            self.target_box = 0;
        }
        row.inputs[self.target_box].push(ch);
        row.clear_result();
        row.error = None;
    }

    pub fn backspace(&mut self) {
        self.ensure_target();
        let row = &mut self.rows[self.target_row];
        if row.inputs.is_empty() || self.target_box >= row.inputs.len() {
            return;
        }
        row.inputs[self.target_box].pop();
        row.clear_result();
        row.error = None;
    }

    pub fn clear_entry(&mut self) {
        self.ensure_target();
        let row = &mut self.rows[self.target_row];
        if row.inputs.is_empty() || self.target_box >= row.inputs.len() {
            return;
        }
        row.inputs[self.target_box].clear();
        row.clear_result();
        row.error = None;
    }
}

impl Default for Document {
    fn default() -> Self {
        Self::new()
    }
}
