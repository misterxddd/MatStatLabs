import numpy as np

from .config import LAPLACE_COEF, UNIFORM_LEFT, UNIFORM_RIGHT, POISSON_PARAM


def standard_normal(x):
    return (1 / np.sqrt(2*np.pi)) * np.exp(- x * x / 2)


def standard_cauchy(x):
    return 1 / (np.pi * (1 + x*x))


def laplace(x):
    return 1 / LAPLACE_COEF * np.exp(-LAPLACE_COEF * np.abs(x))


def uniform(x):
    flag2 = x <= UNIFORM_RIGHT
    flag1 = x >= UNIFORM_LEFT
    return 1 / (UNIFORM_RIGHT - UNIFORM_LEFT) * flag1 * flag2


def poisson(x):
    return (np.power(x, POISSON_PARAM) / np.math.factorial(k)) * np.exp(-x)


functions_dict = {
    'normal': standard_normal,
    'cauchy': standard_cauchy,
    'laplace': laplace,
    'poisson': poisson,
    'uniform': uniform,
}
