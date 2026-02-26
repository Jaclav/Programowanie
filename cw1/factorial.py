#!/usr/bin/python3
# %%
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
from ifactorial import ifactorial
from rfactorial import rfactorial


def factorial(n: int):
    start_time = time.time()
    fi = ifactorial(n)
    ti = time.time() - start_time

    start_time = time.time()
    fr = rfactorial(n)
    tr = time.time() - start_time

    return (fi, ti, fr, tr)


N = int(sys.argv[1])
n = list(range(0, N + 1))
Y = []
for i in n:
    Y.append(factorial(i))

Y=np.array(Y)
# print(Y[:,3])

plt.plot(n,Y[:,1],label="iterative")
plt.plot(n,Y[:,3],label="recursive")
plt.legend()
plt.xlabel("N")
plt.ylabel("T [s]")
plt.plot()
plt.show()