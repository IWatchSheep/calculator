//! Physics operators ported from `operators_one_operator_per_file/physics/physics/*`.
//! One function per operator, named after the folder.  The arguments arrive in this order: the row boxes
//! first, then the optional constants (g, c, h ...) in the order of the Python signature, already filled
//! with their defaults (see `extra` in `generated.rs`).  A result that is not a finite number is turned
//! into an error by `Operator::run`, which is how Python's ZeroDivisionError / math domain errors show up.

use crate::value::Value;
use std::f64::consts::PI;

type R = Result<Value, String>;

fn n(x: f64) -> R {
    Ok(Value::Number(x))
}

/// a / b, but an error (like Python's ZeroDivisionError) when b is 0.
fn d(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("division by zero".into())
    } else {
        Ok(a / b)
    }
}

fn need(cond: bool, msg: &str) -> Result<(), String> {
    if cond {
        Ok(())
    } else {
        Err(msg.into())
    }
}

pub fn bernoulli_equation(a: &[f64]) -> R {
    // P1, v1, h1, v2, h2, rho, g
    n(a[0] + 0.5 * a[5] * (a[1].powi(2) - a[3].powi(2)) + a[5] * a[6] * (a[2] - a[4]))
}
pub fn bohr_energy_level(a: &[f64]) -> R {
    // n, Z
    n(-13.605693122994 * a[1].powi(2) / a[0].powi(2))
}
pub fn brewster_angle(a: &[f64]) -> R {
    n(d(a[1], a[0])?.atan())
}
pub fn buoyant_force(a: &[f64]) -> R {
    // rho, V, g
    n(a[0] * a[2] * a[1])
}
pub fn capacitance(a: &[f64]) -> R {
    n(a[0] * a[1])
}
pub fn centripetal_acceleration(a: &[f64]) -> R {
    n(a[0].powi(2) / a[1])
}
pub fn compton_shift(a: &[f64]) -> R {
    // theta, m, h, c
    n(a[2] / (a[1] * a[3]) * (1.0 - a[0].cos()))
}
pub fn continuity_equation(a: &[f64]) -> R {
    n(a[0] * a[1] / a[2])
}
pub fn coulomb_s_law(a: &[f64]) -> R {
    // q1, q2, r, k
    n(a[3] * a[0] * a[1] / a[2].powi(2))
}
pub fn critical_angle(a: &[f64]) -> R {
    need(a[0] > a[1], "total internal reflection needs n1 > n2")?;
    n((a[1] / a[0]).asin())
}
pub fn cyclotron_radius(a: &[f64]) -> R {
    n(a[0] * a[1] / (a[2].abs() * a[3]))
}
pub fn de_broglie_wavelength(a: &[f64]) -> R {
    // m, v, h
    n(a[2] / (a[0] * a[1]))
}
pub fn density(a: &[f64]) -> R {
    n(a[0] / a[1])
}
pub fn diffraction_grating(a: &[f64]) -> R {
    let s = a[0] * a[1] / a[2];
    need(s.abs() <= 1.0, "this order does not exist")?;
    n(s.asin())
}
pub fn displacement(a: &[f64]) -> R {
    n(a[0] * a[2] + 0.5 * a[1] * a[2].powi(2))
}
pub fn double_slit_fringe_spacing(a: &[f64]) -> R {
    n(a[0] * a[1] / a[2])
}
pub fn electric_power(a: &[f64]) -> R {
    n(a[0] * a[1])
}
pub fn energy_momentum_relation(a: &[f64]) -> R {
    // m, p, c
    n(((a[1] * a[2]).powi(2) + (a[0] * a[2].powi(2)).powi(2)).sqrt())
}
pub fn faradays_law(a: &[f64]) -> R {
    n(-a[0] * a[1] / a[2])
}
pub fn final_velocity(a: &[f64]) -> R {
    n(a[0] + a[1] * a[2])
}
pub fn frequency(a: &[f64]) -> R {
    n(1.0 / a[0])
}
pub fn gravitation(a: &[f64]) -> R {
    // m1, m2, r, G
    n(a[3] * a[0] * a[1] / a[2].powi(2))
}
pub fn gravitational_time_dilation(a: &[f64]) -> R {
    // dt, M, r, G, c
    let (dt, m, r, g, c) = (a[0], a[1], a[2], a[3], a[4]);
    need(r > 2.0 * g * m / c.powi(2), "r must be outside the Schwarzschild radius")?;
    n(dt * (1.0 - 2.0 * g * m / (r * c.powi(2))).sqrt())
}
pub fn heat(a: &[f64]) -> R {
    n(a[0] * a[1] * a[2])
}
pub fn heisenberg_uncertainty(a: &[f64]) -> R {
    // delta_x, hbar
    n(a[1] / (2.0 * a[0]))
}
pub fn hooke_s_law(a: &[f64]) -> R {
    n(-a[0] * a[1])
}
pub fn hydraulic_press(a: &[f64]) -> R {
    n(a[0] * a[2] / a[1])
}
pub fn hydrostatic_pressure(a: &[f64]) -> R {
    // rho, h, g
    n(a[0] * a[2] * a[1])
}
pub fn ideal_gas_law(a: &[f64]) -> R {
    // n, T, V, R
    n(a[0] * a[3] * a[1] / a[2])
}
pub fn impulse(a: &[f64]) -> R {
    n(a[0] * a[1])
}
pub fn inductor_energy(a: &[f64]) -> R {
    n(0.5 * a[0] * a[1].powi(2))
}
pub fn length_contraction(a: &[f64]) -> R {
    // L0, v, c
    need(a[1].abs() < a[2], "speed must be less than the speed of light")?;
    n(a[0] * (1.0 - a[1].powi(2) / a[2].powi(2)).sqrt())
}
pub fn lens_magnification(a: &[f64]) -> R {
    n(-a[0] / a[1])
}
pub fn lensmakers_equation(a: &[f64]) -> R {
    n(1.0 / ((a[0] - 1.0) * (d(1.0, a[1])? - d(1.0, a[2])?)))
}
pub fn magnetic_field_solenoid(a: &[f64]) -> R {
    // n, I, mu0
    n(a[2] * a[0] * a[1])
}
pub fn magnetic_field_straight_wire(a: &[f64]) -> R {
    // I, r, mu0
    n(a[2] * a[0] / (2.0 * PI * a[1]))
}
pub fn magnetic_flux(a: &[f64]) -> R {
    n(a[0] * a[1] * a[2].cos())
}
pub fn magnetic_force_on_charge(a: &[f64]) -> R {
    n(a[0] * a[1] * a[2] * a[3].sin())
}
pub fn magnetic_force_on_wire(a: &[f64]) -> R {
    n(a[0] * a[1] * a[2] * a[3].sin())
}
pub fn malus_law(a: &[f64]) -> R {
    n(a[0] * a[1].cos().powi(2))
}
pub fn mass_energy_equivalence(a: &[f64]) -> R {
    // m, c
    n(a[0] * a[1].powi(2))
}
pub fn momentum(a: &[f64]) -> R {
    n(a[0] * a[1])
}
pub fn motional_emf(a: &[f64]) -> R {
    n(a[0] * a[1] * a[2])
}
pub fn particle_in_a_box(a: &[f64]) -> R {
    // n, m, L, h
    n(a[0].powi(2) * a[3].powi(2) / (8.0 * a[1] * a[2].powi(2)))
}
pub fn pendulum_period(a: &[f64]) -> R {
    // L, g
    n(2.0 * PI * (a[0] / a[1]).sqrt())
}
pub fn photoelectric_effect(a: &[f64]) -> R {
    // f, work_function, h
    n((a[2] * a[0] - a[1]).max(0.0))
}
pub fn photon_energy(a: &[f64]) -> R {
    // f, h
    n(a[1] * a[0])
}
pub fn photon_momentum(a: &[f64]) -> R {
    // wavelength, h
    n(a[1] / a[0])
}
pub fn poiseuille_flow(a: &[f64]) -> R {
    n(PI * a[0].powi(4) * a[1] / (8.0 * a[2] * a[3]))
}
pub fn power_physics(a: &[f64]) -> R {
    n(a[0] / a[1])
}
pub fn pressure(a: &[f64]) -> R {
    n(a[0] / a[1])
}
pub fn quantum_harmonic_oscillator(a: &[f64]) -> R {
    // n, omega, hbar
    n(a[2] * a[1] * (a[0] + 0.5))
}
pub fn refractive_index(a: &[f64]) -> R {
    // v, c
    n(a[1] / a[0])
}
pub fn relativistic_doppler(a: &[f64]) -> R {
    // f0, v, c
    need(a[1].abs() < a[2], "speed must be less than the speed of light")?;
    let beta = a[1] / a[2];
    n(a[0] * ((1.0 - beta) / (1.0 + beta)).sqrt())
}
pub fn gravitational_time_dilation_from_radius(a: &[f64]) -> R {
    // dt, rs, r
    need(a[2] > a[1], "r must be outside the Schwarzschild radius")?;
    n(a[0] * (1.0 - a[1] / a[2]).sqrt())
}
pub fn relativistic_beta(a: &[f64]) -> R {
    // v, c
    need(a[0].abs() < a[1], "speed must be less than the speed of light")?;
    n(a[0] / a[1])
}
pub fn relativistic_doppler_frequency(a: &[f64]) -> R {
    // f0, beta
    n(a[0] * ((1.0 - a[1]) / (1.0 + a[1])).sqrt())
}
pub fn relativistic_kinetic_energy_from_gamma(a: &[f64]) -> R {
    // gamma, m, c
    n((a[0] - 1.0) * a[1] * a[2].powi(2))
}
pub fn relativistic_momentum_from_gamma(a: &[f64]) -> R {
    // gamma, m, v
    n(a[1] * a[2] * a[0])
}
pub fn length_contraction_from_gamma(a: &[f64]) -> R {
    // L0, gamma
    n(a[0] / a[1])
}
pub fn time_dilation_from_gamma(a: &[f64]) -> R {
    // dt0, gamma
    n(a[0] * a[1])
}
pub fn relativistic_kinetic_energy(a: &[f64]) -> R {
    // m, v, c
    need(a[1].abs() < a[2], "speed must be less than the speed of light")?;
    n((1.0 / (1.0 - a[1].powi(2) / a[2].powi(2)).sqrt() - 1.0) * a[0] * a[2].powi(2))
}
pub fn relativistic_momentum(a: &[f64]) -> R {
    // m, v, c
    need(a[1].abs() < a[2], "speed must be less than the speed of light")?;
    n(a[0] * a[1] / (1.0 - a[1].powi(2) / a[2].powi(2)).sqrt())
}
pub fn relativistic_velocity_addition(a: &[f64]) -> R {
    // u, v, c
    n((a[0] + a[1]) / (1.0 + a[0] * a[1] / a[2].powi(2)))
}
pub fn reynolds_number(a: &[f64]) -> R {
    n(a[0] * a[1] * a[2] / a[3])
}
pub fn rydberg_formula(a: &[f64]) -> R {
    // n1, n2, Z, R
    need(a[1] > a[0], "n2 must be larger than n1")?;
    n(1.0 / (a[3] * a[2].powi(2) * (d(1.0, a[0].powi(2))? - d(1.0, a[1].powi(2))?)))
}
pub fn schwarzschild_radius(a: &[f64]) -> R {
    // M, G, c
    n(2.0 * a[1] * a[0] / a[2].powi(2))
}
pub fn self_induced_emf(a: &[f64]) -> R {
    n(-a[0] * a[1] / a[2])
}
pub fn snell_s_law(a: &[f64]) -> R {
    n((a[0] * a[1].sin() / a[2]).asin())
}
pub fn stokes_drag(a: &[f64]) -> R {
    n(6.0 * PI * a[0] * a[1] * a[2])
}
pub fn thin_lens_equation(a: &[f64]) -> R {
    n(1.0 / (d(1.0, a[0])? - d(1.0, a[1])?))
}
pub fn torque(a: &[f64]) -> R {
    n(a[0] * a[1] * a[2].sin())
}
pub fn torricelli_speed(a: &[f64]) -> R {
    // h, g
    n((2.0 * a[1] * a[0]).sqrt())
}
pub fn velocity_squared(a: &[f64]) -> R {
    n((a[0] * a[0] + 2.0 * a[1] * a[2]).sqrt())
}
pub fn volume_flow_rate(a: &[f64]) -> R {
    n(a[0] * a[1])
}
pub fn wave_speed(a: &[f64]) -> R {
    n(a[0] * a[1])
}
pub fn weight(a: &[f64]) -> R {
    // m, g
    n(a[0] * a[1])
}
pub fn work(a: &[f64]) -> R {
    n(a[0] * a[1])
}

// ---------- motion for a walking or flying robot (the same operations in the same order as the Python files) ----------

pub fn speed_after_distance(a: &[f64]) -> R {
    // u, a, s
    let v2 = a[0] * a[0] + 2.0 * a[1] * a[2];
    need(v2 >= 0.0, "the motion stops before that distance")?;
    n(v2.sqrt())
}

pub fn time_to_distance(a: &[f64]) -> R {
    // u, a, s
    let (u, acc, s) = (a[0], a[1], a[2]);
    if acc == 0.0 {
        if u == 0.0 {
            need(s == 0.0, "not moving")?;
            return n(0.0);
        }
        let t = s / u;
        need(t >= 0.0, "that distance is not reached")?;
        return n(t + 0.0);
    }
    let disc = u * u + 2.0 * acc * s;
    need(disc >= 0.0, "that distance is not reached")?;
    let root = disc.sqrt();
    let mut best: Option<f64> = None;
    for t in [(-u + root) / acc, (-u - root) / acc] {
        if t >= 0.0 && best.map_or(true, |b| t < b) {
            best = Some(t);
        }
    }
    let t = best.ok_or_else(|| "that distance is not reached".to_string())?;
    n(t + 0.0)
}

fn opposes(u: f64, a: f64) -> Result<(), String> {
    need(!(u != 0.0 && a == 0.0), "no acceleration, it does not stop")?;
    need(u * a <= 0.0, "it is speeding up, it does not stop")
}

pub fn stopping_distance(a: &[f64]) -> R {
    // u, a
    opposes(a[0], a[1])?;
    if a[0] == 0.0 {
        return n(0.0);
    }
    n(-a[0] * a[0] / (2.0 * a[1]))
}

pub fn braking_time(a: &[f64]) -> R {
    // u, a
    opposes(a[0], a[1])?;
    if a[0] == 0.0 {
        return n(0.0);
    }
    n(-a[0] / a[1])
}

fn launch(v: f64, angle: f64, g: f64) -> Result<(), String> {
    need(v >= 0.0, "speed cannot be negative")?;
    need(angle.abs() <= std::f64::consts::FRAC_PI_2, "the angle is past straight up")?;
    need(g > 0.0, "gravity must pull downward")
}

pub fn projectile_range(a: &[f64]) -> R {
    // v, angle, g
    launch(a[0], a[1], a[2])?;
    n(a[0] * a[0] * (2.0 * a[1]).sin() / a[2])
}

pub fn projectile_time_of_flight(a: &[f64]) -> R {
    // v, angle, g
    launch(a[0], a[1], a[2])?;
    n(2.0 * a[0] * a[1].sin() / a[2])
}

pub fn hover_thrust(a: &[f64]) -> R {
    // m, g
    need(a[0] > 0.0, "mass must be positive")?;
    need(a[1] > 0.0, "gravity must pull downward")?;
    n(a[0] * a[1])
}

// ---------- walking and flying mechanics, batch 4 (the same operations in the same order as the Python files) ----------

fn mass_slope_gravity(m: f64, angle: f64, g: f64) -> Result<(), String> {
    need(m > 0.0, "mass must be positive")?;
    need((0.0..=std::f64::consts::FRAC_PI_2).contains(&angle), "the slope is past vertical")?;
    need(g > 0.0, "gravity must pull downward")
}

pub fn slope_force(a: &[f64]) -> R {
    // m, angle, g
    mass_slope_gravity(a[0], a[1], a[2])?;
    n(a[0] * a[2] * a[1].sin())
}

pub fn max_friction_on_slope(a: &[f64]) -> R {
    // mu, m, angle, g
    need(a[0] >= 0.0, "friction cannot be negative")?;
    mass_slope_gravity(a[1], a[2], a[3])?;
    n(a[0] * a[1] * a[3] * a[2].cos())
}

pub fn steepest_climb_angle(a: &[f64]) -> R {
    need(a[0] >= 0.0, "friction cannot be negative")?;
    n(a[0].atan())
}

pub fn cylinder_moment_of_inertia(a: &[f64]) -> R {
    // mass, radius
    need(a[0] > 0.0, "mass must be positive")?;
    need(a[1] >= 0.0, "radius cannot be negative")?;
    n(0.5 * a[0] * a[1] * a[1])
}

pub fn angular_acceleration(a: &[f64]) -> R {
    // torque, inertia
    need(a[1] > 0.0, "the moment of inertia must be positive")?;
    n(a[0] / a[1])
}

pub fn tipping_margin(a: &[f64]) -> R {
    // half_width, height, angle
    need(a[0] >= 0.0 && a[1] >= 0.0, "a length cannot be negative")?;
    need((0.0..=std::f64::consts::FRAC_PI_2).contains(&a[2]), "the slope is past vertical")?;
    n(a[0] * a[2].cos() - a[1] * a[2].sin())
}

pub fn impact_force(a: &[f64]) -> R {
    // mass, speed, distance
    need(a[0] > 0.0, "mass must be positive")?;
    need(a[2] > 0.0, "the stopping distance must be positive")?;
    n(a[0] * a[1] * a[1] / (2.0 * a[2]))
}
