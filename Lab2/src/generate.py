import numpy as np

from .config import LAPLACE_COEF, UNIFORM_LEFT, UNIFORM_RIGHT, POISSON_PARAM


def generate_laplace(x):
    return np.random.laplace(0, 1/LAPLACE_COEF, x)


def generate_uniform(x):
    return np.random.uniform(UNIFORM_LEFT, UNIFORM_RIGHT, x)


def generate_poisson(x):
    return np.random.poisson(POISSON_PARAM, x)


random_generate_dict = {
    'normal': np.random.standard_normal,
    'cauchy': np.random.standard_cauchy,
    'laplace': generate_laplace,
    'poisson': generate_poisson,
    'uniform': generate_uniform,
}
