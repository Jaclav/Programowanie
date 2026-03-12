#!/bin/python3

import random as r

if __name__ == "__main__":
    A=set()
    while len(A) < 6:
        x = r.randint(0,49)
        A.add(x)
    print(sorted(A))

