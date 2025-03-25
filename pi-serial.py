import numpy as np
import sys
import datetime
import math

def inside_circle(total_count):
    x = np.random.uniform(size=total_count)
    y = np.random.uniform(size=total_count)
    radii = np.sqrt(x*x + y*y)
    count = len(radii[np.where(radii<=1.0)])
    return count

def write_to_csv(data):
    with open('output.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main(n_samples):
    start_time = datetime.datetime.now()
    counts = inside_circle(n_samples)
    my_pi = 4.0 * counts / n_samples
    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    size_of_float = np.dtype(np.float64).itemsize
    memory_required = 3 * n_samples * size_of_float / (1024**3)
    error = my_pi-math.pi
    write_to_csv([n_samples, my_pi, memory_required, elapsed_time, error])

if __name__ == '__main__':
    n_samples = int(sys.argv[1])
    main(n_samples)
