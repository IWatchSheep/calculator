"""Variance   [σ²]

Category : Math > Statistics and probability
Formula  : σ² = Σ(xᵢ − μ)² / n   (population)

Status   : ready to use - call compute(data)
"""
import statistics

NAME = 'Variance'
SYMBOL = 'σ²'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'σ² = Σ(xᵢ − μ)² / n   (population)'


def compute(data):
    """σ² = Σ(xᵢ − μ)² / n   (population)"""
    return statistics.pvariance(data)
