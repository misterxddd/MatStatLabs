import numpy as np
import matplotlib.pyplot as plot

from .config import selection, smoothing_params
from .functions import standard_normal, functions_dict
from .generate import random_generate_dict


def kernel_function(sample, h, x):
    res_array = []
    n = len(sample)
    m = len(x)

    for i in range(m):
        res_array.append(0)

    for i in range(m):
        for j in range(n):
            res_array[i] += standard_normal((x[i] - sample[j]) / h)
        res_array[i] = res_array[i] / (n * h)

    return res_array


def draw_kernel(sample, func, sector, h, num):
    if sector == 3:
        plot.title(f'n = {num}. Distribution: {func}. h = [0.5*h_n, h_n, 2*h_n].')
    plot.subplot(130+sector)
    if func == 'poisson':
        xx = np.linspace(6, 14, 100)
    else:
        xx = np.linspace(-4, 4, 100)
    plot.plot(xx, functions_dict[func](xx), 'r')
    plot.plot(xx, kernel_function(sample, h,  xx), 'black')


def research_kernel(dist_type):
    sector = 1
    for num in selection:
        sample = random_generate_dict[dist_type](num)
        plot.figure("distribution " + dist_type + f'n = {num}', (11, 7))
        for h in smoothing_params:
            draw_kernel(sample, dist_type, sector, h, num)
            sector += 1
        sector = 1
    plot.show()
