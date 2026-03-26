#!/bin/python3

import sys

with open(sys.argv[2], "r") as f:
    with open(sys.argv[3], "w") as w:
        L = f.readlines()
        for l in L:
            l = l.strip()
            if l[0] != sys.argv[1]:
                w.write(l + "\n")
