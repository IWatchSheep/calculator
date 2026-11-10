"""Turn radius   [r = v² / (g tan φ)]

Category : Physics > Physics
Formula  : r = v² / (g tan φ)   (a level banked turn; φ in radians, positive to the left; a negative radius turns the other way; g = 9.81 m/s²)

Status   : ready to use - call compute(speed, bank, g=9.81)
"""
import math

NAME = 'Turn radius'
SYMBOL = 'r = v² / (g tan φ)'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'r = v² / (g tan φ)   (a level banked turn; φ in radians, positive to the left; a negative radius turns the other way; g = 9.81 m/s²)'


def compute(speed, bank, g=9.81):
    """r = v² / (g tan φ)"""
    if speed < 0:
        raise ValueError("speed cannot be negative")
    if bank == 0:
        raise ValueError("no bank, the turn radius is infinite")
    if abs(bank) >= math.pi / 2:
        raise ValueError("the bank is past horizontal")
    if g <= 0:
        raise ValueError("gravity must pull downward")
    return speed * speed / (g * math.tan(bank))
