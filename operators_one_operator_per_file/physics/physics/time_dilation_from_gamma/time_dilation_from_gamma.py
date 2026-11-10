"""Time dilation: from the Lorentz factor   [Δt = γΔt₀]

Category : Physics > Physics
Formula  : Δt = Δt₀ γ   (γ is the answer of the row above)

Status   : ready to use - call compute(dt0, gamma)
"""

NAME = 'Time dilation: from the Lorentz factor'
SYMBOL = 'Δt = γΔt₀'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'Δt = Δt₀ γ   (γ is the answer of the row above)'


def compute(dt0, gamma):
    """Δt = Δt₀ γ"""
    return dt0 * gamma
