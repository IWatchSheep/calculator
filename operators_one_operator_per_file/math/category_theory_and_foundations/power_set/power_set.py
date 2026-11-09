"""Power set   [𝒫(A)]

Category : Math > Category theory and foundations
Formula  : 𝒫(A) = set of all subsets of A;  |𝒫(A)| = 2^|A|

Status   : ready to use - call compute(A)
"""
import itertools

NAME = 'Power set'
SYMBOL = '𝒫(A)'
CATEGORY = 'Math'
SUBCATEGORY = 'Category theory and foundations'
FORMULA = '𝒫(A) = set of all subsets of A;  |𝒫(A)| = 2^|A|'


def compute(A):
    """𝒫(A) = set of all subsets of A;  |𝒫(A)| = 2^|A|"""
    return [set(c) for r in range(len(A) + 1) for c in itertools.combinations(A, r)]
