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

