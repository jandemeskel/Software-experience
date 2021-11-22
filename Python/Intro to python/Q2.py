# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:54:52 2017

@author: sbm37
"""
import matplotlib.pyplot as plt
import numpy as np

N = 10000 # The number of integration "steps" taken by the trapezium rule

a = 0.0 # Integral lower limit
b = np.pi # Integral upper limit
h = (b-a)/N # Integral "step" size

theta = 0 # Diffraction angle
m = 0 # Bessel function order
x = 0 # x-dimension position

def j(m, x, theta): # The expression for a Bessel function
    return (1/np.pi)*(np.cos(m*(theta) - (x)*np.sin(theta)))
    
trap_sum = 0  # Global variable; this keeps track of the sum DURING each iteration of the trapezium rule
trapezium = 0.5*(h)*trap_sum # The general formula for the trapezium rule

y_axis0 = [] # Array to store values to the y-dimension
x_axis0 = [] # Array to store values to the x-dimension
y_axis1 = [] 
x_axis1 = []
y_axis2 = [] 
x_axis2 = []

while m <= 2:                                             # While the second order Bessel function is yet to be computed
    while x <= 20:                                          # While 20 units in the x-direction have yet to be integrated to
        while (theta<=b):                                       # While the upper limit of the integral has not been reached
            if theta == a:                                          # If the current θ value is the first term
                theta = theta + h
                trap_sum = trap_sum + j(m, x, theta)
            elif theta == b:                                        # Else, if the current θ value is the last term
                theta = theta + h
                trap_sum = trap_sum + j(m, x, theta)
            else:                                                   # Else, if the θ value any middle term
                y = 2*j(m, x, theta)
                theta = theta + h
                trap_sum = trap_sum + 2*j(m, x, theta)
            trapezium = 0.5*(h)*trap_sum                            # Calculate the integral for the current iteration x-value
            
        if (m == 0):                                            # If this x-value belongs to the zero order Bessel function...
            x_axis0.append(x)                                   # ... append the integral to the zero order array
            y_axis0.append(trapezium)
        elif (m == 1):                                          # If this x-value belongs to the first order Bessel function...
            x_axis1.append(x)                                   # ... append the integral to the zero order array
            y_axis1.append(trapezium)
        else:                                                   # If this x-value belongs to the second order Bessel function...
            x_axis2.append(x)                                   # ... append the integral to the zero order array
            y_axis2.append(trapezium)

            
        theta = 0 # Resets the current value of θ to zero in preparation for the next integral
        trap_sum = 0 # Clears the currently stored trapezium rule in preparation for the next integral
        x += 0.2 # Increments the x-position
    print("""The J({}) Bessel function has been computed""" .format(m))

    x = 0 # Rests the x-position to zero in preparation for the next order Bessel function
    m += 1 # Increments the order of Bessel function

print("")
print("Below are the plots of the computed Bessel functions.")
print("")
      
plt.plot(x_axis0, y_axis0, label= 'J_0(x)') # Plots the zero order Bessel function
plt.plot(x_axis1, y_axis1, label= 'J_1(x)') # Plots the first order Bessel function
plt.plot(x_axis2, y_axis2, label= 'J_2(x)') # Plots the second order Bessel function
plt.legend(loc='upper right')
plt.xlabel('x', fontsize = 18)
plt.ylabel('J(x)', fontsize = 18)
plt.ylim(-0.4, 1.0)
