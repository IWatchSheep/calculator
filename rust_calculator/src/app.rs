//! egui desktop UI — same jobs as the Python Tkinter shell (phase 1).

use eframe::egui::{self, Color32, RichText, Ui};
use egui::{Button, ScrollArea, TextEdit};

use crate::ops;
use crate::row::{Document, Join, Row};

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
    /// Every card of a row shows its Label / Item and Context boxes (the words you type to describe it).
    show_card_words: bool,
    /// The Advanced Input window.
    show_adv: bool,
    adv_kind: String,
    adv_text: String,
    adv_msg: String,
    adv_filter: String,
    /// The operator (or `word:` problem) whose picture is shown in the side panel.
    preview_key: Option<String>,
    /// The word problem whose diagram is open in its own window (clicking another problem reuses the same window).
    diagram: Option<&'static ops::words::Item>,
    /// Mathematical Templates: typed math kept for later.
    tpl_text: String,
    tpl_saved: Vec<String>,
    tpl_pick: String,
    tpl_hide_guide: bool,
    tpl_guide: bool,
    tpl_previewed: Option<String>,
    tpl_applied: bool,
    tpl_last_text: String,
    tpl_preview: Option<TplPreview>,
    tpl_path: std::path::PathBuf,
}

/// The last preview posted into a row: what the row held before (put back when the preview is replaced, if the row was not edited since).
struct TplPreview {
    row: usize,
    snapshot: Row,
    shown: Vec<String>,
}

fn row_signature(r: &Row) -> Vec<String> {
    r.flatten().into_iter().map(|c| c.text).collect()
}

const GUIDE_STEPS: [(&str, &str); 4] = [
    (
        "Type your math in the text box",
        "Use ? or a letter such as x for a box you will fill in later. Examples:   (? + 3) × 2     sqrt(x) + 4     Time dilation(1, x)",
    ),
    (
        "Press  Preview Posted",
        "Your math appears in the target row, just like an operator from the Operators list, so you can see it. You can change the text and preview again.",
    ),
    (
        "Like it?  Press  Save Template",
        "It is kept on this computer, so it will be there next time too. Not happy? Change the text and press Preview Posted again.",
    ),
    (
        "Use it whenever you want",
        "Pick it in the list next to Apply Template, then press Apply Template. It goes into the row. Then fill the empty boxes and press the keypad = key.",
    ),
];

impl Default for CalculatorApp {
    fn default() -> Self {
        let tpl_path = crate::pictures::root().cloned().unwrap_or_else(|| std::path::PathBuf::from(".")).join("saved_templates.json");
        let tpl_loaded = crate::template_math::load_data(&tpl_path);
        Self {
            doc: Document::new(),
            status: "Pick Operators, choose Addition, type numbers, press =.".into(),
            show_ops: true,
            op_filter: String::new(),
            selected_category: "All".into(),
            show_words: false,
            show_card_words: false,
            word_category: "All".into(),
            show_adv: false,
            adv_kind: "list".into(),
            adv_text: String::new(),
            adv_msg: String::new(),
            adv_filter: String::new(),
            preview_key: None,
            diagram: None,
            tpl_text: String::new(),
            tpl_saved: tpl_loaded.0,
            tpl_pick: String::new(),
            tpl_hide_guide: tpl_loaded.1,
            tpl_guide: false,
            tpl_previewed: None,
            tpl_applied: false,
            tpl_last_text: String::new(),
            tpl_preview: None,
            tpl_path,
        }
    }
}

impl CalculatorApp {
    /// Open with Row 1 already holding an operator and its numbers, and `=` pressed (used to look at a row: `rust_calculator --demo <operator key> <numbers...>`).
    pub fn with_demo(key: &str, inputs: &[String]) -> Self {
        let mut app = Self::default();
        if let Some(op) = ops::get(key) {
            app.preview_key = Some(key.to_string());
            app.diagram = key.strip_prefix("word:").and_then(|k| ops::words::items().iter().find(|i| i.key == k));
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
                if colored_btn(ui, "Advanced Input", Color32::from_rgb(0x4a, 0x2a, 0x6a)).clicked() {
                    self.show_adv = !self.show_adv;
                    if self.show_adv {
                        self.adv_pick_suggested();
                    }
                }
            });
            ui.label(
                RichText::new(format!(
                    "Selected target: Row {} | Box {}",
                    self.doc.target_row + 1,
                    self.doc
                        .rows
                        .get(self.doc.target_row)
                        .and_then(|r| r.box_paths().iter().position(|p| *p == self.doc.target_path))
                        .map_or(1, |k| k + 1)
                ))
                .color(ORANGE)
                .strong(),
            );
        });

        egui::TopBottomPanel::bottom("status").show(ctx, |ui| {
            ui.label(&self.status);
        });
        self.ui_templates(ctx);
        self.ui_diagram_window(ctx);

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
        self.ui_advanced(ctx);
    }
}

impl CalculatorApp {
    fn ui_operators(&mut self, ui: &mut Ui) {
        ui.horizontal(|ui| {
            ui.selectable_value(&mut self.show_words, false, "Operators");
            ui.selectable_value(&mut self.show_words, true, "Algebra word problems");
        });
        self.ui_picture(ui);
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

    /// The formula picture of the selected operator, or the diagram of the selected word problem (read from the project folder).
    fn ui_picture(&mut self, ui: &mut Ui) {
        let Some(key) = self.preview_key.clone() else {
            ui.weak("Click an operator or a problem to see its picture.");
            return;
        };
        match crate::pictures::picture_for(&key) {
            Some(path) => {
                ui.add(egui::Image::new(crate::pictures::uri(&path)).max_width(300.0).max_height(170.0));
            }
            None => {
                ui.weak("(picture unavailable)");
            }
        }
        ui.separator();
    }

    /// The diagram of the clicked word problem in a window of its own: id, category, status, the problem text and the picture.
    fn ui_diagram_window(&mut self, ctx: &egui::Context) {
        let Some(it) = self.diagram else { return };
        let mut close = false;
        let builder = egui::ViewportBuilder::default().with_title(format!("{}  {}", it.id, it.category)).with_inner_size([1000.0, 640.0]);
        ctx.show_viewport_immediate(egui::ViewportId::from_hash_of("word_diagram"), builder, |ctx, _class| {
            egui::CentralPanel::default().frame(egui::Frame::none().fill(Color32::WHITE).inner_margin(egui::Margin::same(12.0))).show(ctx, |ui| {
                ui.label(RichText::new(format!("{}    {}    {}", it.id, it.category, if it.ready { "Ready" } else { "Reference" })).color(BLUE).strong().size(18.0));
                ui.add_space(4.0);
                ui.label(RichText::new(it.problem).color(Color32::BLACK).size(16.0));
                ui.add_space(8.0);
                match crate::pictures::word_picture(it.key) {
                    Some(path) => {
                        ui.add(egui::Image::new(crate::pictures::uri(&path)).max_width(960.0).max_height(480.0));
                    }
                    None => {
                        ui.label("The diagram file is not in the folder.");
                    }
                }
            });
            if ctx.input(|i| i.viewport().close_requested()) {
                close = true;
            }
        });
        if close {
            self.diagram = None;
        }
    }

    fn apply_word_problem(&mut self, it: &'static ops::words::Item) {
        self.diagram = Some(it);
        self.preview_key = Some(format!("word:{}", it.key));
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

    /// What the template steps have reached for the text in the box: (typed OK, previewed, saved, applied).
    fn tpl_progress(&self) -> [bool; 4] {
        let text = self.tpl_text.trim();
        let ok = crate::template_math::parse_math(text).is_ok();
        [
            ok,
            ok && self.tpl_previewed.as_deref() == Some(text),
            ok && self.tpl_saved.iter().any(|t| t == text),
            ok && self.tpl_applied && self.tpl_pick.trim() == text,
        ]
    }

    fn tpl_write_file(&mut self) {
        if let Err(e) = crate::template_math::save_data(&self.tpl_path, &self.tpl_saved, self.tpl_hide_guide) {
            self.status = format!("(Could not write {}: {}. The templates will be forgotten when the window closes.)", self.tpl_path.display(), e);
        }
    }

    /// Take the last preview out of its row again (only if nothing has been changed in that row since).
    fn tpl_restore_preview(&mut self) {
        let Some(state) = self.tpl_preview.take() else { return };
        if state.row < self.doc.rows.len() && row_signature(&self.doc.rows[state.row]) == state.shown {
            self.doc.rows[state.row] = state.snapshot;
        }
    }

    /// Preview Posted: put the typed math into the target row so it can be seen (and tried out).
    fn tpl_do_preview(&mut self) {
        let text = self.tpl_text.trim().to_string();
        let row = match crate::template_math::parse_math(&text) {
            Ok(r) => r,
            Err(e) => {
                self.status = format!("Template: {}", e);
                return;
            }
        };
        self.tpl_restore_preview();
        self.doc.ensure_target();
        let i = self.doc.target_row;
        let snapshot = if self.doc.rows[i].is_result { Row::blank() } else { self.doc.rows[i].clone() };
        let (describe, n) = (crate::template_math::describe(&row), crate::template_math::empty_boxes(&row));
        self.doc.place_row(row);
        self.tpl_preview = Some(TplPreview { row: i, snapshot, shown: row_signature(&self.doc.rows[i]) });
        self.tpl_previewed = Some(text);
        self.status = format!(
            "Preview - posted in Row {}:\n  {}\n{}\nLike it? Press Save Template. Not right? Change the text and press Preview Posted again.",
            i + 1,
            describe,
            if n > 0 { format!("{} empty square box{} to fill in.", n, if n == 1 { "" } else { "es" }) } else { "No empty boxes, so press the keypad = key to calculate it.".into() }
        );
    }

    /// Save Template: keep the typed math so it shows up in the Apply Template list.
    fn tpl_do_save(&mut self) {
        let text = self.tpl_text.trim().to_string();
        if let Err(e) = crate::template_math::parse_math(&text) {
            self.status = format!("Template: {}", e);
            return;
        }
        if self.tpl_saved.contains(&text) {
            self.status = format!("Already saved: {}\nPick it in the list next to Apply Template.", text);
        } else {
            self.tpl_saved.push(text.clone());
            self.tpl_write_file();
            if !self.status.starts_with("(Could not") {
                self.status = format!("Saved template: {}\nPick it in the list next to Apply Template and press Apply Template whenever you want it in a row. It is kept for next time too.", text);
            }
        }
        self.tpl_pick = text;
    }

    /// Apply Template: put the chosen template into the target row, like an operator from Operators.
    fn tpl_do_apply(&mut self) {
        let text = self.tpl_pick.trim().to_string();
        if text.is_empty() {
            self.status = "No template picked yet. Type some math in the text box, press Preview Posted, then Save Template, then pick it in this list.".into();
            return;
        }
        let row = match crate::template_math::parse_math(&text) {
            Ok(r) => r,
            Err(e) => {
                self.status = format!("Template: {}", e);
                return;
            }
        };
        self.tpl_restore_preview();
        let (describe, n) = (crate::template_math::describe(&row), crate::template_math::empty_boxes(&row));
        self.doc.place_row(row);
        self.tpl_applied = true;
        self.status = format!(
            "Template placed in Row {}:  {}\n{}",
            self.doc.target_row + 1,
            describe,
            if n > 0 { format!("Fill the {} empty square box{} (click one, then use the number pad), then press =.", n, if n == 1 { "" } else { "es" }) } else { "Nothing to fill in: press =".into() }
        );
    }

    /// The Mathematical Templates panel (typed math kept for later) and its how-to guide.
    fn ui_templates(&mut self, ctx: &egui::Context) {
        egui::TopBottomPanel::bottom("templates").show(ctx, |ui| {
            ui.horizontal(|ui| {
                ui.label(RichText::new("Mathematical Templates").strong());
                let r = ui.add(TextEdit::singleline(&mut self.tpl_text).desired_width(300.0).hint_text("(? + 3) × 2"));
                if r.changed() {
                    let text = self.tpl_text.trim().to_string();
                    if text != self.tpl_last_text {
                        self.tpl_applied = false;
                        if !text.is_empty() && self.tpl_last_text.is_empty() && !self.tpl_hide_guide {
                            self.tpl_guide = true;
                        }
                        self.tpl_last_text = text;
                    }
                }
                if ui.button("Preview Posted").clicked() {
                    self.tpl_do_preview();
                }
                if ui.button("Save Template").clicked() {
                    self.tpl_do_save();
                }
                egui::ComboBox::from_id_salt("tplpick").width(200.0).selected_text(if self.tpl_pick.is_empty() { "(saved templates)" } else { self.tpl_pick.as_str() }).show_ui(ui, |ui| {
                    for t in self.tpl_saved.clone() {
                        ui.selectable_value(&mut self.tpl_pick, t.clone(), t);
                    }
                });
                if ui.button("Apply Template").clicked() {
                    self.tpl_do_apply();
                }
                if ui.button("?").clicked() {
                    self.tpl_guide = true;
                }
            });
        });
        if !self.tpl_guide {
            return;
        }
        let mut open = true;
        let done = self.tpl_progress();
        let current = done.iter().position(|d| !d);
        let text = self.tpl_text.trim().to_string();
        let target_row = self.doc.target_row;
        let mut hide = self.tpl_hide_guide;
        egui::Window::new("Make your own template - 4 steps").open(&mut open).resizable(false).show(ctx, |ui| {
            ui.label("Follow the steps in order, left to right. The step you are on is yellow, finished steps are green with a tick.");
            ui.horizontal_top(|ui| {
                for (k, (title, detail)) in GUIDE_STEPS.iter().enumerate() {
                    let (fill, mark) = if done[k] {
                        (Color32::from_rgb(0xdf, 0xf3, 0xdc), "✓".to_string())
                    } else if Some(k) == current {
                        (Color32::from_rgb(0xff, 0xf3, 0xc4), (k + 1).to_string())
                    } else {
                        (Color32::WHITE, (k + 1).to_string())
                    };
                    egui::Frame::none().fill(fill).stroke(egui::Stroke::new(2.0, Color32::LIGHT_GRAY)).inner_margin(egui::Margin::same(8.0)).show(ui, |ui| {
                        ui.set_width(200.0);
                        ui.set_min_height(150.0);
                        ui.label(RichText::new(mark).size(22.0).strong());
                        ui.label(RichText::new(*title).strong());
                        ui.label(detail.replace("the target row", &format!("Row {}", target_row + 1)));
                        if k == 0 {
                            if text.is_empty() {
                                ui.weak("Nothing typed yet.");
                            } else {
                                match crate::template_math::parse_math(&text) {
                                    Ok(r) => {
                                        let n = crate::template_math::empty_boxes(&r);
                                        ui.colored_label(
                                            Color32::from_rgb(0x2a, 0x6a, 0x20),
                                            format!("✓ Understood:  {}   ({} empty box{})", crate::template_math::describe(&r), n, if n == 1 { "" } else { "es" }),
                                        );
                                    }
                                    Err(e) if e.incomplete => {
                                        ui.weak(format!("… keep typing.  {}", e));
                                    }
                                    Err(e) => {
                                        ui.colored_label(RED, format!("✗ {}", e));
                                    }
                                }
                            }
                        }
                    });
                }
            });
            ui.checkbox(&mut hide, "Don't show this again  (the ? button opens it any time)");
        });
        if hide != self.tpl_hide_guide {
            self.tpl_hide_guide = hide;
            self.tpl_write_file();
        }
        self.tpl_guide = open;
    }

    /// The operator, input name and kind of the selected box.
    fn selected_box_kind(&self) -> (String, String, String) {
        let row = &self.doc.rows[self.doc.target_row.min(self.doc.rows.len() - 1)];
        match row.operator() {
            Some(op) => {
                let _ = op;
                match row.owner_of(&self.doc.target_path) {
                    Some((owner, j)) => {
                        let kind = owner.kinds.get(j).copied().unwrap_or("number").to_string();
                        let name = owner.inputs.get(j).copied().unwrap_or("input").to_string();
                        (owner.name.to_string(), name, kind)
                    }
                    None => (op.name.to_string(), "input".into(), "number".into()),
                }
            }
            None => (String::new(), String::new(), "number".into()),
        }
    }

    fn adv_pick_suggested(&mut self) {
        let (_, _, kind) = self.selected_box_kind();
        self.adv_kind = kind;
        self.adv_msg.clear();
    }

    /// Advanced Input: type what the number pad can't (lists, matrices, functions, sets, graphs) and put it in the selected box.
    fn ui_advanced(&mut self, ctx: &egui::Context) {
        if !self.show_adv {
            return;
        }
        let mut open = true;
        let (opname, boxname, sug) = self.selected_box_kind();
        egui::Window::new("Advanced Input").open(&mut open).default_width(380.0).show(ctx, |ui| {
            if opname.is_empty() {
                ui.colored_label(RED, "No box selected - pick an operator, then click a box in the rows.");
            } else {
                ui.colored_label(
                    Color32::from_rgb(0x10, 0x60, 0x10),
                    format!("Box: {} > {}      suggested: {}", opname, boxname, crate::kinds::kind_title(&sug)),
                );
            }
            ui.horizontal(|ui| {
                ui.label("Search:");
                ui.text_edit_singleline(&mut self.adv_filter);
                if ui.button("✕").clicked() {
                    self.adv_filter.clear();
                }
            });
            let q = self.adv_filter.to_ascii_lowercase();
            egui::ScrollArea::vertical().max_height(150.0).show(ui, |ui| {
                let mut shown = 0;
                for (id, title, how, ex) in crate::kinds::KINDS {
                    if !q.is_empty() && !format!("{title} {how} {ex}").to_ascii_lowercase().contains(&q) {
                        continue;
                    }
                    shown += 1;
                    if ui.selectable_label(self.adv_kind == *id, format!("{title}    e.g.  {ex}")).clicked() {
                        self.adv_kind = id.to_string();
                        self.adv_text.clear();
                        self.adv_msg.clear();
                    }
                }
                if shown == 0 {
                    ui.weak("Nothing matches");
                }
            });
            ui.separator();
            ui.label(RichText::new(format!("Typing: {}", crate::kinds::kind_title(&self.adv_kind))).strong());
            ui.weak(format!("{}   Example: {}", crate::kinds::how_to_type(&self.adv_kind), crate::kinds::example(&self.adv_kind)));
            ui.add(TextEdit::multiline(&mut self.adv_text).desired_rows(4).desired_width(f32::INFINITY).font(egui::TextStyle::Monospace));
            ui.horizontal(|ui| {
                if ui.button(RichText::new("Put in box").strong()).clicked() {
                    self.adv_put_in_box();
                }
                if ui.button("Use example").clicked() {
                    self.adv_text = crate::kinds::example(&self.adv_kind).to_string();
                }
                if ui.button("Clear box").clicked() {
                    self.doc.ensure_target();
                    let (r, b) = (self.doc.target_row, self.doc.target_path.clone());
                    if let Some(slot) = self.doc.rows[r].slot_mut(&b) {
                        slot.clear();
                        self.doc.rows[r].clear_result();
                    }
                    self.adv_text.clear();
                    self.adv_msg.clear();
                }
            });
            if !self.adv_msg.is_empty() {
                ui.label(RichText::new(&self.adv_msg).strong());
            }
        });
        self.show_adv = open;
    }

    fn adv_put_in_box(&mut self) {
        self.doc.ensure_target();
        let (r, b) = (self.doc.target_row, self.doc.target_path.clone());
        if self.doc.rows[r].slot_text(&b).is_none() {
            self.adv_msg = "Click a square box in the rows first.".into();
            return;
        }
        let raw = self.adv_text.trim().to_string();
        match crate::kinds::parse_kind(&self.adv_kind, &raw) {
            Ok(_) => {
                if let Some(slot) = self.doc.rows[r].slot_mut(&b) {
                    *slot = raw;
                }
                self.doc.rows[r].clear_result();
                self.doc.rows[r].error = None;
                self.adv_msg = "Put in the box. Press = on the number pad to calculate.".into();
            }
            Err(e) => self.adv_msg = e,
        }
    }

    fn apply_operator(&mut self, key: &str) {
        self.apply_operator_inner(key);
        // an operator that comes with words for its cards shows the Label / Context boxes, so the words are seen
        if self.doc.rows.iter().any(|r| r.card_words().iter().any(|w| !w.0.is_empty() || !w.1.is_empty())) {
            self.show_card_words = true;
        }
    }

    fn apply_operator_inner(&mut self, key: &str) {
        self.preview_key = Some(key.to_string());
        self.doc.ensure_target();
        if let Some(spec) = crate::multirow::get(key) {
            // an operator that needs more than one row: the rows it needs are added and filled in
            let name = ops::get(key).map_or("This operator", |o| o.name);
            let static_key = ops::get(key).map_or("", |o| o.key);
            match self.doc.apply_template(static_key, spec) {
                Ok(()) => {
                    let steps: Vec<String> = spec.rows.iter().enumerate().map(|(k, r)| format!("Row {}: {}.", k + 1, r.title)).collect();
                    self.status = format!(
                        "{} needs {} rows.\n{}\n{}\nJoined with {}. Fill the boxes in every row, then press =.",
                        name,
                        spec.rows.len(),
                        steps.join("   "),
                        spec.title,
                        spec.joins.join(" ")
                    );
                }
                Err(e) => self.status = e,
            }
            return;
        }
        if let Some(op) = ops::get(key) {
            let nests = self.doc.target_row == 0 && self.doc.rows[0].operator().is_some();
            self.doc.place_operator(op);
            self.status = if nests {
                format!("{} is now inside the selected box of Row 1 — fill the boxes, press =.  {}", op.name, op.formula)
            } else {
                format!("Row {}: {} — fill the boxes, press =.  {}", self.doc.target_row + 1, op.name, op.formula)
            };
        }
    }

    fn ui_rows(&mut self, ui: &mut Ui) {
        ui.horizontal(|ui| {
            ui.heading("Mathematical Addend Sequence");
            ui.checkbox(&mut self.show_card_words, "Label / Context boxes").on_hover_text("Show a Label (Item for a number) box and a Context box under every card, to type words that describe it");
        });
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
                            self.doc.target_path = self.doc.rows[i].first_box();
                        }
                        if !self.doc.rows[i].is_result && self.doc.rows[i].operator().is_some() && ui.small_button("Clear math").clicked() {
                            self.doc.clear_row_math(i);
                            self.doc.template = None;
                        }
                        if let Some(t) = self.doc.template {
                            if let Some(rs) = t.spec.rows.get(i) {
                                ui.weak(rs.title);
                            }
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
                    let target_path = self.doc.target_path.clone();
                    let focused = self.ui_formula(ui, i, is_target, &target_path);
                    if let Some(b) = focused {
                        self.doc.target_row = i;
                        self.doc.target_path = b;
                    }
                });
                ui.add_space(6.0);
            }
        });
    }

    /// One row's math: the operator's picture written as cards on a grid (an operator inside a box is written out in that box).  Fractions are drawn top
    /// to bottom, exponents one line up and subscripts one line down; all of those lines are this ONE row.  The answer is in the card to the right of the
    /// `=`, on the same row.  Returns the path of the input box that was clicked or focused.
    fn ui_formula(&mut self, ui: &mut Ui, i: usize, is_target: bool, target_path: &[usize]) -> Option<Vec<usize>> {
        use crate::layout::{self, CardKind};
        let mut focused = None;
        let cards = self.doc.rows[i].flatten();
        if cards.is_empty() {
            ui.label("(no picture for this operator)");
            return None;
        }
        let words = self.doc.rows[i].card_words();
        let show_card_words = self.show_card_words;
        let mut word_edits: Vec<(usize, String, String)> = Vec::new();
        let pcs: Vec<layout::PC> = cards.iter().map(|c| c.pc()).collect();
        let stack = self.doc.rows[i].op_key.as_deref().map_or(false, layout::stacks);
        let plan = layout::plan_pc(&pcs, stack);
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
        let main_row = cards
            .iter()
            .enumerate()
            .find(|(_, c)| c.level == 0 && c.frac.is_empty())
            .and_then(|(idx, _)| plan.placed[idx])
            .map(|(r, _)| r as usize)
            .unwrap_or(0);

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
                                let card = &cards[idx];
                                let (label, context) = words.get(idx).cloned().unwrap_or_default();
                                let shown = ui.vertical(|ui| {
                                match card.kind {
                                    CardKind::Op => {
                                        ui.label(RichText::new(card.text.as_str()).size(22.0).strong());
                                    }
                                    CardKind::Dec => {
                                        let t = if card.text.is_empty() { "□" } else { card.text.as_str() };
                                        ui.label(RichText::new(t).size(22.0));
                                    }
                                    CardKind::Out => {
                                        // a framed label, so it is exactly as wide as the answer (an answer box is never typed into)
                                        egui::Frame::none()
                                            .stroke(egui::Stroke::new(1.0, Color32::GRAY))
                                            .inner_margin(egui::Margin::same(4.0))
                                            .rounding(3.0)
                                            .show(ui, |ui| {
                                                let t = if card.text.is_empty() { "□".to_string() } else { card.text.clone() };
                                                ui.label(RichText::new(t).size(20.0));
                                            });
                                    }
                                    CardKind::Box => {
                                        let owner = self.doc.rows[i].owner_of(&card.path);
                                        let (name, kind) = match owner {
                                            Some((op, j)) => (op.inputs.get(j).copied().unwrap_or("?"), op.kinds.get(j).copied().unwrap_or("number")),
                                            None => ("?", "number"),
                                        };
                                        if self.doc.rows[i].slot_text(&card.path).is_some() {
                                            ui.vertical(|ui| {
                                                let caption = if kind == "number" { name.to_string() } else { format!("{} ({})", name, kind) };
                                                ui.small(caption);
                                                let width = if kind == "number" { 64.0 } else { 140.0 };
                                                let chain = self.doc.chain_source(i, &card.path); // a box that reads an earlier row's answer
                                                if let Some(text) = self.doc.rows[i].slot_mut(&card.path) {
                                                    let hint = match chain {
                                                        Some(k) => format!("row {}", k + 1),
                                                        None if kind == "number" => String::new(),
                                                        None => crate::kinds::example(kind).to_string(),
                                                    };
                                                    let te = TextEdit::singleline(text)
                                                        .desired_width(width)
                                                        .hint_text(hint)
                                                        .interactive(chain.is_none())
                                                        .font(egui::TextStyle::Heading);
                                                    let resp = ui.add(te);
                                                    if resp.gained_focus() || resp.clicked() {
                                                        focused = Some(card.path.clone());
                                                    }
                                                }
                                                if is_target && card.path == target_path {
                                                    ui.small(RichText::new("◀").color(ORANGE));
                                                }
                                            });
                                        } else {
                                            ui.label(RichText::new("□").size(22.0));
                                        }
                                    }
                                }
                                if show_card_words {
                                    let (mut l, mut c) = (label.clone(), context.clone());
                                    let hint = if card.kind == CardKind::Box { "item" } else { "label" };
                                    let a = ui.add(TextEdit::singleline(&mut l).desired_width(78.0).hint_text(hint).font(egui::TextStyle::Small));
                                    let b = ui.add(TextEdit::singleline(&mut c).desired_width(78.0).hint_text("context").font(egui::TextStyle::Small));
                                    if !l.is_empty() {
                                        a.clone().on_hover_text(l.clone());          // the boxes are narrow: the whole word on hover
                                    }
                                    if !c.is_empty() {
                                        b.clone().on_hover_text(c.clone());
                                    }
                                    if a.changed() || b.changed() {
                                        word_edits.push((idx, l, c));
                                    }
                                }
                                });
                                if !show_card_words && (!label.is_empty() || !context.is_empty()) {
                                    shown.response.on_hover_text(format!("{}\n{}", label, context));
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
        for (idx, l, c) in word_edits {
            self.doc.rows[i].words.insert(idx, (l, c));
        }
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
        ui.label(format!("{} operators loaded.", ops::all_operators().len()));
        
    }

    fn on_key(&mut self, key: &str) {
        match key {
            "±" => {
                self.doc.ensure_target();
                let path = self.doc.target_path.clone();
                let row = &mut self.doc.rows[self.doc.target_row];
                if let Some(s) = row.slot_mut(&path) {
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
