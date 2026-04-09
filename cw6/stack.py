#!/bin/python3
import sys


class Stack:
    __s = []

    def __init__(self):
        pass

    def push(self, v):
        self.__s.append(v)

    def pop(self):
        r = self.__s[-1]
        self.__s.pop(-1)
        return r

    def isEmpty(self) -> bool:
        return len(self.__s) == 0


stack = Stack()
for i in range(1, len(sys.argv)):
    stack.push(i)

while not stack.isEmpty():
    print(stack.pop())
