"""Photoelectric effect   [K = hf − φ]

Category : Physics > Physics
Formula  : K_max = h f − φ   (0 if h f < φ: no electrons are ejected)

Status   : ready to use - call compute(f, work_function, h)
"""
import math

NAME = 'Photoelectric effect'
SYMBOL = 'K = hf − φ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'K_max = h f − φ   (0 if h f < φ: no electrons are ejected)'


def compute(f, work_function, h=6.62607015e-34):
    """K_max = h f − φ   (0 if h f < φ: no electrons are ejected)"""
    return max(0.0, h * f - work_function)
