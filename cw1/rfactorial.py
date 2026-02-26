#!/usr/bin/python3

def rfactorial(n):
    if n <= 1:
        return 1

    return n * rfactorial(n - 1)