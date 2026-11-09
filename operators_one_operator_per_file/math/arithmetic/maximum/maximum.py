"""Maximum   [max]

Category : Math > Arithmetic
Formula  : max(a, b, …) = largest value

Status   : ready to use - call compute(*values)
"""

NAME = 'Maximum'
SYMBOL = 'max'
CATEGORY = 'Math'
SUBCATEGORY = 'Arithmetic'
FORMULA = 'max(a, b, …) = largest value'


def compute(*values):
    """max(a, b, …) = largest value"""
    return max(values)
