import numpy as np
import matplotlib.pyplot as plt
import time


def escape(z, c, z_max, n_max):
    i = 0
    z_max2 = z_max * z_max
    while norm2(z) < z_max2 and i < n_max:
        z = z * z + c
        i += 1
    return i


def norm2(z):
    return z.real * z.real + z.imag * z.imag


def calc_mandelbrot(resolution, bound=1.2, z_max=2.0, n_max=500):
    step = 2.0 * bound / resolution
    counts = np.zeros((resolution+1, resolution+1), dtype=np.int32)

    for i in range(resolution+1):
        imag = bound - i * step
        for j in range(resolution+1):
            real = -bound + j * step - 0.5
            w = real + imag * 1j
            counts[i, j] = escape(w, w, z_max, n_max)

    return np.asarray(counts)


def mandelbrot():
    tm_start = time.time()
    n = calc_mandelbrot(1000)
    tm_end = time.time()

    plt.figure(figsize=(10, 10))
    plt.imshow(np.log(n+1))
    print("time={}".format(tm_end-tm_start))
    plt.show()


if __name__ == '__main__':
    mandelbrot()
