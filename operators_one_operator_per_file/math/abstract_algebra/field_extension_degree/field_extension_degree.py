"""Field extension: degree   [[K:F]]

Category : Math > Abstract algebra
Formula  : [K:F] = dim_F K   (the dimension of K as a vector space over F)

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Field extension: degree'
SYMBOL = '[K:F]'
CATEGORY = 'Math'
SUBCATEGORY = 'Abstract algebra'
FORMULA = '[K:F] = dim_F K   (the dimension of K as a vector space over F)'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Field extension: degree is reference-only for now; see FORMULA.')
