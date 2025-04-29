import numpy as np

def midpoint_rule(f, a, b, n):
    h = (b - a) / n
    total = 0
    for i in range(n):
        xi = a + h * (i + 0.5)
        total += f(xi)
    return h * total
