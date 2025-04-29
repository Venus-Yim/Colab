def gauss_quadrature_4pt(f, a, b):
    # Nodes and weights for 4-point Gauss-Legendre quadrature
    nodes = np.array([-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116])
    weights = np.array([0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451])
    
    # Change of variables to map from [-1,1] to [a,b]
    transformed_nodes = 0.5 * (b - a) * nodes + 0.5 * (b + a)
    integral = 0.5 * (b - a) * np.sum(weights * f(transformed_nodes))
    return integral
