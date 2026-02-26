#!/usr/bin/python3
# %%
import time
import sys
import numpy as np
import matplotlib.pyplot as plt


def fibi(n: int) -> int:
    if n <= 2:
        return 1
    F = [np.nan, 1, 1]
    for i in range(3, n + 1):
        F.append(F[i - 1] + F[i - 2])
    return F[-1]


def fibr(n: int) -> int:
    if n <= 2:
        return 1
    return fibr(n - 1) + fibr(n - 2)

if __name__=='__main__':
    N = int(sys.argv[1])
    n = list(range(0, N + 1))

    print(fibi(N))
    print(fibr(N))
