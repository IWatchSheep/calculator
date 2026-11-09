"""Wave speed   [v = fλ]

Category : Physics > Physics
Formula  : v = f λ

Status   : ready to use - call compute(f, wavelength)
"""

NAME = 'Wave speed'
SYMBOL = 'v = fλ'
CATEGORY = 'Physics'
SUBCATEGORY = 'Physics'
FORMULA = 'v = f λ'


def compute(f, wavelength):
    """v = f λ"""
    return f * wavelength
