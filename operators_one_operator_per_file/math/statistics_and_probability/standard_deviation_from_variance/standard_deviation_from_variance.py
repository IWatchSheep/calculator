"""Standard deviation: from the variance   [σ = √(σ²)]

Category : Math > Statistics and probability
Formula  : σ = √(σ²)   (σ² is the answer of the row above)

Status   : ready to use - call compute(variance)
"""
import math

NAME = 'Standard deviation: from the variance'
SYMBOL = 'σ = √(σ²)'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'σ = √(σ²)   (σ² is the answer of the row above)'


def compute(variance):
    """σ = √(σ²)"""
    return math.sqrt(variance)
