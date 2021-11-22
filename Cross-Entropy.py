# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 00:56:13 2021

@author: jun xiang
"""
from sympy import diff, solve
from sympy import symbols
import sympy
import matplotlib.pyplot as plt
import numpy as np
import math

def func(x):
    return x[0]**2 - x[0]*x[1] + 3*x[1]**2 + 5


def crossEntropy(func, initial, k, topk, iteration):
    xrecord = [initial]
    vrecord = [func(initial)]
    currentMin = func(initial)
    mean = initial
    cov = np.identity(len(mean))
    for it in range(iteration):
        p = []
        v = []
        for i in range(k):
            p.append(np.random.multivariate_normal(mean, cov))
            v.append(func(p[i]))
        y = np.asarray(v).mean()
        v = list(enumerate(v))
        v.sort(key=lambda x: x[1])
        E = v[0:topk]
        Ex = []
        for i in range(topk):
            Ex.append(p[E[i][0]])
        Ex = np.asmatrix(Ex)
        mean = Ex.mean(axis=0)
        
        sumC = np.zeros((len(initial),len(initial)))
        for i in range(topk):
            sumC = sumC + (Ex[i] - mean).T*(Ex[i] - mean)
        cov = sumC/topk
        mean = tuple(np.asarray(mean)[0])
        
        xrecord.append(mean)
        vrecord.append(y)
    return xrecord, vrecord
        
k = 100
topk = round(0.2*k)
iteration = 100
initial = [2, 2]

xrecord, vrecord = crossEntropy(func, initial, k, topk, iteration)
plt.plot(vrecord)
plt.title('value vs iteration')
plt.xlabel('iteration')
plt.ylabel('func(x)')
plt.show()