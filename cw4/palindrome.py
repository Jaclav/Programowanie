#!/bin/python3
import sys

def is_palindrome(S):
    S="".join(filter(str.isalpha,S))
    S=S.lower()
    for i,s in enumerate(S[:len(S)//2]):
        # print(i,s,-(i+1))
        if s != S[-(i+1)]:
            return False
    return True

for s in sys.argv[1:]:
    if(is_palindrome(s)):
        print(s)