//! Desktop calculator (Rust port of the Python Tkinter app).
//!
//! Phase 1: operator rows, number pad, Operators browser, ready compute for a
//! core library. Same program as `main.py`, built toward full parity.

use rust_calculator::app::CalculatorApp;

fn main() -> eframe::Result<()> {
    let options = eframe::NativeOptions {
        viewport: egui::ViewportBuilder::default()
            .with_inner_size([1280.0, 680.0])
            .with_title("Rust Calculator — Smart Token Expression Builder"),
        ..Default::default()
    };
    eframe::run_native(
        "Rust Calculator",
        options,
        Box::new(|cc| {
            egui_extras::install_image_loaders(&cc.egui_ctx);
            // `--demo <operator key> <numbers...>` opens with that operator in Row 1, filled in and calculated
            let args: Vec<String> = std::env::args().skip(1).collect();
            if args.first().map(|a| a == "--demo").unwrap_or(false) && args.len() >= 2 {
                return Ok(Box::new(CalculatorApp::with_demo(&args[1], &args[2..])));
            }
            Ok(Box::new(CalculatorApp::default()))
        }),
    )
}
