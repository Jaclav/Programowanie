#!/bin/python3

# %%
import json
import matplotlib.pyplot as plt
import numpy as np


def przygotuj_histogram(G: list, D: list):
    out = {}
    G.insert(0, -np.inf)
    G.append(np.inf)
    for i, g in enumerate(G[0:-1]):
        out[str(G[i]) + " - " + str(G[i + 1])] = 0

    for d in D:
        for i, g in enumerate(G[0:-1]):
            if G[i] <= d < G[i + 1]:
                out[list(out.keys())[i]] += 1
                break

    return out


def narysuj_histogram(hist):
    fig, ax = plt.subplots()
    fig.set_size_inches(20,10)
    ax.bar(hist.keys(), hist.values())

    for label in ax.get_xticklabels():
        label.set_rotation(90)


f = open("D-42.json", "r")
j = json.load(f)

h = przygotuj_histogram(j["granice"], j["dane"])
print(h)
narysuj_histogram(h)


# %%
