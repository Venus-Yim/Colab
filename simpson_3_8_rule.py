def simpson_3_8_rule(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 rule.")
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        if i % 3 == 0:
            weight = 2
        else:
            weight = 3
        total += weight * f(xi)
    return 3 * h * total / 8
