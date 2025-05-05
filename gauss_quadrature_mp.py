import sys
import datetime
import csv
from mpmath import mp, mpf, quadgl
import math

# 设置高精度小数位数（例如 60 位）
mp.dps = 30

# 精确积分值（用于误差计算）
true_value = mp.mpf('12.5') * mp.pi

# 被积函数定义
def f(x):
    return 10 * np.sqrt(1 - (x**2) / 25)

# 复合高斯-勒让德求积（使用 mpmath）
def composite_gauss_quadrature(f, a, b, n_intervals, n_points):
    a = mpf(a)
    b = mpf(b)
    h = (b - a) / n_intervals
    total = mpf(0)
    
    for i in range(n_intervals):
        sub_a = a + i * h
        sub_b = sub_a + h
        integral = quadgl(f, [sub_a, sub_b], n=n_points)
        total += integral

    return total

# 写入 CSV 文件
def write_to_csv(data, n_points):
    with open(f'output{n_points + 3}mp2.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# 主程序入口
def main(n_samples, k):
    start_time = datetime.datetime.now()
    
    area = composite_gauss_quadrature(f, 0, 5, n_samples, k)
    
    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()

    # 估算内存（mpmath 的对象占内存无法精确估算，这里保留原公式）
    size_of_float = 8  # 假设每 float64 是 8 字节，仅供近似参考
    memory_required = 3 * n_samples * size_of_float / (1024**3)  # GiB

    # 误差
    error = abs(area - true_value) / true_value

    # 写入数据
    write_to_csv([n_samples, str(area), memory_required, elapsed_time, str(error)], k)


if __name__ == '__main__':
    n_samples = int(sys.argv[1])
    k = int(sys.argv[2])
    main(n_samples, k)
