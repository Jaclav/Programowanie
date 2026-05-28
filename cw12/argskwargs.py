#!/bin/python3
# %%
def method_1(*args, **kwargs):
    for a in args:
        print(a)

    for k in kwargs.keys():
        print(k, kwargs[k])


method_1(2, 3, 4, j=2, c=8)
# %%


def method_2(a, b, *args, c=None, **kwargs):
    print(a, b, c)
    for ar in args:
        print(ar)

    for k in kwargs.keys():
        print(k, kwargs[k])


method_2(10, "a", 23, "aa", c=16, g=22)
# %%
import matplotlib.pyplot as plt


def plot_with_params(x, y, **params):
    plt.plot(x, y, **params)


# %%
plot_with_params([1, 2, 3], [1, 4, 9], marker="o")
# %%
