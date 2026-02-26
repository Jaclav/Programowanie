#!/usr/bin/python3

def ifactorial(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r