#!/bin/python3

from collections import *

if __name__ == "__main__":
    A = input()
    A = A.split(" ")
    
    X=Counter(A).most_common()
    for i in X:
        print(i[0],i[1])
