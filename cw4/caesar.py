#!/bin/python3

import sys


def caesar(n, S):
    for s in S:
        print(
            # (ord(s) + n - ord("a")) % (ord("z")-ord("a")+1)+ord("a"),
            chr((ord(s) + n - ord("a")) % (ord("z") - ord("a") + 1) + ord("a")),
            end="",
            sep="",
        )


if __name__ == "__main__":
    if sys.argv[1] == "encrypt":
        caesar(int(sys.argv[2]), sys.argv[3])
    else:
        caesar(-int(sys.argv[2]), sys.argv[3])
    print("")
