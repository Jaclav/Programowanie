#!/bin/python3
# %%
from typing import Union


class Velocity:
    __v = 0

    def __init__(self, v: float = 0):
        assert v <= 1
        self.__v = v

    def get_velocity(self) -> float:
        return self.__v

    def gamma(self) -> float:
        return (1 - self.__v**2) ** -0.5

    def __add__(self, v: "Velocity") -> "Velocity":
        return Velocity(
            (self.__v + v.get_velocity()) / (1 + self.__v * v.get_velocity())
        )

    def __str__(self) -> str:
        return str(self.__v)

    def __iadd__(self, v: Union[float, "Velocity"]) -> "Velocity":
        if type(v) == float:
            self.__v = (self.__v + v) / (1 + self.__v * v)
        elif type(v) == Velocity:
            self.__v = (self.__v + v.get_velocity()) / (1 + self.__v * v.get_velocity())
        return self

    def __repr__(self) -> str:
        return "AAA"


if __name__ == "__main__":
    a, b = input().split(" ")
    a = float(a.strip())
    b = float(b.strip())

    print("beta", Velocity(a) + Velocity(b))
    print("gamma", (Velocity(a) + Velocity(b)).gamma())

    v1 = Velocity(0.4)
    v2 = Velocity(0.4)
    print(v1 + v2)
    v0 = Velocity()
    v0 += 0.1
    print(v0)

    v0 = Velocity()
    v0 += Velocity(0.2)
    print(v0)
