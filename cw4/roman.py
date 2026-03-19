#!/bin/python3

import sys

if __name__ == "__main__":
    R = ["I", "V", "X", "L", "C", "D", "M", " "]
    S = sys.argv[2]
    if sys.argv[1] == "r":
        i = 0
        S = reversed(S)
        O = []
        for s in S:
            print(s, i)
            if int(s) == 0:
                pass
            elif 1 <= int(s) <= 3:
                O.append(R[i] * int(s))
            elif int(s) == 4:
                O.append(R[i] + R[i + 1])
            elif int(s) < 9:
                O.append(R[i + 1] + R[i] * (int(s) % 5))
            elif int(s) == 9:
                O.append(R[i] + R[i + 2])
            i += 2
        O.reverse()
        print(O[0:])

    if sys.argv[1] == "a":
        i = 0
        R = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "Q": 0,
            "W": 0,
        }
        S = "Q" + sys.argv[2] + "W"
        i = 1
        prev = ""
        sum = 0
        SUMA = 0
        for s in S[1:]:
            # print(s, prev, sum)
            if s != prev:
                # print(sum)
                SUMA += sum
                sum = 0
            if s == "W":
                sum += R[s] - (R[S[i - 1]] if R[S[i - 1]] < R[s] else 0)
                break
            if R[S[i + 1]] <= R[s]:
                sum += R[s] - (R[S[i - 1]] if R[S[i - 1]] < R[s] else 0)
            prev = s
            i += 1

        print(SUMA)
