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
    "math/constants_and_relations/open_bracket": _BRACKETS,
    "math/constants_and_relations/close_bracket": _BRACKETS,
    "math/constants_and_relations/square_brackets": _BRACKETS,
    "math/constants_and_relations/curly_braces": _BRACKETS,
}


def get(key):
    return SPECS.get(key)
