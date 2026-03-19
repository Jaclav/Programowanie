#!/bin/python3

import sys

if __name__ == "__main__":
    if sys.argv[1] == "check":
        S = []
        for i, s in enumerate(sys.argv[2]):
            # print(s,S)
            if s == "(":
                S.append("(")
            if s == "[":
                S.append("[")
            if s == "{":
                S.append("{")

            if s == ")":
                if S[-1] == "(":
                    S.pop()
                else:
                    print("NIE")
                    exit(-1)
            if s == "]":
                if S[-1] == "[":
                    S.pop()
                else:
                    print("NIE")
                    exit(-1)

            if s == "}":
                if S[-1] == "{":
                    S.pop()
                else:
                    print("NIE")
                    exit(-1)
        print("TAK")
    if sys.argv[1] == "fix":
        S = []
        for i, s in enumerate(sys.argv[2]):
            if s == "(":
                S.append("(")
                print(s)
            if s == "[":
                S.append("[")
                print(s)
            if s == "{":
                S.append("{")
                print(s)

            if s == ")":
                if S[-1] == "(":
                    S.pop()
                    print(s)
                else:
                    print("(")
                    print(")")
            if s == "]":
                if S[-1] == "[":
                    S.pop()
                    print(s)
                else:
                    print("[")
                    print("]")

            if s == "}":
                if S[-1] == "{":
                    S.pop()
                    print(s)
                else:
                    print("{")
                    print("}")
        for s in S:
            if s == "(":
                print(")")
            if s == "[":
                print("]")
            if s == "{":
                print("}")
                
    if sys.argv[1] == "list":
        n=int(sys.argv[2])
        ret = []
        def fun(c, countOp, countCl):
            if len(c) == 2 * n:
                ret.append(c)
                return

            if countOp < n:
                fun(c + "(", countOp + 1, countCl)

            if countCl < countOp:
                fun(c + ")", countOp, countCl + 1)

        fun("", 0, 0)
        print(ret)
