"""Sample variance   [s²]

Category : Math > Statistics and probability
Formula  : s² = Σ(xᵢ − x̄)² / (n − 1)

Status   : ready to use - call compute(data)
"""
import statistics

NAME = 'Sample variance'
SYMBOL = 's²'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 's² = Σ(xᵢ − x̄)² / (n − 1)'


def compute(data):
    """s² = Σ(xᵢ − x̄)² / (n − 1)"""
    return statistics.variance(data)
