"""Standard deviation   [σ]

Category : Math > Statistics and probability
Formula  : σ = √(σ²)   (population)

Status   : ready to use - call compute(data)
"""
import statistics

NAME = 'Standard deviation'
SYMBOL = 'σ'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'σ = √(σ²)   (population)'


def compute(data):
    """σ = √(σ²)   (population)"""
    return statistics.pstdev(data)
