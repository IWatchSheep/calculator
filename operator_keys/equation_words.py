"""Label and context words for equation operators.

A label is what the symbol is. A context is its unit or its meaning. These are written into
operator_keys/operator_row_specs.txt as symbol{label|context}. The row file and the Rust layout
are generated from that line, and the picture lists the same words under the equation.

    python operator_keys/equation_words.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(HERE, "operator_row_specs.txt")

# key -> {spec token: (label, context)}
# tokens are written exactly as they appear in the spec: [m1], {}, G, ρ
W = {}


def add(key, **words):
    W[key] = words


# ---------------------------------------------------------------- physics
add("physics/physics/acceleration", **{"{}": ("acceleration", "metres per second squared"), "[delta_v]": ("change in velocity", "metres per second"), "[t]": ("time", "seconds")})
add("physics/physics/bernoulli_equation", **{"{}": ("downstream pressure", "pascals"), "[P1]": ("upstream pressure", "pascals"), "[v1]": ("upstream speed", "metres per second"), "[h1]": ("upstream height", "metres"), "[v2]": ("downstream speed", "metres per second"), "[h2]": ("downstream height", "metres"), "[rho]": ("density", "kilograms per cubic metre"), "g": ("gravity", "9.81 m/s2")})
add("physics/physics/bohr_energy_level", **{"{}": ("energy level", "electron-volts"), "[n]": ("level number", "1, 2, 3, ..."), "Z": ("atomic number", "1 for hydrogen")})
add("physics/physics/brewster_angle", **{"{}": ("Brewster angle", "radians"), "[n1]": ("first refractive index", "where the light starts"), "[n2]": ("second refractive index", "where the light goes")})
add("physics/physics/buoyant_force", **{"{}": ("buoyant force", "newtons, upward"), "[rho]": ("fluid density", "kilograms per cubic metre"), "[V]": ("displaced volume", "cubic metres"), "g": ("gravity", "9.81 m/s2")})
add("physics/physics/capacitance", **{"{}": ("charge", "coulombs"), "[C]": ("capacitance", "farads"), "[V]": ("voltage", "volts")})
add("physics/physics/centripetal_acceleration", **{"{}": ("centripetal acceleration", "metres per second squared, toward the centre"), "[v]": ("speed", "metres per second"), "[r]": ("radius", "metres")})
add("physics/physics/compton_shift", **{"{}": ("wavelength shift", "metres"), "[theta]": ("scatter angle", "radians"), "h": ("Planck constant", "6.626e-34 J s"), "m": ("electron mass", "kilograms"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/continuity_equation", **{"{}": ("downstream speed", "metres per second"), "[A1]": ("upstream area", "square metres"), "[v1]": ("upstream speed", "metres per second"), "[A2]": ("downstream area", "square metres")})
add("physics/physics/coulomb_s_law", **{"{}": ("electric force", "newtons"), "[q1]": ("first charge", "coulombs"), "[q2]": ("second charge", "coulombs"), "[r]": ("separation", "metres"), "k": ("Coulomb constant", "8.988e9 N m2/C2")})
add("physics/physics/critical_angle", **{"{}": ("critical angle", "radians, for total reflection"), "[n1]": ("denser index", "the side the light starts in"), "[n2]": ("rarer index", "must be smaller than n1")})
add("physics/physics/cyclotron_radius", **{"{}": ("orbit radius", "metres"), "[m]": ("mass", "kilograms"), "[v]": ("speed", "metres per second"), "[q]": ("charge", "coulombs"), "[B]": ("magnetic field", "tesla")})
add("physics/physics/de_broglie_wavelength", **{"{}": ("wavelength", "metres"), "[m]": ("mass", "kilograms"), "[v]": ("speed", "metres per second"), "h": ("Planck constant", "6.626e-34 J s")})
add("physics/physics/density", **{"{}": ("density", "kilograms per cubic metre"), "[m]": ("mass", "kilograms"), "[V]": ("volume", "cubic metres")})
add("physics/physics/diffraction_grating", **{"{}": ("diffraction angle", "radians"), "[m]": ("order", "0, 1, 2, ..."), "[wavelength]": ("wavelength", "metres"), "[d]": ("slit spacing", "metres")})
add("physics/physics/displacement", **{"{}": ("displacement", "metres"), "[u]": ("starting speed", "metres per second"), "[a]": ("acceleration", "metres per second squared"), "[t]": ("time", "seconds")})
add("physics/physics/double_slit_fringe_spacing", **{"{}": ("fringe spacing", "metres on the screen"), "[wavelength]": ("wavelength", "metres"), "[L]": ("screen distance", "metres"), "[d]": ("slit separation", "metres")})
add("physics/physics/electric_power", **{"{}": ("power", "watts"), "[I]": ("current", "amperes"), "[V]": ("voltage", "volts")})
add("physics/physics/energy_momentum_relation", **{"{}": ("total energy", "joules"), "[m]": ("rest mass", "kilograms"), "[p]": ("momentum", "kg m/s"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/faradays_law", **{"{}": ("induced emf", "volts"), "[N]": ("number of turns", "how many loops"), "[delta_flux]": ("flux change", "webers"), "[dt]": ("time taken", "seconds")})
add("physics/physics/final_velocity", **{"{}": ("final speed", "metres per second"), "[u]": ("starting speed", "metres per second"), "[a]": ("acceleration", "metres per second squared"), "[t]": ("time", "seconds")})
add("physics/physics/frequency", **{"{}": ("frequency", "hertz, cycles per second"), "[T]": ("period", "seconds for one cycle")})
add("physics/physics/gravitation", **{"{}": ("force", "newtons, the pull between the masses"), "G": ("gravitational constant", "6.674e-11 N m2/kg2"), "[m1]": ("first mass", "kilograms"), "[m2]": ("second mass", "kilograms"), "[r]": ("separation", "metres between the centres")})
add("physics/physics/gravitational_time_dilation", **{"{}": ("clock time", "seconds on the clock near the mass"), "[dt]": ("far-away time", "seconds measured far from the mass"), "[M]": ("mass", "kilograms"), "[r]": ("distance", "metres from the centre, outside the horizon"), "G": ("gravitational constant", "6.674e-11 N m2/kg2"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/heat", **{"{}": ("heat", "joules"), "[m]": ("mass", "kilograms"), "[c]": ("specific heat", "joules per kilogram per kelvin"), "[delta_T]": ("temperature change", "kelvin")})
add("physics/physics/heisenberg_uncertainty", **{"{}": ("momentum uncertainty", "smallest possible, kg m/s"), "[delta_x]": ("position uncertainty", "metres")})
add("physics/physics/hooke_s_law", **{"{}": ("restoring force", "newtons, back toward the rest point"), "[k]": ("spring constant", "newtons per metre"), "[x]": ("stretch", "metres from the rest point")})
add("physics/physics/hydraulic_press", **{"{}": ("output force", "newtons"), "[F1]": ("input force", "newtons"), "[A1]": ("input area", "square metres"), "[A2]": ("output area", "square metres")})
add("physics/physics/hydrostatic_pressure", **{"{}": ("pressure", "pascals, from the fluid alone"), "[rho]": ("density", "kilograms per cubic metre"), "[h]": ("depth", "metres"), "g": ("gravity", "9.81 m/s2")})
add("physics/physics/ideal_gas_law", **{"{}": ("pressure", "pascals"), "[n]": ("amount of gas", "moles"), "[T]": ("temperature", "kelvin"), "[V]": ("volume", "cubic metres"), "R": ("gas constant", "8.314 J/(mol K)")})
add("physics/physics/impulse", **{"{}": ("impulse", "newton seconds, the change in momentum"), "[F]": ("force", "newtons"), "[dt]": ("time", "seconds the force acts")})
add("physics/physics/inductor_energy", **{"{}": ("stored energy", "joules"), "[L]": ("inductance", "henries"), "[I]": ("current", "amperes")})
add("physics/physics/kinetic_energy", **{"{}": ("kinetic energy", "joules"), "[m]": ("mass", "kilograms"), "[v]": ("speed", "metres per second")})
add("physics/physics/length_contraction", **{"{}": ("moving length", "metres, in the direction of motion"), "[L0]": ("rest length", "metres"), "[v]": ("speed", "metres per second"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/lens_magnification", **{"{}": ("magnification", "negative means the image is upside down"), "[d_i]": ("image distance", "metres"), "[d_o]": ("object distance", "metres")})
add("physics/physics/lensmakers_equation", **{"{}": ("focal length", "metres"), "[n]": ("refractive index", "of the lens glass"), "[R1]": ("first radius", "metres, sign by the sign convention"), "[R2]": ("second radius", "metres")})
add("physics/physics/lorentz_factor", **{"{}": ("Lorentz factor", "how much time and mass stretch"), "[v]": ("speed", "metres per second, less than light"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/magnetic_field_solenoid", **{"{}": ("magnetic field", "tesla, inside the coil"), "[n]": ("turns per metre", "how tightly the wire is wound"), "[I]": ("current", "amperes")})
add("physics/physics/magnetic_field_straight_wire", **{"{}": ("magnetic field", "tesla"), "[I]": ("current", "amperes"), "[r]": ("distance", "metres from the wire")})
add("physics/physics/magnetic_flux", **{"{}": ("flux", "webers"), "[B]": ("magnetic field", "tesla"), "[A]": ("area", "square metres"), "[theta]": ("angle", "radians, between the field and the normal")})
add("physics/physics/magnetic_force_on_charge", **{"{}": ("force", "newtons"), "[q]": ("charge", "coulombs"), "[v]": ("speed", "metres per second"), "[B]": ("magnetic field", "tesla"), "[theta]": ("angle", "radians, between velocity and field")})
add("physics/physics/magnetic_force_on_wire", **{"{}": ("force", "newtons"), "[B]": ("magnetic field", "tesla"), "[I]": ("current", "amperes"), "[L]": ("length", "metres of wire in the field"), "[theta]": ("angle", "radians, between the wire and the field")})
add("physics/physics/malus_law", **{"{}": ("transmitted intensity", "watts per square metre"), "[I0]": ("starting intensity", "watts per square metre"), "[theta]": ("angle", "radians between the two polariser axes")})
add("physics/physics/mass_energy_equivalence", **{"{}": ("energy", "joules"), "[m]": ("mass", "kilograms"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/momentum", **{"{}": ("momentum", "kg m/s"), "[m]": ("mass", "kilograms"), "[v]": ("velocity", "metres per second")})
add("physics/physics/motional_emf", **{"{}": ("induced emf", "volts"), "[B]": ("magnetic field", "tesla"), "[L]": ("rod length", "metres"), "[v]": ("speed", "metres per second across the field")})
add("physics/physics/newton_s_second_law", **{"{}": ("force", "newtons"), "[m]": ("mass", "kilograms"), "[a]": ("acceleration", "metres per second squared")})
add("physics/physics/ohm_s_law", **{"{}": ("voltage", "volts"), "[I]": ("current", "amperes"), "[R]": ("resistance", "ohms")})
add("physics/physics/particle_in_a_box", **{"{}": ("energy", "joules"), "[n]": ("level number", "1, 2, 3, ..."), "[m]": ("mass", "kilograms"), "[L]": ("box width", "metres"), "h": ("Planck constant", "6.626e-34 J s")})
add("physics/physics/pendulum_period", **{"{}": ("period", "seconds for one swing"), "[L]": ("length", "metres of the string"), "g": ("gravity", "9.81 m/s2")})
add("physics/physics/photoelectric_effect", **{"{}": ("maximum kinetic energy", "joules of the freed electron, or 0"), "[f]": ("light frequency", "hertz"), "[work_function]": ("work function", "joules to free one electron"), "h": ("Planck constant", "6.626e-34 J s")})
add("physics/physics/photon_energy", **{"{}": ("photon energy", "joules"), "[f]": ("frequency", "hertz"), "h": ("Planck constant", "6.626e-34 J s")})
add("physics/physics/photon_momentum", **{"{}": ("photon momentum", "kg m/s"), "[wavelength]": ("wavelength", "metres"), "h": ("Planck constant", "6.626e-34 J s")})
add("physics/physics/poiseuille_flow", **{"{}": ("volume flow", "cubic metres per second"), "[r]": ("pipe radius", "metres"), "[delta_P]": ("pressure drop", "pascals along the pipe"), "[mu]": ("viscosity", "pascal seconds"), "[L]": ("pipe length", "metres")})
add("physics/physics/potential_energy", **{"{}": ("potential energy", "joules"), "[m]": ("mass", "kilograms"), "[h]": ("height", "metres"), "g": ("gravity", "9.81 m/s2")})
add("physics/physics/power_physics", **{"{}": ("power", "watts"), "[W]": ("work", "joules"), "[t]": ("time", "seconds")})
add("physics/physics/pressure", **{"{}": ("pressure", "pascals"), "[F]": ("force", "newtons"), "[A]": ("area", "square metres")})
add("physics/physics/quantum_harmonic_oscillator", **{"{}": ("energy", "joules"), "[n]": ("level number", "0, 1, 2, ..."), "[omega]": ("angular frequency", "radians per second")})
add("physics/physics/refractive_index", **{"{}": ("refractive index", "how much the material slows light"), "[v]": ("speed in the material", "metres per second"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/relativistic_doppler", **{"{}": ("observed frequency", "hertz"), "[f0]": ("proper frequency", "hertz of the source"), "[v]": ("speed", "metres per second, positive when receding"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/relativistic_kinetic_energy", **{"{}": ("kinetic energy", "joules above the rest energy"), "[m]": ("rest mass", "kilograms"), "[v]": ("speed", "metres per second"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/relativistic_momentum", **{"{}": ("momentum", "kg m/s"), "[m]": ("rest mass", "kilograms"), "[v]": ("speed", "metres per second"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/relativistic_velocity_addition", **{"{}": ("combined speed", "metres per second"), "[u]": ("first speed", "metres per second"), "[v]": ("second speed", "metres per second, in the same direction"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/resistors_in_parallel", **{"{}": ("total resistance", "ohms"), "[resistors]": ("resistances", "ohms, one number for each resistor")})
add("physics/physics/resistors_in_series", **{"{}": ("total resistance", "ohms"), "[resistors]": ("resistances", "ohms, one number for each resistor")})
add("physics/physics/reynolds_number", **{"{}": ("Reynolds number", "small means smooth flow, large means turbulent"), "[rho]": ("density", "kilograms per cubic metre"), "[v]": ("speed", "metres per second"), "[L]": ("size", "metres, a length of the object"), "[mu]": ("viscosity", "pascal seconds")})
add("physics/physics/rydberg_formula", **{"{}": ("wavelength", "metres of the emitted light"), "[n1]": ("lower level", "1, 2, 3, ..."), "[n2]": ("upper level", "greater than n1"), "R": ("Rydberg constant", "1.097e7 per metre"), "Z": ("atomic number", "1 for hydrogen")})
add("physics/physics/schwarzschild_radius", **{"{}": ("horizon radius", "metres"), "[M]": ("mass", "kilograms"), "G": ("gravitational constant", "6.674e-11 N m2/kg2"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/self_induced_emf", **{"{}": ("induced emf", "volts"), "[L]": ("inductance", "henries"), "[delta_I]": ("current change", "amperes"), "[dt]": ("time taken", "seconds")})
add("physics/physics/snell_s_law", **{"{}": ("refracted angle", "radians"), "[n1]": ("first index", "where the light starts"), "[theta1]": ("incoming angle", "radians"), "[n2]": ("second index", "where the light goes")})
add("physics/physics/stokes_drag", **{"{}": ("drag force", "newtons"), "[mu]": ("viscosity", "pascal seconds"), "[r]": ("sphere radius", "metres"), "[v]": ("speed", "metres per second")})
add("physics/physics/thin_lens_equation", **{"{}": ("image distance", "metres"), "[f]": ("focal length", "metres"), "[d_o]": ("object distance", "metres")})
add("physics/physics/time_dilation", **{"{}": ("elapsed time", "seconds for the stay-at-home clock"), "[dt0]": ("proper time", "seconds on the moving clock"), "[v]": ("speed", "metres per second"), "c": ("speed of light", "299792458 m/s")})
add("physics/physics/torque", **{"{}": ("torque", "newton metres"), "[r]": ("lever arm", "metres"), "[F]": ("force", "newtons"), "[theta]": ("angle", "radians between the arm and the force")})
add("physics/physics/torricelli_speed", **{"{}": ("exit speed", "metres per second"), "[h]": ("depth", "metres from the surface to the hole"), "g": ("gravity", "9.81 m/s2")})
add("physics/physics/velocity", **{"{}": ("velocity", "metres per second"), "[d]": ("displacement", "metres"), "[t]": ("time", "seconds")})
add("physics/physics/velocity_squared", **{"{}": ("final speed", "metres per second"), "[u]": ("starting speed", "metres per second"), "[a]": ("acceleration", "metres per second squared"), "[s]": ("distance", "metres")})
add("physics/physics/volume_flow_rate", **{"{}": ("volume flow", "cubic metres per second"), "[A]": ("area", "square metres"), "[v]": ("speed", "metres per second")})
add("physics/physics/wave_speed", **{"{}": ("wave speed", "metres per second"), "[f]": ("frequency", "hertz"), "[wavelength]": ("wavelength", "metres")})
add("physics/physics/weight", **{"{}": ("weight", "newtons"), "[m]": ("mass", "kilograms"), "g": ("gravity", "9.81 m/s2")})
add("physics/physics/work", **{"{}": ("work", "joules"), "[F]": ("force", "newtons, along the motion"), "[d]": ("distance", "metres")})

# ---------------------------------------------------------------- geometry
add("geometry/geometry/arc_length", **{"{}": ("arc length", "metres along the circle"), "[r]": ("radius", "metres"), "[theta]": ("angle", "radians")})
add("geometry/geometry/circle_area", **{"{}": ("area", "square metres"), "[r]": ("radius", "metres")})
add("geometry/geometry/circle_circumference", **{"{}": ("circumference", "metres around the circle"), "[r]": ("radius", "metres")})
add("geometry/geometry/cone_surface_area", **{"{}": ("surface area", "square metres, including the base"), "[r]": ("base radius", "metres"), "[l]": ("slant height", "metres along the side")})
add("geometry/geometry/cone_volume", **{"{}": ("volume", "cubic metres"), "[r]": ("base radius", "metres"), "[h]": ("height", "metres")})
add("geometry/geometry/cube_surface_area", **{"{}": ("surface area", "square metres"), "[s]": ("side", "metres")})
add("geometry/geometry/cube_volume", **{"{}": ("volume", "cubic metres"), "[s]": ("side", "metres")})
add("geometry/geometry/cylinder_surface_area", **{"{}": ("surface area", "square metres, including both ends"), "[r]": ("radius", "metres"), "[h]": ("height", "metres")})
add("geometry/geometry/cylinder_volume", **{"{}": ("volume", "cubic metres"), "[r]": ("radius", "metres"), "[h]": ("height", "metres")})
add("geometry/geometry/degrees_to_radians_geometry", **{"[degrees]": ("angle", "degrees"), "{}": ("angle", "radians")})
add("geometry/geometry/distance_formula", **{"{}": ("distance", "metres between the two points"), "[x1]": ("first x", "metres"), "[y1]": ("first y", "metres"), "[x2]": ("second x", "metres"), "[y2]": ("second y", "metres")})
add("geometry/geometry/heron_s_formula", **{"{}": ("area", "square metres of the triangle"), "[a]": ("side a", "metres"), "[b]": ("side b", "metres"), "[c]": ("side c", "metres"), "s": ("semi-perimeter", "(a + b + c) / 2, not typed")})
add("geometry/geometry/law_of_cosines", **{"{}": ("side c", "metres, opposite angle C"), "[a]": ("side a", "metres"), "[b]": ("side b", "metres"), "[C]": ("included angle", "radians")})
add("geometry/geometry/law_of_sines", **{"{}": ("side b", "metres, opposite angle B"), "[a]": ("side a", "metres"), "[A]": ("angle A", "radians, opposite side a"), "[B]": ("angle B", "radians")})
add("geometry/geometry/midpoint_formula", **{"{}": ("midpoint", "the point halfway between"), "[x1]": ("first x", "metres"), "[y1]": ("first y", "metres"), "[x2]": ("second x", "metres"), "[y2]": ("second y", "metres")})
add("geometry/geometry/parallelogram_area", **{"{}": ("area", "square metres"), "[b]": ("base", "metres"), "[h]": ("height", "metres, perpendicular to the base")})
add("geometry/geometry/polygon_interior_angle_sum", **{"[n]": ("number of sides", "3 or more"), "{}": ("angle sum", "degrees, inside the polygon")})
add("geometry/geometry/pyramid_volume", **{"{}": ("volume", "cubic metres"), "[base_area]": ("base area", "square metres"), "[h]": ("height", "metres")})
add("geometry/geometry/pythagorean_theorem", **{"{}": ("hypotenuse", "metres, the longest side"), "[a]": ("leg a", "metres"), "[b]": ("leg b", "metres")})
add("geometry/geometry/radians_to_degrees_geometry", **{"[radians]": ("angle", "radians"), "{}": ("angle", "degrees")})
add("geometry/geometry/rectangle_area", **{"{}": ("area", "square metres"), "[l]": ("length", "metres"), "[w]": ("width", "metres")})
add("geometry/geometry/rectangle_perimeter", **{"{}": ("perimeter", "metres around the rectangle"), "[l]": ("length", "metres"), "[w]": ("width", "metres")})
add("geometry/geometry/rectangular_prism_surface_area", **{"{}": ("surface area", "square metres"), "[l]": ("length", "metres"), "[w]": ("width", "metres"), "[h]": ("height", "metres")})
add("geometry/geometry/rectangular_prism_volume", **{"{}": ("volume", "cubic metres"), "[l]": ("length", "metres"), "[w]": ("width", "metres"), "[h]": ("height", "metres")})
add("geometry/geometry/regular_polygon_area", **{"{}": ("area", "square metres"), "[perimeter]": ("perimeter", "metres"), "[apothem]": ("apothem", "metres from the centre to a side")})
add("geometry/geometry/rhombus_area", **{"{}": ("area", "square metres"), "[d1]": ("first diagonal", "metres"), "[d2]": ("second diagonal", "metres")})
add("geometry/geometry/sector_area", **{"{}": ("sector area", "square metres of the pie slice"), "[r]": ("radius", "metres"), "[theta]": ("angle", "radians")})
add("geometry/geometry/slope", **{"{}": ("slope", "rise over run"), "[x1]": ("first x", "metres"), "[y1]": ("first y", "metres"), "[x2]": ("second x", "metres"), "[y2]": ("second y", "metres")})
add("geometry/geometry/sphere_surface_area", **{"{}": ("surface area", "square metres"), "[r]": ("radius", "metres")})
add("geometry/geometry/sphere_volume", **{"{}": ("volume", "cubic metres"), "[r]": ("radius", "metres")})
add("geometry/geometry/square_area", **{"{}": ("area", "square metres"), "[s]": ("side", "metres")})
add("geometry/geometry/trapezoid_area", **{"{}": ("area", "square metres"), "[a]": ("first base", "metres"), "[b]": ("second base", "metres"), "[h]": ("height", "metres")})
add("geometry/geometry/triangle_area", **{"{}": ("area", "square metres"), "[b]": ("base", "metres"), "[h]": ("height", "metres")})

# ---------------------------------------------------------------- statistics
add("math/statistics_and_probability/bayes_theorem", **{"{}": ("updated probability", "P(A|B), after seeing B"), "[p_b_given_a]": ("likelihood", "P(B|A)"), "[p_a]": ("prior", "P(A), before seeing B"), "[p_b]": ("evidence", "P(B)")})
add("math/statistics_and_probability/binomial_distribution", **{"{}": ("probability", "of exactly k successes"), "[n]": ("trials", "how many times"), "[k]": ("successes", "how many you want"), "[p]": ("success chance", "between 0 and 1, each trial")})
add("math/statistics_and_probability/chi_square_statistic", **{"{}": ("chi-square", "how far the counts are from what was expected"), "[observed]": ("observed counts", "what you counted"), "[expected]": ("expected counts", "what the model predicted")})
add("math/statistics_and_probability/conditional_probability", **{"{}": ("conditional probability", "P(A|B)"), "[p_a_and_b]": ("joint probability", "P(A and B)"), "[p_b]": ("condition", "P(B), must be greater than 0")})
add("math/statistics_and_probability/confidence_interval", **{"{}": ("interval", "the range the mean is likely in"), "[mean]": ("sample mean", "average of the data"), "[sd]": ("standard deviation", "spread of the data"), "[n]": ("sample size", "how many values")})
add("math/statistics_and_probability/correlation", **{"{}": ("correlation", "from -1 to 1, how the two lists move together"), "[x]": ("first list", "one number per pair"), "[y]": ("second list", "one number per pair")})
add("math/statistics_and_probability/covariance", **{"{}": ("covariance", "positive if the lists rise together"), "[x]": ("first list", "one number per pair"), "[y]": ("second list", "one number per pair")})
add("math/statistics_and_probability/expected_value", **{"{}": ("expected value", "the probability-weighted average"), "[values]": ("values", "the possible numbers"), "[probs]": ("probabilities", "same length as the values, they add to 1")})
add("math/statistics_and_probability/exponential_distribution", **{"{}": ("density", "chance density at x"), "[x]": ("value", "zero or greater"), "[lam]": ("rate", "how many events per unit of time")})
add("math/statistics_and_probability/interquartile_range", **{"{}": ("interquartile range", "third quartile minus the first"), "[data]": ("data", "the list of numbers")})
add("math/statistics_and_probability/linear_regression", **{"{}": ("best-fit line", "slope and intercept"), "[x]": ("x values", "the inputs"), "[y]": ("y values", "the outputs, one per x")})
add("math/statistics_and_probability/mean", **{"{}": ("mean", "the average"), "[data]": ("data", "the list of numbers")})
add("math/statistics_and_probability/median", **{"{}": ("median", "the middle value"), "[data]": ("data", "the list of numbers")})
add("math/statistics_and_probability/mode", **{"{}": ("mode", "the most common value"), "[data]": ("data", "the list of numbers")})
add("math/statistics_and_probability/normal_distribution", **{"{}": ("density", "the bell-curve height at x"), "[x]": ("value", "where you read the curve")})
add("math/statistics_and_probability/p_value", **{"{}": ("p-value", "chance of a result at least this far from the mean"), "[z]": ("z score", "how many standard deviations from the mean")})
add("math/statistics_and_probability/percentile", **{"{}": ("percentile value", "the value that k percent of the data is below"), "[data]": ("data", "the list of numbers"), "[k]": ("percent", "0 to 100")})
add("math/statistics_and_probability/poisson_distribution", **{"{}": ("probability", "of exactly k events"), "[k]": ("count", "0, 1, 2, ..."), "[lam]": ("average count", "the expected number")})
add("math/statistics_and_probability/probability", **{"{}": ("probability", "favourable divided by total"), "[favorable]": ("favourable", "how many ways the event happens"), "[total]": ("total", "how many ways there are")})
add("math/statistics_and_probability/quartiles", **{"{}": ("quartiles", "the 25, 50 and 75 percent points"), "[data]": ("data", "the list of numbers")})
add("math/statistics_and_probability/range", **{"{}": ("range", "largest minus smallest"), "[data]": ("data", "the list of numbers")})
add("math/statistics_and_probability/sample_standard_deviation", **{"{}": ("sample standard deviation", "spread, dividing by n - 1"), "[data]": ("data", "the list of numbers")})
add("math/statistics_and_probability/sample_variance", **{"{}": ("sample variance", "spread squared, dividing by n - 1"), "[data]": ("data", "the list of numbers")})
add("math/statistics_and_probability/standard_deviation", **{"{}": ("standard deviation", "the usual spread of the numbers"), "[data]": ("data", "the list of numbers")})
add("math/statistics_and_probability/t_test_statistic", **{"{}": ("t statistic", "how far the mean is from the claimed value"), "[mean]": ("sample mean", "average of the data"), "[mu0]": ("claimed mean", "the value being tested"), "[s]": ("sample standard deviation", "spread of the data"), "[n]": ("sample size", "how many values")})
add("math/statistics_and_probability/uniform_distribution", **{"{}": ("density", "the same height everywhere between a and b"), "[x]": ("value", "where you read the density"), "[a]": ("low end", "the smallest possible value"), "[b]": ("high end", "the largest possible value")})
add("math/statistics_and_probability/variance", **{"{}": ("variance", "the square of the standard deviation"), "[data]": ("data", "the list of numbers")})
add("math/statistics_and_probability/variance_of_random_variable", **{"{}": ("variance", "the spread of a random variable"), "[values]": ("values", "the possible numbers"), "[probs]": ("probabilities", "same length as the values")})
add("math/statistics_and_probability/z_score", **{"{}": ("z score", "how many standard deviations x is from the mean"), "[x]": ("value", "the number you measured"), "[mean]": ("mean", "the average"), "[sd]": ("standard deviation", "the spread")})


TOKEN = re.compile(r"\S*?\{[^{}|]*\|[^{}]*\}|\S+")


def annotate_side(text, words):
    out = []
    for raw in TOKEN.findall(text):
        if "|" in raw and "{" in raw:
            out.append(raw)
            continue
        pair = words.get(raw)
        if pair and all(ch not in pair[0] + pair[1] for ch in "|{}"):
            out.append("%s{%s|%s}" % (raw, pair[0], pair[1]))
        else:
            out.append(raw)
    return " ".join(out)


def annotate(dsl, words):
    # words on the right of => are not allowed: that side may only be {}
    left, arrow, right = dsl.partition("=>")
    left = annotate_side(left, words)
    right = right.strip()
    if right.startswith("{}"):
        right = "{}"
    return left + (" => " + right if arrow else "")


def main():
    lines = open(SPEC, encoding="utf-8").read().splitlines()
    changed = 0
    new = []
    for line in lines:
        if not line.strip() or line.startswith("#") or "|" not in line:
            new.append(line)
            continue
        key, _, dsl = line.partition("|")
        key = key.strip()
        if key not in W:
            new.append(line)
            continue
        new.append(key + " | " + annotate(dsl.strip(), W[key]))
        changed += 1
    open(SPEC, "w", encoding="utf-8", newline="\n").write("\n".join(new) + "\n")
    print("annotated", changed, "operators")


if __name__ == "__main__":
    main()
