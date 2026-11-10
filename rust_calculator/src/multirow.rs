//! Operators that need MORE THAN ONE ROW (Python `operator_row_math/multirow_specs.py`).
//!
//! Choosing one of these in the Operators list adds the rows it needs, puts the named operator into each row, writes the join symbol of rows 2, 3 ... and,
//! when `=` is pressed, calculates every row and combines the results with the joins:  total = row 1;  total = join(total, row k)  for k = 2, 3 ...
//! `links` make a box copy another box, so the same u / point only has to be typed once.

/// What goes into a box of a row: typed text, or an operator with boxes of its own.
#[derive(Debug)]
pub enum Fill {
    Text(&'static str),
    Node(&'static NodeSpec),
}

/// An operator with some of its boxes pre-filled.
#[derive(Debug)]
pub struct NodeSpec {
    pub op: &'static str,
    pub fill: &'static [(usize, Fill)],
}

#[derive(Debug)]
pub struct RowSpec {
    pub title: &'static str,
    pub node: NodeSpec,
}

/// A link: the box `to` copies the box `from` (each given as (row, path of the box inside the row)).
pub type Link = ((usize, &'static [usize]), (usize, &'static [usize]));

#[derive(Debug)]
pub struct Spec {
    pub title: &'static str,
    pub rows: &'static [RowSpec],
    /// The join symbol between row 1 and 2, between the total and row 3 ...
    pub joins: &'static [&'static str],
    pub links: &'static [Link],
}

/// The multi-row operator laid out in the rows right now.
#[derive(Clone, Copy, Debug)]
pub struct Template {
    pub key: &'static str,
    pub spec: &'static Spec,
}

const PLAIN: &[(usize, Fill)] = &[];

static BRACKETS: Spec = Spec {
    title: "Brackets: work out the inside first, then use the result",
    rows: &[
        RowSpec { title: "inside the brackets  ( □ + □ )", node: NodeSpec { op: "math/arithmetic/addition", fill: PLAIN } },
        RowSpec { title: "outside the brackets  × □", node: NodeSpec { op: "_number", fill: PLAIN } },
    ],
    joins: &["×"],
    links: &[],
};

static STOKES: Spec = Spec {
    title: "Stokes' / Green's theorem (flat case): the line integral round the edge equals the double integral of (∂Q/∂x − ∂P/∂y) over the inside",
    rows: &[
        RowSpec { title: "∮ F · dr round the boundary", node: NodeSpec { op: "math/calculus/line_integral", fill: PLAIN } },
        RowSpec { title: "∬ (∂Q/∂x − ∂P/∂y) dA over the region", node: NodeSpec { op: "math/calculus/double_integral", fill: PLAIN } },
    ],
    joins: &["="],
    links: &[],
};

static SECOND_X: NodeSpec = NodeSpec { op: "math/calculus/second_partial_derivative", fill: &[(2, Fill::Text("0"))] };

static HEAT: Spec = Spec {
    title: "Heat equation  ∂u/∂t = α · ∂²u/∂x²  (u uses x for position and y for time; point = [x, t])",
    rows: &[
        RowSpec { title: "∂u/∂t", node: NodeSpec { op: "math/calculus/partial_derivative", fill: &[(2, Fill::Text("1"))] } },
        RowSpec { title: "α · ∂²u/∂x²", node: NodeSpec { op: "math/arithmetic/multiplication", fill: &[(1, Fill::Node(&SECOND_X))] } },
    ],
    joins: &["="],
    links: &[((1, &[1, 0]), (0, &[0])), ((1, &[1, 1]), (0, &[1]))],
};

static SQUARE: NodeSpec = NodeSpec { op: "math/algebra/square", fill: PLAIN };

static WAVE: Spec = Spec {
    title: "Wave equation  ∂²u/∂t² = c² · ∂²u/∂x²  (u uses x for position and y for time; point = [x, t])",
    rows: &[
        RowSpec { title: "∂²u/∂t²", node: NodeSpec { op: "math/calculus/second_partial_derivative", fill: &[(2, Fill::Text("1"))] } },
        RowSpec {
            title: "c² · ∂²u/∂x²",
            node: NodeSpec { op: "math/arithmetic/multiplication", fill: &[(0, Fill::Node(&SQUARE)), (1, Fill::Node(&SECOND_X))] },
        },
    ],
    joins: &["="],
    links: &[((1, &[1, 0]), (0, &[0])), ((1, &[1, 1]), (0, &[1]))],
};

static LAPLACE: Spec = Spec {
    title: "Laplace's equation  ∂²u/∂x² + ∂²u/∂y² = 0  (point = [x, y])",
    rows: &[
        RowSpec { title: "∂²u/∂x²", node: NodeSpec { op: "math/calculus/second_partial_derivative", fill: &[(2, Fill::Text("0"))] } },
        RowSpec { title: "∂²u/∂y²", node: NodeSpec { op: "math/calculus/second_partial_derivative", fill: &[(2, Fill::Text("1"))] } },
        RowSpec { title: "equals 0", node: NodeSpec { op: "_number", fill: &[(0, Fill::Text("0"))] } },
    ],
    joins: &["+", "="],
    links: &[((1, &[0]), (0, &[0])), ((1, &[1]), (0, &[1]))],
};

static NAVIER_STOKES: Spec = Spec {
    title: "Navier–Stokes equations for an incompressible fluid. u = (u, v, w) is the velocity of the fluid, ρ its density, μ its viscosity, p the pressure and f an outside force on each volume of fluid, such as gravity. Row 1 says: density × the fluid's acceleration = the push from pressure differences (−∇p) + the friction between layers of fluid (μ∇²u) + the outside force (f). The acceleration has two parts: ∂u/∂t is how the velocity changes in time at one point, and (u·∇)u is the change from being carried along by the flow. Rows 2, 3 and 4 are Row 1 written out for the x, y and z directions. Row 5, continuity, says ∂u/∂x + ∂v/∂y + ∂w/∂z = 0: the flow neither squeezes nor creates fluid. Each row is one equation, drawn on the same rows and columns as its diagram. Reference only: nothing is calculated.",
    rows: &[
        RowSpec { title: "Vector form: density × acceleration = pressure push + friction + outside force", node: NodeSpec { op: "physics/physics/navier_stokes_equation", fill: &[] } },
        RowSpec { title: "x direction: the same balance for the velocity u along x", node: NodeSpec { op: "physics/physics/navier_stokes_x_momentum", fill: &[] } },
        RowSpec { title: "y direction: the same balance for the velocity v along y", node: NodeSpec { op: "physics/physics/navier_stokes_y_momentum", fill: &[] } },
        RowSpec { title: "z direction: the same balance for the velocity w along z", node: NodeSpec { op: "physics/physics/navier_stokes_z_momentum", fill: &[] } },
        RowSpec { title: "Continuity: the fluid is incompressible, so none is created or lost", node: NodeSpec { op: "physics/physics/navier_stokes_continuity", fill: &[] } },
    ],
    joins: &["=", "=", "=", "="],
    links: &[],
};

/// The multi-row operators, by operator key.
pub fn get(key: &str) -> Option<&'static Spec> {
    Some(match key {
        "math/differential_geometry_and_tensors/stokes_theorem" => &STOKES,
        "math/transforms_and_differential_equations/heat_equation" => &HEAT,
        "math/transforms_and_differential_equations/wave_equation" => &WAVE,
        "math/transforms_and_differential_equations/laplace_s_equation" => &LAPLACE,
        "physics/physics/navier_stokes_equation" => &NAVIER_STOKES,
        "math/constants_and_relations/open_bracket"
        | "math/constants_and_relations/close_bracket"
        | "math/constants_and_relations/square_brackets"
        | "math/constants_and_relations/curly_braces" => &BRACKETS,
        _ => return None,
    })
}
