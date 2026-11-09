"""Show one operator's rows.   python operator_row_math/preview.py math/arithmetic/addition"""
import os
import sys
import tkinter as tk
from tkinter import ttk

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operator_row_math import get  # noqa: E402


def main(key):
    op = get(key)
    root = tk.Tk()
    root.title("Operator row: " + op.NAME)
    root.geometry("1500x420")
    root.configure(bg="#fffbe6")
    canvas = tk.Canvas(root, bg="#fffbe6", highlightthickness=0)
    hbar = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
    canvas.configure(xscrollcommand=hbar.set)
    hbar.pack(side="bottom", fill="x")
    canvas.pack(fill="both", expand=True)
    inner = tk.Frame(canvas, bg="#fffbe6")
    canvas.create_window((0, 0), window=inner, anchor="nw")
    tk.Label(inner, text=op.NAME + "      " + op.PATTERN, bg="#fffbe6",
             font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=10, pady=6)
    tk.Label(inner, text="Full row", bg="#fffbe6", fg="#2a6a20", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=10)
    op.place(inner).pack(anchor="w", padx=10)
    tk.Label(inner, text="Stacked row (operator only; operands come from the rows above)", bg="#fffbe6",
             fg="#2a6a20", font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=10, pady=(10, 0))
    op.place(inner, stacked=True).pack(anchor="w", padx=10)
    inner.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    root.mainloop()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "math/arithmetic/addition")
