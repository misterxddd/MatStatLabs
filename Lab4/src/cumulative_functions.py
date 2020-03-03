import numpy as np

from scipy.stats import norm
from scipy.stats import laplace
from scipy.stats import uniform
from scipy.stats import poisson

from .config import LAPLACE_COEF, POISSON_PARAM


def cumulative_laplace(x):
    return laplace.cdf(x, 0, 1 / LAPLACE_COEF)


def cumulative_poisson(x):
    return poisson.cdf(x, POISSON_PARAM)


def cumulative_cauchy(x):
    return (1/np.pi) * np.arctan(x) + 0.5


def cumulative_uniform(x):
    return uniform.cdf(x, -4, 8)


cumulative_func_dict = {
    'normal': norm.cdf,
    'laplace': cumulative_laplace,
    'uniform': cumulative_uniform,
    'cauchy': cumulative_cauchy,
    'poisson': cumulative_poisson
}