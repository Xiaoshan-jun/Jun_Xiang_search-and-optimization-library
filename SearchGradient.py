# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 01:36:49 2021

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
    #return x[0]**2 + x[1]**2


def SearchGradient(func, mean, sigma, lr, iteration, k):
    xrecord = []
    yrecord = []
    xc = mean.copy()
    for i in range(iteration):
        dmu = np.zeros(len(mean))
        dsigma = np.zeros(len(mean))
        y = np.zeros(k)
        for g in range(k):      
            for j in range(len(mean)):
                xc[j] = np.random.normal(mean[j],sigma[j]**2)
            y[g] = func(xc)
            for j in range(len(mean)):
                dmu[j] += (xc[j] - mean[j])/(sigma[j])**2 * y[g]
                dsigma[j] += ((xc[j] - mean[j])**2 - (sigma[j])**2)/(sigma[j])**3 * y[g]
        
        dmu = dmu/k
        dsigma = dsigma/k
        mean -= lr*dmu
        sigma -= lr*dsigma
        yc = y.mean()
        
        

        xrecord.append(list(mean))
        yrecord.append(yc)
        
    return xrecord, yrecord

lr = 0.01
iteration = 100
colormap = ['b', 'r', 'g', 'c', 'm']
k = 50
mean = np.zeros(2) + 2
sigma = np.zeros(2) + 1
xrecord, vrecord = SearchGradient(func, mean, sigma, lr, iteration, k)
plt.plot(vrecord)
plt.title('value vs iteration')
plt.xlabel('iteration')
plt.ylabel('func(x)')
plt.show()
