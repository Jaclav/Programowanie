#!/bin/python3

import math


class Rational:
    __p, __q = int(0), int(0)

    def _reduce(self):
        if self.__p < 0 and self.__q < 0:
            self.__p = abs(self.__p)
            self.__q = abs(self.__q)
        elif self.__p < 0 or self.__q < 0:
            self.__p = -abs(self.__p)
            self.__q = abs(self.__q)

        r = math.gcd(self.__p, self.__q)
        self.__p //= r
        self.__q //= r

    def __init__(self, p: int = 0, q: int = 1):
        self.__p, self.__q = p, q
        self._reduce()

    @property
    def numerator(self):
        return self.__p

    @property
    def denominator(self):
        return self.__q

    def __float__(self) -> float:
        return self.__p / self.__q

    def __str__(self) -> str:
        if self.__q == 1:
            return str(self.__p)
        return str(self.__p) + "/" + str(self.__q)

    def __neg__(self) -> "Rational":
        return Rational(-1 * self.__p, self.__q)

    def __add__(self, a: "Rational") -> "Rational":
        return Rational(
            self.__p * a.denominator + self.__q * a.numerator,
            self.__q * a.denominator,
        )

    def __sub__(self, a: "Rational") -> "Rational":
        return Rational(
            self.__p * a.denominator - self.__q * a.numerator,
            self.__q * a.denominator,
        )

    def __mul__(self, a: "Rational") -> "Rational":
        return Rational(self.__p * a.numerator, self.__q * a.denominator)

    def __lt__(self, a: "Rational") -> bool:
        return self.__p * a.denominator < self.__q * a.numerator


if __name__ == "__main__":
    a, b = input().split(" ")
    r1 = Rational(int(a[0 : a.find("/")]), int(a[a.find("/") + 1 :]))
    r2 = Rational(int(b[0 : b.find("/")]), int(b[b.find("/") + 1 :]))
    print(float(r1), float(r2))
    print(-r1, -r2)
    print(min(r1, r2), max(r1, r2))
    print(r1 + r2, r1 * r2)
