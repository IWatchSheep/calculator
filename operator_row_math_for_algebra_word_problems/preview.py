"""Show one algebra word problem's row.   python operator_row_math_for_algebra_word_problems/preview.py savings/0848"""
import os
import sys
import tkinter as tk
from tkinter import ttk

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operator_row_math_for_algebra_word_problems import get  # noqa: E402


def main(key):
    op = get(key)
    root = tk.Tk()
    root.title("Algebra word problem row: " + op.NAME)
    root.geometry("1500x420")
    root.configure(bg="#fffbe6")
    canvas = tk.Canvas(root, bg="#fffbe6", highlightthickness=0)
    hbar = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
    canvas.configure(xscrollcommand=hbar.set)
    hbar.pack(side="bottom", fill="x")
    canvas.pack(fill="both", expand=True)
    inner = tk.Frame(canvas, bg="#fffbe6")
    canvas.create_window((0, 0), window=inner, anchor="nw")
    tk.Label(inner, text=op.NAME + "      " + op.PATTERN + "      (" + op.CALC + ")", bg="#fffbe6", font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=10, pady=6)
    tk.Label(inner, text="Numbers in the stored problem: " + ", ".join(op.DEFAULTS), bg="#fffbe6", fg="#2a6a20", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=10)
    op.place(inner).pack(anchor="w", padx=10)
    inner.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    root.mainloop()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "savings/0848")
