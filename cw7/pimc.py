#!/bin/python3

# import ctypes#ctypes.c_ulong
import sys


class LCG:
    __x_nth, __a, __b, __m = 0, 0, 0, 0

    def __init__(self, x0: int, a: int, b: int, m: int):
        assert a < m and b < m
        assert a >= 0 and b >= 0 and m >= 0
        self.__x_nth = x0
        self.__a = a
        self.__b = b
        self.__m = m

    def __call__(self) -> int:
        self.__x_nth = (self.__a * self.__x_nth + self.__b) % self.__m
        return self.__x_nth

    @property
    def min(self):
        return 1 if self.__m == 0 else 0

    @property
    def max(self):
        return self.__m - 1


if __name__ == "__main__":
    M = 100000000000
    l = LCG(53249, 1664525, 1013904223, M + 1)
    print(l.min, l.max)
    N = int(sys.argv[1])
    k = 0
    for i in range(0, N):
        x, y = l() / M, l() / M
        if x**2 + y**2 <= 1:
            k += 1
    print(4 * k / N)
