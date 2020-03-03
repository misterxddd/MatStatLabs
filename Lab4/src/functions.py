import numpy as np

from .config import LAPLACE_COEF, UNIFORM_FRONT, POISSON_PARAM


def standard_normal(x):
    return (1 / np.sqrt(2*np.pi)) * np.exp(- x * x / 2)


def standard_cauchy(x):
    return 1 / (np.pi * (1 + x*x))


def laplace(x):
    return 1 / LAPLACE_COEF * np.exp(-LAPLACE_COEF * np.abs(x))


def uniform(x):
    flag = (x <= UNIFORM_FRONT)
    return 1 / (2 * UNIFORM_FRONT) * flag


def poisson(x):
    n = x.size
    res = []
    for i in range(n):
        res.append(0)

    for i in range(n):
        res[i] = (1 / np.power(np.e, POISSON_PARAM)) / np.math.factorial(int(x[i])) * np.power(POISSON_PARAM, int(x[i]))
    return res


functions_dict = {
    'normal': standard_normal,
    'cauchy': standard_cauchy,
    'laplace': laplace,
    'poisson': poisson,
    'uniform': uniform,
}