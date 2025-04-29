import numpy as np
import sys
import datetime
import math
import csv

def f(x):
    return 10*np.sqrt(1 - (x**2) / 25)


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

def write_to_csv(data):
    with open('output5.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main(n_samples):
    start_time = datetime.datetime.now()
    area = gaussian_quadrature(f,0,5,n_samples)
    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    size_of_float = np.dtype(np.float64).itemsize
    memory_required = 3 * n_samples * size_of_float / (1024**3)
    error = abs(area-12.5*math.pi)/(12.5*math.pi)
    write_to_csv([n_samples, area, memory_required, elapsed_time, error])

if __name__ == '__main__':
    n_samples = int(sys.argv[1])
    main(n_samples)