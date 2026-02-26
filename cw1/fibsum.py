#!/usr/bin/python3
# %%
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

n = int(sys.argv[1])

s=0
for i in range(0,n+1)
    if n <= 2:
        s+=1
    F = [np.nan, 1, 1]
    for i in range(3, n + 1):
        F.append(F[i - 1] + F[i - 2])
    s+=F[-1]