# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:27:35 2017

@author: sbm37
"""

G = 6.674e-11 # The universal gravitational constant
M = 5.974e24 # Mass of the Earth 
m = 7.348e22 # Mass of the moon
R = 3.844e8 # Radius of the moon's orbit about Earth
w = 2.662e-6 # Angular velocity

def f(r):
    return (G*M/(r)**2) - (G*m/(R-r)**2) - (w**2*r) # Where 'r' is the lagrange point

def Secant_Lagrange():
    print("This program will calculate the position of the Lagrange point between the earth and the moon with respect to the centre of the Earth.")
    print("You must provide two estimate positions. Please input them in SI meters.")
    print("")
    x1 = float(input("""Please input your upper estimate of the Lagrange point. """)) # First user input estimate near point to the Lagrange point 
    x2 = float(input("""Please input your lower estimate of the Lagrange point. """)) # Second user input estimate near point to the Lagrange point 
    
    while abs(x2-x1) > 0: # The program will repeat the function until the difference between the estimate values is negligible
        r = x2 - f(x2)*((x2-x1)/(f(x2)-f(x1))) # This is the secant method, derived as an extension of the Newton-Raphson and central difference methods
        x1 = x2 # The program assigns the previous second estimate as the new first estimate 
        x2 = r # The program assigns the recently calcuated estimate as the new second estimate 
        # The program now repeats the function using the reassigned values.
    print("")
    print("""The distance from Earth to the Lagrange point L1 is {:10.4e} meters""" .format(r))

Secant_Lagrange()
