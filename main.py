import os
import tkinter as tk
from tkinter import ttk

from operator_links import LINKS

try:
    from PIL import Image, ImageTk
except ImportError:          # pictures need Pillow (pip install pillow)
    Image = ImageTk = None

OPS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "operators_one_operator_per_file")
WORD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "operators_one_algebra_word_problem_per_file")

from gui_style import (ARROWS, ARROW_BG, BLUE, CREAM, GREEN, ORANGE, PALE_BLUE, PALE_ORANGE,  # noqa: F401
                       PURPLE, RED, btn, main_row_position, main_row_positions,
                       configure_excel_workspace_grid, excel_total_workspace_width,
                       excel_start_row, excel_heading_row, excel_workspace_position,
                       excel_workspace_positions, EXCEL_COL_ROW_LABEL, EXCEL_COL_ACTIONS,
                       GridPosition, LayoutRegion, EXCEL_13COL_COLUMN_WIDTHS,
                       excel_13col_total_row_positions, excel_13col_start_row,
                       EXCEL_13COL_RESULT_EQUALS, EXCEL_13COL_RESULT_BOX, EXCEL_13COL_EFFECTIVE_DEFAULT_WIDTHS,
                       EXCEL_17COL_COLUMN_WIDTHS, EXCEL_17COL_EFFECTIVE_DEFAULT_WIDTHS,
                       excel_17col_start_row, excel_17col_workspace_position,
                       excel_17col_workspace_positions, excel_17col_total_row_positions,
                       EXCEL_17COL_ROW_LABEL, EXCEL_17COL_MATH_SIGN, EXCEL_17COL_NUMBER_MATH,
                       EXCEL_17COL_MATH_BOX1, EXCEL_17COL_MATH_TRAILING, EXCEL_17COL_ACTIONS,
                       EXCEL_17COL_RESULT_EQUALS, EXCEL_17COL_PAREN_OPEN, EXCEL_17COL_RESULT_BOX,
                       EXCEL_17COL_EXPONENT_1, EXCEL_17COL_PAREN_CLOSE, EXCEL_17COL_EXPONENT_2,
                       EXCEL_17COL_RESULT_BOX1, EXCEL_17COL_RESULT_TRAILING)
import operator_row_math
import operators_one_operator_per_file as operators_library
from operator_row_math.row_builder import build_row, make_component, DescriptionRegion
from operator_row_math import advanced_input, multirow_specs, row_tree, template_math


MATH_OPS = [
    "## Arithmetic",
    "+   Addition", "−   Subtraction", "×   Multiplication", "÷   Division", "%   Modulo",
    "a/b   Fraction", "|x|   Absolute value", "±   Negate", "1/x   Reciprocal",
    "floor   Round down", "ceil   Round up", "round   Round nearest", "min   Minimum", "max   Maximum",
    "## Algebra",
    "^   Power", "x²   Square", "x³   Cube", "√   Square root", "ⁿ√   Nth root", "∛   Cube root",
    "eˣ   Exponential", "10ˣ   Power of ten", "log   Log base 10", "ln   Natural log",
    "logₐ   Log any base", "Quadratic formula   (−b±√(b²−4ac))/2a", "Discriminant   b²−4ac",
    "Factor", "Expand", "Simplify", "Solve for x", "Solve system of equations",
    "Binomial theorem   (a+b)ⁿ", "Difference of squares   a²−b²", "Slope-intercept   y = mx + b",
    "Arithmetic sequence   aₙ = a₁+(n−1)d", "Geometric sequence   aₙ = a₁rⁿ⁻¹",
    "Arithmetic series sum", "Geometric series sum", "Complex number   a + bi",
    "i   Imaginary unit", "Modulus of complex   |z|", "Conjugate   z̄",
    "## Trigonometry",
    "sin", "cos", "tan", "csc", "sec", "cot",
    "asin   Inverse sine", "acos   Inverse cosine", "atan   Inverse tangent", "atan2",
    "sinh", "cosh", "tanh", "asinh", "acosh", "atanh",
    "sin²θ + cos²θ = 1", "Double angle   sin2θ", "Half angle", "Sum of angles   sin(a+b)",
    "Degrees → radians", "Radians → degrees",
    "## Calculus",
    "lim   Limit", "d/dx   Derivative", "∂/∂x   Partial derivative", "∂²/∂xᵢ²   Second partial derivative", "d²/dx²   Second derivative",
    "∫   Indefinite integral", "∫ₐᵇ   Definite integral", "∬   Double integral", "∭   Triple integral",
    "∮   Line integral", "∇   Gradient", "∇·   Divergence", "∇×   Curl", "Δ   Laplacian",
    "Chain rule", "Product rule", "Quotient rule", "L'Hôpital's rule",
    "Taylor series", "Maclaurin series", "Σ   Summation", "∏   Product", "∞   Infinity",
    "dy/dx = f(x,y)   Differential equation",
    "## Linear algebra",
    "Matrix add", "Matrix subtract", "Matrix multiply", "Scalar multiply", "Transpose   Aᵀ",
    "Determinant   det(A)", "Inverse   A⁻¹", "Trace   tr(A)", "Rank", "Identity matrix   I",
    "Row reduce   RREF", "Eigenvalues   λ", "Eigenvectors", "Characteristic polynomial",
    "Dot product   a·b", "Cross product   a×b", "Vector magnitude   ‖v‖", "Unit vector",
    "Projection", "Norm", "Null space", "Column space", "LU decomposition", "QR decomposition",
    "SVD   Singular value decomposition", "Solve Ax = b",
    "## Statistics & probability",
    "mean   Average", "median   Median", "mode   Mode", "range", "variance   σ²", "std dev   σ",
    "sample variance   s²", "sample std dev   s", "z-score", "covariance", "correlation   r",
    "linear regression", "Quartiles   Q1 Q3", "IQR", "Percentile",
    "P(A)   Probability", "P(A|B)   Conditional probability", "Bayes' theorem",
    "E[X]   Expected value", "Var(X)", "Normal distribution", "Binomial distribution",
    "Poisson distribution", "Uniform distribution", "Exponential distribution",
    "Confidence interval", "t-test", "Chi-square", "p-value",
    "## Discrete & number theory",
    "n!   Factorial", "nCr   Combinations", "nPr   Permutations", "gcd   Greatest common divisor",
    "lcm   Least common multiple", "mod   Modular arithmetic", "Prime check", "Prime factorization",
    "Fibonacci", "Euler's totient   φ(n)", "Pigeonhole", "Inclusion–exclusion",
    "## Logic & sets",
    "∧   AND", "∨   OR", "¬   NOT", "⊕   XOR", "→   Implies", "↔   If and only if",
    "∀   For all", "∃   There exists", "∈   Element of", "∉   Not element of",
    "⊂   Subset", "⊆   Subset or equal", "∪   Union", "∩   Intersection", "∅   Empty set",
    "A − B   Set difference", "Aᶜ   Complement", "|A|   Cardinality",
    "## Abstract algebra",
    "Group   (G, ∘)", "Subgroup   H ≤ G", "Normal subgroup   N ◁ G", "Quotient group   G/N",
    "Order of group   |G|", "Order of element", "Cyclic group   ⟨g⟩", "Cosets   gH",
    "Homomorphism   φ: G → H", "Isomorphism   ≅", "Kernel   ker φ", "Image   im φ",
    "Direct product   G × H", "Symmetric group   Sₙ", "Alternating group   Aₙ",
    "Ring", "Ideal", "Field", "Integral domain", "Polynomial ring   R[x]",
    "Field extension   K/F", "Galois group", "Module", "Vector space", "Basis", "Dimension",
    "Tensor product   ⊗", "Direct sum   ⊕",
    "## Topology",
    "Open set", "Closed set", "Closure   Ā", "Interior   A°", "Boundary   ∂A",
    "Neighborhood", "Basis of topology", "Subspace topology", "Product topology",
    "Continuous map", "Homeomorphism", "Compact", "Connected", "Path-connected",
    "Hausdorff", "Metric space   d(x,y)", "Open ball   B(x,r)", "Cauchy sequence",
    "Complete space", "Fundamental group   π₁", "Homology   Hₙ", "Cohomology   Hⁿ",
    "Euler characteristic   χ", "Homotopy   ≃", "Covering space", "Manifold",
    "## Real analysis",
    "sup   Supremum", "inf   Infimum", "lim sup", "lim inf", "Convergence   →",
    "Uniform convergence", "Series convergence test", "Ratio test", "Root test",
    "Comparison test", "Integral test", "Alternating series test", "Radius of convergence",
    "Continuity   ε–δ", "Uniform continuity", "Lipschitz", "Mean value theorem",
    "Intermediate value theorem", "Riemann sum", "Riemann–Stieltjes integral",
    "Measure   μ", "Lebesgue integral", "σ-algebra", "Outer measure", "Almost everywhere   a.e.",
    "Lᵖ norm", "Banach space", "Hilbert space", "Inner product   ⟨x,y⟩",
    "## Complex analysis",
    "Re(z)   Real part", "Im(z)   Imaginary part", "arg(z)   Argument", "Euler's formula   e^(iθ)",
    "De Moivre's theorem", "Cauchy–Riemann equations", "Analytic function", "Contour integral",
    "Residue", "Residue theorem", "Laurent series", "Cauchy integral formula",
    "Möbius transformation", "Conformal map", "Branch cut",
    "## Transforms & differential equations",
    "Fourier transform   F{f}", "Inverse Fourier transform", "Fourier series",
    "Laplace transform   L{f}", "Inverse Laplace transform", "Z-transform",
    "Convolution   f ∗ g", "Dirac delta   δ(x)", "Heaviside step   H(x)",
    "First-order ODE", "Second-order ODE", "Separable equation", "Integrating factor",
    "Characteristic equation", "Wronskian", "Variation of parameters", "Power series solution",
    "PDE   Partial differential equation", "Heat equation", "Wave equation", "Laplace's equation",
    "## Graph theory & combinatorics",
    "Graph   G = (V, E)", "Degree   deg(v)", "Path", "Cycle", "Tree", "Spanning tree",
    "Adjacency matrix", "Shortest path", "Chromatic number   χ(G)", "Planar graph",
    "Euler path", "Hamiltonian path", "Bipartite", "Max flow / min cut",
    "Catalan number", "Stirling number", "Bell number", "Partition   p(n)",
    "Generating function", "Recurrence relation", "Burnside's lemma",
    "## Optimization & numerical methods",
    "Minimize", "Maximize", "Lagrange multipliers   λ", "Gradient descent", "Hessian",
    "Linear programming", "Simplex method", "Convex function", "KKT conditions",
    "Newton's method", "Bisection method", "Secant method", "Fixed-point iteration",
    "Euler's method", "Runge–Kutta", "Trapezoid rule", "Simpson's rule",
    "Lagrange interpolation", "Newton interpolation", "Spline", "Least squares",
    "Gaussian elimination", "Jacobi iteration", "Gauss–Seidel",
    "## Differential geometry & tensors",
    "Tangent vector", "Tangent space", "Differential form   ω", "Exterior derivative   d",
    "Wedge product   ∧", "Pullback   f*", "Metric tensor   g", "Christoffel symbol   Γ",
    "Riemann curvature   R", "Ricci tensor", "Gaussian curvature   K", "Geodesic",
    "Lie derivative", "Lie bracket   [X,Y]", "Stokes' theorem", "Tensor contraction",
    "## Category theory & foundations",
    "Category", "Functor", "Natural transformation", "Morphism   f: A → B",
    "Product / coproduct", "Limit / colimit", "Adjunction",
    "Cardinal   ℵ₀", "Ordinal   ω", "Axiom of choice", "Zorn's lemma", "Power set   𝒫(A)",
    "Cartesian product   A × B", "Function   f: A → B", "Injective", "Surjective", "Bijective",
    "ℕ   Naturals", "ℤ   Integers", "ℚ   Rationals", "ℝ   Reals", "ℂ   Complex", "ℍ   Quaternions",
    "## Constants & relations",
    "π   Pi", "e   Euler's number", "φ   Golden ratio", "γ   Euler–Mascheroni",
    "=   Equals", "≠   Not equal", "≈   Approximately", "<   Less than", ">   Greater than",
    "≤   Less or equal", "≥   Greater or equal", "∝   Proportional to",
    "(   Open bracket", ")   Close bracket", "[ ]   Brackets", "{ }   Braces",
]

GEOMETRY_OPS = [
    "Circle area   πr²", "Circle circumference   2πr", "Arc length   rθ", "Sector area   ½r²θ",
    "Rectangle area   l×w", "Rectangle perimeter   2(l+w)", "Square area   s²",
    "Triangle area   ½bh", "Heron's formula   √(s(s−a)(s−b)(s−c))",
    "Pythagorean theorem   a²+b²=c²", "Parallelogram area   bh", "Trapezoid area   ½(a+b)h",
    "Rhombus area   ½d₁d₂", "Regular polygon area   ½·p·a",
    "Polygon interior angle sum   (n−2)×180°",
    "Cube volume   s³", "Cube surface area   6s²", "Rectangular prism volume   lwh",
    "Rectangular prism surface area   2(lw+lh+wh)", "Cylinder volume   πr²h",
    "Cylinder surface area   2πr(r+h)", "Cone volume   ⅓πr²h", "Cone surface area   πr(r+l)",
    "Sphere volume   ⁴⁄₃πr³", "Sphere surface area   4πr²", "Pyramid volume   ⅓Bh",
    "Distance formula   √((x₂−x₁)²+(y₂−y₁)²)", "Midpoint formula", "Slope   (y₂−y₁)/(x₂−x₁)",
    "Law of sines   a/sinA = b/sinB", "Law of cosines   c²=a²+b²−2ab·cosC",
    "Degrees → radians", "Radians → degrees",
]

PHYSICS_OPS = [
    "## Mechanics, heat, waves and electricity",
    "Velocity   v = d/t", "Acceleration   a = Δv/t", "Final velocity   v = u + at",
    "Displacement   s = ut + ½at²", "Velocity²   v² = u² + 2as",
    "Newton's 2nd law   F = ma", "Weight   W = mg", "Momentum   p = mv", "Impulse   J = FΔt",
    "Work   W = Fd", "Power   P = W/t", "Kinetic energy   ½mv²", "Potential energy   mgh",
    "Pressure   P = F/A", "Density   ρ = m/V", "Hooke's law   F = −kx",
    "Gravitation   F = G·m₁m₂/r²", "Centripetal acceleration   a = v²/r",
    "Torque   τ = rF·sinθ", "Pendulum period   T = 2π√(L/g)",
    "Frequency   f = 1/T", "Wave speed   v = fλ", "Snell's law   n₁sinθ₁ = n₂sinθ₂",
    "Heat   Q = mcΔT", "Ideal gas law   PV = nRT", "Mass-energy   E = mc²",
    "Ohm's law   V = IR", "Electric power   P = IV", "Coulomb's law   F = k·q₁q₂/r²",
    "Capacitance   Q = CV", "Resistors in series   R₁+R₂", "Resistors in parallel   1/R = 1/R₁+1/R₂",
    "## Magnetism",
    "Magnetic force on a moving charge   F = qvB sin θ",
    "Magnetic force on a current-carrying wire   F = BIL sin θ",
    "Magnetic field of a straight wire   B = μ₀I/2πr",
    "Magnetic field inside a solenoid   B = μ₀nI",
    "Magnetic flux   Φ = BA cos θ",
    "Faraday's law of induction   ε = −N ΔΦ/Δt",
    "Self-induced emf of an inductor   ε = −L ΔI/Δt",
    "Energy stored in an inductor   U = ½LI²",
    "Cyclotron radius of a charged particle   r = mv/(|q|B)",
    "Motional emf   ε = BLv",
    "## Fluid dynamics",
    "Buoyant force (Archimedes' principle)   F = ρgV",
    "Hydrostatic pressure   P = ρgh",
    "Continuity equation   A₁v₁ = A₂v₂",
    "Bernoulli's equation   P + ½ρv² + ρgh = const",
    "Reynolds number   Re = ρvL/μ",
    "Navier–Stokes equation   ρ(∂u/∂t + (u·∇)u) = −∇p + μ∇²u + f",
    "Poiseuille's law (flow in a pipe)   Q = πr⁴ΔP/8μL",
    "Torricelli's law   v = √(2gh)",
    "Stokes' drag force   F = 6πμrv",
    "Volume flow rate   Q = Av",
    "Hydraulic press (Pascal's principle)   F₂ = F₁A₂/A₁",
    "## Quantum mechanics",
    "Photon energy (Planck's relation)   E = hf",
    "Photon momentum   p = h/λ",
    "de Broglie wavelength   λ = h/mv",
    "Heisenberg uncertainty principle   Δx·Δp ≥ ħ/2",
    "Photoelectric effect   K = hf − φ",
    "Bohr energy level (hydrogen-like atom)   Eₙ = −13.6 Z²/n² eV",
    "Rydberg formula   1/λ = RZ²(1/n₁² − 1/n₂²)",
    "Particle in a box (energy levels)   Eₙ = n²h²/8mL²",
    "Quantum harmonic oscillator   Eₙ = ħω(n + ½)",
    "Compton wavelength shift   Δλ = (h/mc)(1 − cos θ)",
    "## Optics",
    "Thin lens equation   1/f = 1/dₒ + 1/dᵢ",
    "Lens magnification   m = −dᵢ/dₒ",
    "Lensmaker's equation   1/f = (n−1)(1/R₁ − 1/R₂)",
    "Critical angle (total internal reflection)   θc = arcsin(n₂/n₁)",
    "Brewster's angle   θB = arctan(n₂/n₁)",
    "Double-slit fringe spacing   Δy = λL/d",
    "Diffraction grating   d sin θ = mλ",
    "Malus's law   I = I₀cos²θ",
    "Refractive index   n = c/v",
    "## Relativity",
    "Lorentz factor   γ = 1/√(1 − v²/c²)",
    "Time dilation   Δt = γΔt₀",
    "Length contraction   L = L₀/γ",
    "Relativistic momentum   p = γmv",
    "Relativistic kinetic energy   K = (γ − 1)mc²",
    "Energy-momentum relation   E² = (pc)² + (mc²)²",
    "Relativistic velocity addition   u′ = (u + v)/(1 + uv/c²)",
    "Relativistic Doppler effect   f = f₀√((1−β)/(1+β))",
    "Schwarzschild radius   rₛ = 2GM/c²",
    "Gravitational time dilation   Δt₀ = Δt√(1 − rₛ/r)",
]


def operator_keys(key):
    """Button(s) needed to make an operator's math work, e.g. ["+"] for addition."""
    sym = ""
    try:
        sym = str(operators_library.get(key).SYMBOL).strip()
    except Exception:
        pass
    if sym and len(sym) <= 8 and " " not in sym:
        return [sym]
    out = []
    for kind, text in operator_row_math.get(key).LEFT:
        if kind == "op" and text not in out:
            out.append(text)
    return out[:5] or [sym or "?"]


def _copy_node(node):
    """A copy of a row's operator tree (the operator modules themselves are shared, not copied)."""
    if not isinstance(node, dict) or "mod" not in node:
        return dict(node) if isinstance(node, dict) else node
    out = dict(node)
    out["slots"] = [_copy_node(slot) for slot in node["slots"]]
    return out


class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Token Addition Calculator (Math Templates & Central Input)")
        self.geometry("1700x850")
        self.configure(bg="#f0f4f4")
        self._build_toolbar()
        self._build_target_bar()
        self._build_rows_area()
        self._build_results()
        self._build_bottom()
        self._setup_keyboard_handling()
        self.focus_set()
        self.update_idletasks()      # tall enough for the keypad, join keys and Advanced Input button
        self.geometry("1700x%d" % min(max(850, self.winfo_reqheight()), self.winfo_screenheight() - 70))

    def _setup_keyboard_handling(self):
        """Bind physical keyboard input to drive the calculator keypad and mathematical operations."""
        self.bind("<Key>", self._on_key_press)
        self.bind_all("<Key>", self._on_key_press)

    def _on_key_press(self, event):
        """Handle physical keyboard presses for digits, operators, and evaluation.

        When focus is inside an editable text box (such as a descriptive Entry field),
        do not intercept so normal typing (including punctuation, math symbols, and spaces)
        and auto-expansion proceed undisturbed.
        """
        w = event.widget
        focused = self.focus_get()

        ks = event.keysym
        ch = event.char

        # Check if focus or event widget is one of the exponent boxes
        is_exponent_entry = False
        for r in self.rows:
            if w in (r.get("exponent_1_box"), r.get("exponent_2_box")) or focused in (r.get("exponent_1_box"), r.get("exponent_2_box")):
                is_exponent_entry = True
                break

        if is_exponent_entry:
            if ch == "=" or ks in ("equal", "KP_Equal", "Return", "KP_Enter"):
                self._equals()
                return "break"
            if ks in ("Escape",):
                self._clear_all()
                return "break"
            return None

        # If focus or target widget is another Entry or Text widget, preserve natural text editing
        if (isinstance(w, (tk.Entry, tk.Text, ttk.Combobox, ttk.Entry)) or
            (hasattr(w, "winfo_class") and w.winfo_class() in ("Entry", "Text", "TEntry", "TCombobox")) or
            (focused is not None and focused != self and hasattr(focused, "winfo_class") and focused.winfo_class() in ("Entry", "Text", "TEntry", "TCombobox"))):
            if ks in ("Return", "KP_Enter"):
                self._equals()
                return "break"
            return None

        ks = event.keysym
        ch = event.char

        # Digits 0..9
        if ks in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                  "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9") or (ch and ch in "0123456789"):
            digit = ch if (ch and ch in "0123456789") else (ks[-1] if ks.startswith("KP_") else ks)
            self._key(digit)
            return "break"

        # Decimal point
        elif ks in ("period", "KP_Decimal") or ch == ".":
            self._key(".")
            return "break"

        # Mathematical operations:
        # Addition / next-row progression
        elif ch == "+" or ks in ("plus", "KP_Add"):
            self._join_key("+")
            return "break"

        # Subtraction / next-row progression
        elif ch in ("-", "−") or ks in ("minus", "KP_Subtract"):
            self._join_key("−")
            return "break"

        # Multiplication / next-row progression
        elif ch in ("*", "×") or ks in ("asterisk", "KP_Multiply"):
            self._join_key("×")
            return "break"

        # Division / next-row progression
        elif ch in ("/", "÷") or ks in ("slash", "KP_Divide"):
            self._join_key("÷")
            return "break"

        # Equals / Evaluation
        elif ch == "=" or ks in ("equal", "KP_Equal"):
            self._equals()
            return "break"

        elif ks in ("Return", "KP_Enter"):
            self._equals()
            return "break"

        # Backspace
        elif ks in ("BackSpace",):
            self._key("⌫")
            return "break"

        # Escape: clear/cancel
        elif ks in ("Escape",):
            self._clear_all()
            return "break"

        return None

    # ---------- top ----------
    def _build_toolbar(self):
        bar = tk.Frame(self, bg="#f0f4f4")
        bar.pack(fill="x", padx=8, pady=(8, 4))
        tk.Label(bar, text="Smart Token Expression Builder (Math Templates)",
                 font=("Segoe UI", 10, "bold"), bg="#f0f4f4").pack(side="left", padx=(8, 12))
        btn(bar, "Clear (C)", RED, command=self._clear_all).pack(side="left", padx=3)
        btn(bar, "Next Row (↓)", GREEN, command=lambda: self._next_row()).pack(side="left", padx=3)

    def _build_target_bar(self):
        f = tk.Frame(self, bg="white", highlightbackground="#c0c0c0", highlightthickness=1)
        f.pack(fill="x", padx=8, pady=2)
        self.target_label = tk.Label(f, text="Selected Target: Row 1 | Addend 1 | Col 1: Number ('o')",
                                     fg="#d05010", bg="white", font=("Segoe UI", 8, "bold"))
        self.target_label.pack(anchor="w", padx=4, pady=3)

    # ---------- rows area ----------
    def _component(self, parent, center, kind, lead="+", on_pick=None, card_slot=None, calc_row=1, **kwargs):
        """kind: 'number' or 'helper'. Blue + | 3x3 arrows | Item/Label | Context | orange +"""
        return make_component(parent, center, kind, lead, on_pick=on_pick, card_slot=card_slot, calc_row=calc_row, **kwargs)

    def _build_rows_area(self):
        header = tk.Frame(self, bg="#e4e4e4")
        header.pack(fill="x", padx=8, pady=(6, 0))
        tk.Label(header, text="Row", font=("Segoe UI", 8, "bold"), bg="#e4e4e4").pack(side="left", padx=(8, 70))
        tk.Label(header, text="Mathematical Addend Sequence (each number owns its Item, Context and extra fields)",
                 font=("Segoe UI", 8, "bold"), bg="#e4e4e4").pack(side="left")

        # scrollable rows section (vertical + horizontal) so wide operator math always fits
        holder = tk.Frame(self, bg=CREAM, highlightbackground="black", highlightthickness=2)
        holder.pack(fill="x", padx=8)
        self.rows_canvas = rc = tk.Canvas(holder, bg=CREAM, height=290, highlightthickness=0)
        rvbar = ttk.Scrollbar(holder, orient="vertical", command=rc.yview)
        rhbar = ttk.Scrollbar(holder, orient="horizontal", command=rc.xview)
        rc.configure(xscrollcommand=rhbar.set, yscrollcommand=rvbar.set)
        rvbar.pack(side="right", fill="y")
        rhbar.pack(side="bottom", fill="x")
        rc.pack(side="left", fill="both", expand=True)

        # Step 4: The 33-column x 9-row Excel workspace is the primary active workspace!
        excel_area = tk.Frame(rc, bg=CREAM)
        configure_excel_workspace_grid(excel_area, num_calc_rows=2)
        win = rc.create_window((0, 0), window=excel_area, anchor="nw")
        self._rows_win = win
        self.excel_area = excel_area
        self.excel_workspace = excel_area
        self.area = excel_area

        def fit(_e=None):
            active_area = self.area
            active_area.update_idletasks()
            max_row_w = 0
            for r_data in getattr(self, "rows", []):
                rf = r_data.get("row_frame")
                if rf:
                    rf.update_idletasks()
                    max_row_w = max(max_row_w, rf.winfo_reqwidth())
            w = max(rc.winfo_width(), active_area.winfo_reqwidth(), max_row_w)
            rc.itemconfigure(self._rows_win, width=w)
            rc.configure(scrollregion=(0, 0, w, active_area.winfo_reqheight()))
        rc.bind("<Configure>", fit)
        self._fit_rows = fit

        def wheel(e):
            w = self.winfo_containing(e.x_root, e.y_root)
            while w is not None and w is not rc:
                w = w.master
            if w is rc:
                if e.state & 0x1:
                    rc.xview_scroll(-1 * (e.delta // 120), "units")
                else:
                    rc.yview_scroll(-1 * (e.delta // 120), "units")
        self.bind("<MouseWheel>", wheel, add="+")

        self.rows = []
        self.op_target = 0
        self.template = None          # the multi-row operator currently laid out (see multirow_specs.py)
        for _ in range(1):
            self._add_row()
        self._select_only(0, (0,))                 # Row 1's box is ready for the number pad
        self._render_row(0)

    def activate_excel_workspace(self):
        """Step 4 migration hook: ensure canvas viewport displays the 33-column Excel grid."""
        if self._rows_win and hasattr(self, "excel_area"):
            self.rows_canvas.itemconfigure(self._rows_win, window=self.excel_area)
            self.area = self.excel_area
            self._fit_rows()

    def _toggle_paren_open(self, r):
        """Toggle active/inactive state of Open Parenthesis '(' in row r."""
        if r < 0 or r >= len(self.rows):
            return
        row = self.rows[r]
        row["paren_open"] = not row.get("paren_open", False)
        b = row.get("paren_open_btn")
        if b is not None:
            if row["paren_open"]:
                b.configure(bg="#b5dca8", fg="#1b5e20", relief="sunken")
            else:
                b.configure(bg="white", fg="black", relief="raised")

    def _on_exponent_focus(self, box):
        """Track which exponent box was clicked or focused, so on-screen number pad routes to it."""
        self._active_exponent_box = box

    def _toggle_paren_close(self, r):
        """Toggle active/inactive state of Close Parenthesis ')' in row r."""
        if r < 0 or r >= len(self.rows):
            return
        row = self.rows[r]
        row["paren_close"] = not row.get("paren_close", False)
        b = row.get("paren_close_btn")
        if b is not None:
            if row["paren_close"]:
                b.configure(bg="#b5dca8", fg="#1b5e20", relief="sunken")
            else:
                b.configure(bg="white", fg="black", relief="raised")

    def _has_active_17col_controls(self):
        """Check if any row currently has parentheses toggled or exponents entered."""
        for row in self.rows:
            if row.get("is_result"):
                continue
            if row.get("paren_open"):
                return True
            if row.get("paren_close"):
                return True
            exp1 = row.get("exponent_1_box")
            if exp1 is not None and exp1.get().strip():
                return True
            exp2 = row.get("exponent_2_box")
            if exp2 is not None and exp2.get().strip():
                return True
        return False

    def _has_unsupported_pemdas_controls(self):
        """In Step 3B, parentheses and Exponent Box 2 (group exponent) are fully active."""
        return False

    @staticmethod
    def _parse_exponent_value(s):
        """Parse text from Exponent Box 1 (Column M).
        Supports:
          - Integers: '3', '0', '-2'
          - Floats: '0.5', '-1.5'
          - Fractions: '1/2', '1/3', '-1/4'
        Returns int or float, or None if string is empty.
        Raises ValueError on invalid syntax or division by zero.
        """
        if s is None:
            return None
        text = str(s).strip()
        if not text:
            return None
        try:
            return int(text)
        except ValueError:
            pass
        try:
            return float(text)
        except ValueError:
            pass
        if "/" in text:
            parts = text.split("/")
            if len(parts) == 2:
                try:
                    num = float(parts[0].strip())
                    den = float(parts[1].strip())
                    if den == 0:
                        raise ValueError("Division by zero in exponent.")
                    val = num / den
                    if val.is_integer() and abs(val) < 1e15:
                        return int(val)
                    return val
                except ValueError as e:
                    if "Division by zero" in str(e):
                        raise
                    pass
        raise ValueError("Invalid exponent '%s'." % text)

    @staticmethod
    def _apply_exponent(base, exp):
        """Raise base to power exp.
        Supports int, float, complex base.
        Raises ValueError on zero division, overflow, or math domain errors.
        """
        if exp is None:
            return base
        if isinstance(base, (list, tuple, set, dict)):
            raise ValueError("Cannot apply exponent to structured data.")
        try:
            if isinstance(base, (int, float)) and base < 0 and isinstance(exp, float):
                recip = 1.0 / exp
                if abs(recip - round(recip)) < 1e-9 and int(round(recip)) % 2 == 1:
                    res = -((-base) ** exp)
                    if isinstance(res, float) and abs(res - round(res)) < 1e-12 and abs(res) < 1e15:
                        return int(round(res))
                    return res
            res = base ** exp
            if isinstance(res, complex) and abs(res.imag) < 1e-12:
                res = res.real
            if isinstance(res, float) and abs(res - round(res)) < 1e-12 and abs(res) < 1e15:
                res = int(round(res))
            return res
        except ZeroDivisionError:
            raise ValueError("Division by zero.")
        except OverflowError:
            raise ValueError("Exponent calculation overflow.")
        except Exception as e:
            raise ValueError("Cannot calculate power: %s" % e)

    def _get_exponent_1(self, r):
        if r < 0 or r >= len(self.rows):
            return ""
        box = self.rows[r].get("exponent_1_box")
        return box.get().strip() if box is not None else ""

    def _set_exponent_1(self, r, text):
        if r < 0 or r >= len(self.rows):
            return
        box = self.rows[r].get("exponent_1_box")
        if box is not None:
            box.delete(0, tk.END)
            box.insert(0, str(text))

    def _get_exponent_2(self, r):
        if r < 0 or r >= len(self.rows):
            return ""
        box = self.rows[r].get("exponent_2_box")
        return box.get().strip() if box is not None else ""

    def _set_exponent_2(self, r, text):
        if r < 0 or r >= len(self.rows):
            return
        box = self.rows[r].get("exponent_2_box")
        if box is not None:
            box.delete(0, tk.END)
            box.insert(0, str(text))

    def _add_row(self):
        """Add one more calculator row at the bottom using authoritative 17-column Excel coordinates in its own grid."""
        area, r = self.area, len(self.rows)
        k = r + 1
        r0 = excel_17col_start_row(k)

        # Create independent grid container for this calculator row
        row_frame = tk.Frame(area, bg=CREAM)
        row_frame.grid(row=r, column=0, sticky="nw", padx=0, pady=(2, 6))

        # Configure 17 columns with authoritative default widths
        for col_1based, width in EXCEL_17COL_COLUMN_WIDTHS.items():
            row_frame.grid_columnconfigure(col_1based - 1, minsize=width, weight=0)

        # Configure 3 sub-rows (row 0: top actions/exponents, row 1: main controls, row 2: bottom actions)
        row_frame.grid_rowconfigure(0, minsize=26, weight=0)
        row_frame.grid_rowconfigure(1, minsize=44, weight=0)
        row_frame.grid_rowconfigure(2, minsize=26, weight=0)

        # 1. Col A: Row label indicator (Excel Col A: 1, 0-based 0, rows 0..2, rowspan=3)
        row_pos = excel_17col_workspace_position(k, "row_label")
        labf = tk.Frame(row_frame, bg=CREAM)
        labf.grid_pos = row_pos
        labf.excel_pos = row_pos
        labf.grid(row=0, column=0, rowspan=3, padx=4, pady=2, sticky="nsew")
        row_label = tk.Label(labf, text="Row %d" % k, bg="#b5dca8", fg="#2a6a20", relief="groove",
                             font=("Segoe UI", 11, "bold"), padx=6)
        row_label.pack(pady=(4, 2))
        sub = tk.Label(labf, text="", bg=CREAM, fg="#2a6a20", font=("Segoe UI", 8, "italic"), wraplength=60)
        sub.pack()

        # 2. Col C: Math operator sign (Excel Col C: 3, 0-based 2, row 1)
        join_btn = None
        if k >= 2:
            join_pos = excel_17col_workspace_position(k, "math_sign")
            join_btn = btn(row_frame, "□", "#fbd34d", fg="black", font=("Segoe UI", 12, "bold"),
                           width=3, highlightbackground="#d0a020",
                           command=lambda r=r: self._set_target_row(r))
            join_btn.grid_pos = join_pos
            join_btn.excel_pos = join_pos
            join_btn.grid(row=1, column=2, padx=2, pady=2, sticky="nsew")

        # 3. Col E: Number / Mathematical expression (Excel Col E: 5, 0-based 4, row 1)
        row = self._math_slot(row_frame, r)

        # 4. Cols F..G: Math Descriptive Region (Excel Cols F..G: 6..7, 0-based 5..6, row 1)
        math_desc = DescriptionRegion(row_frame, role="math", calc_row=k,
                                      words=row.get("words", {}).get(0, ()),
                                      num_boxes=row.get("card_box_counts", {}).get(0, 1),
                                      on_words=lambda which, text, r=r: self._set_word(r, 0, which, text),
                                      on_focus=lambda which, r=r: self._word_focus_set(r, 0, which),
                                      on_add_box=lambda count, r=r: self._add_card_box(r, 0, count),
                                      use_17col=True)
        math_desc_pos = excel_17col_workspace_position(k, "math_box1")
        math_desc.grid_pos = math_desc_pos
        math_desc.excel_pos = math_desc_pos
        math_desc.grid(row=1, column=5, columnspan=2, padx=2, pady=2, sticky="w")

        # 5. Col I: Actions (Excel Col I: 9, 0-based 8, rows 0..2, rowspan=3, width 130px)
        actions_pos = excel_17col_workspace_position(k, "actions_frame")
        act_top_pos = excel_17col_workspace_position(k, "action_math_left")
        act_bot_pos = excel_17col_workspace_position(k, "action_clear_left")

        col3 = tk.Frame(row_frame, bg=CREAM, width=130)
        col3.grid_pos = actions_pos
        col3.excel_pos = actions_pos
        col3.grid(row=0, column=8, rowspan=3, padx=4, pady=2, sticky="nsew")
        col3.grid_rowconfigure(0, minsize=24)
        col3.grid_rowconfigure(1, minsize=28)
        col3.grid_rowconfigure(2, minsize=24)
        col3.grid_columnconfigure(0, minsize=110)

        edge = tk.Frame(col3, bg="black")
        edge.grid_pos = act_top_pos
        edge.excel_pos = act_top_pos
        edge.grid(row=0, column=0, sticky="n")
        btn_top = tk.Button(edge, text="math to put on the left", bg="white", relief="flat", bd=0,
                            font=("Segoe UI", 7, "bold"), wraplength=100,
                            command=lambda i=r: self._open_operators_for(i))
        btn_top.excel_pos = act_top_pos
        btn_top.grid_pos = act_top_pos
        btn_top.pack(padx=2, pady=2)

        btn_bot = tk.Button(col3, text="clear math on the left", bg="#f4d0d0", relief="raised", bd=1,
                            font=("Segoe UI", 7, "bold"), wraplength=100,
                            command=lambda i=r: self._clear_row_math(i))
        btn_bot.grid_pos = act_bot_pos
        btn_bot.excel_pos = act_bot_pos
        btn_bot.grid(row=2, column=0, sticky="s", pady=(4, 0))

        # 6. Col J: Result Equals Sign (Excel Col J: 10, 0-based 9, row 1)
        eq_pos = excel_17col_workspace_position(k, "result_equals")
        eq_lbl = tk.Label(row_frame, text="=", font=("Segoe UI", 16, "bold"), bg=CREAM, fg="black")
        eq_lbl.grid_pos = eq_pos
        eq_lbl.excel_pos = eq_pos
        eq_lbl.grid(row=1, column=9, padx=2, pady=2, sticky="nsew")

        # 7. Col K: Open Parenthesis Button (Excel Col K: 11, 0-based 10, row 1)
        paren_open_pos = excel_17col_workspace_position(k, "paren_open")
        paren_open_btn = tk.Button(row_frame, text="(", bg="white", fg="black",
                                   font=("Segoe UI", 12, "bold"), relief="raised", bd=1, width=3,
                                   command=lambda r=r: self._toggle_paren_open(r))
        paren_open_btn.grid_pos = paren_open_pos
        paren_open_btn.excel_pos = paren_open_pos
        paren_open_btn.grid(row=1, column=10, padx=2, pady=2, sticky="nsew")

        # 8. Col L: Calculated Result Box (Excel Col L: 12, 0-based 11, row 1)
        res_pos = excel_17col_workspace_position(k, "result_box")
        res_btn = tk.Button(row_frame, text="□", bg=PALE_BLUE, fg="black",
                            font=("Segoe UI", 12, "bold"), relief="solid", bd=1,
                            command=lambda r=r: self._set_target_row(r))
        res_btn.grid_pos = res_pos
        res_btn.excel_pos = res_pos
        res_btn.grid(row=1, column=11, padx=2, pady=2, sticky="nsew")

        # 9. Col M: Exponent Number Box 1 (Excel Col M: 13, 0-based 12, row 0, superscript to result)
        exp1_pos = excel_17col_workspace_position(k, "exponent_1")
        exp1_entry = tk.Entry(row_frame, width=4, font=("Segoe UI", 9), justify="center", bd=1,
                              relief="solid", bg="white", fg="black")
        exp1_entry.grid_pos = exp1_pos
        exp1_entry.excel_pos = exp1_pos
        exp1_entry.grid(row=0, column=12, padx=2, pady=(2, 0), sticky="s")
        exp1_entry.bind("<FocusIn>", lambda e, b=exp1_entry: self._on_exponent_focus(b), add="+")
        exp1_entry.bind("<Button-1>", lambda e, b=exp1_entry: self._on_exponent_focus(b), add="+")

        # 10. Col N: Close Parenthesis Button (Excel Col N: 14, 0-based 13, row 1)
        paren_close_pos = excel_17col_workspace_position(k, "paren_close")
        paren_close_btn = tk.Button(row_frame, text=")", bg="white", fg="black",
                                    font=("Segoe UI", 12, "bold"), relief="raised", bd=1, width=3,
                                    command=lambda r=r: self._toggle_paren_close(r))
        paren_close_btn.grid_pos = paren_close_pos
        paren_close_btn.excel_pos = paren_close_pos
        paren_close_btn.grid(row=1, column=13, padx=2, pady=2, sticky="nsew")

        # 11. Col O: Exponent Number Box 2 (Excel Col O: 15, 0-based 14, row 0, superscript to group)
        exp2_pos = excel_17col_workspace_position(k, "exponent_2")
        exp2_entry = tk.Entry(row_frame, width=4, font=("Segoe UI", 9), justify="center", bd=1,
                              relief="solid", bg="white", fg="black")
        exp2_entry.grid_pos = exp2_pos
        exp2_entry.excel_pos = exp2_pos
        exp2_entry.grid(row=0, column=14, padx=2, pady=(2, 0), sticky="s")
        exp2_entry.bind("<FocusIn>", lambda e, b=exp2_entry: self._on_exponent_focus(b), add="+")
        exp2_entry.bind("<Button-1>", lambda e, b=exp2_entry: self._on_exponent_focus(b), add="+")

        # 12. Cols P..Q: Result Descriptive Region (Excel Cols P..Q: 16..17, 0-based 15..16, row 1)
        res_desc = DescriptionRegion(row_frame, role="result", calc_row=k,
                                     words=row.get("result_words", ()),
                                     num_boxes=row.get("result_box_count", 1),
                                     on_words=lambda which, text, r=r: self._set_result_word(r, which, text),
                                     on_focus=lambda which, r=r: self._word_focus_set(r, "result", which),
                                     on_add_box=lambda count, r=r: self._add_result_box(r, count),
                                     use_17col=True)
        res_desc_pos = excel_17col_workspace_position(k, "result_box1")
        res_desc.grid_pos = res_desc_pos
        res_desc.excel_pos = res_desc_pos
        res_desc.grid(row=1, column=15, columnspan=2, padx=2, pady=2, sticky="w")

        res_desc.center_btn = res_btn
        res_desc.lead_btn = eq_lbl

        row.update({
            "row_frame": row_frame,
            "sub": sub,
            "join_btn": join_btn,
            "join": None,
            "mode": "full",
            "label": row_label,
            "is_result": False,
            "words": {},
            "card_box_counts": {},
            "helper_words": (),
            "helper_box_count": 1,
            "result_words": (),
            "result_box_count": 1,
            "grid_positions": excel_17col_workspace_positions(k),
            "main_row_positions": main_row_positions(k),
            "math_desc": math_desc,
            "math_card": math_desc,
            "result": res_btn,
            "result_box": res_btn,
            "result_card": res_desc,
            "result_desc": res_desc,
            "result_equals": eq_lbl,
            "equals_label": eq_lbl,
            "row_label_pos": row_pos,
            "label_frame": labf,
            "actions_frame": col3,
            "paren_open_btn": paren_open_btn,
            "paren_open": False,
            "exponent_1_box": exp1_entry,
            "exponent_1_entry": exp1_entry,
            "paren_close_btn": paren_close_btn,
            "paren_close": False,
            "exponent_2_box": exp2_entry,
            "exponent_2_entry": exp2_entry,
            "node": row_tree.new_node("_number"),
            "helper_card": None,
            "helper_heading": None,
        })
        self.rows.append(row)
        self._render_row(r)
        self._fit_rows()
        return r

    def _join_note(self, parent):
        return None

    def _math_slot(self, parent, r):
        """Mathematical expression slot anchored to Excel Column E (width 110)."""
        k = r + 1
        math_pos = excel_17col_workspace_position(k, "number_for_math")
        box = tk.Frame(parent, bg=CREAM, width=110, height=44)
        box.grid_pos = math_pos
        box.excel_pos = math_pos
        box.grid(row=1, column=4, sticky="nsew", padx=2, pady=2)

        canvas = tk.Canvas(box, bg=CREAM, highlightthickness=0, width=110, height=44)
        canvas.pack(fill="both", expand=True)

        inner = tk.Frame(canvas, bg=CREAM)
        canvas_win = canvas.create_window((55, 22), window=inner, anchor="center")

        def refresh():
            self._fit_rows()
            try:
                inner.update_idletasks()
                req_w = inner.winfo_reqwidth()
                if req_w > 110:
                    canvas.configure(width=req_w, scrollregion=(0, 0, req_w, 44))
                    canvas.coords(canvas_win, 0, 0)
                    canvas.itemconfigure(canvas_win, anchor="nw")
                else:
                    canvas.configure(width=110, scrollregion=(0, 0, 110, 44))
                    canvas.coords(canvas_win, 55, 22)
                    canvas.itemconfigure(canvas_win, anchor="center")
            except Exception:
                pass

        row = {
            "inner": inner,
            "canvas": canvas,
            "refresh": refresh,
            "node": None,
            "sel": None,
            "box": box,
        }
        self._slot_caption(inner)
        return row

    @staticmethod
    def _slot_caption(inner):
        tk.Label(inner, text="math from operator button", bg=CREAM, font=("Segoe UI", 9)
                 ).pack(padx=40, pady=45, anchor="w")

    def _is_blank(self, row):
        """True for a row that still has its default empty square box."""
        n = row["node"]
        return n is None or (n["key"] == "_number" and n["slots"] == [""])

    def _reset_row(self, i):
        """Put row i back to the default: one empty square box, no join symbol, not a result row."""
        row = self.rows[i]
        row["node"], row["sel"], row["is_result"] = row_tree.new_node("_number"), None, False
        row["words"] = {}
        row["card_box_counts"] = {}
        row["label"].configure(text="Row %d" % (i + 1),
                                bg="#6fcf5a" if i == self.op_target else "#b5dca8",
                                fg="#2a6a20")
        row["sub"].configure(text="")
        row["row_frame"].grid(row=i, column=0, sticky="nw", padx=0, pady=(2, 6))
        if i >= 1 and row.get("join_btn") is not None:
            row["join_btn"].grid(row=1, column=2, padx=2, pady=2, sticky="nsew")
            self._set_join(i, None)
        elif row.get("join_btn") is not None:
            row["join_btn"].grid_remove()
        if row.get("box") is not None:
            row["box"].grid(row=1, column=4, padx=2, pady=2, sticky="nsew")
        if row.get("math_desc") is not None:
            row["math_desc"].grid(row=1, column=5, columnspan=2, padx=2, pady=2, sticky="w")
        if row.get("actions_frame") is not None:
            row["actions_frame"].grid(row=0, column=8, rowspan=3, padx=4, pady=2, sticky="nsew")
        if row.get("equals_label") is not None:
            row["equals_label"].grid(row=1, column=9, padx=2, pady=2, sticky="nsew")
            row["equals_label"].configure(text="=")
            row["equals_label"].excel_pos = excel_17col_workspace_position(i + 1, "result_equals")
        if row.get("paren_open_btn") is not None:
            row["paren_open"] = False
            row["paren_open_btn"].configure(bg="white", fg="black", relief="raised")
            row["paren_open_btn"].grid(row=1, column=10, padx=2, pady=2, sticky="nsew")
            row["paren_open_btn"].excel_pos = excel_17col_workspace_position(i + 1, "paren_open")
        if row.get("result_box") is not None:
            row["result_box"].grid(row=1, column=11, padx=2, pady=2, sticky="nsew")
            row["result_box"].excel_pos = excel_17col_workspace_position(i + 1, "result_box")
        if row.get("exponent_1_box") is not None:
            row["exponent_1_box"].delete(0, tk.END)
            row["exponent_1_box"].grid(row=0, column=12, padx=2, pady=(2, 0), sticky="s")
            row["exponent_1_box"].excel_pos = excel_17col_workspace_position(i + 1, "exponent_1")
        if row.get("paren_close_btn") is not None:
            row["paren_close"] = False
            row["paren_close_btn"].configure(bg="white", fg="black", relief="raised")
            row["paren_close_btn"].grid(row=1, column=13, padx=2, pady=2, sticky="nsew")
            row["paren_close_btn"].excel_pos = excel_17col_workspace_position(i + 1, "paren_close")
        if row.get("exponent_2_box") is not None:
            row["exponent_2_box"].delete(0, tk.END)
            row["exponent_2_box"].grid(row=0, column=14, padx=2, pady=(2, 0), sticky="s")
            row["exponent_2_box"].excel_pos = excel_17col_workspace_position(i + 1, "exponent_2")
        if row.get("result_desc") is not None:
            row["result_desc"].grid(row=1, column=15, columnspan=2, padx=2, pady=2, sticky="w")
        for col_1based, width in EXCEL_17COL_COLUMN_WIDTHS.items():
            row["row_frame"].grid_columnconfigure(col_1based - 1, minsize=width, weight=0)
        row["grid_positions"] = excel_17col_workspace_positions(i + 1)
        self._set_result(i)
        self._render_row(i)

    def _invalidate(self):
        """Something changed: the sums and the printed result row are out of date."""
        self._reset_chains()
        for k, row in enumerate(self.rows):
            row_tree.clear_outputs(row["node"])
            self._set_result(k, None)

    def _clear_all(self):
        """C / Clear: back to the start. Exactly one empty Row 1, no join symbols, no extra rows, results cleared."""
        self.template = None
        self._active_exponent_box = None
        self._tpl_preview_state, self._tpl_previewed, self._tpl_applied = None, None, False

        # Destroy and remove all extra mathematical and total rows (rows beyond Row 1)
        for k in range(1, len(self.rows)):
            try:
                self.rows[k]["row_frame"].destroy()
            except Exception:
                pass
        self.rows = self.rows[:1]

        # Restore Row 1 to its initial empty state
        row = self.rows[0]
        row["mode"] = "full"
        self._reset_row(0)

        # Clear entered descriptive text and restore exactly 1 box
        if "math_desc" in row and hasattr(row["math_desc"], "reset"):
            row["math_desc"].reset()
        if "result_desc" in row and hasattr(row["result_desc"], "reset"):
            row["result_desc"].reset()

        self._set_target_row(0)
        self._select_only(0, (0,))
        self._render_row(0)
        self.target_label.configure(text="Selected Target: Row 1 | Addend 1 | Col 1: Number ('□')")
        self._refresh_adv_target()

        # Reset outer canvas scroll position to the beginning and update scrollregion
        self.rows_canvas.yview_moveto(0.0)
        self.rows_canvas.xview_moveto(0.0)
        self._fit_rows()

        self.focus_set()
        self._say("Cleared. Click a square box and type a number, or open Operators.")

    def _clear_row_math(self, i):
        """Remove the math to the left of the = sign in row i (back to one empty square box)."""
        self._reset_row(i)
        if all(self._is_blank(r) and not r["join"] for r in self.rows):
            self.template = None
            for k, r in enumerate(self.rows):
                r["sub"].configure(text="")
                r["mode"] = "full"

    def _show_result_row(self, idx, total):
        """Print the result: the row after the last used row becomes = <total>."""
        while idx >= len(self.rows):
            self._add_row()
        row = self.rows[idx]
        shown = row_tree.fmt(total)
        node = row_tree.new_node("_number")
        node["slots"] = [shown]
        row["node"], row["sel"], row["is_result"] = node, None, True

        row["label"].configure(text="Total", bg="#b5dca8", fg="#2a6a20")
        row["sub"].configure(text="")
        row["row_frame"].grid(row=idx, column=0, sticky="nw", padx=0, pady=(2, 6))

        # Apply authoritative effective default widths so empty columns (C, E, F, G, I)
        # do not collapse, aligning Column J (=), Column K ('('), and Column L (result)
        # directly below standard mathematical rows.
        for col_1based, width in EXCEL_17COL_EFFECTIVE_DEFAULT_WIDTHS.items():
            row["row_frame"].grid_columnconfigure(col_1based - 1, minsize=width, weight=0)

        if row.get("join_btn") is not None:
            row["join_btn"].grid_remove()
        row["join"] = None

        if row.get("box") is not None:
            row["box"].grid_remove()

        if row.get("math_desc") is not None:
            row["math_desc"].grid_remove()

        if row.get("actions_frame") is not None:
            row["actions_frame"].grid_remove()

        if row.get("equals_label") is not None:
            row["equals_label"].grid(row=1, column=9, padx=2, pady=2, sticky="nsew")
            row["equals_label"].configure(text="=")
            row["equals_label"].excel_pos = excel_17col_workspace_position(idx + 1, "result_equals")

        if row.get("paren_open_btn") is not None:
            row["paren_open_btn"].grid(row=1, column=10, padx=2, pady=2, sticky="nsew")
            row["paren_open_btn"].excel_pos = excel_17col_workspace_position(idx + 1, "paren_open")

        self._set_result(idx, advanced_input.short_label(shown, 14))
        if row.get("result_box") is not None:
            row["result_box"].grid(row=1, column=11, padx=2, pady=2, sticky="nsew")
            row["result_box"].excel_pos = excel_17col_workspace_position(idx + 1, "result_box")

        if row.get("exponent_1_box") is not None:
            row["exponent_1_box"].grid(row=0, column=12, padx=2, pady=(2, 0), sticky="s")
            row["exponent_1_box"].excel_pos = excel_17col_workspace_position(idx + 1, "exponent_1")

        if row.get("paren_close_btn") is not None:
            row["paren_close_btn"].grid(row=1, column=13, padx=2, pady=2, sticky="nsew")
            row["paren_close_btn"].excel_pos = excel_17col_workspace_position(idx + 1, "paren_close")

        if row.get("exponent_2_box") is not None:
            row["exponent_2_box"].grid(row=0, column=14, padx=2, pady=(2, 0), sticky="s")
            row["exponent_2_box"].excel_pos = excel_17col_workspace_position(idx + 1, "exponent_2")

        if row.get("result_desc") is not None:
            row["result_desc"].grid(row=1, column=15, columnspan=2, padx=2, pady=2, sticky="w")
            row["result_desc"].excel_pos = excel_17col_workspace_position(idx + 1, "result_box1")

        row["grid_positions"] = excel_17col_total_row_positions(idx + 1)
        self._fit_rows()
        self._scroll_to_row(idx)

    def _set_target_row(self, i):
        """The row that operators, Next Row and the join keys act on (its Row label turns darker)."""
        self.op_target = i
        for k, r in enumerate(self.rows):
            r["label"].configure(bg="#6fcf5a" if k == i else "#b5dca8")
        lbl = getattr(self, "join_label", None)
        if lbl is not None:
            lbl.configure(text="Join Row %d to the rows above (helper card):" % (max(i, 1) + 1))

    def _select_only(self, i, path):
        """Exactly one box is selected at a time: the one just clicked (or the new row's number)."""
        for k, r in enumerate(self.rows):
            if k != i and r["sel"] is not None:
                r["sel"] = None
                self._render_row(k)
        self.rows[i]["sel"] = path
        self.focus_set()

    def _next_row(self):
        """Next Row: go to the next row (adding one at the bottom), ready to type its number."""
        i = self.op_target + 1
        while i >= len(self.rows):
            self._add_row()
        self._set_target_row(i)
        row = self.rows[i]
        if row["is_result"] or row["node"] is None:
            self._reset_row(i)                  # carry on the sum from the printed result row
        self._select_only(i, (0,) if row["node"]["key"] == "_number" else None)
        self._render_row(i)
        self._scroll_to_row(i)
        self._say("Row %d: type its number on the number pad (or open 'math to put on the left'), then pick "
                  "a join symbol  + − × ÷ =  above the Advanced Input button." % (i + 1))

    def _scroll_to_row(self, i):
        """Scroll the rows section only if row i is not currently fully visible in the canvas viewport."""
        if i >= len(self.rows):
            return
        self.rows_canvas.update_idletasks()
        rf = self.rows[i].get("row_frame")
        if not rf:
            return

        total_h = max(1, self.area.winfo_reqheight())
        visible_h = self.rows_canvas.winfo_height()
        if visible_h <= 1:
            visible_h = 290

        if total_h <= visible_h:
            self.rows_canvas.yview_moveto(0.0)
            return

        row_top = rf.winfo_y()
        row_h = rf.winfo_height() if rf.winfo_height() > 0 else rf.winfo_reqheight()
        row_bottom = row_top + row_h

        y1, y2 = self.rows_canvas.yview()
        current_top_px = y1 * total_h
        current_bottom_px = current_top_px + visible_h

        if row_top >= current_top_px and row_bottom <= current_bottom_px:
            return

        if row_bottom > current_bottom_px:
            target_top_px = row_bottom - visible_h
            self.rows_canvas.yview_moveto(min(1.0, max(0.0, target_top_px / total_h)))
        elif row_top < current_top_px:
            self.rows_canvas.yview_moveto(max(0.0, row_top / total_h))

    def _join_key(self, symbol):
        """A join key under the keypad: put the symbol in the helper card of the target row."""
        i = max(self.op_target, 1)
        # a second join key after the number of a joined row starts the NEXT row, like  1 + 1 + 1  on a calculator
        if i < len(self.rows) and self.rows[i].get("join") and not self.rows[i]["is_result"] and not self._is_blank(self.rows[i]):
            i += 1
        while i >= len(self.rows):
            self._add_row()
        if self.rows[i]["is_result"]:
            self._reset_row(i)
        self._invalidate()
        self._set_join(i, symbol)
        # like pressing + on a calculator: carry on in that row, so the next digits are ITS number, not more digits of the row above
        self._set_target_row(i)
        row = self.rows[i]
        if self._is_blank(row):
            if row["node"] is None:
                row["node"] = row_tree.new_node("_number")
            self._select_only(i, (0,))
            self._render_row(i)
            self._scroll_to_row(i)
            self._say("Row %d is joined to the rows above with  %s .  Type its number, then press =." % (i + 1, symbol))
        else:
            self._say("Row %d is joined to the rows above with  %s .  Press = to calculate." % (i + 1, symbol))

    def _set_join(self, i, symbol):
        """Show the join operator in row i's helper card (None puts the small box back)."""
        while i >= len(self.rows):
            self._add_row()
        row = self.rows[i]
        row["join"] = symbol
        if row["join_btn"] is not None:
            t = symbol or "□"
            row["join_btn"].configure(text=t, width=max(2, len(t) + 1))

    def _cards(self, i):
        """Row i's cards: [(kind, text, slot path)]."""
        node = self.rows[i]["node"]
        return row_tree.flatten(node) if node else []

    # ---------- the words of a card (its Label / Item and Context boxes) ----------
    def _card_words(self, i):
        """Row i's (label, context) for every card: what the operator's row file gives it (WORDS), overridden by what was typed."""
        row = self.rows[i]
        base = row_tree.words(row["node"]) if row["node"] else []
        typed = row.get("words", {})
        res = []
        for k in range(max(len(base), len(typed))):
            base_w = base[k] if k < len(base) else ("",)
            w = typed.get(k, base_w)
            res.append(tuple(w))
        return res

    def _set_word(self, i, k, which, text):
        """The person typed `text` into box `which` of card k of row i."""
        all_words = self._card_words(i)
        cur = list(all_words[k]) if k < len(all_words) else []
        while len(cur) <= which:
            cur.append("")
        cur[which] = text
        self.rows[i].setdefault("words", {})[k] = tuple(cur)

    def _set_helper_word(self, r, which, text):
        if r < len(self.rows):
            cur = list(self.rows[r].get("helper_words", ()))
            while len(cur) <= which:
                cur.append("")
            cur[which] = text
            self.rows[r]["helper_words"] = tuple(cur)

    def _add_helper_box(self, r, count):
        if r < len(self.rows):
            self.rows[r]["helper_box_count"] = count

    def _set_result_word(self, r, which, text):
        if r < len(self.rows):
            cur = list(self.rows[r].get("result_words", ()))
            while len(cur) <= which:
                cur.append("")
            cur[which] = text
            self.rows[r]["result_words"] = tuple(cur)

    def _add_result_box(self, r, count):
        if r < len(self.rows):
            self.rows[r]["result_box_count"] = count
            self._fit_rows()

    def _add_card_box(self, i, k, count):
        if i < len(self.rows):
            self.rows[i].setdefault("card_box_counts", {})[k] = count
            self._fit_rows()

    def _word_focus_set(self, i, k, which):
        self._word_focus = (i, k, which)

    def _apply_word(self, which, text):
        """The Descriptive Columns Console: put a word into the box last clicked."""
        focus = getattr(self, "_word_focus", None)
        text = text.strip()
        if focus is None or not text:
            self._say("Click a descriptive text box on a card first, then pick or type a word.")
            return
        i, k, field = focus
        target_field = field if which is None else which
        if i >= len(self.rows):
            self._say("That row is gone: click a descriptive text box again.")
            return
        if k == "helper":
            self._set_helper_word(i, target_field, text)
            card = self.rows[i].get("helper_card")
            if card:
                while len(card.words_data) <= target_field:
                    card.words_data.append("")
                card.words_data[target_field] = text
                if target_field == 0 and card.box1:
                    card.box1.delete(0, "end")
                    card.box1.insert(0, text)
                    card.box1.configure(fg="black")
                    card.box1.hinted = False
                elif card._active_extra_box and card.current_page == target_field + 1:
                    card._active_extra_box.delete(0, "end")
                    card._active_extra_box.insert(0, text)
                    card._active_extra_box.configure(fg="black")
                    card._active_extra_box.hinted = False
        elif k == "result":
            self._set_result_word(i, target_field, text)
            card = self.rows[i].get("result_card")
            if card:
                while len(card.words_data) <= target_field:
                    card.words_data.append("")
                card.words_data[target_field] = text
                if target_field == 0 and card.box1:
                    card.box1.delete(0, "end")
                    card.box1.insert(0, text)
                    card.box1.configure(fg="black")
                    card.box1.hinted = False
                elif card._active_extra_box and card.current_page == target_field + 1:
                    card._active_extra_box.delete(0, "end")
                    card._active_extra_box.insert(0, text)
                    card._active_extra_box.configure(fg="black")
                    card._active_extra_box.hinted = False
        else:
            if k >= len(self._card_words(i)):
                self._say("That card is gone: click a descriptive text box again.")
                return
            self._set_word(i, k, target_field, text)
            self._render_row(i)

    def _render_row(self, i):
        row = self.rows[i]
        for w in row["inner"].winfo_children():
            w.destroy()
        cards = self._cards(i)
        if not cards:
            self._slot_caption(row["inner"])
        else:
            sel = next((n for n, c in enumerate(cards) if c[2] is not None and c[2] == row["sel"]), None)
            card_box_counts = row.setdefault("card_box_counts", {})
            if len(cards) == 1 and cards[0][0] == "box":
                item = cards[0]
                text = item[1] or "□"
                bg = "#5b9bf0" if sel == 0 else PALE_BLUE
                b = tk.Button(row["inner"], text=text, width=max(2, len(text) + 1), bg=bg,
                              relief="sunken" if sel == 0 else "solid", bd=1,
                              font=("Segoe UI", 12, "bold"),
                              command=lambda: self._pick_box(i, 0))
                b.center_btn = b
                b.lead_btn = b
                math_desc = row.get("math_desc")
                if math_desc:
                    b.box1 = math_desc.box1
                    b.box2 = math_desc.box2
                    b.trailing_btn = math_desc.trailing_btn
                    b.boxes = math_desc.boxes
                    b.num_boxes = math_desc.num_boxes
                    b.get_words = math_desc.get_words
                    b.to_excel_coordinate = math_desc.to_excel_coordinate
                b.grid_pos = excel_17col_workspace_position(i + 1, "number_for_math")
                b.excel_pos = b.grid_pos
                b.pack(pady=4)
            else:
                br = build_row(row["inner"], [(k, t) for k, t, _ in cards], [], stacked=(i > 0 and row["mode"] != "full"),
                               on_pick=lambda k, i=i: self._pick_box(i, k), selected=sel, levels=row_tree.levels(row["node"]), fracs=row_tree.fracs(row["node"]),
                               stack_exponents=row_tree.stack_exponents(row["node"]), words=self._card_words(i),
                               num_boxes=card_box_counts,
                               on_words=lambda k, which, text, i=i: self._set_word(i, k, which, text),
                               on_focus=lambda k, which, i=i: self._word_focus_set(i, k, which),
                               on_add_box=lambda k, count, i=i: self._add_card_box(i, k, count),
                               card_slot=2, calc_row=i + 1)
                br.pack(fill="both", expand=True)
            say = row_tree.note(row["node"])
            if say:                                       # a formula-only operator: one sentence under its cards, no box
                tk.Label(row["inner"], text=say, bg=row["inner"].cget("bg"), fg="#555555", font=("Segoe UI", 9, "italic"),
                         wraplength=900, justify="left").pack(anchor="w", padx=6, pady=(0, 4))
        row["refresh"]()

    def _set_result(self, i, text=None):
        """Show text (the sum) in row i's result card; None puts the small box back."""
        b = self.rows[i].get("result")
        if b is not None:
            t = text if text else "□"
            b.configure(text=t, width=max(2, len(t) + 1))

    def _say(self, msg):
        self.results.configure(state="normal")
        self.results.delete("1.0", "end")
        self.results.insert("1.0", msg)
        self.results.configure(state="disabled")

    def _key(self, ch):
        """Number pad: type into the selected box (click a box first); ⌫ deletes."""
        # Route to active exponent box if one is focused/selected
        active_exp = getattr(self, "_active_exponent_box", None)
        if active_exp is not None and active_exp.winfo_exists():
            if ch == "⌫":
                curr = active_exp.get()
                if curr:
                    active_exp.delete(len(curr) - 1, tk.END)
            elif ch == "±":
                curr = active_exp.get().strip()
                if curr.startswith("-"):
                    active_exp.delete(0, tk.END)
                    active_exp.insert(0, curr[1:])
                else:
                    active_exp.delete(0, tk.END)
                    active_exp.insert(0, "-" + curr)
            elif ch in "0123456789.":
                if ch == "." and "." in active_exp.get():
                    return
                active_exp.insert(tk.END, ch)
            return

        sel = self._selected_box()
        if sel is None:
            self._say("Click a square box first, then type its number on the number pad.")
            return
        i, path = sel
        row = self.rows[i]
        if row["is_result"]:
            self._reset_row(i)
            row["sel"] = path = (0,)
        t = row_tree.get_slot(row["node"], path)
        if isinstance(t, dict) and "adv" in t:
            t = ""                          # typing a number replaces an advanced value
        if not isinstance(t, str):
            self._say("That box holds an operator: click one of its square boxes to type a number.")
            return
        if ch == "⌫":
            t = t[:-1]
        elif ch == "±":                     # flip the sign of the number, or of the exponent after "e"
            if "e" in t:
                mant, exp = t.split("e", 1)
                t = mant + "e" + (exp[1:] if exp.startswith("-") else "-" + exp)
            else:
                t = t[1:] if t.startswith("-") else "-" + t
        elif ch == "EE":                    # start a power of ten:  1.5 EE ± 3  ->  1.5e-3
            if "e" in t or not t or not t[-1].isdigit():
                return
            t += "e"
        elif ch == "." and ("." in t or "e" in t):
            return
        else:
            t += ch
        row_tree.set_slot(row["node"], path, t)
        self._invalidate()
        self._render_row(i)
        self._sync_links()

    def _equals(self):
        """Number pad =: calculate the rows, joined by the symbols in their helper cards.  Each row shows its own
        answer in its own answer card (right of its "=", beside "math to put on the left").  When rows are joined
        (Row 2 has a join sign), the answer for all of them is printed in the row after the last one used (Row 3
        for Rows 1 and 2).  A single row prints nothing further down.  With a multi-row operator, every row is
        calculated and the results are joined by that operator's joins."""
        if self.template is not None:
            return self._equals_template()
        if self._is_blank(self.rows[0]):
            self._say("Type a number in Row 1 first: click its square box, then use the number pad "
                      "(or pick an operator with 'math to put on the left').")
            return

        # 1. Identify used mathematical rows
        used_rows = []
        for k, row in enumerate(self.rows):
            if row.get("is_result") or (k > 0 and self._is_blank(row) and not row.get("join")):
                continue
            used_rows.append(k)

        if not used_rows:
            return

        # 2. Validate parentheses and exponents across used rows
        open_row = None
        groups = []  # list of (start_k, end_k)
        for k in used_rows:
            row = self.rows[k]
            has_open = bool(row.get("paren_open"))
            has_close = bool(row.get("paren_close"))
            exp1_str = self._get_exponent_1(k)
            exp2_str = self._get_exponent_2(k)

            # Check for group exponent without close parenthesis
            if exp2_str and not has_close:
                self._say("Row %d has a group exponent (Column O) without a closing parenthesis ')'." % (k + 1))
                return

            # Check exponent syntax
            if exp1_str:
                try:
                    self._parse_exponent_value(exp1_str)
                except ValueError as e:
                    self._say("Row %d: %s" % (k + 1, e))
                    return

            if exp2_str:
                try:
                    self._parse_exponent_value(exp2_str)
                except ValueError as e:
                    self._say("Row %d: %s" % (k + 1, e))
                    return

            if has_open and has_close:
                if open_row is not None:
                    self._say("Nested parentheses across rows are not supported. "
                              "Please close the open parenthesis from Row %d first." % (open_row + 1))
                    return
                groups.append((k, k))
            elif has_open:
                if open_row is not None:
                    self._say("Nested parentheses across rows are not supported. "
                              "Please close the open parenthesis from Row %d first." % (open_row + 1))
                    return
                open_row = k
            elif has_close:
                if open_row is None:
                    self._say("Row %d has a closing parenthesis ')' without a matching opening parenthesis '('. "
                              "Please add '(' or remove ')'. " % (k + 1))
                    return
                groups.append((open_row, k))
                open_row = None

        if open_row is not None:
            self._say("Row %d has an opening parenthesis '(' without a matching closing parenthesis ')'. "
                      "Please close it with ')' or remove '('." % (open_row + 1))
            return

        # 3. Evaluate each row's individual expression and Exponent Box 1
        row_values = {}
        for k in used_rows:
            row = self.rows[k]
            try:
                v = row_tree.evaluate(row["node"])
            except ValueError as e:
                self._say("Row %d: %s" % (k + 1, e) if k else str(e))
                return
            self._render_row(k)
            exp1_str = self._get_exponent_1(k)
            if exp1_str:
                try:
                    exp1 = self._parse_exponent_value(exp1_str)
                    v = self._apply_exponent(v, exp1)
                except ValueError as e:
                    self._say("Row %d: %s" % (k + 1, e) if k else str(e))
                    return
            row_values[k] = v

        # 4. Form top-level items (groups and ungrouped rows)
        group_by_start = {s: (s, e) for s, e in groups}
        items = []
        idx = 0
        while idx < len(used_rows):
            k = used_rows[idx]
            if k in group_by_start:
                s, e = group_by_start[k]
                g_val = row_values[s]
                for j in range(s + 1, e + 1):
                    row_j = self.rows[j]
                    join_sym = row_j.get("join")
                    if not join_sym:
                        self._say("Row %d needs a join symbol: click + − × ÷ = above the Advanced Input button." % (j + 1))
                        return
                    try:
                        g_val = row_tree.join(join_sym, g_val, row_values[j])
                    except ValueError as e_val:
                        self._say(str(e_val))
                        return
                # Apply Exponent Box 2 (group exponent on row e)
                exp2_str = self._get_exponent_2(e)
                if exp2_str:
                    try:
                        exp2 = self._parse_exponent_value(exp2_str)
                        g_val = self._apply_exponent(g_val, exp2)
                    except ValueError as e_val:
                        self._say("Row %d: %s" % (e + 1, e_val))
                        return
                join_leading = self.rows[s].get("join") if s > 0 else None
                if s > 0 and not join_leading:
                    self._say("Row %d needs a join symbol: click + − × ÷ = above the Advanced Input button." % (s + 1))
                    return
                items.append({"val": g_val, "join": join_leading, "start": s, "end": e, "is_group": True})
                while idx < len(used_rows) and used_rows[idx] <= e:
                    idx += 1
            else:
                join_leading = self.rows[k].get("join") if k > 0 else None
                if k > 0 and not join_leading:
                    self._say("Row %d needs a join symbol: click + − × ÷ = above the Advanced Input button." % (k + 1))
                    return
                items.append({"val": row_values[k], "join": join_leading, "start": k, "end": k, "is_group": False})
                idx += 1

        # 5. Check for unsupported mixed precedence among top-level items (+ before ×)
        if len(items) > 2:
            joins = [it["join"] for it in items[1:]]
            first_add_sub = next((i for i, j in enumerate(joins) if j in ("+", "−")), None)
            last_mul_div = max((i for i, j in enumerate(joins) if j in ("×", "÷", "%")), default=-1)
            if first_add_sub is not None and first_add_sub < last_mul_div:
                self._say("Warning: Expression requires Step 3C PEMDAS precedence (+ before × across ungrouped rows). "
                          "Please use parentheses to group operations explicitly.")
                return

        # 6. Evaluate total across items
        total = items[0]["val"]
        for it in items[1:]:
            try:
                total = row_tree.join(it["join"], total, it["val"])
            except ValueError as e_join:
                self._say(str(e_join))
                return

        # 7. Format result rows and log lines
        lines = []
        for k in used_rows:
            cards = " ".join((t if t else "□") for _, t, _p in self._cards(k))
            row = self.rows[k]
            has_open = bool(row.get("paren_open"))
            has_close = bool(row.get("paren_close"))
            exp1_str = self._get_exponent_1(k)
            exp2_str = self._get_exponent_2(k)

            if exp1_str:
                base_part = "(%s)^%s" % (cards, exp1_str) if len(cards.split()) > 1 else "%s^%s" % (cards, exp1_str)
            else:
                base_part = cards

            if has_open and has_close:
                row_part = "( %s )" % base_part
            elif has_open:
                row_part = "( %s" % base_part
            elif has_close:
                row_part = "%s )" % base_part
            else:
                row_part = base_part

            if exp2_str:
                row_part = "%s^%s" % (row_part, exp2_str)

            if k == 0:
                lines.append("Row 1:  %s" % row_part)
            else:
                lines.append("Row %d:  %s %s" % (k + 1, row.get("join"), row_part))

        if len(used_rows) > 1:
            # Multi-row calculation: each input row shows its own value in Column L
            for k in used_rows:
                self._set_result(k, advanced_input.short_label(row_tree.fmt(row_values[k]), 14))
            last = used_rows[-1]
            self._show_result_row(last + 1, total)
            for j in range(last + 2, len(self.rows)):
                if self.rows[j].get("is_result"):
                    self._reset_row(j)
                    self.rows[j]["row_frame"].grid_remove()
            lines.append("=  %s     (all %d rows joined, shown in Row %d)" % (row_tree.fmt(total), len(used_rows), last + 2))
        else:
            # Single-row calculation: Row 1 Column L shows the final evaluated total
            self._set_result(0, advanced_input.short_label(row_tree.fmt(total), 14))
            for j in range(1, len(self.rows)):
                if self.rows[j].get("is_result"):
                    self._reset_row(j)
                    self.rows[j]["row_frame"].grid_remove()
            lines.append("=  %s     (shown in Row 1's answer card, right of the =)" % row_tree.fmt(total))

        self._say("\n".join(lines))

    def _sync_links(self):
        """Boxes that a multi-row operator links (e.g. the same u and point in every row) copy the
        value typed into their source box."""
        t = self.template
        if t is None:
            return
        touched = set()
        for (dr, dp), (sr, sp) in t["spec"].get("links", []):
            src_node, dst_node = self.rows[sr]["node"], self.rows[dr]["node"]
            if src_node is None or dst_node is None:
                continue
            try:
                src = row_tree.get_slot(src_node, sp)
                row_tree.get_slot(dst_node, dp)
            except (IndexError, TypeError, KeyError):
                continue
            if isinstance(src, dict) and "adv" not in src:
                continue                      # the source box was expanded into an operator
            row_tree.set_slot(dst_node, dp, dict(src) if isinstance(src, dict) else src)
            touched.add(dr)
        for r in touched:
            self._render_row(r)

    def _chain_boxes(self):
        """[(row, path of the box, source row)] of the boxes a multi-row operator fills from an earlier row's answer (see row_tree.chain_slots)."""
        t = self.template
        if t is None:
            return []
        return [(i, path, k) for i, rs in enumerate(t["spec"]["rows"]) for path, k in row_tree.chain_slots(rs)]

    def _reset_chains(self):
        """Forget the answers the chained boxes hold (something changed, or a new calculation starts): they show "row k" again until = fills them in."""
        for i, path, k in self._chain_boxes():
            node = self.rows[i]["node"] if i < len(self.rows) else None
            if node is None:
                continue
            try:
                held = row_tree.get_slot(node, path)
                if isinstance(held, dict) and held.get("adv") and held.get("value") is None:
                    continue                                          # already empty
                row_tree.set_slot(node, path, row_tree.chain_placeholder(k))
            except (IndexError, TypeError, KeyError):
                continue
            self._render_row(i)

    def _equals_template(self):
        self._sync_links()
        spec = self.template["spec"]
        self._reset_chains()                      # a chained box never keeps an old answer
        results = []
        for i, rs in enumerate(spec["rows"]):
            node = self.rows[i]["node"]
            if node is None:
                self._say("Row %d (%s) is empty: pick an operator for it." % (i + 1, rs["title"]))
                return
            for path, k in row_tree.chain_slots(rs):                  # boxes that read an earlier row: its answer, as the exact number it is
                earlier = results[k]
                if isinstance(earlier, bool) or not isinstance(earlier, (int, float)):
                    self._say("Row %d (%s) reads the answer of Row %d, which is %s: it needs a single number." % (i + 1, rs["title"], k + 1, row_tree.fmt(earlier)))
                    return
                row_tree.set_slot(node, path, row_tree.chain_value(earlier))
            try:
                v = row_tree.evaluate(node)
            except ValueError as e:
                self._say("Row %d (%s): %s" % (i + 1, rs["title"], e))
                return
            self._render_row(i)
            exp1_str = self._get_exponent_1(i)
            if exp1_str:
                try:
                    exp1 = self._parse_exponent_value(exp1_str)
                    v = self._apply_exponent(v, exp1)
                except ValueError as e:
                    self._say("Row %d (%s): %s" % (i + 1, rs["title"], e) if len(spec["rows"]) > 1 else str(e))
                    return
            results.append(v)
            self._set_result(i, advanced_input.short_label(row_tree.fmt(v), 14))
        try:
            total = results[0]
            for k, symbol in enumerate(spec["joins"], start=1):
                total = row_tree.join(symbol, total, results[k])
        except ValueError as e:
            self._say(str(e))
            return
        lines = ["Row %d = %s" % (i + 1, row_tree.fmt(v)) for i, v in enumerate(results)]
        self._say("%s\n%s\njoined with %s  ->  %s" % (self.template["title"], "   |   ".join(lines),
                                                       " ".join(spec["joins"]), row_tree.fmt(total)))

    def _pick_box(self, i, k):
        """Click on a card's blue + / box: that number becomes the target the next operator expands."""
        self._active_exponent_box = None
        if self.rows[i]["is_result"]:
            self._reset_row(i)
            k = 0
        cards = self._cards(i)
        self._set_target_row(i)
        self._select_only(i, cards[k][2])
        n = sum(1 for c in cards[:k + 1] if c[0] == "box")
        self.target_label.configure(text="Selected Target: Row %d | Addend %d | Col 1: Number ('□')  "
                                         "- pick an operator to expand it" % (i + 1, n))
        self._render_row(i)
        self._refresh_adv_target()
        self.focus_set()

    def _open_operators_for(self, i):
        """The row's 'math to put on the left' button: open (or retarget) the Operators pop-up."""
        same = self.op_target == i
        self._set_target_row(i)
        if getattr(self, "op_popup", None) is None or same:
            self._toggle_operators()
        self._refresh_op_title()

    def _refresh_op_title(self):
        t = getattr(self, "_op_title", None)
        if getattr(self, "op_popup", None) is not None and t is not None:
            t.configure(text="Operators → Row %d  (drag to move)" % (self.op_target + 1))

    def _place_operator_row(self, key, node=None):
        """Put the operator's math into the target row.  node = a ready-made tree (a template) instead of key.
        Empty row 1: the operator with its boxes.  Later rows: just the operator (the operands are the
        rows above).  Row 1 that already has math: the operator EXPANDS the selected number (or the first
        number if none is selected) into that operator's math, so it nests."""
        spec = None if node is not None else multirow_specs.get(key)
        if spec is not None:
            self._apply_template(key, spec)
            return
        i = self.op_target
        row = self.rows[i]
        if row["is_result"]:
            self._reset_row(i)
        new = node if node is not None else row_tree.new_node(key)
        boxes = [c[2] for c in self._cards(i) if c[0] == "box"]
        if (i == 0 or row["mode"] == "full") and row["node"] is not None and boxes:
            path = row["sel"] if row["sel"] in boxes else boxes[0]
            row_tree.set_slot(row["node"], path, new)
        else:
            row["node"] = new
        row["words"] = {}
        row["sel"] = None
        self._invalidate()
        self._render_row(i)
        self._refresh_adv_target()
        self.focus_set()
        mod = new["mod"]
        if node is not None:
            n = template_math.empty_boxes(new)
            self._say("Template placed in Row %d:  %s\n%s" % (i + 1, template_math.describe(new),
                      "Fill the %d empty square box%s (click one, then use the number pad), then press =."
                      % (n, "" if n == 1 else "es") if n else "Nothing to fill in: press ="))
        elif mod.CALC in ("ready", "advanced"):
            how = "number pad" if mod.CALC == "ready" else "number pad / Advanced Input"
            self._say("%s: fill the boxes in order -> %s  (%s), then press =." % (mod.NAME, ", ".join(row_tree.inputs_in_box_order(mod)), how))
        else:
            try:
                row_tree.evaluate(new)
            except ValueError as e:
                self._say(str(e))

    def _apply_template(self, key, spec):
        """A multi-row operator: add the rows it needs, put its operator in each row, show the joins."""
        need = len(spec["rows"])
        while len(self.rows) < need:
            self._add_row()
        for k, row in enumerate(self.rows):
            row["node"], row["sel"], row["is_result"] = row_tree.new_node("_number"), None, False
            row["words"] = {}
            row["sub"].configure(text="")
            row["mode"] = "full"
            if row["join_btn"] is not None:
                self._set_join(k, None)
            self._set_result(k)
        for k, rs in enumerate(spec["rows"]):
            row = self.rows[k]
            row["mode"] = "full"
            row["node"] = row_tree.build_node(rs)
            row["words"] = {}
            row["sub"].configure(text=rs["title"])
            if k > 0:
                self._set_join(k, spec["joins"][k - 1])
        for k in range(len(self.rows)):
            self._render_row(k)
        self.template = {"key": key, "spec": spec, "title": spec["title"]}
        name = operator_row_math.get(key).NAME
        steps = "   ".join("Row %d: %s." % (k + 1, rs["title"]) for k, rs in enumerate(spec["rows"]))
        self.target_label.configure(text="%s needs %d rows - Row 1 to Row %d are filled in; joined by %s"
                                         % (name, need, need, " ".join(spec["joins"])))
        self._say("%s needs %d rows.\n%s\n%s\nJoined with %s. Fill the boxes in every row, then press =."
                  % (name, need, steps, spec["title"], " ".join(spec["joins"])))
        self._refresh_adv_target()
        self.focus_set()

    # ---------- mathematical templates (typed math saved for later) ----------
    # The steps:  1 type math   2 Preview Posted   3 Save Template   4 pick it in the list + Apply Template
    GUIDE_STEPS = [
        ("Type your math in the text box",
         "Use ? or a letter such as x for a box you will fill in later. Examples:   (? + 3) × 2     "
         "sqrt(x) + 4     Time dilation(1, x)"),
        ("Press  Preview Posted",
         "Your math appears in Row %d, just like an operator from the Operators list, so you can see it. "
         "You can change the text and preview again."),
        ("Like it?  Press  Save Template",
         "It is kept on this computer, so it will be there next time too. "
         "Not happy? Change the text and press Preview Posted again."),
        ("Use it whenever you want",
         "Pick it in the list next to Apply Template, then press Apply Template. It goes into the row. "
         "Then fill the empty boxes and press the keypad = key."),
    ]

    def _tpl_build(self, text):
        """The operator tree for typed math, or None (after telling the user what is wrong)."""
        try:
            return template_math.parse_math(text)
        except ValueError as e:
            self._say("Template: %s" % e)
            return None

    def _tpl_write_file(self):
        """Save the templates and the guide choice.  Returns None, or the reason it could not be written."""
        try:
            template_math.save_data(self.template_path, self.saved_templates, self.tpl_hide_guide)
        except OSError as e:
            return str(e)
        return None

    def _tpl_progress(self):
        """(typed OK, previewed, saved, applied) for what is in the text box right now."""
        text = self.tpl_entry.get().strip()
        try:
            template_math.parse_math(text)
            ok = True
        except ValueError:
            ok = False
        return (ok, ok and self._tpl_previewed == text, ok and text in self.saved_templates,
                ok and self._tpl_applied and self.tpl_combo.get().strip() == text)

    def _tpl_typed(self):
        """Called after every key typed in the template text box."""
        text = self.tpl_entry.get().strip()
        if text != getattr(self, "_tpl_last_text", ""):
            self._tpl_last_text = text
            self._tpl_applied = False
        if text and self._tpl_was_empty and not self.tpl_hide_guide and self.tpl_guide is None:
            self._tpl_show_guide()
        self._tpl_was_empty = not text
        self._tpl_guide_refresh()

    def _tpl_show_guide(self):
        """The how-to pop-up: the four steps side by side, the one you are on highlighted."""
        if self.tpl_guide is not None:
            self.tpl_guide.lift()
            self._tpl_guide_refresh()
            return
        bg = "#f6f1e0"
        win = tk.Toplevel(self, bg=bg)
        win.title("Make your own template - 4 steps")
        win.transient(self)
        win.resizable(False, False)
        win.protocol("WM_DELETE_WINDOW", self._tpl_close_guide)
        self.tpl_guide = win
        tk.Label(win, text="Making your own template", font=("Segoe UI", 13, "bold"), bg=bg,
                 fg="#4a2a6a").pack(anchor="w", padx=14, pady=(10, 0))
        tk.Label(win, text="Follow the steps in order, left to right. The step you are on is yellow, "
                           "finished steps are green with a tick.", font=("Segoe UI", 9), bg=bg, fg="#555555",
                 wraplength=900, justify="left").pack(anchor="w", padx=14, pady=(0, 4))
        row = tk.Frame(win, bg=bg)
        row.pack(fill="both", padx=8)
        self._tpl_step_boxes = []
        for n, (title, detail) in enumerate(self.GUIDE_STEPS, start=1):
            row.grid_columnconfigure(n - 1, weight=1, uniform="step")
            f = tk.Frame(row, bg="white", highlightthickness=2)
            f.grid(row=0, column=n - 1, sticky="nsew", padx=5, pady=4)
            badge = tk.Label(f, text=str(n), font=("Segoe UI", 18, "bold"), bg="white")
            badge.pack(anchor="w", padx=10, pady=(6, 0))
            head = tk.Label(f, text=title, font=("Segoe UI", 10, "bold"), anchor="w", justify="left",
                            wraplength=215, bg="white")
            head.pack(anchor="w", padx=10)
            body = tk.Label(f, text=detail, font=("Segoe UI", 9), anchor="w", justify="left", wraplength=215,
                            bg="white")
            body.pack(anchor="w", padx=10, pady=(2, 0))
            extra = tk.Label(f, text="", font=("Segoe UI", 9, "bold"), anchor="w", justify="left",
                             wraplength=215, bg="white")
            extra.pack(anchor="w", padx=10, pady=(4, 8))
            self._tpl_step_boxes.append((f, badge, head, body, extra, detail))
        foot = tk.Frame(win, bg=bg)
        foot.pack(fill="x", padx=14, pady=(2, 10))
        hide_var = tk.BooleanVar(value=self.tpl_hide_guide)
        win.hide_var = hide_var               # the window keeps its own variable alive
        tk.Checkbutton(foot, text="Don't show this again  (the ? button opens it any time)", bg=bg,
                       variable=hide_var, font=("Segoe UI", 9),
                       command=lambda v=hide_var: self._tpl_hide_changed(v)).pack(side="left")
        btn(foot, "Got it", "#6a3aa0", command=self._tpl_close_guide, width=8).pack(side="right")
        self._tpl_guide_refresh()
        self._tpl_place_guide(win)

    def _tpl_place_guide(self, win):
        """Put the guide fully on screen and clear of the whole Templates panel (text box, list and buttons).
        Tries: right of the panel, right of the calculator, above / below the panel, left of the calculator."""
        win.update_idletasks()
        w, h = win.winfo_reqwidth() + 16, win.winfo_reqheight() + 40   # plus the title bar and borders Windows adds
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        top_limit, bottom_limit = 0, sh - 60                      # leave room for the taskbar
        ax, aw = self.winfo_rootx(), self.winfo_width()
        panel = self.tpl_panel
        px, py, pw, ph = panel.winfo_rootx(), panel.winfo_rooty(), panel.winfo_width(), panel.winfo_height()
        side_y = py - 10
        # first choice: right of the Templates panel (over the mostly empty inspector area)
        candidates = [(px + pw + 8, side_y), (ax + aw + 8, side_y), (px, py - h - 8), (px, py + ph + 8),
                      (ax - w - 8, side_y), (px - w - 8, side_y)]

        def fits(x, y):
            return x >= 0 and y >= top_limit and x + w <= sw and y + h <= bottom_limit

        def clear_of_panel(x, y):
            m = 6
            return x + w + m <= px or px + pw + m <= x or y + h + m <= py or py + ph + m <= y

        for x, y in candidates:
            y = max(top_limit, min(y, bottom_limit - h))           # sideways positions may slide up or down
            if fits(x, y) and clear_of_panel(x, y):
                break
        else:                                                      # nowhere is clear: top-right corner
            x, y = max(0, sw - w - 10), top_limit
        win.geometry("+%d+%d" % (x, y))

    def _tpl_hide_changed(self, var):
        self.tpl_hide_guide = bool(var.get())
        self._tpl_write_file()

    def _tpl_close_guide(self):
        """Hide the guide now and destroy it on the next turn of Tk's event loop (destroying a window in the
        same breath as rebuilding the rows can crash Tk)."""
        win, self.tpl_guide = self.tpl_guide, None
        if win is not None:
            win.withdraw()
            self.after(0, lambda w=win: self._tpl_destroy_window(w))

    @staticmethod
    def _tpl_destroy_window(win):
        try:
            win.destroy()
        except tk.TclError:
            pass
        win.hide_var = None                   # let go of the Tk variable while Tk is still running

    def destroy(self):
        win, self.tpl_guide = getattr(self, "tpl_guide", None), None
        if win is not None:
            try:
                self.update()
                self._tpl_destroy_window(win)
            except tk.TclError:
                pass
        super().destroy()

    def _tpl_guide_refresh(self):
        """Colour the steps: done = green with a tick, the one to do now = yellow, the rest = plain."""
        if self.tpl_guide is None:
            return
        done = self._tpl_progress()
        current = next((k for k, d in enumerate(done) if not d), None)
        text = self.tpl_entry.get().strip()
        for k, (frame, badge, head, body, extra, detail) in enumerate(self._tpl_step_boxes):
            if done[k]:
                bg, edge, mark = "#dff3dc", "#5aa85a", "✓"
            elif k == current:
                bg, edge, mark = "#fff3c4", "#e0a000", str(k + 1)
            else:
                bg, edge, mark = "white", "#d0d0d0", str(k + 1)
            frame.configure(bg=bg, highlightbackground=edge, highlightcolor=edge)
            for w in (badge, head, body, extra):
                w.configure(bg=bg)
            badge.configure(text=mark, fg="#2a6a20" if done[k] else "#333333")
            body.configure(text=detail % (self.op_target + 1) if "%d" in detail else detail)
            extra.configure(text="")
        extra = self._tpl_step_boxes[0][4]
        if not text:
            extra.configure(text="Nothing typed yet.", fg="#777777")
        else:
            try:
                node = template_math.parse_math(text)
                n = template_math.empty_boxes(node)
                extra.configure(text="✓ Understood:  %s   (%d empty box%s)"
                                     % (template_math.describe(node), n, "" if n == 1 else "es"), fg="#2a6a20")
            except template_math.IncompleteMath as e:
                extra.configure(text="… keep typing.  %s" % e, fg="#777777")
            except ValueError as e:
                extra.configure(text="✗ %s" % e, fg="#b03010")

    def _tpl_restore_preview(self):
        """Take the last preview out of its row again (only if nothing has been changed in that row since)."""
        state, self._tpl_preview_state = self._tpl_preview_state, None
        if not state or state["row"] >= len(self.rows):
            return
        i = state["row"]
        if tuple(t for _k, t, _p in self._cards(i)) != state["shown"]:
            return                                    # the row was edited since: leave the user's work alone
        row = self.rows[i]
        row["node"] = state["snapshot"]
        row["sel"], row["is_result"] = None, False
        self._invalidate()
        self._render_row(i)

    def _tpl_preview(self):
        """Preview Posted: put the typed math into the target row so it can be seen (and tried out)."""
        text = self.tpl_entry.get().strip()
        node = self._tpl_build(text)
        if node is None:
            self._tpl_guide_refresh()
            return
        self._tpl_restore_preview()                   # a new preview replaces the previous one
        i = self.op_target
        snapshot = _copy_node(self.rows[i]["node"]) if not self.rows[i]["is_result"] else None
        self._place_operator_row(None, node=node)
        if snapshot is None:
            snapshot = row_tree.new_node("_number")
        self._tpl_preview_state = {"row": i, "snapshot": snapshot,
                                   "shown": tuple(t for _k, t, _p in self._cards(i))}
        self._tpl_previewed = text
        n = template_math.empty_boxes(node)
        self._say("Preview - posted in Row %d:\n  %s\n%s\nLike it? Press Save Template. "
                  "Not right? Change the text and press Preview Posted again."
                  % (i + 1, template_math.describe(node),
                     "%d empty square box%s to fill in." % (n, "" if n == 1 else "es") if n
                     else "No empty boxes, so press the keypad = key to calculate it."))
        self._tpl_guide_refresh()

    def _tpl_save(self):
        """Save Template: keep the typed math so it shows up in the Apply Template list."""
        text = self.tpl_entry.get().strip()
        node = self._tpl_build(text)
        if node is None:
            self._tpl_guide_refresh()
            return
        if text in self.saved_templates:
            self._say("Already saved: %s\nPick it in the list next to Apply Template." % text)
        else:
            self.saved_templates.append(text)
            problem = self._tpl_write_file()
            note = ("It is kept for next time too." if problem is None else
                    "(Could not write %s: %s. It will be forgotten when the window closes.)"
                    % (os.path.basename(self.template_path), problem))
            self.tpl_combo.configure(values=self.saved_templates)
            self._say("Saved template: %s\nPick it in the list next to Apply Template and press Apply Template "
                      "whenever you want it in a row. %s" % (text, note))
        self.tpl_combo.set(text)
        self._tpl_guide_refresh()

    def _tpl_apply(self):
        """Apply Template: put the chosen template into the target row, like an operator from Operators."""
        text = self.tpl_combo.get().strip()
        if not text:
            self._say("No template picked yet. Type some math in the text box, press Preview Posted, "
                      "then Save Template, then pick it in this list.")
            return
        node = self._tpl_build(text)
        if node is None:
            return
        self._tpl_restore_preview()                   # replace the preview instead of nesting inside it
        self._place_operator_row(None, node=node)
        self._tpl_applied = True
        self._tpl_guide_refresh()

    # ---------- advanced input popup ----------
    def _selected_box(self):
        """(row index, path) of the box the user clicked, or None."""
        order = [self.op_target] + [k for k in range(len(self.rows)) if k != self.op_target]
        for i in order:
            if i < len(self.rows):
                row = self.rows[i]
                if row["sel"] is not None and row["node"] is not None:
                    return i, row["sel"]
        return None

    def _refresh_adv_target(self):
        """Tell the Advanced Input window which box/input is selected and pre-pick the likely type."""
        lbl = getattr(self, "_adv_target_lbl", None)
        if getattr(self, "adv_popup", None) is None or lbl is None:
            return
        sel = self._selected_box()
        if sel is None:
            lbl.configure(text="No box selected - click a square box in the rows first.", fg="#b03010")
            return
        i, path = sel
        parent, j = row_tree.owner(self.rows[i]["node"], path)
        mod = parent["mod"]
        kinds = getattr(mod, "KINDS", [])
        names = getattr(mod, "INPUTS", [])
        kind = kinds[j] if j < len(kinds) else "list"
        name = names[j] if j < len(names) else "input %d" % (j + 1)
        lbl.configure(text="Box: %s > %s      suggested: %s" % (mod.NAME, name, advanced_input.kind_title(kind)),
                      fg="#106010")
        self._adv_select(kind)

    def _toggle_advanced(self):
        if getattr(self, "adv_popup", None) is not None:
            self.adv_popup.destroy()
            self.adv_popup = None
            return
        pop = tk.Toplevel(self, bg="#555555")
        pop.overrideredirect(True)
        pop.transient(self)
        outer = tk.Frame(pop, bg="#f4eefa")
        outer.pack(padx=1, pady=1)
        bar = tk.Frame(outer, bg="#4a2a6a")
        bar.grid(row=0, column=0, columnspan=2, sticky="ew")
        tk.Button(bar, text="x", bg="#c02020", fg="white", relief="flat", bd=0, width=3,
                  font=("Segoe UI", 9, "bold"), activebackground="#e03030",
                  command=self._toggle_advanced).pack(side="right")
        title = tk.Label(bar, text="Advanced Input  (drag to move)", bg="#4a2a6a", fg="white",
                         font=("Segoe UI", 9, "bold"), cursor="fleur")
        title.pack(side="left", fill="x", expand=True, pady=3)
        drag = {}

        def start_drag(e):
            drag["off"] = (e.x_root - pop.winfo_x(), e.y_root - pop.winfo_y())

        def do_drag(e):
            pop.geometry("+%d+%d" % (e.x_root - drag["off"][0], e.y_root - drag["off"][1]))

        for w in (bar, title):
            w.bind("<ButtonPress-1>", start_drag)
            w.bind("<B1-Motion>", do_drag)

        self._adv_target_lbl = tk.Label(outer, text="", bg="#f4eefa", anchor="w", wraplength=350,
                                        font=("Segoe UI", 9, "bold"))
        self._adv_target_lbl.grid(row=1, column=0, columnspan=2, sticky="ew", padx=6, pady=(6, 2))

        sbar = tk.Frame(outer, bg="#f4eefa")
        sbar.grid(row=2, column=0, columnspan=2, sticky="ew", padx=4, pady=2)
        tk.Label(sbar, text="Search:", bg="#f4eefa", font=("Segoe UI", 9)).pack(side="left")
        query = tk.StringVar()
        entry = tk.Entry(sbar, textvariable=query, font=("Segoe UI", 10))
        entry.pack(side="left", fill="x", expand=True, padx=(4, 2))
        entry.bind("<Button-1>", lambda e: entry.focus_force())
        tk.Button(sbar, text="✕", relief="flat", bg="#f4eefa", command=lambda: query.set("")).pack(side="left")

        canvas = tk.Canvas(outer, width=350, height=170, bg="#f4eefa", highlightthickness=0)
        vbar = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        hbar = ttk.Scrollbar(outer, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.grid(row=3, column=0)
        vbar.grid(row=3, column=1, sticky="ns")
        hbar.grid(row=4, column=0, sticky="ew")
        inner = tk.Frame(canvas, bg="#f4eefa")
        canvas.create_window((0, 0), window=inner, anchor="nw")

        # editor
        ed = tk.Frame(outer, bg="#f4eefa")
        ed.grid(row=5, column=0, columnspan=2, sticky="ew", padx=6, pady=4)
        kind_var = {"kind": "list"}
        head = tk.Label(ed, text="", bg="#f4eefa", anchor="w", font=("Segoe UI", 9, "bold"), fg="#4a2a6a")
        head.pack(fill="x")
        hint = tk.Label(ed, text="", bg="#f4eefa", anchor="w", justify="left", wraplength=340,
                        font=("Segoe UI", 8))
        hint.pack(fill="x")
        text = tk.Text(ed, height=4, width=46, font=("Consolas", 10), wrap="word")
        text.pack(fill="x", pady=3)
        text.bind("<Button-1>", lambda e: text.focus_force())
        msg = tk.Label(ed, text="", bg="#f4eefa", anchor="w", justify="left", wraplength=340,
                       font=("Segoe UI", 8, "bold"))
        msg.pack(fill="x")
        btns = tk.Frame(ed, bg="#f4eefa")
        btns.pack(fill="x", pady=(2, 0))

        def select_kind(kind):
            kind_var["kind"] = kind
            head.configure(text="Typing: " + advanced_input.kind_title(kind))
            h = next((k[2] for k in advanced_input.KINDS if k[0] == kind), "")
            hint.configure(text=h + "   Example: " + advanced_input.example(kind))
            text.delete("1.0", "end")
            msg.configure(text="")

        def use_example():
            text.delete("1.0", "end")
            text.insert("1.0", advanced_input.example(kind_var["kind"]))

        def put_in_box():
            sel = self._selected_box()
            if sel is None:
                msg.configure(text="Click a square box in the rows first.", fg="#b03010")
                return
            raw = text.get("1.0", "end").strip()
            try:
                val = advanced_input.parse(kind_var["kind"], raw)
            except ValueError as e:
                msg.configure(text=str(e), fg="#b03010")
                return
            i, path = sel
            row_tree.set_slot(self.rows[i]["node"], path, row_tree.advanced_slot(
                kind_var["kind"], raw, val, advanced_input.short_label(raw)))
            self._invalidate()
            self._render_row(i)
            self._sync_links()
            msg.configure(text="Put in the box. Press = on the number pad to calculate.", fg="#106010")

        def clear_box():
            sel = self._selected_box()
            if sel is not None:
                i, path = sel
                row_tree.set_slot(self.rows[i]["node"], path, "")
                self._set_result(i)
                self._render_row(i)
                self._sync_links()
            text.delete("1.0", "end")

        tk.Button(btns, text="Put in box", bg="#cfe9cf", font=("Segoe UI", 9, "bold"),
                  command=put_in_box).pack(side="left", padx=(0, 4))
        tk.Button(btns, text="Use example", bg="#e8e8e8", font=("Segoe UI", 9), command=use_example
                  ).pack(side="left", padx=4)
        tk.Button(btns, text="Clear box", bg="#f4d0d0", font=("Segoe UI", 9), command=clear_box
                  ).pack(side="left", padx=4)

        def wheel(e):
            canvas.yview_scroll(-1 * (e.delta // 120), "units")

        def populate(*_):
            for w in inner.winfo_children():
                w.destroy()
            q = query.get().strip().lower()
            shown = 0
            for kid, ttl, how, ex in advanced_input.KINDS:
                if q and q not in (ttl + " " + how + " " + ex).lower():
                    continue
                tk.Button(inner, text="%s\n    e.g.  %s" % (ttl, ex), anchor="w", justify="left", width=44,
                          bg="#e6d6f6", font=("Segoe UI", 9), command=lambda k=kid: select_kind(k)
                          ).pack(anchor="w", pady=1)
                shown += 1
            if not shown:
                tk.Label(inner, text="Nothing matches", bg="#f4eefa", font=("Segoe UI", 9, "italic")).pack(padx=10, pady=10)
            for w in inner.winfo_children():
                w.bind("<MouseWheel>", wheel)
            inner.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.yview_moveto(0)

        populate()
        query.trace_add("write", populate)
        canvas.bind("<MouseWheel>", wheel)
        canvas.bind("<Shift-MouseWheel>", lambda e: canvas.xview_scroll(-1 * (e.delta // 120), "units"))

        self._adv_select = select_kind
        self.adv_popup = pop
        select_kind("list")
        self._refresh_adv_target()
        self.focus_set()
        # place to the right of the keypad (beside the Operators pop-up if that is open)
        self.update_idletasks()
        pop.update_idletasks()
        pad = self.operators_btn.master
        x = pad.winfo_rootx() + pad.winfo_width() + 6
        op = getattr(self, "op_popup", None)
        if op is not None:
            x += op.winfo_width() + 6
        y = pad.winfo_rooty()
        y = max(0, min(y, self.winfo_screenheight() - pop.winfo_reqheight() - 50))
        x = max(0, min(x, self.winfo_screenwidth() - pop.winfo_reqwidth()))
        pop.geometry("%dx%d+%d+%d" % (pop.winfo_reqwidth(), pop.winfo_reqheight(), x, y))
        pop.update()
        pop.lift()

    # ---------- results ----------
    def _build_results(self):
        top = tk.Frame(self, bg="#f0f4f4")
        top.pack(fill="x", padx=8, pady=(10, 0))
        tk.Label(top, text="Detailed Results & Mathematical Analysis:",
                 font=("Segoe UI", 8, "bold"), bg="#f0f4f4").pack(side="left")
        for t in ["A -", "100%", "A +", "Wrap: ON", "Copy Results", "Expand ↑"]:
            btn(top, t, "#f4e8c0", fg="black", font=("Segoe UI", 7, "bold")).pack(side="right", padx=2)

        self.results = tk.Text(self, height=5, bg="white", fg="#106010",
                               font=("Consolas", 8), relief="flat")
        self.results.insert("1.0", "Mathematical and descriptive calculation results will appear here.")
        self.results.configure(state="disabled")
        self.results.pack(fill="x", padx=8, pady=2)

    # ---------- operators popup ----------
    def _word_catalog(self):
        """The algebra word problems, one per wording, loaded once from INDEX.md."""
        if getattr(self, "_word_catalog_items", None) is None:
            import algebra_word_problem_catalog as catalog
            self._word_catalog_items = catalog.load_catalog(os.path.join(WORD_DIR, "INDEX.md"))
        return self._word_catalog_items

    def _place_word_problem(self, item):
        """A Ready algebra word problem goes into the target row as `Name(□, □ ...) = □`, one box for every number
        in its text (in the order they appear).  A Reference problem only shows its diagram: nothing answers it yet."""
        if item["status"] != "Ready":
            self._say("%s %s is reference only: its text, steps and diagram are stored, but no solver answers it yet, so it is not placed in a row.\n%s"
                      % (item["category"], item["id"], item["problem"]))
            return
        key = row_tree.WORD_PREFIX + item["key"]
        self._place_operator_row(key)
        self._say("%s\n%s %s: the row is its equation. Each box holds a number from the text, already filled in: press =, or change a box first."
                  % (item["problem"], item["category"], item["id"]))

    def _show_word_diagram(self, item):
        """Open the problem's diagram. Clicking another problem uses the same window."""
        import algebra_word_problem_catalog as catalog
        path = catalog.diagram_path(WORD_DIR, item)
        win = getattr(self, "_word_diagram", None)
        if win is None or not win.winfo_exists():
            win = tk.Toplevel(self)
            win.configure(bg="white")
            self._word_diagram = win
            self._word_diagram_heading = tk.Label(win, bg="white", fg=BLUE, justify="left",
                                                  font=("Segoe UI", 11, "bold"))
            self._word_diagram_heading.pack(anchor="w", padx=12, pady=(10, 2))
            self._word_diagram_text = tk.Label(win, bg="white", fg="black", justify="left",
                                               wraplength=880, font=("Segoe UI", 10))
            self._word_diagram_text.pack(anchor="w", padx=12, pady=(0, 8))
            self._word_diagram_pic = tk.Label(win, bg="white")
            self._word_diagram_pic.pack(padx=12, pady=(0, 12))
        win.title("%s  %s" % (item["id"], item["category"]))
        self._word_diagram_heading.configure(text="%s    %s    %s" % (item["id"], item["category"], item["status"]))
        self._word_diagram_text.configure(text=item["problem"])
        if Image is None or not os.path.isfile(path):
            self._word_photo = None
            self._word_diagram_pic.configure(image="", text="The diagram file is not in the folder.")
        else:
            img = Image.open(path)
            img.thumbnail((960, 480))
            self._word_photo = ImageTk.PhotoImage(img)
            self._word_diagram_pic.configure(image=self._word_photo, text="")
        win.deiconify()
        win.lift()

    def _toggle_operators(self):
        if getattr(self, "op_popup", None) is not None:
            self.op_popup.destroy()
            self.op_popup = None
            return
        pop = tk.Toplevel(self, bg="#555555")
        pop.overrideredirect(True)
        pop.transient(self)
        outer = tk.Frame(pop, bg="#f0f4f4")
        outer.pack(padx=1, pady=1)
        self._op_dragged = False
        bar = tk.Frame(outer, bg="#333333")
        bar.grid(row=0, column=0, columnspan=2, sticky="ew")
        tk.Button(bar, text="x", bg="#c02020", fg="white", relief="flat", bd=0, width=3,
                  font=("Segoe UI", 9, "bold"), activebackground="#e03030",
                  command=self._toggle_operators).pack(side="right")
        title = tk.Label(bar, text="Operators  (drag to move)", bg="#333333", fg="white",
                         font=("Segoe UI", 9, "bold"), cursor="fleur")
        title.pack(side="left", fill="x", expand=True, pady=3)
        self._op_title = title

        def start_drag(e):
            self._drag_off = (e.x_root - pop.winfo_x(), e.y_root - pop.winfo_y())

        def do_drag(e):
            self._op_dragged = True
            pop.geometry(f"+{e.x_root - self._drag_off[0]}+{e.y_root - self._drag_off[1]}")

        for w in (bar, title):
            w.bind("<ButtonPress-1>", start_drag)
            w.bind("<B1-Motion>", do_drag)
        # search box
        sbar = tk.Frame(outer, bg="#f0f4f4")
        sbar.grid(row=1, column=0, columnspan=2, sticky="ew", padx=4, pady=4)
        tk.Label(sbar, text="Search:", bg="#f0f4f4", font=("Segoe UI", 9)).pack(side="left")
        query = tk.StringVar()
        entry = tk.Entry(sbar, textvariable=query, font=("Segoe UI", 10))
        entry.pack(side="left", fill="x", expand=True, padx=(4, 2))
        entry.bind("<Button-1>", lambda e: entry.focus_force())
        tk.Button(sbar, text="✕", relief="flat", bg="#f0f4f4", command=lambda: query.set("")
                  ).pack(side="left")

        canvas = tk.Canvas(outer, width=260, height=400, bg="#f0f4f4", highlightthickness=0)
        vbar = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        hbar = ttk.Scrollbar(outer, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.grid(row=2, column=0)
        vbar.grid(row=2, column=1, sticky="ns")
        hbar.grid(row=3, column=0, sticky="ew")
        # the algebra word problems replace this list while that view is open
        word_list = tk.Listbox(outer, width=62, height=24, bg="white", fg="black",
                               font=("Segoe UI", 9), activestyle="dotbox",
                               exportselection=False, highlightthickness=0, bd=0)
        self._op_mode = "operators"
        self._op_word_rows = []

        # picture of the selected operator (from its folder in operators_one_operator_per_file)
        prev = tk.Frame(outer, bg="white", height=175)
        prev.grid(row=4, column=0, columnspan=2, sticky="ew", padx=4, pady=4)
        prev.grid_propagate(False)
        prev_title = tk.Label(prev, text="Click an operator to see its picture", bg="white",
                              fg="#555555", font=("Segoe UI", 8, "bold"), wraplength=270)
        prev_title.pack(pady=(4, 0))
        prev_pic = tk.Label(prev, bg="white")
        prev_pic.pack(expand=True)
        # the key(s) needed to make this operator's math work, e.g. "+" for addition
        keys = tk.Frame(prev, bg="white")
        keys.pack(side="bottom", pady=(0, 6))

        def show_keys(key):
            for w in keys.winfo_children():
                w.destroy()
            tk.Label(keys, text="Key:", bg="white", font=("Segoe UI", 9, "bold")).pack(side="left", padx=(0, 4))
            for text in operator_keys(key):
                tk.Button(keys, text=text, bg="#fbd34d", relief="raised", bd=2, font=("Segoe UI", 11, "bold"),
                          padx=8, command=lambda: None).pack(side="left", padx=2)

        def show_picture(sec_name, label):
            key = LINKS.get((sec_name + "_OPS", label))
            if not key:
                return
            path = os.path.join(OPS_DIR, *key.split("/"), key.split("/")[-1] + ".jpg")
            self._place_operator_row(key)
            show_keys(key)
            spec = multirow_specs.get(key)
            prev_title.configure(text=label.split("   ")[-1] + "   [" + key + "]"
                                 + ("\nNeeds %d rows" % len(spec["rows"]) if spec else ""))
            if Image is None or not os.path.exists(path):
                prev_pic.configure(image="", text="(picture unavailable)")
                return
            img = Image.open(path)
            img.thumbnail((280, 85))
            self._op_photo = ImageTk.PhotoImage(img)      # keep a reference
            prev_pic.configure(image=self._op_photo, text="")

        inner = tk.Frame(canvas, bg="#f0f4f4")
        canvas.create_window((0, 0), window=inner, anchor="nw")
        sections = [("MATH", "#d6e6fa", MATH_OPS), ("GEOMETRY", "#d8f0d8", GEOMETRY_OPS),
                    ("PHYSICS", "#fbe4cf", PHYSICS_OPS)]
        back = tk.Button(sbar, text="← Operators", bg="#333333", fg="white", relief="flat",
                         font=("Segoe UI", 8, "bold"), command=lambda: show_operators())

        def wheel(e):
            canvas.yview_scroll(-1 * (e.delta // 120), "units")

        def show_operators():
            self._op_mode = "operators"
            title.configure(text="Operators → Row %d  (drag to move)" % (self.op_target + 1))
            back.pack_forget()
            word_list.grid_remove()
            canvas.grid(row=2, column=0)
            hbar.grid(row=3, column=0, sticky="ew")
            vbar.configure(command=canvas.yview)
            canvas.configure(yscrollcommand=vbar.set)
            populate()

        def show_words():
            self._op_mode = "words"
            title.configure(text="Algebra word problems")
            back.pack(side="left", padx=(0, 6))
            canvas.grid_remove()
            hbar.grid_remove()
            word_list.grid(row=2, column=0, sticky="nsew")
            vbar.configure(command=word_list.yview)
            word_list.configure(yscrollcommand=vbar.set)
            populate()

        def on_word(_event=None):
            sel = word_list.curselection()
            if not sel:
                return
            item = self._op_word_rows[sel[0]]
            if item is None:
                return
            prev_title.configure(text="%s   %s   [%s]" % (item["id"], item["category"], item["status"]))
            self._show_word_diagram(item)
            self._place_word_problem(item)

        word_list.bind("<<ListboxSelect>>", on_word)

        def populate(*_):
            q = query.get().strip().lower()
            if self._op_mode == "words":
                word_list.delete(0, "end")
                self._op_word_rows = []
                category = None
                any_problem = False
                for item in self._word_catalog():
                    blob = (item["id"] + " " + item["problem"] + " " + item["category"]).lower()
                    if q and q not in blob:
                        continue
                    if item["category"] != category:
                        category = item["category"]
                        word_list.insert("end", category)
                        word_list.itemconfig("end", fg=BLUE)
                        self._op_word_rows.append(None)
                    label = "%s   %s" % (item["id"], item["problem"])
                    if len(label) > 72:
                        label = label[:69] + "..."
                    word_list.insert("end", "    " + label)
                    word_list.itemconfig("end", fg="#2a6a20" if item["status"] == "Ready" else "#555555")
                    self._op_word_rows.append(item)
                    any_problem = True
                if not any_problem:
                    word_list.insert("end", "No matching problems")
                    self._op_word_rows.append(None)
                return
            for w in inner.winfo_children():
                w.destroy()
            shown = 0
            if not q or any(part in "algebra word problems" for part in q.split()):
                btn(inner, "Algebra word problems", "#fff3c4", fg="black", anchor="w", width=48,
                    font=("Segoe UI", 9, "bold"), command=show_words).pack(anchor="w", pady=(4, 2))
                shown += 1
            for sec, color, ops in sections:
                # keep a sub-heading only if something under it matches
                items, pending = [], None
                for label in ops:
                    if label.startswith("##"):
                        pending = label
                    elif not q or q in label.lower():
                        if pending:
                            items.append(pending)
                            pending = None
                        items.append(label)
                if not items:
                    continue
                tk.Label(inner, text=sec, bg="#333333", fg="white", anchor="w",
                         font=("Segoe UI", 8, "bold")).pack(fill="x", pady=(6, 2))
                for label in items:
                    if label.startswith("##"):
                        tk.Label(inner, text=label[2:].strip(), bg=color, fg="black", anchor="w",
                                 font=("Segoe UI", 8, "bold italic")).pack(fill="x", pady=(5, 1))
                    else:
                        spec = multirow_specs.get(LINKS.get((sec + "_OPS", label), ""))
                        btn(inner, label + ("   ▤ %d rows" % len(spec["rows"]) if spec else ""),
                            color, fg="black", anchor="w", width=48,
                            font=("Segoe UI", 9),
                            command=lambda s=sec, l=label: show_picture(s, l)).pack(anchor="w", pady=1)
                        shown += 1
            if not shown:
                tk.Label(inner, text="No matching operators", bg="#f0f4f4",
                         font=("Segoe UI", 9, "italic")).pack(padx=10, pady=10)
            for w in inner.winfo_children():
                w.bind("<MouseWheel>", wheel)
            inner.update_idletasks()
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.xview_moveto(0)
            canvas.yview_moveto(0)

        populate()
        query.trace_add("write", populate)
        canvas.bind("<MouseWheel>", wheel)
        inner.bind("<MouseWheel>", wheel)
        canvas.bind("<Shift-MouseWheel>", lambda e: canvas.xview_scroll(-1 * (e.delta // 120), "units"))
        self.op_popup = pop
        self._refresh_op_title()
        self._place_operators()
        if not getattr(self, "_op_bound", False):
            self.bind("<Configure>", lambda e: self._place_operators(), add="+")
            self._op_bound = True

    def _place_operators(self):
        pop = getattr(self, "op_popup", None)
        if pop is None or getattr(self, "_op_dragged", False):
            return
        b = self.operators_btn.master  # keypad frame
        x = b.winfo_rootx() + b.winfo_width() + 6
        y = b.winfo_rooty()
        pop.update_idletasks()      # keep the whole pop-up (incl. picture + key) on screen
        y = max(0, min(y, self.winfo_screenheight() - pop.winfo_reqheight() - 50))
        x = max(0, min(x, self.winfo_screenwidth() - pop.winfo_reqwidth()))
        pop.geometry(f"+{x}+{y}")
        pop.lift()

    # ---------- bottom ----------
    def _build_bottom(self):
        bottom = tk.Frame(self, bg="#f0f4f4")
        bottom.pack(fill="both", expand=True, padx=8, pady=8)

        # keypad
        pad = tk.Frame(bottom, bg="#f0f4f4")
        pad.pack(side="left", anchor="n", padx=(4, 10))
        keys = [
            [("(", PALE_BLUE, "black"), (")", PALE_BLUE, "black"), ("C", RED, "white"), ("Operators", PALE_BLUE, "black")],
            [("7", "#e8e8e8", "black"), ("8", "#e8e8e8", "black"), ("9", "#e8e8e8", "black"), ("Next Row (↓)", "#e8e8e8", "black")],
            [("4", "#e8e8e8", "black"), ("5", "#e8e8e8", "black"), ("6", "#e8e8e8", "black")],
            [("1", "#e8e8e8", "black"), ("2", "#e8e8e8", "black"), ("3", "#e8e8e8", "black")],
            [("0", "#e8e8e8", "black"), (".", "#e8e8e8", "black"), ("Backspace", "#e8e8e8", "black"), ("=", GREEN, "white")],
            [("±", "#e8e8e8", "black"), ("EE", "#e8e8e8", "black")],      # minus sign, power of ten (1e-34)
        ]
        for r, row in enumerate(keys):
            for c, (t, bg, fg) in enumerate(row):
                b = btn(pad, t, bg, fg=fg, width=16 if c == 3 else 8, height=1,
                        font=("Segoe UI", 8, "bold"))
                b.grid(row=r, column=c, padx=2, pady=2, ipady=2)
                if t == "Operators":
                    b.configure(command=self._toggle_operators)
                    self.operators_btn = b
                elif t in list("0123456789.") + ["±", "EE"]:
                    b.configure(command=lambda ch=t: self._key(ch))
                elif t == "Next Row (↓)":
                    b.configure(command=lambda: self._next_row())
                elif t == "Backspace":
                    b.configure(command=lambda: self._key("⌫"))
                elif t == "C":
                    b.configure(command=self._clear_all)
                elif t == "=":
                    b.configure(command=self._equals)
                    b.grid(row=2, column=3, rowspan=3, sticky="nsew", padx=2, pady=2)      # tall = key

        # Advanced Input: lists, matrices, functions, sets, graphs
        joinf = tk.Frame(pad, bg="#f0f4f4")
        joinf.grid(row=len(keys), column=0, columnspan=4, sticky="ew", pady=(6, 0))
        self.join_label = tk.Label(joinf, text="Join Row 2 to the rows above (helper card):", bg="#f0f4f4",
                                   font=("Segoe UI", 8, "bold"), fg="#b03010")
        self.join_label.grid(row=0, column=0, columnspan=10, sticky="w")
        for n, sym in enumerate(["+", "−", "×", "÷", "=", "≠", "<", ">", "≤", "≥"]):
            tk.Button(joinf, text=sym, width=2, bg="#fbd34d", font=("Segoe UI", 11, "bold"), relief="raised",
                      command=lambda sy=sym: self._join_key(sy)).grid(row=1, column=n, padx=1, pady=2, sticky="ew")
        for c in range(10):
            joinf.grid_columnconfigure(c, weight=1)
        self.adv_btn = btn(pad, "Advanced Input", "#e6d6f6", fg="black", font=("Segoe UI", 8, "bold"),
                           command=self._toggle_advanced)
        self.adv_btn.grid(row=len(keys) + 1, column=0, columnspan=4, sticky="ew", padx=2, pady=2, ipady=2)
        self._set_target_row(0)

        # templates + descriptive console
        mid = tk.Frame(bottom, bg="#f0f4f4")
        mid.pack(side="left", anchor="n", padx=6)

        tpl = tk.LabelFrame(mid, text="Mathematical Templates (Column 1)", fg=BLUE,
                            font=("Segoe UI", 8, "bold"), bg="#f0f4f4")
        tpl.pack(fill="x", ipadx=4, ipady=4)
        r1 = tk.Frame(tpl, bg="#f0f4f4")
        r1.pack(anchor="w", padx=4, pady=2)
        self.tpl_panel = tpl
        self.template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saved_templates.json")
        self.saved_templates, self.tpl_hide_guide = template_math.load_data(self.template_path)
        self.tpl_guide = None                 # the how-to pop-up, while it is open
        self._tpl_previewed = None            # the text that Preview Posted last put in a row
        self._tpl_preview_state = None        # what to put back when the preview is replaced
        self._tpl_applied = False
        self._tpl_was_empty = True
        self.tpl_combo = ttk.Combobox(r1, values=self.saved_templates, width=26, state="readonly")
        self.tpl_combo.pack(side="left")
        btn(r1, "Apply Template", "#cfe0f7", fg=BLUE, command=self._tpl_apply).pack(side="left", padx=4)
        btn(r1, "?", "#fff3c4", fg="#7a5a00", width=2,
            command=lambda: self._tpl_show_guide()).pack(side="left", padx=2)          # opens the how-to guide
        r2 = tk.Frame(tpl, bg="#f0f4f4")
        r2.pack(anchor="w", padx=4, pady=2)
        self.tpl_entry = tk.Entry(r2, width=26)
        self.tpl_entry.pack(side="left")
        self.tpl_entry.bind("<KeyRelease>", lambda e: self._tpl_typed())
        tk.Label(r2, text="=", bg="#f0f4f4", font=("Segoe UI", 11, "bold")).pack(side="left", padx=4)
        btn(r2, "Preview Posted", "#fbe4cf", fg="#c05000", command=self._tpl_preview).pack(side="left", padx=2)
        btn(r2, "Save Template", "#e8e8e8", fg="black", command=self._tpl_save).pack(side="left", padx=2)

        desc = tk.LabelFrame(mid, text="Descriptive Columns Console (Col 2 & 3)", fg=PURPLE,
                             font=("Segoe UI", 8, "bold"), bg="#f0f4f4")
        desc.pack(fill="x", pady=(14, 0), ipadx=4, ipady=4)
        ur = tk.Frame(desc, bg="#f0f4f4")
        ur.pack(anchor="w", padx=4, pady=2)
        tk.Label(ur, text="Unit:", font=("Segoe UI", 8, "bold"), bg="#f0f4f4").pack(side="left")
        for u in ["pens", "pencils", "books", "apples", "oranges", "cars"]:
            btn(ur, u, "#e8e8f8", fg="black", font=("Segoe UI", 8), command=lambda u=u: self._apply_word(0, u)).pack(side="left", padx=1)
        cr = tk.Frame(desc, bg="#f0f4f4")
        cr.pack(anchor="w", padx=4, pady=2)
        tk.Label(cr, text="Context:", font=("Segoe UI", 8, "bold"), bg="#f0f4f4").pack(side="left")
        for c in ["in the drawer", "on the desk", "in the room", "in the basket"]:
            btn(cr, c, "#fbe0e8", fg="#a01040", font=("Segoe UI", 8), command=lambda c=c: self._apply_word(1, c)).pack(side="left", padx=1)
        wr = tk.Frame(desc, bg="#f0f4f4")
        wr.pack(anchor="w", padx=4, pady=2)
        self.word_entry = tk.Entry(wr, width=22)
        self.word_entry.pack(side="left", padx=(40, 2))
        btn(wr, "Apply Word", "#e8e8e8", fg="black", command=lambda: self._apply_word(None, self.word_entry.get())).pack(side="left")

        # inspector
        insp = tk.Frame(bottom, bg="#f0f4f4")
        insp.pack(side="left", fill="both", expand=True, padx=(10, 0))
        tk.Label(insp, text="Addend Representations Inspector", fg=BLUE,
                 font=("Segoe UI", 8, "bold"), bg="#f0f4f4").pack(anchor="w")
        text = tk.Text(insp, bg="white", font=("Consolas", 7), relief="solid", bd=1)
        text.insert("1.0",
                    "=== TOTAL SUMMARY ===\n"
                    "Math Total: (not available: not calculated yet)\n\n"
                    "=== ROWS ===\n\n"
                    "--- Row 1 (Addend): pattern □ ---\n"
                    "  Editing tokens: []\n"
                    "  Number Group 1 (id c64a2f65): □ | Item (empty) | Context (empty)\n"
                    "  Calculated Terms: (not available: not calculated yet)\n")
        text.configure(state="disabled")
        text.pack(fill="both", expand=True)


if __name__ == "__main__":
    CalculatorGUI().mainloop()
