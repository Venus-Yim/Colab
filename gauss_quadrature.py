def gaussian_quadrature(f, a, b, n):
    # 2-point Gauss-Legendre weights and nodes
    nodes = [-1/np.sqrt(3), 1/np.sqrt(3)]
    weights = [1, 1]
    h = (b - a) / n
    total = 0
    for i in range(n):
        xi = a + i * h
        xi1 = xi
        xi2 = xi + h
        for j in range(2):
            x = ((xi2 - xi1) / 2) * nodes[j] + (xi2 + xi1) / 2
            total += weights[j] * f(x)
    return total * h / 2