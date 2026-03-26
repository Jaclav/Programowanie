#!/bin/python3

import sys


def calc(l):
    i = l.split(" ")
    C = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "%": lambda a, b: a % b,
    }
    print(l.strip(), "=", C[i[1]](float(i[0]), float(i[2])))
    return C[i[1]](float(i[0]), float(i[2]))


calc(input())
