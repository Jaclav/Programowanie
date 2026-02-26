#!/usr/bin/python3
# %%
from fib  import *

def fib(n: int):
    start_time = time.time()
    fi = fibi(n)
    ti = time.time() - start_time

    start_time = time.time()
    fr = fibr(n)
    tr = time.time() - start_time

    return (fi, ti, fr, tr)


N = int(sys.argv[1])
n = list(range(0, N + 1))
Y = []
for i in n:
    Y.append(fib(i))

Y=np.array(Y)
# print(Y[:,3])

plt.plot(n,Y[:,1],label="iterative")
plt.plot(n,Y[:,3],label="recursive")
plt.legend()
plt.xlabel("N")
plt.ylabel("T [s]")
plt.plot()
plt.savefig("fibT.png")
plt.show()

plt.plot(n,Y[:,0],label="iterative")
plt.plot(n,Y[:,2],label="recursive")
plt.legend()
plt.xlabel("N")
plt.ylabel("F(n)")
plt.plot()
plt.savefig("fibN.png")
plt.show()