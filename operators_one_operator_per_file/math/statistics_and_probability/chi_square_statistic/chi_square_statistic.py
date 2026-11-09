"""Chi-square statistic   [χ²]

Category : Math > Statistics and probability
Formula  : χ² = Σ (Oᵢ − Eᵢ)² / Eᵢ

Status   : ready to use - call compute(observed, expected)
"""

NAME = 'Chi-square statistic'
SYMBOL = 'χ²'
CATEGORY = 'Math'
SUBCATEGORY = 'Statistics and probability'
FORMULA = 'χ² = Σ (Oᵢ − Eᵢ)² / Eᵢ'


def compute(observed, expected):
    """χ² = Σ (Oᵢ − Eᵢ)² / Eᵢ"""
    return sum((o - e) ** 2 / e for o, e in zip(observed, expected))
