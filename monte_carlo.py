import numpy as np
import sys
import datetime
import math
import csv

def f(x):
    return x**5 - 5*x**4 + 10*x**3 - 10*x**2 + 5*x - 1

def monte_carlo(f, a, b, n_samples):
    x_random = np.random.uniform(a, b, n_samples)
    y_values = f(x_random)
    average_value = np.mean(y_values)
    return (b - a) * average_value

def write_to_csv(data):
    with open('output9.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main(n_samples):
    start_time = datetime.datetime.now()
    area = monte_carlo(f, 0, 5, n_samples)
    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    size_of_float = np.dtype(np.float64).itemsize
    memory_required = 2 * n_samples * size_of_float / (1024**3)
    exact_value = 682.5
    error = abs(area - exact_value) / exact_value
    write_to_csv([n_samples, area, memory_required, elapsed_time, error])

if __name__ == '__main__':
    n_samples = int(sys.argv[1])
    main(n_samples)
