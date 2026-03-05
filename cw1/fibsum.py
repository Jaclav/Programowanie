#!/usr/bin/python3
# %%
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

n = int(sys.argv[1])

s = 0
if True:
    F = [np.nan, 1, 1]
    for i in range(3, n + 1):
        F.append(F[i - 1] + F[i - 2])
        if i % 2 == 0:
            s += F[-1]

        if F[-1] >= 3e6:
            print(s)
            break

print(s)
