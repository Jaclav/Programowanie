#!/bin/python3

import sys

if sys.argv[1] == "-e":
    with open(sys.argv[3], "r") as f:
        with open(sys.argv[4], "w") as w:
            for l in f.readlines():
                for c in l:
                    print(ord(c) ^ int(sys.argv[2]), end=" ")
                    w.write(str(ord(c) ^ int(sys.argv[2])) + " ")

elif sys.argv[1] == "-d":
    with open(sys.argv[3], "r") as f:
        with open(sys.argv[4], "w") as w:
            for l in f.readlines():
                for c in l.split(" "):
                    try:
                        print(chr(int(c) ^ int(sys.argv[2])), end="")
                        w.write(chr(int(c) ^ int(sys.argv[2])) + " ")
                    except ValueError:
                        pass
else:
    print("ERROR!")

print("")
