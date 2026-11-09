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
        return abs(actual - expected) <= tol * max(1.0, abs(expected))
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
        self.assertEqual(len(self.ops), 458)

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
        self.assertEqual(len(status), 458)
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


if __name__ == "__main__":
    unittest.main(verbosity=1)
