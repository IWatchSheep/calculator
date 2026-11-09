"""Laurent series   [Σ aₙ (z−a)ⁿ]

Category : Math > Complex analysis
Formula  : f(z) = Σ_{n=−∞}^{∞} aₙ (z − a)ⁿ

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Laurent series'
SYMBOL = 'Σ aₙ (z−a)ⁿ'
CATEGORY = 'Math'
SUBCATEGORY = 'Complex analysis'
FORMULA = 'f(z) = Σ_{n=−∞}^{∞} aₙ (z − a)ⁿ'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Laurent series is reference-only for now; see FORMULA.')
