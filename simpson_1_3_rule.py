def simpson_1_3_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 rule.")
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        weight = 4 if i % 2 != 0 else 2
        total += weight * f(xi)
    return h * total / 3
