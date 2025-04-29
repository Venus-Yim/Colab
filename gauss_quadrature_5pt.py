def gauss_quadrature_5pt(f, a, b):
    # Nodes and weights for 5-point Gauss-Legendre quadrature
    nodes = np.array([-0.9061798459, -0.5384693101, 0.0, 0.5384693101, 0.9061798459])
    weights = np.array([0.2369268851, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268851])
    
    # Change of variables to map from [-1,1] to [a,b]
    transformed_nodes = 0.5 * (b - a) * nodes + 0.5 * (b + a)
    integral = 0.5 * (b - a) * np.sum(weights * f(transformed_nodes))
    return integral