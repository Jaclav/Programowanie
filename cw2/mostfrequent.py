#!/bin/python3

import sys
from collections import *
import numpy as np


def most_frequent(L: list) -> tuple[list, int]:
    tab = {}

    for l in L:
        if l in tab.keys():
            tab[int(l)] += 1
        else:
            tab[int(l)] = 1

    most_freq = []
    M = max(tab.values())
    for l in tab.keys():
        if tab[l] == M:
            most_freq.append(l)

    return (most_freq, M)


if __name__ == "__main__":
    A = np.array(sys.argv[1:]).astype(float)

    print(Counter(A).most_common())
    print(most_frequent(A))
