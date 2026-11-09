"""Open bracket   [(]

Category : Math > Constants and relations
Formula  : ( begins a group; what is inside is evaluated first

Status   : reference only (no calculation is wired up yet)
"""

NAME = 'Open bracket'
SYMBOL = '('
CATEGORY = 'Math'
SUBCATEGORY = 'Constants and relations'
FORMULA = '( begins a group; what is inside is evaluated first'


def compute(*args, **kwargs):
    """Reference only: see FORMULA above."""
    raise NotImplementedError('Open bracket is reference-only for now; see FORMULA.')
