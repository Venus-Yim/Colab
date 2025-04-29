import numpy as np
import sys
import datetime
import math
import csv

def gauss_quadrature_4pt(f, a, b):
    # Nodes and weights for 4-point Gauss-Legendre quadrature
    nodes = np.array([-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116])
    weights = np.array([0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451])
    
    # Change of variables to map from [-1,1] to [a,b]
    transformed_nodes = 0.5 * (b - a) * nodes + 0.5 * (b + a)
    integral = 0.5 * (b - a) * np.sum(weights * f(transformed_nodes))
    return integral

def write_to_csv(data):
    with open('output7.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    start_time = datetime.datetime.now()
    area = gauss_quadrature_4pt(f,0,5)
    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    size_of_float = np.dtype(np.float64).itemsize
    memory_required = 3 * n_samples * size_of_float / (1024**3)
    error = abs(area-12.5*math.pi)/(12.5*math.pi)
    write_to_csv([n_samples, area, memory_required, elapsed_time, error])

if __name__ == '__main__':
    main()