#!/usr/bin/python3
#%%
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
import fib


n = int(sys.argv[1])
n = n if n % 2 == 0 else n + 1
print(fib.fibi(n + 1) - 1)
