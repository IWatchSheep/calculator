//! egui desktop UI — same jobs as the Python Tkinter shell (phase 1).

use eframe::egui::{self, Color32, RichText, Ui};
use egui::{Button, ScrollArea, TextEdit};

use crate::ops;
use crate::row::{Document, Join};

const CREAM: Color32 = Color32::from_rgb(0xff, 0xfb, 0xe6);
const BLUE: Color32 = Color32::from_rgb(0x1e, 0x6f, 0xd9);
const GREEN: Color32 = Color32::from_rgb(0x3c, 0xb0, 0x43);
const RED: Color32 = Color32::from_rgb(0xe0, 0x20, 0x20);
const ORANGE: Color32 = Color32::from_rgb(0xf0, 0x70, 0x30);

pub struct CalculatorApp {
    doc: Document,
    status: String,
    show_ops: bool,
    op_filter: String,
    selected_category: String,
    /// The list shows the 1,000 algebra word problems instead of the operators.
    show_words: bool,
    word_category: String,
}

impl Default for CalculatorApp {
    fn default() -> Self {
        Self {
            doc: Document::new(),
            status: "Pick Operators, choose Addition, type numbers, press =.".into(),
            show_ops: true,
            op_filter: String::new(),
            selected_category: "All".into(),
            show_words: false,
            word_category: "All".into(),
        }
    }
}

impl CalculatorApp {
    /// Open with Row 1 already holding an operator and its numbers, and `=` pressed (used to look at a row: `rust_calculator --demo <operator key> <numbers...>`).
    pub fn with_demo(key: &str, inputs: &[String]) -> Self {
        let mut app = Self::default();
        if let Some(op) = ops::get(key) {
            app.doc.rows[0].set_operator(op);
            for (i, t) in inputs.iter().enumerate() {
                if let Some(slot) = app.doc.rows[0].inputs.get_mut(i) {
                    *slot = t.clone();
                }
            }
            app.equals();
        } else {
            app.status = format!("no operator {key}");
        }
        app
    }
}

impl eframe::App for CalculatorApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        let mut style = (*ctx.style()).clone();
        style.visuals.panel_fill = CREAM;
        style.visuals.window_fill = Color32::WHITE;
        ctx.set_style(style);

        egui::TopBottomPanel::top("toolbar").show(ctx, |ui| {
            ui.horizontal(|ui| {
                ui.heading(RichText::new("Smart Token Expression Builder").strong());
                ui.add_space(12.0);
                if colored_btn(ui, "Clear (C)", RED).clicked() {
                    self.doc.clear();
                    self.status = "Cleared.".into();
                }
                if colored_btn(ui, "Next Row (↓)", GREEN).clicked() {
                    self.doc.next_row();
                    self.status = format!("Row {} ready.", self.doc.target_row + 1);
                }
                if colored_btn(ui, "Operators", BLUE).clicked() {
                    self.show_ops = !self.show_ops;
                }
            });
            ui.label(
                RichText::new(format!(
                    "Selected target: Row {} | Box {}",
                    self.doc.target_row + 1,
                    self.doc.target_box + 1
                ))
                .color(ORANGE)
                .strong(),
            );
        });

        egui::TopBottomPanel::bottom("status").show(ctx, |ui| {
            ui.label(&self.status);
        });

        if self.show_ops {
            egui::SidePanel::right("operators")
                .default_width(320.0)
                .show(ctx, |ui| {
                    self.ui_operators(ui);
                });
        }

        egui::SidePanel::left("keypad")
            .default_width(220.0)
            .show(ctx, |ui| {
                self.ui_keypad(ui);
            });

        egui::CentralPanel::default().show(ctx, |ui| {
            self.ui_rows(ui);
        });
    }
}

impl CalculatorApp {
    fn ui_operators(&mut self, ui: &mut Ui) {
        ui.horizontal(|ui| {
            ui.selectable_value(&mut self.show_words, false, "Operators");
            ui.selectable_value(&mut self.show_words, true, "Algebra word problems");
        });
        if self.show_words {
            self.ui_word_problems(ui);
            return;
        }
        ui.heading("Operators");
        ui.label("Click an operator to put it on the target row.");
        ui.horizontal(|ui| {
            ui.label("Filter:");
            ui.text_edit_singleline(&mut self.op_filter);
        });

        let cats = {
            let mut c = vec!["All".to_string()];
            for op in ops::all_operators() {
                let lab = if op.subcategory.is_empty() {
                    op.category.to_string()
                } else {
                    format!("{} / {}", op.category, op.subcategory)
                };
                if !c.contains(&lab) {
                    c.push(lab);
                }
            }
            c
        };
        egui::ComboBox::from_id_salt("cat")
            .selected_text(&self.selected_category)
            .show_ui(ui, |ui| {
                for c in &cats {
                    ui.selectable_value(&mut self.selected_category, c.clone(), c);
                }
            });

        ui.separator();
        let filter = self.op_filter.to_ascii_lowercase();
        ScrollArea::vertical().show(ui, |ui| {
            let mut pick: Option<&'static str> = None;
            for op in ops::all_operators() {
                let lab = if op.subcategory.is_empty() {
                    op.category.to_string()
                } else {
                    format!("{} / {}", op.category, op.subcategory)
                };
                if self.selected_category != "All" && lab != self.selected_category {
                    continue;
                }
                if !filter.is_empty() {
                    let blob = format!("{} {} {} {}", op.name, op.symbol, op.key, op.formula).to_ascii_lowercase();
                    if !blob.contains(&filter) {
                        continue;
                    }
                }
                let label = format!("{}   {}", op.symbol, op.name);
                if ui.selectable_label(false, label).clicked() {
                    pick = Some(op.key);
                }
                ui.weak(op.formula);
            }
            if let Some(key) = pick {
                self.apply_operator(key);
            }
        });
    }

    /// The 1,000 algebra word problems: a Ready one goes into the target row as its equation (the boxes hold the numbers of the text, press `=`);
    /// a Reference one only says that nothing answers it yet.
    fn ui_word_problems(&mut self, ui: &mut Ui) {
        ui.heading("Algebra word problems");
        ui.label("Click a problem. Ready ones go into the target row as their equation.");
        ui.horizontal(|ui| {
            ui.label("Filter:");
            ui.text_edit_singleline(&mut self.op_filter);
        });
        let items = ops::words::items();
        let cats = {
            let mut c = vec!["All".to_string()];
            for it in items {
                if !c.iter().any(|x| x == it.category) {
                    c.push(it.category.to_string());
                }
            }
            c
        };
        egui::ComboBox::from_id_salt("wordcat").selected_text(&self.word_category).show_ui(ui, |ui| {
            for c in &cats {
                ui.selectable_value(&mut self.word_category, c.clone(), c);
            }
        });
        let ready = items.iter().filter(|i| i.ready).count();
        ui.weak(format!("{} problems: {} ready, {} reference only.", items.len(), ready, items.len() - ready));
        ui.separator();
        let filter = self.op_filter.to_ascii_lowercase();
        ScrollArea::vertical().show(ui, |ui| {
            let mut pick: Option<&'static ops::words::Item> = None;
            for it in items {
                if self.word_category != "All" && it.category != self.word_category {
                    continue;
                }
                if !filter.is_empty() && !format!("{} {} {}", it.id, it.category, it.problem).to_ascii_lowercase().contains(&filter) {
                    continue;
                }
                let tag = if it.ready { "Ready" } else { "Reference" };
                if ui.selectable_label(false, format!("{}  {}  [{}]", it.id, it.category, tag)).clicked() {
                    pick = Some(it);
                }
                ui.weak(it.problem);
            }
            if let Some(it) = pick {
                self.apply_word_problem(it);
            }
        });
    }

    fn apply_word_problem(&mut self, it: &ops::words::Item) {
        if !it.ready {
            self.status = format!(
                "{} {} is reference only: its text and steps are stored, but no solver answers it yet, so it is not placed in a row.  {}",
                it.category, it.id, it.problem
            );
            return;
        }
        self.apply_operator(&format!("word:{}", it.key));
        self.status = format!(
            "{}  {} {}: the row is its equation. Each box holds a number from the text, already filled in: press =, or change a box first.",
            it.problem, it.category, it.id
        );
    }

    fn apply_operator(&mut self, key: &str) {
        self.doc.ensure_target();
        if let Some(op) = ops::get(key) {
            let row = &mut self.doc.rows[self.doc.target_row];
            row.set_operator(op);
            self.doc.target_box = 0;
            self.status = format!(
                "Row {}: {} — fill the boxes, press =.  {}",
                self.doc.target_row + 1,
                op.name,
                op.formula
            );
        }
    }

    fn ui_rows(&mut self, ui: &mut Ui) {
        ui.heading("Mathematical Addend Sequence");
        ScrollArea::both().show(ui, |ui| {
            for i in 0..self.doc.rows.len() {
                ui.group(|ui| {
                    ui.horizontal(|ui| {
                        let selected = i == self.doc.target_row;
                        let title = format!("Row {}", i + 1);
                        if ui
                            .selectable_label(selected, RichText::new(title).strong())
                            .clicked()
                        {
                            self.doc.target_row = i;
                            self.doc.target_box = 0;
                        }
                        if self.doc.rows[i].is_result {
                            ui.weak("(the answer for the rows above)");
                        } else if let Some(op) = self.doc.rows[i].operator() {
                            ui.label(format!("{}  ({})", op.pattern, op.name));
                        } else {
                            ui.weak("(no operator — open Operators)");
                        }
                    });

                    // Row 2 and below are joined to the rows above by a math sign.
                    if i > 0 && !self.doc.rows[i].is_result {
                        ui.horizontal(|ui| {
                            ui.label(format!("Join Row {} to the rows above:", i + 1));
                            for (j, label) in [
                                (Join::None, "·"),
                                (Join::Add, "+"),
                                (Join::Sub, "−"),
                                (Join::Mul, "×"),
                                (Join::Div, "÷"),
                                (Join::Eq, "="),
                                (Join::Ne, "≠"),
                                (Join::Lt, "<"),
                                (Join::Gt, ">"),
                                (Join::Le, "≤"),
                                (Join::Ge, "≥"),
                            ] {
                                if ui
                                    .selectable_label(self.doc.rows[i].join == j, label)
                                    .clicked()
                                {
                                    self.doc.rows[i].join = j;
                                    self.doc.rows[i].clear_result();
                                }
                            }
                        });
                    }

                    if self.doc.rows[i].is_result {
                        ui.horizontal(|ui| {
                            ui.label(RichText::new("=").size(20.0).strong());
                            let mut shown = self.doc.rows[i].result.clone();
                            let w = answer_width(&shown, 220.0);
                                        ui.add(TextEdit::singleline(&mut shown).desired_width(w).interactive(false));
                        });
                        return;
                    }

                    let is_target = i == self.doc.target_row;
                    let target_box = self.doc.target_box;
                    let focused = self.ui_formula(ui, i, is_target, target_box);
                    if let Some(b) = focused {
                        self.doc.target_row = i;
                        self.doc.target_box = b;
                    }
                });
                ui.add_space(6.0);
            }
        });
    }

    /// One row's math: the operator's picture written as cards on a grid.  Fractions are drawn top to bottom, exponents one line up and subscripts one line
    /// down; all of those lines are this ONE row.  The answer is in the card to the right of the `=`, on the same row.
    /// Returns the input box that was clicked or focused.
    fn ui_formula(&mut self, ui: &mut Ui, i: usize, is_target: bool, target_box: usize) -> Option<usize> {
        use crate::layout::{self, CardKind};
        let mut focused = None;
        let layout = self.doc.rows[i].operator().and_then(|op| layout::get(op.key));
        let Some(layout) = layout else {
            ui.label("(no picture for this operator)");
            return None;
        };
        let plan = layout::plan(layout.cards);
        let (n_rows, n_cols) = (plan.rows().max(1) as usize, plan.columns.max(1) as usize);
        // what is in each grid cell
        enum Cell {
            Empty,
            Card(usize),
            Bar,
        }
        let mut grid: Vec<Vec<Cell>> = (0..n_rows).map(|_| (0..n_cols).map(|_| Cell::Empty).collect()).collect();
        for (idx, p) in plan.placed.iter().enumerate() {
            if let Some((r, c)) = p {
                grid[*r as usize][*c as usize] = Cell::Card(idx);
            }
        }
        for &(r, c, w) in &plan.bars {
            for k in c..c + w {
                if let Cell::Empty = grid[r as usize][k as usize] {
                    grid[r as usize][k as usize] = Cell::Bar;
                }
            }
        }
        // the grid row of the main line: the first card on the line, outside any fraction
        let main_row = layout
            .cards
            .iter()
            .enumerate()
            .find(|(_, c)| c.level == 0 && c.frac.is_empty())
            .and_then(|(idx, _)| plan.placed[idx])
            .map(|(r, _)| r as usize)
            .unwrap_or(0);
        let arity = self.doc.rows[i].inputs.len();
        let outs = self.doc.rows[i].outs.clone();
        let names: Vec<&'static str> = self.doc.rows[i].operator().map(|o| o.inputs.to_vec()).unwrap_or_default();

        ui.horizontal(|ui| {
            egui::Grid::new(("formula", i)).spacing([4.0, 8.0]).show(ui, |ui| {
                for r in 0..n_rows {
                    for c in 0..n_cols {
                        match grid[r][c] {
                            Cell::Empty => {
                                ui.label("");
                            }
                            Cell::Bar => {
                                ui.add(egui::Separator::default().horizontal().spacing(2.0));
                            }
                            Cell::Card(idx) => {
                                let card = &layout.cards[idx];
                                match card.kind {
                                    CardKind::Op => {
                                        ui.label(RichText::new(card.text).size(22.0).strong());
                                    }
                                    CardKind::Dec => {
                                        let t = if card.text.is_empty() { "□" } else { card.text };
                                        ui.label(RichText::new(t).size(22.0));
                                    }
                                    CardKind::Out => {
                                        // the k-th answer box of the formula (counted over the whole layout, not this grid row)
                                        let k = layout.cards[..idx].iter().filter(|c| c.kind == CardKind::Out).count();
                                        let shown = outs.get(k).cloned().unwrap_or_default();
                                        // a framed label, so it is exactly as wide as the answer (an answer box is never typed into)
                                        egui::Frame::none()
                                            .stroke(egui::Stroke::new(1.0, Color32::GRAY))
                                            .inner_margin(egui::Margin::same(4.0))
                                            .rounding(3.0)
                                            .show(ui, |ui| {
                                                let t = if shown.is_empty() { "□".to_string() } else { shown.clone() };
                                                ui.label(RichText::new(t).size(20.0));
                                            });
                                    }
                                    CardKind::Box => {
                                        let slot = card.slot as usize;
                                        if slot < arity {
                                            ui.vertical(|ui| {
                                                ui.small(names.get(slot).copied().unwrap_or("?"));
                                                let te = TextEdit::singleline(&mut self.doc.rows[i].inputs[slot])
                                                    .desired_width(64.0)
                                                    .font(egui::TextStyle::Heading);
                                                let resp = ui.add(te);
                                                if resp.gained_focus() || resp.clicked() {
                                                    focused = Some(slot);
                                                }
                                                if is_target && slot == target_box {
                                                    ui.small(RichText::new("◀").color(ORANGE));
                                                }
                                            });
                                        } else {
                                            ui.label(RichText::new("□").size(22.0));
                                        }
                                    }
                                }
                            }
                        }
                    }
                    ui.end_row();
                }
            });
            // the answer: to the right of the "=", on the main line of the same row
            ui.vertical(|ui| {
                ui.add_space(main_row as f32 * 46.0);
                ui.horizontal(|ui| {
                    ui.label(RichText::new("=").size(22.0).strong());
                    let mut shown = self.doc.rows[i].result.clone();
                    let w = answer_width(&shown, 130.0);
                                        ui.add(TextEdit::singleline(&mut shown).desired_width(w).font(egui::TextStyle::Heading).interactive(false));
                });
                if let Some(err) = &self.doc.rows[i].error {
                    ui.colored_label(RED, err);
                }
            });
        });
        focused
    }

    fn ui_keypad(&mut self, ui: &mut Ui) {
        ui.heading("Keypad");
        let rows = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "±", "+"],
        ];
        for row in rows {
            ui.horizontal(|ui| {
                for key in row {
                    let size = egui::vec2(44.0, 36.0);
                    if ui.add_sized(size, Button::new(key)).clicked() {
                        self.on_key(key);
                    }
                }
            });
        }
        ui.horizontal(|ui| {
            if colored_btn(ui, "C", RED).clicked() {
                self.doc.clear_entry();
            }
            if colored_btn(ui, "⌫", ORANGE).clicked() {
                self.doc.backspace();
            }
            if colored_btn(ui, "=", GREEN).clicked() {
                self.equals();
            }
        });
        ui.separator();
        ui.label("Phase 1 Rust port of the Python calculator.");
        ui.label(format!("{} ready operators loaded.", ops::all_operators().len()));
        ui.weak("Templates, Advanced Input, nested ops, formula pictures: later phases.");
    }

    fn on_key(&mut self, key: &str) {
        match key {
            "±" => {
                self.doc.ensure_target();
                let row = &mut self.doc.rows[self.doc.target_row];
                if let Some(s) = row.inputs.get_mut(self.doc.target_box) {
                    if let Some(rest) = s.strip_prefix('-') {
                        *s = rest.to_string();
                    } else if !s.is_empty() {
                        s.insert(0, '-');
                    } else {
                        s.push('-');
                    }
                }
            }
            "." => self.doc.append_digit('.'),
            d if d.len() == 1 && d.chars().next().unwrap().is_ascii_digit() => {
                self.doc.append_digit(d.chars().next().unwrap());
            }
            _ => {}
        }
    }

    /// `=`: calculate every row (Row 1, and Row 2 joined to it, ...).  Each row shows its own answer to the right of its `=`; joined rows also give the
    /// answer for all of them in the next row (Row 3 for Rows 1 and 2).
    fn equals(&mut self) {
        self.status = match self.doc.equals_all() {
            Ok(msg) => msg,
            Err(e) => e,
        };
    }
}

/// Wide enough for the whole answer (a long answer such as 7.415555556e-11 must not be cut off).
fn answer_width(text: &str, min: f32) -> f32 {
    (text.chars().count() as f32 * 15.0 + 16.0).max(min)
}

fn colored_btn(ui: &mut Ui, text: &str, bg: Color32) -> egui::Response {
    ui.add(Button::new(RichText::new(text).color(Color32::WHITE).strong()).fill(bg))
}
