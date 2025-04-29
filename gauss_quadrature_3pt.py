import numpy as np

def gauss_quadrature_3pt(f, a, b):
    # Nodes and weights for 3-point Gauss-Legendre quadrature
    nodes = np.array([-0.7745966692, 0.0, 0.7745966692])
    weights = np.array([0.5555555556, 0.8888888889, 0.5555555556])
    
    # Change of variables to map from [-1,1] to [a,b]
    transformed_nodes = 0.5 * (b - a) * nodes + 0.5 * (b + a)
    integral = 0.5 * (b - a) * np.sum(weights * f(transformed_nodes))
    return integral
