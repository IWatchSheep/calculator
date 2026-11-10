//! Operators on lists / vectors of numbers (statistics, vector algebra, series, interpolation, transforms).
//! One function per operator, named after its folder; `a` holds the box values, then the optional constants.

use super::vals::*;
use crate::value::Value;
use std::f64::consts::PI;

// ---------------------------------------------------------------- vectors
pub fn tensor_product(a: &[Value]) -> R {
    let (x, y) = (nums(&a[0])?, nums(&a[1])?);
    Ok(vlist(x.iter().flat_map(|p| y.iter().map(move |q| p * q)).collect()))
}

pub fn wedge_product(a: &[Value]) -> R {
    let (x, y) = (nums(&a[0])?, nums(&a[1])?);
    let mut out = vec![];
    for i in 0..x.len() {
        for j in i + 1..x.len() {
            out.push(x[i] * at(&y, j as i64)? - x[j] * at(&y, i as i64)?);
        }
    }
    Ok(vlist(out))
}

pub fn cross_product(a: &[Value]) -> R {
    let (x, y) = (nums(&a[0])?, nums(&a[1])?);
    let g = |v: &Vec<f64>, i: i64| at(v, i);
    Ok(vlist(vec![
        g(&x, 1)? * g(&y, 2)? - g(&x, 2)? * g(&y, 1)?,
        g(&x, 2)? * g(&y, 0)? - g(&x, 0)? * g(&y, 2)?,
        g(&x, 0)? * g(&y, 1)? - g(&x, 1)? * g(&y, 0)?,
    ]))
}

fn dot(x: &[f64], y: &[f64]) -> f64 {
    x.iter().zip(y).map(|(p, q)| p * q).sum()
}

pub fn dot_product(a: &[Value]) -> R {
    n(dot(&nums(&a[0])?, &nums(&a[1])?))
}

pub fn inner_product(a: &[Value]) -> R {
    n(dot(&nums(&a[0])?, &nums(&a[1])?))
}

fn hypot(v: &[f64]) -> f64 {
    let m = v.iter().fold(0.0_f64, |acc, x| acc.max(x.abs()));
    if m == 0.0 || !m.is_finite() {
        return m;
    }
    m * v.iter().map(|x| (x / m) * (x / m)).sum::<f64>().sqrt()
}

pub fn norm(a: &[Value]) -> R {
    // v, p
    let (v, p) = (nums(&a[0])?, num(&a[1])?);
    let mut s = 0.0;
    for x in &v {
        s += pypow(x.abs(), p)?;
    }
    n(pypow(s, div(1.0, p)?)?)
}

pub fn unit_vector(a: &[Value]) -> R {
    let v = nums(&a[0])?;
    let h = hypot(&v);
    let mut out = vec![];
    for x in &v {
        out.push(div(*x, h)?);
    }
    Ok(vlist(out))
}

pub fn vector_magnitude(a: &[Value]) -> R {
    n(hypot(&nums(&a[0])?))
}

pub fn vector_projection(a: &[Value]) -> R {
    let (x, y) = (nums(&a[0])?, nums(&a[1])?);
    let mut out = vec![];
    for q in &y {
        out.push(div(dot(&x, &y), dot(&y, &y))? * q);
    }
    Ok(vlist(out))
}

pub fn metric_space_distance(a: &[Value]) -> R {
    let (x, y) = (nums(&a[0])?, nums(&a[1])?);
    need(x.len() == y.len(), "both points must have the same number of dimensions")?;
    let d: Vec<f64> = x.iter().zip(&y).map(|(p, q)| p - q).collect();
    n(hypot(&d))
}

// ---------------------------------------------------------------- sums, products, series
pub fn product(a: &[Value]) -> R {
    n(nums(&a[0])?.iter().product())
}

pub fn summation(a: &[Value]) -> R {
    n(nums(&a[0])?.iter().sum())
}

pub fn maclaurin_series(a: &[Value]) -> R {
    let (d, x) = (nums(&a[0])?, num(&a[1])?);
    let mut s = 0.0;
    for (k, dk) in d.iter().enumerate() {
        s += dk / factorial(k)? * pypow(x, k as f64)?;
    }
    n(s)
}

pub fn taylor_series(a: &[Value]) -> R {
    // derivs, a, x
    let (d, c, x) = (nums(&a[0])?, num(&a[1])?, num(&a[2])?);
    let mut s = 0.0;
    for (k, dk) in d.iter().enumerate() {
        s += dk / factorial(k)? * pypow(x - c, k as f64)?;
    }
    n(s)
}

pub fn generating_function(a: &[Value]) -> R {
    let (t, x) = (nums(&a[0])?, num(&a[1])?);
    let mut s = 0.0;
    for (k, tk) in t.iter().enumerate() {
        s += tk * pypow(x, k as f64)?;
    }
    n(s)
}

pub fn burnside_s_lemma(a: &[Value]) -> R {
    let f = nums(&a[0])?;
    n(div(f.iter().sum(), f.len() as f64)?)
}

pub fn recurrence_relation(a: &[Value]) -> R {
    // coeffs, start, n
    let (coeffs, start, idx) = (nums(&a[0])?, nums(&a[1])?, int_of(num(&a[2])?)?);
    need(start.len() >= coeffs.len(), "give at least as many starting terms as coefficients")?;
    let mut seq = start;
    while (seq.len() as i64) <= idx {
        let last = seq.len();
        let mut s = 0.0;
        for (i, c) in coeffs.iter().enumerate() {
            s += c * seq[last - 1 - i];
        }
        seq.push(s);
    }
    n(at(&seq, idx)?)
}

pub fn alternating_series_test(a: &[Value]) -> R {
    let t: Vec<f64> = nums(&a[0])?.iter().map(|x| x.abs()).collect();
    let dec = t.windows(2).all(|w| w[1] <= w[0]);
    Ok(Value::Tuple(vec![Value::Bool(dec), Value::Number(at(&t, -1)?)]))
}

pub fn comparison_test(a: &[Value]) -> R {
    let (x, y) = (nums(&a[0])?, nums(&a[1])?);
    b(x.len() == y.len() && x.iter().zip(&y).all(|(p, q)| 0.0 <= *p && p <= q))
}

pub fn convergence(a: &[Value]) -> R {
    // terms, L, eps
    let (t, l, eps) = (nums(&a[0])?, num(&a[1])?, num(&a[2])?);
    let mut last_bad: i64 = -1;
    for (k, x) in t.iter().enumerate() {
        if (x - l).abs() >= eps {
            last_bad = k as i64;
        }
    }
    need(last_bad != t.len() as i64 - 1, "the last term is not within eps of L")?;
    n((last_bad + 1) as f64)
}

pub fn infimum(a: &[Value]) -> R {
    let v = nums(&a[0])?;
    need(!v.is_empty(), "min() of an empty list")?;
    n(v.iter().cloned().fold(f64::INFINITY, f64::min))
}

pub fn supremum(a: &[Value]) -> R {
    let v = nums(&a[0])?;
    need(!v.is_empty(), "max() of an empty list")?;
    n(v.iter().cloned().fold(f64::NEG_INFINITY, f64::max))
}

pub fn limit_inferior(a: &[Value]) -> R {
    let v = nums(&a[0])?;
    let tail = &v[v.len() / 2..];
    need(!tail.is_empty(), "min() of an empty list")?;
    n(tail.iter().cloned().fold(f64::INFINITY, f64::min))
}

pub fn limit_superior(a: &[Value]) -> R {
    let v = nums(&a[0])?;
    let tail = &v[v.len() / 2..];
    need(!tail.is_empty(), "max() of an empty list")?;
    n(tail.iter().cloned().fold(f64::NEG_INFINITY, f64::max))
}

pub fn series_convergence_test(a: &[Value]) -> R {
    let t = nums(&a[0])?;
    let r = div(at(&t, -1)?, at(&t, -2)?)?.abs();
    let verdict = if r < 1.0 {
        "converges (ratio < 1)"
    } else if r > 1.0 {
        "diverges (ratio > 1)"
    } else {
        "inconclusive (ratio = 1)"
    };
    Ok(Value::Tuple(vec![Value::Number(r), Value::Text(verdict.into())]))
}

pub fn cauchy_sequence(a: &[Value]) -> R {
    // terms, eps
    let (t, eps) = (nums(&a[0])?, num(&a[1])?);
    for start in 0..t.len() {
        let tail = &t[start..];
        let hi = tail.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
        let lo = tail.iter().cloned().fold(f64::INFINITY, f64::min);
        if hi - lo < eps {
            return n(start as f64);
        }
    }
    Err("the terms never settle within eps".into())
}

// ---------------------------------------------------------------- interpolation, transforms
pub fn lagrange_interpolation(a: &[Value]) -> R {
    // xs, ys, x
    let (xs, ys, x) = (nums(&a[0])?, nums(&a[1])?, num(&a[2])?);
    let mut total = 0.0;
    for i in 0..xs.len() {
        let mut p = 1.0;
        for j in 0..xs.len() {
            if j != i {
                p *= div(x - xs[j], xs[i] - xs[j])?;
            }
        }
        total += at(&ys, i as i64)? * p;
    }
    n(total)
}

pub fn newton_interpolation(a: &[Value]) -> R {
    let (xs, ys, x) = (nums(&a[0])?, nums(&a[1])?, num(&a[2])?);
    let nn = xs.len();
    let mut coef = ys;
    for j in 1..nn {
        for i in (j..nn).rev() {
            let (ci, cp) = (at(&coef, i as i64)?, at(&coef, i as i64 - 1)?);
            coef[i] = div(ci - cp, xs[i] - xs[i - j])?;
        }
    }
    let mut result = at(&coef, -1)?;
    for i in (0..nn.saturating_sub(1)).rev() {
        result = result * (x - xs[i]) + at(&coef, i as i64)?;
    }
    n(result)
}

pub fn spline(a: &[Value]) -> R {
    let (xs, ys, x) = (nums(&a[0])?, nums(&a[1])?, num(&a[2])?);
    let nn = xs.len();
    let mut sorted = xs.clone();
    sorted.sort_by(|p, q| p.partial_cmp(q).unwrap_or(std::cmp::Ordering::Equal));
    need(nn >= 3 && sorted == xs, "give at least 3 increasing x values")?;
    let h: Vec<f64> = (0..nn - 1).map(|i| xs[i + 1] - xs[i]).collect();
    let mut m = vec![vec![0.0; nn + 1]; nn];
    m[0][0] = 1.0;
    m[nn - 1][nn - 1] = 1.0;
    for i in 1..nn - 1 {
        m[i][i - 1] = h[i - 1];
        m[i][i] = 2.0 * (h[i - 1] + h[i]);
        m[i][i + 1] = h[i];
        m[i][nn] = 3.0 * (div(at(&ys, i as i64 + 1)? - ys[i], h[i])? - div(ys[i] - ys[i - 1], h[i - 1])?);
    }
    let (r, _) = rref(&m)?;
    let c: Vec<f64> = (0..nn).map(|i| r[i][nn]).collect();
    need(xs[0] <= x && x <= xs[nn - 1], "x is outside the data")?;
    let i = (0..nn - 1).filter(|k| xs[*k] <= x).max().ok_or("x is outside the data")?;
    let dx = x - xs[i];
    let bb = div(at(&ys, i as i64 + 1)? - ys[i], h[i])? - h[i] * (2.0 * c[i] + c[i + 1]) / 3.0;
    let d = (c[i + 1] - c[i]) / (3.0 * h[i]);
    n(ys[i] + bb * dx + c[i] * dx.powi(2) + d * dx.powi(3))
}

pub fn convolution(a: &[Value]) -> R {
    let (f, g) = (nums(&a[0])?, nums(&a[1])?);
    if f.is_empty() && g.is_empty() {
        return Ok(vlist(vec![]));
    }
    let len = (f.len() + g.len()).saturating_sub(1);
    let mut out = vec![];
    for k in 0..len {
        let mut s = 0.0;
        for (j, fj) in f.iter().enumerate() {
            let d = k as i64 - j as i64;
            if 0 <= d && (d as usize) < g.len() {
                s += fj * g[d as usize];
            }
        }
        out.push(s);
    }
    Ok(vlist(out))
}

fn cplx(re: f64, im: f64) -> Value {
    Value::Complex(re, im)
}

pub fn discrete_fourier_transform(a: &[Value]) -> R {
    let x = nums(&a[0])?;
    let nn = x.len();
    let mut out = vec![];
    for k in 0..nn {
        let (mut re, mut im) = (0.0, 0.0);
        for (j, xj) in x.iter().enumerate() {
            let ang = -2.0 * PI * k as f64 * j as f64 / nn as f64;
            re += xj * ang.cos();
            im += xj * ang.sin();
        }
        out.push(cplx(re, im));
    }
    Ok(Value::List(out))
}

pub fn inverse_discrete_fourier_transform(a: &[Value]) -> R {
    // the input list may hold plain numbers (a complex spectrum cannot be typed in a box)
    let x = nums(&a[0])?;
    let nn = x.len();
    let mut out = vec![];
    for j in 0..nn {
        let (mut re, mut im) = (0.0, 0.0);
        for (k, xk) in x.iter().enumerate() {
            let ang = 2.0 * PI * k as f64 * j as f64 / nn as f64;
            re += xk * ang.cos();
            im += xk * ang.sin();
        }
        out.push(cplx(re / nn as f64, im / nn as f64));
    }
    Ok(Value::List(out))
}

pub fn z_transform(a: &[Value]) -> R {
    let (x, z) = (nums(&a[0])?, num(&a[1])?);
    let mut s = 0.0;
    for (k, xk) in x.iter().enumerate() {
        s += xk * pypow(z, -(k as f64))?;
    }
    n(s)
}

// ---------------------------------------------------------------- statistics
pub fn chi_square_statistic(a: &[Value]) -> R {
    let (o, e) = (nums(&a[0])?, nums(&a[1])?);
    let mut s = 0.0;
    for (p, q) in o.iter().zip(&e) {
        s += div((p - q).powi(2), *q)?;
    }
    n(s)
}

pub fn correlation(a: &[Value]) -> R {
    let (x, y) = (nums(&a[0])?, nums(&a[1])?);
    need(x.len() == y.len(), "correlation requires that both inputs have same number of data points")?;
    need(x.len() >= 2, "correlation requires at least two data points")?;
    let (xb, yb) = (st_mean(&x)?, st_mean(&y)?);
    let sxy: f64 = x.iter().zip(&y).map(|(p, q)| (p - xb) * (q - yb)).sum();
    let (sxx, syy) = (st_ss(&x)?, st_ss(&y)?);
    need(sxx != 0.0 && syy != 0.0, "at least one of the inputs is constant")?;
    n(sxy / (sxx * syy).sqrt())
}

pub fn covariance(a: &[Value]) -> R {
    let (x, y) = (nums(&a[0])?, nums(&a[1])?);
    need(x.len() == y.len(), "covariance requires that both inputs have same number of data points")?;
    need(x.len() >= 2, "covariance requires at least two data points")?;
    let (xb, yb) = (st_mean(&x)?, st_mean(&y)?);
    n(x.iter().zip(&y).map(|(p, q)| (p - xb) * (q - yb)).sum::<f64>() / (x.len() - 1) as f64)
}

pub fn expected_value(a: &[Value]) -> R {
    let (v, p) = (nums(&a[0])?, nums(&a[1])?);
    n(v.iter().zip(&p).map(|(x, q)| x * q).sum())
}

pub fn list_maximum(a: &[Value]) -> R {
    let d = nums(&a[0])?;
    need(!d.is_empty(), "max() of an empty list")?;
    n(d.iter().cloned().fold(f64::NEG_INFINITY, f64::max))
}

pub fn list_minimum(a: &[Value]) -> R {
    let d = nums(&a[0])?;
    need(!d.is_empty(), "min() of an empty list")?;
    n(d.iter().cloned().fold(f64::INFINITY, f64::min))
}

pub fn third_quartile(a: &[Value]) -> R {
    let q = st_quantiles(&nums(&a[0])?, 4)?;
    n(q[2])
}

pub fn first_quartile(a: &[Value]) -> R {
    let q = st_quantiles(&nums(&a[0])?, 4)?;
    n(q[0])
}

pub fn expected_square(a: &[Value]) -> R {
    let (v, p) = (nums(&a[0])?, nums(&a[1])?);
    n(v.iter().zip(&p).map(|(x, q)| x * x * q).sum())
}

pub fn variance_of_random_variable(a: &[Value]) -> R {
    let (v, p) = (nums(&a[0])?, nums(&a[1])?);
    let ex2: f64 = v.iter().zip(&p).map(|(x, q)| x * x * q).sum();
    let ex: f64 = v.iter().zip(&p).map(|(x, q)| x * q).sum();
    n(ex2 - ex.powi(2))
}

pub fn interquartile_range(a: &[Value]) -> R {
    let q = st_quantiles(&nums(&a[0])?, 4)?;
    n(q[2] - q[0])
}

pub fn percentile(a: &[Value]) -> R {
    // data, k
    let (d, k) = (nums(&a[0])?, whole(num(&a[1])?)?);
    let q = st_quantiles(&d, 100)?;
    n(at(&q, k - 1)?)
}

pub fn quartiles(a: &[Value]) -> R {
    Ok(vlist(st_quantiles(&nums(&a[0])?, 4)?))
}

pub fn linear_regression(a: &[Value]) -> R {
    let (s, i) = st_regression(&nums(&a[0])?, &nums(&a[1])?)?;
    Ok(vtuple(vec![s, i]))
}

pub fn least_squares(a: &[Value]) -> R {
    linear_regression(a)
}

pub fn mean(a: &[Value]) -> R {
    n(st_mean(&nums(&a[0])?)?)
}

pub fn median(a: &[Value]) -> R {
    let mut d = nums(&a[0])?;
    need(!d.is_empty(), "no median for empty data")?;
    d.sort_by(|p, q| p.partial_cmp(q).unwrap_or(std::cmp::Ordering::Equal));
    let m = d.len();
    n(if m % 2 == 1 { d[m / 2] } else { (d[m / 2 - 1] + d[m / 2]) / 2.0 })
}

pub fn mode(a: &[Value]) -> R {
    let d = nums(&a[0])?;
    need(!d.is_empty(), "no mode for empty data")?;
    let mut counts: Vec<(f64, usize)> = vec![];
    for x in &d {
        match counts.iter_mut().find(|(v, _)| v == x) {
            Some(slot) => slot.1 += 1,
            None => counts.push((*x, 1)),
        }
    }
    let mut best = counts[0];
    for c in &counts[1..] {
        if c.1 > best.1 {
            best = *c;
        }
    }
    n(best.0)
}

pub fn range(a: &[Value]) -> R {
    let d = nums(&a[0])?;
    need(!d.is_empty(), "max() of an empty list")?;
    n(d.iter().cloned().fold(f64::NEG_INFINITY, f64::max) - d.iter().cloned().fold(f64::INFINITY, f64::min))
}

pub fn sample_variance(a: &[Value]) -> R {
    let d = nums(&a[0])?;
    need(d.len() >= 2, "variance requires at least two data points")?;
    n(st_ss(&d)? / (d.len() - 1) as f64)
}

pub fn sample_standard_deviation(a: &[Value]) -> R {
    let d = nums(&a[0])?;
    need(d.len() >= 2, "stdev requires at least two data points")?;
    n((st_ss(&d)? / (d.len() - 1) as f64).sqrt())
}

pub fn variance(a: &[Value]) -> R {
    let d = nums(&a[0])?;
    need(!d.is_empty(), "pvariance requires at least one data point")?;
    n(st_ss(&d)? / d.len() as f64)
}

pub fn standard_deviation(a: &[Value]) -> R {
    let d = nums(&a[0])?;
    need(!d.is_empty(), "pstdev requires at least one data point")?;
    n((st_ss(&d)? / d.len() as f64).sqrt())
}

// ---------------------------------------------------------------- circuits
pub fn resistors_in_parallel(a: &[Value]) -> R {
    let r = nums(&a[0])?;
    let mut s = 0.0;
    for x in &r {
        s += div(1.0, *x)?;
    }
    n(div(1.0, s)?)
}

pub fn resistors_in_series(a: &[Value]) -> R {
    n(nums(&a[0])?.iter().sum())
}
