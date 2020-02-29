import numpy as np


def E(arr):
    return np.mean(arr)


def IQR(x):
    return np.abs(np.quantile(x, 1 / 4) - np.quantile(x, 3 / 4))
