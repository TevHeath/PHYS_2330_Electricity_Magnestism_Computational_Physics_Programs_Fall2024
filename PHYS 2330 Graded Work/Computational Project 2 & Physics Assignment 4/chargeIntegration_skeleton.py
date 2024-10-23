# Computational Exercise 3 for PHYS*2330 - Fall 2023
# chargeIntegration.py - scaffold code
# MVM
#------------------------------------------------------------------------------


""" Section 1:  Start by importing relevant libraries
#---------------------------------------------------------------------------"""
import numpy as np


""" Section 2:  Define functions for the script
#---------------------------------------------------------------------------"""
# This produces arrays of (x,y) positions for a line 
# segment, from position ri to rf, divided into N equally spaced intervals
def lineSegment(ri,rf,N):
    x = np.linspace(ri[0], rf[0], N)
    y = np.linspace(ri[1], rf[1], N)
    dL = np.sqrt( (x[1] - x[0])**2 + (y[1] - y[0])**2 )
    return x, y, dL

	
# Return the electric field, E, due to a charge "q" located at position (xq,yq).
# Evaluate V at the given position (x,y).
# This can be taken and modified from exercise 1.
def eField(q, xq, yq, x, y):
    k = 9.0e9
    denom = ((x-xq)**2 + (y-yq)**2)**1.5
    dEx = k*q * (x - xq) / denom
    dEy = k*q * (y - yq) / denom
    return dEx, dEy

# Create a function that will integrate, using Trapezoid Rule
# Inputs should be A function f, and a segment length dL (associated with dQ)
def trapz (f, dL):       
	
    return 


""" Section 3:  Main body of code
#---------------------------------------------------------------------------"""
# Define characteristics of the uniformly charged line segment
Ri = np.array([-5,0])
Rf = np.array([5,0])
#Nsegments = 
#Qtot = 
#dL = 

# linear charge density (charge per unit length)
#lamb = 

# position at which electric field is calculated
Ro = np.array([0,5])


# compute dEx, dEy at position Ro due to each segment along the 
# charged line segment.
# NOTE:  the *Ro - assigns Ro values to appropriate variables, in order of how
#        they are defined in function

# Notice that we input 'lamb' instead of dQ here?
dEx, dEy = eField(lamb,X,Y,*Ro)

# Apply trapz function to integrate all contributions dEx, dEy to computer the 
# total electric field at position Ro
Ex = trapz(dEx,dL)
Ey = trapz(dEy,dL)

print(Ex,Ey)

# def simpson(f, a, b, n):  # Define a function 'simpson' that takes in:
#     # f: the function to be integrated
#     # a: the lower limit of integration
#     # b: the upper limit of integration
#     # n: the number of points to sample (should be odd for Simpson's Rule to work correctly)
#
#     h = (b - a) / (n - 1)  # Calculate the step size h between points
#     # This step size is the distance between successive sample points
#     # It is determined by dividing the interval [a, b] into (n-1) equal parts
#
#     xs = a + np.arange(n) * h  # Generate 'n' evenly spaced sample points from 'a' to 'b'
#     # np.arange(n) creates an array of 'n' values: [0, 1, 2, ..., n-1]
#     # Multiply by 'h' and add 'a' to get sample points in the range [a, b]
#
#     cs = 2 * np.ones(n)  # Create an array of coefficients, initialized to 2
#     # This array will hold the Simpson's rule coefficients for each sample point
#
#     cs[1::2] = 4  # Set the coefficients for odd-indexed points to 4 (Simpson's rule alternates)
#     cs[0] = 1     # Set the coefficient for the first point to 1
#     cs[-1] = 1    # Set the coefficient for the last point to 1
#     # Simpson's Rule uses 1 for the first and last points, 4 for odd points, and 2 for even points
#
#     contribs = cs * f(xs)  # Calculate the contribution of each point to the integral
#     # f(xs) applies the function 'f' to each sample point
#     # Multiply each result by the corresponding coefficient in 'cs'
#
#     return (h / 3) * np.sum(contribs)  # Apply Simpson's Rule formula to compute the integral
#     # Multiply the sum of the weighted function values (contribs) by h/3 to get the final result