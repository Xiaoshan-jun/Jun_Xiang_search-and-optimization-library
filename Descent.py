# -*- coding: utf-8 -*-
"""
0Created on Sat Nov 20 20:30:33 2021
Descent library
Gradient Descent, Newton Descent
@author: jun xiang
"""
from sympy import diff
from sympy import symbols
from sympy.solvers import solve
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x[0]**2 - x[0]*x[1] + 3*x[1]**2 + 5

#calculate the first derivative of the func
def derivativeCalculator(func, variable):
    derivative = []
    for i in range(len(variable)):
        derivative.append(diff(func(variable), variable[i]))
    return derivative
    
#gradientDescent
#input: function, optimized variable, initial value, learning rate, iteration
def gradientDescent(func, variable, initial, alpha, iteration):
    v = func(initial)
    derivative = derivativeCalculator(func, variable)
    vrecord = [v]
    xrecord = [initial]
    
    for i in range(iteration):
        dx = []

        #calculate dx for every optimized variables
        for d in derivative:
            for i in range(len(variable)):
                d = d.subs(variable[i], initial[i])
            dx.append(d)
        dx = np.asarray(dx)
        #update variable
        initial -= alpha * dx
        initial = list(initial)
        vrecord.append(func(initial)) #record function(variable)
        xrecord.append(initial)#record variables
    return xrecord, vrecord

#Newton Descent
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
plt.title('value vs iteration(NewtonDescent)')
plt.xlabel('iteration')
plt.ylabel('func(x)')
plt.show()

xrecord, vrecord = gradientDescent(func, variable, initial, alpha, iteration)
plt.plot(vrecord)
plt.title('value vs iteration(gradientDescent)')
plt.xlabel('iteration')
plt.ylabel('func(x)')
plt.show()
                
    
    
    
    