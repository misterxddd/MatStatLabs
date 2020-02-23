import numpy as np

from .config import selection
from .characteristics import characteristics_dict, E, D
from .generate import random_generate_dict


def research(dist_type):
    print('-------------------------------------')
    print(dist_type)
    for num in selection:
        # print(num)
        print_table = {
            'E': [],
            'D': []
        }
        for char_name, char_func in characteristics_dict.items():
            z = []
            for i in range(0, 1000):
                arr = np.sort(random_generate_dict[dist_type](num))
                z.append(char_func(arr))

            print_table['E'].append(E(z))
            print_table['D'].append(D(z))

        print()
        print("%-10s;" % ('n = %i' % num), end="")
        for char_name, _ in characteristics_dict.items():
            print("%-12s;" % char_name, end="")

        print()
        print("%-10s;" % 'E =', end="")
        for e in print_table['E']:
            print("%-12f;" % e, end="")

        print()
        print("%-10s;" % 'D =', end="")
        for d in print_table['D']:
            print("%-12f;" % d, end="")
        print()
