# -*- coding: utf-8 -*-
"""
0Created on Sat Nov 20 20:30:33 2021
Descent library

@author: jun xiang
"""
from sympy import diff
from sympy import symbols
from sympy.solvers import solve
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x[0]**2 - x[0]*x[1] + 3*x[1]**2 + 5

def derivativeCalculator(func, variable):
    derivative = []
    for i in range(len(variable)):
        derivative.append(diff(func(variable), variable[i]))
    return derivative
    

def gradientDescent(func, variable, initial, alpha, iteration):
    v = func(initial)
    derivative = derivativeCalculator(func, variable)
    vrecord = [v]
    xrecord = [initial]
    
    for i in range(iteration):
        dx = []
        
        for d in derivative:
            for i in range(len(variable)):
                d = d.subs(variable[i], initial[i])
            dx.append(d)
        dx = np.asarray(dx)
        initial -= alpha * dx
        initial = list(initial)
        vrecord.append(func(initial))
        xrecord.append(initial)
    return xrecord, vrecord

def NewtonDescent(func, variable, initial, iteration):
    v = func(initial)
    derivative = derivativeCalculator(func, variable)
    vrecord = [v]
    xrecord = [initial]
    a = symbols("a")
    for i in range(iteration):
        dx = []
        for d in derivative:
            for i in range(len(variable)):
                d = d.subs(variable[i], initial[i])
            dx.append(d)
        dx = np.asarray(dx)
        fxp = func(initial - a*dx)
        d = diff(fxp, a)
        alpha = solve(d, a)[0]
        initial -= alpha * dx
        initial = list(initial)
        vrecord.append(func(initial))
        xrecord.append(initial)
    return xrecord, vrecord



initial = [2, 2]
x1,x2 = symbols("x1,x2")
variable = [x1, x2]
alpha = 0.3
iteration = 100
xrecord, vrecord = NewtonDescent(func, variable, initial, iteration)
#xrecord, vrecord = gradientDescent(func, variable, initial, alpha, iteration)
plt.plot(vrecord)
plt.title('value vs iteration')
plt.xlabel('iteration')
plt.ylabel('func(x)')
plt.show()
    
                
    
    
    
    