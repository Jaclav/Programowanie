#!/bin/python3
# %%
import numpy as np
import sys
from typing import Self
from typing import Literal


class Inf(float):
    def __new__(cls):
        return super().__new__(cls, np.inf)


class Circle:
    _x, _y, _r = 0.0, 0.0, 0.0

    def __init__(self, x: float, y: float, r: float):
        assert r > 0
        self._x = x
        self._y = y
        self._r = r

    def Circumference(self) -> float:
        return 2 * np.pi * self._r

    def getX(self) -> float:
        return self._x

    def getY(self) -> float:
        return self._y

    def getR(self) -> float:
        return self._r

    def Intersection(self, other: Self) -> Literal[-1, 0, 1, 2] | Inf:
        d = np.sqrt((self._x - other.getX()) ** 2 + (self._y - other.getY()) ** 2)

        if d > self._r + other.getR() or d < np.abs(self._r - other.getR()):
            return 0
        elif d == self._r + other.getR() or d == np.abs(self._r - other.getR()):
            if (
                self._x == other.getX()
                and self._y == other.getY()
                and self._r == other.getR()
            ):
                return Inf()
            else:
                return 1
        elif np.abs(self._r - other.getR()) < d < self._r + other.getR():
            return 2

        return -1


if __name__ == "__main__":
    c1 = Circle(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    c2 = Circle(float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]))

    print(c1.Intersection(c2))
    print(c2.Intersection(c1))

    print(Inf() == np.inf)
