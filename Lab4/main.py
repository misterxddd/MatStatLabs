import sys

from Lab4.src.functions import functions_dict
from Lab4.src.kernel import research_kernel
from Lab4.src.empirical import research_empirical


if __name__ == '__main__':
    for name, _ in functions_dict.items():
        research_empirical(name)

    for name, _ in functions_dict.items():
        research_kernel(name)
