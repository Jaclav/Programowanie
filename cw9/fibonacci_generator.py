#!/bin/python3
import sys
from typing import Callable


class FibIterator:
    __n: int = 1
    __prev: int = 0

    def __init__(self):
        pass

    def __iter__(self):
        self.__n: int = 1
        self.__prev: int = 0

        return self

    def __next__(self) -> int:
        self.__prev, self.__n = self.__n, self.__prev + self.__n
        return self.__n


def filter_gen(iterator: FibIterator, select: Callable[[int], bool]):
    for x in iterator:
        if select(x):
            yield x


if __name__ == "__main__":
    N = int(sys.argv[1])
    for x in FibIterator():
        if x > N:
            print(x)
            break

    evens = filter_gen(FibIterator(), lambda x: x % 2 == 0)
    print([next(evens) for _ in range(N)])
