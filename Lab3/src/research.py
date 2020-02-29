import numpy as np
import seaborn as sns
import matplotlib.pyplot as plot

from .config import selection
from .characteristics import E, IQR
from .generate import random_generate_dict


def outliers_percent(x):
    length = x.size
    outliers_count = 0

    left_bound = np.quantile(x, 1 / 4) - 1.5 * IQR(x)
    right_bound = np.quantile(x, 3 / 4) + 1.5 * IQR(x)

    for i in range(0, length):
        if x[i] < left_bound or x[i] > right_bound:
            outliers_count += 1

    return outliers_count / length


def research(dist_type):
    print()
    print(dist_type + r"&\\ \hline")

    data = []

    for num in selection:
        outliers_arr = []
        arr = np.sort(random_generate_dict[dist_type](num))
        data.append(arr)

        for i in range(0, 1000):
            arr = np.sort(random_generate_dict[dist_type](num))
            outliers_arr.append(outliers_percent(arr))

        print("%-10s &" % ('n = %i' % num), end="")
        print(r"%-12f \\ \hline" % E(outliers_arr), end="")
        print()

    plot.figure(dist_type)
    plot.title(dist_type)
    sns.set(style="whitegrid")
    sns.boxplot(data=data, palette='rainbow', orient='h')
    plot.yticks(np.arange(2), ('20', '100'))
    plot.show()
