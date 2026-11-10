"""Operators that need MORE THAN ONE ROW, and what goes in each row.

When one of these operators is chosen in the Operators pop-up, the window adds the rows it needs,
puts the named operator into each row, writes the join symbol in the helper card of rows 2, 3, ...
and, when = is pressed, calculates every row and combines the results with the joins:

    total = row 1 result;   total = join(total, row k result)  for k = 2, 3, ...

SPECS[operator key] = {
    "title":  text shown to the user,
    "rows":   [ {"op": key of the operator in this row ("_number" = a plain number),
                 "title": what this row is for,
                 "fill": {box number: "typed value"  or  nested {"op": ..., "fill": ...}}  (optional)}, ... ],
    "joins":  [symbol between row 1 and 2, between the total and row 3, ...]   one fewer than rows
    "links":  [((row, path), (row, path)), ...]  optional: the first box copies the second, so the same
              u / point only has to be typed once.  A path is the box numbers from the row's operator
              inward, e.g. (1, 0) = box 0 of the operator sitting in box 1.
}
Join symbols:  +  −  ×  ÷  =  ≠  <  >  ≤  ≥
"""

_BRACKETS = {
    "title": "Brackets: work out the inside first, then use the result",
    "rows": [
        {"op": "math/arithmetic/addition", "title": "inside the brackets  ( □ + □ )"},
        {"op": "_number", "title": "outside the brackets  × □"},
    ],
    "joins": ["×"],
}

SPECS = {
    "math/differential_geometry_and_tensors/stokes_theorem": {
        "title": "Stokes' / Green's theorem (flat case): the line integral round the edge equals the "
                 "double integral of (∂Q/∂x − ∂P/∂y) over the inside",
        "rows": [
            {"op": "math/calculus/line_integral", "title": "∮ F · dr round the boundary"},
            {"op": "math/calculus/double_integral", "title": "∬ (∂Q/∂x − ∂P/∂y) dA over the region"},
        ],
        "joins": ["="],
    },
    "math/transforms_and_differential_equations/heat_equation": {
        "title": "Heat equation  ∂u/∂t = α · ∂²u/∂x²  (u uses x for position and y for time; point = [x, t])",
        "rows": [
            {"op": "math/calculus/partial_derivative", "title": "∂u/∂t", "fill": {2: "1"}},
            {"op": "math/arithmetic/multiplication", "title": "α · ∂²u/∂x²",
             "fill": {1: {"op": "math/calculus/second_partial_derivative", "fill": {2: "0"}}}},
        ],
        "joins": ["="],
        "links": [((1, (1, 0)), (0, (0,))), ((1, (1, 1)), (0, (1,)))],
    },
    "math/transforms_and_differential_equations/wave_equation": {
        "title": "Wave equation  ∂²u/∂t² = c² · ∂²u/∂x²  (u uses x for position and y for time; point = [x, t])",
        "rows": [
            {"op": "math/calculus/second_partial_derivative", "title": "∂²u/∂t²", "fill": {2: "1"}},
            {"op": "math/arithmetic/multiplication", "title": "c² · ∂²u/∂x²",
             "fill": {0: {"op": "math/algebra/square"},
                      1: {"op": "math/calculus/second_partial_derivative", "fill": {2: "0"}}}},
        ],
        "joins": ["="],
        "links": [((1, (1, 0)), (0, (0,))), ((1, (1, 1)), (0, (1,)))],
    },
    "math/transforms_and_differential_equations/laplace_s_equation": {
        "title": "Laplace's equation  ∂²u/∂x² + ∂²u/∂y² = 0  (point = [x, y])",
        "rows": [
            {"op": "math/calculus/second_partial_derivative", "title": "∂²u/∂x²", "fill": {2: "0"}},
            {"op": "math/calculus/second_partial_derivative", "title": "∂²u/∂y²", "fill": {2: "1"}},
            {"op": "_number", "title": "equals 0", "fill": {0: "0"}},
        ],
        "joins": ["+", "="],
        "links": [((1, (0,)), (0, (0,))), ((1, (1,)), (0, (1,)))],
    },
    "math/differential_geometry_and_tensors/exterior_derivative": {
        "title": "Exterior derivative. Row 1 is the product rule: d of f dx equals df wedged with dx. Row 2 says applying d twice gives the zero form.",
        "rows": [
            {"op": "math/differential_geometry_and_tensors/exterior_derivative", "title": "Product rule: d(f dx) = df ∧ dx"},
            {"op": "math/differential_geometry_and_tensors/exterior_derivative_nilpotent", "title": "Nilpotent: d of d is zero"},
        ],
        "joins": ["="],
    },
    "math/abstract_algebra/direct_sum": {
        "title": "Direct sum of two vector spaces. Row 1 is the sum A ⊕ B. Row 2 says its dimension is the sum of the two dimensions.",
        "rows": [
            {"op": "math/abstract_algebra/direct_sum", "title": "The sum: pairs (a, b) with component-wise operations"},
            {"op": "math/abstract_algebra/direct_sum_dimension", "title": "Dimension: dim(A ⊕ B) = dim A + dim B"},
        ],
        "joins": ["="],
    },
    "physics/physics/navier_stokes_equation": {
        "title": "Navier–Stokes equations for an incompressible fluid. u = (u, v, w) is the velocity of the fluid, ρ its density, μ its viscosity, p the pressure and f an outside force on each volume of fluid, such as gravity. Row 1 says: density × the fluid's acceleration = the push from pressure differences (−∇p) + the friction between layers of fluid (μ∇²u) + the outside force (f). The acceleration has two parts: ∂u/∂t is how the velocity changes in time at one point, and (u·∇)u is the change from being carried along by the flow. Rows 2, 3 and 4 are Row 1 written out for the x, y and z directions. Row 5, continuity, says ∂u/∂x + ∂v/∂y + ∂w/∂z = 0: the flow neither squeezes nor creates fluid. Each row is one equation, drawn on the same rows and columns as its diagram. Reference only: nothing is calculated.",
        "rows": [
            {"op": "physics/physics/navier_stokes_equation", "title": "Vector form: density × acceleration = pressure push + friction + outside force"},
            {"op": "physics/physics/navier_stokes_x_momentum", "title": "x direction: the same balance for the velocity u along x"},
            {"op": "physics/physics/navier_stokes_y_momentum", "title": "y direction: the same balance for the velocity v along y"},
            {"op": "physics/physics/navier_stokes_z_momentum", "title": "z direction: the same balance for the velocity w along z"},
            {"op": "physics/physics/navier_stokes_continuity", "title": "Continuity: the fluid is incompressible, so none is created or lost"},
        ],
        "joins": ["=", "=", "=", "="],
    },
    "math/optimization_and_numerical_methods/kkt_conditions": {
        "title": "KKT conditions (Karush–Kuhn–Tucker): the conditions a best point must meet when the problem has inequality constraints g(x) ≤ 0. Row 1, stationarity: the slope of the objective and the slopes of the constraints cancel. Row 2, primal feasibility: the point is allowed, every constraint is satisfied. Row 3, dual feasibility: each multiplier λ is not negative. Row 4, complementary slackness: a constraint that is slack has multiplier zero. Reference only: nothing is calculated.",
        "rows": [
            {"op": "math/optimization_and_numerical_methods/kkt_conditions", "title": "Stationarity: the slope of the objective and the slopes of the constraints cancel."},
            {"op": "math/optimization_and_numerical_methods/kkt_primal_feasibility", "title": "The point is allowed: every constraint is satisfied."},
            {"op": "math/optimization_and_numerical_methods/kkt_dual_feasibility", "title": "The multiplier pushes the right way: it is not negative."},
            {"op": "math/optimization_and_numerical_methods/kkt_complementary_slackness", "title": "A constraint that is slack has multiplier zero."},
        ],
        "joins": ["=", "=", "="],
    },
    "math/abstract_algebra/field_extension": {
        "title": "Field extension: K is a field that contains F as a subfield. Row 1 says K sits over F. Row 2 says the degree [K:F] is the dimension of K as a vector space over F. Reference only: nothing is calculated.",
        "rows": [
            {"op": "math/abstract_algebra/field_extension", "title": "K contains F."},
            {"op": "math/abstract_algebra/field_extension_degree", "title": "The degree is the dimension of K as a vector space over F."},
        ],
        "joins": ["="],
    },
    "math/constants_and_relations/open_bracket": _BRACKETS,
    "math/constants_and_relations/close_bracket": _BRACKETS,
    "math/constants_and_relations/square_brackets": _BRACKETS,
    "math/constants_and_relations/curly_braces": _BRACKETS,
}


def get(key):
    return SPECS.get(key)
