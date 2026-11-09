"""Pullback   [f*]

Category : Math > Differential geometry and tensors
Formula  : (f*ω)(v) = ω(df(v))

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Pullback'
SYMBOL = 'f*'
CATEGORY = 'Math'
SUBCATEGORY = 'Differential geometry and tensors'
FORMULA = '(f*ω)(v) = ω(df(v))'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Pullback is reference-only for now; see FORMULA.')
