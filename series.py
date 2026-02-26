#!/usr/bin/python3
# %%
from math import factorial
import sys


def sum_a(x: float, n: int):
    s = 0
    for k in range(0, n + 1):
        s += x**k / factorial(k)
    return s


def sum_b(x: float, n: int):
    s = 0
    for k in range(0, n + 1):
        s += (-1) ** k * x ** (2 * k) / (factorial(2 * k))
    return s


if __name__ == "__main__":
    x = float(sys.argv[1])
    n = int(sys.argv[2])
    print(sum_a(x, n))
    print(sum_b(x, n))