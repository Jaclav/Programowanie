#!/bin/python3

import sys

i = input()
print(eval(i))

i = i.split(" ")
C = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b,
    "^": lambda a, b: a**b,
}
print(C[i[1]](float(i[0]), float(i[2])))
