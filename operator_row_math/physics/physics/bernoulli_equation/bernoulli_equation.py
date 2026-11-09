"""Row for the operator: Bernoulli's equation

Picture:      □ = □ + ½ × □ × (□² − □²) + □ × g × (□ − □)
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/bernoulli_equation
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = "Bernoulli's equation"
KEY = 'physics/physics/bernoulli_equation'
PATTERN = '□ = □ + ½ × □ × (□² − □²) + □ × g × (□ − □)'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['P1', 'v1', 'h1', 'v2', 'h2', 'rho']    # what each box (left to right) is
KINDS = ['number', 'number', 'number', 'number', 'number', 'number']    # what to type in each box (see advanced_input.KINDS)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('op', "Bernoulli's equation("), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ','), ('box', ''), ('op', ')')]      # cards left of "="
RIGHT = [('box', ''), ('op', '+ ½ ×'), ('box', ''), ('op', '× ('), ('box', ''), ('op', '² −'), ('box', ''), ('op', '²) +'), ('box', ''), ('op', '× g × ('), ('box', ''), ('op', '−'), ('box', ''), ('op', ')')]    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked)
