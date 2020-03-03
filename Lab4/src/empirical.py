import numpy as np
import matplotlib.pyplot as plot

from .config import selection
from .cumulative_functions import cumulative_func_dict
from .generate import random_generate_dict


def empirical_function(sample, x):
    counter_array = []
    n = len(sample)
    m = len(x)
    for i in range(m):
        counter_array.append(0)

    for i in range(m):
        for j in range(n):
            if sample[j] < x[i]:
                counter_array[i] = counter_array[i] + 1
        counter_array[i] = counter_array[i] / n
    return counter_array


def draw_empirical(sample, func, sector, num):
    ax = plot.subplot(130+sector)
    ax.set_title(f'n = {num}')
    if func == 'poisson':
        xx = np.linspace(6, 14, 100)
    else:
        xx = np.linspace(-4, 4, 100)
    plot.plot(xx, cumulative_func_dict[func](xx), 'b')
    plot.plot(xx, empirical_function(sample, xx), 'r')
    

def research_empirical(dist_type):
    plot.figure("distribution " + dist_type)
    sector = 1
    for num in selection:
        sample = random_generate_dict[dist_type](num)
        draw_empirical(sample, dist_type, sector, num)
        sector += 1
    plot.show()

