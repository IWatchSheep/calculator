"""Normal distribution   [N(μ, σ²)]

Category : Math > Statistics and probability
Formula  : f(x) = e^(−(x−μ)² / 2σ²) / (σ√(2π))   (probability density)

Status   : ready to use - call compute(x, mu=0, sigma=1)
"""
import math

NAME = 'Normal distribution'
SYMBOL = 'N(μ, σ²)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'f(x) = e^(−(x−μ)² / 2σ²) / (σ√(2π))   (probability density)'


def compute(x, mu=0, sigma=1):
    """f(x) = e^(−(x−μ)² / 2σ²) / (σ√(2π))   (probability density)"""
    return math.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))
