#!/bin/python3

import sys, regex

with open(sys.argv[1], "r") as f:
    s = 0
    for l in f.readlines():
        r = regex.search("[[:space:]][0-9.]*$", l)
        if r != None:
            # print(l[r.span()[0] : r.span()[1]])
            s += float(l[r.span()[0] : r.span()[1]])
    print(s)
