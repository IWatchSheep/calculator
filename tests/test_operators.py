"""Independent verification of every operator in operators_one_operator_per_file/.

Run from the project root (standard library only, no pytest needed):

    python tests/test_operators.py            # run everything
    python tests/test_operators.py -v         # list every test
    python -m unittest tests.test_operators   # same thing

Expected values are worked out BY HAND or from textbook identities (e.g. sin(pi/2) = 1,
C(5,2) = 10, det [[1,2],[3,4]] = -2).  They are NOT copied from the code's own output.
"""
import math
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from operators_one_operator_per_file import get, load_all, diagram_path  # noqa: E402

OPS_DIR = os.path.join(ROOT, "operators_one_operator_per_file")
PI, E = math.pi, math.e


def approx(actual, expected, tol=1e-6):
    """Recursive tolerant comparison for numbers, complex numbers, lists, tuples, dicts, sets."""
    if isinstance(expected, bool) or isinstance(actual, bool):
        return actual is expected or actual == expected
    if isinstance(expected, (int, float, complex)) and isinstance(actual, (int, float, complex)):
        if actual == expected:
            return True
        if expected == 0:                      # nothing to scale by: small absolute slack
            return abs(actual) <= 1e-9
        return abs(actual - expected) <= tol * abs(expected)
    if isinstance(expected, dict):
        return (isinstance(actual, dict) and set(actual) == set(expected)
                and all(approx(actual[k], expected[k], tol) for k in expected))
    if isinstance(expected, (list, tuple)) and isinstance(actual, (list, tuple)):
        return len(actual) == len(expected) and all(approx(a, e, tol) for a, e in zip(actual, expected))
    return actual == expected


# --------------------------------------------------------------------------- 1. structure
def _index_text():
    with open(os.path.join(OPS_DIR, "INDEX.md"), encoding="utf-8") as fh:
        return fh.read()


class StructureTests(unittest.TestCase):
    """Every operator folder is complete and consistent with the rest of the project."""

    @classmethod
    def setUpClass(cls):
        cls.ops = load_all()

    def test_operator_count(self):
        self.assertEqual(len(self.ops), 507)

    def test_every_operator_has_required_metadata(self):
        for key, m in self.ops.items():
            for attr in ("NAME", "SYMBOL", "CATEGORY", "SUBCATEGORY", "FORMULA", "compute"):
                self.assertTrue(hasattr(m, attr), f"{key} is missing {attr}")
            self.assertTrue(callable(m.compute), key)

    def test_every_operator_has_a_diagram(self):
        for key in self.ops:
            self.assertTrue(os.path.isfile(diagram_path(key)), f"{key}: missing .jpg")

    def test_diagrams_are_valid_jpegs(self):
        try:
            from PIL import Image
        except ImportError:
            self.skipTest("Pillow not installed")
        for key in self.ops:
            with Image.open(diagram_path(key)) as im:
                im.verify()

    def test_index_md_lists_every_operator(self):
        text = _index_text()
        for key in self.ops:
            self.assertIn(f"`{key}/`", text, f"{key} not in INDEX.md")

    def test_index_ready_vs_reference_matches_code(self):
        """INDEX.md says Ready/Reference; Reference operators must raise NotImplementedError."""
        text = _index_text()
        status = {m.group(2): m.group(1)
                  for m in re.finditer(r"\| (Ready|Reference) \| `([^`]+)/` \|", text)}
        self.assertEqual(len(status), 507)
        for key, st in status.items():
            if st == "Reference":
                with self.assertRaises(NotImplementedError, msg=key):
                    self.ops[key].compute()

    def test_operator_links_point_to_real_operators(self):
        import operator_links
        for (section, label), key in operator_links.LINKS.items():
            self.assertIn(key, self.ops, f"operator_links: {label!r} -> unknown {key}")

    def test_every_operator_has_a_row_module(self):
        import operator_row_math
        missing = sorted(set(self.ops) - set(operator_row_math.keys()))
        self.assertEqual(missing, [], f"no operator_row_math folder for: {missing}")

    def test_all_python_files_compile(self):
        import py_compile
        for folder, dirs, files in os.walk(ROOT):
            dirs[:] = [d for d in dirs if d not in (".venv", ".git", "__pycache__", ".idea")]
            for f in files:
                if f.endswith(".py"):
                    py_compile.compile(os.path.join(folder, f), doraise=True)


# --------------------------------------------------------------------------- 2. numeric table
M = "math/"
A = M + "arithmetic/"
AL = M + "algebra/"
TR = M + "trigonometry/"
GE = "geometry/geometry/"
PH = "physics/physics/"
CA = M + "calculus/"
DN = M + "discrete_and_number_theory/"
LA = M + "linear_algebra/"
ST = M + "statistics_and_probability/"
LS = M + "logic_and_sets/"
GT = M + "graph_theory_and_combinatorics/"
OP = M + "optimization_and_numerical_methods/"
RA = M + "real_analysis/"
TP = M + "topology/"
TD = M + "transforms_and_differential_equations/"
CX = M + "complex_analysis/"
CR = M + "constants_and_relations/"
AA = M + "abstract_algebra/"
CT = M + "category_theory_and_foundations/"
DG = M + "differential_geometry_and_tensors/"

# (operator key, args tuple, expected value)
CASES = [
    # ---- arithmetic
    (A + "addition", (2, 3), 5), (A + "addition", (-2, 3), 1), (A + "addition", (0.1, 0.2), 0.3),
    (A + "subtraction", (5, 3), 2), (A + "subtraction", (3, 5), -2),
    (A + "multiplication", (4, -3), -12), (A + "multiplication", (0, 99), 0),
    (A + "division", (7, 2), 3.5), (A + "division", (-9, 3), -3),
    (A + "modulo", (7, 3), 1), (A + "modulo", (-7, 3), 2), (A + "modulo", (7.5, 2), 1.5),
    (A + "fraction", (1, 2), 0.5), (A + "fraction", (3, 4), 0.75),
    (A + "absolute_value", (-4,), 4), (A + "absolute_value", (4,), 4), (A + "absolute_value", (0,), 0),
    (A + "negate", (5,), -5), (A + "negate", (-5,), 5),
    (A + "reciprocal", (4,), 0.25), (A + "reciprocal", (-0.5,), -2),
    (A + "round_down", (-1.5,), -2), (A + "round_down", (2.9,), 2),
    (A + "round_up", (-1.5,), -1), (A + "round_up", (2.1,), 3),
    (A + "round_nearest", (2.6,), 3), (A + "round_nearest", (2.4,), 2), (A + "round_nearest", (-2.6,), -3),
    (A + "minimum", (3, 1, 2), 1), (A + "maximum", (3, 1, 2), 3), (A + "maximum", (-5, -9), -5),
    # ---- algebra
    (AL + "power", (2, 10), 1024), (AL + "power", (9, 0.5), 3), (AL + "power", (5, 0), 1),
    (AL + "power", (2, -2), 0.25),
    (AL + "square", (-3,), 9), (AL + "cube", (-2,), -8),
    (AL + "square_root", (144,), 12), (AL + "square_root", (2,), 2 ** 0.5),
    (AL + "nth_root", (27, 3), 3), (AL + "nth_root", (16, 4), 2),
    (AL + "cube_root", (-27,), -3), (AL + "cube_root", (8,), 2),
    (AL + "exponential", (0,), 1), (AL + "exponential", (1,), E),
    (AL + "power_of_ten", (3,), 1000), (AL + "power_of_ten", (-1,), 0.1),
    (AL + "log_base_10", (1000,), 3), (AL + "log_base_10", (1,), 0),
    (AL + "natural_log", (E,), 1), (AL + "natural_log", (1,), 0),
    (AL + "log_any_base", (8, 2), 3), (AL + "log_any_base", (81, 3), 4),
    (AL + "discriminant", (1, -3, 2), 1), (AL + "discriminant", (1, 2, 1), 0),
    (AL + "discriminant", (1, 0, 1), -4),
    (AL + "quadratic_formula", (1, -3, 2), (2, 1)), (AL + "quadratic_formula", (1, 0, 1), (1j, -1j)),
    (AL + "binomial_theorem", (2, 3, 2), 25), (AL + "binomial_theorem", (1, 1, 3), 8),
    (AL + "difference_of_squares", (5, 3), (2, 8)),
    (AL + "slope_intercept_form", (2, 3, 1), 7),
    (AL + "arithmetic_sequence", (2, 3, 5), 14), (AL + "arithmetic_series_sum", (2, 3, 5), 40),
    (AL + "geometric_sequence", (2, 3, 4), 54), (AL + "geometric_series_sum", (2, 3, 4), 80),
    (AL + "complex_number", (3, 4), 3 + 4j), (AL + "imaginary_unit", (), 1j),
    (AL + "modulus_of_complex_number", (3 + 4j,), 5), (AL + "complex_conjugate", (3 + 4j,), 3 - 4j),
    (AL + "solve_system_of_equations", ([[2, 1], [1, 3]], [5, 10]), [1, 3]),
    (AL + "expand", ("(x+1)(x-1)",), "x² - 1"),
    (AL + "simplify", ("2*x+3*x",), "5x"),
    # ---- trigonometry (radians)
    (TR + "sine", (PI / 2,), 1), (TR + "sine", (0,), 0), (TR + "sine", (PI / 6,), 0.5),
    (TR + "cosine", (0,), 1), (TR + "cosine", (PI,), -1), (TR + "cosine", (PI / 3,), 0.5),
    (TR + "tangent", (PI / 4,), 1), (TR + "tangent", (0,), 0),
    (TR + "cosecant", (PI / 2,), 1), (TR + "secant", (0,), 1), (TR + "cotangent", (PI / 4,), 1),
    (TR + "inverse_sine", (1,), PI / 2), (TR + "inverse_cosine", (0,), PI / 2),
    (TR + "inverse_cosine", (1,), 0), (TR + "inverse_tangent", (1,), PI / 4),
    (TR + "two_argument_arctangent", (1, 1), PI / 4), (TR + "two_argument_arctangent", (1, -1), 3 * PI / 4),
    (TR + "hyperbolic_sine", (0,), 0), (TR + "hyperbolic_cosine", (0,), 1), (TR + "hyperbolic_tangent", (0,), 0),
    (TR + "hyperbolic_sine", (1,), (E - 1 / E) / 2), (TR + "hyperbolic_cosine", (1,), (E + 1 / E) / 2),
    (TR + "inverse_hyperbolic_sine", (0,), 0), (TR + "inverse_hyperbolic_cosine", (1,), 0),
    (TR + "inverse_hyperbolic_tangent", (0,), 0),
    (TR + "pythagorean_identity", (1.234,), 1), (TR + "double_angle", (PI / 6,), math.sqrt(3) / 2),
    (TR + "half_angle", (PI,), 1), (TR + "angle_sum", (PI / 6, PI / 3), 1),
    (TR + "degrees_to_radians", (180,), PI), (TR + "degrees_to_radians", (90,), PI / 2),
    (TR + "radians_to_degrees", (PI,), 180), (TR + "radians_to_degrees", (PI / 2,), 90),
    # ---- geometry
    (GE + "circle_area", (2,), 4 * PI), (GE + "circle_circumference", (3,), 6 * PI),
    (GE + "arc_length", (2, PI / 2), PI), (GE + "sector_area", (2, PI), 2 * PI),
    (GE + "cone_volume", (3, 4), 12 * PI), (GE + "cone_surface_area", (3, 5), 24 * PI),
    (GE + "cube_volume", (3,), 27), (GE + "cube_surface_area", (3,), 54),
    (GE + "cylinder_volume", (2, 5), 20 * PI), (GE + "cylinder_surface_area", (2, 5), 28 * PI),
    (GE + "sphere_volume", (3,), 36 * PI), (GE + "sphere_surface_area", (3,), 36 * PI),
    (GE + "degrees_to_radians_geometry", (180,), PI), (GE + "radians_to_degrees_geometry", (PI,), 180),
    (GE + "distance_formula", (0, 0, 3, 4), 5), (GE + "midpoint_formula", (0, 0, 4, 6), (2, 3)),
    (GE + "slope", (0, 0, 2, 4), 2), (GE + "slope", (1, 5, 3, 1), -2),
    (GE + "heron_s_formula", (3, 4, 5), 6),
    (GE + "law_of_cosines", (3, 4, PI / 2), 5), (GE + "law_of_sines", (1, PI / 6, PI / 2), 2),
    (GE + "parallelogram_area", (4, 3), 12), (GE + "polygon_interior_angle_sum", (5,), 540),
    (GE + "polygon_interior_angle_sum", (3,), 180), (GE + "pyramid_volume", (9, 4), 12),
    (GE + "pythagorean_theorem", (5, 12), 13),
    (GE + "rectangle_area", (3, 4), 12), (GE + "rectangle_perimeter", (3, 4), 14),
    (GE + "rectangular_prism_volume", (2, 3, 4), 24), (GE + "rectangular_prism_surface_area", (2, 3, 4), 52),
    (GE + "regular_polygon_area", (20, 3), 30), (GE + "rhombus_area", (6, 8), 24),
    (GE + "square_area", (5,), 25), (GE + "trapezoid_area", (3, 5, 2), 8), (GE + "triangle_area", (6, 4), 12),
    # ---- physics
    (PH + "acceleration", (10, 2), 5), (PH + "capacitance", (2, 3), 6),
    (PH + "centripetal_acceleration", (10, 5), 20), (PH + "coulomb_s_law", (1e-6, 1e-6, 1), 8.9875517923e-3),
    (PH + "density", (10, 2), 5), (PH + "displacement", (0, 2, 3), 9), (PH + "displacement", (1, 2, 3), 12),
    (PH + "electric_power", (2, 5), 10), (PH + "final_velocity", (1, 2, 3), 7), (PH + "frequency", (0.5,), 2),
    (PH + "gravitation", (1, 1, 1), 6.674e-11), (PH + "heat", (2, 4, 5), 40), (PH + "hooke_s_law", (10, 0.5), -5),
    (PH + "ideal_gas_law", (1, 273.15, 0.0224), 8.314462618 * 273.15 / 0.0224),
    (PH + "impulse", (5, 2), 10), (PH + "kinetic_energy", (2, 3), 9),
    (PH + "mass_energy_equivalence", (1,), 299792458 ** 2), (PH + "momentum", (2, 3), 6),
    (PH + "newton_s_second_law", (2, 5), 10), (PH + "ohm_s_law", (2, 5), 10),
    (PH + "pendulum_period", (9.81,), 2 * PI), (PH + "potential_energy", (2, 3), 58.86),
    (PH + "power_physics", (100, 5), 20), (PH + "pressure", (10, 2), 5),
    (PH + "resistors_in_parallel", ([2, 2],), 1), (PH + "resistors_in_parallel", ([6, 3],), 2),
    (PH + "resistors_in_series", ([1, 2, 3],), 6), (PH + "snell_s_law", (1, PI / 6, 1), PI / 6),
    (PH + "snell_s_law", (1, PI / 6, 2), math.asin(0.25)), (PH + "torque", (2, 3, PI / 2), 6),
    (PH + "velocity", (10, 2), 5), (PH + "velocity_squared", (0, 2, 4), 4), (PH + "wave_speed", (2, 3), 6),
    (PH + "weight", (2,), 19.62), (PH + "work", (3, 4), 12),
    # ---- discrete & number theory
    (DN + "combinations", (5, 2), 10), (DN + "combinations", (5, 0), 1), (DN + "combinations", (10, 10), 1),
    (DN + "permutations", (5, 2), 20), (DN + "factorial", (5,), 120), (DN + "factorial", (0,), 1),
    (DN + "fibonacci", (10,), 55), (DN + "fibonacci", (0,), 0), (DN + "fibonacci", (1,), 1),
    (DN + "euler_s_totient", (10,), 4), (DN + "euler_s_totient", (12,), 4), (DN + "euler_s_totient", (13,), 12),
    (DN + "greatest_common_divisor", (12, 18), 6), (DN + "greatest_common_divisor", (17, 5), 1),
    (DN + "least_common_multiple", (4, 6), 12), (DN + "inclusion_exclusion", (5, 4, 2), 7),
    (DN + "modular_arithmetic", (-7, 3), 2), (DN + "modular_arithmetic", (17, 5), 2),
    (DN + "pigeonhole_principle", (10, 3), 4), (DN + "pigeonhole_principle", (9, 3), 3),
    (DN + "prime_check", (97,), True), (DN + "prime_check", (91,), False), (DN + "prime_check", (1,), False),
    (DN + "prime_check", (2,), True), (DN + "prime_factorization", (360,), [2, 2, 2, 3, 3, 5]),
    # ---- linear algebra
    (LA + "determinant", ([[1, 2], [3, 4]],), -2), (LA + "determinant", ([[2, 0, 0], [0, 3, 0], [0, 0, 4]],), 24),
    (LA + "dot_product", ([1, 2, 3], [4, 5, 6]), 32), (LA + "cross_product", ([1, 0, 0], [0, 1, 0]), [0, 0, 1]),
    (LA + "cross_product", ([1, 2, 3], [4, 5, 6]), [-3, 6, -3]),
    (LA + "trace", ([[1, 2], [3, 4]],), 5), (LA + "transpose", ([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]]),
    (LA + "identity_matrix", (3,), [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    (LA + "matrix_add", ([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[6, 8], [10, 12]]),
    (LA + "matrix_subtract", ([[5, 6], [7, 8]], [[1, 2], [3, 4]]), [[4, 4], [4, 4]]),
    (LA + "matrix_multiply", ([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[19, 22], [43, 50]]),
    (LA + "scalar_multiply", (3, [[1, 2], [3, 4]]), [[3, 6], [9, 12]]),
    (LA + "matrix_inverse", ([[1, 2], [3, 4]],), [[-2, 1], [1.5, -0.5]]),
    (LA + "matrix_rank", ([[1, 2], [2, 4]],), 1), (LA + "matrix_rank", ([[1, 0], [0, 1]],), 2),
    (LA + "norm", ([3, 4],), 5), (LA + "norm", ([3, 4], 1), 7), (LA + "vector_magnitude", ([2, 3, 6],), 7),
    (LA + "unit_vector", ([3, 4],), [0.6, 0.8]), (LA + "vector_projection", ([3, 4], [1, 0]), [3, 0]),
    (LA + "solve_ax_b", ([[2, 1], [1, 3]], [5, 10]), [1, 3]),
    (LA + "characteristic_polynomial", ([[2, 0], [0, 3]],), [1, -5, 6]),
    (LA + "row_reduce_rref", ([[1, 2], [3, 4]],), [[1, 0], [0, 1]]),
    # ---- statistics & probability
    (ST + "mean", ([1, 2, 3, 4],), 2.5), (ST + "median", ([3, 1, 2],), 2), (ST + "median", ([1, 2, 3, 4],), 2.5),
    (ST + "mode", ([1, 2, 2, 3],), 2), (ST + "range", ([4, 9, 1],), 8),
    (ST + "variance", ([2, 4, 4, 4, 5, 5, 7, 9],), 4), (ST + "standard_deviation", ([2, 4, 4, 4, 5, 5, 7, 9],), 2),
    (ST + "sample_variance", ([1, 2, 3, 4, 5],), 2.5),
    (ST + "sample_standard_deviation", ([1, 2, 3, 4, 5],), math.sqrt(2.5)),
    (ST + "covariance", ([1, 2, 3], [2, 4, 6]), 2), (ST + "correlation", ([1, 2, 3], [2, 4, 6]), 1),
    (ST + "correlation", ([1, 2, 3], [6, 4, 2]), -1),
    (ST + "expected_value", ([1, 2, 3], [0.2, 0.3, 0.5]), 2.3),
    (ST + "variance_of_random_variable", ([0, 1], [0.5, 0.5]), 0.25),
    (ST + "binomial_distribution", (5, 2, 0.5), 0.3125), (ST + "poisson_distribution", (0, 1), 1 / E),
    (ST + "poisson_distribution", (2, 3), 9 * math.exp(-3) / 2),
    (ST + "normal_distribution", (0,), 1 / math.sqrt(2 * PI)), (ST + "exponential_distribution", (0, 2), 2),
    (ST + "uniform_distribution", (1, 0, 4), 0.25), (ST + "uniform_distribution", (5, 0, 4), 0),
    (ST + "z_score", (70, 60, 5), 2), (ST + "t_test_statistic", (52, 50, 4, 16), 2),
    (ST + "conditional_probability", (0.2, 0.5), 0.4), (ST + "bayes_theorem", (0.9, 0.01, 0.1), 0.09),
    (ST + "probability", (1, 6), 1 / 6), (ST + "chi_square_statistic", ([10, 20], [15, 15]), 25 / 15 + 25 / 15),
    (ST + "confidence_interval", (100, 10, 100), (98.04, 101.96)),
    (ST + "percentile", ([1, 2, 3, 4, 5], 50), 3),
    (ST + "p_value", (0,), 1.0),
    # ---- logic & sets
    (LS + "and", (True, False), False), (LS + "and", (True, True), True),
    (LS + "or", (False, False), False), (LS + "or", (True, False), True), (LS + "not", (True,), False),
    (LS + "xor", (True, True), False), (LS + "xor", (True, False), True),
    (LS + "implies", (True, False), False), (LS + "implies", (False, False), True),
    (LS + "implies", (True, True), True),
    (LS + "if_and_only_if", (True, True), True), (LS + "if_and_only_if", (True, False), False),
    (LS + "union", ({1, 2}, {2, 3}), {1, 2, 3}), (LS + "intersection", ({1, 2}, {2, 3}), {2}),
    (LS + "set_difference", ({1, 2, 3}, {2}), {1, 3}), (LS + "complement", ({1}, {1, 2, 3}), {2, 3}),
    (LS + "cardinality", ({4, 5, 6},), 3), (LS + "element_of", (2, {1, 2}), True),
    (LS + "not_element_of", (2, {1, 2}), False), (LS + "subset_or_equal", ({1}, {1}), True),
    (LS + "proper_subset", ({1}, {1}), False), (LS + "proper_subset", ({1}, {1, 2}), True),
    (LS + "empty_set", (), set()), (LS + "for_all", (lambda x: x > 0, [1, 2, 3]), True),
    (LS + "for_all", (lambda x: x > 1, [1, 2, 3]), False),
    (LS + "there_exists", (lambda x: x > 2, [1, 2, 3]), True),
    (LS + "there_exists", (lambda x: x > 5, [1, 2, 3]), False),
    # ---- constants & relations
    (CR + "pi", (), PI), (CR + "euler_s_number", (), E), (CR + "golden_ratio", (), (1 + 5 ** 0.5) / 2),
    (CR + "euler_mascheroni_constant", (), 0.5772156649015329),
    (CR + "equals", (3, 3), True), (CR + "equals", (3, 4), False), (CR + "not_equal", (3, 4), True),
    (CR + "greater_than", (4, 3), True), (CR + "greater_than", (3, 3), False),
    (CR + "greater_than_or_equal", (3, 3), True), (CR + "less_than", (3, 4), True),
    (CR + "less_than_or_equal", (4, 3), False), (CR + "approximately_equal", (0.1 + 0.2, 0.3), True),
    (CR + "approximately_equal", (1, 1.1), False), (CR + "proportional_to", (2, 6), 3),
    # ---- calculus (numerical, so compared with tolerance)
    (CA + "derivative", (lambda x: x ** 2, 3), 6), (CA + "derivative", (math.sin, 0), 1),
    (CA + "second_derivative", (lambda x: x ** 3, 2), 12),
    (CA + "partial_derivative", (lambda x, y: x * x * y, [2, 3], 0), 12),
    (CA + "partial_derivative", (lambda x, y: x * x * y, [2, 3], 1), 4),
    (CA + "second_partial_derivative", (lambda x, y: x ** 3 + y, [2, 0], 0), 12),
    (CA + "gradient", (lambda x, y: x * x + y * y, [1, 2]), [2, 4]),
    (CA + "definite_integral", (lambda x: x ** 2, 0, 3), 9), (CA + "definite_integral", (math.sin, 0, PI), 2),
    (CA + "double_integral", (lambda x, y: x * y, 0, 2, 0, 3), 9),
    (CA + "triple_integral", (lambda x, y, z: 1, 0, 1, 0, 2, 0, 3), 6),
    (CA + "limit", (lambda x: math.sin(x) / x, 0), 1),
    (CA + "l_hopital_s_rule", (math.sin, lambda x: x, 0), 1),
    (CA + "summation", ([1, 2, 3, 4],), 10), (CA + "product", ([1, 2, 3, 4],), 24),
    (CA + "chain_rule", (3, 4), 12), (CA + "product_rule", (2, 3, 4, 5), 3 * 4 + 2 * 5),
    (CA + "quotient_rule", (6, 1, 2, 1), (1 * 2 - 6 * 1) / 4),
    (CA + "taylor_series", ([1, 1, 1, 1], 0, 1), 1 + 1 + 1 / 2 + 1 / 6),
    (CA + "maclaurin_series", ([1] * 10, 1), sum(1 / math.factorial(n) for n in range(10))),
    (CA + "divergence", (lambda x, y, z: [x, y, z], [1, 2, 3]), 3),
    (CA + "curl", (lambda x, y, z: [-y, x, 0], [1, 2, 3]), [0, 0, 2]),
    (CA + "laplacian", (lambda x, y, z: x * x + y * y + z * z, [1, 1, 1]), 6),
    (CA + "infinity", (), math.inf),
    # ---- optimization & numerical
    (OP + "newton_s_method", (lambda x: x * x - 2, lambda x: 2 * x, 1), 2 ** 0.5),
    (OP + "bisection_method", (lambda x: x * x - 2, 0, 2), 2 ** 0.5),
    (OP + "secant_method", (lambda x: x * x - 2, 1, 2), 2 ** 0.5),
    (OP + "fixed_point_iteration", (math.cos, 1), 0.7390851332151607),
    (OP + "simpson_s_rule", (lambda x: x ** 2, 0, 3), 9), (OP + "trapezoid_rule", (lambda x: x, 0, 4), 8),
    (OP + "lagrange_interpolation", ([0, 1, 2], [0, 1, 4], 3), 9),
    (OP + "newton_interpolation", ([0, 1, 2], [0, 1, 4], 3), 9),
    (OP + "gaussian_elimination", ([[2, 1], [1, 3]], [5, 10]), [1, 3]),
    (OP + "jacobi_iteration", ([[4, 1], [2, 5]], [9, 12]), [33 / 18, 30 / 18]),
    (OP + "gauss_seidel_iteration", ([[4, 1], [2, 5]], [9, 12]), [33 / 18, 30 / 18]),
    (OP + "gradient_descent", (lambda p: [2 * p[0]], [5.0], 0.1, 500), [0]),
    (OP + "minimize", (lambda x: (x - 2) ** 2, -5, 5), (2, 0)),  # returns (x, f(x))
    (OP + "maximize", (lambda x: -(x - 2) ** 2, -5, 5), (2, 0)),
    (OP + "hessian", (lambda x, y: x * x + 3 * y * y, [0, 0]), [[2, 0], [0, 6]]),
    # ---- graph theory & combinatorics
    (GT + "adjacency_matrix", (3, [(0, 1), (1, 2)]), [[0, 1, 0], [1, 0, 1], [0, 1, 0]]),
    (GT + "bell_number", (5,), 52), (GT + "catalan_number", (5,), 42), (GT + "partition_number", (5,), 7),
    (GT + "stirling_number_second_kind", (5, 2), 15), (GT + "stirling_number_second_kind", (4, 2), 7),
    (GT + "vertex_degree", ({"A": ["B", "C"], "B": ["A"], "C": ["A"]}, "A"), 2),
    (GT + "recurrence_relation", ([1, 1], [0, 1], 10), 55),
    (GT + "shortest_path_dijkstra", ({"A": [("B", 4), ("C", 1)], "B": [("C", 2)], "C": []}, "A"),
     {"A": 0, "B": 4, "C": 1}),
    (GT + "burnside_s_lemma", ([4, 0, 2, 0],), 1.5),
    (GT + "generating_function", ([1, 1, 1], 2), 7),
    # ---- real analysis
    (RA + "supremum", ([1, 5, 3],), 5), (RA + "infimum", ([1, 5, 3],), 1),
    (RA + "inner_product", ([1, 2, 3], [4, 5, 6]), 32), (RA + "radius_of_convergence", (0.5,), 2),
    (RA + "lipschitz_ratio", (lambda x: 3 * x, 1, 2), 3),
    (RA + "lp_norm", (lambda x: 1, 0, 1), 1),
    (RA + "ratio_test", (1, 0.5), 0.5), (RA + "root_test", (0.25, 2), 0.5),
    # ---- topology
    (TP + "euler_characteristic", (8, 12, 6), 2), (TP + "metric_space_distance", ([0, 0], [3, 4]), 5),
    (TP + "open_ball", (lambda a, b: abs(a - b), 0, 0.5, 1), True),
    (TP + "open_ball", (lambda a, b: abs(a - b), 0, 2, 1), False),
    # ---- transforms & differential equations
    (TD + "convolution", ([1, 2], [3, 4]), [3, 10, 8]),
    (TD + "discrete_fourier_transform", ([1, 0, 0, 0],), [1, 1, 1, 1]),
    (TD + "inverse_discrete_fourier_transform", ([1, 1, 1, 1],), [1, 0, 0, 0]),
    (TD + "heaviside_step", (-1,), 0), (TD + "heaviside_step", (1,), 1), (TD + "heaviside_step", (0,), 0.5),
    (TD + "dirac_delta", (1,), 0), (TD + "wronskian", (1, 0, 2, 3), 3),
    (TD + "laplace_transform", (lambda t: 1, 2), 0.5),
    (TD + "z_transform", ([1, 1, 1], 2), 1 + 0.5 + 0.25),
    (TD + "characteristic_equation", (1, -3, 2), (2, 1)),
    # ---- complex analysis
    (CX + "real_part", (3 + 4j,), 3), (CX + "imaginary_part", (3 + 4j,), 4), (CX + "argument", (1j,), PI / 2),
    (CX + "euler_s_formula", (PI,), -1 + 0j), (CX + "de_moivre_s_theorem", (1, PI / 2, 2), -1 + 0j),
    (CX + "mobius_transformation", (1, 0, 0, 1, 5), 5),
    # ---- abstract algebra
    (AA + "symmetric_group_order", (4,), 24), (AA + "alternating_group_order", (4,), 12),
    (AA + "quotient_group_order", (12, 3), 4), (AA + "order_of_group", ([1, 2, 3],), 3),
    (AA + "order_of_element", (1, lambda a, b: (a + b) % 6, 0), 6),
    (AA + "order_of_element", (2, lambda a, b: (a + b) % 6, 0), 3),
    (AA + "tensor_product", ([1, 2], [3, 4]), [3, 4, 6, 8]),
    (AA + "dimension", ([[1, 0], [0, 1], [1, 1]],), 2),
    # ---- category theory & foundations
    (CT + "cartesian_product", ({1, 2}, {3}), [(1, 3), (2, 3)]),
    (CT + "power_set", ({1, 2},), [set(), {1}, {2}, {1, 2}]),
    (CT + "injective", (lambda x: x * 2, [1, 2, 3]), True), (CT + "injective", (lambda x: x * x, [-1, 1]), False),
    (CT + "surjective", (lambda x: x % 2, [0, 1, 2, 3], [0, 1]), True),
    (CT + "bijective", (lambda x: x + 1, [1, 2, 3], [2, 3, 4]), True),
    # ---- differential geometry
    (DG + "gaussian_curvature", (2, 3), 6),
]

# second batch: structures, graphs, decompositions, ODEs, topology (hand-checked)
_Z6, _ADD6 = list(range(6)), (lambda a, b: (a + b) % 6)
_MOD3 = lambda x: x % 3
_ADD3 = lambda a, b: (a + b) % 3
_P3 = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}                      # path A-B-C
_K3 = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}            # triangle
_TOPO = [set(), {1}, {1, 2}]                                         # Sierpinski space on {1, 2}
CASES += [
    # ---- abstract algebra (Z6 under addition mod 6)
    (AA + "group", (_Z6, _ADD6), True), (AA + "group", ([0, 1, 2], _ADD6), False),
    (AA + "subgroup", ([0, 2, 4], _Z6, _ADD6), True), (AA + "subgroup", ([0, 1], _Z6, _ADD6), False),
    (AA + "normal_subgroup", ([0, 3], _Z6, _ADD6), True),
    (AA + "coset", (1, [0, 3], _ADD6), {1, 4}), (AA + "cyclic_group", (2, _ADD6, 0), [2, 4, 0]),
    (AA + "direct_product", ([0, 1], [0, 1]), [(0, 0), (0, 1), (1, 0), (1, 1)]),
    (AA + "homomorphism", (_MOD3, _Z6, _ADD6, _ADD3), True), (AA + "kernel", (_MOD3, _Z6, 0), {0, 3}),
    (AA + "image", (_MOD3, _Z6), {0, 1, 2}), (AA + "isomorphism", (lambda x: x, _Z6, _Z6, _ADD6, _ADD6), True),
    (AA + "basis", ([[1, 0], [0, 1], [1, 1]],), [[1, 0], [0, 1]]),
    (AA + "field", (5,), True), (AA + "field", (6,), False),
    (AA + "integral_domain", (5,), True), (AA + "integral_domain", (6,), False),
    # ---- algebra / calculus
    (AL + "factor", ("x**2-5*x+6",), "(x - 2) (x - 3)"), (AL + "solve_for_x", (lambda x: x * x - 4,), [-2, 2]),
    (CA + "indefinite_integral", (lambda x: 2 * x, 3, 0), 9),
    (CA + "line_integral", (lambda x, y: [y, x], lambda t: [t, t], 0, 1), 1),
    (CA + "differential_equation", (lambda x, y: y, 0, 1, 1), E),
    # ---- category theory & foundations
    (CT + "function", (lambda x: x + 1, 2), 3), (CT + "integers", (5,), True),
    (CT + "natural_numbers", (5,), True), (CT + "natural_numbers", (-5,), False),
    (CT + "rational_numbers", (3, 6), 0.5), (CT + "complex_numbers", (1, 2), 1 + 2j),
    (CT + "quaternions", (1, 2, 3, 4), math.sqrt(30)), (CT + "real_numbers", (2.5,), True),
    (CT + "axiom_of_choice", ([{1, 2}, {3}],), [1, 3]),
    # ---- complex analysis
    (CX + "contour_integral", (lambda z: 1 / z, 0, 1), 2j * PI), (CX + "residue", (lambda z: 1 / z, 0), 1),
    (CX + "residue_theorem", (lambda z: 1 / z, 0, 1), 2j * PI),
    (CX + "cauchy_integral_formula", (lambda z: z * z, 1, 0.5), 1),
    (CX + "cauchyriemann_equations", (lambda x, y: x * x - y * y, lambda x, y: 2 * x * y, 1, 1), (True, 0, 0)),
    # ---- differential geometry
    (DG + "metric_tensor", ([[1, 0], [0, 1]], [1, 2], [3, 4]), 11), (DG + "wedge_product", ([1, 0], [0, 1]), [1]),
    (DG + "tensor_contraction", ([[1, 2], [3, 4]],), 5),
    (DG + "lie_bracket", (lambda x, y: [1, 0], lambda x, y: [0, 1], [0, 0]), [0, 0]),
    (DG + "tangent_vector", (lambda t: [t, t * t], 2), [1, 4]),
    # ---- graphs
    (GT + "tree", (_P3,), True), (GT + "tree", (_K3,), False), (GT + "graph", ({"A": ["B"], "B": ["A"]},), (2, 1)),
    (GT + "cycle", (_K3,), True), (GT + "cycle", (_P3,), False),
    (GT + "bipartite_graph", (_P3,), True), (GT + "bipartite_graph", (_K3,), False),
    (GT + "chromatic_number", (_K3,), 3), (GT + "chromatic_number", (_P3,), 2),
    (GT + "euler_path", (_P3,), True), (GT + "hamiltonian_path", (_P3,), ["A", "B", "C"]),
    (GT + "path", (_P3, "A", "C"), ["A", "B", "C"]), (GT + "planar_graph", (_K3,), True),
    (GT + "spanning_tree", ({"A": [("B", 1), ("C", 3)], "B": [("A", 1), ("C", 2)], "C": [("A", 3), ("B", 2)]},),
     ([("A", "B", 1), ("B", "C", 2)], 3)),
    (GT + "max_flow_min_cut", ({"S": [("A", 3), ("B", 2)], "A": [("T", 2)], "B": [("T", 3)], "T": []}, "S", "T"), 4),
    # ---- linear algebra decompositions
    (LA + "eigenvalues", ([[2, 0], [0, 3]],), (2, 3)), (LA + "eigenvalues", ([[2, 1], [1, 2]],), (1, 3)),
    (LA + "null_space", ([[1, 1], [2, 2]],), [[-1, 1]]), (LA + "column_space", ([[1, 2], [2, 4]],), [[1, 2]]),
    (LA + "lu_decomposition", ([[4, 3], [6, 3]],), ([[1, 0], [1.5, 1]], [[4, 3], [0, -1.5]])),
    (LA + "qr_decomposition", ([[3, 0], [4, 5]],), ([[0.6, -0.8], [0.8, 0.6]], [[5, 4], [0, 3]])),
    (LA + "singular_value_decomposition", ([[3, 0], [0, 4]],), [4, 3]),
    # ---- optimization & ODE solvers
    (OP + "euler_s_method", (lambda x, y: y, 0, 1, 0.5, 2), [(0, 1), (0.5, 1.5), (1.0, 2.25)]),
    (OP + "linear_programming", ([3, 2], [[1, 1], [1, 3]], [4, 6]), ([4, 0], 12)),
    (OP + "simplex_method", ([3, 2], [[1, 1], [1, 3]], [4, 6]), ([4, 0], 12)),
    (OP + "least_squares", ([0, 1, 2], [1, 3, 5]), (2, 1)), (OP + "spline", ([0, 1, 2], [0, 1, 4], 1.5), 2.3125),
    (OP + "convex_function", (lambda x: x * x, -1, 3), True),
    (OP + "lagrange_multipliers", (lambda x, y: x + y, lambda x, y: x * x + y * y - 2, [1, 1]), (0.5, 0)),
    (TD + "first_order_ode", (lambda x, y: y, 0, 1, 1), E),
    (TD + "second_order_ode", (lambda x, y, v: -y, 0, 1, 0, PI), -1),
    (TD + "separable_equation", (lambda x: 1, lambda y: y, 0, 1, 1), E),
    (TD + "integrating_factor", (lambda x: 1, 0, 1), E), (TD + "fourier_series", (lambda x: x, 1), (0, 2)),
    (TD + "variation_of_parameters", (math.cos, math.sin, lambda x: 1, 0, 1), 1 - math.cos(1)),
    # ---- real analysis
    (RA + "riemann_sum", (lambda x: x, 0, 1, 4), 0.375), (RA + "riemannstieltjes_sum", (lambda x: x, lambda x: x * x, [0, 1, 2]), 3),
    (RA + "limit_inferior", ([1, 2, 1, 2, 1, 2, 1, 2],), 1), (RA + "limit_superior", ([1, 2, 1, 2, 1, 2, 1, 2],), 2),
    (RA + "mean_value_theorem", (lambda x: x * x, 0, 2), 2),
    (RA + "intermediate_value_theorem", (lambda x: x * x, 0, 2, 2), 2 ** 0.5),
    (RA + "convergence", ([1, 1.5, 1.9, 2], 2, 0.5), 2), (RA + "alternating_series_test", ([1, 1 / 2, 1 / 3, 1 / 4],), (True, 0.25)),
    (RA + "comparison_test", ([1, 2, 3], [2, 3, 4]), True),
    (RA + "series_convergence_test", ([1, 0.5, 0.25, 0.125],), (0.5, "converges (ratio < 1)")),
    (RA + "integral_test", (lambda x: 1 / x ** 2, 10), (sum(1 / n ** 2 for n in range(1, 11)), 0.9)),
    (RA + "lebesgue_integral", (lambda x: x, 0, 2), 2), (RA + "measure", ([(0, 1), (2, 4)],), 3),
    (RA + "outer_measure", ([(0, 1), (2, 4)],), 3),
    # ---- statistics
    (ST + "quartiles", ([1, 2, 3, 4, 5, 6, 7, 8],), [2.25, 4.5, 6.75]),
    (ST + "interquartile_range", ([1, 2, 3, 4, 5, 6, 7, 8],), 4.5), (ST + "linear_regression", ([1, 2, 3], [2, 4, 6]), (2, 0)),
    # ---- topology (Sierpinski space)
    (TP + "open_set", (_TOPO, {1}), True), (TP + "closed_set", (_TOPO, {2}), True),
    (TP + "closure", (_TOPO, {1}), {1, 2}), (TP + "interior", (_TOPO, {1, 2}), {1, 2}),
    (TP + "boundary", (_TOPO, {1}), {2}), (TP + "connected", (_TOPO,), True), (TP + "hausdorff", (_TOPO,), False),
    (TP + "neighborhood", (_TOPO, 1, {1, 2}), True), (TP + "subspace_topology", (_TOPO, {1}), {frozenset(), frozenset({1})}),
    (TP + "basis_of_topology", (_TOPO, [set(), {1}, {1, 2}]), True), (TP + "cauchy_sequence", ([1, 1.1, 1.01, 1.001], 0.5), 0),
]

# new physics operators: magnetism, fluid dynamics, quantum mechanics, optics, relativity
CASES += [
    # ---- Magnetism
    (PH + "magnetic_force_on_charge", (2, 3, 4, PI / 2), 24),
    (PH + "magnetic_force_on_charge", (2, 3, 4, PI / 6), 12),
    (PH + "magnetic_force_on_charge", (2, 3, 4, 0), 0),
    (PH + "magnetic_force_on_wire", (2, 3, 4, PI / 2), 24),
    (PH + "magnetic_force_on_wire", (2, 3, 4, PI / 6), 12),
    (PH + "magnetic_field_straight_wire", (1, 1), 2e-7),
    (PH + "magnetic_field_straight_wire", (10, 0.5), 4e-6),
    (PH + "magnetic_field_solenoid", (1000, 2), 8 * PI * 1e-4),
    (PH + "magnetic_field_solenoid", (0, 5), 0),
    (PH + "magnetic_flux", (2, 3, 0), 6),
    (PH + "magnetic_flux", (2, 3, PI / 3), 3),
    (PH + "magnetic_flux", (2, 3, PI / 2), 0),
    (PH + "faradays_law", (10, 0.5, 2), -2.5),
    (PH + "faradays_law", (1, -4, 2), 2),
    (PH + "self_induced_emf", (2, 3, 0.5), -12),
    (PH + "self_induced_emf", (0.1, -5, 0.01), 50),
    (PH + "inductor_energy", (2, 3), 9),
    (PH + "inductor_energy", (0.5, 4), 4),
    (PH + "cyclotron_radius", (2, 3, 1, 4), 1.5),
    (PH + "cyclotron_radius", (2, 3, -1, 4), 1.5),
    (PH + "motional_emf", (0.5, 2, 3), 3),
    (PH + "motional_emf", (0, 2, 3), 0),
    # ---- Fluid dynamics
    (PH + "buoyant_force", (1000, 0.002), 19.62),
    (PH + "buoyant_force", (1000, 0), 0),
    (PH + "hydrostatic_pressure", (1000, 10), 98100),
    (PH + "hydrostatic_pressure", (1000, 0), 0),
    (PH + "continuity_equation", (2, 3, 1.5), 4),
    (PH + "continuity_equation", (1, 5, 1), 5),
    (PH + "bernoulli_equation", (100000, 2, 0, 4, 1, 1000), 84190),
    (PH + "bernoulli_equation", (5, 1, 0, 1, 0, 1000), 5),
    (PH + "reynolds_number", (1000, 2, 0.1, 0.001), 200000),
    (PH + "reynolds_number", (1000, 0, 0.1, 0.001), 0),
    (PH + "poiseuille_flow", (0.01, 1000, 0.001, 1), PI * 1.25e-3),
    (PH + "poiseuille_flow", (0.02, 1000, 0.001, 1), PI * 20e-3),
    (PH + "torricelli_speed", (5,), math.sqrt(98.1)),
    (PH + "torricelli_speed", (0,), 0),
    (PH + "stokes_drag", (0.001, 0.01, 2), 6 * PI * 0.001 * 0.01 * 2),
    (PH + "stokes_drag", (0.001, 0.01, 0), 0),
    (PH + "volume_flow_rate", (0.5, 4), 2),
    (PH + "volume_flow_rate", (0.5, 0), 0),
    (PH + "hydraulic_press", (100, 0.01, 0.5), 5000),
    (PH + "hydraulic_press", (10, 1, 1), 10),
    # ---- Quantum mechanics
    (PH + "photon_energy", (1e15,), 6.62607015e-19),
    (PH + "photon_energy", (0,), 0),
    (PH + "photon_momentum", (500e-9,), 1.32521403e-27),
    (PH + "photon_momentum", (1,), 6.62607015e-34),
    (PH + "de_broglie_wavelength", (1, 1), 6.62607015e-34),
    (PH + "de_broglie_wavelength", (2, 3), 6.62607015e-34 / 6),
    (PH + "heisenberg_uncertainty", (1e-10,), 1.054571817e-34 / 2e-10),
    (PH + "heisenberg_uncertainty", (1,), 1.054571817e-34 / 2),
    (PH + "photoelectric_effect", (1e15, 3e-19), 3.62607015e-19),
    (PH + "photoelectric_effect", (1e14, 3e-19), 0),
    (PH + "bohr_energy_level", (1,), -13.605693122994),
    (PH + "bohr_energy_level", (2,), -13.605693122994 / 4),
    (PH + "bohr_energy_level", (1, 2), -54.422772491976),
    (PH + "rydberg_formula", (1, 2), 4 / (3 * 10973731.568160)),
    (PH + "rydberg_formula", (2, 3), 36 / (5 * 10973731.568160)),
    (PH + "particle_in_a_box", (2, 1, 1), 6.62607015e-34 ** 2 / 2),
    (PH + "particle_in_a_box", (1, 2, 1), 6.62607015e-34 ** 2 / 16),
    (PH + "quantum_harmonic_oscillator", (0, 2), 1.054571817e-34),
    (PH + "quantum_harmonic_oscillator", (2, 2), 5 * 1.054571817e-34),
    (PH + "compton_shift", (PI / 2,), 2.42631023867e-12),
    (PH + "compton_shift", (PI,), 2 * 2.42631023867e-12),
    (PH + "compton_shift", (0,), 0),
    # ---- Optics
    (PH + "thin_lens_equation", (10, 30), 15),
    (PH + "thin_lens_equation", (10, 20), 20),
    (PH + "thin_lens_equation", (10, 5), -10),
    (PH + "lens_magnification", (15, 30), -0.5),
    (PH + "lens_magnification", (-10, 5), 2),
    (PH + "lensmakers_equation", (1.5, 0.2, -0.2), 0.2),
    (PH + "lensmakers_equation", (1.5, 0.1, math.inf), 0.2),
    (PH + "critical_angle", (1.5, 1), math.asin(2 / 3)),
    (PH + "critical_angle", (2, 1), PI / 6),
    (PH + "brewster_angle", (1, 1), PI / 4),
    (PH + "brewster_angle", (1, 1.5), math.atan(1.5)),
    (PH + "double_slit_fringe_spacing", (500e-9, 2, 1e-3), 1e-3),
    (PH + "double_slit_fringe_spacing", (600e-9, 1, 1e-3), 6e-4),
    (PH + "diffraction_grating", (1, 500e-9, 2e-6), math.asin(0.25)),
    (PH + "diffraction_grating", (2, 500e-9, 1e-6), PI / 2),
    (PH + "diffraction_grating", (0, 500e-9, 1e-6), 0),
    (PH + "malus_law", (100, PI / 3), 25),
    (PH + "malus_law", (100, 0), 100),
    (PH + "malus_law", (100, PI / 2), 0),
    (PH + "refractive_index", (2e8,), 299792458 / 2e8),
    (PH + "refractive_index", (299792458,), 1),
    # ---- Relativity
    (PH + "lorentz_factor", (0.6, 1), 1.25),
    (PH + "lorentz_factor", (0.8, 1), 5 / 3),
    (PH + "lorentz_factor", (0, 1), 1),
    (PH + "lorentz_factor", (0.6 * 299792458,), 1.25),
    (PH + "time_dilation", (1, 0.6, 1), 1.25),
    (PH + "time_dilation", (10, 0.8, 1), 50 / 3),
    (PH + "length_contraction", (100, 0.8, 1), 60),
    (PH + "length_contraction", (100, 0, 1), 100),
    (PH + "relativistic_momentum", (2, 0.6, 1), 1.5),
    (PH + "relativistic_momentum", (1, 0, 1), 0),
    (PH + "relativistic_kinetic_energy", (1, 0.6, 1), 0.25),
    (PH + "relativistic_kinetic_energy", (2, 0.8, 1), 2 * (5 / 3 - 1)),
    (PH + "energy_momentum_relation", (3, 4, 1), 5),
    (PH + "energy_momentum_relation", (0, 2, 1), 2),
    (PH + "energy_momentum_relation", (1, 0, 1), 1),
    (PH + "relativistic_velocity_addition", (0.5, 0.5, 1), 0.8),
    (PH + "relativistic_velocity_addition", (1, 0.5, 1), 1),
    (PH + "relativistic_velocity_addition", (0, 0.3, 1), 0.3),
    (PH + "relativistic_doppler", (100, 0.6, 1), 50),
    (PH + "relativistic_doppler", (100, -0.6, 1), 200),
    (PH + "relativistic_doppler", (100, 0, 1), 100),
    (PH + "schwarzschild_radius", (1, 1, 1), 2),
    (PH + "schwarzschild_radius", (1.989e30,), 2 * 6.674e-11 * 1.989e30 / 299792458 ** 2),
    (PH + "gravitational_time_dilation", (100, 1, 4, 1, 1), 100 * math.sqrt(0.5)),
    (PH + "gravitational_time_dilation", (100, 0, 4, 1, 1), 100),
]

# operators whose result order is not defined (compare after sorting)
UNORDERED = {AL + "quadratic_formula", TD + "characteristic_equation", LA + "eigenvalues"}


class NumericTests(unittest.TestCase):
    """compute() returns the hand-calculated answer for known inputs."""


def _make(key, args, expected):
    def test(self):
        actual = get(key).compute(*args)
        exp = expected
        if key in UNORDERED:
            sort_key = lambda z: (complex(z).real, complex(z).imag)
            actual, exp = sorted(actual, key=sort_key), sorted(expected, key=sort_key)
        self.assertTrue(approx(actual, exp, 1e-6),
                        f"{key}{args!r}\n  expected {exp!r}\n  got      {actual!r}")
    return test


for _i, (_k, _a, _e) in enumerate(CASES):
    setattr(NumericTests, f"test_{_i:03d}_{_k.replace('/', '.')}", _make(_k, _a, _e))


# --------------------------------------------------------------------------- 3. error handling
class ErrorTests(unittest.TestCase):
    """Invalid input must raise a clear exception, never return a silent wrong number."""

    def raises(self, key, args, exc):
        with self.assertRaises(exc, msg=f"{key}{args}"):
            get(key).compute(*args)

    def test_divide_by_zero(self):
        self.raises(A + "division", (1, 0), ZeroDivisionError)

    def test_modulo_by_zero(self):
        self.raises(A + "modulo", (1, 0), ZeroDivisionError)

    def test_reciprocal_of_zero(self):
        self.raises(A + "reciprocal", (0,), ZeroDivisionError)

    def test_sqrt_of_negative(self):
        self.raises(AL + "square_root", (-1,), ValueError)

    def test_log_of_zero_and_negative(self):
        self.raises(AL + "natural_log", (0,), ValueError)
        self.raises(AL + "log_base_10", (-5,), ValueError)

    def test_singular_matrix_inverse(self):
        self.raises(LA + "matrix_inverse", ([[1, 2], [2, 4]],), ValueError)

    def test_acos_out_of_domain(self):
        self.raises(TR + "inverse_cosine", (2,), ValueError)

    def test_factorial_of_negative(self):
        self.raises(DN + "factorial", (-1,), ValueError)

    def test_reference_only_operators_say_so(self):
        for key in (AA + "ring", CR + "open_bracket", CR + "curly_braces", TP + "manifold"):
            self.raises(key, (), NotImplementedError)


# --------------------------------------------------------------------------- 4. cross-checks
class IdentityTests(unittest.TestCase):
    """Cross-check operators against each other, so one wrong operator cannot hide."""

    def c(self, key, *a):
        return get(key).compute(*a)

    def test_sin2_plus_cos2(self):
        for t in (0.1, 1.0, 2.5, -3.0):
            s, c = self.c(TR + "sine", t), self.c(TR + "cosine", t)
            self.assertAlmostEqual(s * s + c * c, 1, places=12)

    def test_degrees_radians_round_trip(self):
        for d in (0, 30, 45, 90, 123.4):
            r = self.c(TR + "degrees_to_radians", d)
            self.assertAlmostEqual(self.c(TR + "radians_to_degrees", r), d, places=9)

    def test_exp_ln_inverse(self):
        for x in (0.5, 1, 7.3):
            self.assertAlmostEqual(self.c(AL + "natural_log", self.c(AL + "exponential", x)), x, places=10)

    def test_square_sqrt_inverse(self):
        for x in (0, 1, 2, 9.5):
            self.assertAlmostEqual(self.c(AL + "square_root", self.c(AL + "square", x)), x, places=10)

    def test_matrix_times_inverse_is_identity(self):
        m = [[4, 7], [2, 6]]
        prod = self.c(LA + "matrix_multiply", m, self.c(LA + "matrix_inverse", m))
        self.assertTrue(approx(prod, [[1, 0], [0, 1]], 1e-9))

    def test_quadratic_roots_satisfy_equation(self):
        for a, b, c in ((1, -3, 2), (2, 5, -3), (1, 2, 5)):
            for x in self.c(AL + "quadratic_formula", a, b, c):
                self.assertAlmostEqual(abs(a * x * x + b * x + c), 0, places=9)

    def test_ax_equals_b_solution(self):
        a_mat, b = [[3, 2], [1, 4]], [7, 9]
        x = self.c(LA + "solve_ax_b", a_mat, b)
        prod = self.c(LA + "matrix_multiply", a_mat, [[x[0]], [x[1]]])
        self.assertTrue(approx([prod[0][0], prod[1][0]], b, 1e-9))

    def test_pascal_rule(self):
        for n in range(2, 9):
            for r in range(1, n):
                self.assertEqual(self.c(DN + "combinations", n, r),
                                 self.c(DN + "combinations", n - 1, r - 1) + self.c(DN + "combinations", n - 1, r))

    def test_gcd_lcm_product(self):
        for a, b in ((12, 18), (7, 5), (100, 75)):
            self.assertEqual(self.c(DN + "greatest_common_divisor", a, b)
                             * self.c(DN + "least_common_multiple", a, b), a * b)

    def test_prime_factorization_multiplies_back(self):
        for n in (2, 17, 360, 1001, 65536):
            self.assertEqual(math.prod(self.c(DN + "prime_factorization", n)), n)

    def test_fibonacci_recurrence(self):
        for n in range(2, 30):
            self.assertEqual(self.c(DN + "fibonacci", n),
                             self.c(DN + "fibonacci", n - 1) + self.c(DN + "fibonacci", n - 2))

    def test_derivative_of_integral(self):
        f = lambda x: x ** 3 + 2 * x
        big_f = lambda x: self.c(CA + "definite_integral", f, 0, x)
        self.assertAlmostEqual(self.c(CA + "derivative", big_f, 2.0), f(2.0), places=4)

    def test_variance_is_std_squared(self):
        d = [2, 4, 4, 4, 5, 5, 7, 9, 1.5]
        self.assertAlmostEqual(self.c(ST + "standard_deviation", d) ** 2, self.c(ST + "variance", d), places=10)

    def test_demorgan(self):
        for a in (True, False):
            for b in (True, False):
                self.assertEqual(self.c(LS + "not", self.c(LS + "and", a, b)),
                                 self.c(LS + "or", self.c(LS + "not", a), self.c(LS + "not", b)))

    def test_eigenvectors_satisfy_av_equals_lambda_v(self):
        m = [[2, 1], [1, 2]]
        for lam, vecs in self.c(LA + "eigenvectors", m):
            for v in vecs:
                av = [sum(m[i][j] * v[j] for j in range(2)) for i in range(2)]
                self.assertTrue(approx(av, [lam * x for x in v], 1e-9), (lam, v))

    def test_rk4_matches_exp(self):
        pts = self.c(OP + "runge_kutta_rk4", lambda x, y: y, 0, 1, 0.1, 10)
        self.assertEqual(len(pts), 11)
        self.assertAlmostEqual(pts[-1][1], E, places=4)

    def test_epsilon_delta_returns_a_valid_delta(self):
        delta = self.c(RA + "epsilon_delta_continuity", lambda x: 2 * x, 1, 0.1)
        self.assertTrue(0 < delta <= 0.05, delta)       # |2x-2| < 0.1 needs |x-1| < 0.05

    def test_trig_and_geometry_agree(self):
        self.assertAlmostEqual(self.c(GE + "degrees_to_radians_geometry", 77),
                               self.c(TR + "degrees_to_radians", 77))


# --------------------------------------------------------------------------- 5. input parser + GUI
class InputParserTests(unittest.TestCase):
    """operator_row_math.advanced_input.parse turns typed text into values compute() accepts."""

    def setUp(self):
        from operator_row_math import advanced_input
        self.parse = advanced_input.parse

    def test_plain_values(self):
        self.assertEqual(self.parse("number", "3.5"), 3.5)
        self.assertEqual(self.parse("list", "1, 2, 3"), [1, 2, 3])
        self.assertEqual(self.parse("matrix", "1 2; 3 4"), [[1, 2], [3, 4]])
        self.assertEqual(self.parse("set", "1,2,3"), {1, 2, 3})
        self.assertEqual(self.parse("pairs", "(0,1),(1,2)"), [(0, 1), (1, 2)])
        self.assertEqual(self.parse("item", "A"), "A")

    def test_graphs(self):
        self.assertEqual(self.parse("graph", "A: B, C; B: C; C: A"), {"A": ["B", "C"], "B": ["C"], "C": ["A"]})
        self.assertEqual(self.parse("wgraph", "A: B=4, C=1; B: C=2; C:"),
                         {"A": [("B", 4), ("C", 1)], "B": [("C", 2)], "C": []})

    def test_function_and_predicate_are_callable(self):
        self.assertAlmostEqual(self.parse("function", "x**2+3*x")(2.0), 10.0)
        self.assertIs(self.parse("predicate", "x > 2")(3), True)
        self.assertIs(self.parse("predicate", "x > 2")(1), False)

    def test_unsafe_function_text_is_rejected(self):
        for bad in ("__import__('os').system('echo hi')", "x.__class__", "open('f')", "exec('1')"):
            with self.assertRaises(ValueError, msg=bad):
                self.parse("function", bad)


class GuiSmokeTest(unittest.TestCase):
    """The main window builds and closes without raising (needs a display + tkinter)."""

    def test_window_opens(self):
        try:
            import tkinter
            import main
            app = main.CalculatorGUI()
        except (ImportError, tkinter.TclError) as exc:
            self.skipTest(f"no GUI available: {exc}")
        try:
            app.update()
        finally:
            app.destroy()


# --------------------------------------------------------------------------- 6. new physics: row modules + calculator
NEW_PHYSICS = [
    'magnetic_force_on_charge', 'magnetic_force_on_wire', 'magnetic_field_straight_wire',
    'magnetic_field_solenoid', 'magnetic_flux', 'faradays_law',
    'self_induced_emf', 'inductor_energy', 'cyclotron_radius',
    'motional_emf', 'buoyant_force', 'hydrostatic_pressure',
    'continuity_equation', 'bernoulli_equation', 'reynolds_number',
    'poiseuille_flow', 'torricelli_speed', 'stokes_drag',
    'volume_flow_rate', 'hydraulic_press', 'photon_energy',
    'photon_momentum', 'de_broglie_wavelength', 'heisenberg_uncertainty',
    'photoelectric_effect', 'bohr_energy_level', 'rydberg_formula',
    'particle_in_a_box', 'quantum_harmonic_oscillator', 'compton_shift',
    'thin_lens_equation', 'lens_magnification', 'lensmakers_equation',
    'critical_angle', 'brewster_angle', 'double_slit_fringe_spacing',
    'diffraction_grating', 'malus_law', 'refractive_index',
    'lorentz_factor', 'time_dilation', 'length_contraction',
    'relativistic_momentum', 'relativistic_kinetic_energy', 'energy_momentum_relation',
    'relativistic_velocity_addition', 'relativistic_doppler', 'schwarzschild_radius',
    'gravitational_time_dilation',
]


def _required_inputs(key):
    """Number of boxes the calculator shows for an operator = compute() parameters without a default."""
    import inspect
    return sum(1 for p in inspect.signature(get(key).compute).parameters.values() if p.default is p.empty)


class NewPhysicsRowTests(unittest.TestCase):
    """Row modules for the 49 magnetism / fluid / quantum / optics / relativity operators."""

    @classmethod
    def setUpClass(cls):
        import inspect
        import operator_links
        import operator_row_math
        cls.links, cls.rows, cls.inspect = operator_links.LINKS, operator_row_math, inspect

    def test_row_module_matches_compute_signature(self):
        for n in NEW_PHYSICS:
            key = "physics/physics/" + n
            row = self.rows.get(key)
            params = [p.name for p in self.inspect.signature(get(key).compute).parameters.values()
                      if p.default is p.empty]
            from operator_row_math import row_tree
            self.assertEqual(row.INPUTS, params, n)
            self.assertEqual(len(row.KINDS), len(params), n)
            self.assertEqual(row_tree.slot_count(row), len(params), n)           # one input per parameter (the picture may write a variable twice)
            self.assertEqual((row.KEY, row.CALC), (key, "ready"), n)
            # the answer is shown in the formula's own answer box ({} on the left) or in the result box right of the row
            self.assertTrue(any(k == "out" for k, _ in row.LEFT) or any(k == "box" for k, _ in row.RIGHT), n)

    def test_every_operator_has_a_calculator_button(self):
        import main
        buttons = set(main.PHYSICS_OPS)
        linked = {k: v for (sec, label), v in self.links.items() if sec == "PHYSICS_OPS" for k in [label]}
        for n in NEW_PHYSICS:
            labels = [lab for lab, v in linked.items() if v == "physics/physics/" + n]
            self.assertEqual(len(labels), 1, n)
            self.assertIn(labels[0], buttons, n)

    def test_row_tree_evaluates_like_compute(self):
        """Fill the boxes exactly as the window does and compare with compute()."""
        from operator_row_math import row_tree
        for key, args, expected in CASES:
            n = key.split("/")[-1]
            if not key.startswith(PH) or n not in NEW_PHYSICS or len(args) != _required_inputs(key):
                continue
            node = row_tree.new_node(key)
            self.assertEqual(len(node["slots"]), len(args), key)
            node["slots"] = [repr(a) for a in args]
            self.assertTrue(approx(row_tree.evaluate(node), expected, 1e-6), f"{key}{args}")


class NewPhysicsCalculatorTests(unittest.TestCase):
    """Drive the real calculator window: pick the operator, type the numbers on the keypad, press =."""

    @classmethod
    def setUpClass(cls):
        try:
            import tkinter
            import main
            cls.app = main.CalculatorGUI()
            cls.app.update()
        except (ImportError, tkinter.TclError) as exc:
            raise unittest.SkipTest(f"no GUI available: {exc}")

    @classmethod
    def tearDownClass(cls):
        cls.app.destroy()

    @staticmethod
    def _keys(x):
        """The keypad presses that type a number: digits, '.', ± for a minus sign, EE for a power of ten."""
        keys = []
        for ch in repr(x):
            if ch == "-":
                keys.append("±")
            elif ch == "e":
                keys.append("EE")
            elif ch != "+":
                keys.append(ch)
        return keys

    def _type_into_boxes(self, args):
        """Click each square box of Row 1 in turn (left to right) and type its number on the keypad."""
        app = self.app
        paths = sorted({p for kind, _t, p in app._cards(0) if kind == "box"})     # one path per input (a variable written twice has two cards)
        self.assertEqual(len(paths), len(args), "the row has a different number of inputs than the call")
        for path, a in zip(paths, args):
            app.rows[0]["sel"] = path
            for ch in self._keys(a):
                app._key(ch)

    def _calculate(self, key, args):
        app = self.app
        app._reset_row(0)
        app.op_target = 0
        app._place_operator_row(key)
        self._type_into_boxes(args)
        app._equals()
        said = app.results.get("1.0", "end")
        m = re.search(r"=\s+(\S+)\s+\(printed", said)
        self.assertIsNotNone(m, f"{key}: no result in the window, it said: {said!r}")
        return float(m.group(1))

    def test_every_new_operator_works_in_the_window(self):
        done = set()
        for key, args, expected in CASES:
            n = key.split("/")[-1]
            if not key.startswith(PH) or n not in NEW_PHYSICS or n in done or len(args) != _required_inputs(key):
                continue
            if any(isinstance(a, bool) or not isinstance(a, (int, float)) for a in args) or isinstance(expected, bool):
                continue
            got = self._calculate(key, args)
            self.assertTrue(approx(got, expected, 1e-8), f"{key}{args}: window gave {got}, expected {expected}")
            done.add(n)
        # relativity operators: their stored cases use c = 1, so use real speeds with the default c
        c = 299792458.0
        extra = [
            ("lorentz_factor", (0.6 * c,), 1.25),
            ("time_dilation", (1, 0.6 * c), 1.25),
            ("length_contraction", (100, 0.8 * c), 60),
            ("relativistic_momentum", (2, 0.6 * c), 2 * 0.6 * c * 1.25),
            ("relativistic_kinetic_energy", (1, 0.6 * c), 0.25 * c * c),
            ("energy_momentum_relation", (1, 0), c * c),
            ("relativistic_velocity_addition", (0.5 * c, 0.5 * c), 0.8 * c),
            ("relativistic_doppler", (100, 0.6 * c), 50),
            ("gravitational_time_dilation", (1000, 1.989e30, 6.957e8),
             1000 * math.sqrt(1 - 2 * 6.674e-11 * 1.989e30 / (6.957e8 * c * c))),
        ]
        for n, args, expected in extra:
            key = PH + n
            got = self._calculate(key, args)
            self.assertTrue(approx(got, expected, 1e-8), f"{key}{args}: window gave {got}, expected {expected}")
            done.add(n)
        missing = sorted(set(NEW_PHYSICS) - done)
        self.assertEqual(missing, [], f"not exercised in the window: {missing}")

    def test_keypad_minus_and_exponent_keys(self):
        """± flips the sign (of the exponent after EE), EE starts a power of ten, . is refused after EE."""
        app = self.app
        app._reset_row(0)
        app._place_operator_row("math/arithmetic/addition")
        paths = [p for kind, _t, p in app._cards(0) if kind == "box"]
        from operator_row_math import row_tree

        def typed(keys):
            row_tree.set_slot(app.rows[0]["node"], paths[0], "")
            app.rows[0]["sel"] = paths[0]
            for k in keys:
                app._key(k)
            return row_tree.get_slot(app.rows[0]["node"], paths[0])

        self.assertEqual(typed(["±", "5"]), "-5")
        self.assertEqual(typed(["±", "5", "±"]), "5")                       # second press removes the minus
        self.assertEqual(typed(["1", ".", "5", "EE", "±", "3"]), "1.5e-3")
        self.assertEqual(typed(["6", "EE", "3", "±", "±"]), "6e3")
        self.assertEqual(typed(["EE", "5"]), "5")                           # no exponent without a number first
        self.assertEqual(typed(["2", "EE", "EE", "4"]), "2e4")              # only one exponent
        self.assertEqual(typed(["2", "EE", ".", "5"]), "2e5")               # no decimal point in the exponent
        self.assertEqual(typed(["7", "EE", "5", "⌫", "⌫"]), "7")           # backspace removes the exponent

    def test_negative_and_tiny_numbers_calculate(self):
        c = self._calculate("physics/physics/faradays_law", (10, -4, 2))
        self.assertAlmostEqual(c, 20)                                        # −N·ΔΦ/Δt with ΔΦ = −4
        h = self._calculate("physics/physics/photon_energy", (1e15,))
        self.assertAlmostEqual(h / 6.62607015e-19, 1, places=8)
        e = self._calculate("physics/physics/de_broglie_wavelength", (9.1093837015e-31, 1e6))
        self.assertAlmostEqual(e / 7.2737e-10, 1, places=3)

    def _buttons(self):
        import tkinter as tk
        found, stack = [], [self.app]
        while stack:
            w = stack.pop()
            stack.extend(w.winfo_children())
            if isinstance(w, tk.Button):
                found.append(w)
        return found

    def test_c_key_and_clear_button_reset_everything(self):
        from operator_row_math import row_tree
        app = self.app
        clear_buttons = [b for b in self._buttons() if b.cget("text") in ("C", "Clear (C)")]
        self.assertEqual(len(clear_buttons), 2)                   # the keypad C and the toolbar Clear (C)
        for button in clear_buttons:
            app._reset_row(0)
            app._place_operator_row("physics/physics/time_dilation")
            self._type_into_boxes([1, 179875474.8])
            app._equals()
            self.assertIn("1.25", app.results.get("1.0", "end"))
            app._set_join(1, "+")                                  # leave a join symbol behind as well
            button.invoke()
            for row in app.rows:
                self.assertEqual(row["node"]["key"], "_number")
                self.assertEqual(row["node"]["slots"], [""])
                self.assertFalse(row["is_result"])
                self.assertIsNone(row["join"])
            self.assertIsNone(app.template)
            self.assertEqual(app.op_target, 0)
            self.assertIn("Cleared", app.results.get("1.0", "end"))
            self.assertEqual(row_tree.fmt(0), "0")

    def test_keypad_has_only_working_keys(self):
        texts = {b.cget("text") for b in self._buttons()}
        self.assertNotIn("Next Col (→)", texts)
        self.assertNotIn("Next Number (—)", texts)
        for key in list("0123456789.") + ["±", "EE", "Backspace", "Next Row (↓)", "=", "C", "Operators"]:
            self.assertIn(key, texts)

    def test_window_reports_errors_nicely(self):
        app = self.app
        app._reset_row(0)
        app._place_operator_row("physics/physics/lorentz_factor")
        self._type_into_boxes([300000000])                          # faster than light (c = 299 792 458 m/s)
        app._equals()
        said = app.results.get("1.0", "end")
        self.assertIn("speed must be less than the speed of light", said)


# --------------------------------------------------------------------------- 7. Mathematical Templates (typed math)
class TemplateMathTests(unittest.TestCase):
    """operator_row_math.template_math: typed math -> the operator tree a row can hold."""

    def setUp(self):
        from operator_row_math import row_tree, template_math
        self.tm, self.rt = template_math, row_tree

    def value(self, text):
        return self.rt.evaluate(self.tm.parse_math(text))

    def test_calculates_like_ordinary_maths(self):
        cases = [("2 + 3 × 4", 14), ("(2+3)×4", 20), ("2^3^2", 512), ("-2^2", -4),
                 ("-5 + 2", -3), ("7 − 2 − 1", 4), ("8 / 4 / 2", 1), ("2 * -3", -6), ("10 % 4", 2),
                 ("2 + 3 * 4 - 5", 9), ("(1 + 2) * (3 + 4)", 21), ("1.5e-3 * 1000", 1.5), (".5 + .5", 1)]
        for text, expected in cases:
            self.assertTrue(approx(self.value(text), expected), text)

    def test_operators_by_name_and_short_name(self):
        cases = [("sqrt(16) + abs(-3)", 7), ("square root(81)", 9), ("Square_Root(81)", 9),
                 ("Time dilation(1, 179875474.8)", 1.25), ("Newton's second law(2, 5)", 10),
                 ("sin(pi / 2)", 1), ("ln(e)", 1), ("log(1000) ÷ 3", 1), ("max(2, 9, 4)", 9), ("round(2.6)", 3),
                 ("factorial(5)", 120), ("gcd(12, 18)", 6), ("lcm(4, 6)", 12)]
        for text, expected in cases:
            self.assertTrue(approx(self.value(text), expected), text)

    def test_every_alias_points_at_a_real_operator(self):
        for alias, ident in self.tm.ALIASES.items():
            key = self.tm.find_operator(alias)
            self.assertIsNotNone(key, alias)
            self.assertEqual(key, self.tm.find_operator(ident), alias)

    def test_description_shows_the_grouping(self):
        d = lambda t: self.tm.describe(self.tm.parse_math(t))
        self.assertEqual(d("(2 + 3) × 4"), "(2 + 3) × 4")
        self.assertEqual(d("2 + 3 × 4"), "2 + (3 × 4)")
        self.assertEqual(d("(□ + 3) * 2"), "(□ + 3) × 2")
        self.assertEqual(d("Time dilation(1, x)"), "1 / √ ( 1 − □^2 / c^2 )")      # the row is the picture's formula: the template reads its right-hand side

    def test_empty_boxes(self):
        n = lambda t: self.tm.empty_boxes(self.tm.parse_math(t))
        self.assertEqual(n("(□ + 3) * 2"), 1)
        self.assertEqual(n("x * x + ?"), 3)                  # each box, bare letter or ? is its own box
        self.assertEqual(n("2 + 3"), 0)
        with self.assertRaises(ValueError):
            self.value("x + 1")                              # cannot calculate until the box is filled

    def test_mistakes_get_readable_messages(self):
        bad = [("", "Type some math"), ("2 +", "ends too soon"), ("(2 + 3", "never closed"),
               ("2 + 3)", "Unexpected"), ("5", "at least one operator"), ("3 3", "Put an operator between"),
               ("2 x", "Put an operator between"), ("foo(2)", "no operator called"),
               ("Time dilation(1)", "needs 2 input"), ("sqrt(1, 2)", "needs 1 input"),
               ("square root 9", "inputs in brackets"), ("2 $ 3", "don't understand")]
        for text, expected in bad:
            with self.assertRaises(ValueError, msg=text) as ctx:
                self.tm.parse_math(text)
            self.assertIn(expected, str(ctx.exception), text)

    def test_runtime_errors_are_value_errors(self):
        with self.assertRaises(ValueError):
            self.value("7 ÷ 0")
        with self.assertRaises(ValueError):
            self.value("sqrt(-4)")

    def test_unsafe_text_is_just_rejected(self):
        for text in ("__import__('os').system('echo hi')", "open('f')", "x.__class__", "exec('1')"):
            with self.assertRaises(ValueError, msg=text):
                self.tm.parse_math(text)

    def test_saved_file_round_trip(self):
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "saved_templates.json")
            self.assertEqual(self.tm.load_templates(path), [])                     # missing file
            self.tm.save_templates(path, ["(□ + 3) × 2", "Time dilation(1, □)", "x ÷ π"])
            self.assertEqual(self.tm.load_templates(path), ["(□ + 3) × 2", "Time dilation(1, □)", "x ÷ π"])
            with open(path, "w", encoding="utf-8") as f:
                f.write("this is not json")
            self.assertEqual(self.tm.load_templates(path), [])                     # damaged file
            with open(path, "w", encoding="utf-8") as f:
                f.write('["ok", 5, "", null, "also ok"]')                          # the first file format: a bare list
            self.assertEqual(self.tm.load_templates(path), ["ok", "also ok"])
            self.assertEqual(self.tm.load_data(path), (["ok", "also ok"], False))

    def test_guide_choice_is_saved_with_the_templates(self):
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "saved_templates.json")
            self.tm.save_data(path, ["a + b"], hide_guide=True)
            self.assertEqual(self.tm.load_data(path), (["a + b"], True))
            self.tm.save_templates(path, ["a + b", "sqrt(x)"])                      # keeps the choice
            self.assertEqual(self.tm.load_data(path), (["a + b", "sqrt(x)"], True))


class TemplatePanelTests(unittest.TestCase):
    """The Mathematical Templates panel in the real window:
    type -> Preview Posted (shows it in the row) -> Save Template -> pick it in the list -> Apply Template,
    with a step-by-step guide pop-up that opens when you start typing."""

    @classmethod
    def setUpClass(cls):
        try:
            import tkinter
            import main
            cls.app = main.CalculatorGUI()
            cls.app.update()
        except (ImportError, tkinter.TclError) as exc:
            raise unittest.SkipTest(f"no GUI available: {exc}")

    @classmethod
    def tearDownClass(cls):
        cls.app.destroy()

    def setUp(self):
        import tempfile
        self.folder = tempfile.TemporaryDirectory()
        app = self.app
        app.update()
        app._tpl_close_guide()
        app.update()                                               # lets Tk finish closing the old guide
        app.template_path = os.path.join(self.folder.name, "saved_templates.json")   # never touch the real file
        app.saved_templates, app.tpl_hide_guide = [], False
        app.tpl_combo.configure(values=[])
        app.tpl_combo.set("")
        app.tpl_entry.delete(0, "end")
        app._tpl_was_empty, app._tpl_last_text = True, ""
        app._clear_all()

    def tearDown(self):
        self.app.update()
        self.app._tpl_close_guide()
        self.app.update()
        self.folder.cleanup()

    def widgets(self, root=None):
        stack, out = [root or self.app], []
        while stack:
            w = stack.pop()
            stack.extend(w.winfo_children())
            out.append(w)
        return out

    def button(self, text, root=None):
        import tkinter as tk
        for w in self.widgets(root):
            if isinstance(w, tk.Button) and w.cget("text") == text:
                return w
        self.fail(f"no button {text!r}")

    def said(self):
        return self.app.results.get("1.0", "end")

    def type_math(self, text):
        """Type into the text box the way a person does: the text changes, then a key is released."""
        self.app.tpl_entry.delete(0, "end")
        self.app.tpl_entry.insert(0, text)
        self.app._tpl_typed()

    def row_text(self, i=0):
        return " ".join(t if t else "\u25a1" for _k, t, _p in self.app._cards(i))

    def guide_text(self):
        import tkinter as tk
        return " ".join(str(w.cget("text")) for w in self.widgets(self.app.tpl_guide) if isinstance(w, tk.Label))

    # ---- the buttons
    def test_the_three_unused_toolbar_buttons_are_gone(self):
        import tkinter as tk
        texts = {w.cget("text") for w in self.widgets() if isinstance(w, tk.Button)}
        for gone in ("Calculate (e)", "+ Add Description Col", "Delete Selected Col"):
            self.assertNotIn(gone, texts)
        for kept in ("Clear (C)", "Next Row (\u2193)", "Apply Template", "Save Template", "Preview Posted", "?"):
            self.assertIn(kept, texts)

    def test_the_equals_beside_the_text_box_is_only_a_sign(self):
        import tkinter as tk
        panel = self.widgets(self.app.tpl_panel)
        self.assertEqual([w for w in panel if isinstance(w, tk.Button) and w.cget("text") == "="], [])
        self.assertTrue(any(isinstance(w, tk.Label) and w.cget("text") == "=" for w in panel))

    # ---- Preview Posted
    def test_preview_posted_puts_the_math_in_the_row(self):
        self.type_math("(\u25a1 + 3) * 2")
        self.button("Preview Posted").invoke()
        self.assertEqual(self.row_text(), "\u25a1 + 3 \u00d7 2")           # the row now holds the template
        self.assertIn("Preview - posted in Row 1", self.said())
        self.assertIn("(\u25a1 + 3) \u00d7 2", self.said())
        self.assertIn("Save Template", self.said())

    def test_a_new_preview_replaces_the_old_one(self):
        self.type_math("\u25a1 \u00d7 10")
        self.button("Preview Posted").invoke()
        self.assertIn("10", self.row_text())
        self.type_math("sqrt(\u25a1)")
        self.button("Preview Posted").invoke()
        shown = self.row_text()
        self.assertIn("\u221a", shown)
        self.assertNotIn("10", shown)                              # the first preview was taken out first

    def test_preview_leaves_other_work_alone_and_clear_forgets_it(self):
        app = self.app
        self.type_math("\u25a1 + \u25a1")
        self.button("Preview Posted").invoke()
        first, second = [pth for k, t, pth in app._cards(0) if k == "box"][:2]
        app.rows[0]["sel"] = first
        app._key("7")                                              # the user starts using the previewed row
        app.rows[0]["sel"] = second
        self.type_math("sqrt(\u25a1)")
        self.button("Preview Posted").invoke()                     # goes into the selected box; must not wipe the 7
        self.assertIn("7", self.row_text())
        self.assertIn("\u221a", self.row_text())
        app._clear_all()
        self.assertEqual(self.row_text(), "\u25a1")
        self.assertIsNone(app._tpl_preview_state)

    def test_bad_math_is_explained_and_nothing_is_posted_or_saved(self):
        self.type_math("sqrt(")
        self.button("Preview Posted").invoke()
        self.assertIn("Template:", self.said())
        self.assertEqual(self.row_text(), "\u25a1")
        self.button("Save Template").invoke()
        self.assertEqual(self.app.saved_templates, [])
        self.assertFalse(os.path.exists(self.app.template_path))

    # ---- Save Template and Apply Template
    def test_the_whole_journey(self):
        """type -> preview -> save -> pick from the list -> apply -> fill the box -> calculate"""
        app = self.app
        self.type_math("(\u25a1 + 3) \u00d7 2")
        self.button("Preview Posted").invoke()
        self.button("Save Template").invoke()
        self.assertEqual(app.saved_templates, ["(\u25a1 + 3) \u00d7 2"])
        self.assertIn("(\u25a1 + 3) \u00d7 2", app.tpl_combo.cget("values"))
        from operator_row_math import template_math
        self.assertEqual(template_math.load_templates(app.template_path), ["(\u25a1 + 3) \u00d7 2"])
        app._clear_all()                                           # later: start with an empty row
        app.tpl_combo.set("(\u25a1 + 3) \u00d7 2")
        self.button("Apply Template").invoke()
        self.assertEqual(self.row_text(), "\u25a1 + 3 \u00d7 2")
        empty = [pth for kind, t, pth in app._cards(0) if kind == "box" and not t]
        self.assertEqual(len(empty), 1)
        app.rows[0]["sel"] = empty[0]
        for ch in NewPhysicsCalculatorTests._keys(4):
            app._key(ch)
        app._equals()
        self.assertIn("= 14", self.said().replace("  ", " "))      # (4 + 3) x 2

    def test_apply_replaces_the_preview_instead_of_nesting_in_it(self):
        self.type_math("\u25a1 \u00d7 10")
        self.button("Preview Posted").invoke()
        self.button("Save Template").invoke()
        self.button("Apply Template").invoke()                     # same template, picked from the list
        self.assertEqual(self.row_text().count("10"), 1)

    def test_a_template_can_use_any_operator(self):
        app = self.app
        self.type_math("Time dilation(1, x)")
        self.button("Save Template").invoke()
        self.button("Apply Template").invoke()
        empty = [pth for kind, t, pth in app._cards(0) if kind == "box" and not t]
        app.rows[0]["sel"] = empty[0]
        for ch in NewPhysicsCalculatorTests._keys(179875474.8):
            app._key(ch)
        app._equals()
        self.assertIn("1.25", self.said())

    def test_several_templates_and_no_duplicates(self):
        app = self.app
        for text in ("x + y", "sqrt(x)", "x + y"):
            self.type_math(text)
            self.button("Save Template").invoke()
        self.assertEqual(app.saved_templates, ["x + y", "sqrt(x)"])
        self.assertEqual(list(app.tpl_combo.cget("values")), ["x + y", "sqrt(x)"])

    def test_apply_with_nothing_picked_says_what_to_do(self):
        self.button("Apply Template").invoke()
        self.assertIn("No template picked yet", self.said())
        self.assertIn("Preview Posted", self.said())

    def test_a_template_nests_into_the_selected_box(self):
        app = self.app
        self.type_math("\u25a1 \u00d7 10")
        self.button("Save Template").invoke()
        self.button("Apply Template").invoke()
        app.rows[0]["sel"] = [pth for kind, t, pth in app._cards(0) if kind == "box"][0]
        self.type_math("sqrt(\u25a1)")
        self.button("Save Template").invoke()
        self.button("Apply Template").invoke()
        shown = self.row_text()
        self.assertIn("\u221a", shown)
        self.assertIn("10", shown)

    # ---- the how-to guide pop-up
    def test_guide_opens_when_you_start_typing_and_lists_the_four_steps(self):
        app = self.app
        self.assertIsNone(app.tpl_guide)
        self.assertTrue(app.tpl_entry.bind("<KeyRelease>"))        # typing in the text box calls the guide
        self.type_math("x")
        self.assertIsNotNone(app.tpl_guide)
        text = self.guide_text()
        for words in ("Type your math", "Preview Posted", "Save Template", "Apply Template"):
            self.assertIn(words, text)
        self.button("Got it", app.tpl_guide)
        self.assertEqual(sum(1 for w in self.widgets(app.tpl_guide) if w.winfo_class() == "Checkbutton"), 1)

    def test_guide_is_fully_on_screen_and_does_not_cover_the_template_buttons(self):
        app = self.app
        self.type_math("x")
        app.update()
        win = app.tpl_guide
        x, y, w, h = win.winfo_rootx(), win.winfo_rooty(), win.winfo_width(), win.winfo_height()
        sw, sh = app.winfo_screenwidth(), app.winfo_screenheight()
        if sw >= w and sh >= h + 60:                                   # only when the screen is big enough at all
            self.assertGreaterEqual(x, 0)
            self.assertGreaterEqual(y, 0)
            self.assertLessEqual(x + w, sw)
            self.assertLessEqual(y + h, sh)                            # the Got it button is reachable
        for name in ("Preview Posted", "Save Template", "Apply Template"):
            b = self.button(name)
            bx, by, bw, bh = b.winfo_rootx(), b.winfo_rooty(), b.winfo_width(), b.winfo_height()
            overlap = bx < x + w and x < bx + bw and by < y + h and y < by + bh
            self.assertFalse(overlap, f"the guide covers the {name} button")
        text_box = app.tpl_entry
        ex, ey, ew, eh = text_box.winfo_rootx(), text_box.winfo_rooty(), text_box.winfo_width(), text_box.winfo_height()
        self.assertFalse(ex < x + w and x < ex + ew and ey < y + h and y < ey + eh, "the guide covers the text box")

    def test_guide_does_not_open_for_an_empty_box_and_opens_once(self):
        app = self.app
        self.type_math("")
        self.assertIsNone(app.tpl_guide)
        self.type_math("x")
        first = app.tpl_guide
        self.type_math("x + 1")
        self.assertIs(app.tpl_guide, first)                        # one pop-up, not one per key

    def test_guide_follows_your_progress(self):
        app = self.app
        self.type_math("sqrt(")
        self.assertEqual(app._tpl_progress(), (False, False, False, False))
        self.assertIn("keep typing", self.guide_text())                 # unfinished: a gentle hint, not an error
        self.assertNotIn("\u2717", self.guide_text())
        self.type_math("foo(2)")
        self.assertIn("\u2717 There is no operator called", self.guide_text())   # a real mistake: shown in red
        self.type_math("sqrt(x) + 4")
        self.assertEqual(app._tpl_progress(), (True, False, False, False))
        self.assertIn("\u2713 Understood", self.guide_text())
        self.button("Preview Posted").invoke()
        self.assertEqual(app._tpl_progress(), (True, True, False, False))
        self.button("Save Template").invoke()
        self.assertEqual(app._tpl_progress(), (True, True, True, False))
        self.button("Apply Template").invoke()
        self.assertEqual(app._tpl_progress(), (True, True, True, True))
        ticks = [w.cget("text") for w in self.widgets(app.tpl_guide) if w.winfo_class() == "Label"
                 and w.cget("text") == "\u2713"]
        self.assertEqual(len(ticks), 4)                            # every step ticked
        self.type_math("sqrt(x) + 5")                              # new text: back to step 2
        self.assertEqual(app._tpl_progress(), (True, False, False, False))

    def test_guide_got_it_closes_it_and_the_question_mark_reopens_it(self):
        app = self.app
        self.type_math("x")
        self.button("Got it", app.tpl_guide).invoke()
        self.assertIsNone(app.tpl_guide)
        app.update()
        self.type_math("")
        self.type_math("x")                                        # typing again from empty shows it again
        self.assertIsNotNone(app.tpl_guide)
        app.update()
        app._tpl_close_guide()
        app.update()
        self.button("?").invoke()
        self.assertIsNotNone(app.tpl_guide)

    def test_dont_show_again_is_remembered(self):
        from operator_row_math import template_math
        app = self.app
        self.type_math("x")
        check = next(w for w in self.widgets(app.tpl_guide) if w.winfo_class() == "Checkbutton")
        check.invoke()
        self.assertTrue(app.tpl_hide_guide)
        self.assertEqual(template_math.load_data(app.template_path)[1], True)     # kept for next time
        app.update()
        app._tpl_close_guide()
        app.update()
        self.type_math("")
        self.type_math("x + 1")
        self.assertIsNone(app.tpl_guide)                           # no pop-up any more
        self.button("?").invoke()                                  # but ? still opens it
        self.assertIsNotNone(app.tpl_guide)


if __name__ == "__main__":
    unittest.main(verbosity=1)
