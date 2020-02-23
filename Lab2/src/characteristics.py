import numpy as np


def E(arr):
    return np.mean(arr)


def D(arr):
    return np.var(arr)


def Zr(x):
    return (np.amin(x) + np.amax(x)) / 2


def Zq(x):
    return (np.quantile(x, 1/4) + np.quantile(x, 3/4)) / 2


def Ztr(x):
    n = x.size
    r = int(n / 4)
    amount = 0
    for i in range(r, n - r):
        amount += x[i + 1]
    return amount / (n - 2 * r)


characteristics_dict = {
    'average': np.mean,
    'med': np.median,
    'Zr': Zr,
    'Zq': Zq,
    'Ztr': Ztr
}