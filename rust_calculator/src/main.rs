//! Desktop calculator (Rust port of the Python Tkinter app).
//!
//! Phase 1: operator rows, number pad, Operators browser, ready compute for a
//! core library. Same program as `main.py`, built toward full parity.

use rust_calculator::app::CalculatorApp;

fn main() -> eframe::Result<()> {
    let options = eframe::NativeOptions {
        viewport: egui::ViewportBuilder::default()
            .with_inner_size([1280.0, 800.0])
            .with_title("Rust Calculator — Smart Token Expression Builder"),
        ..Default::default()
    };
    eframe::run_native(
        "Rust Calculator",
        options,
        Box::new(|_cc| Ok(Box::new(CalculatorApp::default()))),
    )
}
