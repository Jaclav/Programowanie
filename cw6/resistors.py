#!/bin/python3
# %%

class Resistor:
    __r = 0

    def __init__(self, r: float = 0):
        assert r >= 0
        self.__r = r

    def get_resistance(self) -> float:
        return self.__r

    def set_resistance(self, r: float):
        assert r >= 0
        self.__r = r

    def __add__(self, r: "Resistor") -> "Resistor":
        return Resistor(self.__r + r.get_resistance())

    def __or__(self, r: "Resistor") -> "Resistor":
        assert self.__r != 0 and r.get_resistance() != 0
        return Resistor(1 / (1 / self.get_resistance() + 1 / r.get_resistance()))


def series(a: Resistor, b: Resistor) -> Resistor:
    return Resistor(a.get_resistance() + b.get_resistance())


def parallel(a: Resistor, b: Resistor) -> Resistor:
    assert a.get_resistance() != 0 and a.get_resistance() != 0
    return Resistor(1 / (1 / a.get_resistance() + 1 / b.get_resistance()))


if __name__ == "__main__":
    a, b = input().split(" ")
    a = float(a.strip())
    b = float(b.strip())

    r1 = Resistor(a)
    r2 = Resistor(b)

    print(series(r1, r2).get_resistance(), parallel(r1, r2).get_resistance())
    print((r1 + r2).get_resistance(), (r1 | r2).get_resistance())
