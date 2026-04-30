#!/bin/python3
from typing import List
from math import factorial
from sys import argv


def HermiteCoefficients(n: int):
    from sympy import hermite, Poly, Symbol

    x = Symbol("x")
    return Poly(hermite(n, x), x).all_coeffs()


def LegendreCoefficients(n: int):
    from sympy import legendre, Poly, Symbol

    x = Symbol("x")
    return Poly(legendre(n, x), x).all_coeffs()


class Polynomial:
    __c: List[float] = [0]

    def __init__(self, c: List[float]):
        self.__c = c
        if c == []:
            self.__c = [0]

    @property
    def deg(self) -> int:
        assert len(self.__c) != 0
        return len(self.__c) - 1

    def __getitem__(self, key: int) -> float:
        return self.__c[key]

    def __setitem__(self, key: int, value: float) -> None:
        self.__c[key] = value

    def __call__(self, x: float):
        s = 0
        for i, c in enumerate(self.__c):
            s += c * x**i
        return s

    def __add__(self, b: "Polynomial") -> "Polynomial":
        tmp: List[float] = []
        for i in range(0, max(self.deg, b.deg)):
            sum = 0
            if i <= self.deg:
                sum += self[i]
            if i <= b.deg:
                sum += b[i]
            tmp.append(sum)
        return Polynomial(tmp)

    def __mul__(self, b: float) -> "Polynomial":
        tmp: List[float] = []
        for c in self.__c:
            tmp.append(c * b)
        return Polynomial(tmp)

    def D(self) -> "Polynomial":
        tmp: List[float] = []
        for i, c in enumerate(self.__c):
            if i != 0:
                tmp.append(c * factorial(i))
        return Polynomial(tmp)


class Hermite(Polynomial):
    def __init__(self, n: int):
        super().__init__(HermiteCoefficients(n))


class Legandre(Polynomial):
    def __init__(self, n: int):
        super().__init__(LegendreCoefficients(n))


if __name__ == "__main__":
    N: int = int(argv[1])
    X: float = float(argv[2])

    H, L = Hermite(N), Legandre(N)
    print(H(X), L(X), 3 * (H.D() + L.D() + (H + L))(X))
