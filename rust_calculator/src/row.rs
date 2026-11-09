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
        }
    }
}

#[derive(Clone, Debug)]
pub struct Row {
    pub op_key: Option<String>,
    /// Text in each input box (left of =).
    pub inputs: Vec<String>,
    pub result: String,
    pub join: Join,
    pub error: Option<String>,
}

impl Row {
    pub fn blank() -> Self {
        Self {
            op_key: None,
            inputs: Vec::new(),
            result: String::new(),
            join: Join::None,
            error: None,
        }
    }

    pub fn set_operator(&mut self, op: &Operator) {
        self.op_key = Some(op.key.to_string());
        self.inputs = vec![String::new(); op.arity()];
        self.result.clear();
        self.error = None;
    }

    pub fn operator(&self) -> Option<&'static Operator> {
        self.op_key.as_deref().and_then(ops::get)
    }

    pub fn compute(&mut self) {
        self.error = None;
        self.result.clear();
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
            Ok(v) => self.result = v.display(),
            Err(e) => self.error = Some(e),
        }
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

    pub fn next_row(&mut self) {
        if self.target_row + 1 >= self.rows.len() {
            self.rows.push(Row::blank());
        }
        self.target_row += 1;
        self.target_box = 0;
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
        row.result.clear();
        row.error = None;
    }

    pub fn backspace(&mut self) {
        self.ensure_target();
        let row = &mut self.rows[self.target_row];
        if row.inputs.is_empty() || self.target_box >= row.inputs.len() {
            return;
        }
        row.inputs[self.target_box].pop();
        row.result.clear();
        row.error = None;
    }

    pub fn clear_entry(&mut self) {
        self.ensure_target();
        let row = &mut self.rows[self.target_row];
        if row.inputs.is_empty() || self.target_box >= row.inputs.len() {
            return;
        }
        row.inputs[self.target_box].clear();
        row.result.clear();
        row.error = None;
    }
}

impl Default for Document {
    fn default() -> Self {
        Self::new()
    }
}
