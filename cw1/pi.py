#!/usr/bin/python3
# %%
from math import factorial
import sys
import numpy as np
import matplotlib.pyplot as plt


def arctg(x: float, N: int) -> float:
    s = 0
    for n in range(0, N + 1):
        s += (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
    return s


N = int(sys.argv[1])
K = list(range(0, N + 1))

Y = []
for i, k in enumerate(K):
    Y.append(16 * arctg(1 / 5, k) - 4 * arctg(1 / 239, k))

plt.plot(K, np.pi * np.ones(N + 1), label="$\\pi$")
plt.plot(K, Y, label="approx")
plt.legend()
plt.title("Oszacowanie $\\pi$ w funkcji K, dla %d elementów: %.3f" % (N, Y[-1]))
plt.xlabel("K")
plt.show()
