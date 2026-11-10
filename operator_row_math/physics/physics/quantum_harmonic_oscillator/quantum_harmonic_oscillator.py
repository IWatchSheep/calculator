"""Row for the operator: Quantum harmonic oscillator

Picture:      □ = ħ × □ × ( □ + ½ )
Calculation:  ready - fill the boxes, press = and the sum appears right of =
Try it:       python operator_row_math/preview.py physics/physics/quantum_harmonic_oscillator
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from operator_row_math.row_builder import build_row  # noqa: E402

NAME = 'Quantum harmonic oscillator'
KEY = 'physics/physics/quantum_harmonic_oscillator'
PATTERN = '□ = ħ × □ × ( □ + ½ )'
# "ready"     = the boxes on the left feed compute() and the sum shows right of "="
# "reference" = formula only (no calculation yet)
# "advanced"  = needs a list / matrix / function / set / graph: use the Advanced Input window
CALC = 'ready'
INPUTS = ['n', 'omega']    # what each box (left to right) is
KINDS = ['number', 'number']    # what to type in each box (see advanced_input.KINDS)
SLOTS = [1, 0]    # which input each box of LEFT shows (an input the picture writes twice has two boxes that share one value)
# ("box", "")  = small square box card      ("op", text) = operator card
LEFT = [('out', ''), ('op', '='), ('op', 'ħ'), ('op', '×'), ('box', ''), ('op', '×'), ('op', '('), ('box', ''), ('op', '+'), ('op', '½'), ('op', ')')]      # cards left of "="
RIGHT = []    # cards right of "="  (the result box = Row 1's number card)


def place(parent, stacked=False):
    """Create this operator's row inside `parent` and return the Frame (caller grids/packs it)."""
    return build_row(parent, LEFT, RIGHT, stacked, levels=globals().get("LEVELS"))
