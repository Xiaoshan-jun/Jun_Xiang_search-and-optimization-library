# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 00:32:14 2021
Simulated Annealing
@author: Jun Xiang
"""
from sympy import diff, solve
from sympy import symbols
import sympy
import matplotlib.pyplot as plt
import numpy as np
import math
import random
from numpy.random import rand

def func(x):
    return x[0]**2 - x[0]*x[1] + 3*x[1]**2 + 5

#input: func, initial value, iteration, T
#output: value of variable and function in each iteration.
#
def SimulatedAnnealing(func, initial, iteration, T):
    xrecord = [initial]
    vrecord = [func(initial)]
    currentMin = func(initial)
    for i in range(iteration):
        c = []
        for x in initial:
            c.append(np.random.normal(x,1))
        yc = func(c)
        t = T/float(i + 1)
        diff = yc - currentMin
        if yc < currentMin or rand() < np.exp(-diff/t):
            currentMin = yc
            initial = c
        xrecord.append(initial)
        vrecord.append(currentMin)
    return xrecord, vrecord

initial = np.zeros(50) + 2
T = 10
iteration = 100
xrecord, vrecord = SimulatedAnnealing(func, initial,iteration, T)
plt.plot(vrecord)
plt.title('value vs iteration Simulated Annealing')
plt.xlabel('iteration')
plt.ylabel('func(x)')
plt.show()

