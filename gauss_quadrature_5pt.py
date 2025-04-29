import numpy as np
import sys
import datetime
import math
import csv

def f(x):
    return 10*np.sqrt(1 - (x**2) / 25)

def gauss_quadrature_5pt(f, a, b):
    # Nodes and weights for 5-point Gauss-Legendre quadrature
    nodes = np.array([-0.9061798459, -0.5384693101, 0.0, 0.5384693101, 0.9061798459])
    weights = np.array([0.2369268851, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268851])
    
    # Change of variables to map from [-1,1] to [a,b]
    transformed_nodes = 0.5 * (b - a) * nodes + 0.5 * (b + a)
    integral = 0.5 * (b - a) * np.sum(weights * f(transformed_nodes))
    return integral

def write_to_csv(data):
    with open('output8.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    start_time = datetime.datetime.now()
    area = gauss_quadrature_5pt(f,0,5)
    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    size_of_float = np.dtype(np.float64).itemsize
    memory_required = 3 * n_samples * size_of_float / (1024**3)
    error = abs(area-12.5*math.pi)/(12.5*math.pi)
    write_to_csv([n_samples, area, memory_required, elapsed_time, error])

if __name__ == '__main__':
    main()