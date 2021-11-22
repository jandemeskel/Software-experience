# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 11:43:50 2017

@author: sbm37
"""
import matplotlib.pyplot as plt
import numpy as np

N = 1000

a = 0.0
b = np.pi
h = (b-a)/N

theta = 0
m = 1
w = 450e-9
r = -25.0e-6 # Starts the scan at the negative 25 micrometers x-position

def j(m, r, theta):
    return (np.cos((theta) - ((np.pi*r)/10*w)*np.sin(theta))) # The expression for the mth order Bessel function
    
trap_sum = 0 # Global variable; this keeps track of the sum DURING each iteration of the trapezium rule
trapezium = 0.5*(h)*trap_sum  # The general formula for the trapezium rule

y_axis = [] # Array to store values to the y-dimension
x_axis = [] # Array to store values to the x-dimension

    
while r <= 25.0e-6:                                             # While the second order Bessel function is yet to be computed                                         # While 20 units in the x-direction have yet to be integrated to
    while (theta<=b):                                       # While the upper limit of the integral has not been reached
        if theta == a:                                          # If the current θ value is the first term
            theta = theta + h
            trap_sum = trap_sum + j(m, r, theta)
        elif theta == b:                                  # Else, if the current θ value is the last term
            theta = theta + h
            trap_sum = trap_sum + j(m, r, theta)
        else:                                                   # Else, if the θ value any middle term
            theta = theta + h
            trap_sum = trap_sum + 2*j(m, r, theta)
        trapezium = 0.5*(h)*trap_sum
    x_axis.append(r)
    print(trapezium)
    I = ((2.0*trapezium)/((np.pi)*r)/10*w)**2.0
    y_axis.append(I)
    r = r + 0.05e-6 # Increments the positon along the x-dimension for the next iteration
    theta = 0
    trap_sum = 0

plt.plot(x_axis, y_axis)
plt.xlabel('x', fontsize = 18)
plt.ylabel('I(r)', fontsize = 18)
theta = 0
trap_sum = 0



    