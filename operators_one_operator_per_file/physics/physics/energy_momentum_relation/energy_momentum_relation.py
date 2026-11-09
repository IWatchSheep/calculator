"""Energy-momentum relation   [E² = (pc)² + (mc²)²]

Category : Physics > Physics
Formula  : E = √( (p c)² + (m c²)² )   (total energy)

Status   : ready to use - call compute(m, p, c)
"""
import math

NAME = 'Energy-momentum relation'
SYMBOL = 'E² = (pc)² + (mc²)²'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'E = √( (p c)² + (m c²)² )   (total energy)'


def compute(m, p, c=299792458):
    """E = √( (p c)² + (m c²)² )   (total energy)"""
    return math.sqrt((p * c) ** 2 + (m * c ** 2) ** 2)
