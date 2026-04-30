#!/bin/python3
from typing import List
from abc import ABC, abstractmethod
from numpy import abs


class Mean(ABC):
    _x: List[float] = []

    def __init__(self, l: List[float]):
        self._x = l

    def N(self) -> float:
        return len(self._x)

    @abstractmethod
    def __call__(self) -> float:
        pass


class ArithmeticMean(Mean):
    def __call__(self) -> float:
        sum: float = 0
        for e in self._x:
            sum += e
        return sum / self.N()


class GeometricMean(Mean):
    def __call__(self) -> float:
        s: float = 1
        for e in self._x:
            s *= e
        return (abs(s)) ** (1 / self.N())


class HarmonicMean(Mean):
    def __call__(self) -> float:
        sum: float = 0
        for e in self._x:
            assert e != 0
            sum += 1 / e
        return self.N() / sum


if __name__ == "__main__":
    a = ArithmeticMean([1, 2, 3, 4])
    b = GeometricMean([1, 2, 3, 4])
    c = HarmonicMean([1, 2, 3, 4])
    print(a())
    print(b())
    print(c())
