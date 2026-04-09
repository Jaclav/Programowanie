#!/bin/python3
import sys
import random as r
import numpy as np

class Person:
    x,y=.0,.0
    MaxDistance=1.0
    MaxIllDistance=0.1
    status="zdrowy"

    def Move(self):
        self.x,self.y=np.array([2,3])*(self.MaxIllDistance if self.status == "chory" else self.MaxDistance)

    def Info(self):
        pass

    def __str__(self):
