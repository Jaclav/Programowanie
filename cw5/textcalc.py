#!/bin/python3

import sys

with open(sys.argv[1], "r") as f:
    with open(sys.argv[2], "w") as w:
        for l in f.readlines():
            i = l.split(" ")
            C = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: a / b,
                "%": lambda a, b: a % b,
                "^": lambda a, b: a**b,
            }
            w.write("%s = %.2f\n" % (l.strip(), C[i[1]](float(i[0]), float(i[2]))))
            print(eval(l))
