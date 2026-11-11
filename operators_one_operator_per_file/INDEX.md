# Operator index

One folder per operator, holding `<name>.py` (formula + `compute()`) and `<name>.jpg` (diagram drawn with small square boxes).
**Ready** = `compute()` works today; **Reference** = formula/definition only.


## Math / Arithmetic

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Addition | + | a + b | Ready | `math/arithmetic/addition/` |
| Subtraction | − | a − b | Ready | `math/arithmetic/subtraction/` |
| Multiplication | × | a × b | Ready | `math/arithmetic/multiplication/` |
| Division | ÷ | a ÷ b | Ready | `math/arithmetic/division/` |
| Modulo | % | a mod b = a − b·⌊a/b⌋  (remainder of a ÷ b) | Ready | `math/arithmetic/modulo/` |
| Fraction | a/b | numerator / denominator | Ready | `math/arithmetic/fraction/` |
| Absolute value | \|x\| | \|x\| = x if x ≥ 0, otherwise −x | Ready | `math/arithmetic/absolute_value/` |
| Negate | ± | −x  (flip the sign) | Ready | `math/arithmetic/negate/` |
| Reciprocal | 1/x | 1/x | Ready | `math/arithmetic/reciprocal/` |
| Round down | floor | ⌊x⌋ = greatest integer ≤ x | Ready | `math/arithmetic/round_down/` |
| Round up | ceil | ⌈x⌉ = smallest integer ≥ x | Ready | `math/arithmetic/round_up/` |
| Round nearest | round | round(x) = nearest integer to x | Ready | `math/arithmetic/round_nearest/` |
| Minimum | min | min(a, b, …) = smallest value | Ready | `math/arithmetic/minimum/` |
| Maximum | max | max(a, b, …) = largest value | Ready | `math/arithmetic/maximum/` |

## Math / Algebra

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Power | ^ | aᵇ | Ready | `math/algebra/power/` |
| Square | x² | x² = x · x | Ready | `math/algebra/square/` |
| Cube | x³ | x³ = x · x · x | Ready | `math/algebra/cube/` |
| Square root | √ | √x  (y such that y² = x) | Ready | `math/algebra/square_root/` |
| Nth root | ⁿ√ | ⁿ√x = x^(1/n) | Ready | `math/algebra/nth_root/` |
| Cube root | ∛ | ∛x  (y such that y³ = x) | Ready | `math/algebra/cube_root/` |
| Exponential | eˣ | eˣ | Ready | `math/algebra/exponential/` |
| Power of ten | 10ˣ | 10ˣ | Ready | `math/algebra/power_of_ten/` |
| Log base 10 | log | log₁₀(x) | Ready | `math/algebra/log_base_10/` |
| Natural log | ln | ln(x) = logₑ(x) | Ready | `math/algebra/natural_log/` |
| Log any base | logₐ | logₐ(x) = ln(x) / ln(a) | Ready | `math/algebra/log_any_base/` |
| Quadratic formula | ax²+bx+c=0 | x = (−b ± √(b² − 4ac)) / 2a | Ready | `math/algebra/quadratic_formula/` |
| Discriminant | Δ | Δ = b² − 4ac  (>0: two real roots, 0: one, <0: complex) | Ready | `math/algebra/discriminant/` |
| Factor | factor | Rewrite a polynomial as a product of lower-degree polynomials, e.g. x² − 1 = (x − 1)(x + 1) | Ready | `math/algebra/factor/` |
| Expand | expand | Multiply out products, e.g. (x + 1)(x − 1) = x² − 1 | Ready | `math/algebra/expand/` |
| Simplify | simplify | Rewrite an expression in an equivalent, shorter or standard form | Ready | `math/algebra/simplify/` |
| Solve for x | solve | Find the value(s) of x that make an equation true | Ready | `math/algebra/solve_for_x/` |
| Solve system of equations | system | Find values satisfying several equations at once; for linear systems solve Ax = b | Ready | `math/algebra/solve_system_of_equations/` |
| Binomial theorem | (a+b)ⁿ | (a + b)ⁿ = Σₖ C(n,k) · aⁿ⁻ᵏ · bᵏ | Ready | `math/algebra/binomial_theorem/` |
| Difference of squares | a²−b² | a² − b² = (a − b)(a + b)  (returns the two factors) | Ready | `math/algebra/difference_of_squares/` |
| Slope-intercept form | y = mx + b | y = m·x + b | Ready | `math/algebra/slope_intercept_form/` |
| Arithmetic sequence | aₙ | aₙ = a₁ + (n − 1)d | Ready | `math/algebra/arithmetic_sequence/` |
| Geometric sequence | aₙ | aₙ = a₁ · rⁿ⁻¹ | Ready | `math/algebra/geometric_sequence/` |
| Arithmetic series sum | Sₙ | Sₙ = n/2 · (2a₁ + (n − 1)d) | Ready | `math/algebra/arithmetic_series_sum/` |
| Geometric series sum | Sₙ | Sₙ = a₁(1 − rⁿ) / (1 − r)   (r ≠ 1) | Ready | `math/algebra/geometric_series_sum/` |
| Complex number | a + bi | z = a + bi | Ready | `math/algebra/complex_number/` |
| Imaginary unit | i | i² = −1 | Ready | `math/algebra/imaginary_unit/` |
| Modulus of complex number | \|z\| | \|a + bi\| = √(a² + b²) | Ready | `math/algebra/modulus_of_complex_number/` |
| Complex conjugate | z̄ | conj(a + bi) = a − bi | Ready | `math/algebra/complex_conjugate/` |

## Math / Trigonometry

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Sine | sin | sin θ = opposite / hypotenuse   (θ in radians) | Ready | `math/trigonometry/sine/` |
| Cosine | cos | cos θ = adjacent / hypotenuse   (θ in radians) | Ready | `math/trigonometry/cosine/` |
| Tangent | tan | tan θ = sin θ / cos θ | Ready | `math/trigonometry/tangent/` |
| Cosecant | csc | csc θ = 1 / sin θ | Ready | `math/trigonometry/cosecant/` |
| Secant | sec | sec θ = 1 / cos θ | Ready | `math/trigonometry/secant/` |
| Cotangent | cot | cot θ = cos θ / sin θ | Ready | `math/trigonometry/cotangent/` |
| Inverse sine | asin | θ = arcsin(x),  −1 ≤ x ≤ 1 | Ready | `math/trigonometry/inverse_sine/` |
| Inverse cosine | acos | θ = arccos(x),  −1 ≤ x ≤ 1 | Ready | `math/trigonometry/inverse_cosine/` |
| Inverse tangent | atan | θ = arctan(x) | Ready | `math/trigonometry/inverse_tangent/` |
| Two-argument arctangent | atan2 | atan2(y, x) = angle of the point (x, y) from the +x axis | Ready | `math/trigonometry/two_argument_arctangent/` |
| Hyperbolic sine | sinh | sinh x = (eˣ − e⁻ˣ) / 2 | Ready | `math/trigonometry/hyperbolic_sine/` |
| Hyperbolic cosine | cosh | cosh x = (eˣ + e⁻ˣ) / 2 | Ready | `math/trigonometry/hyperbolic_cosine/` |
| Hyperbolic tangent | tanh | tanh x = sinh x / cosh x | Ready | `math/trigonometry/hyperbolic_tangent/` |
| Inverse hyperbolic sine | asinh | asinh x = ln(x + √(x² + 1)) | Ready | `math/trigonometry/inverse_hyperbolic_sine/` |
| Inverse hyperbolic cosine | acosh | acosh x = ln(x + √(x² − 1)),  x ≥ 1 | Ready | `math/trigonometry/inverse_hyperbolic_cosine/` |
| Inverse hyperbolic tangent | atanh | atanh x = ½ ln((1 + x)/(1 − x)),  \|x\| < 1 | Ready | `math/trigonometry/inverse_hyperbolic_tangent/` |
| Pythagorean identity | sin²θ+cos²θ=1 | sin²θ + cos²θ = 1  (function returns the left side, always 1) | Ready | `math/trigonometry/pythagorean_identity/` |
| Double angle | sin 2θ | sin 2θ = 2 sin θ cos θ | Ready | `math/trigonometry/double_angle/` |
| Half angle | sin θ/2 | sin(θ/2) = √((1 − cos θ) / 2)   (for θ/2 in the first two quadrants) | Ready | `math/trigonometry/half_angle/` |
| Angle sum | sin(a+b) | sin(a + b) = sin a cos b + cos a sin b | Ready | `math/trigonometry/angle_sum/` |
| Degrees to radians | deg→rad | radians = degrees × π / 180 | Ready | `math/trigonometry/degrees_to_radians/` |
| Radians to degrees | rad→deg | degrees = radians × 180 / π | Ready | `math/trigonometry/radians_to_degrees/` |

## Math / Calculus

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Limit | lim | lim_{x→a} f(x) = L  means f(x) gets arbitrarily close to L as x gets close to a | Ready | `math/calculus/limit/` |
| Derivative | d/dx | f′(x) = lim_{h→0} (f(x+h) − f(x−h)) / 2h   (numerical central difference) | Ready | `math/calculus/derivative/` |
| Partial derivative | ∂/∂x | ∂f/∂xᵢ ≈ (f(…xᵢ+h…) − f(…xᵢ−h…)) / 2h   (point is a list, i is the variable index) | Ready | `math/calculus/partial_derivative/` |
| Second partial derivative | ∂²/∂x² | ∂²f/∂xᵢ² ≈ (f(…xᵢ+h…) − 2f(…) + f(…xᵢ−h…)) / h²   (point is a list, i is the variable index) | Ready | `math/calculus/second_partial_derivative/` |
| Second derivative | d²/dx² | f″(x) ≈ (f(x+h) − 2f(x) + f(x−h)) / h² | Ready | `math/calculus/second_derivative/` |
| Indefinite integral | ∫ | ∫ f(x) dx = F(x) + C   where F′(x) = f(x) | Ready | `math/calculus/indefinite_integral/` |
| Definite integral | ∫ₐᵇ | ∫ₐᵇ f(x) dx   (numerical: Simpson's rule with n subintervals) | Ready | `math/calculus/definite_integral/` |
| Double integral | ∬ | ∬_R f(x, y) dA = ∫∫ f(x, y) dy dx over a region R | Ready | `math/calculus/double_integral/` |
| Triple integral | ∭ | ∭_V f(x, y, z) dV = ∫∫∫ f(x, y, z) dz dy dx over a volume V | Ready | `math/calculus/triple_integral/` |
| Line integral | ∮ | ∮_C F · dr = ∫ₐᵇ F(r(t)) · r′(t) dt   (∮ when C is a closed curve) | Ready | `math/calculus/line_integral/` |
| Gradient | ∇ | ∇f = (∂f/∂x₁, …, ∂f/∂xₙ)   (numerical) | Ready | `math/calculus/gradient/` |
| Divergence | ∇· | ∇·F = ∂Fx/∂x + ∂Fy/∂y + ∂Fz/∂z | Ready | `math/calculus/divergence/` |
| Curl | ∇× | ∇×F = (∂Fz/∂y − ∂Fy/∂z, ∂Fx/∂z − ∂Fz/∂x, ∂Fy/∂x − ∂Fx/∂y) | Ready | `math/calculus/curl/` |
| Laplacian | Δ | Δf = ∂²f/∂x² + ∂²f/∂y² + ∂²f/∂z² | Ready | `math/calculus/laplacian/` |
| Chain rule | (f∘g)′ | (f∘g)′(x) = f′(g(x)) · g′(x) | Ready | `math/calculus/chain_rule/` |
| Product rule | (fg)′ | (f·g)′ = f′g + fg′ | Ready | `math/calculus/product_rule/` |
| Quotient rule | (f/g)′ | (f/g)′ = (f′g − fg′) / g² | Ready | `math/calculus/quotient_rule/` |
| L'Hopital's rule | L'H | If lim f/g is 0/0 or ∞/∞ then lim f/g = lim f′/g′  (when that limit exists) | Ready | `math/calculus/l_hopital_s_rule/` |
| Taylor series | Σ f⁽ⁿ⁾(a)/n! | f(x) ≈ Σₙ f⁽ⁿ⁾(a)/n! · (x − a)ⁿ   (derivs = [f(a), f′(a), f″(a), …]) | Ready | `math/calculus/taylor_series/` |
| Maclaurin series | Σ f⁽ⁿ⁾(0)/n! | f(x) ≈ Σₙ f⁽ⁿ⁾(0)/n! · xⁿ   (Taylor series about 0) | Ready | `math/calculus/maclaurin_series/` |
| Summation | Σ | Σ aᵢ = a₁ + a₂ + … + aₙ | Ready | `math/calculus/summation/` |
| Product | ∏ | ∏ aᵢ = a₁ · a₂ · … · aₙ | Ready | `math/calculus/product/` |
| Infinity | ∞ | ∞ = value larger than any real number | Ready | `math/calculus/infinity/` |
| Differential equation | dy/dx = f(x,y) | An equation relating a function to its derivatives; see the Euler / Runge–Kutta operators to solve numerically | Ready | `math/calculus/differential_equation/` |

## Math / Linear algebra

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Matrix add | A + B | (A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ | Ready | `math/linear_algebra/matrix_add/` |
| Matrix subtract | A − B | (A − B)ᵢⱼ = Aᵢⱼ − Bᵢⱼ | Ready | `math/linear_algebra/matrix_subtract/` |
| Matrix multiply | A·B | (AB)ᵢⱼ = Σₖ Aᵢₖ · Bₖⱼ | Ready | `math/linear_algebra/matrix_multiply/` |
| Scalar multiply | kA | (kA)ᵢⱼ = k · Aᵢⱼ | Ready | `math/linear_algebra/scalar_multiply/` |
| Transpose | Aᵀ | (Aᵀ)ᵢⱼ = Aⱼᵢ | Ready | `math/linear_algebra/transpose/` |
| Determinant | det(A) | det(A) = Σⱼ (−1)ʲ · A₀ⱼ · det(minor₀ⱼ)   (cofactor expansion along row 0) | Ready | `math/linear_algebra/determinant/` |
| Matrix inverse | A⁻¹ | A·A⁻¹ = I   (Gauss–Jordan elimination) | Ready | `math/linear_algebra/matrix_inverse/` |
| Trace | tr(A) | tr(A) = Σᵢ Aᵢᵢ  (sum of the diagonal) | Ready | `math/linear_algebra/trace/` |
| Matrix rank | rank(A) | rank(A) = number of linearly independent rows (pivots after elimination) | Ready | `math/linear_algebra/matrix_rank/` |
| Identity matrix | I | Iᵢⱼ = 1 if i = j else 0 | Ready | `math/linear_algebra/identity_matrix/` |
| Row reduce (RREF) | RREF | Reduced row echelon form via Gauss–Jordan elimination | Ready | `math/linear_algebra/row_reduce_rref/` |
| Eigenvalues | λ | det(A − λI) = 0   (closed form for a 2×2 matrix: λ = (tr ± √(tr² − 4·det)) / 2) | Ready | `math/linear_algebra/eigenvalues/` |
| Eigenvectors | v | A·v = λ·v  — solve (A − λI)v = 0 for v ≠ 0 for each eigenvalue λ | Ready | `math/linear_algebra/eigenvectors/` |
| Characteristic polynomial | p(λ) | p(λ) = det(A − λI);  for 2×2: λ² − tr(A)·λ + det(A)  (returns [1, −tr, det]) | Ready | `math/linear_algebra/characteristic_polynomial/` |
| Dot product | a·b | a·b = Σ aᵢbᵢ = \|a\|\|b\|cos θ | Ready | `math/linear_algebra/dot_product/` |
| Cross product | a×b | a × b = (a₂b₃ − a₃b₂, a₃b₁ − a₁b₃, a₁b₂ − a₂b₁)   (3D vectors) | Ready | `math/linear_algebra/cross_product/` |
| Vector magnitude | ‖v‖ | ‖v‖ = √(v₁² + v₂² + …) | Ready | `math/linear_algebra/vector_magnitude/` |
| Unit vector | v̂ | v̂ = v / ‖v‖ | Ready | `math/linear_algebra/unit_vector/` |
| Vector projection | proj_b a | proj_b(a) = (a·b / b·b) · b | Ready | `math/linear_algebra/vector_projection/` |
| Quaternion multiply | q₁ q₂ | Hamilton product of two quaternions (w, x, y, z), the second turn done first | Ready | `math/linear_algebra/quaternion_multiply/` |
| Quaternion conjugate | q* | q* = w − x i − y j − z k | Ready | `math/linear_algebra/quaternion_conjugate/` |
| Quaternion inverse | q⁻¹ | q⁻¹ = q* / (w² + x² + y² + z²) | Ready | `math/linear_algebra/quaternion_inverse/` |
| Quaternion normalise | q̂ | q̂ = q / √(w² + x² + y² + z²) | Ready | `math/linear_algebra/quaternion_normalize/` |
| Quaternion from axis and angle | axis θ | q = cos(θ/2) + sin(θ/2) · (the unit axis) | Ready | `math/linear_algebra/quaternion_from_axis_angle/` |
| Rotate a vector | q v q⁻¹ | v turned by q: q v q⁻¹ (the axes stay fixed; a q that is not unit length is allowed) | Ready | `math/linear_algebra/rotate_vector_by_quaternion/` |
| Quaternion to yaw, pitch and roll | q → yaw pitch roll | yaw = atan2(2(wz + xy), 1 − 2(y² + z²)),  pitch = asin(2(wy − zx)),  roll = atan2(2(wx + yz), 1 − 2(x² + y²))  (q normalised first) | Ready | `math/linear_algebra/quaternion_to_yaw_pitch_roll/` |
| Yaw, pitch and roll to quaternion | yaw pitch roll → q | q = q_yaw q_pitch q_roll, with q_roll = [cos(r/2), sin(r/2), 0, 0], q_pitch = [cos(p/2), 0, sin(p/2), 0], q_yaw = [cos(y/2), 0, 0, sin(y/2)] | Ready | `math/linear_algebra/quaternion_from_yaw_pitch_roll/` |
| Rotation matrix from a quaternion | R(q) | R(q) from the normalised quaternion (w, x, y, z): [1 − 2(y² + z²), 2(xy − zw), 2(xz + yw)], [2(xy + zw), 1 − 2(x² + z²), 2(yz − xw)], [2(xz − yw), 2(yz + xw), 1 − 2(x² + y²)] | Ready | `math/linear_algebra/rotation_matrix_from_quaternion/` |
| Rotation matrix from axis and angle | R(axis, θ) | the quaternion cos(θ/2) + sin(θ/2) · (the unit axis), then R(q); the axis is normalised first, the angle is in radians | Ready | `math/linear_algebra/rotation_matrix_from_axis_angle/` |
| Rotation matrix from yaw, pitch and roll | R(yaw, pitch, roll) | the quaternion q_yaw q_pitch q_roll, then R(q) | Ready | `math/linear_algebra/rotation_matrix_from_yaw_pitch_roll/` |
| Rotate a vector by a matrix | R v | R v: the three rows of R times v | Ready | `math/linear_algebra/rotate_vector_by_matrix/` |
| Quaternion blend | slerp | slerp(q₀, q₁, t) = (sin((1 − t)ω) q₀ + sin(tω) q₁) / sin ω, ω = acos(q₀ · q₁); the short way round (q and −q are the same turn) | Ready | `math/linear_algebra/quaternion_slerp/` |
| Angle between two orientations | ∠(q₀, q₁) | ∠ = 2 acos(|q₀ · q₁|) with both quaternions normalised (q and −q are the same orientation), from 0 to π radians | Ready | `math/linear_algebra/angle_between_quaternions/` |
| Quaternion from a rotation matrix | q(R) | Shepperd's method: the largest of w, x, y, z is found first; the answer has w ≥ 0 | Ready | `math/linear_algebra/rotation_matrix_to_quaternion/` |
| Norm | ‖v‖ₚ | ‖v‖ₚ = (Σ \|vᵢ\|ᵖ)^(1/p) | Ready | `math/linear_algebra/norm/` |
| Null space | null(A) | null(A) = { x : A·x = 0 } | Ready | `math/linear_algebra/null_space/` |
| Column space | col(A) | col(A) = span of the columns of A = { A·x : x } | Ready | `math/linear_algebra/column_space/` |
| LU decomposition | A = LU | A = L·U with L lower-triangular and U upper-triangular | Ready | `math/linear_algebra/lu_decomposition/` |
| QR decomposition | A = QR | A = Q·R with Q orthogonal (QᵀQ = I) and R upper-triangular | Ready | `math/linear_algebra/qr_decomposition/` |
| Singular value decomposition | SVD | A = U·Σ·Vᵀ with U, V orthogonal and Σ diagonal of singular values | Ready | `math/linear_algebra/singular_value_decomposition/` |
| Solve Ax = b | Ax = b | Solve the linear system A·x = b  (Gaussian elimination with partial pivoting) | Ready | `math/linear_algebra/solve_ax_b/` |

## Math / Statistics and probability

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Mean | x̄ | mean = Σxᵢ / n | Ready | `math/statistics_and_probability/mean/` |
| Median | median | middle value of the sorted data (average of the two middle values if n is even) | Ready | `math/statistics_and_probability/median/` |
| Mode | mode | most frequent value | Ready | `math/statistics_and_probability/mode/` |
| Range | range | range = max − min | Ready | `math/statistics_and_probability/range/` |
| Maximum of a list | max | max of the list | Ready | `math/statistics_and_probability/list_maximum/` |
| Minimum of a list | min | min of the list | Ready | `math/statistics_and_probability/list_minimum/` |
| Range: from the ends | range = max − min | range = max − min   (max is the answer of Row 1, min the answer of Row 2) | Ready | `math/statistics_and_probability/range_from_ends/` |
| Variance | σ² | σ² = Σ(xᵢ − μ)² / n   (population) | Ready | `math/statistics_and_probability/variance/` |
| Standard deviation | σ | σ = √(σ²)   (population) | Ready | `math/statistics_and_probability/standard_deviation/` |
| Standard deviation: from the variance | σ = √(σ²) | σ = √(σ²)   (σ² is the answer of the row above) | Ready | `math/statistics_and_probability/standard_deviation_from_variance/` |
| Sample variance | s² | s² = Σ(xᵢ − x̄)² / (n − 1) | Ready | `math/statistics_and_probability/sample_variance/` |
| Sample standard deviation | s | s = √(s²) | Ready | `math/statistics_and_probability/sample_standard_deviation/` |
| Sample standard deviation: from the sample variance | s = √(s²) | s = √(s²)   (s² is the answer of the row above) | Ready | `math/statistics_and_probability/sample_standard_deviation_from_variance/` |
| Z-score | z | z = (x − μ) / σ | Ready | `math/statistics_and_probability/z_score/` |
| Covariance | cov(X,Y) | cov(X,Y) = Σ(xᵢ − x̄)(yᵢ − ȳ) / (n − 1) | Ready | `math/statistics_and_probability/covariance/` |
| Correlation | r | r = cov(X,Y) / (sₓ · s_y) | Ready | `math/statistics_and_probability/correlation/` |
| Linear regression | y = mx + b | least-squares line; returns (slope, intercept) | Ready | `math/statistics_and_probability/linear_regression/` |
| Quartiles | Q1 Q2 Q3 | values that split sorted data into four equal parts | Ready | `math/statistics_and_probability/quartiles/` |
| Interquartile range | IQR | IQR = Q3 − Q1 | Ready | `math/statistics_and_probability/interquartile_range/` |
| Third quartile | Q3 | Q3, the 75th percentile (quantiles of the list in four parts, the third cut) | Ready | `math/statistics_and_probability/third_quartile/` |
| First quartile | Q1 | Q1, the 25th percentile (quantiles of the list in four parts, the first cut) | Ready | `math/statistics_and_probability/first_quartile/` |
| Interquartile range: from the quartiles | IQR = Q3 − Q1 | IQR = Q3 − Q1   (Q3 is the answer of Row 1, Q1 the answer of Row 2) | Ready | `math/statistics_and_probability/interquartile_range_from_quartiles/` |
| Percentile | Pₖ | value below which k percent of the data fall (k = 1 … 99) | Ready | `math/statistics_and_probability/percentile/` |
| Probability | P(A) | P(A) = favorable outcomes / total outcomes | Ready | `math/statistics_and_probability/probability/` |
| Conditional probability | P(A\|B) | P(A\|B) = P(A ∩ B) / P(B) | Ready | `math/statistics_and_probability/conditional_probability/` |
| Bayes' theorem | P(A\|B) | P(A\|B) = P(B\|A) · P(A) / P(B) | Ready | `math/statistics_and_probability/bayes_theorem/` |
| Expected value | E[X] | E[X] = Σ xᵢ · pᵢ | Ready | `math/statistics_and_probability/expected_value/` |
| Variance of random variable | Var(X) | Var(X) = E[X²] − (E[X])² | Ready | `math/statistics_and_probability/variance_of_random_variable/` |
| Expected square | E[X²] | E[X²] = Σ xᵢ² · pᵢ | Ready | `math/statistics_and_probability/expected_square/` |
| Variance: from the expectations | Var = E[X²] − (E[X])² | Var = E[X²] − (E[X])²   (E[X²] is the answer of Row 2, E[X] the answer of Row 1) | Ready | `math/statistics_and_probability/variance_from_expectations/` |
| Normal distribution | N(μ, σ²) | f(x) = e^(−(x−μ)² / 2σ²) / (σ√(2π))   (probability density) | Ready | `math/statistics_and_probability/normal_distribution/` |
| Binomial distribution | B(n, p) | P(X = k) = C(n,k) · pᵏ · (1−p)ⁿ⁻ᵏ | Ready | `math/statistics_and_probability/binomial_distribution/` |
| Poisson distribution | Pois(λ) | P(X = k) = λᵏ · e^(−λ) / k! | Ready | `math/statistics_and_probability/poisson_distribution/` |
| Uniform distribution | U(a, b) | f(x) = 1 / (b − a) for a ≤ x ≤ b, else 0 | Ready | `math/statistics_and_probability/uniform_distribution/` |
| Exponential distribution | Exp(λ) | f(x) = λ · e^(−λx) for x ≥ 0 | Ready | `math/statistics_and_probability/exponential_distribution/` |
| Confidence interval | CI | x̄ ± z · s / √n   (z = 1.96 for 95%) | Ready | `math/statistics_and_probability/confidence_interval/` |
| t-test statistic | t | t = (x̄ − μ₀) / (s / √n)   (one-sample) | Ready | `math/statistics_and_probability/t_test_statistic/` |
| Chi-square statistic | χ² | χ² = Σ (Oᵢ − Eᵢ)² / Eᵢ | Ready | `math/statistics_and_probability/chi_square_statistic/` |
| p-value | p | probability, assuming the null hypothesis is true, of a result at least as extreme as the one observed | Ready | `math/statistics_and_probability/p_value/` |

## Math / Discrete and number theory

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Factorial | n! | n! = n · (n−1) · … · 2 · 1 | Ready | `math/discrete_and_number_theory/factorial/` |
| Combinations | nCr | C(n, r) = n! / (r! (n − r)!) | Ready | `math/discrete_and_number_theory/combinations/` |
| Permutations | nPr | P(n, r) = n! / (n − r)! | Ready | `math/discrete_and_number_theory/permutations/` |
| Greatest common divisor | gcd | largest integer dividing both a and b | Ready | `math/discrete_and_number_theory/greatest_common_divisor/` |
| Least common multiple | lcm | lcm(a, b) = \|a·b\| / gcd(a, b) | Ready | `math/discrete_and_number_theory/least_common_multiple/` |
| Modular arithmetic | a mod m | a ≡ r (mod m) where r = a − m·⌊a/m⌋ | Ready | `math/discrete_and_number_theory/modular_arithmetic/` |
| Prime check | prime? | n is prime if n > 1 and has no divisor other than 1 and n | Ready | `math/discrete_and_number_theory/prime_check/` |
| Prime factorization | n = p₁·p₂·… | every integer > 1 is a product of primes | Ready | `math/discrete_and_number_theory/prime_factorization/` |
| Fibonacci | Fₙ | F₀ = 0, F₁ = 1, Fₙ = Fₙ₋₁ + Fₙ₋₂ | Ready | `math/discrete_and_number_theory/fibonacci/` |
| Euler's totient | φ(n) | φ(n) = number of integers in 1…n that are coprime to n = n · ∏(1 − 1/p) | Ready | `math/discrete_and_number_theory/euler_s_totient/` |
| Pigeonhole principle | ⌈n/m⌉ | Putting n items in m boxes forces some box to hold at least ⌈n/m⌉ items | Ready | `math/discrete_and_number_theory/pigeonhole_principle/` |
| Inclusion-exclusion | \|A∪B\| | \|A ∪ B\| = \|A\| + \|B\| − \|A ∩ B\| | Ready | `math/discrete_and_number_theory/inclusion_exclusion/` |

## Math / Logic and sets

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| AND | ∧ | A ∧ B is true only when both are true | Ready | `math/logic_and_sets/and/` |
| OR | ∨ | A ∨ B is true when at least one is true | Ready | `math/logic_and_sets/or/` |
| NOT | ¬ | ¬A is true when A is false | Ready | `math/logic_and_sets/not/` |
| XOR | ⊕ | A ⊕ B is true when exactly one is true | Ready | `math/logic_and_sets/xor/` |
| Implies | → | A → B is false only when A is true and B is false  (¬A ∨ B) | Ready | `math/logic_and_sets/implies/` |
| If and only if | ↔ | A ↔ B is true when A and B have the same truth value | Ready | `math/logic_and_sets/if_and_only_if/` |
| For all | ∀ | ∀x ∈ D: P(x)  — P holds for every x in D | Ready | `math/logic_and_sets/for_all/` |
| There exists | ∃ | ∃x ∈ D: P(x)  — P holds for at least one x in D | Ready | `math/logic_and_sets/there_exists/` |
| Element of | ∈ | x ∈ S  — x is a member of S | Ready | `math/logic_and_sets/element_of/` |
| Not element of | ∉ | x ∉ S  — x is not a member of S | Ready | `math/logic_and_sets/not_element_of/` |
| Proper subset | ⊂ | A ⊂ B  — every element of A is in B and A ≠ B | Ready | `math/logic_and_sets/proper_subset/` |
| Subset or equal | ⊆ | A ⊆ B  — every element of A is in B | Ready | `math/logic_and_sets/subset_or_equal/` |
| Union | ∪ | A ∪ B = elements in A or B (or both) | Ready | `math/logic_and_sets/union/` |
| Intersection | ∩ | A ∩ B = elements in both A and B | Ready | `math/logic_and_sets/intersection/` |
| Empty set | ∅ | ∅ = the set with no elements | Ready | `math/logic_and_sets/empty_set/` |
| Set difference | A − B | A − B = elements of A that are not in B | Ready | `math/logic_and_sets/set_difference/` |
| Complement | Aᶜ | Aᶜ = elements of the universal set U not in A | Ready | `math/logic_and_sets/complement/` |
| Cardinality | \|A\| | \|A\| = number of elements in A | Ready | `math/logic_and_sets/cardinality/` |

## Math / Abstract algebra

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Group | (G, ∘) | A set G with an operation ∘ that is closed, associative, has an identity e, and every element has an inverse | Ready | `math/abstract_algebra/group/` |
| Subgroup | H ≤ G | A subset H of G that is itself a group under the same operation | Ready | `math/abstract_algebra/subgroup/` |
| Normal subgroup | N ◁ G | A subgroup N with gNg⁻¹ = N for every g in G | Ready | `math/abstract_algebra/normal_subgroup/` |
| Quotient group order | G/N | \|G/N\| = \|G\| / \|N\| | Ready | `math/abstract_algebra/quotient_group_order/` |
| Order of group | \|G\| | \|G\| = number of elements of G | Ready | `math/abstract_algebra/order_of_group/` |
| Order of element | ord(g) | smallest k > 0 with gᵏ = e   (op = the group operation) | Ready | `math/abstract_algebra/order_of_element/` |
| Cyclic group | ⟨g⟩ | A group generated by a single element g: {…, g⁻¹, e, g, g², …} | Ready | `math/abstract_algebra/cyclic_group/` |
| Coset | gH | gH = { g∘h : h ∈ H } | Ready | `math/abstract_algebra/coset/` |
| Homomorphism | φ: G → H | A map with φ(a∘b) = φ(a)∘φ(b) | Ready | `math/abstract_algebra/homomorphism/` |
| Isomorphism | ≅ | A bijective homomorphism; G ≅ H means G and H have the same structure | Ready | `math/abstract_algebra/isomorphism/` |
| Kernel | ker φ | ker φ = { g ∈ G : φ(g) = e_H } | Ready | `math/abstract_algebra/kernel/` |
| Image | im φ | im φ = { φ(g) : g ∈ G } | Ready | `math/abstract_algebra/image/` |
| Direct product | G × H | G × H = { (g, h) : g ∈ G, h ∈ H } | Ready | `math/abstract_algebra/direct_product/` |
| Symmetric group order | Sₙ | \|Sₙ\| = n!   (all permutations of n objects) | Ready | `math/abstract_algebra/symmetric_group_order/` |
| Alternating group order | Aₙ | \|Aₙ\| = n!/2   (even permutations, n ≥ 2) | Ready | `math/abstract_algebra/alternating_group_order/` |
| Ring | (R, +, ·) | A set with addition (an abelian group) and associative multiplication that distributes over addition | Reference | `math/abstract_algebra/ring/` |
| Ideal | I ◁ R | A subring I with r·i and i·r in I for all r ∈ R, i ∈ I | Reference | `math/abstract_algebra/ideal/` |
| Field | F | A commutative ring where every non-zero element has a multiplicative inverse | Ready | `math/abstract_algebra/field/` |
| Integral domain | ID | A commutative ring with 1 ≠ 0 and no zero divisors | Ready | `math/abstract_algebra/integral_domain/` |
| Polynomial ring | R[x] | All polynomials a₀ + a₁x + … + aₙxⁿ with coefficients in R | Reference | `math/abstract_algebra/polynomial_ring/` |
| Field extension | K/F | A field K that contains F as a subfield; [K:F] = dimension of K as an F-vector space | Reference | `math/abstract_algebra/field_extension/` |
| Field extension: degree | [K:F] | [K:F] = dim_F K   (the dimension of K as a vector space over F) | Reference | `math/abstract_algebra/field_extension_degree/` |
| Galois group | Gal(K/F) | The group of automorphisms of K that fix F | Reference | `math/abstract_algebra/galois_group/` |
| Module | M | Like a vector space but over a ring R instead of a field | Reference | `math/abstract_algebra/module/` |
| Vector space | V | A set with vector addition and scalar multiplication over a field satisfying the vector space axioms | Reference | `math/abstract_algebra/vector_space/` |
| Basis | {e₁, …, eₙ} | A linearly independent set that spans the vector space | Ready | `math/abstract_algebra/basis/` |
| Dimension | dim V | The number of vectors in any basis of V | Ready | `math/abstract_algebra/dimension/` |
| Tensor product | ⊗ | (a ⊗ b) = (a₁b₁, a₁b₂, …, aₘbₙ)   (Kronecker product of two vectors) | Ready | `math/abstract_algebra/tensor_product/` |
| Direct sum | ⊕ | A ⊕ B = { (a, b) : a ∈ A, b ∈ B } with component-wise operations; dim(A ⊕ B) = dim A + dim B | Reference | `math/abstract_algebra/direct_sum/` |
| Direct sum: dimension | dim(A ⊕ B) | dim(A ⊕ B) = dim A + dim B | Reference | `math/abstract_algebra/direct_sum_dimension/` |

## Math / Topology

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Open set | U | A set U in a topology τ  (a member of τ) | Ready | `math/topology/open_set/` |
| Closed set | F | A set whose complement is open | Ready | `math/topology/closed_set/` |
| Closure | Ā | Smallest closed set containing A | Ready | `math/topology/closure/` |
| Interior | A° | Largest open set contained in A | Ready | `math/topology/interior/` |
| Boundary | ∂A | ∂A = Ā − A° | Ready | `math/topology/boundary/` |
| Neighborhood | N(x) | A set containing an open set that contains x | Ready | `math/topology/neighborhood/` |
| Basis of topology | ℬ | A collection of open sets such that every open set is a union of members of ℬ | Ready | `math/topology/basis_of_topology/` |
| Subspace topology | τ_A | τ_A = { U ∩ A : U ∈ τ } | Ready | `math/topology/subspace_topology/` |
| Product topology | X × Y | Topology generated by open rectangles U × V | Reference | `math/topology/product_topology/` |
| Continuous map | f: X → Y | f is continuous if the preimage of every open set is open | Reference | `math/topology/continuous_map/` |
| Homeomorphism | ≈ | A continuous bijection with continuous inverse | Reference | `math/topology/homeomorphism/` |
| Compact | compact | Every open cover has a finite subcover | Reference | `math/topology/compact/` |
| Connected | connected | Cannot be split into two disjoint non-empty open sets | Ready | `math/topology/connected/` |
| Path-connected | path-connected | Any two points are joined by a continuous path | Reference | `math/topology/path_connected/` |
| Hausdorff | T₂ | Any two distinct points have disjoint open neighborhoods | Ready | `math/topology/hausdorff/` |
| Metric space distance | d(x, y) | d(x, y) = √Σ(xᵢ − yᵢ)²   (Euclidean metric) | Ready | `math/topology/metric_space_distance/` |
| Open ball | B(x, r) | B(x, r) = { y : d(x, y) < r };  returns True if y is in the ball | Ready | `math/topology/open_ball/` |
| Cauchy sequence | (xₙ) | For every ε > 0 there is N with d(xₘ, xₙ) < ε for all m, n > N | Ready | `math/topology/cauchy_sequence/` |
| Complete space | complete | Every Cauchy sequence converges | Reference | `math/topology/complete_space/` |
| Fundamental group | π₁(X) | The group of loops at a base point, up to homotopy | Reference | `math/topology/fundamental_group/` |
| Homology | Hₙ(X) | Hₙ = ker ∂ₙ / im ∂ₙ₊₁ | Reference | `math/topology/homology/` |
| Cohomology | Hⁿ(X) | Dual to homology: Hⁿ = ker δⁿ / im δⁿ⁻¹ | Reference | `math/topology/cohomology/` |
| Euler characteristic | χ | χ = V − E + F   (vertices − edges + faces) | Ready | `math/topology/euler_characteristic/` |
| Homotopy | ≃ | A continuous deformation of one map into another | Reference | `math/topology/homotopy/` |
| Covering space | p: X̃ → X | A map where every point has a neighborhood evenly covered by p | Reference | `math/topology/covering_space/` |
| Manifold | M | A space that locally looks like ℝⁿ | Reference | `math/topology/manifold/` |

## Math / Real analysis

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Supremum | sup | least upper bound of a set (for a finite set, the maximum) | Ready | `math/real_analysis/supremum/` |
| Infimum | inf | greatest lower bound of a set (for a finite set, the minimum) | Ready | `math/real_analysis/infimum/` |
| Limit superior | lim sup | lim sup aₙ = lim_{n→∞} sup{ aₖ : k ≥ n } | Ready | `math/real_analysis/limit_superior/` |
| Limit inferior | lim inf | lim inf aₙ = lim_{n→∞} inf{ aₖ : k ≥ n } | Ready | `math/real_analysis/limit_inferior/` |
| Convergence | → | aₙ → L if for every ε > 0 there is N with \|aₙ − L\| < ε for all n > N | Ready | `math/real_analysis/convergence/` |
| Uniform convergence | fₙ ⇉ f | sup_x \|fₙ(x) − f(x)\| → 0 as n → ∞ | Reference | `math/real_analysis/uniform_convergence/` |
| Series convergence test | Σ aₙ | Σ aₙ converges if its partial sums converge; use the ratio/root/comparison/integral tests | Ready | `math/real_analysis/series_convergence_test/` |
| Ratio test | L = \|aₙ₊₁/aₙ\| | L = lim \|aₙ₊₁ / aₙ\|;  converges if L < 1, diverges if L > 1 | Ready | `math/real_analysis/ratio_test/` |
| Root test | L = ⁿ√\|aₙ\| | L = lim ⁿ√\|aₙ\|;  converges if L < 1, diverges if L > 1 | Ready | `math/real_analysis/root_test/` |
| Comparison test | aₙ ≤ bₙ | If 0 ≤ aₙ ≤ bₙ and Σbₙ converges then Σaₙ converges | Ready | `math/real_analysis/comparison_test/` |
| Integral test | ∫ vs Σ | For positive decreasing f, Σ f(n) and ∫ f(x) dx converge or diverge together | Ready | `math/real_analysis/integral_test/` |
| Alternating series test | Σ (−1)ⁿ aₙ | Converges if aₙ decreases to 0 | Ready | `math/real_analysis/alternating_series_test/` |
| Radius of convergence | R | R = 1 / L  where L = lim \|aₙ₊₁ / aₙ\| | Ready | `math/real_analysis/radius_of_convergence/` |
| Epsilon-delta continuity | ε–δ | f is continuous at a if ∀ε>0 ∃δ>0: \|x − a\| < δ ⇒ \|f(x) − f(a)\| < ε | Ready | `math/real_analysis/epsilon_delta_continuity/` |
| Uniform continuity | unif. cont. | ∀ε>0 ∃δ>0 (independent of x): \|x − y\| < δ ⇒ \|f(x) − f(y)\| < ε | Reference | `math/real_analysis/uniform_continuity/` |
| Lipschitz ratio | K | \|f(x) − f(y)\| ≤ K \|x − y\|;  this returns \|f(x) − f(y)\| / \|x − y\| | Ready | `math/real_analysis/lipschitz_ratio/` |
| Mean value theorem | f′(c) | f′(c) = (f(b) − f(a)) / (b − a) for some c in (a, b) | Ready | `math/real_analysis/mean_value_theorem/` |
| Intermediate value theorem | IVT | If f is continuous on [a, b] then f takes every value between f(a) and f(b) | Ready | `math/real_analysis/intermediate_value_theorem/` |
| Riemann sum | Σ f(xᵢ)Δx | Σ f(xᵢ) · Δx   (left endpoints, n subintervals) | Ready | `math/real_analysis/riemann_sum/` |
| Riemann–Stieltjes sum | ∫ f dg | Σ f(xᵢ) · (g(xᵢ₊₁) − g(xᵢ)) | Ready | `math/real_analysis/riemannstieltjes_sum/` |
| Measure | μ | A function assigning size to sets: μ(∅) = 0 and countably additive on disjoint sets | Ready | `math/real_analysis/measure/` |
| Lebesgue integral | ∫ f dμ | Integral defined by approximating f with simple functions and measuring their level sets | Ready | `math/real_analysis/lebesgue_integral/` |
| Sigma-algebra | σ-algebra | A collection of sets closed under complement and countable unions, containing the whole space | Reference | `math/real_analysis/sigma_algebra/` |
| Outer measure | μ* | μ*(A) = inf { Σ μ(Iₖ) : A ⊆ ∪ Iₖ } | Ready | `math/real_analysis/outer_measure/` |
| Almost everywhere | a.e. | A property holding except on a set of measure zero | Reference | `math/real_analysis/almost_everywhere/` |
| Lp norm | ‖f‖ₚ | ‖f‖ₚ = (∫\|f\|ᵖ dx)^(1/p)   (numerical, Riemann sum) | Ready | `math/real_analysis/lp_norm/` |
| Banach space | B | A complete normed vector space | Reference | `math/real_analysis/banach_space/` |
| Hilbert space | H | A complete inner-product space | Reference | `math/real_analysis/hilbert_space/` |
| Inner product | ⟨x, y⟩ | ⟨x, y⟩ = Σ xᵢyᵢ   (real vectors) | Ready | `math/real_analysis/inner_product/` |

## Math / Complex analysis

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Real part | Re(z) | Re(a + bi) = a | Ready | `math/complex_analysis/real_part/` |
| Imaginary part | Im(z) | Im(a + bi) = b | Ready | `math/complex_analysis/imaginary_part/` |
| Argument | arg(z) | arg(a + bi) = atan2(b, a) | Ready | `math/complex_analysis/argument/` |
| Euler's formula | e^(iθ) | e^(iθ) = cos θ + i sin θ | Ready | `math/complex_analysis/euler_s_formula/` |
| De Moivre's theorem | (r e^(iθ))ⁿ | (r(cos θ + i sin θ))ⁿ = rⁿ(cos nθ + i sin nθ) | Ready | `math/complex_analysis/de_moivre_s_theorem/` |
| Cauchy–Riemann equations | uₓ = v_y | f = u + iv is complex-differentiable only if ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x | Ready | `math/complex_analysis/cauchyriemann_equations/` |
| Analytic function | holomorphic | A function complex-differentiable in a neighborhood of every point of its domain | Reference | `math/complex_analysis/analytic_function/` |
| Contour integral | ∮ f(z) dz | ∮_C f(z) dz = ∫ f(γ(t)) γ′(t) dt | Ready | `math/complex_analysis/contour_integral/` |
| Residue | Res(f, a) | The coefficient of 1/(z − a) in the Laurent series of f about a | Ready | `math/complex_analysis/residue/` |
| Residue theorem | 2πi Σ Res | ∮_C f(z) dz = 2πi Σ Res(f, aₖ) over poles aₖ inside C | Ready | `math/complex_analysis/residue_theorem/` |
| Laurent series | Σ aₙ (z−a)ⁿ | f(z) = Σ_{n=−∞}^{∞} aₙ (z − a)ⁿ | Reference | `math/complex_analysis/laurent_series/` |
| Cauchy integral formula | f(a) | f(a) = (1 / 2πi) ∮ f(z) / (z − a) dz | Ready | `math/complex_analysis/cauchy_integral_formula/` |
| Mobius transformation | (az+b)/(cz+d) | f(z) = (az + b) / (cz + d),  ad − bc ≠ 0 | Ready | `math/complex_analysis/mobius_transformation/` |
| Conformal map | conformal | An angle-preserving map; any analytic function with f′ ≠ 0 is conformal | Reference | `math/complex_analysis/conformal_map/` |
| Branch cut | branch cut | A curve removed from the complex plane so a multi-valued function (e.g. log, √) becomes single-valued | Reference | `math/complex_analysis/branch_cut/` |

## Math / Transforms and differential equations

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Discrete Fourier transform | F{x} | Xₖ = Σₙ xₙ · e^(−2πi·kn/N) | Ready | `math/transforms_and_differential_equations/discrete_fourier_transform/` |
| Inverse discrete Fourier transform | F⁻¹{X} | xₙ = (1/N) Σₖ Xₖ · e^(2πi·kn/N) | Ready | `math/transforms_and_differential_equations/inverse_discrete_fourier_transform/` |
| Fourier series | Σ aₙcos + bₙsin | f(x) = a₀/2 + Σ (aₙ cos nx + bₙ sin nx),  aₙ = (1/π)∫f cos nx dx,  bₙ = (1/π)∫f sin nx dx | Ready | `math/transforms_and_differential_equations/fourier_series/` |
| Laplace transform | L{f} | F(s) = ∫₀^∞ f(t) e^(−st) dt | Ready | `math/transforms_and_differential_equations/laplace_transform/` |
| Inverse Laplace transform | L⁻¹{F} | f(t) = (1 / 2πi) ∫ F(s) e^(st) ds | Reference | `math/transforms_and_differential_equations/inverse_laplace_transform/` |
| Z-transform | X(z) | X(z) = Σₙ x[n] · z⁻ⁿ | Ready | `math/transforms_and_differential_equations/z_transform/` |
| Convolution | f ∗ g | (f ∗ g)[k] = Σⱼ f[j] · g[k − j] | Ready | `math/transforms_and_differential_equations/convolution/` |
| Dirac delta | δ(x) | δ(x) = 0 for x ≠ 0 and ∫ δ(x) dx = 1 | Ready | `math/transforms_and_differential_equations/dirac_delta/` |
| Heaviside step | H(x) | H(x) = 0 for x < 0, 1 for x > 0 (½ at 0) | Ready | `math/transforms_and_differential_equations/heaviside_step/` |
| First-order ODE | y′ = f(x, y) | An ordinary differential equation involving only the first derivative | Ready | `math/transforms_and_differential_equations/first_order_ode/` |
| Second-order ODE | y″ = f(x, y, y′) | An ordinary differential equation involving up to the second derivative | Ready | `math/transforms_and_differential_equations/second_order_ode/` |
| Separable equation | dy/dx = g(x)h(y) | Rewrite as dy/h(y) = g(x) dx and integrate both sides | Ready | `math/transforms_and_differential_equations/separable_equation/` |
| Integrating factor | μ(x) | For y′ + P(x)y = Q(x):  μ = e^(∫P dx),  (μy)′ = μQ | Ready | `math/transforms_and_differential_equations/integrating_factor/` |
| Characteristic equation | ar² + br + c = 0 | For ay″ + by′ + cy = 0 try y = e^(rx) and solve the quadratic for r | Ready | `math/transforms_and_differential_equations/characteristic_equation/` |
| Wronskian | W(f, g) | W(f, g) = f·g′ − g·f′   (f, g and their derivatives at a point) | Ready | `math/transforms_and_differential_equations/wronskian/` |
| Variation of parameters | yₚ | Particular solution yₚ = −y₁∫(y₂ g / W) dx + y₂∫(y₁ g / W) dx | Ready | `math/transforms_and_differential_equations/variation_of_parameters/` |
| Power series solution | y = Σ cₙ xⁿ | Substitute a power series into the ODE and solve for the coefficients cₙ | Reference | `math/transforms_and_differential_equations/power_series_solution/` |
| Partial differential equation | PDE | An equation involving partial derivatives of a function of several variables | Reference | `math/transforms_and_differential_equations/partial_differential_equation/` |
| Heat equation | uₜ = α uₓₓ | ∂u/∂t = α ∂²u/∂x² | Reference | `math/transforms_and_differential_equations/heat_equation/` |
| Wave equation | uₜₜ = c² uₓₓ | ∂²u/∂t² = c² ∂²u/∂x² | Reference | `math/transforms_and_differential_equations/wave_equation/` |
| Laplace's equation | ∇²u = 0 | ∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z² = 0 | Reference | `math/transforms_and_differential_equations/laplace_s_equation/` |

## Math / Graph theory and combinatorics

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Graph | G = (V, E) | A set of vertices V and a set of edges E joining pairs of vertices | Ready | `math/graph_theory_and_combinatorics/graph/` |
| Vertex degree | deg(v) | deg(v) = number of edges at v   (graph = {vertex: [neighbors]}) | Ready | `math/graph_theory_and_combinatorics/vertex_degree/` |
| Path | path | A sequence of distinct vertices where consecutive vertices are joined by edges | Ready | `math/graph_theory_and_combinatorics/path/` |
| Cycle | cycle | A path that returns to its starting vertex | Ready | `math/graph_theory_and_combinatorics/cycle/` |
| Tree | tree | A connected graph with no cycles; a tree on n vertices has n − 1 edges | Ready | `math/graph_theory_and_combinatorics/tree/` |
| Spanning tree | T ⊆ G | A tree that contains every vertex of G | Ready | `math/graph_theory_and_combinatorics/spanning_tree/` |
| Adjacency matrix | A | Aᵢⱼ = 1 if vertices i and j are joined (undirected), else 0 | Ready | `math/graph_theory_and_combinatorics/adjacency_matrix/` |
| Shortest path (Dijkstra) | d(u, v) | Dijkstra's algorithm; graph = {node: [(neighbor, weight), …]}, returns {node: distance} | Ready | `math/graph_theory_and_combinatorics/shortest_path_dijkstra/` |
| Shortest path (A*) | A* | A* on the Dijkstra graph with node positions; straight-line distance to the goal; returns the path of nodes | Ready | `math/graph_theory_and_combinatorics/a_star/` |
| Chromatic number | χ(G) | The smallest number of colors needed to color vertices so adjacent vertices differ | Ready | `math/graph_theory_and_combinatorics/chromatic_number/` |
| Planar graph | planar | Can be drawn in the plane without crossing edges; then E ≤ 3V − 6 (V ≥ 3) | Ready | `math/graph_theory_and_combinatorics/planar_graph/` |
| Euler path | Euler path | A path using every edge exactly once; exists iff the graph is connected with 0 or 2 odd-degree vertices | Ready | `math/graph_theory_and_combinatorics/euler_path/` |
| Hamiltonian path | Hamilton path | A path visiting every vertex exactly once | Ready | `math/graph_theory_and_combinatorics/hamiltonian_path/` |
| Bipartite graph | bipartite | Vertices split into two sets with edges only between the sets (no odd cycles) | Ready | `math/graph_theory_and_combinatorics/bipartite_graph/` |
| Max flow min cut | max-flow = min-cut | The maximum flow from source to sink equals the capacity of the minimum cut | Ready | `math/graph_theory_and_combinatorics/max_flow_min_cut/` |
| Catalan number | Cₙ | Cₙ = C(2n, n) / (n + 1) | Ready | `math/graph_theory_and_combinatorics/catalan_number/` |
| Stirling number (second kind) | S(n, k) | S(n, k) = (1/k!) Σⱼ (−1)ʲ C(k, j) (k − j)ⁿ | Ready | `math/graph_theory_and_combinatorics/stirling_number_second_kind/` |
| Bell number | Bₙ | Bₙ = Σₖ S(n, k)   (number of partitions of an n-element set) | Ready | `math/graph_theory_and_combinatorics/bell_number/` |
| Partition number | p(n) | p(n) = number of ways to write n as a sum of positive integers (order ignored) | Ready | `math/graph_theory_and_combinatorics/partition_number/` |
| Generating function | G(x) | G(x) = Σ aₙ xⁿ  encodes the sequence a₀, a₁, a₂, … | Ready | `math/graph_theory_and_combinatorics/generating_function/` |
| Recurrence relation | aₙ = f(aₙ₋₁, …) | Defines each term from earlier terms, e.g. Fibonacci Fₙ = Fₙ₋₁ + Fₙ₋₂ | Ready | `math/graph_theory_and_combinatorics/recurrence_relation/` |
| Burnside's lemma | \|X/G\| | Number of orbits = (1/\|G\|) Σ_g \|Fix(g)\| | Ready | `math/graph_theory_and_combinatorics/burnside_s_lemma/` |

## Math / Optimization and numerical methods

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Minimize | min f | Find x that makes f(x) as small as possible | Ready | `math/optimization_and_numerical_methods/minimize/` |
| Maximize | max f | Find x that makes f(x) as large as possible (minimize −f) | Ready | `math/optimization_and_numerical_methods/maximize/` |
| Lagrange multipliers | ∇f = λ∇g | Extrema of f subject to g = 0 occur where ∇f = λ ∇g | Ready | `math/optimization_and_numerical_methods/lagrange_multipliers/` |
| Gradient descent | xₖ₊₁ = xₖ − η∇f | Repeat xₖ₊₁ = xₖ − η ∇f(xₖ) | Ready | `math/optimization_and_numerical_methods/gradient_descent/` |
| Hessian | H | Hᵢⱼ = ∂²f / ∂xᵢ∂xⱼ  (matrix of second partial derivatives) | Ready | `math/optimization_and_numerical_methods/hessian/` |
| Linear programming | LP | Maximize cᵀx subject to Ax ≤ b, x ≥ 0 | Ready | `math/optimization_and_numerical_methods/linear_programming/` |
| Simplex method | simplex | Algorithm that walks along vertices of the feasible region to solve a linear program | Ready | `math/optimization_and_numerical_methods/simplex_method/` |
| Convex function | convex | f(tx + (1−t)y) ≤ t·f(x) + (1−t)·f(y) for t in [0, 1] | Ready | `math/optimization_and_numerical_methods/convex_function/` |
| KKT conditions | KKT | Necessary conditions for optimality under inequality constraints: stationarity, feasibility, complementary slackness | Reference | `math/optimization_and_numerical_methods/kkt_conditions/` |
| KKT: primal feasibility | g(x) ≤ 0 | g(x) ≤ 0 | Reference | `math/optimization_and_numerical_methods/kkt_primal_feasibility/` |
| KKT: dual feasibility | λ ≥ 0 | λ ≥ 0 | Reference | `math/optimization_and_numerical_methods/kkt_dual_feasibility/` |
| KKT: complementary slackness | λ·g(x) = 0 | λ·g(x) = 0 | Reference | `math/optimization_and_numerical_methods/kkt_complementary_slackness/` |
| Newton's method | xₙ₊₁ = xₙ − f/f′ | xₙ₊₁ = xₙ − f(xₙ) / f′(xₙ) | Ready | `math/optimization_and_numerical_methods/newton_s_method/` |
| Bisection method | bisect | Repeatedly halve [a, b] keeping the half where f changes sign | Ready | `math/optimization_and_numerical_methods/bisection_method/` |
| Secant method | secant | xₙ₊₁ = xₙ − f(xₙ)(xₙ − xₙ₋₁) / (f(xₙ) − f(xₙ₋₁)) | Ready | `math/optimization_and_numerical_methods/secant_method/` |
| Fixed-point iteration | x = g(x) | xₙ₊₁ = g(xₙ) | Ready | `math/optimization_and_numerical_methods/fixed_point_iteration/` |
| Euler's method | yₙ₊₁ = yₙ + h·f | yₙ₊₁ = yₙ + h · f(xₙ, yₙ)   (returns list of (x, y) points) | Ready | `math/optimization_and_numerical_methods/euler_s_method/` |
| Runge-Kutta (RK4) | RK4 | yₙ₊₁ = yₙ + h/6 · (k₁ + 2k₂ + 2k₃ + k₄) | Ready | `math/optimization_and_numerical_methods/runge_kutta_rk4/` |
| Trapezoid rule | T | ∫ₐᵇ f ≈ h · (f(a)/2 + Σ f(xᵢ) + f(b)/2),  h = (b − a)/n | Ready | `math/optimization_and_numerical_methods/trapezoid_rule/` |
| Simpson's rule | S | ∫ₐᵇ f ≈ h/3 · (f₀ + 4f₁ + 2f₂ + … + fₙ),  n even | Ready | `math/optimization_and_numerical_methods/simpson_s_rule/` |
| Lagrange interpolation | L(x) | L(x) = Σᵢ yᵢ ∏_{j≠i} (x − xⱼ) / (xᵢ − xⱼ) | Ready | `math/optimization_and_numerical_methods/lagrange_interpolation/` |
| Newton interpolation | N(x) | N(x) = c₀ + c₁(x − x₀) + c₂(x − x₀)(x − x₁) + …  (divided differences) | Ready | `math/optimization_and_numerical_methods/newton_interpolation/` |
| Spline | S(x) | A piecewise polynomial (often cubic) joined smoothly at knots | Ready | `math/optimization_and_numerical_methods/spline/` |
| Least squares | min Σ(yᵢ − ŷᵢ)² | Best-fit line y = mx + b minimizing squared error; returns (slope, intercept) | Ready | `math/optimization_and_numerical_methods/least_squares/` |
| Gaussian elimination | A\|b → U | Reduce [A \| b] to upper-triangular form, then back-substitute | Ready | `math/optimization_and_numerical_methods/gaussian_elimination/` |
| Jacobi iteration | x⁽ᵏ⁺¹⁾ | xᵢ⁽ᵏ⁺¹⁾ = (bᵢ − Σ_{j≠i} Aᵢⱼ xⱼ⁽ᵏ⁾) / Aᵢᵢ | Ready | `math/optimization_and_numerical_methods/jacobi_iteration/` |
| Gauss-Seidel iteration | x⁽ᵏ⁺¹⁾ | Like Jacobi but uses the newest values immediately | Ready | `math/optimization_and_numerical_methods/gauss_seidel_iteration/` |

## Math / Differential geometry and tensors

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Tangent vector | v ∈ TₚM | The velocity vector of a curve through p on a manifold | Ready | `math/differential_geometry_and_tensors/tangent_vector/` |
| Tangent space | TₚM | The vector space of all tangent vectors at p | Reference | `math/differential_geometry_and_tensors/tangent_space/` |
| Differential form | ω | A smooth, antisymmetric, multilinear field that can be integrated over manifolds | Reference | `math/differential_geometry_and_tensors/differential_form/` |
| Exterior derivative | d | d(f dx) = df ∧ dx,  d² = 0 | Reference | `math/differential_geometry_and_tensors/exterior_derivative/` |
| Exterior derivative: d squared is zero | d² = 0 | d² = 0 | Reference | `math/differential_geometry_and_tensors/exterior_derivative_nilpotent/` |
| Wedge product | ∧ | α ∧ β = −β ∧ α  (antisymmetric product of differential forms) | Ready | `math/differential_geometry_and_tensors/wedge_product/` |
| Pullback | f* | (f*ω)(v) = ω(df(v)) | Reference | `math/differential_geometry_and_tensors/pullback/` |
| Metric tensor | g | gᵢⱼ gives lengths and angles: ds² = gᵢⱼ dxⁱ dxʲ | Ready | `math/differential_geometry_and_tensors/metric_tensor/` |
| Christoffel symbol | Γᵏᵢⱼ | Γᵏᵢⱼ = ½ gᵏˡ (∂ᵢgⱼˡ + ∂ⱼgᵢˡ − ∂ˡgᵢⱼ) | Reference | `math/differential_geometry_and_tensors/christoffel_symbol/` |
| Riemann curvature | Rᵃᵦᵧδ | Measures how parallel transport around a small loop fails to return a vector unchanged | Reference | `math/differential_geometry_and_tensors/riemann_curvature/` |
| Ricci tensor | Rᵢⱼ | Rᵢⱼ = Rᵏᵢₖⱼ  (contraction of the Riemann tensor) | Reference | `math/differential_geometry_and_tensors/ricci_tensor/` |
| Gaussian curvature | K | K = κ₁ · κ₂  (product of the principal curvatures) | Ready | `math/differential_geometry_and_tensors/gaussian_curvature/` |
| Geodesic | γ″ = 0 | A locally shortest path; ẍᵏ + Γᵏᵢⱼ ẋⁱ ẋʲ = 0 | Reference | `math/differential_geometry_and_tensors/geodesic/` |
| Lie derivative | L_X | The rate of change of a tensor field along the flow of the vector field X | Reference | `math/differential_geometry_and_tensors/lie_derivative/` |
| Lie bracket | [X, Y] | [X, Y] f = X(Y f) − Y(X f) | Ready | `math/differential_geometry_and_tensors/lie_bracket/` |
| Stokes' theorem | ∫_M dω = ∫_∂M ω | The integral of dω over M equals the integral of ω over the boundary ∂M | Reference | `math/differential_geometry_and_tensors/stokes_theorem/` |
| Tensor contraction | Tⁱᵢ | Sum over a paired upper and lower index, lowering the tensor's rank by 2 | Ready | `math/differential_geometry_and_tensors/tensor_contraction/` |

## Math / Category theory and foundations

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Category | 𝒞 | Objects and morphisms with composition (associative) and identity morphisms | Reference | `math/category_theory_and_foundations/category/` |
| Functor | F: 𝒞 → 𝒟 | A map between categories preserving composition and identities | Reference | `math/category_theory_and_foundations/functor/` |
| Natural transformation | η: F ⇒ G | A family of morphisms ηₓ: F(X) → G(X) that commute with F(f) and G(f) | Reference | `math/category_theory_and_foundations/natural_transformation/` |
| Morphism | f: A → B | An arrow from object A to object B in a category | Reference | `math/category_theory_and_foundations/morphism/` |
| Product and coproduct | A × B, A ⊔ B | Universal objects with projections (product) or injections (coproduct) | Reference | `math/category_theory_and_foundations/product_and_coproduct/` |
| Limit and colimit | lim, colim | Universal cone over (or cocone under) a diagram | Reference | `math/category_theory_and_foundations/limit_and_colimit/` |
| Adjunction | F ⊣ G | Hom(F(A), B) ≅ Hom(A, G(B)) naturally | Reference | `math/category_theory_and_foundations/adjunction/` |
| Aleph-null | ℵ₀ | The cardinality of the natural numbers | Reference | `math/category_theory_and_foundations/aleph_null/` |
| Omega ordinal | ω | The first infinite ordinal, the order type of the natural numbers | Reference | `math/category_theory_and_foundations/omega_ordinal/` |
| Axiom of choice | AC | Every collection of non-empty sets has a choice function | Ready | `math/category_theory_and_foundations/axiom_of_choice/` |
| Zorn's lemma | Zorn | If every chain in a poset has an upper bound, then the poset has a maximal element | Reference | `math/category_theory_and_foundations/zorn_s_lemma/` |
| Power set | 𝒫(A) | 𝒫(A) = set of all subsets of A;  \|𝒫(A)\| = 2^\|A\| | Ready | `math/category_theory_and_foundations/power_set/` |
| Cartesian product | A × B | A × B = { (a, b) : a ∈ A, b ∈ B } | Ready | `math/category_theory_and_foundations/cartesian_product/` |
| Function | f: A → B | A rule assigning to each element of A exactly one element of B | Ready | `math/category_theory_and_foundations/function/` |
| Injective | one-to-one | f(x) = f(y) ⇒ x = y | Ready | `math/category_theory_and_foundations/injective/` |
| Surjective | onto | every element of the codomain is f(x) for some x | Ready | `math/category_theory_and_foundations/surjective/` |
| Bijective | one-to-one and onto | both injective and surjective | Ready | `math/category_theory_and_foundations/bijective/` |
| Natural numbers | ℕ | {0, 1, 2, 3, …} (or {1, 2, 3, …}) | Ready | `math/category_theory_and_foundations/natural_numbers/` |
| Integers | ℤ | {…, −2, −1, 0, 1, 2, …} | Ready | `math/category_theory_and_foundations/integers/` |
| Rational numbers | ℚ | { p/q : p, q ∈ ℤ, q ≠ 0 } | Ready | `math/category_theory_and_foundations/rational_numbers/` |
| Real numbers | ℝ | The complete ordered field: all rational and irrational numbers | Ready | `math/category_theory_and_foundations/real_numbers/` |
| Complex numbers | ℂ | { a + bi : a, b ∈ ℝ } | Ready | `math/category_theory_and_foundations/complex_numbers/` |
| Quaternions | ℍ | { a + bi + cj + dk } with i² = j² = k² = ijk = −1 | Ready | `math/category_theory_and_foundations/quaternions/` |

## Math / Constants and relations

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Pi | π | π = circumference / diameter ≈ 3.14159265… | Ready | `math/constants_and_relations/pi/` |
| Euler's number | e | e = lim (1 + 1/n)ⁿ ≈ 2.71828182… | Ready | `math/constants_and_relations/euler_s_number/` |
| Golden ratio | φ | φ = (1 + √5) / 2 ≈ 1.6180339887… | Ready | `math/constants_and_relations/golden_ratio/` |
| Euler-Mascheroni constant | γ | γ = lim (1 + 1/2 + … + 1/n − ln n) ≈ 0.5772156649 | Ready | `math/constants_and_relations/euler_mascheroni_constant/` |
| Equals | = | a = b | Ready | `math/constants_and_relations/equals/` |
| Not equal | ≠ | a ≠ b | Ready | `math/constants_and_relations/not_equal/` |
| Approximately equal | ≈ | a ≈ b  (equal within a small tolerance) | Ready | `math/constants_and_relations/approximately_equal/` |
| Less than | < | a < b | Ready | `math/constants_and_relations/less_than/` |
| Greater than | > | a > b | Ready | `math/constants_and_relations/greater_than/` |
| Less than or equal | ≤ | a ≤ b | Ready | `math/constants_and_relations/less_than_or_equal/` |
| Greater than or equal | ≥ | a ≥ b | Ready | `math/constants_and_relations/greater_than_or_equal/` |
| Proportional to | ∝ | y ∝ x  means y = k·x;  returns the constant k = y / x | Ready | `math/constants_and_relations/proportional_to/` |
| Open bracket | ( | ( begins a group; what is inside is evaluated first | Reference | `math/constants_and_relations/open_bracket/` |
| Close bracket | ) | ) ends a group opened by ( | Reference | `math/constants_and_relations/close_bracket/` |
| Square brackets | [ ] | [ … ] group an expression, or denote a closed interval [a, b] / a list | Reference | `math/constants_and_relations/square_brackets/` |
| Curly braces | { } | { … } denote a set or a group of terms | Reference | `math/constants_and_relations/curly_braces/` |

## Geometry / Geometry

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Circle area | πr² | A = π r² | Ready | `geometry/geometry/circle_area/` |
| Circle circumference | 2πr | C = 2 π r | Ready | `geometry/geometry/circle_circumference/` |
| Arc length | rθ | s = r θ   (θ in radians) | Ready | `geometry/geometry/arc_length/` |
| Sector area | ½r²θ | A = ½ r² θ   (θ in radians) | Ready | `geometry/geometry/sector_area/` |
| Rectangle area | l×w | A = l · w | Ready | `geometry/geometry/rectangle_area/` |
| Rectangle perimeter | 2(l+w) | P = 2(l + w) | Ready | `geometry/geometry/rectangle_perimeter/` |
| Square area | s² | A = s² | Ready | `geometry/geometry/square_area/` |
| Triangle area | ½bh | A = ½ · base · height | Ready | `geometry/geometry/triangle_area/` |
| Heron's formula | √(s(s−a)(s−b)(s−c)) | A = √(s(s−a)(s−b)(s−c)),  s = (a + b + c)/2 | Ready | `geometry/geometry/heron_s_formula/` |
| Heron's formula: semi-perimeter | s = (a+b+c)/2 | s = (a + b + c) / 2   (half the distance round the triangle) | Ready | `geometry/geometry/heron_semiperimeter/` |
| Heron's formula: area | √(s(s−a)(s−b)(s−c)) | A = √(s(s−a)(s−b)(s−c))   (s is the semi-perimeter, from the row above) | Ready | `geometry/geometry/heron_area/` |
| Pythagorean theorem | a²+b²=c² | c = √(a² + b²)   (hypotenuse of a right triangle) | Ready | `geometry/geometry/pythagorean_theorem/` |
| Parallelogram area | bh | A = base · height | Ready | `geometry/geometry/parallelogram_area/` |
| Trapezoid area | ½(a+b)h | A = ½ (a + b) h | Ready | `geometry/geometry/trapezoid_area/` |
| Rhombus area | ½d₁d₂ | A = ½ d₁ d₂ | Ready | `geometry/geometry/rhombus_area/` |
| Regular polygon area | ½·p·a | A = ½ · perimeter · apothem | Ready | `geometry/geometry/regular_polygon_area/` |
| Polygon interior angle sum | (n−2)·180° | sum of interior angles = (n − 2) × 180° | Ready | `geometry/geometry/polygon_interior_angle_sum/` |
| Cube volume | s³ | V = s³ | Ready | `geometry/geometry/cube_volume/` |
| Cube surface area | 6s² | SA = 6 s² | Ready | `geometry/geometry/cube_surface_area/` |
| Rectangular prism volume | lwh | V = l · w · h | Ready | `geometry/geometry/rectangular_prism_volume/` |
| Rectangular prism surface area | 2(lw+lh+wh) | SA = 2(lw + lh + wh) | Ready | `geometry/geometry/rectangular_prism_surface_area/` |
| Cylinder volume | πr²h | V = π r² h | Ready | `geometry/geometry/cylinder_volume/` |
| Cylinder surface area | 2πr(r+h) | SA = 2 π r (r + h) | Ready | `geometry/geometry/cylinder_surface_area/` |
| Cone volume | ⅓πr²h | V = ⅓ π r² h | Ready | `geometry/geometry/cone_volume/` |
| Cone surface area | πr(r+l) | SA = π r (r + l),  l = slant height | Ready | `geometry/geometry/cone_surface_area/` |
| Sphere volume | ⁴⁄₃πr³ | V = 4/3 π r³ | Ready | `geometry/geometry/sphere_volume/` |
| Sphere surface area | 4πr² | SA = 4 π r² | Ready | `geometry/geometry/sphere_surface_area/` |
| Pyramid volume | ⅓Bh | V = ⅓ · base area · height | Ready | `geometry/geometry/pyramid_volume/` |
| Distance formula | √((x₂−x₁)²+(y₂−y₁)²) | d = √((x₂ − x₁)² + (y₂ − y₁)²) | Ready | `geometry/geometry/distance_formula/` |
| Midpoint formula | ((x₁+x₂)/2, (y₁+y₂)/2) | M = ((x₁ + x₂)/2, (y₁ + y₂)/2) | Ready | `geometry/geometry/midpoint_formula/` |
| Slope | (y₂−y₁)/(x₂−x₁) | m = (y₂ − y₁) / (x₂ − x₁) | Ready | `geometry/geometry/slope/` |
| Law of sines | a/sin A = b/sin B | b = a · sin B / sin A   (angles in radians) | Ready | `geometry/geometry/law_of_sines/` |
| Law of cosines | c²=a²+b²−2ab·cos C | c = √(a² + b² − 2ab cos C)   (C in radians) | Ready | `geometry/geometry/law_of_cosines/` |
| Degrees to radians (Geometry) | deg→rad | radians = degrees × π / 180 | Ready | `geometry/geometry/degrees_to_radians_geometry/` |
| Radians to degrees (Geometry) | rad→deg | degrees = radians × 180 / π | Ready | `geometry/geometry/radians_to_degrees_geometry/` |

## Physics / Physics

| Operator | Symbol | Formula | Status | Folder |
|---|---|---|---|---|
| Velocity | v = d/t | v = d / t | Ready | `physics/physics/velocity/` |
| Acceleration | a = Δv/t | a = Δv / t | Ready | `physics/physics/acceleration/` |
| Final velocity | v = u + at | v = u + a t | Ready | `physics/physics/final_velocity/` |
| Displacement | s = ut + ½at² | s = u t + ½ a t² | Ready | `physics/physics/displacement/` |
| Velocity squared | v² = u² + 2as | v = √(u² + 2 a s) | Ready | `physics/physics/velocity_squared/` |
| Newton's second law | F = ma | F = m a | Ready | `physics/physics/newton_s_second_law/` |
| Weight | W = mg | W = m g   (g = 9.81 m/s²) | Ready | `physics/physics/weight/` |
| Speed after a distance | v² = u² + 2as | v = √(u² + 2 a s)   (u in m/s, a in m/s², s in metres along the line) | Ready | `physics/physics/speed_after_distance/` |
| Time to a distance | s = ut + ½at² | the smallest t ≥ 0 with s = u t + ½ a t²   (s is the signed displacement) | Ready | `physics/physics/time_to_distance/` |
| Stopping distance | s = −u²/2a | s = −u² / (2 a)   (the signed displacement until the speed is 0; a must oppose u) | Ready | `physics/physics/stopping_distance/` |
| Braking time | t = −u/a | t = −u / a   (the time until the speed is 0; a must oppose u) | Ready | `physics/physics/braking_time/` |
| Projectile range | R = v² sin 2θ / g | R = v² sin(2θ) / g   (level ground, no drag, g = 9.81 m/s², θ in radians) | Ready | `physics/physics/projectile_range/` |
| Projectile time of flight | T = 2v sin θ / g | T = 2 v sin θ / g   (back to the same height, no drag, g = 9.81 m/s², θ in radians) | Ready | `physics/physics/projectile_time_of_flight/` |
| Projectile position | x, y at t | x = v cos θ · t,  y = v sin θ · t − ½ g t²   (y is up, no drag, g = 9.81 m/s²) | Ready | `physics/physics/projectile_position/` |
| Hover thrust | T = mg | T = m g   (the upward force that balances the weight, g = 9.81 m/s²) | Ready | `physics/physics/hover_thrust/` |
| Force down a slope | F = mg sin θ | F = m g sin θ   (the part of the weight that pulls down the slope, g = 9.81 m/s², θ in radians above the horizontal) | Ready | `physics/physics/slope_force/` |
| Most friction on a slope | f = μ m g cos θ | f = μ m g cos θ   (the largest static friction, μ times the normal force, g = 9.81 m/s², θ in radians) | Ready | `physics/physics/max_friction_on_slope/` |
| Steepest climb | θ = atan μ | θ = atan μ   (the steepest slope friction μ can hold, in radians; mass and gravity cancel) | Ready | `physics/physics/steepest_climb_angle/` |
| Centre of mass | Σ m x / Σ m | [x, y, z] = Σ mᵢ pᵢ / Σ mᵢ   (each position is x, y, z in metres) | Ready | `physics/physics/centre_of_mass/` |
| Cylinder moment of inertia | I = ½ M R² | I = ½ M R²   (a solid cylinder or disc about its own centre axis) | Ready | `physics/physics/cylinder_moment_of_inertia/` |
| Angular acceleration | α = τ / I | α = τ / I   (a negative torque turns the other way) | Ready | `physics/physics/angular_acceleration/` |
| Tipping margin | b cos θ − h sin θ | b cos θ − h sin θ   (metres from the downhill foot to where the weight falls; positive stays upright) | Ready | `physics/physics/tipping_margin/` |
| Tree impact force | F = mv² / 2s | F = m v² / (2 s)   (the average force to stop a mass from speed v over a distance s) | Ready | `physics/physics/impact_force/` |
| Dead reckoning | x + v t along the heading | east = x + v cos(heading) t,  north = y + v sin(heading) t   (heading 0 is east, positive turns toward north; a negative speed backs up) | Ready | `physics/physics/dead_reckoning/` |
| Exponential smoothing | y = αx + (1 − α)y₀ | y = α x + (1 − α) y₀   (one new sample blended into the previous estimate; α = 0 keeps the old value, α = 1 takes the new sample) | Ready | `physics/physics/exponential_smoothing/` |
| Kalman predict state | x′ = x + ut | x′ = x + u t   (the position a 1-D filter expects after coasting at speed u for time t) | Ready | `physics/physics/kalman_predict_state/` |
| Kalman predict variance | p′ = p + q | p′ = p + q   (the uncertainty grows by the process noise q) | Ready | `physics/physics/kalman_predict_variance/` |
| Kalman update | x⁺ = x + k(z − x) | k = p / (p + r),  x⁺ = x + k (z − x)   (the menu operator opens three rows: predict the state, predict the variance, then this update) | Ready | `physics/physics/kalman_update_state/` |
| Kalman update variance | p⁺ = (1 − k)p | k = p / (p + r),  p⁺ = (1 − k) p   (kept out of the three-row step: the robot needs this variance for the next step) | Ready | `physics/physics/kalman_update_variance/` |
| Haversine distance | great-circle distance | a = sin²(Δlat/2) + cos(lat1) cos(lat2) sin²(Δlon/2),  d = 6371000 · 2 atan2(√a, √(1 − a))   (Earth radius 6371000 m, angles in radians) | Ready | `physics/physics/haversine_distance/` |
| Bearing between two points | atan2(north, east) | east = sin(Δlon) cos(lat2),  north = cos(lat1) sin(lat2) − sin(lat1) cos(lat2) cos(Δlon),  heading = atan2(north, east)   (0 is east, positive turns toward north) | Ready | `physics/physics/bearing_between/` |
| Complementary filter | α(θ + ωt) + (1 − α)θₘ | θ = α (θ₀ + ω t) + (1 − α) θₘ   (the gyro prediction blended with a measured angle; α close to 1 trusts the gyro) | Ready | `physics/physics/complementary_filter/` |
| Local east, north, up | a small GPS step on the flat Earth | east = 6371000 cos(lat) Δlon,  north = 6371000 Δlat,  up = Δheight   (radians and metres; the flat patch, not the haversine arc) | Ready | `physics/physics/local_east_north_up/` |
| Control error | e = setpoint − measured | e = setpoint − measured   (positive means too low) | Ready | `physics/physics/control_error/` |
| PID proportional | P = Kp e | P = Kp e   (the proportional term) | Ready | `physics/physics/pid_proportional/` |
| PID integral state | I ← I + e t | I ← I + e t   (the stored integral the robot keeps for the next step; not part of the four-row sum) | Ready | `physics/physics/pid_integral_state/` |
| PID integral term | Iout = Ki (I + e t) | Iout = Ki (I + e t)   (the integral contribution: this step's error is added before multiplying by Ki) | Ready | `physics/physics/pid_integral_term/` |
| PID derivative | D = Kd (e − e₀) / t | D = Kd (e − e₀) / t   (the derivative contribution) | Ready | `physics/physics/pid_derivative/` |
| PID output | P + I + D | P + I + D   (the sum of the three terms; the menu operator opens four rows joined by →, the answer is the last row) | Ready | `physics/physics/pid_sum/` |
| Saturation | clamp | clamp(value, low, high)   (the value limited to the low and high ends) | Ready | `physics/physics/saturation/` |
| Low-pass step | y + (t/(t+τ))(x − y) | y + (t / (t + τ)) (x − y)   (one step of a low-pass filter with time constant τ; the weight is t / (t + τ), not a typed α) | Ready | `physics/physics/low_pass_step/` |
| Distance in 3D | |b − a| | |b − a|   (the straight-line distance between two points, in metres) | Ready | `physics/physics/distance_3d/` |
| Time to collision | distance / closing speed | t = |r| / (−(r · v) / |r|)   (r is the obstacle minus the robot, v the robot's velocity; only when the closing speed is positive) | Ready | `physics/physics/time_to_collision/` |
| Point inside a sphere | |p − c| ≤ R | 1 if the point is inside or on the sphere, 0 if it is outside | Ready | `physics/physics/point_inside_sphere/` |
| Point inside a tree trunk | a vertical cylinder | 1 if the point is inside or on the vertical cylinder standing on z = 0 at (cx, cy), out to radius R and up to height h; 0 otherwise | Ready | `physics/physics/point_inside_cylinder/` |
| Turn radius | r = v² / (g tan φ) | r = v² / (g tan φ)   (a level banked turn; φ in radians, positive to the left; a negative radius turns the other way; g = 9.81 m/s²) | Ready | `physics/physics/turn_radius/` |
| Closing speed | −(r · v) / |r| | −(r · v) / |r|   (how fast the distance to a fixed obstacle is shrinking; positive means approaching) | Ready | `physics/physics/closing_speed/` |
| GPS kinematic clock | (1/γ − 1) per day | (1/γ − 1) · 86400 · 1000000   (microseconds per day by which a moving clock runs behind a clock at rest; the answer is negative) | Ready | `physics/physics/gps_kinematic_clock/` |
| GPS gravitational clock | GM (1/R − 1/r) / c² per day | GM (1/R − 1/r) / c² · 86400 · 10⁶   (microseconds per day by which a clock at radius r runs ahead of a clock at radius R; GM = 3.986004418e14 m³/s², c = 299792458 m/s) | Ready | `physics/physics/gps_gravitational_clock/` |
| GPS clock correction | special plus gravitational | special + gravitational   (about +38 microseconds per day; the menu operator opens four rows joined by →, the answer is the last row) | Ready | `physics/physics/gps_clock_correction/` |
| Distance to a segment | distance from a point to a segment | t = ((p − a) · (b − a)) / |b − a|² clamped to 0..1;  the closest point is a + t (b − a);  the answer is the distance from p to it (metres) | Ready | `physics/physics/distance_to_segment/` |
| Point inside a camera cone | field of view | 1 when v · d > 0 and (v · d) / (|v| |d|) ≥ cos α, with v = p − c (the camera c looks along d with half-angle α; the edge counts as inside); 0 otherwise | Ready | `physics/physics/point_inside_camera_cone/` |
| Potential-field step | pull plus push | F = k_att (goal − position) + F_rep;  inside the influence distance F_rep = k_rep (1/d − 1/influence)(1/d²) u, otherwise 0  (u points from the obstacle toward the robot) | Ready | `physics/physics/potential_field_step/` |
| Schwarzschild g_tt | g_tt = −(1 − Rs/r) | g_tt = −(1 − Rs/r)   (the time coefficient of the Schwarzschild metric outside a spherical mass, signature (−, +, +, +); r and Rs in metres) | Ready | `physics/physics/schwarzschild_g_tt/` |
| Schwarzschild g_rr | g_rr = 1/(1 − Rs/r) | g_rr = 1 / (1 − Rs/r)   (the radial coefficient of the Schwarzschild metric outside a spherical mass; r and Rs in metres) | Ready | `physics/physics/schwarzschild_g_rr/` |
| Photon sphere | r = 3GM/c² = 1.5 Rs | r = 3GM/c² = 1.5 Rs   (the radius of the unstable circular orbit of a light ray) | Ready | `physics/physics/photon_sphere_radius/` |
| Innermost stable circular orbit | r = 6GM/c² = 3 Rs | r = 6GM/c² = 3 Rs   (the closest stable circular orbit of a massive particle around a non-spinning mass) | Ready | `physics/physics/isco_radius/` |
| Circular-orbit angular speed | Ω = c √(Rs / (2 r³)) | Ω = c √(Rs / (2 r³))   (radians per second of coordinate time for a circular orbit around a non-spinning mass; the Kepler form; r > 1.5 Rs; c = 299792458 m/s) | Ready | `physics/physics/schwarzschild_orbit_angular_speed/` |
| Circular-orbit period | T = 2π / Ω | T = 2π / Ω   (the coordinate-time period of a circular orbit around a non-spinning mass; r > 1.5 Rs) | Ready | `physics/physics/schwarzschild_orbit_period/` |
| Circular-orbit coordinate speed | r Ω = c √(Rs / (2 r)) | r Ω = c √(Rs / (2 r))   (the Kepler speed of a circular orbit: circumference radius times the angular speed; not the speed a hovering observer measures; r > 1.5 Rs) | Ready | `physics/physics/schwarzschild_coordinate_speed/` |
| Circular-orbit local speed | v = c √((Rs/2r) / (1 − Rs/r)) | v = c √( (Rs / (2 r)) / (1 − Rs / r) )   (the speed an observer hovering at that radius measures; stable orbits only, r ≥ 3 Rs) | Ready | `physics/physics/schwarzschild_local_orbit_speed/` |
| Light deflection | δ = 2 Rs / b | δ = 4GM / (c² b) = 2 Rs / b   (the weak-field bend of a ray with closest approach b, in radians; only accurate when Rs/b is small; b ≤ (3√3/2) Rs falls into the mass) | Ready | `physics/physics/light_deflection_angle/` |
| Perihelion advance | 3π Rs / (a (1 − e²)) per orbit | 3π Rs / (a (1 − e²)) radians per orbit, times 36525 / period_days orbits per century, times 648000/π: arcseconds per century (the general-relativity part only, not the pull of other planets) | Ready | `physics/physics/perihelion_advance/` |
| Schwarzschild frequency ratio | ν_receiver / ν_source | ν_receiver / ν_source = √((1 − Rs/r_source) / (1 − Rs/r_receiver))   (between two static clocks outside the horizon; below 1 when the source is deeper, above 1 when the receiver is deeper) | Ready | `physics/physics/schwarzschild_frequency_ratio/` |
| Schwarzschild radial step | one proper-time step of r | r_next = r + v Δτ + ½ a Δτ²  with  a = −Rs c² / (2 r²)   (one step of a radial fall outside the horizon; returns r only, not the new speed; c = 299792458 m/s) | Ready | `physics/physics/schwarzschild_radial_step/` |
| Kerr outer horizon | r+ = Rs/2 + √((Rs/2)² − a²) | r+ = Rs/2 + √((Rs/2)² − a²)   (the larger horizon of a spinning mass; a = J/(M c) in metres; a = 0 gives r+ = Rs; |a| ≤ Rs/2) | Ready | `physics/physics/kerr_outer_horizon/` |
| Kerr inner horizon | r− = Rs/2 − √((Rs/2)² − a²) | r− = Rs/2 − √((Rs/2)² − a²)   (the smaller horizon of a spinning mass; a = J/(M c) in metres; a = 0 gives r− = 0; |a| ≤ Rs/2) | Ready | `physics/physics/kerr_inner_horizon/` |
| Kerr g_tφ | g_tφ = −Rs a / r | g_tφ = −Rs a / r   (the equator value of the frame-dragging coefficient of the Kerr metric; a = J/(M c) in metres; positive a gives a negative answer) | Ready | `physics/physics/kerr_frame_dragging_g_tphi/` |
| Lense–Thirring rate | Ω = 2GJ / (c² r³) | Ω = 2 G J / (c² r³)   (radians per second by which local inertial frames are dragged around a slowly spinning mass; G = 6.674e-11, c = 299792458; positive J is a right-hand spin) | Ready | `physics/physics/lense_thirring_rate/` |
| Gravitational-wave frequency | f_gw = 2 f_orb | f_gw = 2 f_orb   (a circular binary radiates at twice its orbital frequency) | Ready | `physics/physics/gravitational_wave_frequency/` |
| Chirp mass | (m1 m2)^(3/5) / (m1 + m2)^(1/5) | Mc = (m1 m2)^(3/5) / (m1 + m2)^(1/5)   (the mass combination that sets the leading gravitational wave) | Ready | `physics/physics/chirp_mass/` |
| Gravitational-wave strain | h = 4 (G Mc)^(5/3) (π f)^(2/3) / (c⁴ d) | h = 4 (G Mc)^(5/3) (π f)^(2/3) / (c⁴ d)   (leading-order amplitude of a face-on circular binary at distance d; f is the wave frequency, twice the orbital frequency; G = 6.674e-11, c = 299792458) | Ready | `physics/physics/gravitational_wave_strain/` |
| TOV pressure step | one shell of dP/dr | ΔP = −(G M ρ / r²) (1 + P/(ρ c²)) (1 + 4π r³ P / (M c²)) / (1 − 2GM/(r c²)) Δr   (the pressure change across one thin shell of a static spherical star, Tolman–Oppenheimer–Volkoff; M is the mass already inside r; G = 6.674e-11, c = 299792458) | Ready | `physics/physics/tov_pressure_step/` |
| Infinite-well transition | ΔE = (n₂² − n₁²) h² / (8 m L²) | ΔE = (n₂² − n₁²) h² / (8 m L²)   (the photon energy when a particle in a one-dimensional box drops from level n₂ to the lower level n₁; h = 6.62607015e-34 J s) | Ready | `physics/physics/infinite_well_transition/` |
| Infinite-well probability density | |ψ|² = (2/L) sin²(n π x / L) | |ψ|² = (2/L) sin²(n π x / L)   (the probability per metre of finding a particle in a one-dimensional box at x; the walls are at 0 and L) | Ready | `physics/physics/infinite_well_probability_density/` |
| Bohr radius | a = a₀ / Z | a = a₀ / Z   (a₀ = 5.29177210903e-11 m, the hydrogen Bohr radius; a nucleus of charge Z pulls it in to a₀/Z) | Ready | `physics/physics/bohr_radius/` |
| Electron Compton wavelength | λ = h / (m c) | λ = h / (m_e c)   (m_e = 9.1093837015e-31 kg, c = 299792458 m/s, h = 6.62607015e-34 J s; the wavelength itself, not the scattering shift) | Ready | `physics/physics/electron_compton_wavelength/` |
| Rectangular-barrier transmission | T = [1 + V² sinh²(κ L) / (4 E (V − E))]⁻¹ | T = [1 + V² sinh²(κ L) / (4 E (V − E))]⁻¹, κ = √(2 m (V − E)) / ħ   (the probability that a particle of mass m and energy E below a barrier of height V and thickness L gets through; ħ = 1.054571817e-34 J s unless another is passed) | Ready | `physics/physics/rectangular_barrier_transmission/` |
| Oscillator level gap | ΔE = ħ ω | ΔE = ħ ω   (the energy between neighbouring levels of a quantum harmonic oscillator; it does not depend on n; ħ = 1.054571817e-34 J s unless another is passed) | Ready | `physics/physics/oscillator_level_gap/` |
| Oscillator ground-state density | |ψ₀|² = √(m ω / (π ħ)) exp(−m ω x² / ħ) | |ψ₀|² = √(m ω / (π ħ)) exp(−m ω x² / ħ)   (the probability per metre of finding the particle at x in the ground state of a quantum harmonic oscillator; ħ = 1.054571817e-34 J s unless another is passed) | Ready | `physics/physics/oscillator_ground_density/` |
| Oscillator ground-state variance | ⟨x²⟩ = ħ / (2 m ω) | ⟨x²⟩ = ħ / (2 m ω)   (the mean of x is 0, so this is the spread of the ground state of a quantum harmonic oscillator, in square metres; ħ = 1.054571817e-34 J s unless another is passed) | Ready | `physics/physics/oscillator_ground_variance/` |
| Spin up along z | P(↑_z) | P(↑_z) = 1 if the spin-1/2 particle was prepared spin up along z, 0 if it was prepared spin down (the prepared value is 1 or −1) | Ready | `physics/physics/spin_z_up_probability/` |
| Spin up at an angle | P = (1 + cos θ) / 2 | P = (1 + cos θ) / 2 = cos²(θ/2)   (a spin-1/2 particle prepared spin up along z is found spin up along an axis at angle θ from z, in radians; the (1 + cos θ) / 2 form makes 90° exactly 0.5 and 180° exactly 0) | Ready | `physics/physics/spin_up_at_angle/` |
| Hydrogen mean radius | ⟨r⟩ = (a₀ / (2 Z)) [3 n² − l(l+1)] | ⟨r⟩ = (a₀ / (2 Z)) [3 n² − l(l+1)]   (the average distance of the electron from the nucleus in hydrogen or a one-electron ion, in metres; a₀ = 5.29177210903e-11 m is the hydrogen Bohr radius; it does not depend on the magnetic number) | Ready | `physics/physics/hydrogen_mean_radius/` |
| Fermi energy | E_F = (ħ² / 2 m) (3 π² n)^(2/3) | E_F = (ħ² / 2 m) (3 π² n)^(2/3)   (the Fermi energy in joules of a three-dimensional free-electron gas at zero temperature; n is the number of electrons per cubic metre; ħ = 1.054571817e-34 J s unless another is passed; not a band structure) | Ready | `physics/physics/fermi_energy/` |
| Momentum | p = mv | p = m v | Ready | `physics/physics/momentum/` |
| Impulse | J = FΔt | J = F Δt | Ready | `physics/physics/impulse/` |
| Work | W = Fd | W = F d   (force parallel to displacement) | Ready | `physics/physics/work/` |
| Power (Physics) | P = W/t | P = W / t | Ready | `physics/physics/power_physics/` |
| Kinetic energy | ½mv² | KE = ½ m v² | Ready | `physics/physics/kinetic_energy/` |
| Potential energy | mgh | PE = m g h | Ready | `physics/physics/potential_energy/` |
| Pressure | P = F/A | P = F / A | Ready | `physics/physics/pressure/` |
| Density | ρ = m/V | ρ = m / V | Ready | `physics/physics/density/` |
| Hooke's law | F = −kx | F = −k x | Ready | `physics/physics/hooke_s_law/` |
| Gravitation | F = G·m₁m₂/r² | F = G m₁ m₂ / r²   (G = 6.674×10⁻¹¹ N·m²/kg²) | Ready | `physics/physics/gravitation/` |
| Centripetal acceleration | a = v²/r | a = v² / r | Ready | `physics/physics/centripetal_acceleration/` |
| Torque | τ = rF·sin θ | τ = r F sin θ | Ready | `physics/physics/torque/` |
| Pendulum period | T = 2π√(L/g) | T = 2π √(L / g) | Ready | `physics/physics/pendulum_period/` |
| Frequency | f = 1/T | f = 1 / T | Ready | `physics/physics/frequency/` |
| Wave speed | v = fλ | v = f λ | Ready | `physics/physics/wave_speed/` |
| Snell's law | n₁sin θ₁ = n₂sin θ₂ | θ₂ = arcsin(n₁ sin θ₁ / n₂)   (angles in radians) | Ready | `physics/physics/snell_s_law/` |
| Heat | Q = mcΔT | Q = m c ΔT | Ready | `physics/physics/heat/` |
| Ideal gas law | PV = nRT | P = n R T / V   (R = 8.314 J/(mol·K)) | Ready | `physics/physics/ideal_gas_law/` |
| Mass-energy equivalence | E = mc² | E = m c²   (c = 299 792 458 m/s) | Ready | `physics/physics/mass_energy_equivalence/` |
| Ohm's law | V = IR | V = I R | Ready | `physics/physics/ohm_s_law/` |
| Electric power | P = IV | P = I V | Ready | `physics/physics/electric_power/` |
| Coulomb's law | F = k·q₁q₂/r² | F = k q₁ q₂ / r²   (k = 8.988×10⁹ N·m²/C²) | Ready | `physics/physics/coulomb_s_law/` |
| Capacitance | Q = CV | Q = C V | Ready | `physics/physics/capacitance/` |
| Resistors in series | R₁+R₂+… | R_total = R₁ + R₂ + … | Ready | `physics/physics/resistors_in_series/` |
| Resistors in parallel | 1/R = Σ 1/Rᵢ | 1 / R_total = 1/R₁ + 1/R₂ + … | Ready | `physics/physics/resistors_in_parallel/` |
| Magnetic force on a moving charge | F = qvB sin θ | F = q v B sin θ   (θ = angle between v and B, radians) | Ready | `physics/physics/magnetic_force_on_charge/` |
| Magnetic force on a current-carrying wire | F = BIL sin θ | F = B I L sin θ   (θ = angle between wire and B, radians) | Ready | `physics/physics/magnetic_force_on_wire/` |
| Magnetic field of a straight wire | B = μ₀I/2πr | B = μ₀ I / (2π r)   (μ₀ = 4π×10⁻⁷ T·m/A) | Ready | `physics/physics/magnetic_field_straight_wire/` |
| Magnetic field inside a solenoid | B = μ₀nI | B = μ₀ n I   (n = turns per metre, μ₀ = 4π×10⁻⁷ T·m/A) | Ready | `physics/physics/magnetic_field_solenoid/` |
| Magnetic flux | Φ = BA cos θ | Φ = B A cos θ   (θ = angle between B and the surface normal, radians) | Ready | `physics/physics/magnetic_flux/` |
| Faraday's law of induction | ε = −N ΔΦ/Δt | ε = −N ΔΦ / Δt | Ready | `physics/physics/faradays_law/` |
| Self-induced emf of an inductor | ε = −L ΔI/Δt | ε = −L ΔI / Δt | Ready | `physics/physics/self_induced_emf/` |
| Energy stored in an inductor | U = ½LI² | U = ½ L I² | Ready | `physics/physics/inductor_energy/` |
| Cyclotron radius of a charged particle | r = mv/(\|q\|B) | r = m v / (\|q\| B)   (charge moving perpendicular to B) | Ready | `physics/physics/cyclotron_radius/` |
| Motional emf | ε = BLv | ε = B L v   (rod of length L moving at speed v across B) | Ready | `physics/physics/motional_emf/` |
| Buoyant force (Archimedes' principle) | F = ρgV | F = ρ g V   (g = 9.81 m/s²) | Ready | `physics/physics/buoyant_force/` |
| Hydrostatic pressure | P = ρgh | P = ρ g h   (pressure due to the fluid alone, g = 9.81 m/s²) | Ready | `physics/physics/hydrostatic_pressure/` |
| Continuity equation | A₁v₁ = A₂v₂ | v₂ = A₁ v₁ / A₂   (incompressible fluid) | Ready | `physics/physics/continuity_equation/` |
| Bernoulli's equation | P + ½ρv² + ρgh = const | P₂ = P₁ + ½ρ(v₁² − v₂²) + ρg(h₁ − h₂)   (g = 9.81 m/s²) | Ready | `physics/physics/bernoulli_equation/` |
| Reynolds number | Re = ρvL/μ | Re = ρ v L / μ   (μ = dynamic viscosity) | Ready | `physics/physics/reynolds_number/` |
| Navier–Stokes equation | ρ(∂u/∂t + (u·∇)u) = −∇p + μ∇²u + f | ρ(∂u/∂t + (u·∇)u) = −∇p + μ∇²u + f   (incompressible flow, ∇·u = 0) | Reference | `physics/physics/navier_stokes_equation/` |
| Navier–Stokes: x momentum | ρ Du/Dt = −∂p/∂x + μ∇²u + fₓ | ρ(∂u/∂t + u ∂u/∂x + v ∂u/∂y + w ∂u/∂z) = −∂p/∂x + μ(∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z²) + f_x   (incompressible flow) | Reference | `physics/physics/navier_stokes_x_momentum/` |
| Navier–Stokes: y momentum | ρ Dv/Dt = −∂p/∂y + μ∇²v + f_y | ρ(∂v/∂t + u ∂v/∂x + v ∂v/∂y + w ∂v/∂z) = −∂p/∂y + μ(∂²v/∂x² + ∂²v/∂y² + ∂²v/∂z²) + f_y   (incompressible flow) | Reference | `physics/physics/navier_stokes_y_momentum/` |
| Navier–Stokes: z momentum | ρ Dw/Dt = −∂p/∂z + μ∇²w + f_z | ρ(∂w/∂t + u ∂w/∂x + v ∂w/∂y + w ∂w/∂z) = −∂p/∂z + μ(∂²w/∂x² + ∂²w/∂y² + ∂²w/∂z²) + f_z   (incompressible flow) | Reference | `physics/physics/navier_stokes_z_momentum/` |
| Navier–Stokes: continuity (incompressible) | ∇·u = 0 | ∂u/∂x + ∂v/∂y + ∂w/∂z = 0   (incompressible flow) | Reference | `physics/physics/navier_stokes_continuity/` |
| Poiseuille's law (flow in a pipe) | Q = πr⁴ΔP/8μL | Q = π r⁴ ΔP / (8 μ L)   (laminar flow in a round pipe) | Ready | `physics/physics/poiseuille_flow/` |
| Torricelli's law | v = √(2gh) | v = √(2 g h)   (g = 9.81 m/s²) | Ready | `physics/physics/torricelli_speed/` |
| Stokes' drag force | F = 6πμrv | F = 6π μ r v   (small sphere, slow flow) | Ready | `physics/physics/stokes_drag/` |
| Volume flow rate | Q = Av | Q = A v | Ready | `physics/physics/volume_flow_rate/` |
| Hydraulic press (Pascal's principle) | F₂ = F₁A₂/A₁ | F₂ = F₁ A₂ / A₁   (pressure is the same everywhere in the fluid) | Ready | `physics/physics/hydraulic_press/` |
| Photon energy (Planck's relation) | E = hf | E = h f   (h = 6.62607015×10⁻³⁴ J·s) | Ready | `physics/physics/photon_energy/` |
| Photon momentum | p = h/λ | p = h / λ   (h = 6.62607015×10⁻³⁴ J·s) | Ready | `physics/physics/photon_momentum/` |
| de Broglie wavelength | λ = h/mv | λ = h / (m v)   (h = 6.62607015×10⁻³⁴ J·s, non-relativistic) | Ready | `physics/physics/de_broglie_wavelength/` |
| Heisenberg uncertainty principle | Δx·Δp ≥ ħ/2 | Δp ≥ ħ / (2 Δx)   (returns the smallest possible Δp) | Ready | `physics/physics/heisenberg_uncertainty/` |
| Photoelectric effect | K = hf − φ | K_max = h f − φ   (0 if h f < φ: no electrons are ejected) | Ready | `physics/physics/photoelectric_effect/` |
| Bohr energy level (hydrogen-like atom) | Eₙ = −13.6 Z²/n² eV | Eₙ = −13.605693 eV × Z² / n²   (energy in electron-volts) | Ready | `physics/physics/bohr_energy_level/` |
| Rydberg formula | 1/λ = RZ²(1/n₁² − 1/n₂²) | λ = 1 / ( R Z² (1/n₁² − 1/n₂²) )   (n₂ > n₁, R = 1.0973731568×10⁷ /m) | Ready | `physics/physics/rydberg_formula/` |
| Particle in a box (energy levels) | Eₙ = n²h²/8mL² | Eₙ = n² h² / (8 m L²)   (h = 6.62607015×10⁻³⁴ J·s) | Ready | `physics/physics/particle_in_a_box/` |
| Quantum harmonic oscillator | Eₙ = ħω(n + ½) | Eₙ = ħ ω (n + ½)   (ω in rad/s) | Ready | `physics/physics/quantum_harmonic_oscillator/` |
| Compton wavelength shift | Δλ = (h/mc)(1 − cos θ) | Δλ = h / (m c) × (1 − cos θ)   (scattering off an electron by default) | Ready | `physics/physics/compton_shift/` |
| Thin lens equation | 1/f = 1/dₒ + 1/dᵢ | dᵢ = 1 / (1/f − 1/dₒ)   (returns the image distance, real-is-positive) | Ready | `physics/physics/thin_lens_equation/` |
| Lens magnification | m = −dᵢ/dₒ | m = −dᵢ / dₒ   (negative m means an inverted image) | Ready | `physics/physics/lens_magnification/` |
| Lensmaker's equation | 1/f = (n−1)(1/R₁ − 1/R₂) | f = 1 / ( (n − 1)(1/R₁ − 1/R₂) )   (thin lens in air) | Ready | `physics/physics/lensmakers_equation/` |
| Critical angle (total internal reflection) | θc = arcsin(n₂/n₁) | θc = arcsin(n₂ / n₁)   (n₁ > n₂, angle in radians) | Ready | `physics/physics/critical_angle/` |
| Brewster's angle | θB = arctan(n₂/n₁) | θB = arctan(n₂ / n₁)   (angle in radians) | Ready | `physics/physics/brewster_angle/` |
| Double-slit fringe spacing | Δy = λL/d | Δy = λ L / d   (small angles) | Ready | `physics/physics/double_slit_fringe_spacing/` |
| Diffraction grating | d sin θ = mλ | θ = arcsin(m λ / d)   (angle in radians) | Ready | `physics/physics/diffraction_grating/` |
| Malus's law | I = I₀cos²θ | I = I₀ cos²θ   (θ = angle between polariser axes, radians) | Ready | `physics/physics/malus_law/` |
| Refractive index | n = c/v | n = c / v   (c = 299 792 458 m/s) | Ready | `physics/physics/refractive_index/` |
| Lorentz factor | γ = 1/√(1 − v²/c²) | γ = 1 / √(1 − v²/c²)   (|v| < c) | Ready | `physics/physics/lorentz_factor/` |
| Relativistic kinetic energy: from the Lorentz factor | K = (γ − 1)mc² | K = (γ − 1) m c²   (γ is the answer of the row above) | Ready | `physics/physics/relativistic_kinetic_energy_from_gamma/` |
| Relativistic momentum: from the Lorentz factor | p = γmv | p = γ m v   (γ is the answer of the row above) | Ready | `physics/physics/relativistic_momentum_from_gamma/` |
| Length contraction: from the Lorentz factor | L = L₀/γ | L = L₀ / γ   (γ is the answer of the row above) | Ready | `physics/physics/length_contraction_from_gamma/` |
| Time dilation: from the Lorentz factor | Δt = γΔt₀ | Δt = Δt₀ γ   (γ is the answer of the row above) | Ready | `physics/physics/time_dilation_from_gamma/` |
| Time dilation | Δt = γΔt₀ | Δt = Δt₀ / √(1 − v²/c²)   (Δt₀ = time measured by the moving clock) | Ready | `physics/physics/time_dilation/` |
| Length contraction | L = L₀/γ | L = L₀ √(1 − v²/c²)   (L₀ = length at rest) | Ready | `physics/physics/length_contraction/` |
| Relativistic momentum | p = γmv | p = m v / √(1 − v²/c²) | Ready | `physics/physics/relativistic_momentum/` |
| Relativistic kinetic energy | K = (γ − 1)mc² | K = (γ − 1) m c²   (γ = 1/√(1 − v²/c²)) | Ready | `physics/physics/relativistic_kinetic_energy/` |
| Energy-momentum relation | E² = (pc)² + (mc²)² | E = √( (p c)² + (m c²)² )   (total energy) | Ready | `physics/physics/energy_momentum_relation/` |
| Relativistic velocity addition | u′ = (u + v)/(1 + uv/c²) | w = (u + v) / (1 + u v / c²) | Ready | `physics/physics/relativistic_velocity_addition/` |
| Relativistic Doppler effect | f = f₀√((1−β)/(1+β)) | f = f₀ √( (1 − β)/(1 + β) ),  β = v/c   (v > 0 receding, v < 0 approaching) | Ready | `physics/physics/relativistic_doppler/` |
| Relativistic Doppler: beta | β = v/c | β = v / c   (v > 0 receding, v < 0 approaching; the speed must be less than the speed of light) | Ready | `physics/physics/relativistic_beta/` |
| Relativistic Doppler: frequency | f = f₀√((1−β)/(1+β)) | f = f₀ √( (1 − β)/(1 + β) )   (β is the answer of the row above) | Ready | `physics/physics/relativistic_doppler_frequency/` |
| Schwarzschild radius | rₛ = 2GM/c² | rₛ = 2 G M / c²   (G = 6.674×10⁻¹¹ N·m²/kg²) | Ready | `physics/physics/schwarzschild_radius/` |
| Gravitational time dilation | Δt₀ = Δt√(1 − rₛ/r) | Δt₀ = Δt √(1 − 2GM/(r c²))   (clock at distance r from mass M, r > rₛ) | Ready | `physics/physics/gravitational_time_dilation/` |
| Gravitational time dilation: from the horizon | Δt₀ = Δt√(1 − rₛ/r) | Δt₀ = Δt √(1 − rₛ/r)   (rₛ is the answer of the row above; r > rₛ) | Ready | `physics/physics/gravitational_time_dilation_from_radius/` |
