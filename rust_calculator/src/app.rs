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
}

impl Default for CalculatorApp {
    fn default() -> Self {
        Self {
            doc: Document::new(),
            status: "Pick Operators, choose Addition, type numbers, press =.".into(),
            show_ops: true,
            op_filter: String::new(),
            selected_category: "All".into(),
        }
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
                        if let Some(op) = self.doc.rows[i].operator() {
                            ui.label(format!("{}  ({})", op.pattern, op.name));
                        } else {
                            ui.weak("(no operator — open Operators)");
                        }
                    });

                    ui.horizontal(|ui| {
                        let arity = self.doc.rows[i].inputs.len();
                        for b in 0..arity {
                            let focused = i == self.doc.target_row && b == self.doc.target_box;
                            let name = self.doc.rows[i]
                                .operator()
                                .and_then(|o| o.inputs.get(b).copied())
                                .unwrap_or("?");
                            ui.vertical(|ui| {
                                ui.small(name);
                                let te = TextEdit::singleline(&mut self.doc.rows[i].inputs[b])
                                    .desired_width(72.0)
                                    .font(egui::TextStyle::Heading);
                                let resp = ui.add(te);
                                if resp.gained_focus() || resp.clicked() {
                                    self.doc.target_row = i;
                                    self.doc.target_box = b;
                                }
                                if focused {
                                    ui.small(RichText::new("◀").color(ORANGE));
                                }
                            });
                            if let Some(op) = self.doc.rows[i].operator() {
                                // show op symbol between boxes when pattern uses a single symbol
                                if b + 1 < arity {
                                    ui.label(RichText::new(op.symbol).size(18.0).strong());
                                }
                            }
                        }
                        ui.label(RichText::new("=").size(20.0).strong());
                        ui.add(
                            TextEdit::singleline(&mut self.doc.rows[i].result)
                                .desired_width(120.0)
                                .interactive(false),
                        );
                        if let Some(err) = &self.doc.rows[i].error {
                            ui.colored_label(RED, err);
                        }
                    });

                    ui.horizontal(|ui| {
                        ui.label("Join to next row:");
                        for (j, label) in [
                            (Join::None, "·"),
                            (Join::Add, "+"),
                            (Join::Sub, "−"),
                            (Join::Mul, "×"),
                            (Join::Div, "÷"),
                            (Join::Eq, "="),
                        ] {
                            if ui
                                .selectable_label(self.doc.rows[i].join == j, label)
                                .clicked()
                            {
                                self.doc.rows[i].join = j;
                            }
                        }
                    });
                });
                ui.add_space(6.0);
            }
        });
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

    fn equals(&mut self) {
        self.doc.ensure_target();
        let i = self.doc.target_row;
        self.doc.rows[i].compute();
        if let Some(err) = &self.doc.rows[i].error {
            self.status = err.clone();
        } else {
            self.status = format!("Row {} = {}", i + 1, self.doc.rows[i].result);
            // advance to next empty input, or stay on result
            if let Some(op) = self.doc.rows[i].operator() {
                if self.doc.target_box + 1 < op.arity() {
                    self.doc.target_box += 1;
                }
            }
        }
    }
}

fn colored_btn(ui: &mut Ui, text: &str, bg: Color32) -> egui::Response {
    ui.add(Button::new(RichText::new(text).color(Color32::WHITE).strong()).fill(bg))
}
