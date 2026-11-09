"""Partition number   [p(n)]

Category : Math > Graph theory and combinatorics
Formula  : p(n) = number of ways to write n as a sum of positive integers (order ignored)

Status   : ready to use - call compute(n)
"""

NAME = 'Partition number'
SYMBOL = 'p(n)'
CATEGORY = 'Math'
SUBCATEGORY = 'Graph theory and combinatorics'
FORMULA = 'p(n) = number of ways to write n as a sum of positive integers (order ignored)'


def compute(n):
    """p(n) = number of ways to write n as a sum of positive integers (order ignored)"""
    p = [1] + [0] * n
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            p[i] += p[i - k]
    return p[n]
