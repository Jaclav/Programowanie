#!/bin/python3

# %%
import json
import matplotlib.pyplot as plt
import numpy as np

f = open("ludnosc.json", "r")
j = json.load(f)

print(j["2020"].keys())
w = input()

years = []
people = []
surface = []
for y in j.keys():
    years.append(y)
    people.append(j[y][w]["ludność"])
    surface.append(j[y][w]["powierzchnia km2"])


def plot(X, Y, name):
    plt.plot(X, Y)
    plt.xlabel("Rok")
    plt.ylabel(name)
    plt.show()
    plt.clf()


people = np.array(people)
surface = np.array(surface)

plot(years, people / 1e6, "Ludność [mln. os.]")
plot(years, surface / 1e3, "Powierzchnia [tys km kw.]")
plot(years, people / surface, "Gęstość zaludnienia [os / km kw]")

years = []
people = []
surface = []
for y in j.keys():
    a,b,c=0,0,0
    for w in j["2020"].keys():
        a+=j[y][w]["ludność"]
        b+=j[y][w]["powierzchnia km2"]
    years.append(y)
    people.append(a)
    surface.append(b)

people = np.array(people)
surface = np.array(surface)
plot(years, people / 1e6, "PL Ludność [mln. os.]")
plot(years, surface / 1e3, "PL Powierzchnia [tys km kw.]")
plot(years, people / surface, "PL Gęstość zaludnienia [os / km kw]")


f.close()
# %%
